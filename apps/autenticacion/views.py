from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from apps.permisos.roles import es_personal_interno
from apps.permisos.views import destino_personal
from apps.clientes.forms import DireccionRegistroForm
from apps.clientes.services import guardar_telefonos, leer_telefonos
from . import recuperacion
from .forms import (
    CodigoRecuperacionForm, IngresarUsuarioForm, NuevaContrasenaForm, PerfilUsuarioForm,
    RecuperarContrasenaForm, RegistroClienteWebForm,
)


# Páginas de la tienda que sólo usan los clientes.
_SOLO_CLIENTES = ('/carrito', '/pedidos/checkout', '/pedidos/confirmar', '/pedidos/mis-pedidos', '/clientes/mi-perfil')


def _ya_ingresado(request):
    """Un usuario con sesión iniciada no vuelve a ver el login ni el registro."""
    if not request.user.is_authenticated:
        return None
    messages.info(request, f'Ya ingresaste como {request.user.username}.')
    if es_personal_interno(request.user):
        return redirect(destino_personal(request.user))
    return redirect('inicio')


def registrar_usuario(request):
    if (ya := _ya_ingresado(request)) is not None:
        return ya
    if request.method == 'POST':
        form = RegistroClienteWebForm(request.POST, request.FILES)
        form_dir = DireccionRegistroForm(request.POST, prefix='dir')
        telefonos, errores_telefonos = leer_telefonos(request.POST)
        if form.is_valid() and form_dir.is_valid() and not errores_telefonos:
            with transaction.atomic():
                usuario = form.save()
                guardar_telefonos(usuario.perfil_cliente, telefonos)
                # La señal de clientes ya creó su perfil: le sumamos el domicilio principal.
                direccion = form_dir.save(commit=False)
                direccion.cliente = usuario.perfil_cliente
                direccion.es_principal = True
                direccion.save()
            messages.success(request, 'Tu cuenta se creó. Ya podés ingresar.')
            return redirect('apps.autenticacion:ingresar')
        messages.error(request, 'No se pudo crear la cuenta: revisá los campos marcados.')
    else:
        form = RegistroClienteWebForm()
        form_dir = DireccionRegistroForm(prefix='dir')
        telefonos, errores_telefonos = None, []
    return render(request, 'autenticacion/registrar.html', {
        'form': form, 'form_dir': form_dir,
        'telefonos': telefonos, 'errores_telefonos': errores_telefonos,
    })

def ingresar_usuario(request):
    if (ya := _ya_ingresado(request)) is not None:
        return ya
    next_url = request.GET.get('next')
    if request.method == 'GET' and next_url and 'carrito' in next_url:
        messages.info(request, "Ingresá para ver tu carrito.")
    if request.method == 'POST':
        form = IngresarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Ingreso exitoso.')
                destino = request.POST.get('next') or next_url
                if destino and es_personal_interno(user) and destino.startswith(_SOLO_CLIENTES):
                    destino = None  # el personal no compra: va a su panel
                if destino and url_has_allowed_host_and_scheme(
                    destino, allowed_hosts={request.get_host()}, require_https=request.is_secure()
                ):
                    return redirect(destino)
                if es_personal_interno(user):
                    return redirect(destino_personal(user))
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos. Probá de nuevo.')
    else:
        form = IngresarUsuarioForm()
    return render(request, 'autenticacion/ingresar.html', {'form': form})

def cerrar_sesion(request):
    if request.method != 'POST':
        # Cerrar sesión por GET permitiría desloguear con un simple enlace (H-31).
        return redirect('inicio')
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('apps.autenticacion:ingresar')

