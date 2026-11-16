"""
Contador de pedidos pendientes para el menú del panel.

`pedidos_pendientes` es una función que el template llama al mostrarlo: la
consulta sólo se hace si el ítem «Pedidos» se dibuja (únicamente para quien
puede verlos) y se hace una sola vez aunque el menú se incluya dos veces
(escritorio y móvil).
"""


def pedidos_pendientes(request):
    user = getattr(request, 'user', None)
    if user is None or not user.is_authenticated:
        return {}

    memoria = {}

    def contar():
        if 'n' not in memoria:
            from .models import Pedido
            memoria['n'] = Pedido.objects.filter(estado='Pendiente').count()
        return memoria['n']

    return {'pedidos_pendientes': contar}
