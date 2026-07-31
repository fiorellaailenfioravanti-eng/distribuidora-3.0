from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import HojaRuta, DetalleHojaRuta, Zona, Barrio, Camion, Empleado, RutaReparto
from .forms  import HojaRutaForm, DetalleRutaForm, ActualizarEstadoForm, ZonaForm, CamionForm
from apps.clientes.models import DireccionEntrega


# ─────────────────────────────────────────────────────────────
# HELPERS DE PERMISOS
# ─────────────────────────────────────────────────────────────
def es_admin_o_vendedor(user):
    return user.is_superuser or user.groups.filter(name__in=['Vendedor']).exists()


def es_repartidor(user):
    return user.groups.filter(name='Repartidor').exists()


def es_admin_vendedor_o_repartidor(user):
    return es_admin_o_vendedor(user) or es_repartidor(user)


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
        try:
            empleado = request.user.empleado
            rutas = HojaRuta.objects.filter(empleado=empleado)
        except Empleado.DoesNotExist:
            rutas = HojaRuta.objects.none()
    else:
        rutas = HojaRuta.objects.all()

    # Filtros opcionales
    filtro_zona   = request.GET.get('zona', '')
    filtro_estado = request.GET.get('estado', '')
    filtro_fecha  = request.GET.get('fecha', '')

    if filtro_zona:
        rutas = rutas.filter(ruta_reparto__zona__id_zona=filtro_zona)
    if filtro_estado:
        rutas = rutas.filter(estado=filtro_estado)
    if filtro_fecha:
        rutas = rutas.filter(fecha=filtro_fecha)

    rutas = rutas.select_related('empleado__usuario', 'camion', 'ruta_reparto', 'ruta_reparto__zona')

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
    ruta = get_object_or_404(HojaRuta.objects.select_related('ruta_reparto__zona'), id_ruta=pk)

    # Repartidor solo puede ver sus propias rutas
    if es_repartidor(request.user) and not es_admin_o_vendedor(request.user):
        try:
            if ruta.empleado.usuario != request.user:
                messages.error(request, 'No tenés permiso para ver esta ruta.')
                return redirect('apps.logistica:mi_ruta_hoy')
        except Empleado.DoesNotExist:
            return redirect('apps.logistica:mi_ruta_hoy')

    detalles     = ruta.detalles.all()
    form_parada  = DetalleRutaForm()

    # Sugerencias: clientes de la zona
    dia_semana = ruta.fecha.weekday()  # 0=Lunes, 6=Domingo
    ruta_reparto = ruta.ruta_reparto
    zona = ruta_reparto.zona
    
    coincide_dia = (dia_semana == ruta_reparto.dia_semana)

    sugerencias = []
    if coincide_dia and es_admin_o_vendedor(request.user):
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
        try:
            if ruta.empleado.usuario != request.user:
                return redirect('apps.logistica:mi_ruta_hoy')
        except Empleado.DoesNotExist:
            return redirect('apps.logistica:mi_ruta_hoy')

    detalles = ruta.detalles.all()

    contexto = {
        'ruta': ruta,
        'detalles': detalles,
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
    parada = get_object_or_404(DetalleHojaRuta, id_detalle=pk)

    es_admin = es_admin_o_vendedor(request.user)
    try:
        es_asignado = (parada.hoja_ruta.empleado.usuario == request.user)
    except Empleado.DoesNotExist:
        es_asignado = False

    if not (es_admin or es_asignado):
        messages.error(request, 'No tenés permiso para actualizar esta entrega.')
        return redirect('apps.logistica:mi_ruta_hoy')

    if request.method == 'POST':
        form = ActualizarEstadoForm(request.POST, instance=parada)
        if form.is_valid():
            nuevo_estado = form.cleaned_data['estado']
            parada_obj   = form.save(commit=False)
            parada_obj.marcar_estado(nuevo_estado)
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

    try:
        empleado = request.user.empleado
        ruta     = HojaRuta.objects.filter(
            empleado=empleado,
            fecha=hoy
        ).select_related('camion', 'ruta_reparto__zona').first()

        if ruta:
            detalles = ruta.detalles.all()
    except Empleado.DoesNotExist:
        pass

    contexto = {
        'ruta':    ruta,
        'detalles': detalles,
        'hoy':     hoy,
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
