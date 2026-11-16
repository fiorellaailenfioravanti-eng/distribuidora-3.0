from django.db import models
from django.conf import settings
from distribuidora.bajas import SinEliminadosManager
from distribuidora.limites import LARGO_NOMBRE, LARGO_TEXTO, limite_largo

# Grupo de Django que otorga cada rol (decisión A-D3). El rol del empleado es
# la fuente de verdad en la UI y el grupo se sincroniza solo
# (`apps/permisos/signals.py`). Ningún rol otorga superusuario.
GRUPOS_PERMISOS_CHOICES = [
    ('', 'Sin acceso al panel'),
    ('Vendedor', 'Vendedor / Administración'),
    ('Repartidor', 'Repartidor'),
]

class RolEmpleado(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=LARGO_NOMBRE, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(max_length=LARGO_TEXTO, blank=True, verbose_name="Descripción")
    grupo_permisos = models.CharField(
        max_length=20,
        choices=GRUPOS_PERMISOS_CHOICES,
        blank=True,
        default='',
        verbose_name='Tipo de acceso',
        help_text='Base del rol: panel de administración, recorrido de reparto o sin acceso. '
                  'Lo que puede hacer en detalle se elige en «funciones».',
    )
    funciones = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='roles_empleado',
        limit_choices_to={'content_type__app_label': 'permisos', 'content_type__model': 'funcion'},
        verbose_name='Funciones',
        help_text='Qué puede hacer en el sistema un empleado con este rol.',
    )

    eliminado = models.BooleanField(default=False, verbose_name='Eliminado',
                                    help_text='Baja lógica: se oculta pero no se borra; se puede restaurar.')

    objects = SinEliminadosManager()
    todos = models.Manager()

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Rol de empleado'
        verbose_name_plural = 'Roles de empleado'
        constraints = limite_largo(nombre=LARGO_NOMBRE, descripcion=LARGO_TEXTO)

    def __str__(self):
        return self.nombre

    def codigos_funciones(self):
        return set(self.funciones.values_list('codename', flat=True))


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='perfil_empleado',
        verbose_name="Usuario"
    )
    nombre = models.CharField(max_length=LARGO_NOMBRE, verbose_name="Nombre")
    apellido = models.CharField(max_length=LARGO_NOMBRE, verbose_name="Apellido")
    dni = models.CharField(max_length=15, unique=True, verbose_name="DNI")
    celular = models.CharField(max_length=30, blank=True, verbose_name="Celular")
    email = models.EmailField(blank=True, verbose_name="Email")
    rol = models.ForeignKey(
        RolEmpleado,
        on_delete=models.PROTECT,
        related_name='empleados',
        verbose_name="Rol"
    )
    activo = models.BooleanField(default=True, verbose_name="Activo")
    eliminado = models.BooleanField(
        default=False, verbose_name="Eliminado",
        help_text="Baja lógica: deja de aparecer en la lista y no puede ingresar. "
                  "Se restaura desde «Empleados eliminados»; su historial se conserva.",
    )
    foto = models.ImageField(upload_to='empleados/', null=True, blank=True, verbose_name="Foto de perfil")
    notas = models.TextField(max_length=LARGO_TEXTO, blank=True, verbose_name="Notas")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        constraints = limite_largo(nombre=LARGO_NOMBRE, apellido=LARGO_NOMBRE, notas=LARGO_TEXTO)

    def nombre_completo(self):
        if self.usuario and self.usuario.get_full_name():
            return self.usuario.get_full_name()
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.nombre_completo()

    def iniciales(self):
        return f"{self.nombre[:1]}{self.apellido[:1]}".upper()

    def dar_de_baja(self):
        """Baja lógica: queda inactivo, oculto y sin acceso al sistema."""
        self.eliminado = True
        self.activo = False
        self.save(update_fields=['eliminado', 'activo'])
        if self.usuario is not None and not self.usuario.is_superuser:
            self.usuario.is_active = False
            self.usuario.save(update_fields=['is_active'])

    def restaurar(self):
        self.eliminado = False
        self.activo = True
        self.save(update_fields=['eliminado', 'activo'])
        if self.usuario is not None:
            self.usuario.is_active = True
            self.usuario.save(update_fields=['is_active'])
