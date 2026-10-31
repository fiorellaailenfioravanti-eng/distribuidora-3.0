# Graph Report - distribuidora-3.0  (2026-10-31)

## Corpus Check
- 207 files · ~294,761 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1654 nodes · 4150 edges · 129 communities (70 shown, 59 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 662 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a9d76cc8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- pedidos/views.py
- base_dashboard.html
- vender_promocion
- django_db
- ModeloEmpleadoUnicoTests
- cuentas/views.py
- logistica/tests.py
- PedidoAutomaticoTests
- abonos/views.py
- clientes/urls.py
- Empleado
- logistica/services.py
- Producto
- productos/views.py
- seed_demo.py
- PROCEDURE.md
- Carrito
- CarritoSoloPorPostTests
- logistica/views.py
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- logistica/admin.py
- crear_cliente_con_cuenta
- pedidos/views.py
- generar_cargos_mensuales
- crear_perfil_cliente
- Abono
- RecorridoRepartidorTests
- Tests de abonos (RF-05)
- CuentaCorriente
- es_admin_vendedor_o_repartidor
- puede_ver_nota_seguridad
- django_apps
- GeneracionBorradorTests
- base_tienda.html
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- CheckoutFechaEstimadaTests
- distribuidora/views.py
- registrar_cargo
- Zona
- pedidos/admin.py
- SuscripcionReposicion
- Migración: unificar empleados
- StockComprometidoTests
- Migración: métodos de pago
- CobroManualTests
- TransicionesManualesTests
- sincronizar_grupo_empleado
- 6A — Pagos parciales (RF-13) · ~4 h
- MetodoPago
- Command
- graphify reference: extra exports and benchmark
- SesionTests
- clientes/services.py
- PagosSegurosTests
- base.py
- EliminarProductoTests
- Barrio
- CheckoutRequiereTelefonosTests
- graphify reference: query, path, explain
- ver_cliente
- django_contrib
- django_shortcuts
- Fase 6 · Pagos parciales y pedido automático
- cuentas/admin.py
- DireccionEntrega
- permisos/apps.py
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- HojaRuta
- Verificar cambios — Distribuidora 3.0
- Verificar cambios — Distribuidora 3.0
- ClientesConfig
- 0006_corregir_ayuda_desc_seguridad.py
- roles.py
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- generar_borradores_periodo
- perfil_cliente_esta_vacio
- Fase 4 · Cuentas corrientes y abonos
- permisos/signals.py
- Fase 5 · Bidones y promociones prepago
- 0013_detallehojaruta_es_venta_calle.py
- clientes/admin.py
- 0007_marcar_botellones.py
- Distribuidora 3.0 / Aquadelluvia
- buscador/apps.py
- carrito/apps.py
- empleados/apps.py
- clientes/views.py
- logistica/apps.py
- pedidos/apps.py
- productos/apps.py
- django_db_models_deletion
- clientes/forms.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 99 edges
2. `es_admin_o_vendedor()` - 87 edges
3. `Pedido` - 76 edges
4. `Producto` - 68 edges
5. `Zona` - 53 edges
6. `DireccionEntrega` - 51 edges
7. `HojaRuta` - 51 edges
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
- `5. 🔗 Dependencias y archivos compartidos` --references--> `registrar_cobro()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/pedidos/services.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (129 total, 59 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.13
Nodes (9): IngresarUsuarioForm, RegistroUsuarioForm, Meta, _solo_digitos(), cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario() (+1 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.11
Nodes (11): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr() (+3 more)

### Community 2 - "base_dashboard.html"
Cohesion: 0.09
Nodes (17): EmpleadoForm, Meta, RolEmpleadoForm, Meta, GuardsUnificadosTests, PantallasDeRolesTests, RolSincronizaGrupoTests, cambiar_estado_empleado() (+9 more)

### Community 3 - "vender_promocion"
Cohesion: 0.05
Nodes (25): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, PromocionForm, Meta, VenderPromocionForm, CompraPromocion, Meta (+17 more)

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (26): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+18 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.25
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "logistica/tests.py"
Cohesion: 0.09
Nodes (19): ActualizarEstadoForm, Meta, AgregarParadaForm, CamionForm, Meta, _etiqueta_direccion_cliente(), HojaRutaForm, Meta (+11 more)

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.05
Nodes (17): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)** (+9 more)

### Community 9 - "abonos/views.py"
Cohesion: 0.40
Nodes (7): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono(), sin_permiso()

### Community 10 - "clientes/urls.py"
Cohesion: 0.34
Nodes (9): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+1 more)

### Community 11 - "Empleado"
Cohesion: 0.08
Nodes (11): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta (+3 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.08
Nodes (22): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellones_por_producto(), confirmar_entrega_en_calle() (+14 more)

### Community 13 - "Producto"
Cohesion: 0.18
Nodes (7): CategoriaAdmin, ProductoAdmin, CategoriaForm, Meta, Categoria, Producto, AltaProductoTests

### Community 14 - "productos/views.py"
Cohesion: 0.25
Nodes (7): ProductoForm, Meta, crear_categoria(), crear_producto(), editar_producto(), eliminar_producto(), listar_productos_admin()

### Community 16 - "PROCEDURE.md"
Cohesion: 0.15
Nodes (13): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose (+5 more)

### Community 17 - "Carrito"
Cohesion: 0.26
Nodes (8): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), stock_disponible(), solo_clientes()

### Community 18 - "CarritoSoloPorPostTests"
Cohesion: 0.18
Nodes (3): ItemCarrito, Meta, CarritoSoloPorPostTests

### Community 19 - "logistica/views.py"
Cohesion: 0.09
Nodes (21): botellon_por_defecto(), carga_sugerida(), envase_de_reparto(), envases_retirados_en_hoja(), productos_de_reparto(), registrar_regreso(), _cargas_confirmacion_desde_post(), confirmar_entrega() (+13 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.11
Nodes (23): Hallazgos nuevos, actualizar_estado_entrega(), agregar_parada(), agregar_pedido_parada(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta() (+15 more)

### Community 23 - "logistica/admin.py"
Cohesion: 0.10
Nodes (15): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+7 more)

### Community 24 - "crear_cliente_con_cuenta"
Cohesion: 0.12
Nodes (8): AltaClienteConCuentaForm, Meta, ClienteSinCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 25 - "pedidos/views.py"
Cohesion: 0.14
Nodes (9): PagoPedido, Meta, _a_decimal(), aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), registrar_pago_manual(), pago_exitoso() (+1 more)

### Community 26 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 28 - "Abono"
Cohesion: 0.18
Nodes (4): AbonoForm, Meta, Abono, Meta

### Community 29 - "RecorridoRepartidorTests"
Cohesion: 0.12
Nodes (4): confirmar_hoja(), resumen_recorrido(), ConfirmacionRegresoTests, RecorridoRepartidorTests

### Community 31 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 34 - "django_apps"
Cohesion: 0.15
Nodes (4): AbonosConfig, AutenticacionConfig, CuentasConfig, PromocionesConfig

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.26
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 36 - "base_tienda.html"
Cohesion: 0.29
Nodes (4): listar_productos(), ver_producto(), inicio(), RNF-03 · Dark mode sin autenticación

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.28
Nodes (8): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, confirmar_pago_qr()

### Community 38 - "CheckoutFechaEstimadaTests"
Cohesion: 0.20
Nodes (3): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests

### Community 39 - "distribuidora/views.py"
Cohesion: 0.17
Nodes (5): clientes_morosos(), resumen_morosidad(), resumen_caja(), promociones_por_vencer(), resumen_dashboard()

### Community 40 - "registrar_cargo"
Cohesion: 0.08
Nodes (8): MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, ReglaFiadoTests, SemaforizacionTests, VistasCuentasTests

### Community 41 - "Zona"
Cohesion: 0.16
Nodes (6): ZonaForm, Meta, Zona, Meta, ZonaDiasRepartoTests, ZonaFormTests

### Community 42 - "pedidos/admin.py"
Cohesion: 0.21
Nodes (9): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido, Meta (+1 more)

### Community 43 - "SuscripcionReposicion"
Cohesion: 0.15
Nodes (10): 4. ❓ Decisiones a tomar antes de empezar, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, SuscripcionReposicion, Meta (+2 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 49 - "sincronizar_grupo_empleado"
Cohesion: 0.33
Nodes (3): sincronizar_grupo_empleado(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado()

### Community 50 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.14
Nodes (7): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, Pedido, Meta

### Community 51 - "MetodoPago"
Cohesion: 0.10
Nodes (9): fecha_estimada_para_direccion(), CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, checkout(), _cliente_puede_comprar(), confirmar_pedido() (+1 more)

### Community 52 - "Command"
Cohesion: 0.09
Nodes (9): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), HistorialBidonesTests, _a_dt() (+1 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "clientes/services.py"
Cohesion: 0.09
Nodes (5): AgregarDireccionTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.19
Nodes (3): firma_webhook_valida(), _firmar(), PagosSegurosTests

### Community 67 - "Barrio"
Cohesion: 0.05
Nodes (9): BarrioForm, Meta, Command, Barrio, Meta, HojaDeRutaUXTests, PedidoEspontaneoTests, PlanificarRepartoViewTests (+1 more)

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "ver_cliente"
Cohesion: 0.24
Nodes (4): _contexto_suscripcion(), mi_perfil_cliente(), ver_cliente(), compras_vigentes()

### Community 73 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 74 - "cuentas/admin.py"
Cohesion: 0.50
Nodes (3): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

### Community 75 - "DireccionEntrega"
Cohesion: 0.20
Nodes (4): DireccionEntrega, Meta, TelefonoContacto, Meta

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
Cohesion: 0.07
Nodes (8): HojaRuta, Meta, EntregaCalleTests, GeneracionQuincenalTests, HojaRutaCapacidadTests, HojaSinChoferTests, InventarioCamionTests, SeedDemoTests

### Community 99 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 100 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 103 - "roles.py"
Cohesion: 0.29
Nodes (9): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_vendedor(), 2. Revisar convenciones del proyecto en lo que cambió (+1 more)

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (6): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "generar_borradores_periodo"
Cohesion: 0.20
Nodes (3): Command, generar_borradores_periodo(), pedidos_candidatos()

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 109 - "permisos/signals.py"
Cohesion: 0.22
Nodes (3): _sincronizar(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 110 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 114 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 116 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 117 - "Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 121 - "clientes/views.py"
Cohesion: 0.24
Nodes (5): MovimientoBidonForm, listar_clientes(), registrar_movimiento_bidon(), _texto_buscable(), normalizar_texto()

### Community 126 - "django_db_models_deletion"
Cohesion: 0.05
Nodes (20): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+12 more)

### Community 133 - "clientes/forms.py"
Cohesion: 0.13
Nodes (8): BuscarClienteForm, ClienteForm, Meta, DireccionEntregaForm, Meta, EditarMiPerfilForm, TelefonoContactoForm, Meta

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 669 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **59 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/views.py`, `vender_promocion`, `clientes/forms.py`, `cuentas/views.py`, `logistica/tests.py`, `clientes/urls.py`, `Empleado`, `logistica/services.py`, `Producto`, `seed_demo.py`, `PROCEDURE.md`, `logistica/views.py`, `base_dashboard.html`, `crear_cliente_con_cuenta`, `pedidos/views.py`, `generar_cargos_mensuales`, `crear_perfil_cliente`, `Abono`, `RecorridoRepartidorTests`, `Tests de abonos (RF-05)`, `CuentaCorriente`, `puede_ver_nota_seguridad`, `GeneracionBorradorTests`, `CheckoutFechaEstimadaTests`, `distribuidora/views.py`, `registrar_cargo`, `SuscripcionReposicion`, `CobroManualTests`, `6A — Pagos parciales (RF-13) · ~4 h`, `MetodoPago`, `Command`, `clientes/services.py`, `Barrio`, `ver_cliente`, `DireccionEntrega`, `HojaRuta`, `✅ Control de cumplimiento de requisitos — 20/10/2026`, `perfil_cliente_esta_vacio`, `Fase 4 · Cuentas corrientes y abonos`, `permisos/signals.py`, `Fase 5 · Bidones y promociones prepago`, `clientes/admin.py`, `clientes/views.py`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 61 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 61 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13043478260869565 - nodes in this community are weakly interconnected._
- **Why does `Pedido` connect `6A — Pagos parciales (RF-13) · ~4 h` to `pedidos/views.py`, `base_dashboard.html`, `vender_promocion`, `logistica/tests.py`, `PedidoAutomaticoTests`, `Empleado`, `logistica/services.py`, `Producto`, `seed_demo.py`, `PROCEDURE.md`, `logistica/views.py`, `base_dashboard.html`, `Cliente`, `pedidos/views.py`, `RecorridoRepartidorTests`, `GeneracionBorradorTests`, `🔎 Auditoría de coherencia — Distribuidora 3.0`, `distribuidora/views.py`, `pedidos/admin.py`, `SuscripcionReposicion`, `StockComprometidoTests`, `CobroManualTests`, `TransicionesManualesTests`, `MetodoPago`, `Command`, `PagosSegurosTests`, `EliminarProductoTests`, `Barrio`, `CheckoutRequiereTelefonosTests`, `ver_cliente`, `DireccionEntrega`, `HojaRuta`, `generar_borradores_periodo`, `perfil_cliente_esta_vacio`, `clientes/views.py`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11083743842364532 - nodes in this community are weakly interconnected._