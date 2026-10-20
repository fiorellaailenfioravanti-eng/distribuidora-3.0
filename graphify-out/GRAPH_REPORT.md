# Graph Report - proj  (2026-10-16)

## Corpus Check
- 205 files · ~67,987 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: .css 3, (none) 2, .example 1)

## Summary
- 986 nodes · 2467 edges · 66 communities (36 shown, 30 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 343 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Catálogo, carrito y buscador
- Pedidos y pagos (MercadoPago)
- Empleados y roles
- Cuentas corrientes y vistas
- Migraciones: auth, clientes, productos
- Tests de permisos y RNF-02
- Abonos: formularios y vistas
- Direcciones de entrega y seed logístico
- Migraciones: logística, clientes, carrito
- Servicios logísticos (hojas y ventas)
- Vistas de clientes
- Movimientos de cuenta
- Modelos y admin de logística
- Autenticación y has_group
- Formularios de logística
- Usuario y modelo de abonos
- Plan de fases y requisitos
- Confirmación y regreso del camión
- Modelo Cliente
- Planificación de reparto por zona
- Vistas del repartidor (RNF-02)
- Guards de permisos en logística
- Vistas de rutas y zonas
- Calendario de reparto
- Formularios de clientes
- Carga sugerida y planificar reparto
- Facturación mensual de abonos
- Admin de clientes
- Alta de clientes con/sin cuenta
- Zonas y días de reparto
- Tests de abonos (RF-05)
- Tests de semaforización (RF-14)
- Camiones
- Arranque Django (asgi/wsgi)
- AppConfigs varias
- Roles: fuente única
- Settings y despliegue
- Documentación .agents
- Señal de alta de cliente
- Tests de vistas de cuentas
- Tests vacíos (H-10)
- Tests de planificar reparto
- Sincronización de permisos
- Fase 4 y precio Premium
- Migración: unificar empleados
- Migración: borrar empleados duplicados
- Migración: métodos de pago
- App permisos
- Fase 5: bidones y promociones
- manage.py
- App clientes
- App autenticacion
- App carrito
- App cuentas
- App empleados
- App logistica
- App pedidos

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 70 edges
2. `es_admin_o_vendedor()` - 70 edges
3. `Producto` - 44 edges
4. `Zona` - 40 edges
5. `Pedido` - 37 edges
6. `DireccionEntrega` - 35 edges
7. `HojaRuta` - 35 edges
8. `CuentaCorriente` - 28 edges
9. `Abono` - 27 edges
10. `DetalleHojaRuta` - 25 edges

## Surprising Connections (you probably didn't know these)
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `D-1 · "VIP" como etiqueta de Premium (2 tipos de cliente)` --rationale_for--> `Cliente`  [EXTRACTED]
  .agents/PROCEDURE.md → apps/clientes/models.py
- `DireccionEntrega` --implements--> `RF-03 · Multidirección de entrega`  [EXTRACTED]
  apps/clientes/models.py → .agents/PROCEDURE.md
- `Carga y regreso del camión (sobrantes a stock)` --references--> `CargaHojaRuta`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (66 total, 30 thin omitted)

### Community 0 - "Catálogo, carrito y buscador"
Cohesion: 0.05
Nodes (31): buscar_productos(), normalizar_texto(), carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito() (+23 more)

### Community 1 - "Pedidos y pagos (MercadoPago)"
Cohesion: 0.07
Nodes (22): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, PagoPedido, Meta, Pedido (+14 more)

### Community 2 - "Empleados y roles"
Cohesion: 0.12
Nodes (21): EmpleadoAdmin, RolEmpleadoAdmin, EmpleadoForm, Meta, RolEmpleadoForm, Meta, Empleado, Meta (+13 more)

### Community 3 - "Cuentas corrientes y vistas"
Cohesion: 0.10
Nodes (13): CargoCuentaForm, PagoCuentaForm, CuentaCorriente, Meta, resumen_morosidad(), cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas() (+5 more)

### Community 4 - "Migraciones: auth, clientes, productos"
Cohesion: 0.05
Nodes (15): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+7 more)

