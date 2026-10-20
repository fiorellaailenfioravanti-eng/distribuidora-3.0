from django import forms

from apps.clientes.models import Cliente
from apps.productos.models import Producto
from .models import Abono


_INPUT  = 'form-control'
_SELECT = 'form-select'


class AbonoForm(forms.ModelForm):
    class Meta:
        model  = Abono
        fields = ['cliente', 'producto', 'fecha_inicio', 'fecha_fin',
                  'costo_mensual', 'dia_facturacion', 'estado', 'observaciones']
        widgets = {
            'cliente': forms.Select(attrs={'class': _SELECT}),
            'producto': forms.Select(attrs={'class': _SELECT}),
            'fecha_inicio': forms.DateInput(attrs={'class': _INPUT, 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': _INPUT, 'type': 'date'}),
            'costo_mensual': forms.NumberInput(attrs={
                'class': _INPUT, 'step': '0.01', 'min': '0',
                'placeholder': '0.00',
            }),
            'dia_facturacion': forms.NumberInput(attrs={
                'class': _INPUT, 'min': 1, 'max': 28,
            }),
            'estado': forms.Select(attrs={'class': _SELECT}),
            'observaciones': forms.Textarea(attrs={
                'class': _INPUT,
                'rows': 3,
                'placeholder': 'Observaciones del contrato...',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['producto'].queryset = Producto.objects.filter(es_envase=False)
        self.fields['cliente'].label_from_instance = lambda c: c.nombre_completo()
        self.fields['producto'].label_from_instance = lambda p: f"{p.nombre} (${p.precio})"

    def clean(self):
        cleaned = super().clean()
        inicio = cleaned.get('fecha_inicio')
        fin = cleaned.get('fecha_fin')
        if inicio and fin and fin < inicio:
            raise forms.ValidationError('La fecha de fin no puede ser anterior al inicio.')
        return cleaned
