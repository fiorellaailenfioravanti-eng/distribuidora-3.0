"""
Catálogo de funciones del sistema (qué puede hacer un empleado).

Cada función es un permiso de Django (`permisos.<codigo>`) que se asigna a los
roles con checkboxes (pantalla Empleados › Roles). Las vistas lo exigen con
`roles.puede(user, '<codigo>')` o el decorador `roles.requiere('<codigo>')`.

Para agregar una función: sumarla acá, correr `makemigrations permisos` y
usarla en la vista. Los roles existentes no la reciben solos: se marca a mano.
"""

# (código, descripción para el checkbox)
FUNCIONES_POR_AREA = [
    ('Panel', [
        ('ver_panel', 'Entrar al panel y ver el resumen general'),
    ]),
    ('Productos', [
        ('ver_inventario', 'Ver el inventario (incluye productos inactivos)'),
        ('gestionar_productos', 'Crear, editar y eliminar productos'),
        ('gestionar_categorias', 'Crear, editar y eliminar categorías'),
    ]),
    ('Clientes', [
        ('ver_clientes', 'Ver la lista y la ficha de los clientes'),
        ('registrar_clientes', 'Registrar y editar clientes (datos, teléfonos y direcciones)'),
        ('cambiar_tipo_cliente', 'Pasar clientes a VIP / Normal (habilita el fiado)'),
        ('registrar_envases', 'Registrar movimientos de envases'),
        ('ver_notas_seguridad', 'Ver las notas de seguridad de todos los domicilios'),
    ]),
    ('Pedidos', [
        ('ver_pedidos', 'Ver los pedidos de todos los clientes'),
        ('gestionar_pedidos', 'Cambiar el estado de los pedidos y el pedido automático'),
        ('cobrar_pedidos', 'Registrar cobros y validar pagos'),
    ]),
    ('Cuentas corrientes', [
        ('ver_cuentas', 'Ver cuentas corrientes y morosidad'),
        ('registrar_movimientos_cuenta', 'Registrar cargos y pagos en las cuentas'),
    ]),
    ('Abonos', [
        ('gestionar_abonos', 'Ver y gestionar abonos de dispensers (y generar los cargos)'),
    ]),
    ('Promociones', [
        ('gestionar_promociones', 'Crear y editar promociones'),
        ('vender_promociones', 'Vender packs de promoción a clientes'),
    ]),
    ('Logística', [
        ('planificar_repartos', 'Planificar repartos y armar o editar hojas de ruta'),
        ('ver_todas_las_rutas', 'Ver todas las hojas de ruta (no sólo las propias)'),
        ('realizar_entregas', 'Hacer el recorrido: entregar, cobrar y vender en la calle'),
        ('gestionar_zonas_camiones', 'Gestionar zonas, barrios y camiones'),
    ]),
    ('Empleados', [
        ('gestionar_empleados', 'Gestionar empleados, roles y permisos'),
    ]),
]

FUNCIONES = [funcion for _, funciones in FUNCIONES_POR_AREA for funcion in funciones]
CODIGOS = [codigo for codigo, _ in FUNCIONES]

# Permisos por defecto de los roles base (se pueden cambiar después).
POR_DEFECTO = {
    'Administrador': set(CODIGOS),
    # El vendedor planifica (y con eso opera cualquier hoja) pero no hace recorridos.
    'Vendedor': set(CODIGOS) - {'gestionar_empleados', 'realizar_entregas'},
    'Repartidor': {'realizar_entregas'},
}
