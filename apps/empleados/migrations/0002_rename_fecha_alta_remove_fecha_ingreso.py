# Migración manual: renombrar fecha_alta → fecha_creacion y eliminar fecha_ingreso

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        # 1. Renombrar fecha_alta → fecha_creacion (preserva datos)
        migrations.RenameField(
            model_name='empleado',
            old_name='fecha_alta',
            new_name='fecha_creacion',
        ),
        # 2. Eliminar el campo fecha_ingreso
        migrations.RemoveField(
            model_name='empleado',
            name='fecha_ingreso',
        ),
        # 3. Actualizar verbose_name del campo renombrado
        migrations.AlterField(
            model_name='empleado',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
            preserve_default=True,
        ),
    ]
