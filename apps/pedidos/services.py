"""
Servicios de pagos de pedidos.

Reúne la lógica que antes estaba copiada en varias vistas (callback de
MercadoPago, webhook, cambio manual del estado del pago y cobro en calle):

- `pago_en_curso(pedido)`: el `PagoPedido` sobre el que se trabaja.
- `registrar_cobro(...)`: cobro presencial aprobado (usado por logística).
- `aplicar_pago_mercadopago(...)`: aplica el estado informado por MercadoPago
  **consultado a su API**, nunca el que llega en la URL del navegador.
- `firma_webhook_valida(...)`: valida la cabecera `x-signature` del webhook.

Regla de seguridad (H-18/H-19): un pago sólo pasa a `Aprobado` por el webhook
verificado, por una consulta a la API de MercadoPago o por un Vendedor.
"""
import hashlib
import hmac
import logging
from decimal import Decimal, InvalidOperation

from django.db import transaction

from .models import PagoPedido

logger = logging.getLogger(__name__)


def pago_en_curso(pedido):
    """Último `PagoPedido` del pedido; si no hay ninguno, crea uno `Pendiente`."""
    pago = pedido.pagos.order_by('id_pago').last()
    if pago is None:
        pago = PagoPedido.objects.create(
            pedido=pedido,
            monto=pedido.total,
            metodo_pago=pedido.metodo_pago,
            estado_pago='Pendiente',
        )
    return pago


def metodo_pago_efectivo():
    """Método por defecto para cobros presenciales (efectivo)."""
    from .models import MetodoPago
    return (
        MetodoPago.objects.filter(codigo='EFECTIVO').first()
        or MetodoPago.objects.first()
    )


@transaction.atomic
def registrar_cobro(pedido, monto, metodo_pago=None):
    """Registra un pago presencial **aprobado** (cobro en calle o en mostrador)."""
    metodo_pago = metodo_pago or metodo_pago_efectivo()
    if not pedido.total:
        pedido.total = monto
        pedido.save(update_fields=['total'])
    return PagoPedido.objects.create(
        pedido=pedido,
        monto=monto,
        metodo_pago=metodo_pago,
        estado_pago='Aprobado',
    )


def _a_decimal(valor):
    try:
        return Decimal(str(valor))
    except (InvalidOperation, TypeError, ValueError):
        return None


@transaction.atomic
def aplicar_pago_mercadopago(pedido, payment_id, status, monto_pagado):
    """Aplica al pedido el estado de un pago **ya consultado** a MercadoPago.

    `approved` sólo confirma el pedido si el monto acreditado cubre el monto
    esperado del pago; si no alcanza, el pago queda `Pendiente` para revisión.
    Devuelve el `PagoPedido` actualizado.
    """
    pago = pago_en_curso(pedido)
    pago.mercadopago_payment_id = str(payment_id or '')
    pago.mercadopago_status = status or ''

    if status == 'approved':
        monto = _a_decimal(monto_pagado)
        if monto is not None and monto >= pago.monto:
            pago.estado_pago = 'Aprobado'
            if pedido.estado == 'Pendiente':
                pedido.estado = 'Confirmado'
                pedido.save(update_fields=['estado'])
        else:
            logger.warning(
                'Pago MP %s aprobado por %s, menor al esperado %s (pedido %s).',
                payment_id, monto_pagado, pago.monto, pedido.pk,
            )
            pago.estado_pago = 'Pendiente'
    elif status in ('rejected', 'cancelled'):
        pago.estado_pago = 'Rechazado'

    pago.save()
    return pago


def consultar_pago_mercadopago(sdk, payment_id):
    """Devuelve el `response` de la API de MercadoPago para un pago, o `{}`."""
    try:
        respuesta = sdk.payment().get(payment_id)
    except Exception:  # error de red o del SDK
        logger.exception('No se pudo consultar el pago %s a MercadoPago.', payment_id)
        return {}
    return respuesta.get('response', {}) or {}


def firma_webhook_valida(secreto, x_signature, x_request_id, data_id):
    """Valida la cabecera `x-signature` de un webhook de MercadoPago.

    Formato: `ts=<timestamp>,v1=<hmac>`. El HMAC-SHA256 se calcula con el
    secreto sobre `id:<data.id>;request-id:<x-request-id>;ts:<ts>;`.
    Sin secreto configurado (desarrollo) no se puede validar y devuelve True;
    `production.py` exige el secreto.
    """
    if not secreto:
        return True
    if not x_signature:
        return False

    partes = {}
    for parte in x_signature.split(','):
        clave, _, valor = parte.strip().partition('=')
        partes[clave] = valor
    ts, v1 = partes.get('ts'), partes.get('v1')
    if not ts or not v1:
        return False

    manifiesto = ''
    if data_id:
        manifiesto += f'id:{str(data_id).lower()};'
    if x_request_id:
        manifiesto += f'request-id:{x_request_id};'
    manifiesto += f'ts:{ts};'

    esperado = hmac.new(secreto.encode(), manifiesto.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(esperado, v1)
