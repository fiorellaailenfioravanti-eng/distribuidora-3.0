from django.db import models
from django.conf import settings

class RolEmpleado(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Rol de empleado'
        verbose_name_plural = 'Roles de empleado'

    def __str__(self):
        return self.nombre

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
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
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
    notas = models.TextField(blank=True, verbose_name="Notas")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def nombre_completo(self):
        if self.usuario and self.usuario.get_full_name():
            return self.usuario.get_full_name()
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.nombre_completo()
