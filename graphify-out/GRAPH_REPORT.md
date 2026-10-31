# Graph Report - distribuidora-3.0  (2026-10-31)

## Corpus Check
- 206 files · ~293,234 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1637 nodes · 4102 edges · 129 communities (66 shown, 63 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 654 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d1226e97`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- productos/views.py
- pedidos/views.py
- empleados/views.py
- vender_promocion
- django_db
- ModeloEmpleadoUnicoTests
- cuentas/views.py
- django_db_models_deletion
- SuscripcionReposicion
- abonos/views.py
- clientes/urls.py
- Empleado
- logistica/services.py
- Producto
- permisos/tests.py
- seed_demo.py
- PROCEDURE.md
- Carrito
- promociones/views.py
- Planificación de reparto por zona
- What You Must Do When Invoked
- logistica/views.py
- Cliente
- logistica/admin.py
- crear_cliente_con_cuenta
- pedidos/tests.py
- Abono
- permisos/signals.py
- CarritoSoloPorPostTests
- ConfirmacionRegresoTests
- Tests de abonos (RF-05)
- CuentaCorriente
- PagosSegurosTests
- Arranque Django (asgi/wsgi)
- django_apps
- CompraPromocion
- Usuario
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- puede_ver_nota_seguridad
- distribuidora/views.py
- registrar_cargo
- logistica/tests.py
- DetallePedido
- SuscripcionReposicion
- Migración: unificar empleados
- GuardsUnificadosTests
- Migración: métodos de pago
- RolSincronizaGrupoTests
- PedidoEspontaneoTests
- SemaforizacionTests
- 6A — Pagos parciales (RF-13) · ~4 h
- CheckoutFechaEstimadaTests
- Command
- graphify reference: extra exports and benchmark
- SesionTests
- clientes/services.py
- CobroManualTests
- base.py
- EliminarProductoTests
- base_tienda.html
- RecorridoRepartidorTests
- graphify reference: query, path, explain
- ver_cliente
- Fase 6 · Pagos parciales y pedido automático
- permisos/views.py
- 0004_asignar_grupo_permisos.py
- webhook_mercadopago
- Verificar cambios — Distribuidora 3.0
- Verificar cambios — Distribuidora 3.0
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- HojaRuta
- Command
- Distribuidora 3.0 / Aquadelluvia
- Barrio
- es_admin_o_vendedor
- roles.py
- promociones/apps.py
- FASE3_LOGISTICA.md
- generar_borradores_periodo
- Fase 4 · Cuentas corrientes y abonos
- permisos/signals.py
- VistasCuentasTests
- DireccionEntrega
- 0007_marcar_botellones.py
- buscador/views.py
- clientes/views.py
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- permisos/apps.py
- ClientesConfig
- DireccionEntregaForm
- autenticacion/apps.py
- buscador/apps.py
- carrito/apps.py
- empleados/apps.py
- productos/apps.py
- H-10 · Suite de tests parcial (faltan carrito y buscador)

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 98 edges
2. `es_admin_o_vendedor()` - 87 edges
3. `Pedido` - 76 edges
4. `Producto` - 66 edges
5. `Zona` - 51 edges
6. `DireccionEntrega` - 50 edges
7. `HojaRuta` - 48 edges
8. `MetodoPago` - 47 edges
9. `Command` - 38 edges
10. `DetalleHojaRuta` - 37 edges

## Surprising Connections (you probably didn't know these)
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `5D — Tests · ~2 h` --references--> `registrar_entrega()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/logistica/services.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `Detalle` --references--> `RegistroUsuarioForm`  [INFERRED]
  .agents/CONTROL_REQUISITOS.md → apps/autenticacion/forms.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (129 total, 63 thin omitted)

### Community 0 - "productos/views.py"
Cohesion: 0.18
Nodes (10): CategoriaForm, Meta, ProductoForm, Meta, Categoria, crear_categoria(), crear_producto(), editar_producto() (+2 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.07
Nodes (22): 1. 🔴 Críticos — seguridad y dinero, fecha_estimada_para_direccion(), CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, pago_en_curso(), cambiar_estado_pago() (+14 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.24
Nodes (12): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+4 more)

### Community 3 - "vender_promocion"
Cohesion: 0.10
Nodes (8): consumir_saldo(), revertir_consumos(), vender_promocion(), BasePromociones, CheckoutConSaldoTests, EscenarioAceptacionTests, ReglasDeSaldoTests, VistasPromocionesTests

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (24): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+16 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.25
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "django_db_models_deletion"
Cohesion: 0.06
Nodes (18): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+10 more)

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "abonos/views.py"
Cohesion: 0.28
Nodes (9): AbonoForm, Meta, cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono() (+1 more)

### Community 10 - "clientes/urls.py"
Cohesion: 0.40
Nodes (9): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), eliminar_direccion(), eliminar_telefono(), es_dueno_o_staff() (+1 more)

