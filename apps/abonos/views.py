from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from apps.permisos.roles import es_admin_o_vendedor
from apps.permisos.views import sin_permiso
from . import services
from .forms import AbonoForm
from .models import Abono



@login_required
def listar_abonos(request):
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)

    estado = request.GET.get('estado', '').strip()
    abonos = Abono.objects.select_related('cliente', 'producto').all()
    if estado:
        abonos = abonos.filter(estado=estado)

    paginator = Paginator(abonos, 15)
    page_obj = paginator.get_page(request.GET.get('page'))

    contexto = {
        'page_obj': page_obj,
        'estado': estado,
        'hoy': timezone.localdate(),
    }
    return render(request, 'abonos/listar_abonos.html', contexto)


@login_required
def ver_abono(request, pk):
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)

    abono = get_object_or_404(
        Abono.objects.select_related('cliente', 'producto'), pk=pk
    )
    movimientos = abono.movimientos_cuenta.select_related('cuenta').all()
    contexto = {
        'abono': abono,
        'movimientos': movimientos,
        'costo_efectivo': abono.costo_para_cliente(),
    }
    return render(request, 'abonos/ver_abono.html', contexto)


@login_required
def crear_abono(request):
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)

    if request.method == 'POST':
        form = AbonoForm(request.POST)
        if form.is_valid():
            abono = form.save()
            messages.success(request, 'Abono creado correctamente.')
            return redirect('apps.abonos:ver_abono', pk=abono.pk)
        messages.error(request, 'Revisá los datos del formulario.')
    else:
        form = AbonoForm(initial={'fecha_inicio': timezone.localdate()})

    return render(request, 'abonos/form_abono.html', {'form': form, 'titulo': 'Nuevo abono'})


@login_required
def editar_abono(request, pk):
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)

    abono = get_object_or_404(Abono, pk=pk)
    if request.method == 'POST':
        form = AbonoForm(request.POST, instance=abono)
        if form.is_valid():
            form.save()
            messages.success(request, 'Abono actualizado correctamente.')
            return redirect('apps.abonos:ver_abono', pk=abono.pk)
        messages.error(request, 'Revisá los datos del formulario.')
    else:
        form = AbonoForm(instance=abono)

    return render(request, 'abonos/form_abono.html', {
        'form': form, 'abono': abono, 'titulo': 'Editar abono',
    })


@login_required
def cambiar_estado_abono(request, pk):
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)
    if request.method != 'POST':
        return redirect('apps.abonos:ver_abono', pk=pk)

    abono = get_object_or_404(Abono, pk=pk)
    nuevo = request.POST.get('estado', '')
    if nuevo in dict(Abono._meta.get_field('estado').choices):
        abono.estado = nuevo
        abono.save(update_fields=['estado'])
        messages.success(request, f'Estado del abono: {nuevo}.')
    else:
        messages.error(request, 'Estado inválido.')
    return redirect('apps.abonos:ver_abono', pk=abono.pk)


@login_required
def generar_cargos(request):
    """Dispara manualmente la facturación mensual de los abonos activos."""
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)
    if request.method != 'POST':
        return redirect('apps.abonos:listar_abonos')

    generados, omitidos = services.generar_cargos_mensuales()
    if generados:
        messages.success(request, f'Se generaron {len(generados)} cargo(s) de abono.')
    else:
        messages.info(request, 'No había abonos para facturar este mes.')
    if omitidos:
        messages.warning(
            request,
            f'{len(omitidos)} abono(s) omitido(s) por falta de fiado (RF-05).'
        )
    return redirect('apps.abonos:listar_abonos')
