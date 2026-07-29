from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import HojaRuta, DetalleHojaRuta, Zona, Camion, Empleado
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
        rutas = rutas.filter(zona__id_zona=filtro_zona)
    if filtro_estado:
        rutas = rutas.filter(estado=filtro_estado)
    if filtro_fecha:
        rutas = rutas.filter(fecha=filtro_fecha)

    rutas = rutas.select_related('empleado__usuario', 'camion', 'zona')

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
    ruta = get_object_or_404(HojaRuta, id_ruta=pk)

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

    # Sugerencias: clientes de la zona (si la ruta coincide con el día de la semana)
    dia_semana = ruta.fecha.weekday()  # 0=Lunes, 6=Domingo
    zona = ruta.zona
    
    coincide_dia = False
    if dia_semana == 0 and zona.lunes: coincide_dia = True
    elif dia_semana == 1 and zona.martes: coincide_dia = True
    elif dia_semana == 2 and zona.miercoles: coincide_dia = True
    elif dia_semana == 3 and zona.jueves: coincide_dia = True
    elif dia_semana == 4 and zona.viernes: coincide_dia = True
    elif dia_semana == 5 and zona.sabado: coincide_dia = True

    sugerencias = []
    if coincide_dia and es_admin_o_vendedor(request.user):
        from apps.clientes.models import DireccionEntrega
        direcciones_zona = DireccionEntrega.objects.filter(zona=zona).select_related('cliente')
        # Filtramos para no sugerir a clientes que ya están en la hoja (aproximación por nombre)
        nombres_ya_agregados = set(d.cliente_nombre for d in detalles)
        for d in direcciones_zona:
            if d.cliente.nombre_completo() not in nombres_ya_agregados:
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

    # Solo el repartidor asignado a esa ruta (o un admin) puede actualizar
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
            # Redirigir al origen correcto
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
        ).select_related('camion', 'zona').first()

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
# ASIGNACIÓN RÁPIDA DE RUTAS A CLIENTES (DOMICILIOS)
# ─────────────────────────────────────────────────────────────
@login_required
def direcciones_sin_zona(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para asignar zonas.')
        return redirect('inicio')

    if request.method == 'POST':
        # Procesamiento masivo de zonas
        # El POST vendrá con names de la forma zona_direccion_{pk}
        actualizados = 0
        for key, value in request.POST.items():
            if key.startswith('zona_direccion_') and value:
                dir_pk = key.replace('zona_direccion_', '')
                try:
                    direccion = DireccionEntrega.objects.get(pk=dir_pk)
                    zona_obj = Zona.objects.get(pk=value)
                    direccion.zona = zona_obj
                    direccion.save()
                    actualizados += 1
                except (DireccionEntrega.DoesNotExist, Zona.DoesNotExist, ValueError):
                    pass
        
        if actualizados > 0:
            messages.success(request, f'Se asignaron {actualizados} domicilios a sus zonas correctamente.')
        return redirect('apps.logistica:direcciones_sin_zona')

    # Filtrar direcciones que no tienen zona asignada
    direcciones_huerfanas = DireccionEntrega.objects.filter(zona__isnull=True).select_related('cliente')
    zonas = Zona.objects.all()

    contexto = {
        'direcciones': direcciones_huerfanas,
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
