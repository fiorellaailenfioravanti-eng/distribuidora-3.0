from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from apps.permisos.roles import es_admin_o_vendedor


def inicio(request):
    return render(request, 'inicio.html')


@login_required
@user_passes_test(es_admin_o_vendedor, login_url='/')
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

    contexto = {
        'total_pedidos': total_pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pagos_pendientes': pagos_pendientes,
        'total_clientes': total_clientes,
        'total_productos': total_productos,
        'morosidad': morosidad,
        'cuentas_morosas': cuentas_morosas,
        'promociones_por_vencer': por_vencer,
    }
    return render(request, 'dashboard/resumen.html', contexto)
