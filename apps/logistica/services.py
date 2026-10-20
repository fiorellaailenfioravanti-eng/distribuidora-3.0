from datetime import timedelta
from decimal import Decimal

from django.db import transaction
from django.db.models import Q, Max
from django.utils import timezone

from apps.clientes.services import sincronizar_bidones_de_parada
from apps.pedidos.services import metodo_pago_efectivo as _metodo_pago_efectivo
from apps.pedidos.services import registrar_cobro  # noqa: F401 (API de logística)

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


# ────────────────────────────────────────────────
# PRODUCTOS DEL REPARTO
#   Por ahora el reparto maneja sólo botellones llenos (`es_botellon`) y
#   envases vacíos (`es_envase`).
# ────────────────────────────────────────────────
def productos_de_reparto():
    """Botellones llenos que se cargan en el camión."""
    from apps.productos.models import Producto
    return Producto.objects.filter(es_botellon=True, activo=True).order_by('nombre')


def envase_de_reparto():
    """Envase vacío de los botellones (el que se presta y se retira)."""
    from apps.productos.models import Producto
    lleno = productos_de_reparto().exclude(envase=None).select_related('envase').first()
    if lleno is not None:
        return lleno.envase
    return Producto.objects.filter(es_envase=True, activo=True).order_by('nombre').first()


def botellon_por_defecto():
    """Botellón que se sugiere para clientes frecuentes y paradas manuales."""
    botellones = list(productos_de_reparto())
    return next((p for p in botellones if '20' in p.nombre), botellones[0] if botellones else None)


def bidones_de_pedido(pedido):
    """Botellones llenos que lleva un pedido."""
    return sum(
        d.cantidad for d in pedido.detalles.select_related('producto').all()
        if d.producto.es_botellon
    )


def botellones_por_producto(pedido):
    """`{producto_id: cantidad}` de los botellones del pedido."""
    cantidades = {}
    if pedido is None:
        return cantidades
    for d in pedido.detalles.select_related('producto'):
        if d.producto.es_botellon:
            cantidades[d.producto_id] = cantidades.get(d.producto_id, 0) + d.cantidad
    return cantidades


def renumerar_paradas(hoja):
    """Deja el orden de las paradas en 1..n respetando el orden actual."""
    for numero, parada in enumerate(hoja.detalles.order_by('orden', 'id_detalle'), start=1):
        if parada.orden != numero:
            DetalleHojaRuta.objects.filter(pk=parada.pk).update(orden=numero)


def _siguiente_orden(hoja):
    return (hoja.detalles.aggregate(m=Max('orden'))['m'] or 0) + 1


def _fijar_botellones(pedido, cantidades):
    """Reemplaza los renglones de botellones del pedido y recalcula el total."""
    from apps.pedidos.models import DetallePedido
    from apps.productos.models import Producto

    pedido.detalles.filter(producto__es_botellon=True).delete()
    for producto_id, cantidad in cantidades.items():
        cantidad = int(cantidad or 0)
        if cantidad <= 0:
            continue
        producto = Producto.objects.get(pk=producto_id)
        DetallePedido.objects.create(
            pedido=pedido, producto=producto, precio_unitario=producto.precio,
            cantidad=cantidad, subtotal=producto.precio * cantidad,
        )
    pedido.total = sum(d.subtotal for d in pedido.detalles.all())
    pedido.save(update_fields=['total'])


def construir_borrador(fecha, zona):
    """Arma los datos de previsualización para generar una hoja de ruta.

    Un frecuente que ya tiene un pedido pendiente en la zona (web, telefónico o
    automático) aparece sólo por su pedido, para no repartirle dos veces.
    """
    pedidos = list(pedidos_candidatos(zona, fecha))
    con_pedido = {p.cliente_id for p in pedidos}
    frecuentes = []
    for cliente in clientes_frecuentes_de_zona(zona):
        if cliente.pk in con_pedido:
            continue
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
        'pedidos': pedidos,
        'ruta_default': ruta_default(zona, fecha),
    }


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
        cantidad = bidones_de_pedido(pedido)
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
            notas_cliente='Cliente frecuente: pedido armado al planificar el reparto.',
        )
        producto = item.get('producto_id') or getattr(botellon_por_defecto(), 'pk', None)
        if producto:
            _fijar_botellones(pedido, {producto: cantidad})
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


