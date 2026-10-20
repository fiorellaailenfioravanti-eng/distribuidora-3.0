# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 178 files · ~274,036 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1306 nodes · 3083 edges · 119 communities (65 shown, 54 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 472 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dca044e4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Producto
- Pedido
- empleados/views.py
- CuentaCorriente
- django_db
- ModeloEmpleadoUnicoTests
- Abono
- DireccionEntrega
- distribuidora/views.py
- logistica/services.py
- Vistas de clientes
- django_db_models_deletion
- logistica/admin.py
- FASE3_LOGISTICA.md
- Barrio
- Usuario y modelo de abonos
- PROCEDURE.md
- permisos/tests.py
- Modelo Cliente
- Planificación de reparto por zona
- What You Must Do When Invoked
- logistica/urls.py
- base.py
- Calendario de reparto
- clientes/forms.py
- DetalleHojaRuta
- Facturación mensual de abonos
- Admin de clientes
- Alta de clientes con/sin cuenta
- RegistroUsuarioForm
- Tests de abonos (RF-05)
- registrar_cargo
- 🏁 Plan de Cierre — Fases 4.5 a 7
- Arranque Django (asgi/wsgi)
- django_apps
- puede_ver_nota_seguridad
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
- VariasDireccionesTests
- GuardsUnificadosTests
- confirmar_pedido
- EliminarProductoTests
- buscador/apps.py
- carrito/apps.py
- graphify reference: query, path, explain
- cuentas/apps.py
- empleados/apps.py
- 0003_grupos_base.py
- 0004_asignar_grupo_permisos.py
- productos/apps.py
- Pedido
- logistica/tests.py
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- base_dashboard.html
- logistica/views.py
- registrar_cobro
- ConfirmacionRegresoTests
- es_admin_o_vendedor
- roles.py
- Usuario
- SemaforizacionTests
- HojaRuta
- MovimientoCuenta
- generar_borradores_periodo
- actualizar_estado_entrega
- AccesoAVistasLogisticasTests
- VistasCuentasTests
- ZonaForm
- TransicionesManualesTests
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- cuentas/admin.py
- Verificar cambios — Distribuidora 3.0
- Verificar cambios — Distribuidora 3.0
- 0006_corregir_ayuda_desc_seguridad.py

## God Nodes (most connected - your core abstractions)
1. `es_admin_o_vendedor()` - 81 edges
2. `Cliente` - 75 edges
3. `Pedido` - 55 edges
4. `Producto` - 51 edges
5. `Zona` - 47 edges
6. `HojaRuta` - 40 edges
7. `DireccionEntrega` - 39 edges
8. `MetodoPago` - 32 edges
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

## Communities (119 total, 54 thin omitted)

### Community 0 - "Producto"
Cohesion: 0.06
Nodes (27): carrito_total(), Carrito, ItemCarrito, Meta, CarritoSoloPorPostTests, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito() (+19 more)

### Community 1 - "Pedido"
Cohesion: 0.13
Nodes (9): cambiar_estado_pago(), cambiar_estado_pedido(), checkout(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente() (+1 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.09
Nodes (18): buscar_productos(), EmpleadoForm, Meta, RolEmpleadoForm, Meta, RolSincronizaGrupoTests, cambiar_estado_empleado(), crear_empleado() (+10 more)

### Community 3 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 4 - "django_db"
Cohesion: 0.06
Nodes (15): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+7 more)

### Community 6 - "Abono"
Cohesion: 0.07
Nodes (21): AbonoAdmin, AbonoForm, Meta, Abono, Meta, cambiar_estado_abono(), crear_abono(), editar_abono() (+13 more)

### Community 7 - "DireccionEntrega"
Cohesion: 0.14
Nodes (7): DireccionEntrega, Meta, Command, EntregaCalleTests, DetallePedido, Meta, RF-03 · Multidirección de entrega

### Community 8 - "distribuidora/views.py"
Cohesion: 0.24
Nodes (3): clientes_morosos(), resumen_morosidad(), resumen_dashboard()

### Community 9 - "logistica/services.py"
Cohesion: 0.23
Nodes (6): bidones_de_pedido(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona(), ruta_default(), _texto_direccion()

### Community 10 - "Vistas de clientes"
Cohesion: 0.24
Nodes (11): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+3 more)

### Community 11 - "django_db_models_deletion"
Cohesion: 0.08
Nodes (13): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+5 more)

