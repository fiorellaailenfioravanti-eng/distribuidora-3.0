# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 175 files · ~271,337 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1245 nodes · 2960 edges · 98 communities (50 shown, 48 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 442 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `097f0556`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Catálogo, carrito y buscador
- pedidos/urls.py
- empleados/views.py
- CuentaCorriente
- Migraciones: auth, clientes, productos
- ModeloEmpleadoUnicoTests
- Abono
- Direcciones de entrega y seed logístico
- Migraciones: logística, clientes, carrito
- logistica/services.py
- Vistas de clientes
- Movimientos de cuenta
- logistica/admin.py
- Autenticación y has_group
- permisos/tests.py
- Usuario y modelo de abonos
- PROCEDURE.md
- logistica/tests.py
- Modelo Cliente
- Planificación de reparto por zona
- What You Must Do When Invoked
- es_admin_o_vendedor
- pedidos/views.py
- Calendario de reparto
- Formularios de clientes
- DetalleHojaRuta
- Facturación mensual de abonos
- Admin de clientes
- Alta de clientes con/sin cuenta
- Zonas y días de reparto
- Tests de abonos (RF-05)
- registrar_cargo
- registrar_cobro
- django_apps
- Roles: fuente única
- Empleado
- TransicionesManualesTests
- Señal de alta de cliente
- Tests de vistas de cuentas
- PagosSegurosTests
- PlanificarRepartoViewTests
- permisos/signals.py
- puede_ver_nota_seguridad
- Migración: unificar empleados
- Migración: borrar empleados duplicados
- Migración: métodos de pago
- Usuario
- RolSincronizaGrupoTests
- manage.py
- PagoPedido
- AccesoAVistasLogisticasTests
- ConfirmacionRegresoTests
- graphify reference: extra exports and benchmark
- SesionTests
- BuscarClientesTests
- GuardsUnificadosTests
- confirmar_pedido
- EliminarProductoTests
- 🏁 Plan de Cierre — Fases 4.5 a 7
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- graphify reference: query, path, explain
- Verificar cambios — Distribuidora 3.0
- Verificar cambios — Distribuidora 3.0
- 0003_grupos_base.py
- 0004_asignar_grupo_permisos.py
- PantallasDeRolesTests
- Distribuidora 3.0 / Aquadelluvia
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md

## God Nodes (most connected - your core abstractions)
1. `es_admin_o_vendedor()` - 81 edges
2. `Cliente` - 73 edges
3. `Pedido` - 50 edges
4. `Producto` - 49 edges
5. `Zona` - 42 edges
6. `HojaRuta` - 38 edges
7. `DireccionEntrega` - 37 edges
8. `DetalleHojaRuta` - 29 edges
9. `MetodoPago` - 29 edges
10. `CuentaCorriente` - 28 edges

