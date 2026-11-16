"""
Configuración del sistema que el administrador cambia desde el panel.

`ConfiguracionCorreo` es una única fila (pk=1): la cuenta de correo que envía
los emails de «Olvidé mi contraseña». Si está desactivada o incompleta, se usa
la configuración del servidor (.env / settings).
"""
from django.db import models

from distribuidora.limites import LARGO_NOMBRE, limite_largo


class ConfiguracionCorreo(models.Model):
    activo = models.BooleanField(
        default=False, verbose_name='Usar esta cuenta para enviar correos',
        help_text='Si está apagado, se usa la configuración del servidor.')
    nombre_remitente = models.CharField(
        max_length=LARGO_NOMBRE, default='Aguadelluvia', verbose_name='Nombre del remitente',
        help_text='Lo que ve el cliente en «De:».')
    correo_remitente = models.EmailField(
        max_length=120, blank=True, verbose_name='Correo que envía',
        help_text='Ej: aguadelluvia@gmail.com')
    servidor = models.CharField(
        max_length=100, default='smtp.gmail.com', verbose_name='Servidor SMTP',
        help_text='Gmail: smtp.gmail.com · Outlook/Hotmail: smtp.office365.com')
    puerto = models.PositiveIntegerField(default=587, verbose_name='Puerto')
    usar_tls = models.BooleanField(default=True, verbose_name='Conexión segura (TLS)')
    usuario = models.CharField(
        max_length=120, blank=True, verbose_name='Usuario',
        help_text='Normalmente es el mismo correo. Si lo dejás vacío, se usa el correo.')
    clave = models.CharField(max_length=128, blank=True, verbose_name='Contraseña de aplicación')
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Configuración de correo'
        verbose_name_plural = 'Configuración de correo'
        constraints = limite_largo(nombre_remitente=LARGO_NOMBRE, correo_remitente=120,
                                   servidor=100, usuario=120, clave=128)

    def __str__(self):
        return f'Correo de envío: {self.correo_remitente or "sin configurar"}'

    @classmethod
    def actual(cls):
        objeto, _ = cls.objects.get_or_create(pk=1)
        return objeto

    def lista(self):
        """True si está activa y completa para enviar."""
        return bool(self.activo and self.correo_remitente and self.servidor and self.clave)

    def remitente(self):
        if self.nombre_remitente:
            return f'{self.nombre_remitente} <{self.correo_remitente}>'
        return self.correo_remitente


def conexion_y_remitente():
    """(conexión SMTP, remitente) según la configuración del panel; (None, None) si no aplica."""
    from django.core.mail import get_connection
    cfg = ConfiguracionCorreo.objects.filter(pk=1).first()
    if cfg is None or not cfg.lista():
        return None, None
    conexion = get_connection(
        'django.core.mail.backends.smtp.EmailBackend',
        host=cfg.servidor, port=cfg.puerto, username=cfg.usuario or cfg.correo_remitente,
        password=cfg.clave, use_tls=cfg.usar_tls, timeout=20,
    )
    return conexion, cfg.remitente()
