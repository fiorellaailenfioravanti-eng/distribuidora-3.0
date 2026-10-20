"""
Completa los pedidos de paradas de clientes frecuentes creados antes de que
«Planificar reparto» les cargara productos (quedaban con total $0 y sin
detalle, así que la carga del camión los contaba como 0).

Para cada parada de una hoja en Borrador o Confirmada cuyo pedido es de la
empresa y no tiene productos, agrega `cantidad_bidones` del botellón de 20 L
(o el primer botellón de reparto) y recalcula el total. Las hojas cerradas no
se tocan: son historia.
"""
from django.db import migrations


def completar(apps, schema_editor):
    Producto = apps.get_model('productos', 'Producto')
    DetalleHojaRuta = apps.get_model('logistica', 'DetalleHojaRuta')
    DetallePedido = apps.get_model('pedidos', 'DetallePedido')

    botellones = list(Producto.objects.filter(es_botellon=True, activo=True).order_by('nombre'))
    if not botellones:
        return
    botellon = next((p for p in botellones if '20' in p.nombre), botellones[0])

    paradas = DetalleHojaRuta.objects.filter(
        hoja_ruta__estado__in=['Borrador', 'Confirmada'], pedido__isnull=False,
        pedido__origen='ADMIN', cantidad_bidones__gt=0,
    ).select_related('pedido')
    for parada in paradas:
        pedido = parada.pedido
        if DetallePedido.objects.filter(pedido=pedido).exists():
            continue
        DetallePedido.objects.create(
            pedido=pedido, producto=botellon, precio_unitario=botellon.precio,
            cantidad=parada.cantidad_bidones, subtotal=botellon.precio * parada.cantidad_bidones,
        )
        pedido.total = botellon.precio * parada.cantidad_bidones
        pedido.save(update_fields=['total'])


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0011_renumerar_paradas'),
        ('productos', '0007_marcar_botellones'),
        ('pedidos', '0004_pedido_confirmado_por_empresa_pedido_fecha_entrega_and_more'),
    ]

    operations = [
        migrations.RunPython(completar, migrations.RunPython.noop),
    ]
