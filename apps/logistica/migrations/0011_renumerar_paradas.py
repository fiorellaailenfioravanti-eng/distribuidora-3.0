"""
Deja el orden de las paradas de cada hoja en 1..n.

Antes el orden se cargaba a mano y las paradas agregadas desde las
sugerencias quedaban todas con 0. Ahora lo asigna el sistema; esta migración
renumera las hojas existentes respetando el orden que tenían.
"""
from django.db import migrations


def renumerar(apps, schema_editor):
    HojaRuta = apps.get_model('logistica', 'HojaRuta')
    DetalleHojaRuta = apps.get_model('logistica', 'DetalleHojaRuta')
    for hoja in HojaRuta.objects.all():
        paradas = DetalleHojaRuta.objects.filter(hoja_ruta=hoja).order_by('orden', 'id_detalle')
        for numero, parada in enumerate(paradas, start=1):
            if parada.orden != numero:
                DetalleHojaRuta.objects.filter(pk=parada.pk).update(orden=numero)


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0010_hojaruta_vacios_recibidos'),
    ]

    operations = [
        migrations.RunPython(renumerar, migrations.RunPython.noop),
    ]
