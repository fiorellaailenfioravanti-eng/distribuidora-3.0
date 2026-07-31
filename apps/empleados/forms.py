from django import forms
from .models import Empleado, RolEmpleado
from apps.autenticacion.models import Usuario

_INPUT = 'form-control'
_SELECT = 'form-select'
_CHECK = 'form-check-input'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'dni', 'celular', 'email', 'rol', 'activo', 'notas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': _INPUT}),
            'apellido': forms.TextInput(attrs={'class': _INPUT}),
            'dni': forms.TextInput(attrs={'class': _INPUT}),
            'celular': forms.TextInput(attrs={'class': _INPUT}),
            'email': forms.EmailInput(attrs={'class': _INPUT}),
            'rol': forms.Select(attrs={'class': _SELECT}),
            'activo': forms.CheckboxInput(attrs={'class': _CHECK}),
            'notas': forms.Textarea(attrs={'class': _INPUT, 'rows': 3}),
        }


    username = forms.CharField(
        required=False,
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Ej: juanperez'})
    )
    password = forms.CharField(
        required=False,
        label="Contraseña temporal",
        widget=forms.PasswordInput(attrs={'class': _INPUT})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filtro de roles por jerarquía
        if self.user and not self.user.is_superuser:
            # Administrador no puede asignar SuperUser
            self.fields['rol'].queryset = RolEmpleado.objects.exclude(nombre__iexact='SuperUser')

        # Si el empleado ya tiene un usuario vinculado, ocultamos los campos de creación
        if self.instance and self.instance.pk and self.instance.usuario:
            self.fields['username'].widget = forms.HiddenInput()
            self.fields['password'].widget = forms.HiddenInput()
        else:
            self.fields['email'].required = True

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not self.instance.pk or not self.instance.usuario:
            if not username:
                self.add_error('username', 'El nombre de usuario es obligatorio para crear la cuenta.')
            elif Usuario.objects.filter(username=username).exists():
                self.add_error('username', 'Este nombre de usuario ya está en uso.')
                
            if not email:
                self.add_error('email', 'El email es obligatorio para crear la cuenta de usuario.')
            elif Usuario.objects.filter(email=email).exists():
                self.add_error('email', 'Ya existe un usuario con este email.')
                
            if not password:
                self.add_error('password', 'La contraseña es obligatoria para crear la cuenta de usuario.')
                
        return cleaned_data

    def save(self, commit=True):
        empleado = super().save(commit=False)
        
        if not empleado.usuario:
            username = self.cleaned_data.get('username')
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            nombre = self.cleaned_data.get('nombre')
            apellido = self.cleaned_data.get('apellido')
            
            # Crear el usuario
            nuevo_usuario = Usuario(
                username=username,
                email=email,
                first_name=nombre,
                last_name=apellido
            )
            nuevo_usuario.set_password(password)
            nuevo_usuario._es_empleado = True  # Bandera para omitir la señal que crea Cliente
            nuevo_usuario.save()
            empleado.usuario = nuevo_usuario
            
        if commit:
            empleado.save()
            self.save_m2m()
            
        return empleado

class RolEmpleadoForm(forms.ModelForm):
    class Meta:
        model = RolEmpleado
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': _INPUT}),
            'descripcion': forms.Textarea(attrs={'class': _INPUT, 'rows': 3}),
        }
