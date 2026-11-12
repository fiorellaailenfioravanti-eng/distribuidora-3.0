from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, UserCreationForm

from distribuidora.validadores import (
    ATTRS_NOMBRE, ATTRS_TELEFONO, aplicar_attrs, solo_digitos, validar_nombre, validar_telefono,
)
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    """Registro de cliente web.

    RF-01: exige dos celulares distintos y la relación de cada uno con el
    cliente ("Titular", "Esposa", "Hijo"...). Se guardan como
    `TelefonoContacto` mediante la señal de `apps.clientes` (H-40).
    """
    relacion1 = forms.CharField(
        max_length=100, label='Relación del celular 1',
        help_text='Ej: Titular', initial='Titular',
    )
    relacion2 = forms.CharField(
        max_length=100, label='Relación del celular 2',
        help_text='Ej: Esposa, Hijo, Trabajo',
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'celular1', 'celular2', 'imagen_perfil')

    field_order = ['username', 'email', 'password1', 'password2',
                   'celular1', 'relacion1', 'celular2', 'relacion2', 'imagen_perfil']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Las subclases que cargan los teléfonos de otra forma (alta por el
        # vendedor) no incluyen estos campos.
        for numero, nombre in enumerate(('celular1', 'celular2'), start=1):
            if nombre in self.fields:
                self.fields[nombre].required = True
                self.fields[nombre].label = f'Celular {numero}'
                aplicar_attrs(self, nombre, ATTRS_TELEFONO)

    def clean_email(self):
        email = (self.cleaned_data.get('email') or '').strip()
        if Usuario.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe una cuenta con ese email.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and Usuario.objects.filter(username__iexact=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ese nombre de usuario ya está en uso.')
        return username

    def clean_celular1(self):
        return validar_telefono(self.cleaned_data.get('celular1'))

    def clean_celular2(self):
        return validar_telefono(self.cleaned_data.get('celular2'))

    def clean(self):
        datos = super().clean()
        c1, c2 = solo_digitos(datos.get('celular1')), solo_digitos(datos.get('celular2'))
        if c1 and c1 == c2:
            self.add_error('celular2', 'Los dos celulares deben ser distintos.')
        return datos

    def save(self, commit=True):
        usuario = super().save(commit=False)
        # La señal post_save de clientes lee estas relaciones al crear los teléfonos.
        usuario._relacion_celular1 = (self.cleaned_data.get('relacion1') or '').strip()
        usuario._relacion_celular2 = (self.cleaned_data.get('relacion2') or '').strip()
        if commit:
            usuario.save()
            self.save_m2m()
        return usuario

class IngresarUsuarioForm(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario', 
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-3 py-2 px-3'})
    )
    password = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3 py-2 px-3'})
    )


class RecuperarContrasenaForm(PasswordResetForm):
    """Pide el email de la cuenta. Por seguridad no revela si el email existe."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Email de tu cuenta'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control rounded-3 py-2 px-3', 'placeholder': 'tu@email.com', 'autofocus': True,
        })


class NuevaContrasenaForm(SetPasswordForm):
    """Nueva contraseña desde el enlace del email (mismos validadores que el registro)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control rounded-3 py-2 px-3'


class PerfilUsuarioForm(forms.ModelForm):
    """Datos propios del personal (nombre, apellido, email y celular)."""

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'celular1')
        labels = {'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Email', 'celular1': 'Celular'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for nombre in ('first_name', 'last_name', 'email'):
            self.fields[nombre].required = True
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'
        aplicar_attrs(self, 'celular1', ATTRS_TELEFONO)
        aplicar_attrs(self, 'first_name', ATTRS_NOMBRE)
        aplicar_attrs(self, 'last_name', ATTRS_NOMBRE)

    def clean_first_name(self):
        return validar_nombre(self.cleaned_data.get('first_name'))

    def clean_last_name(self):
        return validar_nombre(self.cleaned_data.get('last_name'), 'El apellido')

    def clean_email(self):
        email = (self.cleaned_data.get('email') or '').strip()
        if Usuario.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe otra cuenta con ese email.')
        return email

    def clean_celular1(self):
        return validar_telefono(self.cleaned_data.get('celular1'))
