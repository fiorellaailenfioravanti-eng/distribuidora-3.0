# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 195 files · ~282,242 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1462 nodes · 3563 edges · 118 communities (61 shown, 57 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 537 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `21fd91f0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- listar_productos_admin
- Pedido
- empleados/views.py
- vender_promocion
- django_db
- GruposBaseTests
- cuentas/views.py
- DireccionEntrega
- django_urls
- CarritoSoloPorPostTests
- Cliente
- autenticacion/migrations/0001_initial.py
- logistica/admin.py
- Producto
- Barrio
- promociones/tests.py
- PROCEDURE.md
- django_urls
- promociones/views.py
- Planificación de reparto por zona
- What You Must Do When Invoked
- logistica/views.py
- base_dashboard.html
- Calendario de reparto
- CuentaCorriente
- DetalleHojaRuta
- generar_cargos_mensuales
- clientes/signals.py
- Abono
- DireccionEntrega
- Tests de abonos (RF-05)
- MovimientoCuenta
- 🏁 Plan de Cierre — Fases 4.5 a 7
- Arranque Django (asgi/wsgi)
- django_apps
- puede_ver_nota_seguridad
- abonos/views.py
- pedidos/services.py
- permisos/signals.py
- distribuidora/views.py
- PagosSegurosTests
- Zona
- django_contrib
- pedidos/forms.py
- Migración: unificar empleados
- Migración: borrar empleados duplicados
- Migración: métodos de pago
- permisos/apps.py
- autenticacion/views.py
- ClientesConfig
- PagoPedido
- RegistroUsuarioForm
- seed_demo.py
- graphify reference: extra exports and benchmark
- SesionTests
- VariasDireccionesTests
- TransicionesManualesTests
- pedidos/views.py
- EliminarProductoTests
- buscador/apps.py
- carrito/apps.py
- graphify reference: query, path, explain
- cuentas/apps.py
- empleados/apps.py
- vencer_promociones
- 0004_asignar_grupo_permisos.py
- CompraPromocion
- 6A — Pagos parciales (RF-13) · ~4 h
- listar_zonas
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- HojaRuta
- promociones/admin.py
- registrar_cobro
- logistica/tests.py
- es_admin_o_vendedor
- roles.py
- VistasPromocionesTests
- 0006_corregir_ayuda_desc_seguridad.py
- HojaRuta
- carga_sugerida
- logistica/apps.py
- pedidos/apps.py
- promociones/apps.py
- VistasCuentasTests
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- Verificar cambios — Distribuidora 3.0
- Verificar cambios — Distribuidora 3.0

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 88 edges
2. `es_admin_o_vendedor()` - 86 edges
3. `Pedido` - 63 edges
4. `Producto` - 56 edges
5. `Zona` - 47 edges
6. `HojaRuta` - 44 edges
7. `DireccionEntrega` - 41 edges
8. `Command` - 38 edges
9. `MetodoPago` - 36 edges
10. `DetalleHojaRuta` - 31 edges

