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
    # Campos opcionales para Tarjeta de Crédito / Débito
    tarjeta_numero = forms.CharField(
        required=False,
        max_length=19,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-dark-subtle border-secondary text-white',
            'placeholder': '4500 1234 5678 9010',
            'id': 'inputTarjetaNumero'
        })
    )
    tarjeta_titular = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-dark-subtle border-secondary text-white',
            'placeholder': 'Como figura en la tarjeta',
            'id': 'inputTarjetaTitular'
        })
    )
    tarjeta_vencimiento = forms.CharField(
        required=False,
        max_length=7,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-dark-subtle border-secondary text-white',
            'placeholder': 'MM/AA',
            'id': 'inputTarjetaVencimiento'
        })
    )
    tarjeta_cvv = forms.CharField(
        required=False,
        max_length=4,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-dark-subtle border-secondary text-white',
            'placeholder': '123',
            'id': 'inputTarjetaCVV'
        })
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

            # Preseleccionar método de pago activo
            metodos_activos = self.fields['metodo_pago'].queryset
            if metodos_activos.count() == 1 and not self.is_bound:
                self.fields['metodo_pago'].initial = metodos_activos.first().pk
            else:
                ultimo_pedido = cliente.pedidos.first()
                if ultimo_pedido and ultimo_pedido.metodo_pago and not self.is_bound:
                    self.fields['metodo_pago'].initial = ultimo_pedido.metodo_pago.pk