def generar_borradores_periodo(desde=None, dias=15, usuario=None):
    """RF-17 (decisión A-D5): borradores de reparto para los próximos `dias`.

    Recorre cada zona y cada día de reparto del período en orden y crea una
    hoja en **Borrador** con los pedidos agendables que todavía no están en
    ninguna hoja. Cada pedido queda en el primer día de reparto que le toca.

    Respeta la decisión D2: no confirma nada ni agrega clientes frecuentes
    (agregarlos crea pedidos, así que se eligen a mano en «Planificar
    reparto»). Es idempotente: si ya hay una hoja para esa fecha y zona, no
    la toca. Devuelve la lista de hojas creadas.
    """
    from .models import Zona

    desde = desde or timezone.localdate()
    creadas = []
    for offset in range(dias):
        fecha = desde + timedelta(days=offset)
        for zona in Zona.objects.order_by('nombre'):
            if not fecha_es_de_reparto(zona, fecha):
                continue
            if HojaRuta.objects.filter(fecha=fecha, zona=zona).exists():
                continue
            pedidos = list(pedidos_candidatos(zona, fecha))
            if not pedidos:
                continue
            seleccion = {'pedidos': [{'pedido_id': p.pk, 'cantidad': None} for p in pedidos]}
            creadas.append(crear_hoja_borrador(
                fecha, zona, usuario, seleccion,
                observaciones=f'Generada automáticamente para el período de {dias} días desde {desde:%d/%m/%Y}.',
            ))
    return creadas


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
    for parada in hoja.detalles.exclude(estado='Cancelado').select_related('pedido').prefetch_related(
            'pedido__detalles__producto'):
        pedido = parada.pedido
        if pedido is None:
            continue
        for detalle in pedido.detalles.all():
            if not detalle.producto.es_botellon:
                continue
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
def registrar_regreso(hoja, cargas=None, vacios_recibidos=None):
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

    # Vacíos: cada parada ya sumó al stock los envases que retiró. Si en el
    # depósito se cuentan más o menos, la diferencia ajusta el stock del envase.
    if vacios_recibidos is not None:
        vacios_recibidos = max(0, int(vacios_recibidos))
        diferencia = vacios_recibidos - envases_retirados_en_hoja(hoja)
        envase = envase_de_reparto()
        if diferencia and envase is not None:
            producto = Producto.objects.select_for_update().get(pk=envase.pk)
            producto.stock += diferencia
            producto.save(update_fields=['stock'])
        hoja.vacios_recibidos = vacios_recibidos

    hoja.estado = 'Cerrada'
    hoja.fecha_regreso = timezone.now()
    hoja.save(update_fields=['estado', 'fecha_regreso', 'vacios_recibidos'])

    return hoja


def envases_retirados_en_hoja(hoja):
    return sum(p.envases_retirados for p in hoja.detalles.all())


def entregados_por_producto(hoja):
    """`{producto_id: cantidad}` de botellones de las paradas entregadas."""
    totales = {}
    for parada in hoja.detalles.filter(estado='Entregado').select_related('pedido'):
        for producto_id, cantidad in botellones_por_producto(parada.pedido).items():
            totales[producto_id] = totales.get(producto_id, 0) + cantidad
    return totales


# ────────────────────────────────────────────────
# PARADAS: ALTA MANUAL Y PEDIDO DE CADA PARADA
# ────────────────────────────────────────────────
@transaction.atomic
def agregar_parada(hoja, cliente, direccion, cantidades):
    """Agrega una parada con su pedido de botellones (orden automático).

    `cantidades` es `{producto_id: cantidad}`; se exige al menos un botellón.
    """
    from apps.pedidos.models import Pedido

    if not any(int(c or 0) > 0 for c in cantidades.values()):
        raise ValueError('Indicá cuántos botellones lleva la parada.')
    pedido = Pedido.objects.create(
        cliente=cliente,
        direccion_entrega=direccion,
        metodo_pago=_metodo_pago_efectivo(),
        estado='En Camino' if hoja.estado == 'Confirmada' else 'Confirmado',
        origen='ADMIN',
        total=0,
        fecha_estimada_entrega=hoja.fecha,
        fecha_entrega=hoja.fecha,
        notas_cliente='Parada agregada a mano en la hoja de ruta.',
    )
    _fijar_botellones(pedido, cantidades)
    renumerar_paradas(hoja)
    return DetalleHojaRuta.objects.create(
        hoja_ruta=hoja,
        orden=_siguiente_orden(hoja),
        pedido=pedido,
        cliente=cliente,
        es_frecuente=cliente.es_frecuente,
        direccion_entrega=direccion,
        cliente_nombre=cliente.nombre_completo(),
        direccion_texto=_texto_direccion(direccion),
        cantidad_bidones=bidones_de_pedido(pedido),
    )


