from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

from .models import HojaRuta, DetalleHojaRuta, Zona, Barrio, Camion, RutaReparto
from django.urls import reverse

from .forms  import HojaRutaForm, AgregarParadaForm, ActualizarEstadoForm, ZonaForm, CamionForm
from .services import (
    construir_borrador, crear_hoja_borrador,
    carga_sugerida, confirmar_hoja, registrar_regreso,
    registrar_entrega, registrar_cobro, crear_venta_calle,
    agregar_parada as agregar_parada_servicio, agregar_pedido_a_hoja, botellon_por_defecto,
    botellones_por_producto, clientes_frecuentes_de_zona, direccion_en_zona, entregados_por_producto,
    envase_de_reparto, envases_retirados_en_hoja, fijar_pedido_de_parada, pedidos_candidatos,
    productos_de_reparto, renumerar_paradas,
    confirmar_entrega_en_calle, resumen_recorrido, MOTIVOS_NO_ENTREGA, inventario_camion,
)
from apps.clientes.models import DireccionEntrega
from apps.permisos.roles import (
    es_repartidor_asignado,
    es_admin_o_vendedor,
    es_repartidor,
    es_admin_vendedor_o_repartidor,
    obtener_empleado,
    puede_ver_nota_seguridad,
)


def _ids_de_paradas_con_nota(user, detalles):
    """IDs de parada cuya nota de seguridad (RNF-02) puede ver `user`.

    La nota vive en `DireccionEntrega.desc_seguridad` y la decisión se toma por
    parada, no por hoja: el repartidor solo ve la nota de los domicilios que
    tiene asignados. Los templates no pueden confiar en el template tag porque
    el filtro se evalúa por dirección.
    """
    return [
        detalle.id_detalle
        for detalle in detalles
        if detalle.direccion_entrega_id
        and puede_ver_nota_seguridad(user, detalle.direccion_entrega)
    ]


# ─────────────────────────────────────────────────────────────
# HOJAS DE RUTA — LISTADO
# ─────────────────────────────────────────────────────────────
@login_required
def listar_rutas(request):
    if not es_admin_vendedor_o_repartidor(request.user):
        messages.error(request, 'No tenés permiso para acceder a esta sección.')
        return redirect('inicio')

    # Si es repartidor, solo ve sus propias rutas
    if es_repartidor(request.user) and not es_admin_o_vendedor(request.user):
        empleado = obtener_empleado(request.user)
        if empleado is None:
            rutas = HojaRuta.objects.none()
        else:
            rutas = HojaRuta.objects.filter(empleado=empleado)
    else:
        rutas = HojaRuta.objects.all()

    # Filtros opcionales
    filtro_zona   = request.GET.get('zona', '')
    filtro_estado = request.GET.get('estado', '')
    filtro_fecha  = request.GET.get('fecha', '')

    if filtro_zona:
        rutas = rutas.filter(zona__id_zona=filtro_zona)
    if filtro_estado:
        rutas = rutas.filter(estado=filtro_estado)
    if filtro_fecha:
        rutas = rutas.filter(fecha=filtro_fecha)

    rutas = rutas.select_related('empleado__usuario', 'camion', 'zona', 'ruta_reparto')

    contexto = {
        'rutas':         rutas,
        'zonas':         Zona.objects.all(),
        'filtro_zona':   filtro_zona,
        'filtro_estado': filtro_estado,
        'filtro_fecha':  filtro_fecha,
        'ESTADOS_RUTA':  HojaRuta._meta.get_field('estado').choices,
    }
    return render(request, 'logistica/listar_rutas.html', contexto)


# ─────────────────────────────────────────────────────────────
# HOJAS DE RUTA — CREAR
# ─────────────────────────────────────────────────────────────
@login_required
def crear_ruta(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'Solo administradores y vendedores pueden crear rutas.')
        return redirect('apps.logistica:listar_rutas')

    if request.method == 'POST':
        form = HojaRutaForm(request.POST)
        if form.is_valid():
            ruta = form.save(commit=False)
            ruta.creado_por = request.user
            ruta.save()
            messages.success(request, f'Hoja de ruta #{ruta.id_ruta} creada correctamente.')
            return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)
    else:
        form = HojaRutaForm(initial={'fecha': timezone.localdate()})

    return render(request, 'logistica/crear_ruta.html', {'form': form})


