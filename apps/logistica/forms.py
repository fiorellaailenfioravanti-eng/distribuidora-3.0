from django import forms
from .models import HojaRuta, DetalleHojaRuta, Zona, Camion, Empleado


class HojaRutaForm(forms.ModelForm):
    class Meta:
        model  = HojaRuta
        fields = ['fecha', 'empleado', 'camion', 'zona', 'estado', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'camion':   forms.Select(attrs={'class': 'form-select'}),
            'zona':     forms.Select(attrs={'class': 'form-select'}),
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
        fields = ['orden', 'cliente_nombre', 'direccion', 'pedido_ref']
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
            'direccion': forms.TextInput(attrs={
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
    class Meta:
        model  = Zona
        fields = ['nombre', 'descripcion', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Centro, Barrio Norte, Zona Industrial...'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Descripción opcional de la zona'
            }),
            'lunes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'martes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'miercoles': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'jueves': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'viernes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sabado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CamionForm(forms.ModelForm):
    class Meta:
        model  = Camion
        fields = ['patente', 'descripcion', 'activo']
        widgets = {
            'patente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: AB 123 CD'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del vehículo (marca, modelo, color...)'
            }),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
