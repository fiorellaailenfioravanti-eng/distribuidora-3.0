"""
Agrega el método de pago «Cuenta corriente (fiado)».

Lo usa el personal o el repartidor cuando un cliente con fiado no paga en el
momento: el pedido queda saldado y la deuda pasa a su cuenta corriente (RF-05 /
RF-13 / RF-14). No se ofrece en el checkout web.
"""
from django.db import migrations


def crear(apps, schema_editor):
    MetodoPago = apps.get_model('pedidos', 'MetodoPago')
    MetodoPago.objects.get_or_create(codigo='CUENTA', defaults={
        'nombre': 'Cuenta corriente (fiado)',
        'descripcion': 'La deuda pasa a la cuenta corriente del cliente. Sólo clientes con fiado.',
        'activo': True,
    })


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_suscripcion_reposicion'),
    ]

    operations = [
        migrations.RunPython(crear, migrations.RunPython.noop),
    ]
