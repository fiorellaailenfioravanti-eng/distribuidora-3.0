from datetime import timedelta
from decimal import Decimal

from django.db import transaction
from django.db.models import Q, Max
from django.utils import timezone

from .models import CalendarioExcepcion, HojaRuta, DetalleHojaRuta, CargaHojaRuta


ESTADOS_AGENDABLES = ('Pendiente', 'Confirmado')


# ────────────────────────────────────────────────
# CALENDARIO POR ZONA
# ────────────────────────────────────────────────
def _hay_excepcion(zona, fecha, tipo):
    """True si existe una excepción de ese tipo para la fecha (de la zona o global)."""
    return CalendarioExcepcion.objects.filter(fecha=fecha, tipo=tipo).filter(
        Q(zona=zona) | Q(zona__isnull=True)
    ).exists()


def fecha_es_de_reparto(zona, fecha):
    """True si `fecha` es día de reparto para la zona (weekday + excepciones)."""
    if _hay_excepcion(zona, fecha, 'suspende'):
        return False
    if _hay_excepcion(zona, fecha, 'agrega'):
        return True
    return zona.incluye_dia(fecha.weekday())


def proxima_fecha_de_reparto(zona, desde=None, max_dias=60):
    """Primer día de reparto para la zona a partir de `desde` (inclusive)."""
    desde = desde or timezone.localdate()
    fecha = desde
    for _ in range(max_dias):
        if fecha_es_de_reparto(zona, fecha):
            return fecha
        fecha += timedelta(days=1)
    return None


def ruta_default(zona, fecha):
    """RutaReparto configurada para esa zona y día de la semana (si existe)."""
    from .models import RutaReparto
    return RutaReparto.objects.filter(zona=zona, dia_semana=fecha.weekday()).first()


def fecha_estimada_para_direccion(direccion):
    """Fecha estimada de entrega para una dirección, según la zona de su barrio."""
    barrio = getattr(direccion, 'barrio', None)
    zona = getattr(barrio, 'zona', None) if barrio else None
    if zona is None:
        return None
    return proxima_fecha_de_reparto(zona)


# ────────────────────────────────────────────────
# GENERACIÓN DE BORRADORES DE HOJA DE RUTA (3B)
# ────────────────────────────────────────────────
def direccion_en_zona(cliente, zona):
    """Dirección principal del cliente dentro de la zona indicada."""
    return cliente.direcciones.filter(barrio__zona=zona).order_by('-es_principal').first()


def clientes_frecuentes_de_zona(zona):
    """Clientes marcados como frecuentes con al menos una dirección en la zona."""
    from apps.clientes.models import Cliente
    return (
        Cliente.objects
        .filter(es_frecuente=True, direcciones__barrio__zona=zona)
        .select_related('usuario')
        .distinct()
        .order_by('apellido', 'nombre')
    )


def pedidos_candidatos(zona, fecha=None):
    """Pedidos agendables de la zona que todavía no están en ninguna hoja."""
    from apps.pedidos.models import Pedido
    qs = Pedido.objects.filter(
        estado__in=ESTADOS_AGENDABLES,
        direccion_entrega__barrio__zona=zona,
        paradas__isnull=True,
    )
    if fecha:
        qs = qs.filter(
            Q(fecha_estimada_entrega__isnull=True) | Q(fecha_estimada_entrega__lte=fecha)
        )
    return (
        qs.select_related('cliente', 'direccion_entrega', 'direccion_entrega__barrio')
        .order_by('direccion_entrega__barrio__nombre',
                  'direccion_entrega__calle',
                  'direccion_entrega__altura')
    )


def bidones_de_pedido(pedido):
    """Suma de botellones (productos retornables) de un pedido."""
    return sum(
        d.cantidad for d in pedido.detalles.select_related('producto').all()
        if d.producto.es_retornable or d.producto.es_envase
    )


def construir_borrador(fecha, zona):
    """Arma los datos de previsualización para generar una hoja de ruta."""
    frecuentes = []
    for cliente in clientes_frecuentes_de_zona(zona):
        direccion = direccion_en_zona(cliente, zona)
        if direccion is None:
            continue
        frecuentes.append({
            'cliente': cliente,
            'direccion': direccion,
            'cantidad_sugerida': cliente.cantidad_recurrente_default or 1,
        })

    return {
        'fecha': fecha,
        'zona': zona,
        'frecuentes': frecuentes,
        'pedidos': list(pedidos_candidatos(zona, fecha)),
        'ruta_default': ruta_default(zona, fecha),
    }


