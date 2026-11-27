"""Recuperación de contraseña con código temporal por email.

Reglas de seguridad:
- Código de 6 dígitos generado con `secrets` (1 en un millón).
- En la base sólo queda su HMAC con la SECRET_KEY: si se filtra la base, los
  códigos no sirven.
- Vence a los VIGENCIA_MINUTOS y se usa una sola vez.
- MAX_INTENTOS fallidos lo anulan; MAX_POR_HORA códigos por usuario y una
  espera de ESPERA_REENVIO_SEGUNDOS entre envíos (frena la fuerza bruta y el
  abuso del correo).
- Pedir un código nuevo anula los anteriores.
- La pantalla nunca revela si un email tiene cuenta, y el correo se envía en
  segundo plano para que el tiempo de respuesta tampoco lo delate.
- Al cambiar la contraseña se cierran las demás sesiones (Django) y se avisa
  por email.
"""
import hmac
import logging
import secrets
import threading
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.crypto import salted_hmac

from .models import CodigoRecuperacion

VIGENCIA_MINUTOS = 10
MAX_INTENTOS = 5
MAX_POR_HORA = 3
ESPERA_REENVIO_SEGUNDOS = 60
MINUTOS_PARA_CAMBIAR = 10   # tras validar el código, tiempo para elegir la contraseña

log = logging.getLogger('django.contrib.auth')


# ── Código ──────────────────────────────────────────────────────────────

def _hash(usuario_id, codigo):
    return salted_hmac('autenticacion.recuperacion', f'{usuario_id}:{codigo}',
                       algorithm='sha256').hexdigest()


def normalizar_codigo(texto):
    """Deja sólo los dígitos (acepta «123 456» o «123-456»)."""
    return ''.join(c for c in (texto or '') if c.isdigit())


def buscar_usuario(email):
    """Usuario activo con ese email (sin distinguir mayúsculas) o None."""
    usuario = (get_user_model().objects
               .filter(email__iexact=(email or '').strip(), is_active=True).first())
    if usuario and usuario.has_usable_password():
        return usuario
    return None


def puede_pedir_codigo(usuario, ahora=None):
    ahora = ahora or timezone.now()
    recientes = CodigoRecuperacion.objects.filter(usuario=usuario, creado__gte=ahora - timedelta(hours=1))
    if recientes.count() >= MAX_POR_HORA:
        return False
    ultimo = recientes.first()
    return not (ultimo and ultimo.creado > ahora - timedelta(seconds=ESPERA_REENVIO_SEGUNDOS))


def crear_codigo(usuario, ahora=None):
    """Anula los códigos pendientes y crea uno nuevo. Devuelve (registro, código en claro)."""
    ahora = ahora or timezone.now()
    CodigoRecuperacion.objects.filter(creado__lt=ahora - timedelta(days=1)).delete()
    CodigoRecuperacion.objects.filter(usuario=usuario, usado=False).update(usado=True)
    codigo = f'{secrets.randbelow(1_000_000):06d}'
    registro = CodigoRecuperacion.objects.create(
        usuario=usuario, codigo_hash=_hash(usuario.pk, codigo),
        vence=ahora + timedelta(minutes=VIGENCIA_MINUTOS))
    return registro, codigo


def solicitar_codigo(usuario):
    """Crea y envía un código si no se superó el límite. True si se envió."""
    if not puede_pedir_codigo(usuario):
        return False
    _, codigo = crear_codigo(usuario)
    enviar_correo(
        usuario.email, 'Tu código para recuperar la contraseña',
        'autenticacion/correos/codigo',
        {'usuario': usuario, 'codigo': codigo, 'minutos': VIGENCIA_MINUTOS},
    )
    return True


def verificar_codigo(usuario, codigo, ahora=None):
    """Devuelve el registro si el código es correcto y vigente; si no, None
    (y suma un intento fallido al código pendiente)."""
    ahora = ahora or timezone.now()
    registro = (CodigoRecuperacion.objects
                .filter(usuario=usuario, usado=False, verificado_en__isnull=True, vence__gt=ahora)
                .first())
    if registro is None:
        return None
    codigo = normalizar_codigo(codigo)
    if len(codigo) == 6 and hmac.compare_digest(registro.codigo_hash, _hash(usuario.pk, codigo)):
        registro.verificado_en = ahora
        registro.save(update_fields=['verificado_en'])
        return registro
    registro.intentos += 1
    if registro.intentos >= MAX_INTENTOS:
        registro.usado = True
    registro.save(update_fields=['intentos', 'usado'])
    return None


def codigo_verificado(codigo_id, usuario_id, ahora=None):
    """Registro ya validado y todavía apto para cambiar la contraseña, o None."""
    ahora = ahora or timezone.now()
    return (CodigoRecuperacion.objects.select_related('usuario')
            .filter(pk=codigo_id, usuario_id=usuario_id, usado=False,
                    verificado_en__gte=ahora - timedelta(minutes=MINUTOS_PARA_CAMBIAR))
            .first())


def cerrar_recuperacion(registro):
    """Tras cambiar la contraseña: anula todos los códigos y avisa por email."""
    CodigoRecuperacion.objects.filter(usuario=registro.usuario, usado=False).update(usado=True)
    enviar_correo(
        registro.usuario.email, 'Tu contraseña se cambió',
        'autenticacion/correos/contrasena_cambiada',
        {'usuario': registro.usuario, 'fecha': timezone.localtime()},
    )


def enmascarar_email(email):
    """«lucas@gmail.com» → «lu•••@gmail.com» (para mostrar a quién se envió)."""
    usuario, _, dominio = (email or '').partition('@')
    if not dominio:
        return email
    return f'{usuario[:2]}{"•" * 3}@{dominio}'


# ── Envío ───────────────────────────────────────────────────────────────

def enviar_correo(destino, asunto, plantilla, contexto, adjuntos=()):
    """Envía `plantilla`.txt + `plantilla`.html con la cuenta de Configuración
    (o la del servidor). Se renderiza acá y se envía en segundo plano.

    `adjuntos`: tuplas (nombre, contenido, tipo MIME), p. ej. el PDF de un recibo."""
    from apps.configuracion.models import conexion_y_remitente

    contexto = {'asunto': asunto, **contexto}
    texto = render_to_string(f'{plantilla}.txt', contexto)
    html = render_to_string(f'{plantilla}.html', contexto)
    conexion, remitente = conexion_y_remitente()
    mensaje = EmailMultiAlternatives(
        f'{asunto} · Aguadelluvia', texto, remitente or settings.DEFAULT_FROM_EMAIL, [destino],
        connection=conexion or get_connection())
    mensaje.attach_alternative(html, 'text/html')
    for nombre, contenido, tipo in adjuntos:
        mensaje.attach(nombre, contenido, tipo)

    def _enviar():
        try:
            mensaje.send()
        except Exception:
            log.exception('No se pudo enviar el correo «%s»', asunto)

    # En los tests (backend de memoria) se envía en el momento para poder revisarlo.
    if settings.EMAIL_BACKEND.endswith('locmem.EmailBackend'):
        _enviar()
    else:
        threading.Thread(target=_enviar, daemon=True).start()
