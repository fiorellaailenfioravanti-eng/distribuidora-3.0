"""
Servicios de clientes.

RF-08 — Control de envases prestados:
- `registrar_movimiento_bidon(...)`: préstamo, devolución, venta o ajuste manual.
- `sincronizar_bidones_de_parada(parada)`: refleja en el historial lo que el
  repartidor registró en una parada (llenos entregados, vacíos retirados y
  envases vendidos). Reconcilia: borra y recrea los movimientos de esa parada,
  así que volver a guardarla no duplica nada.
- `recalcular_saldo_bidones(cliente)`: `Cliente.bidones_prestados` es una caché
  de la suma del historial (decisión F-D2).
"""
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Sum

from .models import Cliente, MovimientoBidon

# Signo del efecto de cada tipo sobre el saldo de envases prestados.
SIGNO_POR_TIPO = {'Prestamo': 1, 'Devolucion': -1, 'Venta': -1}


def recalcular_saldo_bidones(cliente):
    saldo = cliente.movimientos_bidon.aggregate(total=Sum('cantidad'))['total'] or 0
    Cliente.objects.filter(pk=cliente.pk).update(bidones_prestados=saldo)
    cliente.bidones_prestados = saldo
    return saldo


@transaction.atomic
def registrar_movimiento_bidon(cliente, tipo, cantidad, usuario=None, nota='',
                               pedido=None, parada=None, permitir_negativo=False):
    """Registra un movimiento manual de envases y actualiza el saldo.

    `cantidad` es la cantidad de envases (positiva). En los `Ajuste` el signo
    indica si suma (+) o resta (-). No deja el saldo en negativo salvo que se
    pida explícitamente (registro en campo).
    """
    cantidad = int(cantidad or 0)
    if tipo == 'Ajuste':
        if cantidad == 0:
            raise ValidationError('El ajuste no puede ser cero.')
        efecto = cantidad
    elif tipo in SIGNO_POR_TIPO:
        if cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor a cero.')
        efecto = SIGNO_POR_TIPO[tipo] * cantidad
    else:
        raise ValidationError('Tipo de movimiento inválido.')

    cliente = Cliente.objects.select_for_update().get(pk=cliente.pk)
    saldo_actual = cliente.movimientos_bidon.aggregate(total=Sum('cantidad'))['total'] or 0
    if not permitir_negativo and saldo_actual + efecto < 0:
        raise ValidationError(
            f'El cliente tiene {saldo_actual} envases prestados: no puede devolver o comprar '
            f'{abs(efecto)}. Si el saldo está mal, registrá un ajuste.'
        )

    movimiento = MovimientoBidon.objects.create(
        cliente=cliente, tipo=tipo, cantidad=efecto, registrado_por=usuario,
        nota=nota, pedido=pedido, parada=parada,
    )
    recalcular_saldo_bidones(cliente)
    return movimiento


def _cliente_de_parada(parada):
    if parada.cliente_id:
        return parada.cliente
    if parada.pedido_id and parada.pedido.cliente_id:
        return parada.pedido.cliente
    return None


@transaction.atomic
def sincronizar_bidones_de_parada(parada, usuario=None):
    """Refleja una parada de reparto en el historial de envases del cliente.

    - Entregada: `cantidad_bidones` llenos → Préstamo.
    - Vacíos retirados → Devolución (aunque la entrega se cancele).
    - Envases vendidos → Venta (el cliente se queda con el envase).
    """
    cliente = _cliente_de_parada(parada)
    MovimientoBidon.objects.filter(parada=parada).delete()
    if cliente is None:
        return []

    renglones = []
    if parada.estado == 'Entregado' and parada.cantidad_bidones:
        renglones.append(('Prestamo', parada.cantidad_bidones))
    if parada.envases_retirados:
        renglones.append(('Devolucion', -parada.envases_retirados))
    if parada.envases_vendidos:
        renglones.append(('Venta', -parada.envases_vendidos))

    movimientos = [
        MovimientoBidon.objects.create(
            cliente=cliente, tipo=tipo, cantidad=efecto, parada=parada,
            pedido=parada.pedido, registrado_por=usuario,
            nota=f'Hoja de ruta #{parada.hoja_ruta_id}',
        )
        for tipo, efecto in renglones
    ]
    recalcular_saldo_bidones(cliente)
    return movimientos
