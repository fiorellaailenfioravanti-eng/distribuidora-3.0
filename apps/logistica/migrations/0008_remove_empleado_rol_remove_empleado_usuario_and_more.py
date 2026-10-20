"""
Elimina los modelos `Empleado` y `RolEmpleado` duplicados de `apps.logistica`.

Corrige los hallazgos H-2 y H-3. Antes de esta migración el proyecto tenía
cuatro tablas de personal:

    empleados_empleado        (1 fila)   ← la que se usaba en el panel
    empleados_rolempleado     (3 filas)
    logistica_empleado        (0 filas)  ← la que usaba HojaRuta
    logistica_rolempleado     (0 filas)

`apps.empleados` queda como fuente única: concentra nombre, apellido, DNI,
celular y email. El duplicado de logística solo tenía `usuario`, `rol` y
`activo`, y al estar vacío dejaba el selector de repartidor de `HojaRutaForm`
sin opciones, por lo que no se podía crear ninguna hoja de ruta.

Orden de las operaciones: primero se reapuntan las claves foráneas, después se
eliminan los campos del modelo huérfano y por último las tablas. Al revés,
SQLite no podría reconstruir las tablas referenciantes.

Los datos se copiaron previamente en la migración 0005; aquí se verifica que la
tabla duplicada esté vacía antes de borrarla, para no perder información.
"""

import django.db.models.deletion
from django.db import migrations, models


def verificar_que_no_haya_datos_pendientes(apps, schema_editor):
    """
    Salvaguarda: si la tabla duplicada tuviera filas sin copiar, se aborta la
    migración en lugar de destruirlas silenciosamente.
    """
    EmpleadoLogistica = apps.get_model('logistica', 'Empleado')
    RolLogistica = apps.get_model('logistica', 'RolEmpleado')

    empleados = EmpleadoLogistica.objects.count()
    roles = RolLogistica.objects.count()

    if empleados or roles:
        raise RuntimeError(
            f'logistica_empleado tiene {empleados} filas y '
            f'logistica_rolempleado tiene {roles}. '
            'La migración 0005 debería haberlas copiado a apps.empleados. '
            'Revisar antes de continuar: se aborta para no perder datos.'
        )


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0007_alter_hojaruta_empleado'),
        ('empleados', '0002_rename_fecha_alta_remove_fecha_ingreso'),
    ]

    operations = [
        # 1) Reapuntar las claves foráneas al modelo canónico.
        migrations.AlterField(
            model_name='hojaruta',
            name='empleado',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='hojas_ruta',
                to='empleados.empleado',
            ),
        ),
        migrations.AlterField(
            model_name='rutareparto',
            name='empleado_default',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='rutas_default',
                to='empleados.empleado',
            ),
        ),
        # 2) Confirmar que no quede nada por copiar.
        migrations.RunPython(
            verificar_que_no_haya_datos_pendientes,
            migrations.RunPython.noop,
        ),
        # 3) Eliminar los campos del modelo huérfano y sus tablas.
        migrations.RemoveField(
            model_name='empleado',
            name='rol',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='activo',
        ),
        migrations.DeleteModel(
            name='RolEmpleado',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]
