# -*- coding: utf-8 -*-
from chen import A, E, R, ESP, Diagrama

ENT = [
    E('producto', 950, 720, 'PRODUCTO', [
        A('id_producto', 'Entero', 'clave'), A('nombre', 'Texto(64)'), A('descripcion', 'Texto(500)'),
        A('precio', 'Decimal(10,2)'), A('stock', 'Entero'), A('imagen', 'Imagen'), A('activo', 'Booleano'),
        A('fecha_creacion', 'Fecha y hora'), A('stock_disponible', 'Entero', 'derivado'),
    ], arco=[(250, 300), (342, 390)], r=110, rx=200),
    E('categoria', 260, 720, 'CATEGORIA', [
        A('id_categoria', 'Entero', 'clave'), A('nombre', 'Texto(64)'), A('descripcion', 'Texto(500)'),
    ], arco=(120, 240), r=95, rx=150),
    E('envase', 950, 1140, 'ENVASE', [
        A('es_botellon', 'Booleano'), A('es_retornable', 'Booleano'), A('es_recargable', 'Booleano'),
    ], arco=(30, 150), r=95, rx=170),
    E('carrito', 420, 280, 'CARRITO', [
        A('id_carrito', 'Entero', 'clave'), A('creado', 'Fecha y hora'),
        A('total_items', 'Entero', 'derivado'), A('total_precio', 'Decimal', 'derivado'),
    ], arco=(195, 345), r=95, rx=150),
    E('usuario1', 130, 560, 'USUARIO', ref=True),
    E('promocion', 1600, 330, 'PROMOCION', [
        A('id_promocion', 'Entero', 'clave'), A('nombre', 'Texto(64)'), A('cant_paga', 'Entero'),
        A('cant_lleva', 'Entero'), A('precio', 'Decimal(12,2)'), A('dias_validez', 'Entero'),
        A('activa', 'Booleano'), A('unidades_bonificadas', 'Entero', 'derivado'),
    ], arco=(190, 360), r=120, rx=220),
    E('compra', 1720, 860, 'COMPRA_PROMOCION', [
        A('id_compra', 'Entero', 'clave'), A('fecha_compra', 'Fecha'), A('fecha_caducidad', 'Fecha'),
        A('unid_totales', 'Entero'), A('unid_restantes', 'Entero'), A('estado', 'Texto(10)'),
        A('dias_restantes', 'Entero', 'derivado'),
    ], arco=(-25, 50), r=120, rx=220),
    E('cliente', 2230, 520, 'CLIENTE', ref=True),
    E('pedido', 1720, 1400, 'PEDIDO', ref=True),
    E('recarga', 330, 1160, 'RECARGA_BIDONES', [
        A('id_recarga', 'Entero', 'clave'), A('fecha', 'Fecha (única)'), A('observaciones', 'Texto(200)'),
        A('total', 'Entero', 'derivado'),
    ], arco=(100, 225), r=110, rx=170),
    E('usuario2', 760, 1420, 'USUARIO', ref=True),
]
REL = [
    R('pertenece', 'pertenece', [('producto', '(0,N)'), ('categoria', '(0,N)')], 600, 720, 'N:M'),
    R('usa', 'usa envase', [('producto', '(0,1)'), ('envase', '(0,N)')], 1260, 1010, '1:N'),
    R('contiene', 'contiene', [('carrito', '(0,N)'), ('producto', '(0,N)')], 650, 510, 'N:M',
      attrs=[A('cantidad', 'Entero'), A('subtotal', 'Decimal', 'derivado')], arco=(140, 200), r=80, rx=165),
    R('tiene', 'tiene', [('usuario1', '(0,1)'), ('carrito', '(1,1)')], 240, 420, '1:1'),
    R('bonifica', 'bonifica', [('promocion', '(1,1)'), ('producto', '(0,N)')], 1410, 450, '1:N'),
    R('corresponde', 'corresponde a', [('compra', '(1,1)'), ('promocion', '(0,N)')], 1560, 600, '1:N'),
    R('adquiere', 'adquiere', [('cliente', '(0,N)'), ('compra', '(1,1)')], 2030, 700, '1:N'),
    R('consume', 'consume', [('compra', '(0,N)'), ('pedido', '(0,N)')], 1500, 1150, 'N:M',
      attrs=[A('cantidad', 'Entero'), A('fecha', 'Fecha y hora')], arco=(150, 210), r=60, rx=170),
    R('abona', 'se abona en', [('compra', '(0,1)'), ('pedido', '(0,N)')], 2010, 1240, '1:N'),
    R('recarga_p', 'recarga', [('recarga', '(1,N)'), ('producto', '(0,N)')], 640, 960, 'N:M',
      attrs=[A('cantidad', 'Entero')], arco=(200, 200), r=60, rx=110),
    R('registra', 'registra', [('usuario2', '(0,N)'), ('recarga', '(1,1)')], 520, 1400, '1:N'),
]
ESPS = [ESP('producto', ['envase'], 950, 930, letra='o', total=False)]

DIAGRAMA = Diagrama('DER · Productos, stock y promociones', 2400, 1520, ENT, REL, ESPS,
                    nota='Cardinalidad (mín,máx) junto a cada entidad: cuántas veces participa esa entidad en la relación. Las entidades grises punteadas se detallan en otro diagrama.')
