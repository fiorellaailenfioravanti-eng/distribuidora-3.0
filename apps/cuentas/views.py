from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from apps.clientes.models import Cliente
from apps.permisos.roles import es_admin_o_vendedor
from . import services
from .forms import CargoCuentaForm, PagoCuentaForm
from .models import CuentaCorriente, NIVELES_MOROSIDAD


def _sin_permiso(request):
    messages.error(request, 'No tenés permiso para acceder a esta sección.')
    return redirect('inicio')


def _cuentas_con_morosidad():
    """Todas las cuentas activas, cada una con su nivel de morosidad calculado."""
    resultado = []
    for cuenta in CuentaCorriente.objects.select_related('cliente').filter(activa=True):
        nivel = cuenta.nivel_morosidad()
        resultado.append({
            'cuenta': cuenta,
            'nivel': nivel,
            'estado': NIVELES_MOROSIDAD[nivel],
            'dias_atraso': cuenta.dias_de_atraso(),
        })
    return resultado


# ─────────────────────────────────────────────────────────────
# LISTADO DE CUENTAS CORRIENTES
# ─────────────────────────────────────────────────────────────
@login_required
def listar_cuentas(request):
    if not es_admin_o_vendedor(request.user):
        return _sin_permiso(request)

    nivel = request.GET.get('nivel', '').strip()
    q = request.GET.get('q', '').strip().lower()

    filas = _cuentas_con_morosidad()
    if nivel:
        filas = [f for f in filas if f['nivel'] == nivel]
    if q:
        filas = [f for f in filas if q in f['cuenta'].cliente.nombre_completo().lower()]

    filas.sort(key=lambda f: f['cuenta'].saldo, reverse=True)

    paginator = Paginator(filas, 15)
    page_obj = paginator.get_page(request.GET.get('page'))

    contexto = {
        'page_obj': page_obj,
        'nivel': nivel,
        'q': request.GET.get('q', ''),
        'niveles': NIVELES_MOROSIDAD,
        'resumen': services.resumen_morosidad(),
    }
    return render(request, 'cuentas/listar_cuentas.html', contexto)


# ─────────────────────────────────────────────────────────────
# DETALLE DE UNA CUENTA
# ─────────────────────────────────────────────────────────────
@login_required
def ver_cuenta(request, pk):
    if not es_admin_o_vendedor(request.user):
        return _sin_permiso(request)

    cuenta = get_object_or_404(
        CuentaCorriente.objects.select_related('cliente'), pk=pk
    )
    movimientos = cuenta.movimientos.select_related('pedido', 'abono').all()

    contexto = {
        'cuenta': cuenta,
        'movimientos': movimientos,
        'cargo_form': CargoCuentaForm(),
        'pago_form': PagoCuentaForm(),
        'estado': cuenta.estado_morosidad(),
        'dias_atraso': cuenta.dias_de_atraso(),
    }
    return render(request, 'cuentas/ver_cuenta.html', contexto)


@login_required
def cuenta_de_cliente(request, cliente_pk):
    """Abre (o crea) la cuenta corriente de un cliente y redirige a su detalle."""
    if not es_admin_o_vendedor(request.user):
        return _sin_permiso(request)

    cliente = get_object_or_404(Cliente, pk=cliente_pk)
    cuenta = services.obtener_o_crear_cuenta(cliente)
    return redirect('apps.cuentas:ver_cuenta', pk=cuenta.pk)


# ─────────────────────────────────────────────────────────────
# REGISTRAR CARGO / PAGO
# ─────────────────────────────────────────────────────────────
@login_required
def registrar_cargo(request, pk):
    if not es_admin_o_vendedor(request.user):
        return _sin_permiso(request)
    if request.method != 'POST':
        return redirect('apps.cuentas:ver_cuenta', pk=pk)

    cuenta = get_object_or_404(CuentaCorriente.objects.select_related('cliente'), pk=pk)
    form = CargoCuentaForm(request.POST)
    if form.is_valid():
        try:
            services.registrar_cargo(
                cuenta,
                form.cleaned_data['monto'],
                descripcion=form.cleaned_data.get('descripcion', ''),
                fecha_vencimiento=form.cleaned_data.get('fecha_vencimiento'),
            )
            messages.success(request, 'Cargo registrado correctamente.')
        except ValidationError as exc:
            messages.error(request, exc.messages[0] if exc.messages else 'No se pudo registrar el cargo.')
    else:
        messages.error(request, 'Revisá los datos del cargo (monto inválido).')

    return redirect('apps.cuentas:ver_cuenta', pk=cuenta.pk)


@login_required
def registrar_pago(request, pk):
    if not es_admin_o_vendedor(request.user):
        return _sin_permiso(request)
    if request.method != 'POST':
        return redirect('apps.cuentas:ver_cuenta', pk=pk)

    cuenta = get_object_or_404(CuentaCorriente.objects.select_related('cliente'), pk=pk)
    form = PagoCuentaForm(request.POST)
    if form.is_valid():
        try:
            services.registrar_pago(
                cuenta,
                form.cleaned_data['monto'],
                descripcion=form.cleaned_data.get('descripcion', ''),
            )
            messages.success(request, 'Pago registrado correctamente.')
        except ValidationError as exc:
            messages.error(request, exc.messages[0] if exc.messages else 'No se pudo registrar el pago.')
    else:
        messages.error(request, 'Revisá los datos del pago (monto inválido).')

    return redirect('apps.cuentas:ver_cuenta', pk=cuenta.pk)