### Community 11 - "Empleado"
Cohesion: 0.17
Nodes (8): 2. 🟠 Altos — errores funcionales, EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta, PantallasDeRolesTests

### Community 12 - "logistica/services.py"
Cohesion: 0.08
Nodes (19): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), confirmar_entrega_en_calle(), crear_hoja_borrador() (+11 more)

### Community 13 - "Producto"
Cohesion: 0.16
Nodes (8): ItemCarrito, Meta, MetodoPago, Meta, CategoriaAdmin, ProductoAdmin, Producto, VenderPromocionForm

### Community 14 - "permisos/tests.py"
Cohesion: 0.10
Nodes (8): RutaRepartoForm, Meta, CargaHojaRuta, Meta, RutaReparto, Meta, AccesoAVistasLogisticasTests, Carga y regreso del camión (sobrantes a stock)

### Community 15 - "seed_demo.py"
Cohesion: 0.16
Nodes (4): obtener_o_crear_cuenta(), Command, saldo_vigente(), vencer_promociones()

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (14): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose (+6 more)

### Community 17 - "Carrito"
Cohesion: 0.24
Nodes (8): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), solo_clientes(), redirigir_a_origen()

### Community 18 - "promociones/views.py"
Cohesion: 0.13
Nodes (10): PromocionForm, Meta, Promocion, Meta, promociones_por_vencer(), crear_promocion(), editar_promocion(), _form_promocion() (+2 more)

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.17
Nodes (4): clientes_frecuentes_de_zona(), construir_borrador(), pedidos_candidatos(), GeneracionBorradorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "logistica/views.py"
Cohesion: 0.07
Nodes (35): Hallazgos nuevos, CamionForm, Meta, Camion, Meta, actualizar_estado_entrega(), agregar_parada(), agregar_pedido_parada() (+27 more)

### Community 23 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 24 - "crear_cliente_con_cuenta"
Cohesion: 0.12
Nodes (8): AltaClienteConCuentaForm, Meta, ClienteSinCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 25 - "pedidos/tests.py"
Cohesion: 0.14
Nodes (6): firma_webhook_valida(), resumen_caja(), stock_comprometido(), stock_disponible(), _firmar(), StockComprometidoTests

### Community 26 - "Abono"
Cohesion: 0.10
Nodes (7): AbonoAdmin, Command, Abono, Meta, generar_cargos_mensuales(), FacturacionTests, RF-15 · Alquiler de dispensers (abonos)

### Community 29 - "ConfirmacionRegresoTests"
Cohesion: 0.12
Nodes (8): carga_sugerida(), confirmar_hoja(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), ConfirmacionRegresoTests, _productos_para_carga(), registrar_regreso_ruta()

### Community 31 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 32 - "PagosSegurosTests"
Cohesion: 0.18
Nodes (4): _a_decimal(), aplicar_pago_mercadopago(), registrar_pago_manual(), PagosSegurosTests

### Community 34 - "django_apps"
Cohesion: 0.15
Nodes (4): AbonosConfig, CuentasConfig, LogisticaConfig, PedidosConfig

