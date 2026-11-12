"""Bidones que se recargan en planta y rol «Recargador».

Catálogo (sólo crea lo que falta; no pisa productos existentes):
- «Bidón 20 L agua de mesa» pasa a «Bidón 20 L primera marca» (conserva stock y pedidos).
- Crea «Bidón 20 L segunda marca», «Bidón 10 L primera marca», «Bidón 10 L segunda marca»
  y el «Envase bidón 10 L». Los de 20 L usan el «Envase bidón 20 L».
  Los precios nuevos son de referencia: ajustarlos en Productos.

Permisos: crea `registrar_recargas` y `ver_stock_bidones`; el Administrador recibe
las dos, el Vendedor sólo ver el stock y se crea el rol «Recargador».
"""
from decimal import Decimal

from django.db import migrations

ENVASE_20 = 'Envase bidón 20 L'
ENVASE_10 = 'Envase bidón 10 L'
BIDONES = [
    # (nombre, envase, precio de referencia, descripción)
    ('Bidón 20 L primera marca', ENVASE_20, None, None),
    ('Bidón 20 L segunda marca', ENVASE_20, Decimal('2600'), 'Bidón retornable de 20 litros, segunda marca.'),
    ('Bidón 10 L primera marca', ENVASE_10, Decimal('2000'), 'Bidón retornable de 10 litros, primera marca.'),
    ('Bidón 10 L segunda marca', ENVASE_10, Decimal('1600'), 'Bidón retornable de 10 litros, segunda marca.'),
]
FUNCIONES_NUEVAS = [
    ('registrar_recargas', 'Registrar la recarga diaria de bidones'),
    ('ver_stock_bidones', 'Ver el stock de bidones llenos y vacíos'),
]


def preparar(apps, schema_editor):
    Producto = apps.get_model('productos', 'Producto')
    Categoria = apps.get_model('productos', 'Categoria')
    # Sólo en bases que ya tienen el catálogo de bidones; una instalación nueva
    # los crea con `seed_demo` (o a mano) y no recibe productos con precios estimados.
    if Producto.objects.filter(nombre__in=['Bidón 20 L agua de mesa', 'Bidón 20 L primera marca']).exists():
        _catalogo(Producto, Categoria)
    _permisos_y_roles(apps)


def _catalogo(Producto, Categoria):
    agua = Categoria.objects.filter(nombre='Agua en bidones').first()
    envases_cat = Categoria.objects.filter(nombre='Envases').first()

    envase_20 = Producto.objects.filter(nombre=ENVASE_20).first()
    if envase_20 is None:
        envase_20 = Producto.objects.create(
            nombre=ENVASE_20, descripcion='Envase retornable de 20 litros.', precio=Decimal('9500'),
            stock=0, es_envase=True, es_retornable=True)
        if envases_cat:
            envase_20.categoria.add(envases_cat)
    envase_10 = Producto.objects.filter(nombre=ENVASE_10).first()
    if envase_10 is None:
        envase_10 = Producto.objects.create(
            nombre=ENVASE_10, descripcion='Envase retornable de 10 litros.', precio=Decimal('6000'),
            stock=0, es_envase=True, es_retornable=True)
        if envases_cat:
            envase_10.categoria.add(envases_cat)
    envase = {ENVASE_20: envase_20, ENVASE_10: envase_10}

    # El 20 L de mesa existente es el de primera marca (conserva stock, pedidos y precio).
    if not Producto.objects.filter(nombre='Bidón 20 L primera marca').exists():
        Producto.objects.filter(nombre='Bidón 20 L agua de mesa').update(nombre='Bidón 20 L primera marca')

    for nombre, envase_nombre, precio, descripcion in BIDONES:
        bidon = Producto.objects.filter(nombre=nombre).first()
        if bidon is None:
            bidon = Producto.objects.create(
                nombre=nombre, descripcion=descripcion or '', precio=precio or Decimal('3200'), stock=0,
                es_botellon=True, es_retornable=True, envase=envase[envase_nombre])
            if agua:
                bidon.categoria.add(agua)
        bidon.es_recargable = True
        bidon.es_botellon = True
        bidon.envase = envase[envase_nombre]
        bidon.save(update_fields=['es_recargable', 'es_botellon', 'envase'])



def _permisos_y_roles(apps):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    RolEmpleado = apps.get_model('empleados', 'RolEmpleado')
    tipo, _ = ContentType.objects.get_or_create(app_label='permisos', model='funcion')
    permisos = {}
    for codigo, nombre in FUNCIONES_NUEVAS:
        permisos[codigo], _ = Permission.objects.get_or_create(
            content_type=tipo, codename=codigo, defaults={'name': nombre})

    for rol in RolEmpleado.objects.filter(nombre='Administrador'):
        rol.funciones.add(*permisos.values())
    for rol in RolEmpleado.objects.filter(nombre='Vendedor'):
        rol.funciones.add(permisos['ver_stock_bidones'])
    recargador, creado = RolEmpleado.objects.get_or_create(
        nombre='Recargador',
        defaults={'grupo_permisos': '', 'descripcion': 'Recarga los bidones en la planta y anota la carga del día.'})
    if creado:
        recargador.funciones.add(permisos['registrar_recargas'])


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0001_initial'),
        ('productos', '0008_producto_es_recargable'),
        ('permisos', '0002_alter_funcion_options'),
        ('empleados', '0007_funciones_por_defecto'),
    ]

    operations = [
        migrations.RunPython(preparar, migrations.RunPython.noop),
    ]
