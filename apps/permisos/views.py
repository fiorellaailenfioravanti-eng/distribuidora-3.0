"""
Respuestas comunes de permisos.

- `sin_permiso(request)`: mensaje + redirección cuando un guard de
  `roles.py` rechaza al usuario (antes copiado en cada app, auditoría R-2).
- `csrf_failure`: vista de error para tokens CSRF inválidos (usada por `production.py`).

Devuelve un mensaje entendible en lugar de la página de error genérica de
Django, cuyo texto en inglés es confuso para el usuario final de la
distribuidora. Los formularios de pago y el cierre de sesión son los casos más
frecuentes: caducan por inactividad y el usuario cree que la operación falló.
"""

from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string


def destino_personal(user):
    """Pantalla de inicio de cada empleado: el repartidor su recorrido, el resto el panel."""
    from .roles import es_admin_o_vendedor, es_repartidor
    if es_repartidor(user) and not es_admin_o_vendedor(user):
        return 'apps.logistica:mi_ruta_hoy'
    return 'dashboard'


def solo_clientes(request):
    """Si el usuario es personal de la empresa, lo devuelve a su panel.

    El personal (vendedores, repartidores, administradores) no compra desde la
    tienda: no usa carrito, checkout, «Mis pedidos» ni «Mi cuenta» de cliente.
    Devuelve una redirección o `None` si es un cliente.
    """
    from .roles import es_personal_interno
    if es_personal_interno(request.user):
        messages.info(request, 'Tu cuenta es del personal de la distribuidora: no hace compras en la tienda.')
        return redirect(destino_personal(request.user))
    return None


def sin_permiso(request, destino='inicio'):
    messages.error(request, 'No tenés permiso para acceder a esta sección.')
    return redirect(destino)


def csrf_failure(request, reason=''):
    mensaje = (
        'La sesión expiró o el formulario no se envió correctamente. '
        'Por favor, volvé a intentarlo.'
    )

    try:
        html = render_to_string(
            'errores/csrf_fallo.html',
            {'mensaje': mensaje},
            request=request,
        )
    except TemplateDoesNotExist:
        html = f'<!doctype html><meta charset="utf-8"><p>{mensaje}</p>'

    return HttpResponseForbidden(html)
