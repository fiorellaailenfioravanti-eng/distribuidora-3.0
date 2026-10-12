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


class DetalleRutaForm(forms.ModelForm):
    class Meta:
        model  = DetalleHojaRuta
        fields = ['orden', 'cliente_nombre', 'direccion_entrega', 'direccion_texto', 'pedido_ref']
        widgets = {
            'orden': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': 'Nro. de parada'
            }),
            'cliente_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del cliente'
            }),
            'direccion_entrega': forms.Select(attrs={'class': 'form-select'}),
            'direccion_texto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: San Martín 450, Barrio Norte'
            }),
            'pedido_ref': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Referencia de pedido (opcional)'
            }),
        }


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