def _metodo_pago_efectivo():
    from apps.pedidos.models import MetodoPago
    return (
        MetodoPago.objects.filter(codigo='EFECTIVO').first()
        or MetodoPago.objects.first()
    )


def _texto_direccion(direccion):
    return direccion.direccion_completa() if direccion else ''


@transaction.atomic
def crear_hoja_borrador(fecha, zona, usuario, seleccion, empleado=None, camion=None,
                        observaciones=''):
    """Crea una HojaRuta en estado Borrador con las paradas seleccionadas.

    `seleccion` es un dict con las listas:
      - 'pedidos': [{'pedido_id': int, 'cantidad': int|None}, ...]
      - 'frecuentes': [{'cliente_id': int, 'direccion_id': int|None, 'cantidad': int|None}, ...]
    """
    from apps.clientes.models import Cliente, DireccionEntrega
    from apps.pedidos.models import Pedido

    ruta = ruta_default(zona, fecha)
    if ruta is not None:
        empleado = empleado or ruta.empleado_default
        camion = camion or ruta.camion_default

    hoja = HojaRuta.objects.create(
        fecha=fecha,
        zona=zona,
        ruta_reparto=ruta,
        empleado=empleado,
        camion=camion,
        estado='Borrador',
        generada_automaticamente=True,
        creado_por=usuario,
        observaciones=observaciones,
    )

    orden = 0

    for item in seleccion.get('pedidos', []):
        pedido = Pedido.objects.filter(pk=item.get('pedido_id')).first()
        if pedido is None:
            continue
        orden += 1
        cantidad = item.get('cantidad') or bidones_de_pedido(pedido)
        DetalleHojaRuta.objects.create(
            hoja_ruta=hoja,
            orden=orden,
            pedido=pedido,
            cliente=pedido.cliente,
            direccion_entrega=pedido.direccion_entrega,
            cliente_nombre=pedido.cliente.nombre_completo() if pedido.cliente else '',
            direccion_texto=_texto_direccion(pedido.direccion_entrega),
            cantidad_bidones=cantidad or 0,
        )
        pedido.fecha_entrega = fecha
        pedido.save(update_fields=['fecha_entrega'])

    for item in seleccion.get('frecuentes', []):
        cliente = Cliente.objects.filter(pk=item.get('cliente_id')).first()
        if cliente is None:
            continue
        direccion = (
            DireccionEntrega.objects.filter(pk=item.get('direccion_id')).first()
            or direccion_en_zona(cliente, zona)
        )
        cantidad = item.get('cantidad') or cliente.cantidad_recurrente_default or 1
        pedido = Pedido.objects.create(
            cliente=cliente,
            direccion_entrega=direccion,
            metodo_pago=_metodo_pago_efectivo(),
            estado='Confirmado',
            origen='ADMIN',
            total=0,
            fecha_estimada_entrega=fecha,
            fecha_entrega=fecha,
        )
        orden += 1
        DetalleHojaRuta.objects.create(
            hoja_ruta=hoja,
            orden=orden,
            pedido=pedido,
            cliente=cliente,
            es_frecuente=True,
            direccion_entrega=direccion,
            cliente_nombre=cliente.nombre_completo(),
            direccion_texto=_texto_direccion(direccion),
            cantidad_bidones=cantidad or 0,
        )

    return hoja


# ────────────────────────────────────────────────
# CONFIRMACIÓN, CARGA Y REGRESO DEL CAMIÓN (3C)
# ────────────────────────────────────────────────
def carga_sugerida(hoja):
    """Productos y cantidades a cargar, sugeridos desde las paradas de la hoja.

    Suma los detalles de los pedidos incluidos. Devuelve una lista de dicts
    `{'producto': Producto, 'cantidad': int}`. El administrador puede ajustarla.
    """
    from apps.productos.models import Producto
    totales = {}
    for parada in hoja.detalles.select_related('pedido').prefetch_related(
            'pedido__detalles__producto'):
        pedido = parada.pedido
        if pedido is None:
            continue
        for detalle in pedido.detalles.all():
            totales[detalle.producto_id] = totales.get(detalle.producto_id, 0) + detalle.cantidad

    if not totales:
        return []

    productos = Producto.objects.in_bulk(list(totales.keys()))
    return [
        {'producto': productos[pid], 'cantidad': cant}
        for pid, cant in totales.items() if pid in productos
    ]


