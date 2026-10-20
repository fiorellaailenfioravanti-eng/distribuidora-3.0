"""Utilidades compartidas por las apps del proyecto."""
import unicodedata


def normalizar_texto(texto):
    """Quita tildes, pasa a minúsculas y recorta espacios ("Bidón " → "bidon").

    Base de las búsquedas tolerantes (RF-07) de productos, clientes y
    empleados. Antes había una copia en cada app (auditoría R-1).
    """
    if not texto:
        return ''
    texto = unicodedata.normalize('NFD', str(texto))
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn').lower().strip()


def redirigir_a_origen(request, por_defecto):
    """Vuelve a la página de origen sólo si es de este mismo sitio (H-32).

    `por_defecto` es un nombre de URL o una ruta, como en `redirect()`.
    """
    from django.shortcuts import redirect
    from django.utils.http import url_has_allowed_host_and_scheme

    origen = request.POST.get('next') or request.META.get('HTTP_REFERER')
    if origen and url_has_allowed_host_and_scheme(
        origen, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return redirect(origen)
    return redirect(por_defecto)