# ─────────────────────────────────────────────────────────────
# HOJAS DE RUTA — VER DETALLE
# ─────────────────────────────────────────────────────────────
@login_required
def ver_ruta(request, pk):
    if not es_admin_vendedor_o_repartidor(request.user):
        messages.error(request, 'No tenés permiso para ver esta ruta.')
        return redirect('inicio')

    ruta = get_object_or_404(
        HojaRuta.objects.select_related('ruta_reparto__zona', 'zona', 'camion', 'empleado'), id_ruta=pk)

    # Repartidor solo puede ver sus propias rutas
    if es_repartidor(request.user) and not es_admin_o_vendedor(request.user):
        empleado = obtener_empleado(request.user)
        if empleado is None or ruta.empleado_id != empleado.id_empleado:
            messages.error(request, 'No tenés permiso para ver esta ruta.')
            return redirect('apps.logistica:mi_ruta_hoy')

    es_admin = es_admin_o_vendedor(request.user)
    detalles = list(ruta.detalles.select_related(
        'pedido', 'cliente', 'direccion_entrega__barrio').prefetch_related('pedido__detalles__producto').order_by('orden', 'id_detalle'))
    productos = list(productos_de_reparto())

    # Cada parada se despliega en una subfila con su pedido y el registro de la entrega.
    filas = []
    for d in detalles:
        cantidades = botellones_por_producto(d.pedido)
        filas.append({
            'parada': d,
            'botellones': [{'producto': p, 'cantidad': cantidades.get(p.pk, 0)} for p in productos],
            'otros_items': [x for x in (d.pedido.detalles.all() if d.pedido_id else []) if not x.producto.es_botellon],
            'editable': es_admin and ruta.estado == 'Borrador' and not d.es_pedido_web(),
        })

    zona = ruta.zona or (ruta.ruta_reparto.zona if ruta.ruta_reparto_id else None)
    pedidos_pendientes, frecuentes_sugeridos = [], []
    if zona is not None and es_admin and ruta.estado != 'Cerrada':
        pedidos_pendientes = list(pedidos_candidatos(zona, ruta.fecha))
        en_hoja = {d.cliente_id for d in detalles if d.cliente_id}
        for cliente in clientes_frecuentes_de_zona(zona):
            direccion = direccion_en_zona(cliente, zona)
            if direccion is not None and cliente.pk not in en_hoja:
                frecuentes_sugeridos.append({'cliente': cliente, 'direccion': direccion,
                                             'cantidad': cliente.cantidad_recurrente_default or 1})

    contexto = {
        'ruta':        ruta,
        'filas':       filas,
        'detalles':    detalles,
        'productos_reparto': productos,
        'form_parada': AgregarParadaForm(hoja=ruta),
        'form_estado': ActualizarEstadoForm(),
        'pedidos_pendientes': pedidos_pendientes,
        'frecuentes_sugeridos': frecuentes_sugeridos,
        'botellon_defecto': botellon_por_defecto(),
        'es_admin':    es_admin,
        'paradas_con_nota_visible': _ids_de_paradas_con_nota(request.user, detalles),
        'parada_abierta': request.GET.get('parada'),
    }
    return render(request, 'logistica/ver_ruta.html', contexto)


# ─────────────────────────────────────────────────────────────
# HOJAS DE RUTA — IMPRIMIR
# ─────────────────────────────────────────────────────────────
@login_required
def imprimir_ruta(request, pk):
    if not es_admin_vendedor_o_repartidor(request.user):
        messages.error(request, 'No tenés permiso para imprimir esta ruta.')
        return redirect('inicio')

    ruta = get_object_or_404(HojaRuta.objects.select_related('ruta_reparto__zona', 'empleado__usuario', 'camion'), id_ruta=pk)

    # Repartidor solo puede imprimir sus propias rutas
    if es_repartidor(request.user) and not es_admin_o_vendedor(request.user):
        empleado = obtener_empleado(request.user)
        if empleado is None or ruta.empleado_id != empleado.id_empleado:
            return redirect('apps.logistica:mi_ruta_hoy')

    detalles = ruta.detalles.all()

    contexto = {
        'ruta': ruta,
        'detalles': detalles,
        'paradas_con_nota_visible': _ids_de_paradas_con_nota(request.user, detalles),
    }
    return render(request, 'logistica/imprimir_ruta.html', contexto)


# ─────────────────────────────────────────────────────────────
# HOJAS DE RUTA — EDITAR
# ─────────────────────────────────────────────────────────────
@login_required
def editar_ruta(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para editar rutas.')
        return redirect('apps.logistica:listar_rutas')

    ruta = get_object_or_404(HojaRuta, id_ruta=pk)

    if request.method == 'POST':
        form = HojaRutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta actualizada correctamente.')
            return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)
    else:
        form = HojaRutaForm(instance=ruta)

    return render(request, 'logistica/editar_ruta.html', {'form': form, 'ruta': ruta})


# ─────────────────────────────────────────────────────────────
# PARADAS — AGREGAR
# ─────────────────────────────────────────────────────────────
def _volver_a_hoja(hoja_pk, parada_pk=None):
    url = reverse('apps.logistica:ver_ruta', kwargs={'pk': hoja_pk})
    return redirect(f'{url}?parada={parada_pk}#parada-{parada_pk}' if parada_pk else url)


