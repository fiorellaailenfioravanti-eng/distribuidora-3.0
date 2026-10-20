"""
RF-08: convierte el saldo manual `bidones_prestados` en un movimiento inicial
(`Ajuste`) del historial, para que el saldo pase a ser la suma de movimientos
sin perder el dato que ya estaba cargado.
"""
from django.db import migrations


def crear_saldo_inicial(apps, schema_editor):
    Cliente = apps.get_model('clientes', 'Cliente')
    MovimientoBidon = apps.get_model('clientes', 'MovimientoBidon')
    for cliente in Cliente.objects.exclude(bidones_prestados=0):
        if not MovimientoBidon.objects.filter(cliente=cliente).exists():
            MovimientoBidon.objects.create(
                cliente=cliente,
                tipo='Ajuste',
                cantidad=cliente.bidones_prestados,
                nota='Saldo inicial migrado del contador manual',
            )


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_movimiento_bidon'),
    ]

    operations = [
        migrations.RunPython(crear_saldo_inicial, migrations.RunPython.noop),
    ]
