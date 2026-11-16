from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from apps.permisos.roles import es_admin
from apps.permisos.views import sin_permiso

from .forms import ConfiguracionCorreoForm
from .models import ConfiguracionCorreo, conexion_y_remitente


@login_required
def configuracion(request):
    """Configuración del sistema (sólo administrador): correo de recuperación de contraseña."""
    if not es_admin(request.user):
        return sin_permiso(request)
    cfg = ConfiguracionCorreo.actual()
    form = ConfiguracionCorreoForm(request.POST or None, instance=cfg)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Configuración guardada.')
        return redirect('apps.configuracion:configuracion')
    return render(request, 'configuracion/configuracion.html', {'form': form, 'cfg': cfg})


@login_required
def probar_correo(request):
    """Envía un correo de prueba con la cuenta configurada: al email del
    administrador o, si no tiene, a la misma cuenta que envía."""
    if not es_admin(request.user):
        return sin_permiso(request)
    if request.method != 'POST':
        return redirect('apps.configuracion:configuracion')
    conexion, remitente = conexion_y_remitente()
    if conexion is None:
        messages.error(request, 'Primero completá la cuenta de correo, activala y guardá.')
    else:
        destino = request.user.email or ConfiguracionCorreo.actual().correo_remitente
        try:
            EmailMessage('Prueba de correo — Aguadelluvia',
                         'Si recibiste este mensaje, la cuenta para recuperar contraseñas funciona.',
                         remitente, [destino], connection=conexion).send()
            messages.success(request, f'Correo de prueba enviado a {destino}.')
        except Exception as error:  # el detalle ayuda a corregir usuario, clave o servidor
            messages.error(request, f'No se pudo enviar: {error}')
    return redirect('apps.configuracion:configuracion')
