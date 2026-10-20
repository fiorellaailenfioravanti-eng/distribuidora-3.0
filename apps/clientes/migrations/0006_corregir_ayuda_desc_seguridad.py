"""
Corrige la etiqueta del requerimiento en la nota de seguridad.

La nota de acceso al domicilio no es "RF-03" (que es multidirección), sino
**RNF-02** (ocultación de información sensible). El error de etiquetado se
había propagado a los `help_text`, a los comentarios del código y a los
templates, lo que llevaba a la tesis a mostrar el control de privacidad como un
requerimiento funcional.
"""

from django.db import migrations, models

AYUDA_VIEJA = (
    'SOLO visible para Admin, Vendedor y Repartidor asignado - RF-03'
)
AYUDA_NUEVA = (
    'Información sensible: visible solo para Admin, Vendedor y el Repartidor '
    'asignado a esa dirección (RNF-02).'
)


def corregir_ayuda_desc_seguridad(apps, schema_editor):
    DireccionEntrega = apps.get_model('clientes', 'DireccionEntrega')
    for direccion in DireccionEntrega.objects.filter(desc_seguridad=AYUDA_VIEJA):
        direccion.desc_seguridad = AYUDA_NUEVA
        direccion.save(update_fields=['desc_seguridad'])


def revertir_ayuda_desc_seguridad(apps, schema_editor):
    DireccionEntrega = apps.get_model('clientes', 'DireccionEntrega')
    for direccion in DireccionEntrega.objects.filter(desc_seguridad=AYUDA_NUEVA):
        direccion.desc_seguridad = AYUDA_VIEJA
        direccion.save(update_fields=['desc_seguridad'])


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_alter_direccionentrega_barrio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionentrega',
            name='desc_seguridad',
            field=models.TextField(
                blank=True,
                help_text=AYUDA_NUEVA,
                verbose_name='Nota de seguridad',
            ),
        ),
        migrations.RunPython(
            corregir_ayuda_desc_seguridad,
            revertir_ayuda_desc_seguridad,
        ),
    ]
