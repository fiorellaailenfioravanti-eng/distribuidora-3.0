"""Funciones por defecto de los roles y rol «Administrador».

- Crea los permisos de `apps/permisos/funciones.py` (normalmente los crea
  `post_migrate`, pero acá se necesitan antes de asignarlos).
- Cada rol existente recibe las funciones de su tipo de acceso
  (Vendedor → todas menos empleados; Repartidor → sólo el recorrido).
- Crea el rol «Administrador» con todas las funciones, si no existe.
"""
from django.db import migrations

from apps.permisos.funciones import FUNCIONES, POR_DEFECTO


def _permisos(apps):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    tipo, _ = ContentType.objects.get_or_create(app_label='permisos', model='funcion')
    permisos = {}
    for codigo, nombre in FUNCIONES:
        permiso, _ = Permission.objects.get_or_create(
            content_type=tipo, codename=codigo, defaults={'name': nombre})
        permisos[codigo] = permiso
    return permisos


def asignar(apps, schema_editor):
    permisos = _permisos(apps)
    RolEmpleado = apps.get_model('empleados', 'RolEmpleado')

    for rol in RolEmpleado.objects.all():
        base = 'Vendedor' if rol.grupo_permisos == 'Vendedor' else (
            'Repartidor' if rol.grupo_permisos == 'Repartidor' else None)
        if base and not rol.funciones.exists():
            rol.funciones.set([permisos[c] for c in POR_DEFECTO[base] if c in permisos])

    admin, creado = RolEmpleado.objects.get_or_create(
        nombre='Administrador',
        defaults={'grupo_permisos': 'Vendedor',
                  'descripcion': 'Acceso completo, incluida la gestión de empleados, roles y permisos.'},
    )
    if creado:
        admin.funciones.set(list(permisos.values()))


def quitar(apps, schema_editor):
    RolEmpleado = apps.get_model('empleados', 'RolEmpleado')
    for rol in RolEmpleado.objects.all():
        rol.funciones.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0006_roles_con_funciones'),
        ('permisos', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.RunPython(asignar, quitar),
    ]