### Community 5 - "Tests de permisos y RNF-02"
Cohesion: 0.06
Nodes (5): puede_ver_nota_seguridad(), AccesoAVistasLogisticasTests, GruposBaseTests, ModeloEmpleadoUnicoTests, NotaDeSeguridadTests

### Community 6 - "Abonos: formularios y vistas"
Cohesion: 0.12
Nodes (12): AbonoAdmin, AbonoForm, Meta, Abono, Meta, cambiar_estado_abono(), crear_abono(), editar_abono() (+4 more)

### Community 7 - "Direcciones de entrega y seed logístico"
Cohesion: 0.11
Nodes (10): DireccionEntrega, Meta, Command, Barrio, Meta, CheckoutForm, _etiqueta_direccion_con_fecha(), MetodoPago (+2 more)

### Community 8 - "Migraciones: logística, clientes, carrito"
Cohesion: 0.08
Nodes (13): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+5 more)

### Community 9 - "Servicios logísticos (hojas y ventas)"
Cohesion: 0.12
Nodes (13): bidones_de_pedido(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona(), _metodo_pago_efectivo(), _producto_envase_para(), registrar_cobro(), registrar_entrega() (+5 more)

### Community 10 - "Vistas de clientes"
Cohesion: 0.21
Nodes (13): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+5 more)

### Community 11 - "Movimientos de cuenta"
Cohesion: 0.11
Nodes (9): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests (+1 more)

### Community 12 - "Modelos y admin de logística"
Cohesion: 0.11
Nodes (18): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+10 more)

### Community 13 - "Autenticación y has_group"
Cohesion: 0.15
Nodes (8): IngresarUsuarioForm, RegistroUsuarioForm, Meta, has_group(), cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario()

### Community 14 - "Formularios de logística"
Cohesion: 0.12
Nodes (10): ActualizarEstadoForm, Meta, BarrioForm, Meta, DetalleRutaForm, Meta, HojaRutaForm, Meta (+2 more)

### Community 16 - "Plan de fases y requisitos"
Cohesion: 0.18
Nodes (17): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, RF-03 · Multidirección de entrega, RF-04 · ≥2 teléfonos con relación explícita (+9 more)

### Community 17 - "Confirmación y regreso del camión"
Cohesion: 0.16
Nodes (7): ZonaForm, Meta, confirmar_hoja(), registrar_regreso(), ConfirmacionRegresoTests, HojaRutaCapacidadTests, ZonaFormTests

### Community 18 - "Modelo Cliente"
Cohesion: 0.13
Nodes (3): Cliente, Meta, checkout()

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.16
Nodes (5): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), pedidos_candidatos(), GeneracionBorradorTests

### Community 20 - "Vistas del repartidor (RNF-02)"
Cohesion: 0.18
Nodes (6): actualizar_estado_entrega(), crear_ruta(), _ids_de_paradas_con_nota(), mi_ruta_hoy(), ver_ruta(), obtener_empleado()

### Community 21 - "Guards de permisos en logística"
Cohesion: 0.22
Nodes (6): imprimir_ruta(), listar_rutas(), es_admin_o_vendedor(), es_admin_vendedor_o_repartidor(), es_repartidor(), EvaluacionDeRolesTests

### Community 22 - "Vistas de rutas y zonas"
Cohesion: 0.24
Nodes (9): agregar_parada(), confirmar_ruta(), direcciones_sin_zona(), editar_ruta(), editar_zona(), eliminar_parada(), eliminar_zona(), listar_zonas() (+1 more)

### Community 23 - "Calendario de reparto"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "Formularios de clientes"
Cohesion: 0.12
Nodes (8): BuscarClienteForm, ClienteForm, Meta, ClienteSinCuentaForm, Meta, DireccionEntregaForm, Meta, EditarMiPerfilForm

