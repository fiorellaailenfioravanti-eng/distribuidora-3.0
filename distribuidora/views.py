from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.permisos.roles import requiere


DIAS_SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']


def inicio(request):
    """Portada de la tienda: productos destacados (con stock disponible),
    promociones activas y zonas de reparto con sus días."""
    from apps.logistica.models import Zona
    from apps.productos.models import Producto
    from apps.productos.views import agotados_al_final
    from apps.promociones.models import Promocion

    destacados = agotados_al_final(
        Producto.objects.filter(activo=True, es_envase=False)
    ).filter(disponible__gt=0)[:4]

    promociones = (Promocion.objects.filter(activa=True, producto__activo=True)
                   .select_related('producto')[:3])

    zonas = []
    for zona in Zona.objects.vigentes().exclude(dias_reparto=''):
        dias = zona.get_dias_reparto()
        if dias:
            zonas.append({'nombre': zona.nombre, 'dias': [DIAS_SEMANA[d] for d in dias]})

    return render(request, 'inicio.html', {
        'destacados': destacados,
        'promociones': promociones,
        'zonas': zonas,
    })


@login_required
@requiere('ver_panel')
def resumen_dashboard(request):
    from apps.pedidos.models import Pedido, PagoPedido
    from apps.clientes.models import Cliente
    from apps.productos.models import Producto
    from apps.cuentas.services import resumen_morosidad, clientes_morosos

    total_pedidos = Pedido.objects.count()
    pedidos_pendientes = Pedido.objects.filter(estado='Pendiente').count()
    pagos_pendientes = PagoPedido.objects.filter(estado_pago='Pendiente').count()
    total_clientes = Cliente.objects.count()
    total_productos = Producto.objects.count()

    morosidad = resumen_morosidad()
    cuentas_morosas = clientes_morosos()[:5]
    from apps.promociones.services import promociones_por_vencer
    por_vencer = promociones_por_vencer()
    from apps.pedidos.services import resumen_caja
    caja = resumen_caja(dias=30)

    contexto = {
        'total_pedidos': total_pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pagos_pendientes': pagos_pendientes,
        'total_clientes': total_clientes,
        'total_productos': total_productos,
        'morosidad': morosidad,
        'cuentas_morosas': cuentas_morosas,
        'promociones_por_vencer': por_vencer,
        'caja': caja,
    }
    return render(request, 'dashboard/resumen.html', contexto)