### Community 12 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 13 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (6): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 14 - "Barrio"
Cohesion: 0.18
Nodes (5): BarrioForm, Meta, Command, Barrio, Meta

### Community 16 - "PROCEDURE.md"
Cohesion: 0.16
Nodes (14): Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-04 · ≥2 teléfonos con relación explícita, RF-06 · Catálogo por categorías, RF-09 · Promociones prepago "paga 3 lleva 4" (+6 more)

### Community 17 - "permisos/tests.py"
Cohesion: 0.16
Nodes (6): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.18
Nodes (4): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "logistica/urls.py"
Cohesion: 0.20
Nodes (12): Hallazgos nuevos, DetalleRutaForm, Meta, agregar_parada(), confirmar_ruta(), editar_ruta(), eliminar_camion(), eliminar_parada() (+4 more)

### Community 23 - "Calendario de reparto"
Cohesion: 0.20
Nodes (4): fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "clientes/forms.py"
Cohesion: 0.12
Nodes (8): BuscarClienteForm, ClienteForm, Meta, ClienteSinCuentaForm, Meta, DireccionEntregaForm, Meta, EditarMiPerfilForm

### Community 25 - "DetalleHojaRuta"
Cohesion: 0.20
Nodes (7): 5A — Historial de envases (RF-08) · ~4 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10), Punto de partida real, _producto_envase_para(), registrar_entrega()

### Community 26 - "Facturación mensual de abonos"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "Admin de clientes"
Cohesion: 0.12
Nodes (11): Detalle, ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, TelefonoContactoAdmin, TelefonoContactoInline, TelefonoContactoForm, Meta (+3 more)

### Community 28 - "Alta de clientes con/sin cuenta"
Cohesion: 0.14
Nodes (8): AltaClienteConCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos(), listar_clientes(), _texto_buscable()

### Community 29 - "RegistroUsuarioForm"
Cohesion: 0.13
Nodes (9): 3. 🟡 Medios, IngresarUsuarioForm, RegistroUsuarioForm, Meta, _solo_digitos(), cerrar_sesion(), ingresar_usuario(), perfil_usuario() (+1 more)

### Community 31 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 32 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.22
Nodes (7): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 7 — QA, producción y tesis 🎓, 🏁 Plan de Cierre — Fases 4.5 a 7

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, LogisticaConfig, PedidosConfig

### Community 35 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (5): puede_ver_nota_seguridad(), NotaDeSeguridadTests, Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 36 - "Fase 3 · Logística ↔ Pedido"
Cohesion: 0.25
Nodes (8): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, RF-16 · Hojas de ruta diarias, RF-17 · Agrupación automática y generación de hojas, RF-19 · Confirmación de entrega por repartidor, RNF-01 · Escalabilidad multi-camión/zona/chofer, RNF-02 · Ocultación de la nota de seguridad

### Community 37 - "pedidos/tests.py"
Cohesion: 0.10
Nodes (15): CheckoutForm, metodos_pago_checkout_web(), MetodoPago, Meta, PagoPedido, Meta, _a_decimal(), aplicar_pago_mercadopago() (+7 more)