### Community 25 - "Carga sugerida y planificar reparto"
Cohesion: 0.18
Nodes (9): carga_sugerida(), _cargas_confirmacion_desde_post(), _int_o_none(), _parse_fecha(), planificar_reparto(), _productos_para_carga(), _regreso_desde_post(), _seleccion_desde_post() (+1 more)

### Community 26 - "Facturación mensual de abonos"
Cohesion: 0.17
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "Admin de clientes"
Cohesion: 0.16
Nodes (9): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, TelefonoContactoAdmin, TelefonoContactoInline, TelefonoContactoForm, Meta, TelefonoContacto (+1 more)

### Community 28 - "Alta de clientes con/sin cuenta"
Cohesion: 0.17
Nodes (6): AltaClienteConCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 29 - "Zonas y días de reparto"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 32 - "Camiones"
Cohesion: 0.27
Nodes (7): CamionForm, Meta, Camion, Meta, editar_camion(), eliminar_camion(), listar_camiones()

### Community 34 - "AppConfigs varias"
Cohesion: 0.20
Nodes (3): AbonosConfig, BuscadorConfig, ProductosConfig

### Community 35 - "Roles: fuente única"
Cohesion: 0.24
Nodes (5): _en_grupo(), es_admin(), es_personal_interno(), es_repartidor_asignado(), es_vendedor()

### Community 37 - "Documentación .agents"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 43 - "Fase 4 y precio Premium"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 48 - "Fase 5: bidones y promociones"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

## Knowledge Gaps
- **30 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Modelo Cliente` to `Catálogo, carrito y buscador`, `Pedidos y pagos (MercadoPago)`, `Cuentas corrientes y vistas`, `Tests de permisos y RNF-02`, `Abonos: formularios y vistas`, `Direcciones de entrega y seed logístico`, `Servicios logísticos (hojas y ventas)`, `Vistas de clientes`, `Movimientos de cuenta`, `Usuario y modelo de abonos`, `Plan de fases y requisitos`, `Confirmación y regreso del camión`, `Planificación de reparto por zona`, `Formularios de clientes`, `Facturación mensual de abonos`, `Admin de clientes`, `Alta de clientes con/sin cuenta`, `Tests de abonos (RF-05)`, `Tests de semaforización (RF-14)`, `Señal de alta de cliente`, `Tests de vistas de cuentas`, `Tests de planificar reparto`, `Fase 4 y precio Premium`, `Fase 5: bidones y promociones`?**
  _High betweenness centrality (0.193) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `Catálogo, carrito y buscador` be split into smaller, more focused modules?**
  _Cohesion score 0.05170998632010944 - nodes in this community are weakly interconnected._
- **Why does `es_admin_o_vendedor()` connect `Guards de permisos en logística` to `Catálogo, carrito y buscador`, `Camiones`, `Empleados y roles`, `Cuentas corrientes y vistas`, `Pedidos y pagos (MercadoPago)`, `Roles: fuente única`, `Abonos: formularios y vistas`, `Tests de permisos y RNF-02`, `Direcciones de entrega y seed logístico`, `Vistas de clientes`, `Vistas del repartidor (RNF-02)`, `Vistas de rutas y zonas`, `Carga sugerida y planificar reparto`, `Alta de clientes con/sin cuenta`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `Producto` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Producto` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Should `Pedidos y pagos (MercadoPago)` be split into smaller, more focused modules?**
  _Cohesion score 0.07142857142857142 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Catálogo, carrito y buscador` to `Abonos: formularios y vistas`, `Direcciones de entrega y seed logístico`, `Servicios logísticos (hojas y ventas)`, `Usuario y modelo de abonos`, `Confirmación y regreso del camión`, `Carga sugerida y planificar reparto`, `Facturación mensual de abonos`, `Tests de abonos (RF-05)`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._