"""
Servicios de pagos de pedidos.

Reúne la lógica que antes estaba copiada en varias vistas (callback de
MercadoPago, webhook, cambio manual del estado del pago y cobro en calle):

- `pago_en_curso(pedido)`: el `PagoPedido` sobre el que se trabaja.
- `registrar_cobro(...)`: cobro presencial aprobado (usado por logística).
- `resolver_pago_pendiente(...)`: el Vendedor aprueba o rechaza el pago por verificar.
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

from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from .models import CODIGO_CUENTA_CORRIENTE, PagoPedido

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
def registrar_cobro(pedido, monto, metodo_pago=None, referencia=''):
    """Registra un pago presencial **aprobado** (cobro en calle o en mostrador)."""
    metodo_pago = metodo_pago or metodo_pago_efectivo()
    if not pedido.total:
        pedido.total = monto
        pedido.save(update_fields=['total'])
    pago = PagoPedido.objects.create(
        pedido=pedido,
        monto=monto,
        metodo_pago=metodo_pago,
        estado_pago='Aprobado',
        referencia_comprobante=referencia,
    )
    ajustar_pagos_provisorios(pedido)
    return pago


def sincronizar_pago_pendiente(pedido):
    """Deja al pedido con un pago `Pendiente` por lo que se debe, como el del checkout.

    Lo usan los pedidos que no pasan por el checkout (los que arma la empresa al
    planificar el reparto, los automáticos y las ventas en la calle), para que
    en la gestión todos se puedan aprobar o rechazar igual. Si no hay pago
    pendiente y se debe algo, lo crea con el método del pedido; si cambió el
    total, lo ajusta; si ya no se debe nada, lo quita. Sólo maneja ese pago
    provisorio: si ya hay un cobro declarado esperando aprobación (lo cobrado por
    el repartidor, una transferencia, MercadoPago), no agrega otro.
    """
    from .models import PagoPedido

    pendientes = list(pedido.pagos.filter(estado_pago='Pendiente').order_by('-id_pago'))
    provisorios = [p for p in pendientes if p.es_provisorio()]
    saldo = pedido.saldo_pendiente()
    if saldo <= 0 or len(provisorios) < len(pendientes):
        for pago in provisorios:
            pago.delete()
        return
    if provisorios:
        pago = provisorios[0]
        if pago.monto != saldo:
            pago.monto = saldo
            pago.save(update_fields=['monto'])
        return
    PagoPedido.objects.create(pedido=pedido, monto=saldo, metodo_pago=pedido.metodo_pago,
                              estado_pago='Pendiente')


@transaction.atomic
def registrar_cobro_por_verificar(pedido, monto, metodo_pago, referencia=''):
    """Cobro que hizo el repartidor (efectivo, transferencia, QR): queda `Pendiente`
    hasta que el administrador cuente el efectivo o vea la transferencia y lo apruebe.

    Reemplaza al pago provisorio del pedido. No deja cobrar más de lo que falta,
    contando lo ya declarado que espera aprobación.
    """
    from .models import PagoPedido, Pedido

    pedido = Pedido.objects.select_for_update().get(pk=pedido.pk)
    monto = _a_decimal(monto)
    if monto is None or monto <= 0:
        raise ValidationError('El monto debe ser mayor a cero.')
    por_cobrar = pedido.saldo_por_cobrar()
    if monto > por_cobrar:
        raise ValidationError(f'El monto supera lo que falta cobrar del pedido (${por_cobrar}).')
    for pago in pedido.pagos.filter(estado_pago='Pendiente'):
        if pago.es_provisorio():
            pago.delete()
    return PagoPedido.objects.create(pedido=pedido, monto=monto, metodo_pago=metodo_pago,
                                     estado_pago='Pendiente', referencia_comprobante=referencia or 'Cobro declarado')


def ajustar_pagos_provisorios(pedido):
    """Achica los pagos `Pendiente` al saldo que queda; si ya no se debe nada, los quita.

    El checkout crea un pago `Pendiente` por el total. Cuando después se cobra
    en partes, ese pago provisorio quedaba por el total y el pedido saldado
    seguía mostrando «Pendiente $total». No toca los que ya tienen un pago de
    MercadoPago asociado: esos los resuelve el webhook.
    """
    saldo = pedido.saldo_pendiente()
    for pago in pedido.pagos.filter(estado_pago='Pendiente', mercadopago_payment_id=''):
        if saldo <= 0:
            pago.delete()
        elif pago.monto > saldo:
            pago.monto = saldo
            pago.save(update_fields=['monto'])


@transaction.atomic
def resolver_pago_pendiente(pedido, aprobar):
    """Aprueba o rechaza el pago por verificar del pedido (transferencia, QR, efectivo a cobrar).

    Sólo actúa sobre el pago `Pendiente`: nunca modifica un cobro ya aprobado
    (un «Rechazado» anulaba el último cobro en efectivo y un «Aprobado»
    confirmaba pedidos cobrados a medias). Se aprueba como máximo el saldo.
    """
    from .models import Pedido

    pedido = Pedido.objects.select_for_update().get(pk=pedido.pk)
    pago = pedido.pago_por_verificar()
    if pago is None:
        raise ValidationError(
            'El pedido no tiene pagos pendientes de verificación. '
            'Para cobrar, usá «Registrar cobro» en el detalle del pedido.'
        )
    if not aprobar:
        pago.estado_pago = 'Rechazado'
        pago.save(update_fields=['estado_pago'])
        return pago

    saldo = pedido.saldo_pendiente()
    if saldo <= 0:
        raise ValidationError('El pedido ya está saldado: no hay nada para aprobar.')
    pago.monto = min(pago.monto, saldo)
    pago.estado_pago = 'Aprobado'
    pago.save(update_fields=['monto', 'estado_pago'])
    if pedido.esta_pagado() and pedido.estado == 'Pendiente':
        pedido.estado = 'Confirmado'
        pedido.save(update_fields=['estado'])
    return pago


@transaction.atomic
def corregir_pago_resuelto(pedido, nuevo_estado):
    """Corrige el último pago aprobado o rechazado del pedido (error del administrador).

    `nuevo_estado`: 'Pendiente' (vuelve a quedar por verificar) o 'Rechazado'
    (no se recibió el dinero). Un rechazado sólo puede volver a 'Pendiente'.
    Devuelve el pago corregido.
    """
    from .models import Pedido

    if nuevo_estado not in ('Pendiente', 'Rechazado'):
        raise ValidationError('Corrección de pago no válida.')
    pedido = Pedido.objects.select_for_update().get(pk=pedido.pk)
    pago = pedido.pago_corregible()
    if pago is None:
        raise ValidationError('El pedido no tiene un pago aprobado o rechazado para corregir.')
    if pago.estado_pago == nuevo_estado:
        raise ValidationError(f'El pago ya está {nuevo_estado.lower()}.')
    pago.estado_pago = nuevo_estado
    pago.save(update_fields=['estado_pago'])
    return pago


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



# ─────────────────────────────────────────────────────────────
# RF-13 — COBRO MANUAL CON PAGOS PARCIALES
# ─────────────────────────────────────────────────────────────
@transaction.atomic
def registrar_pago_manual(pedido, monto, metodo_pago, referencia=''):
    """Registra un pago (total o parcial) cargado por el personal.

    Con el método «Cuenta corriente» el importe pasa a la cuenta del cliente
    (sólo si tiene fiado) y el pedido queda saldado por ese monto. Cuando los
    pagos cubren el total, un pedido `Pendiente` pasa a `Confirmado`.
    """
    from apps.cuentas.services import obtener_o_crear_cuenta, registrar_cargo

    monto = _a_decimal(monto)
    if monto is None or monto <= 0:
        raise ValidationError('El monto debe ser mayor a cero.')
    saldo = pedido.saldo_pendiente()
    if monto > saldo:
        raise ValidationError(f'El monto supera el saldo pendiente del pedido (${saldo}).')

    if metodo_pago.codigo == CODIGO_CUENTA_CORRIENTE:
        if pedido.cliente is None:
            raise ValidationError('El pedido no tiene cliente: no se puede cargar a cuenta.')
        cargo = registrar_cargo(  # valida RF-05 (fiado)
            obtener_o_crear_cuenta(pedido.cliente), monto,
            descripcion=f'Pedido #{pedido.pk}', pedido=pedido,
        )
        referencia = referencia or f'Cargo en cuenta corriente #{cargo.pk}'

    pago = PagoPedido.objects.create(
        pedido=pedido, monto=monto, metodo_pago=metodo_pago,
        referencia_comprobante=referencia or '', estado_pago='Aprobado',
    )
    ajustar_pagos_provisorios(pedido)
    if pedido.esta_pagado() and pedido.estado == 'Pendiente':
        pedido.estado = 'Confirmado'
        pedido.save(update_fields=['estado'])
    return pago


def resumen_caja(dias=30, hoy=None):
    """Ingresos de los últimos `dias`: por medio de pago y por día (RF-13, 6A.5).

    No cuenta lo que pasó a cuenta corriente (no es dinero cobrado); sí suma
    los pagos que los clientes hicieron sobre su cuenta.
    """
    from apps.cuentas.models import MovimientoCuenta

    hoy = hoy or timezone.localdate()
    desde = hoy - timedelta(days=dias - 1)
    pagos = (PagoPedido.objects
             .filter(estado_pago='Aprobado', fecha__date__gte=desde)
             .exclude(metodo_pago__codigo=CODIGO_CUENTA_CORRIENTE))
    por_metodo = {
        fila['metodo_pago__nombre']: fila['total']
        for fila in pagos.values('metodo_pago__nombre').annotate(total=Sum('monto')).order_by('-total')
    }
    cobros_cuenta = (MovimientoCuenta.objects.filter(tipo='Pago', fecha__date__gte=desde)
                     .aggregate(t=Sum('monto'))['t'] or 0)
    if cobros_cuenta:
        por_metodo['Cobros de cuenta corriente'] = cobros_cuenta

    por_dia = []
    for offset in range(min(dias, 7) - 1, -1, -1):
        dia = hoy - timedelta(days=offset)
        total = pagos.filter(fecha__date=dia).aggregate(t=Sum('monto'))['t'] or 0
        total += MovimientoCuenta.objects.filter(tipo='Pago', fecha__date=dia).aggregate(t=Sum('monto'))['t'] or 0
        por_dia.append({'dia': dia, 'total': total})
    maximo = max((d['total'] for d in por_dia), default=0) or 1
    for d in por_dia:
        d['porcentaje'] = int(d['total'] * 100 / maximo)
    return {'por_metodo': por_metodo, 'por_dia': por_dia, 'total': sum(por_metodo.values()), 'dias': dias}


# ─────────────────────────────────────────────────────────────
# RF-12 — STOCK DISPONIBLE (decisión F-D3)
# ─────────────────────────────────────────────────────────────
ESTADOS_QUE_COMPROMETEN = ('Pendiente', 'Confirmado')


def stock_comprometido(producto, excluir_pedido=None):
    """Unidades vendidas que todavía no salieron en un camión.

    El stock se descuenta al cargar el camión; hasta entonces lo pedido queda
    comprometido y no puede venderse dos veces.
    """
    from .models import DetallePedido
    qs = DetallePedido.objects.filter(producto=producto, pedido__estado__in=ESTADOS_QUE_COMPROMETEN)
    if excluir_pedido is not None:
        qs = qs.exclude(pedido=excluir_pedido)
    return qs.aggregate(t=Sum('cantidad'))['t'] or 0


def stock_disponible(producto, excluir_pedido=None):
    return producto.stock - stock_comprometido(producto, excluir_pedido)


def con_stock_disponible(productos):
    """Anota en cada producto `reservado` (stock temporal de pedidos Pendientes o
    Confirmados que todavía no salieron en un camión) y `disponible`
    (stock en depósito − reservado), que es lo que ve el cliente."""
    from django.db.models import F, IntegerField, OuterRef, Subquery, Value
    from django.db.models.functions import Coalesce
    from .models import DetallePedido
    reservado = (DetallePedido.objects
                 .filter(producto=OuterRef('pk'), pedido__estado__in=ESTADOS_QUE_COMPROMETEN)
                 .values('producto').annotate(total=Sum('cantidad')).values('total'))
    return (productos
            .annotate(reservado=Coalesce(Subquery(reservado, output_field=IntegerField()), Value(0)))
            .annotate(disponible=F('stock') - F('reservado')))


def stock_reservado_por_producto():
    """Productos con unidades reservadas por pedidos que esperan confirmación o entrega."""
    from apps.productos.models import Producto
    return con_stock_disponible(Producto.objects.all()).filter(reservado__gt=0).order_by('nombre')


# ─────────────────────────────────────────────────────────────
# RF-18 — PEDIDO AUTOMÁTICO DE REPOSICIÓN
# ─────────────────────────────────────────────────────────────
@transaction.atomic
def generar_pedidos_automaticos(fecha=None):
    """Crea el pedido de cada suscripción activa cuya fecha llegó.

    Es idempotente: después de generar adelanta `proxima_fecha` un período (o
    varios, si el comando no corrió durante un tiempo), así que volver a
    correrlo el mismo día no duplica. Usa el saldo de promociones prepagas.
    Devuelve la lista de pedidos creados.
    """
    from apps.logistica.services import fecha_estimada_para_direccion
    from apps.promociones.services import consumir_saldo
    from .models import DetallePedido, Pedido, SuscripcionReposicion

    fecha = fecha or timezone.localdate()
    creados = []
    for sus in (SuscripcionReposicion.objects.select_for_update()
                .filter(activa=True, proxima_fecha__lte=fecha)
                .select_related('cliente', 'direccion', 'producto', 'metodo_pago')):
        direccion = sus.direccion or sus.cliente.direcciones.filter(es_principal=True).first()
        if direccion is None or not sus.producto.activo:
            continue
        pedido = Pedido.objects.create(
            cliente=sus.cliente, direccion_entrega=direccion, metodo_pago=sus.metodo_pago,
            estado='Confirmado', origen='AUTOMATICO', total=0,
            fecha_estimada_entrega=fecha_estimada_para_direccion(direccion) or sus.proxima_fecha,
            notas_cliente=f'Reposición automática cada {sus.periodicidad_dias} días.',
        )
        cubiertas = consumir_saldo(sus.cliente, sus.producto, sus.cantidad, pedido, fecha=fecha)
        if cubiertas:
            DetallePedido.objects.create(pedido=pedido, producto=sus.producto, precio_unitario=0,
                                         cantidad=cubiertas, subtotal=0)
        restantes = sus.cantidad - cubiertas
        if restantes:
            DetallePedido.objects.create(pedido=pedido, producto=sus.producto, precio_unitario=sus.producto.precio,
                                         cantidad=restantes, subtotal=sus.producto.precio * restantes)
        pedido.total = sum(d.subtotal for d in pedido.detalles.all())
        pedido.save(update_fields=['total'])
        sincronizar_pago_pendiente(pedido)

        while sus.proxima_fecha <= fecha:
            sus.proxima_fecha += timedelta(days=sus.periodicidad_dias)
        sus.ultimo_pedido = pedido
        sus.save(update_fields=['proxima_fecha', 'ultimo_pedido'])
        creados.append(pedido)
    return creados