### Community 38 - "Señal de alta de cliente"
Cohesion: 0.22
Nodes (3): _sincronizar(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 39 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 41 - "Zona"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 42 - "permisos/signals.py"
Cohesion: 0.33
Nodes (3): sincronizar_grupo_empleado(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado()

### Community 43 - "CheckoutRequiereTelefonosTests"
Cohesion: 0.15
Nodes (4): _etiqueta_direccion_con_fecha(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, PagosParcialesTests

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 50 - "PagoPedido"
Cohesion: 0.38
Nodes (5): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin

### Community 52 - "ConfirmacionRegresoTests"
Cohesion: 0.20
Nodes (5): CargaHojaRuta, Meta, confirmar_hoja(), registrar_regreso(), Carga y regreso del camión (sobrantes a stock)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "VariasDireccionesTests"
Cohesion: 0.12
Nodes (4): AgregarDireccionTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, VariasDireccionesTests

### Community 64 - "confirmar_pedido"
Cohesion: 0.22
Nodes (7): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18), Punto de partida real, _cliente_puede_comprar(), confirmar_pedido()

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 75 - "Pedido"
Cohesion: 0.15
Nodes (7): 2. 🟠 Altos — errores funcionales, A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, Pedido, Meta

### Community 76 - "logistica/tests.py"
Cohesion: 0.13
Nodes (12): ActualizarEstadoForm, Meta, RutaRepartoForm, Meta, CalendarioExcepcion, Meta, Camion, Meta (+4 more)

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 98 - "base_dashboard.html"
Cohesion: 0.19
Nodes (9): CamionForm, Meta, crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_zona(), listar_camiones(), listar_rutas() (+1 more)

### Community 99 - "logistica/views.py"
Cohesion: 0.18
Nodes (9): carga_sugerida(), _cargas_confirmacion_desde_post(), _int_o_none(), _parse_fecha(), planificar_reparto(), _productos_para_carga(), _regreso_desde_post(), _seleccion_desde_post() (+1 more)

### Community 100 - "registrar_cobro"
Cohesion: 0.14
Nodes (11): 1. 🔴 Críticos — seguridad y dinero, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`) (+3 more)

### Community 101 - "ConfirmacionRegresoTests"
Cohesion: 0.13
Nodes (4): ConfirmacionRegresoTests, GeneracionQuincenalTests, HojaRutaCapacidadTests, HojaSinChoferTests

### Community 102 - "es_admin_o_vendedor"
Cohesion: 0.21
Nodes (3): es_admin_o_vendedor(), es_admin_vendedor_o_repartidor(), EvaluacionDeRolesTests

### Community 103 - "roles.py"
Cohesion: 0.31
Nodes (8): roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_vendedor(), 2. Revisar convenciones del proyecto en lo que cambió, 2. Revisar convenciones del proyecto en lo que cambió

### Community 106 - "HojaRuta"
Cohesion: 0.24
Nodes (4): HojaRutaForm, Meta, HojaRuta, Meta

### Community 107 - "MovimientoCuenta"
Cohesion: 0.22
Nodes (3): MovimientoCuenta, Meta, ReglaFiadoTests

### Community 108 - "generar_borradores_periodo"
Cohesion: 0.22
Nodes (3): Command, generar_borradores_periodo(), pedidos_candidatos()

### Community 109 - "actualizar_estado_entrega"
Cohesion: 0.22
Nodes (5): actualizar_estado_entrega(), _ids_de_paradas_con_nota(), mi_ruta_hoy(), es_repartidor_asignado(), obtener_empleado()

### Community 112 - "ZonaForm"
Cohesion: 0.43
Nodes (3): ZonaForm, Meta, ZonaFormTests

### Community 114 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.33
Nodes (5): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 115 - "cuentas/admin.py"
Cohesion: 0.50
Nodes (3): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

### Community 116 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 117 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

## Knowledge Gaps
- **1 isolated node(s):** `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 519 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **54 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Modelo Cliente` to `Producto`, `Pedido`, `CuentaCorriente`, `Abono`, `DireccionEntrega`, `distribuidora/views.py`, `logistica/services.py`, `Vistas de clientes`, `FASE3_LOGISTICA.md`, `Usuario y modelo de abonos`, `PROCEDURE.md`, `permisos/tests.py`, `Planificación de reparto por zona`, `clientes/forms.py`, `Facturación mensual de abonos`, `Admin de clientes`, `Alta de clientes con/sin cuenta`, `Tests de abonos (RF-05)`, `registrar_cargo`, `puede_ver_nota_seguridad`, `pedidos/tests.py`, `Señal de alta de cliente`, `Fase 4 · Cuentas corrientes y abonos`, `CheckoutRequiereTelefonosTests`, `VariasDireccionesTests`, `confirmar_pedido`, `Pedido`, `logistica/tests.py`, `ConfirmacionRegresoTests`, `Usuario`, `SemaforizacionTests`, `MovimientoCuenta`, `AccesoAVistasLogisticasTests`, `VistasCuentasTests`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Producto` be split into smaller, more focused modules?**
  _Cohesion score 0.059125085440874914 - nodes in this community are weakly interconnected._
- **Why does `es_admin_o_vendedor()` connect `es_admin_o_vendedor` to `Producto`, `Pedido`, `empleados/views.py`, `logistica/views.py`, `registrar_cobro`, `base_dashboard.html`, `Abono`, `pedidos/tests.py`, `roles.py`, `puede_ver_nota_seguridad`, `Vistas de clientes`, `Pedido`, `distribuidora/views.py`, `actualizar_estado_entrega`, `permisos/tests.py`, `logistica/urls.py`, `Alta de clientes con/sin cuenta`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Should `Pedido` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._