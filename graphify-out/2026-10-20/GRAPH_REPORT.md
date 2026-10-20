# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 181 files · ~277,487 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1358 nodes · 3247 edges · 109 communities (54 shown, 55 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 493 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6409ff1d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- base_tienda.html
- Pedido
- empleados/views.py
- Command
- django_db
- GruposBaseTests
- Abono
- DireccionEntrega
- django_urls
- CarritoSoloPorPostTests
- Vistas de clientes
- django_db_models_deletion
- logistica/admin.py
- FASE3_LOGISTICA.md
- Barrio
- Usuario y modelo de abonos
- PROCEDURE.md
- Producto
- Modelo Cliente
- Planificación de reparto por zona
- What You Must Do When Invoked
- es_admin_o_vendedor
- base.py
- Calendario de reparto
- clientes/forms.py
- DetalleHojaRuta
- Abono
- Admin de clientes
- Alta de clientes con/sin cuenta
- CheckoutRequiereTelefonosTests
- Tests de abonos (RF-05)
- MovimientoCuenta
- registrar_cobro
- django_apps
- puede_ver_nota_seguridad
- Fase 5 · Bidones y promociones prepago
- pedidos/services.py
- Señal de alta de cliente
- Fase 4 · Cuentas corrientes y abonos
- PagosSegurosTests
- Zona
- permisos/signals.py
- pedidos/tests.py
- Migración: unificar empleados
- Migración: borrar empleados duplicados
- Migración: métodos de pago
- permisos/apps.py
- DireccionEntregaForm
- ClientesConfig
- PagoPedido
- autenticacion/apps.py
- logistica/services.py
- graphify reference: extra exports and benchmark
- SesionTests
- VariasDireccionesTests
- GuardsUnificadosTests
- pedidos/views.py
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
- Distribuidora 3.0 / Aquadelluvia
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- registrar_cobro
- logistica/tests.py
- es_admin_o_vendedor
- roles.py
- HojaRuta
- Command
- AccesoAVistasLogisticasTests
- VistasCuentasTests
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- Verificar cambios — Distribuidora 3.0
- Verificar cambios — Distribuidora 3.0

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 82 edges
2. `es_admin_o_vendedor()` - 82 edges
3. `Pedido` - 56 edges
4. `Producto` - 51 edges
5. `Zona` - 47 edges
6. `HojaRuta` - 44 edges
7. `DireccionEntrega` - 39 edges
8. `Command` - 35 edges
9. `MetodoPago` - 32 edges
10. `DetalleHojaRuta` - 31 edges