## Surprising Connections (you probably didn't know these)
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `5. 🔗 Dependencias y archivos compartidos` --references--> `registrar_cobro()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/pedidos/services.py
- `Detalle` --references--> `RegistroUsuarioForm`  [INFERRED]
  .agents/CONTROL_REQUISITOS.md → apps/autenticacion/forms.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (118 total, 57 thin omitted)

### Community 0 - "listar_productos_admin"
Cohesion: 0.21
Nodes (7): crear_categoria(), crear_producto(), editar_producto(), eliminar_producto(), listar_productos(), listar_productos_admin(), ver_producto()

### Community 1 - "Pedido"
Cohesion: 0.16
Nodes (7): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_qr(), redirigir_a_origen()

### Community 2 - "empleados/views.py"
Cohesion: 0.06
Nodes (26): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoAdmin, RolEmpleadoAdmin, EmpleadoForm, Meta, RolEmpleadoForm, Meta (+18 more)

### Community 3 - "vender_promocion"
Cohesion: 0.15
Nodes (7): consumir_saldo(), revertir_consumos(), vender_promocion(), BasePromociones, CheckoutConSaldoTests, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.04
Nodes (31): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+23 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.25
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "DireccionEntrega"
Cohesion: 0.22
Nodes (4): ClienteAdmin, DireccionEntregaAdmin, MovimientoBidonAdmin, TelefonoContactoAdmin

### Community 8 - "django_urls"
Cohesion: 0.21
Nodes (8): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito()

### Community 10 - "Cliente"
Cohesion: 0.05
Nodes (35): AltaClienteConCuentaForm, Meta, BuscarClienteForm, ClienteForm, Meta, ClienteSinCuentaForm, Meta, DireccionEntregaForm (+27 more)

### Community 11 - "autenticacion/migrations/0001_initial.py"
Cohesion: 0.25
Nodes (3): Migration, Migration, Migration

### Community 12 - "logistica/admin.py"
Cohesion: 0.18
Nodes (12): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+4 more)

### Community 13 - "Producto"
Cohesion: 0.14
Nodes (10): buscar_productos(), CategoriaAdmin, ProductoAdmin, CategoriaForm, Meta, ProductoForm, Meta, Categoria (+2 more)

### Community 14 - "Barrio"
Cohesion: 0.10
Nodes (6): Command, Barrio, Meta, Camion, Meta, AccesoAVistasLogisticasTests

### Community 16 - "PROCEDURE.md"
Cohesion: 0.06
Nodes (34): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido (+26 more)

### Community 18 - "promociones/views.py"
Cohesion: 0.15
Nodes (9): PromocionForm, Meta, VenderPromocionForm, Promocion, Meta, crear_promocion(), editar_promocion(), _form_promocion() (+1 more)

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.16
Nodes (5): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), ruta_default(), GeneracionBorradorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "logistica/views.py"
Cohesion: 0.12
Nodes (24): CamionForm, Meta, DetalleRutaForm, Meta, HojaRutaForm, Meta, actualizar_estado_entrega(), agregar_parada() (+16 more)

### Community 22 - "base_dashboard.html"
Cohesion: 0.19
Nodes (7): Hallazgos nuevos, _ids_de_paradas_con_nota(), imprimir_ruta(), listar_rutas(), mi_ruta_hoy(), ver_ruta(), obtener_empleado()

### Community 23 - "Calendario de reparto"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 25 - "DetalleHojaRuta"
Cohesion: 0.09
Nodes (12): 5A — Historial de envases (RF-08) · ~4 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, HistorialBidonesTests, ActualizarEstadoForm, Meta, DetalleHojaRuta (+4 more)

### Community 26 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 28 - "Abono"
Cohesion: 0.18
Nodes (4): AbonoForm, Meta, Abono, Meta

### Community 29 - "DireccionEntrega"
Cohesion: 0.15
Nodes (7): DireccionEntregaInline, TelefonoContactoInline, DireccionEntrega, Meta, TelefonoContacto, Meta, CheckoutRequiereTelefonosTests

### Community 31 - "MovimientoCuenta"
Cohesion: 0.06
Nodes (12): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests (+4 more)

### Community 32 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.17
Nodes (12): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)** (+4 more)

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, AutenticacionConfig, ProductosConfig

### Community 35 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (5): puede_ver_nota_seguridad(), NotaDeSeguridadTests, Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 36 - "abonos/views.py"
Cohesion: 0.40
Nodes (7): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono(), sin_permiso()

### Community 37 - "pedidos/services.py"
Cohesion: 0.18
Nodes (5): _a_decimal(), aplicar_pago_mercadopago(), firma_webhook_valida(), pago_en_curso(), _firmar()

### Community 38 - "permisos/signals.py"
Cohesion: 0.22
Nodes (5): sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 39 - "distribuidora/views.py"
Cohesion: 0.17
Nodes (4): clientes_morosos(), resumen_morosidad(), inicio(), resumen_dashboard()

### Community 41 - "Zona"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 43 - "pedidos/forms.py"
Cohesion: 0.21
Nodes (4): CheckoutForm, _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 48 - "autenticacion/views.py"
Cohesion: 0.27
Nodes (5): IngresarUsuarioForm, cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario()

### Community 50 - "PagoPedido"
Cohesion: 0.14
Nodes (10): 5B — Promociones prepago (RF-09) · ~6 h, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, PagoPedido, Meta (+2 more)

### Community 51 - "RegistroUsuarioForm"
Cohesion: 0.20
Nodes (3): RegistroUsuarioForm, Meta, _solo_digitos()

### Community 52 - "seed_demo.py"
Cohesion: 0.08
Nodes (20): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), bidones_de_pedido(), confirmar_hoja() (+12 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "VariasDireccionesTests"
Cohesion: 0.09
Nodes (5): AgregarDireccionTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 64 - "pedidos/views.py"
Cohesion: 0.12
Nodes (10): 1. 🔴 Críticos — seguridad y dinero, consultar_pago_mercadopago(), checkout(), _cliente_puede_comprar(), confirmar_pago_qr(), confirmar_pedido(), pago_exitoso(), pago_fallido() (+2 more)

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 72 - "vencer_promociones"
Cohesion: 0.25
Nodes (4): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, FASE 7 — QA, producción y tesis 🎓, Command, vencer_promociones()

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 74 - "CompraPromocion"
Cohesion: 0.25
Nodes (4): CompraPromocion, Meta, promociones_por_vencer(), listar_promociones()

### Community 75 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.27
Nodes (3): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 6A — Pagos parciales (RF-13) · ~4 h

### Community 76 - "listar_zonas"
Cohesion: 0.36
Nodes (3): direcciones_sin_zona(), editar_zona(), listar_zonas()

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 99 - "promociones/admin.py"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 100 - "registrar_cobro"
Cohesion: 0.29
Nodes (7): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`)