## Surprising Connections (you probably didn't know these)
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Carga y regreso del camión (sobrantes a stock)` --references--> `CargaHojaRuta`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `5A — Historial de envases (RF-08) · ~4 h` --references--> `Usuario`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/autenticacion/models.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (98 total, 48 thin omitted)

### Community 0 - "Catálogo, carrito y buscador"
Cohesion: 0.05
Nodes (29): buscar_productos(), carrito_total(), Carrito, ItemCarrito, Meta, CarritoSoloPorPostTests, agregar_al_carrito(), eliminar_del_carrito() (+21 more)

### Community 1 - "pedidos/urls.py"
Cohesion: 0.12
Nodes (10): 1. 🔴 Críticos — seguridad y dinero, cambiar_estado_pedido(), checkout(), confirmar_pago_qr(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido() (+2 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.27
Nodes (12): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+4 more)

### Community 3 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 4 - "Migraciones: auth, clientes, productos"
Cohesion: 0.05
Nodes (16): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+8 more)

### Community 6 - "Abono"
Cohesion: 0.06
Nodes (24): AbonoAdmin, AbonoForm, Meta, Abono, Meta, cambiar_estado_abono(), crear_abono(), editar_abono() (+16 more)

### Community 7 - "Direcciones de entrega y seed logístico"
Cohesion: 0.13
Nodes (8): DireccionEntrega, Meta, AgregarDireccionTests, Command, MetodoPago, Meta, Pedido, Meta

### Community 8 - "Migraciones: logística, clientes, carrito"
Cohesion: 0.08
Nodes (13): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+5 more)

### Community 9 - "logistica/services.py"
Cohesion: 0.13
Nodes (13): 5B — Promociones prepago (RF-09) · ~6 h, bidones_de_pedido(), clientes_frecuentes_de_zona(), construir_borrador(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona(), pedidos_candidatos() (+5 more)

### Community 10 - "Vistas de clientes"
Cohesion: 0.21
Nodes (11): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+3 more)

### Community 11 - "Movimientos de cuenta"
Cohesion: 0.16
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 12 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 13 - "Autenticación y has_group"
Cohesion: 0.19
Nodes (7): IngresarUsuarioForm, RegistroUsuarioForm, Meta, cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario()

### Community 14 - "permisos/tests.py"
Cohesion: 0.18
Nodes (5): BarrioForm, Meta, Command, Barrio, Meta

### Community 16 - "PROCEDURE.md"
Cohesion: 0.05
Nodes (35): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Carga y regreso del camión (sobrantes a stock), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad (+27 more)

### Community 17 - "logistica/tests.py"
Cohesion: 0.16
Nodes (9): ActualizarEstadoForm, Meta, RutaRepartoForm, Meta, ZonaForm, Meta, RutaReparto, Meta (+1 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "es_admin_o_vendedor"
Cohesion: 0.06
Nodes (44): Hallazgos nuevos, CamionForm, Meta, DetalleRutaForm, Meta, HojaRutaForm, Meta, Camion (+36 more)

### Community 22 - "pedidos/views.py"
Cohesion: 0.13
Nodes (9): _a_decimal(), aplicar_pago_mercadopago(), consultar_pago_mercadopago(), firma_webhook_valida(), metodo_pago_efectivo(), pago_en_curso(), cambiar_estado_pago(), pago_exitoso() (+1 more)

### Community 23 - "Calendario de reparto"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "Formularios de clientes"
Cohesion: 0.15
Nodes (9): BuscarClienteForm, ClienteForm, Meta, DireccionEntregaForm, Meta, EditarMiPerfilForm, listar_clientes(), _texto_buscable() (+1 more)

### Community 25 - "DetalleHojaRuta"
Cohesion: 0.13
Nodes (10): 5A — Historial de envases (RF-08) · ~4 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10), Punto de partida real, DetalleHojaRuta, Meta, _producto_envase_para() (+2 more)

### Community 26 - "Facturación mensual de abonos"
Cohesion: 0.17
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "Admin de clientes"
Cohesion: 0.12
Nodes (11): 4. ♻️ Redundancias, ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, TelefonoContactoAdmin, TelefonoContactoInline, TelefonoContactoForm, Meta (+3 more)

### Community 28 - "Alta de clientes con/sin cuenta"
Cohesion: 0.12
Nodes (8): AltaClienteConCuentaForm, Meta, ClienteSinCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 29 - "Zonas y días de reparto"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 31 - "registrar_cargo"
Cohesion: 0.14
Nodes (4): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, SemaforizacionTests

### Community 32 - "registrar_cobro"
Cohesion: 0.15
Nodes (9): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 5. 🔗 Dependencias y archivos compartidos, 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18), Punto de partida real (+1 more)

### Community 34 - "django_apps"
Cohesion: 0.05
Nodes (11): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, CuentasConfig, EmpleadosConfig, LogisticaConfig (+3 more)

### Community 35 - "Roles: fuente única"
Cohesion: 0.23
Nodes (8): roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor_asignado(), es_vendedor(), 2. Revisar convenciones del proyecto en lo que cambió, 2. Revisar convenciones del proyecto en lo que cambió

### Community 36 - "Empleado"
Cohesion: 0.21
Nodes (6): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta

### Community 37 - "TransicionesManualesTests"
Cohesion: 0.15
Nodes (3): _etiqueta_direccion_con_fecha(), CheckoutFechaEstimadaTests, TransicionesManualesTests

### Community 41 - "PlanificarRepartoViewTests"
Cohesion: 0.13
Nodes (3): HojaRutaCapacidadTests, HojaSinChoferTests, PlanificarRepartoViewTests

### Community 42 - "permisos/signals.py"
Cohesion: 0.24
Nodes (5): sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 47 - "Usuario"
Cohesion: 0.24
Nodes (4): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoForm, Meta

### Community 50 - "PagoPedido"
Cohesion: 0.27
Nodes (7): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, PagoPedido, Meta

### Community 52 - "ConfirmacionRegresoTests"
Cohesion: 0.25
Nodes (4): CargaHojaRuta, Meta, confirmar_hoja(), ConfirmacionRegresoTests

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 64 - "confirmar_pedido"
Cohesion: 0.25
Nodes (3): CheckoutForm, metodos_pago_checkout_web(), confirmar_pedido()

### Community 67 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.29
Nodes (7): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 7 — QA, producción y tesis 🎓, 🏁 Plan de Cierre — Fases 4.5 a 7

### Community 68 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.33
Nodes (6): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 71 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 76 - "Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

## Knowledge Gaps
- **1 isolated node(s):** `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 491 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **48 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Modelo Cliente` to `Catálogo, carrito y buscador`, `pedidos/urls.py`, `CuentaCorriente`, `Abono`, `Direcciones de entrega y seed logístico`, `logistica/services.py`, `Vistas de clientes`, `Movimientos de cuenta`, `permisos/tests.py`, `Usuario y modelo de abonos`, `PROCEDURE.md`, `logistica/tests.py`, `Planificación de reparto por zona`, `pedidos/views.py`, `Formularios de clientes`, `DetalleHojaRuta`, `Facturación mensual de abonos`, `Admin de clientes`, `Alta de clientes con/sin cuenta`, `Tests de abonos (RF-05)`, `registrar_cargo`, `TransicionesManualesTests`, `Señal de alta de cliente`, `Tests de vistas de cuentas`, `PlanificarRepartoViewTests`, `puede_ver_nota_seguridad`, `AccesoAVistasLogisticasTests`, `ConfirmacionRegresoTests`, `BuscarClientesTests`, `confirmar_pedido`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Catálogo, carrito y buscador` be split into smaller, more focused modules?**
  _Cohesion score 0.05393000573723465 - nodes in this community are weakly interconnected._
- **Why does `es_admin_o_vendedor()` connect `es_admin_o_vendedor` to `registrar_cobro`, `Catálogo, carrito y buscador`, `empleados/views.py`, `pedidos/urls.py`, `Roles: fuente única`, `Abono`, `Vistas de clientes`, `puede_ver_nota_seguridad`, `Distribuidora 3.0 / Aquadelluvia`, `permisos/tests.py`, `Usuario`, `pedidos/views.py`, `Formularios de clientes`, `Admin de clientes`, `Alta de clientes con/sin cuenta`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/urls.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12307692307692308 - nodes in this community are weakly interconnected._