@login_required
def agregar_parada(request, pk):
    """Alta manual de parada: cliente existente o nuevo (nombre y dirección obligatorios)."""
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para agregar paradas.')
        return redirect('apps.logistica:listar_rutas')

    ruta = get_object_or_404(HojaRuta, id_ruta=pk)
    if request.method != 'POST':
        return _volver_a_hoja(pk)
    if ruta.estado == 'Cerrada':
        messages.error(request, 'La hoja ya está cerrada.')
        return _volver_a_hoja(pk)

    form = AgregarParadaForm(request.POST, hoja=ruta)
    if not form.is_valid():
        errores = '; '.join(e for lista in form.errors.values() for e in lista)
        messages.error(request, f'No se agregó la parada: {errores}')
        return _volver_a_hoja(pk)

    from apps.clientes.models import Cliente, DireccionEntrega
    datos = form.cleaned_data
    direccion = datos['direccion']
    if direccion is not None:
        cliente = direccion.cliente
    else:
        cliente = Cliente.objects.create(nombre=datos['nombre'].strip(), apellido=(datos['apellido'] or '').strip(),
                                         tipo_registro='pasajero')
        direccion = DireccionEntrega.objects.create(
            cliente=cliente, calle=datos['calle'].strip(), altura=datos['altura'].strip(),
            barrio=datos['barrio'], es_principal=True)
    try:
        parada = agregar_parada_servicio(ruta, cliente, direccion, {datos['producto'].pk: datos['cantidad']})
    except ValueError as error:
        messages.error(request, str(error))
        return _volver_a_hoja(pk)
    messages.success(request, f'Parada {parada.orden} agregada: {cliente.nombre_completo()} '
                              f'({datos["cantidad"]} × {datos["producto"].nombre}).')
    if ruta.estado == 'Confirmada':
        messages.warning(request, 'La hoja ya salió: esos botellones no estaban en la carga del camión.')
    return _volver_a_hoja(pk, parada.pk)


@login_required
def agregar_pedido_parada(request, pk):
    """Suma a la hoja un pedido pendiente de la zona (web o telefónico)."""
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para modificar la hoja.')
        return redirect('apps.logistica:listar_rutas')
    ruta = get_object_or_404(HojaRuta, id_ruta=pk)
    if request.method == 'POST':
        from apps.pedidos.models import Pedido
        pedido = get_object_or_404(Pedido, pk=request.POST.get('pedido_id'))
        try:
            parada = agregar_pedido_a_hoja(ruta, pedido)
            messages.success(request, f'Pedido #{pedido.pk} agregado como parada {parada.orden}.')
            return _volver_a_hoja(pk, parada.pk)
        except ValueError as error:
            messages.error(request, str(error))
    return _volver_a_hoja(pk)


@login_required
def pedido_parada(request, pk):
    """Carga o corrige los botellones que pide el cliente en una parada (subfila)."""
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para modificar pedidos.')
        return redirect('apps.logistica:listar_rutas')
    parada = get_object_or_404(DetalleHojaRuta.objects.select_related('hoja_ruta', 'pedido'), id_detalle=pk)
    if request.method == 'POST':
        cantidades = {}
        for clave, valor in request.POST.items():
            if clave.startswith('botellon_') and clave[len('botellon_'):].isdigit():
                cantidades[int(clave[len('botellon_'):])] = _int_o_none(valor) or 0
        try:
            fijar_pedido_de_parada(parada, cantidades)
            messages.success(request, f'Pedido de {parada.cliente_nombre} actualizado: {parada.resumen_pedido()}.')
        except ValueError as error:
            messages.error(request, str(error))
    return _volver_a_hoja(parada.hoja_ruta_id, parada.pk)


