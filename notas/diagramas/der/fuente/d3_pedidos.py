# -*- coding: utf-8 -*-
from chen import A, E, R, ESP, Diagrama

ENT = [
    E('pedido', 1200, 680, 'PEDIDO', [
        A('id_pedido', 'Entero', 'clave'), A('fecha_pedido', 'Fecha y hora'), A('estado', 'Texto(20)'),
        A('origen', 'Texto(15)'), A('total', 'Decimal(12,2)'), A('notas_cliente', 'Texto(500)'),
        A('fecha_estimada_entrega', 'Fecha'), A('fecha_entrega', 'Fecha'),
        A('confirmado_por_empresa', 'Booleano'), A('total_pagado', 'Decimal', 'derivado'),
        A('saldo_pendiente', 'Decimal', 'derivado'),
    ], arco=(195, 345), r=120, rx=230),
    E('pago', 1620, 1350, 'PAGO_PEDIDO', [
        A('datos_mercadopago', '', 'compuesto', sub=[A('payment_id', 'Texto(100)'), A('preference_id', 'Texto(100)'),
                                                     A('status', 'Texto(50)')]),
        A('id_pago', 'Entero', 'clave'), A('monto', 'Decimal(12,2)'), A('fecha', 'Fecha y hora'),
        A('estado_pago', 'Texto(30)'), A('referencia_comprobante', 'Texto(100)'),
        A('datos_tarjeta', '', 'compuesto', sub=[A('ultimos_4', 'Texto(4)'), A('titular', 'Texto(100)')]),
    ], arco=[(5, 5, 1), (35, 125, 5), (155, 155, 1)], r=110, rx=200),
    E('metodo', 2150, 1000, 'METODO_PAGO', [
        A('id_metodo', 'Entero', 'clave'), A('codigo', 'Texto(50) único'), A('nombre', 'Texto(64)'),
        A('descripcion', 'Texto(500)'), A('activo', 'Booleano'),
    ], arco=(-40, 60), r=100, rx=180),
    E('suscripcion', 560, 1260, 'SUSCRIPCION_REPOSICION', [
        A('id_suscripcion', 'Entero', 'clave'), A('cantidad', 'Entero'), A('periodicidad_dias', 'Entero (7/15/30)'),
        A('proxima_fecha', 'Fecha'), A('activa', 'Booleano'), A('fecha_alta', 'Fecha y hora'),
    ], arco=(140, 230), r=110, rx=200),
    E('cliente', 260, 680, 'CLIENTE', ref=True),
    E('direccion', 1060, 1770, 'DIRECCION_ENTREGA', ref=True),
    E('producto', 2250, 640, 'PRODUCTO', ref=True),
    E('producto2', 200, 1770, 'PRODUCTO', ref=True),
    E('metodo2', 500, 1770, 'METODO_PAGO', ref=True),
]
REL = [
    R('realiza', 'realiza', [('cliente', '(0,N)'), ('pedido', '(0,1)')], 700, 680, '1:N'),
    R('incluye', 'incluye', [('pedido', '(1,N)'), ('producto', '(0,N)')], 1880, 640, 'N:M',
      attrs=[A('precio_unitario', 'Decimal(10,2)'), A('cantidad', 'Entero'), A('subtotal', 'Decimal(12,2)')],
      arco=(260, 340), r=80, rx=150),
    R('paga_con', 'se paga con', [('pedido', '(1,1)'), ('metodo', '(0,N)')], 1700, 860, 'N:1'),
    R('registra', 'registra', [('pedido', '(0,N)'), ('pago', '(1,1)')], 1400, 1000, '1:N'),
    R('mediante', 'mediante', [('pago', '(1,1)'), ('metodo', '(0,N)')], 1860, 1150, 'N:1'),
    R('entrega', 'se entrega en', [('pedido', '(0,1)'), ('direccion', '(0,N)')], 1060, 1250, 'N:1'),
    R('programa', 'programa', [('cliente', '(0,1)'), ('suscripcion', '(1,1)')], 330, 980, '1:1'),
    R('genera', 'genera', [('suscripcion', '(0,1)'), ('pedido', '(0,N)')], 860, 960, '1:N'),
    R('entrega_s', 'se entrega en', [('suscripcion', '(0,1)'), ('direccion', '(0,N)')], 790, 1770, 'N:1'),
    R('repone', 'repone', [('suscripcion', '(1,1)'), ('producto2', '(0,N)')], 300, 1540, 'N:1'),
    R('paga_s', 'se paga con', [('suscripcion', '(1,1)'), ('metodo2', '(0,N)')], 500, 1560, 'N:1'),
]

DIAGRAMA = Diagrama('DER · Pedidos, pagos y suscripciones', 2500, 1860, ENT, REL,
                    nota='Cardinalidad (mín,máx) junto a cada entidad. «genera» registra el último pedido creado por la suscripción. Óvalo punteado: atributo derivado.')
