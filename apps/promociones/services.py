"""
Servicios de promociones prepagas (RF-09 / RF-10).

- `vender_promocion`: registra la compra del pack y su pago (o cargo a cuenta).
- `saldo_vigente` / `compras_vigentes`: unidades disponibles de un producto.
- `consumir_saldo`: usa el saldo en un pedido (primero lo que vence antes).
- `revertir_consumos`: al cancelar un pedido devuelve las unidades, salvo que
  el pack ya haya vencido (decisión F-D5: lo vencido no se reintegra).
- `vencer_promociones`: caducidad estricta a los 30 días corridos (RF-10).
"""
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from .models import CompraPromocion, ConsumoPromocion


def compras_vigentes(cliente, producto=None, fecha=None):
    """Packs con saldo y sin vencer, ordenados por fecha de caducidad (FIFO).

    No depende de que haya corrido `vencer_promociones`: filtra por fecha.
    """
    fecha = fecha or timezone.localdate()
    qs = CompraPromocion.objects.filter(
        cliente=cliente, estado='Vigente', unid_restantes__gt=0, fecha_caducidad__gte=fecha,
    ).select_related('promocion__producto')
    if producto is not None:
        qs = qs.filter(promocion__producto=producto)
    return qs.order_by('fecha_caducidad', 'id_compra')


def saldo_vigente(cliente, producto, fecha=None):
    return compras_vigentes(cliente, producto, fecha).aggregate(t=Sum('unid_restantes'))['t'] or 0


@transaction.atomic
def vender_promocion(cliente, promocion, metodo_pago=None, a_cuenta=False, fecha=None):
    """Registra la compra de un pack prepago.

    Crea el `Pedido` que documenta el pago (no genera entrega: las entregas son
    los pedidos posteriores que consumen el saldo), cobra en el momento o lo
    carga a la cuenta corriente si el cliente tiene fiado, y abre el saldo.
    """
    from apps.cuentas.services import obtener_o_crear_cuenta, registrar_cargo
    from apps.pedidos.models import Pedido
    from apps.pedidos.services import metodo_pago_efectivo, registrar_cobro

    if not promocion.activa:
        raise ValidationError('La promoción no está activa.')
    fecha = fecha or timezone.localdate()
    metodo_pago = metodo_pago or metodo_pago_efectivo()

    pedido = Pedido.objects.create(
        cliente=cliente,
        metodo_pago=metodo_pago,
        total=promocion.precio,
        estado='Entregado',
        origen='ADMIN',
        fecha_entrega=fecha,
        notas_cliente=f'Compra de promoción prepaga: {promocion.nombre}',
    )
    if a_cuenta:
        registrar_cargo(  # valida RF-05: sólo clientes con fiado
            obtener_o_crear_cuenta(cliente), promocion.precio,
            descripcion=f'Promoción {promocion.nombre}', pedido=pedido,
        )
    else:
        registrar_cobro(pedido, promocion.precio, metodo_pago)

    return CompraPromocion.objects.create(
        cliente=cliente,
        promocion=promocion,
        pedido=pedido,
        fecha_compra=fecha,
        fecha_caducidad=fecha + timedelta(days=promocion.dias_validez),
        unid_totales=promocion.cant_lleva,
        unid_restantes=promocion.cant_lleva,
    )


@transaction.atomic
def consumir_saldo(cliente, producto, cantidad, pedido, fecha=None):
    """Usa hasta `cantidad` unidades del saldo prepago en `pedido`.

    Devuelve cuántas unidades quedaron cubiertas por la promoción.
    """
    pendiente = int(cantidad or 0)
    cubiertas = 0
    if cliente is None or pendiente <= 0:
        return 0
    for compra in compras_vigentes(cliente, producto, fecha).select_for_update():
        if pendiente <= 0:
            break
        usar = min(pendiente, compra.unid_restantes)
        ConsumoPromocion.objects.create(compra=compra, pedido=pedido, cantidad=usar)
        compra.unid_restantes -= usar
        if compra.unid_restantes == 0:
            compra.estado = 'Agotada'
        compra.save(update_fields=['unid_restantes', 'estado'])
        pendiente -= usar
        cubiertas += usar
    return cubiertas


@transaction.atomic
def revertir_consumos(pedido, fecha=None):
    """Devuelve al saldo las unidades que usó un pedido cancelado.

    Si el pack ya venció, las unidades no se reintegran (F-D5). Devuelve la
    cantidad reintegrada.
    """
    fecha = fecha or timezone.localdate()
    reintegradas = 0
    for consumo in pedido.consumos_promocion.select_related('compra').select_for_update():
        compra = consumo.compra
        if fecha <= compra.fecha_caducidad and compra.estado != 'Vencida':
            compra.unid_restantes += consumo.cantidad
            compra.estado = 'Vigente'
            compra.save(update_fields=['unid_restantes', 'estado'])
            reintegradas += consumo.cantidad
        consumo.delete()
    return reintegradas


@transaction.atomic
def vencer_promociones(fecha=None):
    """RF-10: los packs cuya caducidad ya pasó quedan en 0 y `Vencida`."""
    fecha = fecha or timezone.localdate()
    return CompraPromocion.objects.filter(
        estado='Vigente', fecha_caducidad__lt=fecha,
    ).update(estado='Vencida', unid_restantes=0)


def promociones_por_vencer(dias=5, fecha=None):
    """Packs con saldo que vencen dentro de `dias` días (alerta del dashboard)."""
    fecha = fecha or timezone.localdate()
    return CompraPromocion.objects.filter(
        estado='Vigente', unid_restantes__gt=0,
        fecha_caducidad__gte=fecha, fecha_caducidad__lte=fecha + timedelta(days=dias),
    ).select_related('cliente', 'promocion').order_by('fecha_caducidad')