@login_required
def perfil_usuario(request):
    """Perfil del personal: editar sus datos y cambiar la contraseña.

    Los clientes tienen su propia pantalla (`clientes:mi_perfil`).
    """
    if not es_personal_interno(request.user):
        return redirect('apps.clientes:mi_perfil')

    usuario = request.user
    form_datos = PerfilUsuarioForm(instance=usuario)
    form_password = PasswordChangeForm(usuario)

    if request.method == 'POST' and 'form_password' in request.POST:
        form_password = PasswordChangeForm(usuario, request.POST)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, form_password.user)  # no cerrar la sesión
            messages.success(request, 'Tu contraseña se cambió correctamente.')
            return redirect('apps.autenticacion:perfil')
        messages.error(request, 'No se pudo cambiar la contraseña: revisá los campos marcados.')

    elif request.method == 'POST':
        form_datos = PerfilUsuarioForm(request.POST, instance=usuario)
        if form_datos.is_valid():
            with transaction.atomic():
                usuario = form_datos.save()
                empleado = getattr(usuario, 'perfil_empleado', None)
                if empleado is not None:
                    # La ficha de empleado muestra los mismos datos: se mantienen iguales.
                    empleado.nombre = usuario.first_name
                    empleado.apellido = usuario.last_name
                    empleado.email = usuario.email
                    empleado.celular = usuario.celular1 or ''
                    empleado.save(update_fields=['nombre', 'apellido', 'email', 'celular'])
            messages.success(request, 'Tus datos se actualizaron.')
            return redirect('apps.autenticacion:perfil')
        messages.error(request, 'No se guardaron los cambios: revisá los campos marcados.')

    for campo in form_password.fields.values():
        campo.widget.attrs['class'] = 'form-control'
    return render(request, 'autenticacion/perfil.html', {
        'form_datos': form_datos,
        'form_password': form_password,
    })



# ── Recuperar contraseña con código temporal (ver recuperacion.py) ──────────

SESION_EMAIL = 'recuperar_email'
SESION_VERIFICADO = 'recuperar_verificado'


def recuperar_contrasena(request):
    """Paso 1: email. Siempre sigue al paso 2, exista o no la cuenta."""
    form = RecuperarContrasenaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        usuario = recuperacion.buscar_usuario(email)
        if usuario:
            recuperacion.solicitar_codigo(usuario)
        request.session[SESION_EMAIL] = email
        request.session.pop(SESION_VERIFICADO, None)
        return redirect('apps.autenticacion:recuperar_codigo')
    return render(request, 'autenticacion/recuperar_contrasena.html', {'form': form})


def recuperar_codigo(request):
    """Paso 2: el código de 6 dígitos que llegó por email."""
    email = request.session.get(SESION_EMAIL)
    if not email:
        return redirect('apps.autenticacion:recuperar')
    form = CodigoRecuperacionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        usuario = recuperacion.buscar_usuario(email)
        registro = usuario and recuperacion.verificar_codigo(usuario, form.cleaned_data['codigo'])
        if registro:
            request.session.cycle_key()  # sesión nueva: evita fijación de sesión
            request.session[SESION_VERIFICADO] = {'codigo': registro.pk, 'usuario': usuario.pk}
            return redirect('apps.autenticacion:recuperar_nueva')
        form.add_error('codigo', 'El código es incorrecto o venció. Revisalo o pedí uno nuevo.')
    return render(request, 'autenticacion/recuperar_codigo.html', {
        'form': form,
        'email': recuperacion.enmascarar_email(email),
        'minutos': recuperacion.VIGENCIA_MINUTOS,
    })


def recuperar_reenviar(request):
    """Pide otro código (respeta la espera y el límite por hora)."""
    email = request.session.get(SESION_EMAIL)
    if request.method != 'POST' or not email:
        return redirect('apps.autenticacion:recuperar')
    usuario = recuperacion.buscar_usuario(email)
    if usuario and not recuperacion.solicitar_codigo(usuario):
        messages.warning(request, 'Esperá un momento antes de pedir otro código.')
    else:
        messages.info(request, 'Si el email corresponde a una cuenta, te enviamos un código nuevo.')
    return redirect('apps.autenticacion:recuperar_codigo')


def recuperar_nueva(request):
    """Paso 3: la contraseña nueva (sólo con un código recién validado)."""
    datos = request.session.get(SESION_VERIFICADO) or {}
    registro = recuperacion.codigo_verificado(datos.get('codigo'), datos.get('usuario'))
    if registro is None:
        request.session.pop(SESION_VERIFICADO, None)
        messages.error(request, 'Se venció el tiempo para cambiar la contraseña. Pedí un código nuevo.')
        return redirect('apps.autenticacion:recuperar')
    form = NuevaContrasenaForm(registro.usuario, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        recuperacion.cerrar_recuperacion(registro)
        request.session.pop(SESION_VERIFICADO, None)
        request.session.pop(SESION_EMAIL, None)
        return redirect('apps.autenticacion:recuperar_listo')
    return render(request, 'autenticacion/recuperar_nueva.html', {'form': form})


def recuperar_listo(request):
    return render(request, 'autenticacion/recuperar_listo.html')
