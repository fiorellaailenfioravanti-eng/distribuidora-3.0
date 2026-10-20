from django import forms
from .models import (
    HojaRuta, DetalleHojaRuta, Zona, Camion, Empleado, RutaReparto, Barrio,
    DIA_SEMANA_CHOICES,
)
from apps.pedidos.models import MetodoPago


class HojaRutaForm(forms.ModelForm):
    class Meta:
        model  = HojaRuta
        fields = ['fecha', 'ruta_reparto', 'empleado', 'camion', 'estado', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'ruta_reparto': forms.Select(attrs={'class': 'form-select'}),
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'camion':   forms.Select(attrs={'class': 'form-select'}),
            'estado':   forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones generales de la ruta...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Solo empleados activos
        self.fields['empleado'].queryset = Empleado.objects.filter(activo=True).select_related('usuario', 'rol')
        # Solo camiones activos
        self.fields['camion'].queryset = Camion.objects.filter(activo=True)


def _etiqueta_direccion_cliente(direccion):
    barrio = f' (B° {direccion.barrio.nombre})' if direccion.barrio_id else ''
    return f'{direccion.cliente.nombre_completo()} — {direccion.calle} {direccion.altura}{barrio}'


class AgregarParadaForm(forms.Form):
    """Alta manual de una parada con su pedido de botellones.

    O se elige un cliente existente (por su domicilio) o se carga uno nuevo:
    en ese caso el nombre y la dirección son obligatorios. El orden de la
    parada lo pone el sistema.
    """
    direccion = forms.ModelChoiceField(
        queryset=None, required=False, label='Cliente existente',
        empty_label='— Cliente nuevo —', widget=forms.Select(attrs={'class': 'form-select'}),
    )
    nombre = forms.CharField(required=False, max_length=100, label='Nombre',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre o razón social'}))
    apellido = forms.CharField(required=False, max_length=100, label='Apellido',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido (opcional)'}))
    calle = forms.CharField(required=False, max_length=150, label='Calle',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: San Martín'}))
    altura = forms.CharField(required=False, max_length=20, label='Altura',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 450'}))
    barrio = forms.ModelChoiceField(queryset=None, required=False, label='Barrio',
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    producto = forms.ModelChoiceField(queryset=None, label='Botellón', empty_label=None,
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    cantidad = forms.IntegerField(min_value=1, initial=1, label='Cantidad',
                                  widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}))

    def __init__(self, *args, hoja=None, **kwargs):
        super().__init__(*args, **kwargs)
        from apps.clientes.models import DireccionEntrega
        from .services import botellon_por_defecto, productos_de_reparto

        direcciones = DireccionEntrega.objects.select_related('cliente', 'barrio').order_by(
            'cliente__apellido', 'cliente__nombre')
        barrios = Barrio.objects.order_by('nombre')
        if hoja is not None and hoja.zona_id:
            direcciones = direcciones.filter(barrio__zona=hoja.zona)
            barrios = barrios.filter(zona=hoja.zona)
        self.fields['direccion'].queryset = direcciones
        self.fields['direccion'].label_from_instance = _etiqueta_direccion_cliente
        self.fields['barrio'].queryset = barrios
        self.fields['producto'].queryset = productos_de_reparto()
        defecto = botellon_por_defecto()
        if defecto is not None:
            self.fields['producto'].initial = defecto.pk

    def clean(self):
        datos = super().clean()
        if datos.get('direccion'):
            return datos
        for campo, mensaje in (('nombre', 'El nombre del cliente es obligatorio.'),
                               ('calle', 'La calle es obligatoria.'),
                               ('altura', 'La altura es obligatoria (o S/N).'),
                               ('barrio', 'Elegí el barrio.')):
            if not datos.get(campo):
                self.add_error(campo, mensaje)
        return datos


class ActualizarEstadoForm(forms.ModelForm):
    """Formulario mínimo para que el repartidor actualice el estado de una entrega."""
    envases_retirados = forms.IntegerField(
        min_value=0, required=False, initial=0, label='Envases retirados (vacíos)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    envases_vendidos = forms.IntegerField(
        min_value=0, required=False, initial=0, label='Envases vendidos (no devueltos)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    monto_cobrado = forms.DecimalField(
        min_value=0, required=False, max_digits=12, decimal_places=2,
        label='Monto cobrado (opcional)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    metodo_pago = forms.ModelChoiceField(
        queryset=MetodoPago.objects.filter(activo=True), required=False,
        label='Método de pago',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model  = DetalleHojaRuta
        fields = ['estado', 'nota_entrega']
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'nota_entrega': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Nota opcional (ej: no había nadie, dejé con vecino...)'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # El repartidor no puede volver a "Pendiente" una vez que actúa
        self.fields['estado'].choices = [
            ('Entregado',    'Entregado ✅'),
            ('Cancelado',    'Cancelado ❌'),
            ('Reprogramado', 'Reprogramado 🔄'),
        ]


class ZonaForm(forms.ModelForm):
    dias_reparto = forms.MultipleChoiceField(
        choices=DIA_SEMANA_CHOICES,
        required=False,
        label='Días de reparto',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model  = Zona
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Zona 1, Zona Centro, Zona Norte...'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Descripción opcional de la zona o referencias de entrega'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['dias_reparto'].initial = self.instance.get_dias_reparto()

    def save(self, commit=True):
        zona = super().save(commit=False)
        zona.set_dias_reparto(self.cleaned_data.get('dias_reparto') or [])
        if commit:
            zona.save()
            self.save_m2m()
        return zona


class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'ciudad', 'zona']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'zona': forms.Select(attrs={'class': 'form-select'}),
        }


class RutaRepartoForm(forms.ModelForm):
    class Meta:
        model = RutaReparto
        fields = ['nombre', 'zona', 'dia_semana', 'empleado_default', 'camion_default']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'zona': forms.Select(attrs={'class': 'form-select'}),
            'dia_semana': forms.Select(attrs={'class': 'form-select'}),
            'empleado_default': forms.Select(attrs={'class': 'form-select'}),
            'camion_default': forms.Select(attrs={'class': 'form-select'}),
        }


class CamionForm(forms.ModelForm):
    class Meta:
        model  = Camion
        fields = ['patente', 'descripcion', 'capacidad_botellones', 'activo']
        widgets = {
            'patente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: AB 123 CD'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del vehículo (marca, modelo, color...)'
            }),
            'capacidad_botellones': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
