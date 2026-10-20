from django import forms


_INPUT = 'form-control'


class CargoCuentaForm(forms.Form):
    monto = forms.DecimalField(
        min_value=0.01,
        max_digits=12,
        decimal_places=2,
        label='Monto del cargo',
        widget=forms.NumberInput(attrs={
            'class': _INPUT,
            'step': '0.01',
            'min': '0.01',
            'placeholder': '0.00',
        }),
    )
    descripcion = forms.CharField(
        required=False,
        max_length=200,
        label='Descripción',
        widget=forms.TextInput(attrs={
            'class': _INPUT,
            'placeholder': 'Ej: Fiado de bidones, venta en cuenta...',
        }),
    )
    fecha_vencimiento = forms.DateField(
        required=False,
        label='Vencimiento (opcional)',
        widget=forms.DateInput(attrs={'class': _INPUT, 'type': 'date'}),
    )


class PagoCuentaForm(forms.Form):
    monto = forms.DecimalField(
        min_value=0.01,
        max_digits=12,
        decimal_places=2,
        label='Monto del pago',
        widget=forms.NumberInput(attrs={
            'class': _INPUT,
            'step': '0.01',
            'min': '0.01',
            'placeholder': '0.00',
        }),
    )
    descripcion = forms.CharField(
        required=False,
        max_length=200,
        label='Descripción',
        widget=forms.TextInput(attrs={
            'class': _INPUT,
            'placeholder': 'Ej: Pago parcial en efectivo',
        }),
    )
