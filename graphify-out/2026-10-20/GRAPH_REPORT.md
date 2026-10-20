# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 176 files · ~273,238 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1280 nodes · 3027 edges · 97 communities (47 shown, 50 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 460 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c7912579`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- base_tienda.html
- Pedido
- empleados/views.py
- CuentaCorriente
- Migraciones: auth, clientes, productos
- ModeloEmpleadoUnicoTests
- Abono
- Direcciones de entrega y seed logístico
- django_contrib
- logistica/services.py
- Vistas de clientes
- cuentas/views.py
- logistica/admin.py
- FASE3_LOGISTICA.md
- permisos/tests.py
- Usuario y modelo de abonos
- PROCEDURE.md
- CarritoSoloPorPostTests
- Modelo Cliente
- Planificación de reparto por zona
- What You Must Do When Invoked
- es_admin_o_vendedor
- base.py
- Calendario de reparto
- clientes/forms.py
- DetalleHojaRuta
- Facturación mensual de abonos
- Admin de clientes
- Alta de clientes con/sin cuenta
- crear_cliente_sin_cuenta
- Tests de abonos (RF-05)
- MovimientoCuenta
- registrar_cobro
- Arranque Django (asgi/wsgi)
- django_apps
- roles.py
- Fase 3 · Logística ↔ Pedido
- pedidos/tests.py
- Señal de alta de cliente
- Fase 4 · Cuentas corrientes y abonos
- PagosSegurosTests
- Zona
- permisos/signals.py
- CheckoutRequiereTelefonosTests
- Migración: unificar empleados
- Migración: borrar empleados duplicados
- Migración: métodos de pago
- permisos/apps.py
- autenticacion/migrations/0001_initial.py
- ClientesConfig
- PagoPedido
- autenticacion/apps.py
- ConfirmacionRegresoTests
- graphify reference: extra exports and benchmark
- SesionTests
- BuscarClientesTests
- GuardsUnificadosTests
- Carrito
- EliminarProductoTests
- buscador/apps.py
- carrito/apps.py
- graphify reference: query, path, explain
- cuentas/apps.py
- empleados/apps.py
- 0003_grupos_base.py
- 0004_asignar_grupo_permisos.py
- productos/apps.py
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
3. `Pedido` - 54 edges
4. `Producto` - 51 edges
5. `Zona` - 42 edges
6. `DireccionEntrega` - 38 edges
7. `HojaRuta` - 38 edges
8. `MetodoPago` - 31 edges
9. `DetalleHojaRuta` - 29 edges
10. `CuentaCorriente` - 28 edges

## Surprising Connections (you probably didn't know these)
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `Detalle` --references--> `RegistroUsuarioForm`  [INFERRED]
  .agents/CONTROL_REQUISITOS.md → apps/autenticacion/forms.py
- `2. 🟠 Altos — errores funcionales` --references--> `Usuario`  [INFERRED]
  .agents/AUDITORIA.md → apps/autenticacion/models.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (97 total, 50 thin omitted)

### Community 0 - "base_tienda.html"
Cohesion: 0.07
Nodes (23): 3. 🟡 Medios, IngresarUsuarioForm, RegistroUsuarioForm, Meta, _solo_digitos(), cerrar_sesion(), ingresar_usuario(), perfil_usuario() (+15 more)

