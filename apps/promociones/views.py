from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from apps.clientes.models import Cliente
from apps.permisos.roles import es_admin_o_vendedor
from apps.permisos.views import sin_permiso

from . import services
from .forms import PromocionForm, VenderPromocionForm
from .models import CompraPromocion, Promocion


@login_required
def listar_promociones(request):
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)
    hoy = timezone.localdate()
    vigentes = CompraPromocion.objects.filter(
        estado='Vigente', unid_restantes__gt=0, fecha_caducidad__gte=hoy,
    ).select_related('cliente', 'promocion__producto')
    return render(request, 'promociones/listar_promociones.html', {
        'promociones': Promocion.objects.select_related('producto'),
        'compras_vigentes': vigentes,
        'por_vencer': services.promociones_por_vencer(),
        'hoy': hoy,
    })


def _form_promocion(request, promocion=None):
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)
    form = PromocionForm(request.POST or None, instance=promocion)
    if request.method == 'POST' and form.is_valid():
        promocion = form.save()
        messages.success(request, f'Promoción "{promocion.nombre}" guardada.')
        return redirect('apps.promociones:listar_promociones')
    return render(request, 'promociones/form_promocion.html', {'form': form, 'promocion': promocion})


@login_required
def crear_promocion(request):
    return _form_promocion(request)


@login_required
def editar_promocion(request, pk):
    return _form_promocion(request, get_object_or_404(Promocion, pk=pk))


@login_required
def vender_promocion(request, cliente_pk):
    """Venta de un pack prepago desde la ficha del cliente (RF-09)."""
    if not es_admin_o_vendedor(request.user):
        return sin_permiso(request)
    cliente = get_object_or_404(Cliente, pk=cliente_pk)
    if request.method != 'POST':
        return redirect('apps.clientes:ver_cliente', pk=cliente.pk)

    form = VenderPromocionForm(request.POST)
    if form.is_valid():
        try:
            compra = services.vender_promocion(
                cliente, form.cleaned_data['promocion'],
                metodo_pago=form.cleaned_data['metodo_pago'], a_cuenta=form.cleaned_data['a_cuenta'],
            )
            messages.success(
                request,
                f'Se vendió "{compra.promocion.nombre}": {compra.unid_totales} unidades disponibles '
                f'hasta el {compra.fecha_caducidad:%d/%m/%Y}.'
            )
        except ValidationError as error:
            messages.error(request, ' '.join(error.messages))
    else:
        messages.error(request, 'Elegí una promoción válida.')
    return redirect('apps.clientes:ver_cliente', pk=cliente.pk)
