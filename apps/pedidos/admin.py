from django.contrib import admin
from .models import MetodoPago, Pedido, DetallePedido, PagoPedido


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0
    readonly_fields = ('precio_unitario', 'subtotal')


class PagoPedidoInline(admin.TabularInline):
    model = PagoPedido
    extra = 0
    readonly_fields = ('fecha',)


@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'activo')
    list_filter = ('activo',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'cliente', 'fecha_pedido', 'estado', 'metodo_pago', 'total')
    list_filter = ('estado', 'metodo_pago', 'fecha_pedido')
    search_fields = ('id_pedido', 'cliente__nombre', 'cliente__apellido', 'cliente__usuario__username')
    inlines = [DetallePedidoInline, PagoPedidoInline]


@admin.register(PagoPedido)
class PagoPedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'pedido', 'monto', 'metodo_pago', 'estado_pago', 'fecha')
    list_filter = ('estado_pago', 'metodo_pago')