### Community 1 - "Pedido"
Cohesion: 0.10
Nodes (17): 1. 🔴 Críticos — seguridad y dinero, Pedido, Meta, aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), cambiar_estado_pago(), cambiar_estado_pedido() (+9 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.06
Nodes (33): 2. 🟠 Altos — errores funcionales, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`) (+25 more)

### Community 3 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 4 - "Migraciones: auth, clientes, productos"
Cohesion: 0.04
Nodes (28): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+20 more)

### Community 5 - "ModeloEmpleadoUnicoTests"
Cohesion: 0.08
Nodes (3): AccesoAVistasLogisticasTests, GruposBaseTests, ModeloEmpleadoUnicoTests

### Community 6 - "Abono"
Cohesion: 0.16
Nodes (11): AbonoForm, Meta, Abono, Meta, cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos() (+3 more)

### Community 7 - "Direcciones de entrega y seed logístico"
Cohesion: 0.12
Nodes (11): DireccionEntrega, Meta, Command, ConfirmacionRegresoTests, EntregaCalleTests, DetallePedido, Meta, CategoriaAdmin (+3 more)

### Community 8 - "django_contrib"
Cohesion: 0.09
Nodes (5): AbonoAdmin, clientes_morosos(), resumen_morosidad(), csrf_failure(), resumen_dashboard()

### Community 9 - "logistica/services.py"
Cohesion: 0.16
Nodes (9): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, bidones_de_pedido(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona(), ruta_default() (+1 more)

### Community 10 - "Vistas de clientes"
Cohesion: 0.25
Nodes (11): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+3 more)

### Community 11 - "cuentas/views.py"
Cohesion: 0.25
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 12 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 13 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (6): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 14 - "permisos/tests.py"
Cohesion: 0.12
Nodes (11): BarrioForm, Meta, RutaRepartoForm, Meta, Command, Barrio, Meta, Camion (+3 more)

### Community 15 - "Usuario y modelo de abonos"
Cohesion: 0.14
Nodes (4): Migration, Usuario, obtener_o_crear_cuenta(), VistasCuentasTests

### Community 16 - "PROCEDURE.md"
Cohesion: 0.15
Nodes (14): Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-04 · ≥2 teléfonos con relación explícita, RF-06 · Catálogo por categorías (+6 more)

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.16
Nodes (5): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), pedidos_candidatos(), GeneracionBorradorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "es_admin_o_vendedor"
Cohesion: 0.06
Nodes (44): Hallazgos nuevos, ActualizarEstadoForm, Meta, CamionForm, Meta, DetalleRutaForm, Meta, HojaRutaForm (+36 more)

### Community 23 - "Calendario de reparto"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "clientes/forms.py"
Cohesion: 0.17
Nodes (6): BuscarClienteForm, ClienteForm, Meta, DireccionEntregaForm, Meta, EditarMiPerfilForm

### Community 25 - "DetalleHojaRuta"
Cohesion: 0.20
Nodes (6): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10), Punto de partida real, _producto_envase_para(), registrar_entrega()

### Community 26 - "Facturación mensual de abonos"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "Admin de clientes"
Cohesion: 0.12
Nodes (11): Detalle, ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, TelefonoContactoAdmin, TelefonoContactoInline, TelefonoContactoForm, Meta (+3 more)

### Community 28 - "Alta de clientes con/sin cuenta"
Cohesion: 0.19
Nodes (6): AltaClienteConCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), listar_clientes(), _texto_buscable()

### Community 29 - "crear_cliente_sin_cuenta"
Cohesion: 0.22
Nodes (4): ClienteSinCuentaForm, Meta, crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 31 - "MovimientoCuenta"
Cohesion: 0.05
Nodes (18): A-D6 — ¿El fiado es sólo Premium o admite excepciones?, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original), 6A — Pagos parciales (RF-13) · ~4 h (+10 more)

### Community 32 - "registrar_cobro"
Cohesion: 0.12
Nodes (14): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)** (+6 more)

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, LogisticaConfig, PedidosConfig

### Community 35 - "roles.py"
Cohesion: 0.07
Nodes (21): roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor_asignado(), es_vendedor(), puede_ver_nota_seguridad(), NotaDeSeguridadTests (+13 more)

### Community 36 - "Fase 3 · Logística ↔ Pedido"
Cohesion: 0.25
Nodes (8): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, RF-16 · Hojas de ruta diarias, RF-17 · Agrupación automática y generación de hojas, RF-19 · Confirmación de entrega por repartidor, RNF-01 · Escalabilidad multi-camión/zona/chofer, RNF-02 · Ocultación de la nota de seguridad

### Community 37 - "pedidos/tests.py"
Cohesion: 0.08
Nodes (11): CheckoutForm, _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), MetodoPago, Meta, _a_decimal(), firma_webhook_valida(), CheckoutFechaEstimadaTests (+3 more)

### Community 38 - "Señal de alta de cliente"
Cohesion: 0.22
Nodes (3): _sincronizar(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 39 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 41 - "Zona"
Cohesion: 0.08
Nodes (9): ZonaForm, Meta, Zona, Meta, HojaRutaCapacidadTests, HojaSinChoferTests, PlanificarRepartoViewTests, ZonaDiasRepartoTests (+1 more)

### Community 42 - "permisos/signals.py"
Cohesion: 0.33
Nodes (3): sincronizar_grupo_empleado(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado()

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 50 - "PagoPedido"
Cohesion: 0.24
Nodes (8): 5B — Promociones prepago (RF-09) · ~6 h, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, PagoPedido, Meta

### Community 52 - "ConfirmacionRegresoTests"
Cohesion: 0.20
Nodes (5): CargaHojaRuta, Meta, confirmar_hoja(), registrar_regreso(), Carga y regreso del camión (sobrantes a stock)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 64 - "Carrito"
Cohesion: 0.12
Nodes (13): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito() (+5 more)

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 507 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **50 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Modelo Cliente` to `Pedido`, `CuentaCorriente`, `ModeloEmpleadoUnicoTests`, `Abono`, `Direcciones de entrega y seed logístico`, `django_contrib`, `logistica/services.py`, `Vistas de clientes`, `cuentas/views.py`, `FASE3_LOGISTICA.md`, `permisos/tests.py`, `Usuario y modelo de abonos`, `PROCEDURE.md`, `Planificación de reparto por zona`, `clientes/forms.py`, `Facturación mensual de abonos`, `Admin de clientes`, `Alta de clientes con/sin cuenta`, `crear_cliente_sin_cuenta`, `Tests de abonos (RF-05)`, `MovimientoCuenta`, `roles.py`, `pedidos/tests.py`, `Señal de alta de cliente`, `Fase 4 · Cuentas corrientes y abonos`, `Zona`, `BuscarClientesTests`, `Carrito`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `base_tienda.html` be split into smaller, more focused modules?**
  _Cohesion score 0.06896551724137931 - nodes in this community are weakly interconnected._
- **Why does `Pedido` connect `Pedido` to `registrar_cobro`, `Carrito`, `empleados/views.py`, `EliminarProductoTests`, `pedidos/tests.py`, `Direcciones de entrega y seed logístico`, `PagosSegurosTests`, `logistica/services.py`, `Vistas de clientes`, `.cambiar_estado_manual`, `CheckoutRequiereTelefonosTests`, `django_contrib`, `PROCEDURE.md`, `PagoPedido`, `Planificación de reparto por zona`, `Modelo Cliente`, `GuardsUnificadosTests`, `MovimientoCuenta`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `Pedido` be split into smaller, more focused modules?**
  _Cohesion score 0.09595959595959595 - nodes in this community are weakly interconnected._