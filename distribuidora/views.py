from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def resumen_dashboard(request):
    from apps.pedidos.models import Pedido, PagoPedido
    from apps.clientes.models import Cliente
    from apps.productos.models import Producto

    total_pedidos = Pedido.objects.count()
    pedidos_pendientes = Pedido.objects.filter(estado='PENDIENTE').count()
    pagos_pendientes = PagoPedido.objects.filter(estado_pago='Pendiente').count()
    total_clientes = Cliente.objects.count()
    total_productos = Producto.objects.count()

    contexto = {
        'total_pedidos': total_pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pagos_pendientes': pagos_pendientes,
        'total_clientes': total_clientes,
        'total_productos': total_productos,
    }
    return render(request, 'dashboard/resumen.html', contexto)