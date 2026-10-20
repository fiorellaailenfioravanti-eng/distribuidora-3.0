from datetime import timedelta
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone

from .models import (
    CuentaCorriente,
    MovimientoCuenta,
    DIAS_NARANJA,
    DIAS_ROJO,
)


DIAS_VENCIMIENTO_DEFAULT = 10

_ORDEN_NIVEL = {'amarillo': 0, 'naranja': 1, 'rojo': 2}


def obtener_o_crear_cuenta(cliente):
    """Devuelve (y crea si hace falta) la cuenta corriente de un cliente."""
    cuenta, _ = CuentaCorriente.objects.get_or_create(cliente=cliente)
    return cuenta


@transaction.atomic
def registrar_cargo(cuenta, monto, descripcion='', pedido=None, abono=None,
                    fecha_vencimiento=None):
    """Registra una deuda en la cuenta.

    RF-05: lanza ValidationError si el cliente no tiene fiado habilitado.
    """
    monto = Decimal(str(monto or 0))
    if monto <= 0:
        raise ValidationError('El monto del cargo debe ser mayor a cero.')
    if not cuenta.cliente.permite_fiado:
        raise ValidationError(
            'El cliente no tiene fiado habilitado (RF-05). '
            'Cambialo a Premium o activá "permite fiado".'
        )

    if fecha_vencimiento is None:
        fecha_vencimiento = timezone.localdate() + timedelta(days=DIAS_VENCIMIENTO_DEFAULT)

    movimiento = MovimientoCuenta(
        cuenta=cuenta,
        tipo='Cargo',
        monto=monto,
        descripcion=descripcion,
        fecha_vencimiento=fecha_vencimiento,
        pedido=pedido,
        abono=abono,
    )
    movimiento.full_clean(exclude=['fecha'])
    movimiento.save()
    return movimiento


@transaction.atomic
def registrar_pago(cuenta, monto, descripcion=''):
    """Registra un pago/abono que reduce el saldo deudor."""
    monto = Decimal(str(monto or 0))
    if monto <= 0:
        raise ValidationError('El monto del pago debe ser mayor a cero.')

    movimiento = MovimientoCuenta(
        cuenta=cuenta,
        tipo='Pago',
        monto=monto,
        descripcion=descripcion,
    )
    movimiento.full_clean(exclude=['fecha'])
    movimiento.save()
    return movimiento


def clientes_morosos(minimo='amarillo'):
    """Cuentas con deuda, ordenadas por antigüedad del cargo más viejo.

    `minimo` filtra desde un nivel del semáforo en adelante
    ('amarillo' | 'naranja' | 'rojo').
    """
    orden_minimo = _ORDEN_NIVEL.get(minimo, 0)
    cuentas = []
    for cuenta in CuentaCorriente.objects.select_related('cliente').filter(activa=True):
        nivel = cuenta.nivel_morosidad()
        if nivel == 'al-dia':
            continue
        if _ORDEN_NIVEL[nivel] >= orden_minimo:
            cuentas.append(cuenta)
    cuentas.sort(key=lambda c: c.dias_de_atraso(), reverse=True)
    return cuentas


def resumen_morosidad():
    """Conteo de cuentas por nivel del semáforo, para el panel."""
    resumen = {'amarillo': 0, 'naranja': 0, 'rojo': 0, 'total_deuda': Decimal('0.00')}
    for cuenta in CuentaCorriente.objects.filter(activa=True):
        nivel = cuenta.nivel_morosidad()
        if nivel == 'al-dia':
            continue
        resumen[nivel] += 1
        resumen['total_deuda'] += cuenta.saldo
    return resumen
