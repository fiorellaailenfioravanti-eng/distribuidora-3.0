"""
Marca como botellón de reparto los productos existentes que son bidones
(nombre que empieza con «bidón»/«bidones», sin ser envase) y les asocia el envase vacío
si no tenían uno, para que la carga del camión y el regreso los cuenten.
"""
import unicodedata

from django.db import migrations


def _normalizar(texto):
    texto = unicodedata.normalize('NFD', texto or '')
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn').lower()


def marcar(apps, schema_editor):
    Producto = apps.get_model('productos', 'Producto')
    envases = list(Producto.objects.filter(es_envase=True))
    envase_bidon = next((e for e in envases if 'bidon' in _normalizar(e.nombre)), envases[0] if envases else None)
    for producto in Producto.objects.filter(es_envase=False):
        if not _normalizar(producto.nombre).startswith('bidon'):  # Bidón / Bidones (no «Bomba para bidón»)
            continue
        producto.es_botellon = True
        producto.es_retornable = True
        if producto.envase_id is None and envase_bidon is not None:
            producto.envase = envase_bidon
        producto.save(update_fields=['es_botellon', 'es_retornable', 'envase'])


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_producto_es_botellon'),
    ]

    operations = [
        migrations.RunPython(marcar, migrations.RunPython.noop),
    ]
