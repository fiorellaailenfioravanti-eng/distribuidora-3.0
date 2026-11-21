# -*- coding: utf-8 -*-
from chen import A, E, R, ESP, Diagrama

ENT = [
    E('cliente', 1300, 900, 'CLIENTE', [
        A('nombre_completo', '', 'compuesto', sub=[A('nombre', 'Texto(64)'), A('apellido', 'Texto(64)')]),
        A('id_cliente', 'Entero', 'clave'), A('numero', 'Texto(10) único'),
        A('dni', 'Texto(15) único'), A('email_contacto', 'Texto(120)'), A('fecha_nacimiento', 'Fecha'),
        A('fecha_alta', 'Fecha'), A('tipo_cliente', 'Texto(10)'), A('permite_fiado', 'Booleano'),
        A('bidones_prestados', 'Entero'), A('es_frecuente', 'Booleano'), A('tipo_registro', 'Texto(12)'),
        A('notas_internas', 'Texto(500)'),
    ], arco=[(196, 196, 1), (218, 258), (283, 345)], r=120, rx=230),
    E('usuario', 1300, 190, 'USUARIO', [
        A('id_usuario', 'Entero', 'clave'), A('username', 'Texto(150) único'), A('email', 'Texto(254) único'),
        A('password', 'Texto(128) cifrada'), A('imagen_perfil', 'Imagen'), A('is_active', 'Booleano'),
        A('date_joined', 'Fecha y hora'),
    ], arco=[(150, 240), (300, 390)], r=80, rx=200),
    E('telefono', 430, 900, 'TELEFONO_CONTACTO', [
        A('numero', 'Texto(20)', 'parcial'), A('desc_relacion', 'Texto(40)'), A('es_principal', 'Booleano'),
    ], debil=True, arco=(150, 215), r=80, rx=200),
    E('direccion', 560, 1360, 'DIRECCION_ENTREGA', [
        A('id_direccion', 'Entero', 'clave'),
        A('domicilio', '', 'compuesto', sub=[A('calle', 'Texto(100)'), A('altura', 'Texto(10)'),
                                             A('piso_depto', 'Texto(30)'), A('ciudad', 'Texto(64)')]),
        A('w3w', 'Texto(80)'), A('coordenadas', 'Texto(40)'), A('desc_seguridad', 'Texto(500)'),
        A('es_principal', 'Booleano'),
    ], arco=(105, 215), r=110, rx=200),
    E('barrio', 700, 1880, 'BARRIO', ref=True),
    E('movbidon', 1250, 1500, 'MOVIMIENTO_BIDON', [
        A('id_movimiento', 'Entero', 'clave'), A('tipo', 'Texto(12)'), A('cantidad', 'Entero'),
        A('fecha', 'Fecha y hora'), A('nota', 'Texto(200)'),
    ], arco=(150, 215), r=95, rx=190),
    E('cuenta', 2300, 820, 'CUENTA_CORRIENTE', [
        A('id_cuenta', 'Entero', 'clave'), A('saldo', 'Decimal(12,2)'), A('limite_credito', 'Decimal(12,2)'),
        A('activa', 'Booleano'), A('fecha_apertura', 'Fecha'), A('dias_de_atraso', 'Entero', 'derivado'),
        A('nivel_morosidad', 'Texto', 'derivado'),
    ], arco=(195, 345), r=110, rx=200),
    E('movcuenta', 2250, 1500, 'MOVIMIENTO_CUENTA', [
        A('id_movimiento', 'Entero', 'clave'), A('tipo', 'Texto(10)'), A('monto', 'Decimal(12,2)'),
        A('descripcion', 'Texto(200)'), A('fecha', 'Fecha y hora'), A('fecha_vencimiento', 'Fecha'),
    ], arco=(-50, 55), r=110, rx=190),
    E('abono', 1720, 1460, 'ABONO', [
        A('id_abono', 'Entero', 'clave'), A('fecha_inicio', 'Fecha'), A('fecha_fin', 'Fecha'),
        A('costo_mensual', 'Decimal(12,2)'), A('dia_facturacion', 'Entero'), A('estado', 'Texto(12)'),
        A('ultima_facturacion', 'Fecha'), A('observaciones', 'Texto(500)'),
    ], arco=(-125, 8), r=100, rx=190),
    E('producto', 1700, 1880, 'PRODUCTO', ref=True),
    E('pedido', 2380, 1880, 'PEDIDO', ref=True),
    E('parada', 1450, 1880, 'PARADA (DETALLE_HOJA_RUTA)', ref=True),
    E('pedido2', 1000, 1880, 'PEDIDO', ref=True),
]
REL = [
    R('posee_u', 'posee cuenta', [('usuario', '(0,1)'), ('cliente', '(0,1)')], 1300, 390, '1:1'),
    R('tiene_t', 'tiene', [('cliente', '(0,N)'), ('telefono', '(1,1)')], 850, 960, '1:N', ident=True),
    R('tiene_d', 'tiene', [('cliente', '(0,N)'), ('direccion', '(1,1)')], 900, 1130, '1:N'),
    R('ubicada', 'ubicada en', [('direccion', '(0,1)'), ('barrio', '(0,N)')], 620, 1650, 'N:1'),
    R('registra_b', 'registra', [('cliente', '(0,N)'), ('movbidon', '(1,1)')], 1170, 1200, '1:N'),
    R('mov_ped', 'asociado a', [('movbidon', '(0,1)'), ('pedido2', '(0,N)')], 1080, 1720, 'N:1'),
    R('mov_par', 'en parada', [('movbidon', '(0,1)'), ('parada', '(0,N)')], 1380, 1720, 'N:1'),
    R('posee_c', 'posee', [('cliente', '(0,1)'), ('cuenta', '(1,1)')], 1780, 930, '1:1'),
    R('registra_c', 'registra', [('cuenta', '(0,N)'), ('movcuenta', '(1,1)')], 2330, 1170, '1:N'),
    R('contrata', 'contrata', [('cliente', '(0,N)'), ('abono', '(1,1)')], 1440, 1360, '1:N'),
    R('alquila', 'alquila', [('abono', '(1,1)'), ('producto', '(0,N)')], 1650, 1700, 'N:1'),
    R('factura', 'factura', [('movcuenta', '(0,1)'), ('abono', '(0,N)')], 2010, 1560, 'N:1'),
    R('origina', 'originado en', [('movcuenta', '(0,1)'), ('pedido', '(0,N)')], 2330, 1760, 'N:1'),
]

DIAGRAMA = Diagrama('DER · Clientes, envases y cuentas corrientes', 2650, 2000, ENT, REL,
                    nota='Cardinalidad (mín,máx) junto a cada entidad. Doble rectángulo y doble rombo: entidad débil y su relación identificadora (clave parcial subrayada con guiones).')