@transaction.atomic
def confirmar_hoja(hoja, usuario, cargas=None):
    """Confirma la hoja (salida del camión).

    Descuenta del stock lo cargado y pasa los pedidos de las paradas a
    'En Camino'. `cargas` es una lista de `{'producto_id': int, 'cantidad': int}`.
    """
    from apps.productos.models import Producto

    if hoja.estado != 'Borrador':
        raise ValueError('Solo se puede confirmar una hoja en estado Borrador.')

    for item in cargas or []:
        cantidad = int(item.get('cantidad') or 0)
        if cantidad <= 0:
            continue
        producto = Producto.objects.select_for_update().filter(pk=item.get('producto_id')).first()
        if producto is None:
            continue
        carga, _ = CargaHojaRuta.objects.get_or_create(
            hoja_ruta=hoja, producto=producto,
            defaults={'cantidad_cargada': 0},
        )
        carga.cantidad_cargada = cantidad
        carga.save(update_fields=['cantidad_cargada'])
        producto.stock -= cantidad
        producto.save(update_fields=['stock'])

    ahora = timezone.now()
    hoja.estado = 'Confirmada'
    hoja.confirmada_por = usuario
    hoja.fecha_confirmacion = ahora
    hoja.fecha_salida = ahora
    hoja.save(update_fields=['estado', 'confirmada_por', 'fecha_confirmacion', 'fecha_salida'])

    for parada in hoja.detalles.select_related('pedido'):
        pedido = parada.pedido
        if pedido is not None and pedido.estado in ESTADOS_AGENDABLES:
            pedido.estado = 'En Camino'
            pedido.save(update_fields=['estado'])

    return hoja


@transaction.atomic
def registrar_regreso(hoja, cargas=None):
    """Registra el regreso del camión y devuelve el stock sobrante.

    `cargas` es una lista de `{'carga_id': int, 'cantidad_entregada': int,
    'cantidad_retornada': int}`. Si no se indica `cantidad_retornada`, se toma
    `cargada - entregada`.
    """
    from apps.productos.models import Producto

    if hoja.estado != 'Confirmada':
        raise ValueError('Solo se puede registrar el regreso de una hoja confirmada.')

    for item in cargas or []:
        carga = hoja.cargas.filter(pk=item.get('carga_id')).first()
        if carga is None:
            continue
        entregada = int(item.get('cantidad_entregada') or 0)
        retornada = item.get('cantidad_retornada')
        if retornada is None:
            retornada = carga.cantidad_cargada - entregada
        retornada = int(retornada)
        carga.cantidad_entregada = entregada
        carga.cantidad_retornada = retornada
        carga.save(update_fields=['cantidad_entregada', 'cantidad_retornada'])

    for carga in hoja.cargas.select_related('producto'):
        if carga.cantidad_retornada:
            producto = Producto.objects.select_for_update().get(pk=carga.producto_id)
            producto.stock += carga.cantidad_retornada
            producto.save(update_fields=['stock'])

    hoja.estado = 'Cerrada'
    hoja.fecha_regreso = timezone.now()
    hoja.save(update_fields=['estado', 'fecha_regreso'])

    return hoja


# ────────────────────────────────────────────────
# ENTREGA EN CALLE, ENVASES Y COBRO (3D)
# ────────────────────────────────────────────────
def _producto_envase_para(parada):
    """Producto que representa el envase retirado/vendido en una parada."""
    from apps.productos.models import Producto
    pedido = parada.pedido
    if pedido is not None:
        for detalle in pedido.detalles.select_related('producto__envase'):
            if detalle.producto.envase_id:
                return detalle.producto.envase
            if detalle.producto.es_envase:
                return detalle.producto
    return Producto.objects.filter(es_envase=True).first()


@transaction.atomic
def registrar_entrega(parada, estado, envases_retirados=0, envases_vendidos=0, nota=''):
    """Registra la entrega de una parada: estado, envases y estado del pedido.

    Ajusta el stock del envase: +retirados (vuelven llenos al depósito) y
    -vendidos (envases no devueltos que se le cobran al cliente).
    """
    from apps.productos.models import Producto

    parada.envases_retirados = max(0, int(envases_retirados or 0))
    parada.envases_vendidos = max(0, int(envases_vendidos or 0))
    if nota:
        parada.nota_entrega = nota

    envase = _producto_envase_para(parada)
    delta = parada.envases_retirados - parada.envases_vendidos
    if envase is not None and delta:
        producto = Producto.objects.select_for_update().get(pk=envase.pk)
        producto.stock += delta
        producto.save(update_fields=['stock'])

    parada.marcar_estado(estado)

    pedido = parada.pedido
    if pedido is not None:
        if estado == 'Entregado':
            pedido.estado = 'Entregado'
            pedido.fecha_entrega = timezone.localdate()
            pedido.save(update_fields=['estado', 'fecha_entrega'])
        elif estado == 'Cancelado':
            pedido.estado = 'Cancelado'
            pedido.save(update_fields=['estado'])

    return parada