@transaction.atomic
def agregar_pedido_a_hoja(hoja, pedido):
    """Suma a la hoja un pedido ya cargado (web o telefónico) como parada."""
    if pedido.paradas.exists():
        raise ValueError(f'El pedido #{pedido.pk} ya está en una hoja de ruta.')
    renumerar_paradas(hoja)
    parada = DetalleHojaRuta.objects.create(
        hoja_ruta=hoja,
        orden=_siguiente_orden(hoja),
        pedido=pedido,
        cliente=pedido.cliente,
        direccion_entrega=pedido.direccion_entrega,
        cliente_nombre=pedido.cliente.nombre_completo() if pedido.cliente else '',
        direccion_texto=_texto_direccion(pedido.direccion_entrega),
        cantidad_bidones=bidones_de_pedido(pedido),
    )
    pedido.fecha_entrega = hoja.fecha
    pedido.save(update_fields=['fecha_entrega'])
    return parada


@transaction.atomic
def fijar_pedido_de_parada(parada, cantidades):
    """Carga o corrige los botellones que pide el cliente en una parada.

    Sólo mientras la hoja está en Borrador (después ya se cargó el camión).
    Los pedidos hechos por la web no se modifican desde acá.
    """
    from apps.pedidos.models import Pedido

    if parada.hoja_ruta.estado != 'Borrador':
        raise ValueError('La hoja ya salió: el pedido de la parada no se puede cambiar.')
    pedido = parada.pedido
    if pedido is not None and pedido.origen == 'WEB':
        raise ValueError('Es un pedido hecho por la web: se modifica desde la gestión de pedidos.')
    if not any(int(c or 0) > 0 for c in cantidades.values()):
        raise ValueError('La parada tiene que llevar al menos un botellón.')
    if pedido is None:
        if parada.cliente_id is None:
            raise ValueError('La parada no tiene cliente: eliminala y agregala de nuevo.')
        pedido = Pedido.objects.create(
            cliente=parada.cliente, direccion_entrega=parada.direccion_entrega,
            metodo_pago=_metodo_pago_efectivo(), estado='Confirmado', origen='ADMIN', total=0,
            fecha_estimada_entrega=parada.hoja_ruta.fecha, fecha_entrega=parada.hoja_ruta.fecha,
        )
        parada.pedido = pedido
    _fijar_botellones(pedido, cantidades)
    parada.cantidad_bidones = bidones_de_pedido(pedido)
    parada.save(update_fields=['pedido', 'cantidad_bidones'])
    return parada


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

    Es idempotente (H-28): volver a guardar la misma parada sólo aplica la
    **diferencia** contra lo ya registrado en la base, no los totales otra vez.
    El `ModelForm` de la vista ya modificó la instancia en memoria, por eso lo
    previo se lee de la base.
    """
    from apps.productos.models import Producto

    previo = (
        DetalleHojaRuta.objects.select_for_update()
        .filter(pk=parada.pk)
        .values('envases_retirados', 'envases_vendidos')
        .first()
    ) or {'envases_retirados': 0, 'envases_vendidos': 0}

    parada.envases_retirados = max(0, int(envases_retirados or 0))
    parada.envases_vendidos = max(0, int(envases_vendidos or 0))
    if nota:
        parada.nota_entrega = nota

    envase = _producto_envase_para(parada)
    delta = (
        (parada.envases_retirados - previo['envases_retirados'])
        - (parada.envases_vendidos - previo['envases_vendidos'])
    )
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
            from apps.promociones.services import revertir_consumos
            revertir_consumos(pedido)

    # RF-08: historial de envases del cliente (idempotente por parada).
    sincronizar_bidones_de_parada(parada)
    return parada


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

    sincronizar_bidones_de_parada(parada)
    return parada
