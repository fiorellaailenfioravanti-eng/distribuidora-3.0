"""
Asigna `grupo_permisos` a los roles existentes y sincroniza los grupos de
los empleados que ya tienen usuario (auditoría H-25, decisión A-D3).

El mapeo por nombre se usa una sola vez, acá; de ahora en más el grupo se
elige explícitamente al crear o editar el rol.
"""
from django.db import migrations

GRUPOS_GESTIONADOS = ('Vendedor', 'Repartidor')


def _grupo_por_nombre(nombre):
    nombre = (nombre or '').lower()
    if 'repart' in nombre or 'chofer' in nombre:
        return 'Repartidor'
    if 'vend' in nombre or 'admin' in nombre or 'super' in nombre:
        return 'Vendedor'
    return ''


def asignar(apps, schema_editor):
    RolEmpleado = apps.get_model('empleados', 'RolEmpleado')
    Empleado = apps.get_model('empleados', 'Empleado')
    Group = apps.get_model('auth', 'Group')

    for rol in RolEmpleado.objects.all():
        rol.grupo_permisos = _grupo_por_nombre(rol.nombre)
        rol.save(update_fields=['grupo_permisos'])

    grupos = {g: Group.objects.get_or_create(name=g)[0] for g in GRUPOS_GESTIONADOS}
    for empleado in Empleado.objects.select_related('rol', 'usuario').exclude(usuario=None):
        usuario = empleado.usuario
        usuario.groups.remove(*grupos.values())
        if empleado.activo and empleado.rol.grupo_permisos:
            usuario.groups.add(grupos[empleado.rol.grupo_permisos])


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_rolempleado_grupo_permisos'),
        ('autenticacion', '0003_grupos_base'),
    ]

    operations = [
        migrations.RunPython(asignar, migrations.RunPython.noop),
    ]
