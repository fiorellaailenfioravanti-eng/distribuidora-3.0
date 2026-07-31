from django import forms
from .models import Pedido, MetodoPago
from apps.clientes.models import DireccionEntrega


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
        if cliente:
            self.fields['direccion_entrega'].queryset = cliente.direcciones.all()
            # Si tiene direcciones, seleccionar la principal por defecto
            direccion_principal = cliente.direcciones.filter(es_principal=True).first()
            if direccion_principal and not self.is_bound:
                self.fields['direccion_entrega'].initial = direccion_principal.pk
            elif cliente.direcciones.exists() and not self.is_bound:
                self.fields['direccion_entrega'].initial = cliente.direcciones.first().pk
