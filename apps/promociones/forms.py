from django import forms

from apps.pedidos.models import MetodoPago
from apps.productos.models import Producto

from .models import Promocion

_INPUT = 'form-control rounded-3'
_SELECT = 'form-select rounded-3'


class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ['nombre', 'producto', 'cant_paga', 'cant_lleva', 'precio', 'dias_validez', 'activa', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Ej: Paga 3, lleva 4 — Bidón 20 L'}),
            'producto': forms.Select(attrs={'class': _SELECT}),
            'cant_paga': forms.NumberInput(attrs={'class': _INPUT, 'min': 1}),
            'cant_lleva': forms.NumberInput(attrs={'class': _INPUT, 'min': 2}),
            'precio': forms.NumberInput(attrs={'class': _INPUT, 'step': '0.01', 'min': '0.01', 'inputmode': 'decimal'}),
            'dias_validez': forms.NumberInput(attrs={'class': _INPUT, 'min': 1}),
            'activa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descripcion': forms.Textarea(attrs={'class': _INPUT, 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.filter(activo=True, es_envase=False).order_by('nombre')
        self.fields['precio'].help_text = 'Si lo dejás vacío se calcula: unidades que paga × precio del producto.'
        self.fields['precio'].required = False

    def clean_cant_paga(self):
        return self._minimo_uno('cant_paga')

    def clean_dias_validez(self):
        return self._minimo_uno('dias_validez')

    def _minimo_uno(self, campo):
        valor = self.cleaned_data.get(campo)
        if valor is not None and valor < 1:
            raise forms.ValidationError('Debe ser al menos 1.')
        return valor

    def clean(self):
        # El precio vacío se calcula antes de la validación del modelo (que lo exige > 0).
        datos = self.cleaned_data
        if datos.get('precio') is None and datos.get('producto') and datos.get('cant_paga'):
            datos['precio'] = datos['producto'].precio * datos['cant_paga']
        if datos.get('precio') is None and 'precio' not in self.errors:
            self.add_error('precio', 'Indicá el precio del pack.')
        return super().clean()


class VenderPromocionForm(forms.Form):
    promocion = forms.ModelChoiceField(
        queryset=Promocion.objects.filter(activa=True).select_related('producto'),
        label='Promoción', widget=forms.Select(attrs={'class': _SELECT}),
    )
    metodo_pago = forms.ModelChoiceField(
        queryset=MetodoPago.objects.filter(activo=True), required=False,
        label='Medio de pago', widget=forms.Select(attrs={'class': _SELECT}),
    )
    a_cuenta = forms.BooleanField(
        required=False, label='Cargar a la cuenta corriente (fiado)',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
