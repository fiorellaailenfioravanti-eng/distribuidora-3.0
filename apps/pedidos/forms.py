from django import forms
from .models import CODIGO_CUENTA_CORRIENTE, MetodoPago, Pedido, SuscripcionReposicion
from apps.clientes.models import DireccionEntrega


def _etiqueta_direccion_con_fecha(direccion):
    """Texto de la dirección con la fecha estimada de entrega de su zona (RF-16/3E)."""
    from apps.logistica.services import fecha_estimada_para_direccion
    etiqueta = str(direccion)
    fecha = fecha_estimada_para_direccion(direccion)
    if fecha:
        etiqueta += f' — entrega estimada: {fecha:%d/%m/%Y}'
    return etiqueta


# Métodos que no se ofrecen en el checkout web. La tarjeta se cobra por
# MercadoPago o con posnet al entregar (decisión A-D1): el sistema no procesa
# datos de tarjetas.
CODIGOS_FUERA_DEL_CHECKOUT_WEB = ('TARJETA', 'CUENTA')


def metodos_pago_checkout_web():
    """Métodos activos ofrecidos al cliente en la web."""
    from django.conf import settings
    excluidos = list(CODIGOS_FUERA_DEL_CHECKOUT_WEB)
    if not getattr(settings, 'MERCADOPAGO_ACCESS_TOKEN', ''):
        # Sin token el checkout online fallaría; no se ofrece (sin desactivarlo).
        excluidos.append('MERCADOPAGO')
    return MetodoPago.objects.filter(activo=True).exclude(codigo__in=excluidos)


class CheckoutForm(forms.Form):
    direccion_entrega = forms.ModelChoiceField(
        queryset=DireccionEntrega.objects.none(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None,
        required=True,
        label="Dirección de entrega"
    )
    metodo_pago = forms.ModelChoiceField(
        queryset=MetodoPago.objects.filter(activo=True),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None,
        required=True,
        label="Método de Pago"
    )
    notas_cliente = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ej: Timbre no funciona, dejar con el encargado o llamar antes de llegar...'
        }),
        required=False,
        label="Indicaciones de entrega (opcional)"
    )

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)
        self.fields['direccion_entrega'].label_from_instance = _etiqueta_direccion_con_fecha
        self.fields['metodo_pago'].queryset = metodos_pago_checkout_web()
        if cliente:
            self.fields['direccion_entrega'].queryset = cliente.direcciones.all()
            # Si tiene direcciones, seleccionar la principal por defecto
            direccion_principal = cliente.direcciones.filter(es_principal=True).first()
            if direccion_principal and not self.is_bound:
                self.fields['direccion_entrega'].initial = direccion_principal.pk
            elif cliente.direcciones.exists() and not self.is_bound:
                self.fields['direccion_entrega'].initial = cliente.direcciones.first().pk

            # Preseleccionar método de pago activo
            metodos_activos = self.fields['metodo_pago'].queryset
            if metodos_activos.count() == 1 and not self.is_bound:
                self.fields['metodo_pago'].initial = metodos_activos.first().pk
            else:
                ultimo_pedido = cliente.pedidos.first()
                if ultimo_pedido and ultimo_pedido.metodo_pago and not self.is_bound:
                    self.fields['metodo_pago'].initial = ultimo_pedido.metodo_pago.pk



class RegistrarPagoForm(forms.Form):
    """Cobro manual de un pedido (total o parcial) — RF-13 / HU-05."""
    monto = forms.DecimalField(min_value=0.01, max_digits=12, decimal_places=2, label='Monto',
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    metodo_pago = forms.ModelChoiceField(queryset=MetodoPago.objects.filter(activo=True), label='Medio de pago',
                                         empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    referencia = forms.CharField(required=False, max_length=100, label='Comprobante / referencia',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opcional'}))

    def __init__(self, *args, pedido=None, **kwargs):
        super().__init__(*args, **kwargs)
        if pedido is not None:
            self.fields['monto'].initial = pedido.saldo_pendiente()
            if not (pedido.cliente and pedido.cliente.permite_fiado):
                self.fields['metodo_pago'].queryset = self.fields['metodo_pago'].queryset.exclude(
                    codigo=CODIGO_CUENTA_CORRIENTE)


class SuscripcionForm(forms.ModelForm):
    """Pedido automático de reposición que activa el cliente (RF-18)."""

    class Meta:
        model = SuscripcionReposicion
        fields = ['producto', 'cantidad', 'periodicidad_dias', 'direccion', 'metodo_pago', 'proxima_fecha', 'activa']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'periodicidad_dias': forms.Select(attrs={'class': 'form-select'}),
            'direccion': forms.Select(attrs={'class': 'form-select'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-select'}),
            'proxima_fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'activa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, cliente=None, **kwargs):
        super().__init__(*args, **kwargs)
        from apps.logistica.services import botellon_por_defecto, fecha_estimada_para_direccion, productos_de_reparto
        self.fields['producto'].queryset = productos_de_reparto()
        self.fields['metodo_pago'].queryset = MetodoPago.objects.filter(
            activo=True, codigo__in=['EFECTIVO', 'TRANSFERENCIA', 'BILLETERA']
            + ([CODIGO_CUENTA_CORRIENTE] if cliente and cliente.permite_fiado else []))
        self.fields['metodo_pago'].empty_label = None
        self.fields['proxima_fecha'].label = 'Primer pedido'
        if cliente is not None:
            self.fields['direccion'].queryset = cliente.direcciones.all()
            self.fields['direccion'].empty_label = None
            if not self.instance.pk:
                principal = cliente.direcciones.filter(es_principal=True).first() or cliente.direcciones.first()
                defecto = botellon_por_defecto()
                self.initial.setdefault('direccion', getattr(principal, 'pk', None))
                self.initial.setdefault('producto', getattr(defecto, 'pk', None))
                self.initial.setdefault('cantidad', cliente.cantidad_recurrente_default or 2)
                self.initial.setdefault('proxima_fecha', fecha_estimada_para_direccion(principal) if principal else None)
                self.initial.setdefault('metodo_pago', MetodoPago.objects.filter(codigo='EFECTIVO').values_list('pk', flat=True).first())

    def clean_proxima_fecha(self):
        from django.utils import timezone
        fecha = self.cleaned_data['proxima_fecha']
        if fecha < timezone.localdate():
            raise forms.ValidationError('La fecha no puede ser anterior a hoy.')
        return fecha