@transaction.atomic
def registrar_cobro(pedido, monto, metodo_pago=None):
    """Registra un pago aprobado (cobro en calle o posterior)."""
    from apps.pedidos.models import PagoPedido

    metodo_pago = metodo_pago or _metodo_pago_efectivo()
    if not pedido.total:
        pedido.total = monto
        pedido.save(update_fields=['total'])
    return PagoPedido.objects.create(
        pedido=pedido,
        monto=monto,
        metodo_pago=metodo_pago,
        estado_pago='Aprobado',
    )


@transaction.atomic
def crear_venta_calle(hoja, datos):
    """Registra una venta en calle (D8): cliente pasajero, dirección, pedido,
    cobro y la parada dentro de la hoja. Devuelve la parada creada.

    `datos` admite: cliente_id | (nombre, apellido); calle, altura, barrio_id;
    productos = [{'producto_id': int, 'cantidad': int}]; metodo_pago_id;
    marcar_frecuente; nota.
    """
    from apps.clientes.models import Cliente, DireccionEntrega
    from apps.pedidos.models import Pedido, DetallePedido, MetodoPago
    from apps.productos.models import Producto

    cliente = None
    if datos.get('cliente_id'):
        cliente = Cliente.objects.filter(pk=datos['cliente_id']).first()
    if cliente is None:
        cliente = Cliente.objects.create(
            nombre=datos.get('nombre') or 'Cliente',
            apellido=datos.get('apellido') or '',
            tipo_registro='pasajero',
        )

    direccion = None
    if datos.get('calle'):
        direccion = DireccionEntrega.objects.create(
            cliente=cliente,
            calle=datos['calle'],
            altura=datos.get('altura') or 'S/N',
            barrio_id=datos.get('barrio_id') or None,
            es_principal=not cliente.direcciones.exists(),
        )

    if datos.get('marcar_frecuente'):
        cliente.es_frecuente = True
        cliente.cantidad_recurrente_default = cliente.cantidad_recurrente_default or 1
        cliente.save(update_fields=['es_frecuente', 'cantidad_recurrente_default'])

    metodo = None
    if datos.get('metodo_pago_id'):
        metodo = MetodoPago.objects.filter(pk=datos['metodo_pago_id']).first()
    metodo = metodo or _metodo_pago_efectivo()

    total = Decimal('0')
    renglones = []
    for item in datos.get('productos', []):
        producto = Producto.objects.select_for_update().filter(pk=item.get('producto_id')).first()
        cantidad = int(item.get('cantidad') or 0)
        if producto is None or cantidad <= 0:
            continue
        subtotal = producto.precio * cantidad
        total += subtotal
        renglones.append((producto, cantidad, subtotal))

    pedido = Pedido.objects.create(
        cliente=cliente,
        direccion_entrega=direccion,
        metodo_pago=metodo,
        estado='Entregado',
        origen='REPARTIDOR',
        total=total,
        fecha_entrega=timezone.localdate(),
    )
    for producto, cantidad, subtotal in renglones:
        DetallePedido.objects.create(
            pedido=pedido,
            producto=producto,
            precio_unitario=producto.precio,
            cantidad=cantidad,
            subtotal=subtotal,
        )
        producto.stock -= cantidad
        producto.save(update_fields=['stock'])

    orden = (hoja.detalles.aggregate(total=Max('orden'))['total'] or 0) + 1
    parada = DetalleHojaRuta.objects.create(
        hoja_ruta=hoja,
        orden=orden,
        pedido=pedido,
        cliente=cliente,
        direccion_entrega=direccion,
        cliente_nombre=cliente.nombre_completo(),
        direccion_texto=_texto_direccion(direccion),
        cantidad_bidones=bidones_de_pedido(pedido),
        estado='Entregado',
        hora_registro=timezone.now(),
    )

    if total > 0:
        registrar_cobro(pedido, total, metodo)

    return parada
