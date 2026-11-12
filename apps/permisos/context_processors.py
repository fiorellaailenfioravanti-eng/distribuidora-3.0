"""
Permisos del usuario disponibles en todos los templates.

- `puede`: conjunto con los códigos de las funciones del usuario
  (`{% if 'registrar_clientes' in puede %}`). El superusuario las tiene todas.
- `es_vendedor` (entra al panel), `es_repartidor` (hace recorridos) y
  `es_personal_interno` se mantienen para los menús.
"""
from .funciones import CODIGOS
from .roles import es_personal_interno, puede


def roles_usuario(request):
    user = getattr(request, 'user', None)
    if user is None or not user.is_authenticated:
        return {'puede': frozenset(), 'es_vendedor': False, 'es_repartidor': False, 'es_personal_interno': False}
    funciones = frozenset(c for c in CODIGOS if puede(user, c))
    return {
        'puede': funciones,
        'es_vendedor': 'ver_panel' in funciones,
        'es_repartidor': 'realizar_entregas' in funciones and 'ver_panel' not in funciones,
        'es_personal_interno': es_personal_interno(user),
    }