### Community 101 - "logistica/tests.py"
Cohesion: 0.08
Nodes (13): BarrioForm, Meta, RutaRepartoForm, Meta, ZonaForm, Meta, RutaReparto, Meta (+5 more)

### Community 102 - "es_admin_o_vendedor"
Cohesion: 0.21
Nodes (3): es_admin_o_vendedor(), es_admin_vendedor_o_repartidor(), EvaluacionDeRolesTests

### Community 103 - "roles.py"
Cohesion: 0.24
Nodes (10): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_repartidor_asignado(), es_vendedor() (+2 more)

### Community 106 - "HojaRuta"
Cohesion: 0.13
Nodes (4): Command, generar_borradores_periodo(), pedidos_candidatos(), GeneracionQuincenalTests

### Community 114 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (6): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 116 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 117 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 579 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **57 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `vender_promocion`, `cuentas/views.py`, `Producto`, `Barrio`, `promociones/tests.py`, `PROCEDURE.md`, `django_urls`, `promociones/views.py`, `Planificación de reparto por zona`, `CuentaCorriente`, `DetalleHojaRuta`, `generar_cargos_mensuales`, `clientes/signals.py`, `Abono`, `DireccionEntrega`, `Tests de abonos (RF-05)`, `MovimientoCuenta`, `puede_ver_nota_seguridad`, `pedidos/services.py`, `distribuidora/views.py`, `pedidos/forms.py`, `PagoPedido`, `seed_demo.py`, `VariasDireccionesTests`, `pedidos/views.py`, `logistica/tests.py`, `HojaRuta`, `VistasCuentasTests`, `✅ Control de cumplimiento de requisitos — 20/10/2026`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 51 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `empleados/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.059298245614035086 - nodes in this community are weakly interconnected._
- **Why does `Pedido` connect `PagoPedido` to `Pedido`, `empleados/views.py`, `vender_promocion`, `Cliente`, `promociones/tests.py`, `PROCEDURE.md`, `django_urls`, `Planificación de reparto por zona`, `DetalleHojaRuta`, `DireccionEntrega`, `MovimientoCuenta`, `🏁 Plan de Cierre — Fases 4.5 a 7`, `pedidos/services.py`, `distribuidora/views.py`, `PagosSegurosTests`, `pedidos/forms.py`, `seed_demo.py`, `TransicionesManualesTests`, `pedidos/views.py`, `EliminarProductoTests`, `6A — Pagos parciales (RF-13) · ~4 h`, `logistica/tests.py`, `HojaRuta`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `vender_promocion` be split into smaller, more focused modules?**
  _Cohesion score 0.1455026455026455 - nodes in this community are weakly interconnected._