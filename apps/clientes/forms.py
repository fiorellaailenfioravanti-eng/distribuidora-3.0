from django import forms

from apps.autenticacion.forms import RegistroUsuarioForm
from django.utils import timezone

from distribuidora.validadores import (
    ATTRS_ALTURA, ATTRS_COORDENADAS, ATTRS_DNI, ATTRS_TELEFONO, aplicar_attrs,
    validar_altura, validar_coordenadas, validar_dni, validar_fecha_no_futura, validar_telefono,
)
from .models import Cliente, TelefonoContacto, DireccionEntrega


_INPUT    = 'form-control'
_SELECT   = 'form-select'
_CHECK    = 'form-check-input'


class _ValidarDatosPersonalesMixin:
    """DNI con formato válido y único, y fecha de nacimiento no futura."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        aplicar_attrs(self, 'dni', ATTRS_DNI)
        aplicar_attrs(self, 'fecha_nacimiento', {'max': timezone.localdate().isoformat()})

    def clean_dni(self):
        dni = validar_dni(self.cleaned_data.get('dni'))
        if not dni:
            return None
        existentes = Cliente.objects.filter(dni=dni)
        if getattr(self, 'instance', None) is not None and isinstance(self.instance, Cliente) and self.instance.pk:
            existentes = existentes.exclude(pk=self.instance.pk)
        if existentes.exists():
            raise forms.ValidationError('Ya hay un cliente registrado con ese DNI.')
        return dni

    def clean_fecha_nacimiento(self):
        return validar_fecha_no_futura(self.cleaned_data.get('fecha_nacimiento'),
                                       'La fecha de nacimiento no puede ser futura.')


class AltaClienteConCuentaForm(_ValidarDatosPersonalesMixin, RegistroUsuarioForm):
    """
    Formulario para alta de cliente con cuenta web, integrando datos
    del Usuario (credenciales) y del Cliente (personales).
    """
    first_name = forms.CharField(label='Nombre', max_length=64, required=True, widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Nombre'}))
    last_name  = forms.CharField(label='Apellido', max_length=64, required=True, widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Apellido'}))
    dni        = forms.CharField(label='DNI', max_length=15, required=False, widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Ej: 30123456'}))
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': _INPUT}))
    tipo_cliente = forms.ChoiceField(label='Tipo de cliente', choices=[('Normal', 'Normal'), ('Premium', 'VIP / Premium')], widget=forms.Select(attrs={'class': _SELECT}))
    notas_internas = forms.CharField(label='Notas internas', required=False, max_length=500, widget=forms.Textarea(attrs={'class': _INPUT, 'rows': 3, 'placeholder': 'Notas internas...'}))
    # Los teléfonos se cargan con la lista dinámica de la pantalla del vendedor.
    relacion1 = None
    relacion2 = None

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


class ClienteForm(_ValidarDatosPersonalesMixin, forms.ModelForm):
    """Alta/edición de los datos de negocio del cliente (también el alta sin cuenta web)."""
    class Meta:
        model  = Cliente
        fields = ['nombre', 'apellido', 'email_contacto', 'dni',
                  'fecha_nacimiento', 'tipo_cliente', 'notas_internas']
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
            'notas_internas': forms.Textarea(attrs={
                'class': _INPUT,
                'rows': 3,
                'placeholder': 'Notas internas (solo visibles para Admin/Vendedor)...'
            }),
        }

    def clean(self):
        cleaned = super().clean()
        if not (cleaned.get('nombre') or '').strip() and not (cleaned.get('apellido') or '').strip():
            raise forms.ValidationError('Ingresá al menos el nombre o el apellido del cliente.')
        return cleaned


class ClienteSinCuentaForm(ClienteForm):
    """Alta de un cliente sin cuenta de acceso web (sólo Admin/Vendedor)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        self.fields['email_contacto'].widget.attrs['placeholder'] = 'email@ejemplo.com (opcional)'


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

    def __init__(self, *args, cliente=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.cliente = cliente or (self.instance.cliente if self.instance.cliente_id else None)
        aplicar_attrs(self, 'numero', ATTRS_TELEFONO)

    def clean_numero(self):
        numero = validar_telefono(self.cleaned_data.get('numero'), obligatorio=True)
        if self.cliente is not None:
            from distribuidora.validadores import solo_digitos
            digitos = solo_digitos(numero)
            repetido = any(solo_digitos(t.numero) == digitos
                           for t in self.cliente.telefonos.exclude(pk=self.instance.pk))
            if repetido:
                raise forms.ValidationError('El cliente ya tiene cargado ese número.')
        return numero


class DireccionEntregaForm(forms.ModelForm):
    """Agregar o editar una dirección de entrega."""
    class Meta:
        model  = DireccionEntrega
        fields = ['calle', 'altura', 'piso_depto', 'barrio', 'ciudad',
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
            'barrio': forms.Select(attrs={'class': _SELECT}),
            'ciudad': forms.TextInput(attrs={
                'class': _INPUT,
                'placeholder': 'Ej: Resistencia',
                'readonly': 'readonly'
            }),
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

    def __init__(self, *args, **kwargs):
        is_staff_or_admin = kwargs.pop('is_staff_or_admin', False)
        super().__init__(*args, **kwargs)

        if not self.is_bound and not self.instance.pk:
            self.initial['ciudad'] = 'Resistencia'
            self.initial['es_principal'] = True

        from apps.logistica.models import Barrio
        if 'barrio' in self.fields:
            self.fields['barrio'].queryset = Barrio.objects.filter(ciudad__icontains='Resistencia').order_by('nombre')
            self.fields['barrio'].required = True

        aplicar_attrs(self, 'altura', ATTRS_ALTURA)
        aplicar_attrs(self, 'coordenadas', ATTRS_COORDENADAS)

        # Sólo el personal carga la nota de seguridad del domicilio (RNF-02).
        if not is_staff_or_admin:
            self.fields.pop('desc_seguridad', None)

    def clean_altura(self):
        return validar_altura(self.cleaned_data.get('altura'))

    def clean_coordenadas(self):
        return validar_coordenadas(self.cleaned_data.get('coordenadas'))


class DireccionRegistroForm(DireccionEntregaForm):
    """Domicilio de entrega que el cliente carga al crear su cuenta (queda como principal)."""
    class Meta(DireccionEntregaForm.Meta):
        fields = ['calle', 'altura', 'piso_depto', 'barrio', 'ciudad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['barrio'].empty_label = '— Elegí tu barrio —'


class BuscarClienteForm(forms.Form):
    """Buscador del panel de clientes."""
    q = forms.CharField(
        required=False,
        max_length=100,
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


class EditarMiPerfilForm(forms.Form):
    """Formulario para que un cliente edite su foto y su teléfono principal."""
    celular = forms.CharField(
        label='Número de teléfono',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Ej: 11 1234-5678'})
    )
    imagen_perfil = forms.ImageField(
        label='Nueva foto de perfil',
        required=False,
        widget=forms.FileInput(attrs={'class': _INPUT})
    )
    eliminar_foto = forms.BooleanField(
        label='Eliminar foto actual',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': _CHECK})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        aplicar_attrs(self, 'celular', ATTRS_TELEFONO)

    def clean_celular(self):
        return validar_telefono(self.cleaned_data.get('celular'))


class MovimientoBidonForm(forms.Form):
    """Registro manual de envases desde la ficha del cliente (RF-08)."""
    TIPOS = [
        ('Devolucion', 'Devolución de vacíos'),
        ('Prestamo', 'Préstamo (entrega fuera de reparto)'),
        ('Venta', 'Envase vendido al cliente'),
        ('Ajuste', 'Ajuste manual (+/-)'),
    ]
    tipo = forms.ChoiceField(choices=TIPOS, label='Movimiento', widget=forms.Select(attrs={'class': _SELECT}))
    cantidad = forms.IntegerField(
        label='Cantidad',
        help_text='En los ajustes, negativo descuenta envases.',
        widget=forms.NumberInput(attrs={'class': _INPUT, 'placeholder': 'Ej: 2'}),
    )
    nota = forms.CharField(
        label='Nota', required=False, max_length=200,
        widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Opcional'}),
    )

    def clean(self):
        datos = super().clean()
        cantidad = datos.get('cantidad')
        if cantidad is None:
            return datos
        if datos.get('tipo') == 'Ajuste':
            if cantidad == 0:
                self.add_error('cantidad', 'El ajuste no puede ser cero.')
        elif cantidad <= 0:
            self.add_error('cantidad', 'La cantidad debe ser mayor a cero (el signo lo pone el tipo de movimiento).')
        if abs(cantidad) > 500:
            self.add_error('cantidad', 'La cantidad es demasiado grande; revisá el número.')
        return datos
