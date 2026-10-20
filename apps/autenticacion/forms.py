from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

def _solo_digitos(numero):
    return ''.join(c for c in (numero or '') if c.isdigit())


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

    def clean(self):
        datos = super().clean()
        c1, c2 = _solo_digitos(datos.get('celular1')), _solo_digitos(datos.get('celular2'))
        for campo, digitos in (('celular1', c1), ('celular2', c2)):
            if datos.get(campo) and len(digitos) < 8:
                self.add_error(campo, 'Ingresá un número válido (al menos 8 dígitos).')
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