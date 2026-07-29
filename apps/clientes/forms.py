from django import forms
from .models import Cliente, TelefonoContacto, DireccionEntrega


_INPUT    = 'form-control'
_SELECT   = 'form-select'
_CHECK    = 'form-check-input'


class ClienteSinCuentaForm(forms.ModelForm):
    """
    Alta de un cliente sin cuenta de acceso web.
    Solo accesible para Admin/Vendedor.
    """
    class Meta:
        model  = Cliente
        fields = ['nombre', 'apellido', 'email_contacto', 'dni',
                  'fecha_nacimiento', 'tipo_cliente', 'notas_internas']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Nombre del cliente',
                'autofocus': True,
            }),
            'apellido': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Apellido del cliente',
            }),
            'email_contacto': forms.EmailInput(attrs={
                'class': _INPUT,
                'placeholder': 'email@ejemplo.com (opcional)',
            }),
            'dni': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Ej: 30123456'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': _INPUT
            }),
            'tipo_cliente': forms.Select(attrs={'class': _SELECT}),
            'notas_internas': forms.Textarea(attrs={
                'class': _INPUT,
                'rows': 3,
                'placeholder': 'Notas internas (Admin/Vendedor)...'
            }),
        }

    def clean(self):
        cleaned = super().clean()
        nombre   = cleaned.get('nombre', '').strip()
        apellido = cleaned.get('apellido', '').strip()
        if not nombre and not apellido:
            raise forms.ValidationError(
                'Ingresá al menos el nombre o el apellido del cliente.'
            )
        return cleaned


from apps.autenticacion.forms import RegistroUsuarioForm

class AltaClienteConCuentaForm(RegistroUsuarioForm):
    """
    Formulario para alta de cliente con cuenta web, integrando datos
    del Usuario (credenciales) y del Cliente (personales).
    """
    first_name = forms.CharField(label='Nombre', max_length=150, required=True, widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Nombre'}))
    last_name  = forms.CharField(label='Apellido', max_length=150, required=True, widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Apellido'}))
    dni        = forms.CharField(label='DNI', max_length=15, required=False, widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Ej: 30123456'}))
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': _INPUT}))
    tipo_cliente = forms.ChoiceField(label='Tipo de cliente', choices=[('Normal', 'Normal'), ('Premium', 'VIP / Premium')], widget=forms.Select(attrs={'class': _SELECT}))
    notas_internas = forms.CharField(label='Notas internas', required=False, widget=forms.Textarea(attrs={'class': _INPUT, 'rows': 3, 'placeholder': 'Notas internas...'}))
    
    class Meta(RegistroUsuarioForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        # password1/2 vienen de UserCreationForm, username/email etc.

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save() # Se dispara la señal post_save que crea el Cliente

            cliente = user.perfil_cliente
            cliente.dni = self.cleaned_data.get('dni')
            cliente.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
            cliente.tipo_cliente = self.cleaned_data.get('tipo_cliente')
            cliente.notas_internas = self.cleaned_data.get('notas_internas')
            cliente.save()
        return user


class ClienteForm(forms.ModelForm):
    """Formulario de alta/edición de datos de negocio del cliente."""
    class Meta:
        model  = Cliente
        fields = ['nombre', 'apellido', 'email_contacto', 'dni',
                  'fecha_nacimiento', 'tipo_cliente', 'bidones_prestados', 'notas_internas']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Apellido'
            }),
            'email_contacto': forms.EmailInput(attrs={
                'class': _INPUT,
                'placeholder': 'Email de contacto (opcional)'
            }),
            'dni': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Ej: 30123456'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': _INPUT
            }),
            'tipo_cliente': forms.Select(attrs={'class': _SELECT}),
            'bidones_prestados': forms.NumberInput(attrs={
                'class': _INPUT,
                'min': 0
            }),
            'notas_internas': forms.Textarea(attrs={
                'class': _INPUT,
                'rows': 3,
                'placeholder': 'Notas internas (solo visibles para Admin/Vendedor)...'
            }),
        }


class TelefonoContactoForm(forms.ModelForm):
    """Agregar o editar un teléfono de contacto."""
    class Meta:
        model  = TelefonoContacto
        fields = ['numero', 'desc_relacion', 'es_principal']
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Ej: 3644 123456'
            }),
            'desc_relacion': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Ej: Titular, Cónyuge, Hijo, Vecino...'
            }),
            'es_principal': forms.CheckboxInput(attrs={'class': _CHECK}),
        }


class DireccionEntregaForm(forms.ModelForm):
    """Agregar o editar una dirección de entrega."""
    class Meta:
        model  = DireccionEntrega
        fields = ['calle', 'altura', 'piso_depto', 'zona',
                  'desc_seguridad', 'coordenadas', 'es_principal']
        widgets = {
            'calle': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Nombre de la calle'
            }),
            'altura': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Ej: 450'
            }),
            'piso_depto': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Ej: 2°B, PB derecha (opcional)'
            }),
            'zona': forms.Select(attrs={'class': _SELECT}),
            'desc_seguridad': forms.Textarea(attrs={
                'class': _INPUT,
                'rows': 2,
                'placeholder': 'Ej: Deja el portón abierto. Timbre no funciona.'
            }),
            'coordenadas': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'lat,lng (opcional)'
            }),
            'es_principal': forms.CheckboxInput(attrs={'class': _CHECK}),
        }


class BuscarClienteForm(forms.Form):
    """Buscador del panel de clientes."""
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': _INPUT,
            'placeholder': 'Buscar por nombre, usuario, email o DNI...',
            'autofocus': True,
        })
    )
    tipo = forms.ChoiceField(
        required=False,
        choices=[('', '— Todos —'), ('Normal', 'Normal'), ('Premium', 'Premium')],
        widget=forms.Select(attrs={'class': _SELECT})
    )
