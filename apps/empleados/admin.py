from django.contrib import admin
from .models import RolEmpleado, Empleado

@admin.register(RolEmpleado)
class RolEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'dni', 'rol', 'activo', 'fecha_creacion')
    list_filter = ('rol', 'activo')
    search_fields = ('nombre', 'apellido', 'dni')
