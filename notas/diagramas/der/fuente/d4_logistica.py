# -*- coding: utf-8 -*-
from chen import A, E, R, ESP, Diagrama

ENT = [
    E('hoja', 1400, 950, 'HOJA_RUTA', [
        A('id_hoja', 'Entero', 'clave'), A('fecha', 'Fecha'), A('estado', 'Texto(20)'),
        A('observaciones', 'Texto(500)'), A('vacios_recibidos', 'Entero'),
        A('fecha_confirmacion', 'Fecha y hora'), A('fecha_salida', 'Fecha y hora'),
        A('fecha_regreso', 'Fecha y hora'), A('generada_automaticamente', 'Booleano'),
        A('total_botellones', 'Entero', 'derivado'), A('porcentaje_completado', 'Decimal', 'derivado'),
    ], arco=[(250, 305), (12, 70)], r=120, rx=230),
    E('parada', 1400, 1750, 'PARADA (DETALLE_HOJA_RUTA)', [
        A('orden', 'Entero', 'parcial'), A('estado', 'Texto(20)'), A('es_venta_calle', 'Booleano'),
        A('es_frecuente', 'Booleano'), A('cantidad_bidones', 'Entero'), A('envases_retirados', 'Entero'),
        A('envases_vendidos', 'Entero'), A('direccion_texto', 'Texto(255)'), A('cliente_nombre', 'Texto(200)'),
        A('nota_entrega', 'Texto(500)'), A('hora_registro', 'Fecha y hora'),
    ], debil=True, arco=[(150, 215), (325, 390)], r=110, rx=250),
    E('zona', 420, 560, 'ZONA', [
        A('id_zona', 'Entero', 'clave'), A('nombre', 'Texto(64) único'), A('descripcion', 'Texto(500)'),
        A('dias_reparto', 'Texto(20)', 'multivaluado'),
    ], arco=(140, 228), r=100, rx=180),
    E('barrio', 140, 950, 'BARRIO', [
        A('id_barrio', 'Entero', 'clave'), A('nombre', 'Texto(64)'), A('ciudad', 'Texto(100)'),
    ], arco=(100, 200), r=90, rx=140),
    E('excepcion', 200, 180, 'CALENDARIO_EXCEPCION', [
        A('id_excepcion', 'Entero', 'clave'), A('fecha', 'Fecha'), A('tipo', 'Texto(10)'), A('motivo', 'Texto(200)'),
    ], arco=(-160, -20), r=70, rx=200),
    E('ruta', 950, 200, 'RUTA_REPARTO', [
        A('id_ruta', 'Entero', 'clave'), A('nombre', 'Texto(64)'), A('dia_semana', 'Entero (0-6)'),
    ], arco=(230, 310), r=80, rx=170),
    E('camion', 2350, 250, 'CAMION', [
        A('patente', 'Texto(10)', 'clave'), A('descripcion', 'Texto(200)'), A('capacidad_botellones', 'Entero'),
        A('activo', 'Booleano'),
    ], arco=(-60, 40), r=100, rx=190),
    E('empleado', 2350, 760, 'EMPLEADO', [
        A('nombre_completo', '', 'compuesto', sub=[A('nombre', 'Texto(64)'), A('apellido', 'Texto(64)')]),
        A('id_empleado', 'Entero', 'clave'),
        A('dni', 'Texto(15) único'), A('celular', 'Texto(30)'), A('email', 'Texto(254)'),
        A('activo', 'Booleano'), A('foto', 'Imagen'), A('notas', 'Texto(500)'),
    ], arco=[(-100, -68, 2), (-15, 65)], r=110, rx=200),
    E('rol', 2350, 1450, 'ROL_EMPLEADO', [
        A('id_rol', 'Entero', 'clave'), A('nombre', 'Texto(64) único'), A('descripcion', 'Texto(500)'),
        A('grupo_permisos', 'Texto(20)'),
    ], arco=(20, 160), r=95, rx=180),
    E('usuario', 2950, 450, 'USUARIO', ref=True),
    E('producto', 620, 1450, 'PRODUCTO', ref=True),
    E('pedido', 1000, 2250, 'PEDIDO', ref=True),
    E('cliente', 1400, 2250, 'CLIENTE', ref=True),
    E('direccion', 1820, 2250, 'DIRECCION_ENTREGA', ref=True),
]
REL = [
    R('contiene', 'contiene', [('hoja', '(0,N)'), ('parada', '(1,1)')], 1400, 1420, '1:N', ident=True),
    R('planifica', 'corresponde a', [('hoja', '(0,1)'), ('zona', '(0,N)')], 900, 760, 'N:1'),
    R('sigue', 'sigue', [('hoja', '(0,1)'), ('ruta', '(0,N)')], 1020, 620, 'N:1'),
    R('usa', 'usa', [('hoja', '(0,1)'), ('camion', '(0,N)')], 2000, 620, 'N:1'),
    R('conduce', 'conduce', [('empleado', '(0,N)'), ('hoja', '(0,1)')], 1900, 850, '1:N'),
    R('recorre', 'recorre', [('ruta', '(1,1)'), ('zona', '(0,N)')], 700, 380, 'N:1'),
    R('camion_def', 'camión habitual', [('ruta', '(0,1)'), ('camion', '(0,N)')], 1650, 200, 'N:1'),
    R('chofer_def', 'chofer habitual', [('ruta', '(0,1)'), ('empleado', '(0,N)')], 1700, 330, 'N:1'),
    R('pertenece', 'pertenece a', [('barrio', '(0,1)'), ('zona', '(0,N)')], 260, 760, 'N:1'),
    R('afecta', 'afecta a', [('excepcion', '(0,1)'), ('zona', '(0,N)')], 330, 380, 'N:1'),
    R('carga', 'carga', [('hoja', '(0,N)'), ('producto', '(0,N)')], 1000, 1250, 'N:M',
      attrs=[A('cantidad_cargada', 'Entero'), A('cantidad_entregada', 'Entero'), A('cantidad_retornada', 'Entero')],
      arco=(195, 265), r=80, rx=160),
    R('entrega', 'entrega', [('parada', '(0,1)'), ('pedido', '(0,N)')], 1100, 2050, 'N:1'),
    R('visita', 'visita a', [('parada', '(0,1)'), ('cliente', '(0,N)')], 1400, 2050, 'N:1'),
    R('en', 'en', [('parada', '(0,1)'), ('direccion', '(0,N)')], 1700, 2050, 'N:1'),
    R('desempena', 'desempeña', [('empleado', '(1,1)'), ('rol', '(0,N)')], 2350, 1150, 'N:1'),
    R('accede', 'accede como', [('usuario', '(0,1)'), ('empleado', '(0,1)')], 2680, 560, '1:1'),
]

DIAGRAMA = Diagrama('DER · Logística, reparto y empleados', 2900, 2000, ENT, REL,
                    nota='Cardinalidad (mín,máx) junto a cada entidad. Doble óvalo: atributo multivaluado (días de reparto). Se omiten las relaciones de auditoría con USUARIO (creada/confirmada por).')
