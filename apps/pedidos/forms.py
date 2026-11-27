from django import forms
from django.core.validators import FileExtensionValidator
from .models import CODIGO_CUENTA_CORRIENTE, MetodoPago, Pedido, SuscripcionReposicion
from apps.clientes.models import DireccionEntrega, TelefonoContacto


def _etiqueta_direccion_con_fecha(direccion):
    """Texto de la dirección con la fecha estimada de entrega de su zona (RF-16/3E)."""
    from apps.logistica.services import fecha_estimada_para_direccion
    etiqueta = str(direccion)
    fecha = fecha_estimada_para_direccion(direccion)
    if fecha:
        etiqueta += f' — entrega estimada: {fecha:%d/%m/%Y}'
    return etiqueta


# Métodos que se ofrecen en el checkout web: efectivo al recibir o
# transferencia con comprobante. La tarjeta se cobra con posnet al entregar
# (decisión A-D1: el sistema no procesa datos de tarjetas) y la cuenta
# corriente, MercadoPago y billetera quedan para el personal.
CODIGOS_CHECKOUT_WEB = ('EFECTIVO', 'TRANSFERENCIA')
CODIGO_TRANSFERENCIA = 'TRANSFERENCIA'

# Comprobante de transferencia: imagen o PDF, hasta 5 MB.
EXTENSIONES_COMPROBANTE = ['jpg', 'jpeg', 'png', 'webp', 'pdf']
TAMANO_MAXIMO_COMPROBANTE = 5 * 1024 * 1024

# Nombre corto con el que se muestra cada método en el checkout.
NOMBRES_CHECKOUT = {'TRANSFERENCIA': 'Transferencia'}


def metodos_pago_checkout_web():
    """Métodos activos ofrecidos al cliente en la web."""
    return MetodoPago.objects.filter(activo=True, codigo__in=CODIGOS_CHECKOUT_WEB).order_by('id_metodo')


class CheckoutForm(forms.Form):
    direccion_entrega = forms.ModelChoiceField(
        queryset=DireccionEntrega.objects.none(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None,
        required=True,
        label="Dirección de entrega"
    )
    telefonos_contacto = forms.ModelMultipleChoiceField(
        queryset=TelefonoContacto.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True,
        label='Teléfonos de contacto',
        error_messages={'required': 'Marcá al menos un teléfono al que podamos llamarte.'},
    )
    metodo_pago = forms.ModelChoiceField(
        queryset=MetodoPago.objects.filter(activo=True),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None,
        required=True,
        label="Método de Pago"
    )
    notas_cliente = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ej: Timbre no funciona, dejar con el encargado o llamar antes de llegar...'
        }),
        required=False,
        label="Indicaciones de entrega (opcional)"
    )
    comprobante = forms.FileField(
        required=False,
        label='Comprobante de la transferencia',
        validators=[FileExtensionValidator(EXTENSIONES_COMPROBANTE,
                                           message='Subí una imagen (JPG, PNG o WEBP) o un PDF.')],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*,.pdf'}),
        help_text='Imagen o PDF, hasta 5 MB.',
    )

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)
        self.fields['direccion_entrega'].label_from_instance = _etiqueta_direccion_con_fecha
        self.fields['metodo_pago'].queryset = metodos_pago_checkout_web()
        self.fields['metodo_pago'].label_from_instance = lambda m: NOMBRES_CHECKOUT.get(m.codigo, m.nombre)
        self.fields['telefonos_contacto'].label_from_instance = (
            lambda t: f'{t.numero} — {t.desc_relacion}' if t.desc_relacion else t.numero)
        if cliente:
            self.fields['direccion_entrega'].queryset = cliente.direcciones.all()
            # Teléfonos: por defecto los del último pedido que sigan vigentes; si no, el principal.
            telefonos = cliente.telefonos.all()
            self.fields['telefonos_contacto'].queryset = telefonos
            if not self.is_bound and telefonos.exists():
                ultimo = cliente.pedidos.first()
                anteriores = list(ultimo.telefonos_contacto.filter(pk__in=telefonos)) if ultimo else []
                self.fields['telefonos_contacto'].initial = [t.pk for t in anteriores] or [telefonos.first().pk]
            # Si tiene direcciones, seleccionar la principal por defecto
            direccion_principal = cliente.direcciones.filter(es_principal=True).first()
            if direccion_principal and not self.is_bound:
                self.fields['direccion_entrega'].initial = direccion_principal.pk
            elif cliente.direcciones.exists() and not self.is_bound:
                self.fields['direccion_entrega'].initial = cliente.direcciones.first().pk

            # Preseleccionar método de pago activo
            # (el del último pedido si se ofrece en la web; si no, efectivo o el primero).
            metodos_activos = self.fields['metodo_pago'].queryset
            if not self.is_bound and metodos_activos.exists():
                ultimo_pedido = cliente.pedidos.first()
                ofrecidos = set(metodos_activos.values_list('pk', flat=True))
                if ultimo_pedido and ultimo_pedido.metodo_pago_id in ofrecidos:
                    inicial = ultimo_pedido.metodo_pago_id
                else:
                    efectivo = metodos_activos.filter(codigo='EFECTIVO').first()
                    inicial = (efectivo or metodos_activos.first()).pk
                self.fields['metodo_pago'].initial = inicial


    def clean_comprobante(self):
        archivo = self.cleaned_data.get('comprobante')
        if archivo and archivo.size > TAMANO_MAXIMO_COMPROBANTE:
            raise forms.ValidationError('El comprobante supera los 5 MB.')
        return archivo

    def clean(self):
        datos = super().clean()
        metodo = datos.get('metodo_pago')
        if metodo and metodo.codigo == CODIGO_TRANSFERENCIA and not datos.get('comprobante'):
            if 'comprobante' not in self.errors:
                self.add_error('comprobante', 'Para pagar por transferencia tenés que subir el comprobante.')
        elif metodo and metodo.codigo != CODIGO_TRANSFERENCIA:
            datos['comprobante'] = None  # sólo se guarda con transferencia
        return datos


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
        from django.utils import timezone
        self.fields['proxima_fecha'].widget.attrs['min'] = timezone.localdate().isoformat()
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
