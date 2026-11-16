from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Empleado, RolEmpleado
from apps.autenticacion.models import Usuario
from distribuidora.validadores import (
    ATTRS_DNI, ATTRS_NOMBRE, ATTRS_TELEFONO, aplicar_attrs, validar_dni, validar_nombre, validar_telefono,
)

_INPUT = 'form-control'
_SELECT = 'form-select'
_CHECK = 'form-check-input'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['foto', 'nombre', 'apellido', 'dni', 'celular', 'email', 'rol', 'activo', 'notas']
        widgets = {
            'foto': forms.ClearableFileInput(attrs={'class': _INPUT, 'accept': 'image/*'}),
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
        aplicar_attrs(self, 'dni', ATTRS_DNI)
        aplicar_attrs(self, 'celular', ATTRS_TELEFONO)
        aplicar_attrs(self, 'nombre', ATTRS_NOMBRE)
        aplicar_attrs(self, 'apellido', ATTRS_NOMBRE)
        
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

    FOTO_MAX_MB = 3

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto and hasattr(foto, 'size') and foto.size > self.FOTO_MAX_MB * 1024 * 1024:
            raise ValidationError(f'La foto no puede pesar más de {self.FOTO_MAX_MB} MB.')
        return foto

    def clean_nombre(self):
        return validar_nombre(self.cleaned_data.get('nombre'))

    def clean_apellido(self):
        return validar_nombre(self.cleaned_data.get('apellido'), 'El apellido')

    def clean_dni(self):
        return validar_dni(self.cleaned_data.get('dni'))

    def clean_celular(self):
        return validar_telefono(self.cleaned_data.get('celular'))

    def clean(self):
        cleaned_data = super().clean()
        username = (cleaned_data.get('username') or '').strip()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not self.instance.pk or not self.instance.usuario:
            if not username:
                self.add_error('username', 'El nombre de usuario es obligatorio para crear la cuenta.')
            elif Usuario.objects.filter(username__iexact=username).exists():
                self.add_error('username', 'Este nombre de usuario ya está en uso.')
                
            if not email:
                self.add_error('email', 'El email es obligatorio para crear la cuenta de usuario.')
            elif Usuario.objects.filter(email__iexact=email).exists():
                self.add_error('email', 'Ya existe un usuario con este email.')
                
            if not password:
                self.add_error('password', 'La contraseña es obligatoria para crear la cuenta de usuario.')
            else:
                # RF-02: mismos validadores que el registro de clientes (H-36).
                usuario_tentativo = Usuario(
                    username=username or '', email=email or '',
                    first_name=cleaned_data.get('nombre') or '',
                    last_name=cleaned_data.get('apellido') or '',
                )
                try:
                    validate_password(password, user=usuario_tentativo)
                except ValidationError as error:
                    self.add_error('password', error)
                
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
    """Rol con sus funciones (checkboxes agrupados por área)."""

    funciones = forms.ModelMultipleChoiceField(
        queryset=None, required=False, widget=forms.CheckboxSelectMultiple,
        label='Qué puede hacer',
    )

    class Meta:
        model = RolEmpleado
        fields = ['nombre', 'descripcion', 'funciones']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Ej: Repartidor, Vendedor de mostrador'}),
            'descripcion': forms.Textarea(attrs={'class': _INPUT, 'rows': 2,
                                                 'placeholder': 'Para qué sirve este rol (opcional)'}),
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        from django.contrib.auth.models import Permission
        from apps.permisos.funciones import CODIGOS
        self.usuario = usuario
        permisos = Permission.objects.filter(content_type__app_label='permisos', codename__in=CODIGOS)
        self.fields['funciones'].queryset = permisos
        self.fields['funciones'].label_from_instance = lambda permiso: permiso.name
        self._codigo_por_pk = {p.pk: p.codename for p in permisos}

    def clean_nombre(self):
        nombre = ' '.join((self.cleaned_data.get('nombre') or '').split())
        otros = RolEmpleado.todos.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk)
        if otros.filter(eliminado=False).exists():
            raise forms.ValidationError('Ya existe un rol con ese nombre.')
        if otros.filter(eliminado=True).exists():
            raise forms.ValidationError('Hay un rol eliminado con ese nombre: restauralo desde «Roles eliminados».')
        return nombre

    def funciones_por_area(self):
        """[(área, [(código, checkbox), ...]), ...] en el orden del catálogo."""
        from apps.permisos.funciones import FUNCIONES_POR_AREA
        por_codigo = {self._codigo_por_pk.get(int(str(checkbox.data['value']))): checkbox
                      for checkbox in self['funciones']}
        return [(area, [(codigo, por_codigo[codigo]) for codigo, _ in funciones if codigo in por_codigo])
                for area, funciones in FUNCIONES_POR_AREA]

    def clean(self):
        datos = super().clean()
        codigos = {p.codename for p in datos.get('funciones') or []}
        # Nadie (salvo el superusuario) puede sacarse a sí mismo la gestión de empleados.
        usuario = self.usuario
        if (usuario is not None and not usuario.is_superuser and self.instance.pk
                and getattr(getattr(usuario, 'perfil_empleado', None), 'rol_id', None) == self.instance.pk
                and 'gestionar_empleados' not in codigos):
            self.add_error('funciones', 'No podés quitarle a tu propio rol la gestión de empleados: '
                                        'te quedarías sin acceso a esta pantalla.')
        return datos

    def save(self, commit=True):
        rol = super().save(commit=False)
        codigos = {p.codename for p in self.cleaned_data.get('funciones') or []}
        # El tipo de acceso se deduce de las funciones (lo usan el menú y los grupos de Django).
        rol.grupo_permisos = ('Vendedor' if 'ver_panel' in codigos
                              else 'Repartidor' if 'realizar_entregas' in codigos else '')
        if commit:
            rol.save()
            self.save_m2m()
            from apps.permisos.roles import sincronizar_grupo_empleado
            for empleado in rol.empleados.select_related('usuario'):
                sincronizar_grupo_empleado(empleado)
        return rol
