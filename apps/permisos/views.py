"""
Vista de error para tokens CSRF inválidos (usada por `production.py`).

Devuelve un mensaje entendible en lugar de la página de error genérica de
Django, cuyo texto en inglés es confuso para el usuario final de la
distribuidora. Los formularios de pago y el cierre de sesión son los casos más
frecuentes: caducan por inactividad y el usuario cree que la operación falló.
"""

from django.http import HttpResponseForbidden
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string


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
