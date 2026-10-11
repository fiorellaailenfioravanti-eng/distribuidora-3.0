from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

from .models import HojaRuta, DetalleHojaRuta, Zona, Barrio, Camion, RutaReparto
from .forms  import HojaRutaForm, DetalleRutaForm, ActualizarEstadoForm, ZonaForm, CamionForm
from .services import (
    construir_borrador, crear_hoja_borrador,
    carga_sugerida, confirmar_hoja, registrar_regreso,
    registrar_entrega, registrar_cobro, crear_venta_calle,
)
from apps.clientes.models import DireccionEntrega
from apps.permisos.roles import (
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

    ruta = get_object_or_404(HojaRuta.objects.select_related('ruta_reparto__zona'), id_ruta=pk)

    # Repartidor solo puede ver sus propias rutas
    if es_repartidor(request.user) and not es_admin_o_vendedor(request.user):
        empleado = obtener_empleado(request.user)
        if empleado is None or ruta.empleado_id != empleado.id_empleado:
            messages.error(request, 'No tenés permiso para ver esta ruta.')
            return redirect('apps.logistica:mi_ruta_hoy')

    detalles     = ruta.detalles.all()
    form_parada  = DetalleRutaForm()

    # Sugerencias: clientes de la zona
    dia_semana = ruta.fecha.weekday()  # 0=Lunes, 6=Domingo
    ruta_reparto = ruta.ruta_reparto
    zona = ruta.zona or (ruta_reparto.zona if ruta_reparto else None)

    coincide_dia = bool(ruta_reparto) and (dia_semana == ruta_reparto.dia_semana)

    sugerencias = []
    if zona is not None and es_admin_o_vendedor(request.user):
        direcciones_zona = DireccionEntrega.objects.filter(barrio__zona=zona).select_related('cliente', 'barrio')
        # Filtramos para no sugerir a clientes que ya están en la hoja (aproximación por nombre o direccion)
        nombres_ya_agregados = set(d.cliente_nombre for d in detalles)
        direcciones_agregadas = set(d.direccion_entrega_id for d in detalles if d.direccion_entrega_id)
        
        for d in direcciones_zona:
            if d.pk not in direcciones_agregadas and d.cliente.nombre_completo() not in nombres_ya_agregados:
                sugerencias.append(d)

    contexto = {
        'ruta':        ruta,
        'detalles':    detalles,
        'form_parada': form_parada,
        'sugerencias': sugerencias,
        'es_admin':    es_admin_o_vendedor(request.user),
        'paradas_con_nota_visible': _ids_de_paradas_con_nota(request.user, detalles),
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
@login_required
def agregar_parada(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para agregar paradas.')
        return redirect('apps.logistica:listar_rutas')

    ruta = get_object_or_404(HojaRuta, id_ruta=pk)

    if request.method == 'POST':
        form = DetalleRutaForm(request.POST)
        if form.is_valid():
            parada = form.save(commit=False)
            parada.hoja_ruta = ruta
            # Si se elige una direccion_entrega, poblamos el texto de direccion de respaldo
            if parada.direccion_entrega:
                if not parada.direccion_texto:
                    parada.direccion_texto = parada.direccion_entrega.direccion_completa()
                if not parada.cliente_nombre:
                    parada.cliente_nombre = parada.direccion_entrega.cliente.nombre_completo()
            parada.save()
            messages.success(request, f'Parada {parada.orden} agregada a la ruta #{ruta.id_ruta}.')
        else:
            messages.error(request, 'Error al agregar la parada. Revisá los datos.')

    return redirect('apps.logistica:ver_ruta', pk=pk)


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
        parada.delete()
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
                registrar_cobro(parada.pedido, monto, form.cleaned_data.get('metodo_pago'))
            messages.success(request, f'Estado actualizado a "{nuevo_estado}" correctamente.')
            if es_admin:
                return redirect('apps.logistica:ver_ruta', pk=parada.hoja_ruta.id_ruta)
            return redirect('apps.logistica:mi_ruta_hoy')
    else:
        form = ActualizarEstadoForm(instance=parada)

    return render(request, 'logistica/actualizar_estado.html', {'form': form, 'parada': parada})


# ─────────────────────────────────────────────────────────────
# MI RUTA HOY — Vista para repartidor
# ─────────────────────────────────────────────────────────────
@login_required
def mi_ruta_hoy(request):
    if not (es_repartidor(request.user) or es_admin_o_vendedor(request.user)):
        messages.error(request, 'No tenés permiso para acceder a esta sección.')
        return redirect('inicio')

    hoy = timezone.localdate()
    ruta = None
    detalles = []

    empleado = obtener_empleado(request.user)
    if empleado is not None:
        ruta = HojaRuta.objects.filter(
            empleado=empleado,
            fecha=hoy
        ).select_related('camion', 'ruta_reparto__zona').first()

        if ruta:
            detalles = ruta.detalles.all()

    contexto = {
        'ruta':    ruta,
        'detalles': detalles,
        'hoy':     hoy,
        'paradas_con_nota_visible': _ids_de_paradas_con_nota(request.user, detalles),
    }
    return render(request, 'logistica/mi_ruta_hoy.html', contexto)


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
        zona.delete()
        messages.success(request, 'Zona eliminada.')
        return redirect('apps.logistica:listar_zonas')

    return render(request, 'logistica/confirmar_eliminar.html', {
        'objeto': zona,
        'tipo': 'zona',
        'url_cancelar': 'apps.logistica:listar_zonas'
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
                hoja = crear_hoja_borrador(fecha, zona, request.user, seleccion)
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
    })


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
    """Productos del catálogo con la cantidad sugerida a cargar en la hoja."""
    from apps.productos.models import Producto
    sugeridas = {c['producto'].pk: c['cantidad'] for c in carga_sugerida(ruta)}
    return [
        {'producto': p, 'cantidad': sugeridas.get(p.pk, 0)}
        for p in Producto.objects.all().order_by('nombre')
    ]


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
        cargas = _cargas_confirmacion_desde_post(request.POST)
        confirmar_hoja(ruta, request.user, cargas)
        messages.success(
            request,
            f'Hoja #{ruta.id_ruta} confirmada. Los pedidos pasaron a "En Camino".'
        )
        return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)

    return render(request, 'logistica/confirmar_ruta.html', {
        'ruta': ruta,
        'productos': _productos_para_carga(ruta),
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
        registrar_regreso(ruta, _regreso_desde_post(request.POST, ruta))
        messages.success(request, f'Regreso de la hoja #{ruta.id_ruta} registrado. Sobrantes devueltos al stock.')
        return redirect('apps.logistica:ver_ruta', pk=ruta.id_ruta)

    return render(request, 'logistica/registrar_regreso.html', {
        'ruta': ruta,
        'cargas': ruta.cargas.select_related('producto'),
    })


# ─────────────────────────────────────────────────────────────
# VENTA EN CALLE (3D) — el repartidor agrega una parada/venta
# ─────────────────────────────────────────────────────────────
@login_required
def venta_calle(request, pk):
    from apps.productos.models import Producto
    from apps.pedidos.models import MetodoPago

    hoja = get_object_or_404(HojaRuta, id_ruta=pk)
    es_admin = es_admin_o_vendedor(request.user)
    empleado = obtener_empleado(request.user)
    es_asignado = empleado is not None and hoja.empleado_id == empleado.id_empleado

    if not (es_admin or es_asignado):
        messages.error(request, 'No tenés permiso para registrar ventas en esta hoja.')
        return redirect('apps.logistica:mi_ruta_hoy')

    if request.method == 'POST':
        productos = []
        for key, value in request.POST.items():
            if key.startswith('cantidad_producto_'):
                pid = key[len('cantidad_producto_'):]
                cantidad = _int_o_none(value)
                if pid.isdigit() and cantidad:
                    productos.append({'producto_id': int(pid), 'cantidad': cantidad})

        if not productos:
            messages.error(request, 'Agregá al menos un producto con cantidad.')
        else:
            parada = crear_venta_calle(hoja, {
                'cliente_id': _int_o_none(request.POST.get('cliente_id')),
                'nombre': (request.POST.get('nombre') or '').strip(),
                'apellido': (request.POST.get('apellido') or '').strip(),
                'calle': (request.POST.get('calle') or '').strip(),
                'altura': (request.POST.get('altura') or '').strip(),
                'barrio_id': _int_o_none(request.POST.get('barrio')),
                'metodo_pago_id': _int_o_none(request.POST.get('metodo_pago')),
                'marcar_frecuente': request.POST.get('marcar_frecuente') == 'on',
                'productos': productos,
            })
            messages.success(request, f'Venta en calle registrada (parada #{parada.id_detalle}).')
            if es_admin:
                return redirect('apps.logistica:ver_ruta', pk=hoja.id_ruta)
            return redirect('apps.logistica:mi_ruta_hoy')

    return render(request, 'logistica/venta_calle.html', {
        'hoja': hoja,
        'productos': Producto.objects.all().order_by('nombre'),
        'barrios': Barrio.objects.all().order_by('nombre'),
        'metodos_pago': MetodoPago.objects.filter(activo=True),
    })
