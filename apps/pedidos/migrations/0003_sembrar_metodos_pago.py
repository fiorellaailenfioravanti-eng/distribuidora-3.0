"""
Siembra el catálogo de métodos de pago y activa los que estaban inactivos.

Corrige los hallazgos H-12 y C-10:
  - `Pedido.metodo_pago` es obligatorio (`on_delete=PROTECT`, no admite null),
    así que sin filas en `MetodoPago` no se puede crear ningún pedido.
  - MERCADOPAGO y TARJETA estaban en `activo=0`.
  - El RF-13 del informe exige Efectivo, Transferencia, Tarjeta y Billetera
    Digital. Faltaban TRANSFERENCIA y BILLETERA.
"""

from django.db import migrations

METODOS = [
    {
        'codigo': 'EFECTIVO',
        'nombre': 'Efectivo en Entrega',
        'descripcion': 'El repartidor cobra en el momento de la entrega.',
        'activo': True,
    },
    {
        'codigo': 'MERCADOPAGO',
        'nombre': 'MercadoPago / Código QR',
        'descripcion': 'Pago online con billetera o código QR. Se confirma vía webhook.',
        'activo': True,
    },
    {
        'codigo': 'TARJETA',
        'nombre': 'Tarjeta de Crédito / Débito',
        'descripcion': 'Lectura de tarjeta en la entrega, cargada al pedido.',
        'activo': True,
    },
    {
        'codigo': 'TRANSFERENCIA',
        'nombre': 'Transferencia Bancaria',
        'descripcion': 'Transferencia previa; se verifica el comprobante antes de confirmar.',
        'activo': True,
    },
    {
        'codigo': 'BILLETERA',
        'nombre': 'Billetera Digital',
        'descripcion': 'Pago desde una billetera digital del cliente.',
        'activo': True,
    },
]


def sembrar_metodos_pago(apps, schema_editor):
    MetodoPago = apps.get_model('pedidos', 'MetodoPago')
    for datos in METODOS:
        MetodoPago.objects.update_or_create(
            codigo=datos['codigo'],
            defaults={
                'nombre': datos['nombre'],
                'descripcion': datos['descripcion'],
                'activo': datos['activo'],
            },
        )


def revertir_metodos_pago(apps, schema_editor):
    MetodoPago = apps.get_model('pedidos', 'MetodoPago')
    MetodoPago.objects.filter(
        codigo__in=[m['codigo'] for m in METODOS],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_pagopedido_tarjeta_titular_and_more'),
    ]

    operations = [
        migrations.RunPython(sembrar_metodos_pago, revertir_metodos_pago),
    ]