## Surprising Connections (you probably didn't know these)
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Carga y regreso del camión (sobrantes a stock)` --references--> `CargaHojaRuta`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `Detalle` --references--> `RegistroUsuarioForm`  [INFERRED]
  .agents/CONTROL_REQUISITOS.md → apps/autenticacion/forms.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (109 total, 55 thin omitted)

### Community 0 - "base_tienda.html"
Cohesion: 0.07
Nodes (23): 3. 🟡 Medios, IngresarUsuarioForm, RegistroUsuarioForm, Meta, _solo_digitos(), cerrar_sesion(), ingresar_usuario(), perfil_usuario() (+15 more)

### Community 1 - "Pedido"
Cohesion: 0.13
Nodes (9): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr() (+1 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.06
Nodes (28): 2. 🟠 Altos — errores funcionales, Usuario, buscar_productos(), EmpleadoAdmin, RolEmpleadoAdmin, EmpleadoForm, Meta, RolEmpleadoForm (+20 more)

### Community 3 - "Command"
Cohesion: 0.10
Nodes (8): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), _a_dt(), Command

### Community 4 - "django_db"
Cohesion: 0.05
Nodes (17): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+9 more)

### Community 6 - "Abono"
Cohesion: 0.06
Nodes (24): AbonoForm, Meta, cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono() (+16 more)

### Community 7 - "DireccionEntrega"
Cohesion: 0.15
Nodes (8): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, DireccionEntrega, Meta

### Community 8 - "django_urls"
Cohesion: 0.29
Nodes (6): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito()

### Community 10 - "Vistas de clientes"
Cohesion: 0.26
Nodes (11): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+3 more)

### Community 11 - "django_db_models_deletion"
Cohesion: 0.06
Nodes (16): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+8 more)

### Community 12 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 13 - "FASE3_LOGISTICA.md"
Cohesion: 0.22
Nodes (5): Arquitectura visual dual: Tienda vs Dashboard, Carga y regreso del camión (sobrantes a stock), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 14 - "Barrio"
Cohesion: 0.15
Nodes (9): BarrioForm, Meta, RutaRepartoForm, Meta, Command, Barrio, Meta, RutaReparto (+1 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (16): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-04 · ≥2 teléfonos con relación explícita (+8 more)

### Community 17 - "Producto"
Cohesion: 0.15
Nodes (6): ItemCarrito, Meta, CategoriaAdmin, ProductoAdmin, Producto, H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.18
Nodes (4): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "es_admin_o_vendedor"
Cohesion: 0.07
Nodes (44): Hallazgos nuevos, ActualizarEstadoForm, Meta, CamionForm, Meta, DetalleRutaForm, Meta, HojaRutaForm (+36 more)

### Community 23 - "Calendario de reparto"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "clientes/forms.py"
Cohesion: 0.12
Nodes (8): BuscarClienteForm, ClienteForm, Meta, ClienteSinCuentaForm, Meta, EditarMiPerfilForm, MovimientoBidonForm, registrar_movimiento_bidon()

### Community 25 - "DetalleHojaRuta"
Cohesion: 0.10
Nodes (11): 5A — Historial de envases (RF-08) · ~4 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10), Punto de partida real, HistorialBidonesTests, DetalleHojaRuta, Meta (+3 more)

### Community 26 - "Abono"
Cohesion: 0.10
Nodes (7): AbonoAdmin, Command, Abono, Meta, generar_cargos_mensuales(), FacturacionTests, RF-15 · Alquiler de dispensers (abonos)

### Community 27 - "Admin de clientes"
Cohesion: 0.17
Nodes (6): Detalle, TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente()

### Community 28 - "Alta de clientes con/sin cuenta"
Cohesion: 0.14
Nodes (8): AltaClienteConCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos(), listar_clientes(), _texto_buscable()

### Community 31 - "MovimientoCuenta"
Cohesion: 0.08
Nodes (10): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests (+2 more)

### Community 32 - "registrar_cobro"
Cohesion: 0.14
Nodes (10): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 7 — QA, producción y tesis 🎓, 🏁 Plan de Cierre — Fases 4.5 a 7 (+2 more)

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, LogisticaConfig, PedidosConfig

### Community 36 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 37 - "pedidos/services.py"
Cohesion: 0.19
Nodes (5): _a_decimal(), aplicar_pago_mercadopago(), firma_webhook_valida(), pago_en_curso(), _firmar()

### Community 38 - "Señal de alta de cliente"
Cohesion: 0.22
Nodes (3): _sincronizar(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 39 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.22
Nodes (7): Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-16 · Hojas de ruta diarias, RF-17 · Agrupación automática y generación de hojas, RF-19 · Confirmación de entrega por repartidor, RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 41 - "Zona"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 42 - "permisos/signals.py"
Cohesion: 0.33
Nodes (3): sincronizar_grupo_empleado(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado()

### Community 43 - "pedidos/tests.py"
Cohesion: 0.11
Nodes (8): CheckoutForm, _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), MetodoPago, Meta, CheckoutFechaEstimadaTests, PagosParcialesTests, TransicionesManualesTests

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 50 - "PagoPedido"
Cohesion: 0.20
Nodes (10): 5B — Promociones prepago (RF-09) · ~6 h, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, DetallePedido, Meta (+2 more)

### Community 52 - "logistica/services.py"
Cohesion: 0.14
Nodes (10): CargaHojaRuta, Meta, bidones_de_pedido(), confirmar_hoja(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona(), registrar_regreso() (+2 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "VariasDireccionesTests"
Cohesion: 0.12
Nodes (4): AgregarDireccionTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, VariasDireccionesTests

### Community 64 - "pedidos/views.py"
Cohesion: 0.17
Nodes (5): consultar_pago_mercadopago(), _cliente_puede_comprar(), confirmar_pedido(), pago_exitoso(), webhook_mercadopago()

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 75 - "Pedido"
Cohesion: 0.15
Nodes (8): 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18), Punto de partida real, Pedido, Meta

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

### Community 100 - "registrar_cobro"
Cohesion: 0.20
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), confirmar_pago_qr() (+1 more)

### Community 101 - "logistica/tests.py"
Cohesion: 0.11
Nodes (5): ConfirmacionRegresoTests, HojaRutaCapacidadTests, HojaSinChoferTests, PlanificarRepartoViewTests, SeedDemoTests

### Community 103 - "roles.py"
Cohesion: 0.24
Nodes (10): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_repartidor_asignado(), es_vendedor() (+2 more)

### Community 106 - "HojaRuta"
Cohesion: 0.15
Nodes (5): HojaRuta, Meta, generar_borradores_periodo(), pedidos_candidatos(), GeneracionQuincenalTests

### Community 114 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.20
Nodes (7): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 116 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 117 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 541 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **55 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Modelo Cliente` to `base_tienda.html`, `Command`, `Abono`, `DireccionEntrega`, `Vistas de clientes`, `Usuario y modelo de abonos`, `PROCEDURE.md`, `Producto`, `Planificación de reparto por zona`, `clientes/forms.py`, `DetalleHojaRuta`, `Abono`, `Admin de clientes`, `Alta de clientes con/sin cuenta`, `Tests de abonos (RF-05)`, `MovimientoCuenta`, `puede_ver_nota_seguridad`, `Fase 5 · Bidones y promociones prepago`, `Señal de alta de cliente`, `Fase 4 · Cuentas corrientes y abonos`, `pedidos/tests.py`, `logistica/services.py`, `VariasDireccionesTests`, `pedidos/views.py`, `Pedido`, `logistica/tests.py`, `es_admin_o_vendedor`, `HojaRuta`, `AccesoAVistasLogisticasTests`, `VistasCuentasTests`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 47 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 47 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `base_tienda.html` be split into smaller, more focused modules?**
  _Cohesion score 0.06612021857923497 - nodes in this community are weakly interconnected._
- **Why does `es_admin_o_vendedor()` connect `es_admin_o_vendedor` to `pedidos/views.py`, `base_tienda.html`, `empleados/views.py`, `Pedido`, `puede_ver_nota_seguridad`, `Abono`, `roles.py`, `django_urls`, `es_admin_o_vendedor`, `Vistas de clientes`, `Pedido`, `Distribuidora 3.0 / Aquadelluvia`, `clientes/forms.py`, `Alta de clientes con/sin cuenta`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `Pedido` be split into smaller, more focused modules?**
  _Cohesion score 0.12923076923076923 - nodes in this community are weakly interconnected._