### Community 35 - "CompraPromocion"
Cohesion: 0.16
Nodes (7): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, CompraPromocion, Meta, ConsumoPromocion, Meta

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.29
Nodes (7): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`)

### Community 39 - "distribuidora/views.py"
Cohesion: 0.19
Nodes (3): clientes_morosos(), resumen_morosidad(), resumen_dashboard()

### Community 40 - "registrar_cargo"
Cohesion: 0.11
Nodes (9): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests (+1 more)

### Community 41 - "logistica/tests.py"
Cohesion: 0.07
Nodes (12): ZonaForm, Meta, Zona, Meta, generar_borradores_periodo(), GeneracionQuincenalTests, HojaRutaCapacidadTests, HojaSinChoferTests (+4 more)

### Community 42 - "DetallePedido"
Cohesion: 0.19
Nodes (11): 5B — Promociones prepago (RF-09) · ~6 h, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido (+3 more)

### Community 43 - "SuscripcionReposicion"
Cohesion: 0.08
Nodes (22): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h (+14 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 47 - "RolSincronizaGrupoTests"
Cohesion: 0.23
Nodes (3): EmpleadoForm, Meta, RolSincronizaGrupoTests

### Community 48 - "PedidoEspontaneoTests"
Cohesion: 0.23
Nodes (3): botellones_por_producto(), entregados_por_producto(), PedidoEspontaneoTests

### Community 50 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.21
Nodes (5): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 6A — Pagos parciales (RF-13) · ~4 h, Pedido, Meta

### Community 51 - "CheckoutFechaEstimadaTests"
Cohesion: 0.20
Nodes (3): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests

### Community 52 - "Command"
Cohesion: 0.09
Nodes (8): _a_dt(), Command, CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "clientes/services.py"
Cohesion: 0.06
Nodes (12): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), AgregarDireccionTests, BuscarClientesTests (+4 more)

### Community 56 - "CobroManualTests"
Cohesion: 0.13
Nodes (3): CobroManualTests, PagosParcialesTests, TransicionesManualesTests

### Community 67 - "base_tienda.html"
Cohesion: 0.29
Nodes (4): csrf_failure(), listar_productos(), ver_producto(), inicio()

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "ver_cliente"
Cohesion: 0.18
Nodes (5): _contexto_suscripcion(), editar_mi_perfil(), mi_perfil_cliente(), ver_cliente(), compras_vigentes()

### Community 71 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 72 - "permisos/views.py"
Cohesion: 0.11
Nodes (9): IngresarUsuarioForm, RegistroUsuarioForm, Meta, _solo_digitos(), cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario() (+1 more)

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 75 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 76 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 98 - "HojaRuta"
Cohesion: 0.24
Nodes (4): HojaRutaForm, Meta, HojaRuta, Meta

### Community 100 - "Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 101 - "Barrio"
Cohesion: 0.10
Nodes (14): ActualizarEstadoForm, Meta, AgregarParadaForm, BarrioForm, Meta, _etiqueta_direccion_cliente(), Barrio, Meta (+6 more)

### Community 103 - "roles.py"
Cohesion: 0.29
Nodes (9): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_vendedor(), 2. Revisar convenciones del proyecto en lo que cambió (+1 more)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (6): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.25
Nodes (6): Fase 4 · Cuentas corrientes y abonos, Fase 5 · Bidones y promociones prepago, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos, RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 109 - "permisos/signals.py"
Cohesion: 0.21
Nodes (6): retirar_perfil_cliente_vacio(), sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 114 - "DireccionEntrega"
Cohesion: 0.06
Nodes (18): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original), ClienteAdmin, DireccionEntregaAdmin (+10 more)

### Community 116 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 121 - "clientes/views.py"
Cohesion: 0.13
Nodes (11): BuscarClienteForm, ClienteForm, Meta, EditarMiPerfilForm, MovimientoBidonForm, TelefonoContactoForm, Meta, listar_clientes() (+3 more)

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 663 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **63 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/views.py`, `vender_promocion`, `cuentas/views.py`, `abonos/views.py`, `clientes/urls.py`, `logistica/services.py`, `permisos/tests.py`, `seed_demo.py`, `PROCEDURE.md`, `promociones/views.py`, `Planificación de reparto por zona`, `logistica/views.py`, `crear_cliente_con_cuenta`, `pedidos/tests.py`, `Abono`, `permisos/signals.py`, `ConfirmacionRegresoTests`, `Tests de abonos (RF-05)`, `CuentaCorriente`, `Usuario`, `puede_ver_nota_seguridad`, `distribuidora/views.py`, `registrar_cargo`, `logistica/tests.py`, `DetallePedido`, `SuscripcionReposicion`, `PedidoEspontaneoTests`, `SemaforizacionTests`, `6A — Pagos parciales (RF-13) · ~4 h`, `CheckoutFechaEstimadaTests`, `Command`, `clientes/services.py`, `CobroManualTests`, `RecorridoRepartidorTests`, `ver_cliente`, `FASE3_LOGISTICA.md`, `Fase 4 · Cuentas corrientes y abonos`, `permisos/signals.py`, `VistasCuentasTests`, `DireccionEntrega`, `clientes/views.py`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Are the 60 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 60 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07138047138047138 - nodes in this community are weakly interconnected._
- **Why does `Pedido` connect `6A — Pagos parciales (RF-13) · ~4 h` to `pedidos/views.py`, `vender_promocion`, `SuscripcionReposicion`, `Empleado`, `logistica/services.py`, `Producto`, `seed_demo.py`, `PROCEDURE.md`, `Planificación de reparto por zona`, `logistica/views.py`, `Cliente`, `pedidos/tests.py`, `ConfirmacionRegresoTests`, `PagosSegurosTests`, `distribuidora/views.py`, `logistica/tests.py`, `DetallePedido`, `SuscripcionReposicion`, `GuardsUnificadosTests`, `Command`, `clientes/services.py`, `CobroManualTests`, `EliminarProductoTests`, `ver_cliente`, `webhook_mercadopago`, `DireccionEntrega`, `clientes/views.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `vender_promocion` be split into smaller, more focused modules?**
  _Cohesion score 0.0953058321479374 - nodes in this community are weakly interconnected._