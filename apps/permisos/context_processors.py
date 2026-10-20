"""
Roles del usuario disponibles en todos los templates (auditoría R-5).

Reemplaza al filtro `has_group`: los templates usan las mismas reglas que las
vistas (`roles.py`), incluido que el superusuario cuenta como Vendedor.
"""
from .roles import es_personal_interno, es_repartidor, es_vendedor


def roles_usuario(request):
    user = getattr(request, 'user', None)
    if user is None or not user.is_authenticated:
        return {'es_vendedor': False, 'es_repartidor': False, 'es_personal_interno': False}
    return {
        'es_vendedor': es_vendedor(user),
        'es_repartidor': es_repartidor(user),
        'es_personal_interno': es_personal_interno(user),
    }
