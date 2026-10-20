"""
Crea los grupos base del sistema.

Corrige el hallazgo H-1: el grupo 'Vendedor' no existía en la base de datos,
por lo que `groups.filter(name='Vendedor').exists()` era False para todos los
usuarios y la rama Vendedor del sistema quedaba inaccesible salvo para el
superusuario. El grupo 'Repartidor' se creaba desde una señal `post_migrate`
en `apps/logistica/apps.py`, un mecanismo frágil que no participa del grafo de
dependencias de migraciones.

Esta migración solo crea los grupos. La asignación de permisos vive en
`apps/permisos/signals.py` (receptor `post_migrate`) porque Django crea las
filas de `auth_permission` en su propio `post_migrate`: dentro de una
migración todavía no existen y se omitirían en silencio.
"""

from django.db import migrations


def crear_grupos_base(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for nombre in ('Vendedor', 'Repartidor'):
        Group.objects.get_or_create(name=nombre)


def revertir_grupos_base(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Vendedor', 'Repartidor']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_usuario_celular1_usuario_celular2_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(crear_grupos_base, revertir_grupos_base),
    ]
