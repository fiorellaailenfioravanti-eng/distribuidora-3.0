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

    crear_usuario = forms.BooleanField(
        required=False,
        label="Crear cuenta de usuario para este empleado",
        widget=forms.CheckboxInput(attrs={'class': _CHECK})
    )
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
            self.fields['crear_usuario'].widget = forms.HiddenInput()
            self.fields['username'].widget = forms.HiddenInput()
            self.fields['password'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        crear_usuario = cleaned_data.get('crear_usuario')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if crear_usuario:
            if not username:
                self.add_error('username', 'El nombre de usuario es obligatorio para crear una cuenta.')
            elif Usuario.objects.filter(username=username).exists():
                self.add_error('username', 'Este nombre de usuario ya está en uso.')
                
            if not email:
                self.add_error('email', 'El email es obligatorio para crear una cuenta de usuario.')
            elif Usuario.objects.filter(email=email).exists():
                self.add_error('email', 'Ya existe un usuario con este email.')
                
            if not password:
                self.add_error('password', 'La contraseña es obligatoria para crear una cuenta de usuario.')
                
        return cleaned_data

    def save(self, commit=True):
        empleado = super().save(commit=False)
        crear_usuario = self.cleaned_data.get('crear_usuario')
        
        if crear_usuario and not empleado.usuario:
            username = self.cleaned_data.get('username')
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            nombre = self.cleaned_data.get('nombre')
            apellido = self.cleaned_data.get('apellido')
            
            # Crear el usuario
            nuevo_usuario = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=nombre,
                last_name=apellido
            )
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