# ─────────────────────────────────────────────────────────────
# PARADAS — ELIMINAR
# ─────────────────────────────────────────────────────────────
@login_required
def eliminar_parada(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para eliminar paradas.')
        return redirect('apps.logistica:listar_rutas')

    parada = get_object_or_404(DetalleHojaRuta, id_detalle=pk)
    ruta_pk = parada.hoja_ruta.id_ruta

    if request.method == 'POST':
        hoja = parada.hoja_ruta
        pedido = parada.pedido
        parada.delete()
        # Un pedido armado sólo para esta parada (no web) se cancela con ella.
        if pedido is not None and pedido.origen != 'WEB' and pedido.estado in ('Pendiente', 'Confirmado'):
            pedido.cambiar_estado_manual('Cancelado')
        renumerar_paradas(hoja)
        messages.success(request, 'Parada eliminada.')

    return redirect('apps.logistica:ver_ruta', pk=ruta_pk)


# ─────────────────────────────────────────────────────────────
# PARADAS — ACTUALIZAR ESTADO (repartidor en campo)
# ─────────────────────────────────────────────────────────────
@login_required
def actualizar_estado_entrega(request, pk):
    if not es_admin_vendedor_o_repartidor(request.user):
        messages.error(request, 'No tenés permiso para actualizar esta entrega.')
        return redirect('inicio')

    parada = get_object_or_404(DetalleHojaRuta, id_detalle=pk)

    es_admin = es_admin_o_vendedor(request.user)
    empleado = obtener_empleado(request.user)
    es_asignado = empleado is not None and parada.hoja_ruta.empleado_id == empleado.id_empleado

    if not (es_admin or es_asignado):
        messages.error(request, 'No tenés permiso para actualizar esta entrega.')
        return redirect('apps.logistica:mi_ruta_hoy')

    if request.method == 'POST':
        ya_entregada = parada.estado == 'Entregado'
        form = ActualizarEstadoForm(request.POST, instance=parada)
        if form.is_valid():
            nuevo_estado = form.cleaned_data['estado']
            registrar_entrega(
                parada,
                nuevo_estado,
                envases_retirados=form.cleaned_data.get('envases_retirados') or 0,
                envases_vendidos=form.cleaned_data.get('envases_vendidos') or 0,
                nota=form.cleaned_data.get('nota_entrega') or '',
            )
            monto = form.cleaned_data.get('monto_cobrado')
            if monto and parada.pedido is not None and nuevo_estado == 'Entregado':
                if ya_entregada:
                    # H-28: corregir una parada no vuelve a cobrar.
                    messages.warning(
                        request,
                        'La parada ya estaba entregada: el cobro no se volvió a registrar. '
                        'Si hace falta corregirlo, hacelo desde el pedido.'
                    )
                else:
                    registrar_cobro(parada.pedido, monto, form.cleaned_data.get('metodo_pago'))
            messages.success(request, f'Estado actualizado a "{nuevo_estado}" correctamente.')
            if es_admin:
                return _volver_a_hoja(parada.hoja_ruta_id, parada.pk)
            return redirect('apps.logistica:mi_ruta_hoy')
    else:
        form = ActualizarEstadoForm(instance=parada)

    return render(request, 'logistica/actualizar_estado.html', {'form': form, 'parada': parada})


# ─────────────────────────────────────────────────────────────
# MI RUTA HOY — Vista para repartidor
# ─────────────────────────────────────────────────────────────
def _link_mapa(direccion, texto):
    """Link a Google Maps: por coordenadas si las hay, si no por la dirección."""
    from urllib.parse import quote
    destino = (direccion.coordenadas if direccion is not None and direccion.coordenadas
               else f'{texto}, Resistencia, Chaco')
    return f'https://www.google.com/maps/dir/?api=1&destination={quote(destino)}'


def _ficha_de_parada(parada, user):
    """Lo que el repartidor necesita ver de cada parada en la calle."""
    cliente = parada.cliente or (parada.pedido.cliente if parada.pedido_id else None)
    telefono = cliente.telefonos.order_by('-es_principal').first() if cliente else None
    pedido = parada.pedido
    return {
        'parada': parada,
        'cliente': cliente,
        'telefono': telefono,
        'mapa': _link_mapa(parada.direccion_entrega, parada.direccion_texto),
        'items': list(pedido.detalles.select_related('producto')) if pedido else [],
        'saldo': pedido.saldo_pendiente() if pedido else 0,
        'pagado': pedido.esta_pagado() if pedido else False,
        'puede_fiar': bool(cliente and cliente.permite_fiado),
        'nota_seguridad': (parada.direccion_entrega.desc_seguridad
                           if parada.direccion_entrega_id and puede_ver_nota_seguridad(user, parada.direccion_entrega)
                           else ''),
    }


@login_required
def mi_ruta_hoy(request):
    """Recorrido del día del repartidor: confirma cada entrega a medida que avanza."""
    if not (es_repartidor(request.user) or es_admin_o_vendedor(request.user)):
        messages.error(request, 'No tenés permiso para acceder a esta sección.')
        return redirect('inicio')

    hoy = timezone.localdate()
    es_admin = es_admin_o_vendedor(request.user)
    empleado = obtener_empleado(request.user)

    # Las de hoy y cualquier hoja en reparto (el camión ya salió aunque sea de otra fecha).
    from django.db.models import Q
    visibles = HojaRuta.objects.exclude(estado='Cerrada').select_related('zona', 'camion', 'empleado')
    if not es_admin:
        visibles = visibles.filter(empleado=empleado) if empleado else HojaRuta.objects.none()
    hojas_hoy = list(visibles.filter(Q(fecha=hoy) | Q(estado='Confirmada')).order_by('-estado', 'fecha', 'id_ruta'))

    pedida = _int_o_none(request.GET.get('hoja'))
    ruta = next((h for h in hojas_hoy if h.pk == pedida), None)
    if ruta is None and pedida:  # vista previa de un recorrido próximo
        ruta = visibles.filter(pk=pedida).first()
    if ruta is None:
        ruta = next((h for h in hojas_hoy if h.estado == 'Confirmada'), hojas_hoy[0] if hojas_hoy else None)

    pendientes, hechas, extras, resumen, camion = [], [], [], None, None
    if ruta is not None:
        for parada in ruta.detalles.select_related(
                'pedido__cliente', 'cliente', 'direccion_entrega').order_by('orden', 'id_detalle'):
            ficha = _ficha_de_parada(parada, request.user)
            if parada.es_venta_calle:
                extras.append(ficha)  # ventas en la calle: no son paradas del recorrido
            else:
                (pendientes if parada.estado == 'Pendiente' else hechas).append(ficha)
        resumen = resumen_recorrido(ruta)
        camion = inventario_camion(ruta)

    proximas = []
    if empleado is not None:
        proximas = [h for h in HojaRuta.objects.filter(empleado=empleado, fecha__gt=hoy)
                    .exclude(estado='Cerrada').select_related('zona').order_by('fecha')[:6] if h not in hojas_hoy][:5]

    from apps.pedidos.models import MetodoPago
    return render(request, 'logistica/mi_ruta_hoy.html', {
        'ruta': ruta,
        'hojas_hoy': hojas_hoy,
        'pendientes': pendientes,
        'hechas': hechas,
        'extras': extras,
        'resumen': resumen,
        'camion': camion,
        'proximas': proximas,
        'hoy': hoy,
        'es_admin': es_admin,
        'motivos': MOTIVOS_NO_ENTREGA,
        'metodos_cobro': sorted(
            MetodoPago.objects.filter(activo=True, codigo__in=['EFECTIVO', 'TRANSFERENCIA', 'MERCADOPAGO', 'BILLETERA']),
            key=lambda m: ['EFECTIVO', 'TRANSFERENCIA', 'MERCADOPAGO', 'BILLETERA'].index(m.codigo)),
    })


@login_required
def confirmar_entrega(request, pk):
    """El repartidor registra la entrega (o el problema) de una parada desde su recorrido."""
    from decimal import Decimal, InvalidOperation
    from django.core.exceptions import ValidationError
    from apps.pedidos.models import MetodoPago

    parada = get_object_or_404(DetalleHojaRuta.objects.select_related('hoja_ruta', 'pedido'), id_detalle=pk)
    destino = reverse('apps.logistica:mi_ruta_hoy') + f'?hoja={parada.hoja_ruta_id}'
    if not (es_admin_o_vendedor(request.user) or es_repartidor_asignado(request.user, parada.hoja_ruta)):
        messages.error(request, 'Esta parada no es de tu recorrido.')
        return redirect('apps.logistica:mi_ruta_hoy')
    if request.method != 'POST':
        return redirect(destino)

    post = request.POST
    try:
        monto = Decimal(post.get('monto') or '0')
    except InvalidOperation:
        monto = Decimal('0')
    try:
        confirmar_entrega_en_calle(
            parada,
            entregado=post.get('resultado') == 'entregado',
            envases_retirados=_int_o_none(post.get('envases_retirados')) or 0,
            envases_vendidos=_int_o_none(post.get('envases_vendidos')) or 0,
            cobro=post.get('cobro') or 'ninguno',
            monto=monto,
            metodo_pago=MetodoPago.objects.filter(pk=_int_o_none(post.get('metodo_pago'))).first(),
            motivo=post.get('motivo') or '',
            reprogramar=post.get('accion') != 'cancelar',
            nota=(post.get('nota') or '').strip(),
        )
    except ValidationError as error:
        messages.error(request, ' '.join(error.messages))
        return redirect(destino)

    parada.refresh_from_db()
    if parada.estado == 'Entregado':
        messages.success(request, f'✔ Entregado a {parada.cliente_nombre}.')
    else:
        messages.warning(request, f'{parada.cliente_nombre}: {parada.estado.lower()}.')
    return redirect(destino)


# ─────────────────────────────────────────────────────────────
# ZONAS — CRUD
# ─────────────────────────────────────────────────────────────
@login_required
def listar_zonas(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para gestionar zonas.')
        return redirect('inicio')

    form = ZonaForm()

    if request.method == 'POST':
        form = ZonaForm(request.POST)
        if form.is_valid():
            zona = form.save()
            messages.success(request, f'Zona "{zona.nombre}" creada correctamente.')
            return redirect('apps.logistica:listar_zonas')

    zonas = Zona.objects.all()
    return render(request, 'logistica/listar_zonas.html', {'zonas': zonas, 'form': form})


@login_required
def editar_zona(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para editar zonas.')
        return redirect('apps.logistica:listar_zonas')

    zona = get_object_or_404(Zona, id_zona=pk)

    if request.method == 'POST':
        form = ZonaForm(request.POST, instance=zona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zona actualizada.')
            return redirect('apps.logistica:listar_zonas')
    else:
        form = ZonaForm(instance=zona)

    return render(request, 'logistica/editar_zona.html', {'form': form, 'zona': zona})


@login_required
def eliminar_zona(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para eliminar zonas.')
        return redirect('apps.logistica:listar_zonas')

    zona = get_object_or_404(Zona, id_zona=pk)
    if request.method == 'POST':
        try:
            zona.delete()
            messages.success(request, 'Zona eliminada.')
        except ProtectedError:
            messages.error(
                request,
                f'La zona "{zona.nombre}" tiene rutas de reparto asociadas: reasignalas antes de eliminarla.'
            )
        return redirect('apps.logistica:listar_zonas')

    return render(request, 'logistica/confirmar_eliminar.html', {
        'objeto': zona,
        'tipo': 'zona',
        'volver': 'apps.logistica:listar_zonas',
    })


# ─────────────────────────────────────────────────────────────
# ASIGNACIÓN RÁPIDA DE BARRIOS A ZONAS
# ─────────────────────────────────────────────────────────────
@login_required
def direcciones_sin_zona(request):
    """
    Vista adaptada para asignar Barrios huerfanos a Zonas,
    en vez de Direcciones a Zonas.
    """
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para asignar zonas.')
        return redirect('inicio')

    if request.method == 'POST':
        actualizados = 0
        for key, value in request.POST.items():
            if key.startswith('zona_barrio_') and value:
                barrio_pk = key.replace('zona_barrio_', '')
                try:
                    barrio = Barrio.objects.get(pk=barrio_pk)
                    zona_obj = Zona.objects.get(pk=value)
                    barrio.zona = zona_obj
                    barrio.save()
                    actualizados += 1
                except (Barrio.DoesNotExist, Zona.DoesNotExist, ValueError):
                    pass
        
        if actualizados > 0:
            messages.success(request, f'Se asignaron {actualizados} barrios a sus zonas correctamente.')
        return redirect('apps.logistica:direcciones_sin_zona')

    from django.db.models import Q
    barrios_huerfanos = Barrio.objects.filter(
        Q(zona__isnull=True) | Q(zona__nombre='Sin Asignar') | Q(zona__nombre='Zona 1')
    ).select_related('zona').order_by('nombre')
    zonas = Zona.objects.all()

    contexto = {
        'barrios': barrios_huerfanos,
        'zonas': zonas
    }
    return render(request, 'logistica/direcciones_sin_zona.html', contexto)


# ─────────────────────────────────────────────────────────────
# CAMIONES — CRUD
# ─────────────────────────────────────────────────────────────
@login_required
def listar_camiones(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para gestionar camiones.')
        return redirect('inicio')

    form = CamionForm()

    if request.method == 'POST':
        form = CamionForm(request.POST)
        if form.is_valid():
            camion = form.save()
            messages.success(request, f'Camión "{camion.patente}" registrado correctamente.')
            return redirect('apps.logistica:listar_camiones')

    camiones = Camion.objects.all()
    return render(request, 'logistica/listar_camiones.html', {'camiones': camiones, 'form': form})


@login_required
def editar_camion(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para editar camiones.')
        return redirect('apps.logistica:listar_camiones')

    camion = get_object_or_404(Camion, patente=pk)

    if request.method == 'POST':
        form = CamionForm(request.POST, instance=camion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Camión actualizado.')
            return redirect('apps.logistica:listar_camiones')
    else:
        form = CamionForm(instance=camion)

    return render(request, 'logistica/editar_camion.html', {'form': form, 'camion': camion})


@login_required
def eliminar_camion(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para eliminar camiones.')
        return redirect('apps.logistica:listar_camiones')

    camion = get_object_or_404(Camion, patente=pk)
    if request.method == 'POST':
        camion.delete()
        messages.success(request, 'Camión eliminado.')
        return redirect('apps.logistica:listar_camiones')

    return render(request, 'logistica/confirmar_eliminar.html', {
        'objeto': camion,
        'tipo': 'camión',
        'volver': 'apps.logistica:listar_camiones',
    })


# ─────────────────────────────────────────────────────────────
# PLANIFICAR REPARTO — generación de borradores (3B)
# ─────────────────────────────────────────────────────────────
def _parse_fecha(valor):
    if not valor:
        return None
    try:
        return datetime.strptime(valor, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        return None


def _int_o_none(valor):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return None


def _seleccion_desde_post(post):
    """Convierte los checkboxes/inputs del formulario en una selección estructurada."""
    seleccion = {'pedidos': [], 'frecuentes': []}
    for key in post:
        if key.startswith('pedido_') and post.get(key) == 'on':
            pid = key[len('pedido_'):]
            if pid.isdigit():
                seleccion['pedidos'].append({
                    'pedido_id': int(pid),
                    'cantidad': _int_o_none(post.get(f'cantidad_pedido_{pid}')),
                })
        elif key.startswith('frecuente_') and post.get(key) == 'on':
            cid = key[len('frecuente_'):]
            if cid.isdigit():
                dir_id = post.get(f'direccion_frecuente_{cid}')
                seleccion['frecuentes'].append({
                    'cliente_id': int(cid),
                    'direccion_id': int(dir_id) if dir_id and dir_id.isdigit() else None,
                    'cantidad': _int_o_none(post.get(f'cantidad_frecuente_{cid}')),
                    'producto_id': _int_o_none(post.get(f'producto_frecuente_{cid}')),
                })
    return seleccion


@login_required
def planificar_reparto(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para planificar repartos.')
        return redirect('inicio')

    zonas = Zona.objects.all()
    fecha = _parse_fecha(request.GET.get('fecha') or request.POST.get('fecha'))
    zona_id = request.GET.get('zona') or request.POST.get('zona')
    zona = Zona.objects.filter(pk=zona_id).first() if zona_id else None

    if request.method == 'POST' and request.POST.get('confirmar') == '1':
        if not (fecha and zona):
            messages.error(request, 'Elegí una fecha y una zona válidas.')
        else:
            seleccion = _seleccion_desde_post(request.POST)
            if not seleccion['pedidos'] and not seleccion['frecuentes']:
                messages.error(request, 'Seleccioná al menos un cliente o pedido para la ruta.')
            else:
                from apps.empleados.models import Empleado
                empleado = Empleado.objects.filter(pk=_int_o_none(request.POST.get('empleado')), activo=True).first()
                camion = Camion.objects.filter(pk=request.POST.get('camion') or None, activo=True).first()
                hoja = crear_hoja_borrador(fecha, zona, request.user, seleccion, empleado=empleado, camion=camion)
                messages.success(
                    request,
                    f'Hoja de ruta #{hoja.id_ruta} creada en borrador con '
                    f'{hoja.total_paradas()} paradas.'
                )
                return redirect('apps.logistica:ver_ruta', pk=hoja.id_ruta)

    borrador = construir_borrador(fecha, zona) if (fecha and zona) else None

    return render(request, 'logistica/planificar_reparto.html', {
        'zonas': zonas,
        'fecha': fecha,
        'zona': zona,
        'borrador': borrador,
        'productos_reparto': productos_de_reparto(),
        'botellon_defecto': botellon_por_defecto(),
        **_opciones_equipo(borrador['ruta_default'] if borrador else None),
    })


def _opciones_equipo(ruta_default=None, hoja=None):
    """Repartidores y camiones disponibles, con el valor preseleccionado."""
    from apps.empleados.models import Empleado
    empleado = getattr(hoja, 'empleado', None) or getattr(ruta_default, 'empleado_default', None)
    camion = getattr(hoja, 'camion', None) or getattr(ruta_default, 'camion_default', None)
    return {
        'repartidores': Empleado.objects.filter(activo=True, rol__grupo_permisos='Repartidor').order_by('apellido', 'nombre'),
        'camiones': Camion.objects.filter(activo=True).order_by('patente'),
        'empleado_elegido': getattr(empleado, 'pk', None),
        'camion_elegido': getattr(camion, 'pk', None),
    }


# ─────────────────────────────────────────────────────────────
# CONFIRMAR SALIDA Y REGISTRAR REGRESO (3C)
# ─────────────────────────────────────────────────────────────
def _cargas_confirmacion_desde_post(post):
    """Lee las cantidades cargadas por producto del formulario de confirmación."""
    cargas = []
    for key, value in post.items():
        if not key.startswith('cantidad_producto_'):
            continue
        pid = key[len('cantidad_producto_'):]
        cantidad = _int_o_none(value)
        if pid.isdigit() and cantidad:
            cargas.append({'producto_id': int(pid), 'cantidad': cantidad})
    return cargas


def _regreso_desde_post(post, hoja):
    """Lee entregadas/retornadas por carga del formulario de regreso."""
    cargas = []
    for carga in hoja.cargas.all():
        entregada = _int_o_none(post.get(f'entregada_{carga.id_carga}'))
        retornada = _int_o_none(post.get(f'retornada_{carga.id_carga}'))
        if entregada is None and retornada is None:
            continue
        cargas.append({
            'carga_id': carga.id_carga,
            'cantidad_entregada': entregada or 0,
            'cantidad_retornada': retornada,
        })
    return cargas


def _productos_para_carga(ruta):
    """Botellones llenos (con lo encargado en las paradas) y el envase vacío."""
    encargados = {c['producto'].pk: c['cantidad'] for c in carga_sugerida(ruta)}
    filas = [
        {'producto': p, 'encargado': encargados.get(p.pk, 0), 'cantidad': encargados.get(p.pk, 0)}
        for p in productos_de_reparto()
    ]
    envase = envase_de_reparto()
    if envase is not None:
        filas.append({'producto': envase, 'encargado': None, 'cantidad': 0, 'es_vacio': True})
    return filas


@login_required
def confirmar_ruta(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para confirmar rutas.')
        return redirect('apps.logistica:listar_rutas')

    ruta = get_object_or_404(HojaRuta, id_ruta=pk)

    if request.method == 'POST':
        if ruta.estado != 'Borrador':
            messages.error(request, 'Esta hoja ya fue confirmada o cerrada.')
            return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)
        from apps.empleados.models import Empleado
        ruta.empleado = Empleado.objects.filter(pk=_int_o_none(request.POST.get('empleado')), activo=True).first()
        ruta.camion = Camion.objects.filter(pk=request.POST.get('camion') or None, activo=True).first()
        ruta.save(update_fields=['empleado', 'camion'])
        cargas = _cargas_confirmacion_desde_post(request.POST)
        confirmar_hoja(ruta, request.user, cargas)
        messages.success(
            request,
            f'Hoja #{ruta.id_ruta} confirmada. Los pedidos pasaron a "En Camino".'
        )
        if ruta.empleado is None or ruta.camion is None:
            messages.warning(request, 'La hoja salió sin repartidor o sin camión asignado.')
        return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)

    productos = _productos_para_carga(ruta)
    return render(request, 'logistica/confirmar_ruta.html', {
        'ruta': ruta,
        'productos': productos,
        'falta_stock': [f for f in productos if f['encargado'] and f['encargado'] > f['producto'].stock],
        **_opciones_equipo(ruta.ruta_reparto, hoja=ruta),
    })


@login_required
def registrar_regreso_ruta(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para registrar el regreso.')
        return redirect('apps.logistica:listar_rutas')

    ruta = get_object_or_404(HojaRuta, id_ruta=pk)

    if request.method == 'POST':
        if ruta.estado != 'Confirmada':
            messages.error(request, 'Solo se puede registrar el regreso de una hoja confirmada.')
            return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)
        registrar_regreso(ruta, _regreso_desde_post(request.POST, ruta),
                          vacios_recibidos=_int_o_none(request.POST.get('vacios_recibidos')))
        messages.success(request, f'Regreso de la hoja #{ruta.id_ruta} registrado. Sobrantes y vacíos devueltos al stock.')
        return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)

    entregados = entregados_por_producto(ruta)
    cargas = [
        {'carga': c, 'entregado': entregados.get(c.producto_id, 0)}
        for c in ruta.cargas.select_related('producto')
    ]
    paradas = ruta.detalles.all()
    return render(request, 'logistica/registrar_regreso.html', {
        'ruta': ruta,
        'cargas': cargas,
        'envase': envase_de_reparto(),
        'vacios_retirados': envases_retirados_en_hoja(ruta),
        'envases_vendidos': sum(p.envases_vendidos for p in paradas),
        'paradas_pendientes': [p for p in paradas if p.estado == 'Pendiente'],
        'resumen': resumen_recorrido(ruta),
    })


# ─────────────────────────────────────────────────────────────
# VENTA EN CALLE (3D) — el repartidor agrega una parada/venta
# ─────────────────────────────────────────────────────────────
@login_required
def venta_calle(request, pk):
    """Pedido espontáneo que el repartidor vende durante el reparto."""
    from apps.clientes.models import DireccionEntrega
    from apps.pedidos.models import MetodoPago

    hoja = get_object_or_404(HojaRuta.objects.select_related('zona'), id_ruta=pk)
    es_admin = es_admin_o_vendedor(request.user)
    if not (es_admin or es_repartidor_asignado(request.user, hoja)):
        messages.error(request, 'No tenés permiso para registrar ventas en esta hoja.')
        return redirect('apps.logistica:mi_ruta_hoy')
    volver = reverse('apps.logistica:mi_ruta_hoy') + f'?hoja={hoja.pk}'
    if hoja.estado != 'Confirmada':
        messages.error(request, 'Las ventas en la calle se registran con la hoja en reparto.')
        return redirect(volver)

    if request.method == 'POST':
        post = request.POST
        productos = []
        for key, value in post.items():
            if key.startswith('cantidad_producto_') and key[len('cantidad_producto_'):].isdigit():
                cantidad = _int_o_none(value)
                if cantidad:
                    productos.append({'producto_id': int(key[len('cantidad_producto_'):]), 'cantidad': cantidad})
        direccion = DireccionEntrega.objects.filter(pk=_int_o_none(post.get('direccion'))).select_related('cliente').first()
        try:
            parada = crear_venta_calle(hoja, {
                'cliente_id': direccion.cliente_id if direccion else None,
                'direccion_id': direccion.pk if direccion else None,
                'nombre': (post.get('nombre') or '').strip(),
                'apellido': (post.get('apellido') or '').strip(),
                'calle': (post.get('calle') or '').strip(),
                'altura': (post.get('altura') or '').strip(),
                'barrio_id': _int_o_none(post.get('barrio')),
                'productos': productos,
                'envases_retirados': _int_o_none(post.get('envases_retirados')) or 0,
                'cobro': post.get('cobro') or 'total',
                'metodo_pago_id': _int_o_none(post.get('metodo_pago')),
                'marcar_frecuente': post.get('marcar_frecuente') == 'on',
                'nota': (post.get('nota') or '').strip(),
            })
        except ValueError as error:
            messages.error(request, str(error))
            return redirect('apps.logistica:venta_calle', pk=hoja.pk)
        messages.success(request, f'Venta registrada: {parada.cliente_nombre} — {parada.resumen_pedido()} (${parada.pedido.total}).')
        faltan = inventario_camion(hoja)['faltan']
        if faltan:
            messages.warning(request, f'Atención: faltan {faltan} botellones para completar los pedidos del recorrido.')
        if es_admin and not es_repartidor(request.user):
            return redirect('apps.logistica:ver_ruta', pk=hoja.id_ruta)
        return redirect(volver)

    # La zona se elige primero (por defecto la de la hoja) y filtra clientes y barrios.
    direcciones = (DireccionEntrega.objects.exclude(barrio__zona=None)
                   .select_related('cliente', 'barrio').order_by('cliente__apellido', 'cliente__nombre'))
    barrios = Barrio.objects.exclude(zona=None).order_by('nombre')
    zonas = Zona.objects.filter(pk__in=barrios.values('zona')).order_by('nombre')
    codigos = ['EFECTIVO', 'TRANSFERENCIA', 'MERCADOPAGO', 'BILLETERA']
    return render(request, 'logistica/venta_calle.html', {
        'hoja': hoja,
        'productos': productos_de_reparto(),
        'botellon_defecto': botellon_por_defecto(),
        'camion': inventario_camion(hoja),
        'direcciones': direcciones,
        'barrios': barrios,
        'zonas': zonas,
        'metodos_pago': sorted(MetodoPago.objects.filter(activo=True, codigo__in=codigos),
                               key=lambda m: codigos.index(m.codigo)),
    })
