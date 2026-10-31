"""
El personal no compra en la tienda: elimina los perfiles de cliente vacíos
que quedaron asociados a usuarios de empleados (los creaba la señal de alta de
usuarios). Sólo borra perfiles sin pedidos, teléfonos, direcciones, envases,
movimientos de cuenta, abonos, promociones ni pedido automático.
"""
from django.db import migrations


def quitar(apps, schema_editor):
    Empleado = apps.get_model('empleados', 'Empleado')
    Cliente = apps.get_model('clientes', 'Cliente')
    Pedido = apps.get_model('pedidos', 'Pedido')
    MovimientoCuenta = apps.get_model('cuentas', 'MovimientoCuenta')
    Abono = apps.get_model('abonos', 'Abono')
    CompraPromocion = apps.get_model('promociones', 'CompraPromocion')
    SuscripcionReposicion = apps.get_model('pedidos', 'SuscripcionReposicion')
    MovimientoBidon = apps.get_model('clientes', 'MovimientoBidon')
    TelefonoContacto = apps.get_model('clientes', 'TelefonoContacto')
    DireccionEntrega = apps.get_model('clientes', 'DireccionEntrega')

    usuarios = Empleado.objects.exclude(usuario=None).values_list('usuario_id', flat=True)
    for cliente in Cliente.objects.filter(usuario_id__in=list(usuarios)):
        con_datos = any((
            Pedido.objects.filter(cliente=cliente).exists(),
            TelefonoContacto.objects.filter(cliente=cliente).exists(),
            DireccionEntrega.objects.filter(cliente=cliente).exists(),
            MovimientoBidon.objects.filter(cliente=cliente).exists(),
            MovimientoCuenta.objects.filter(cuenta__cliente=cliente).exists(),
            Abono.objects.filter(cliente=cliente).exists(),
            CompraPromocion.objects.filter(cliente=cliente).exists(),
            SuscripcionReposicion.objects.filter(cliente=cliente).exists(),
        ))
        if not con_datos:
            cliente.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_asignar_grupo_permisos'),
        ('clientes', '0010_saldo_inicial_bidones'),
        ('pedidos', '0006_metodo_cuenta_corriente'),
        ('cuentas', '0001_initial'),
        ('abonos', '0001_initial'),
        ('promociones', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(quitar, migrations.RunPython.noop),
    ]
