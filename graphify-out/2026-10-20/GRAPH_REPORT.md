# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 200 files · ~286,482 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1527 nodes · 3757 edges · 126 communities (63 shown, 63 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 574 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e387ff5c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- listar_productos_admin
- Pedido
- empleados/views.py
- vender_promocion
- django_db
- GruposBaseTests
- Abono
- django_db_models_deletion
- django_urls
- CarritoSoloPorPostTests
- clientes/views.py
- autenticacion/migrations/0001_initial.py
- logistica/admin.py
- Producto
- AccesoAVistasLogisticasTests
- promociones/tests.py
- PROCEDURE.md
- H-10 · Suite de tests parcial (faltan carrito y buscador)
- promociones/views.py
- Planificación de reparto por zona
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- Calendario de reparto
- listar_clientes
- seed_demo.py
- generar_cargos_mensuales
- permisos/signals.py
- HojaDeRutaUXTests
- DireccionEntrega
- Tests de abonos (RF-05)
- MovimientoCuenta
- 🏁 Plan de Cierre — Fases 4.5 a 7
- Arranque Django (asgi/wsgi)
- django_apps
- puede_ver_nota_seguridad
- productos/views.py
- pedidos/services.py
- permisos/signals.py
- distribuidora/views.py
- PagosSegurosTests
- Zona
- DetallePedido
- confirmar_pedido
- Migración: unificar empleados
- Migración: borrar empleados duplicados
- Migración: métodos de pago
- permisos/apps.py
- autenticacion/views.py
- ClientesConfig
- Pedido
- RegistroUsuarioForm
- Command
- graphify reference: extra exports and benchmark
- SesionTests
- VariasDireccionesTests
- TransicionesManualesTests
- base.py
- EliminarProductoTests
- buscador/apps.py
- carrito/apps.py
- graphify reference: query, path, explain
- cuentas/apps.py
- empleados/apps.py
- vencer_promociones
- 0004_asignar_grupo_permisos.py
- CompraPromocion
- registrar_cobro
- ZonaForm
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
- FASE3_LOGISTICA.md
- HojaRuta
- logistica/views.py
- Fase 4 · Cuentas corrientes y abonos
- pedidos/apps.py
- Fase 6 · Pagos parciales y pedido automático
- VistasCuentasTests
- TelefonoContacto
- 0007_marcar_botellones.py
- Fase 5 · Bidones y promociones prepago
- 0003_grupos_base.py
- ClienteSinCuentaForm
- DireccionEntregaForm
- registrar_movimiento_bidon
- autenticacion/apps.py
- 0010_saldo_inicial_bidones.py
- 0012_completar_pedidos_de_paradas.py
- productos/apps.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 91 edges
2. `es_admin_o_vendedor()` - 88 edges
3. `Pedido` - 68 edges
4. `Producto` - 61 edges
5. `Zona` - 48 edges
6. `HojaRuta` - 46 edges
7. `DireccionEntrega` - 44 edges
8. `Command` - 38 edges
9. `MetodoPago` - 37 edges
10. `DetalleHojaRuta` - 36 edges

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

## Communities (126 total, 63 thin omitted)

### Community 0 - "listar_productos_admin"
Cohesion: 0.22
Nodes (7): crear_categoria(), crear_producto(), editar_producto(), eliminar_producto(), listar_productos(), listar_productos_admin(), ver_producto()

### Community 1 - "Pedido"
Cohesion: 0.14
Nodes (8): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr()

### Community 2 - "empleados/views.py"
Cohesion: 0.06
Nodes (26): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoAdmin, RolEmpleadoAdmin, EmpleadoForm, Meta, RolEmpleadoForm, Meta (+18 more)

### Community 3 - "vender_promocion"
Cohesion: 0.17
Nodes (6): consumir_saldo(), revertir_consumos(), vender_promocion(), BasePromociones, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.05
Nodes (19): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+11 more)

### Community 6 - "Abono"
Cohesion: 0.08
Nodes (20): AbonoAdmin, AbonoForm, Meta, Abono, Meta, cambiar_estado_abono(), crear_abono(), editar_abono() (+12 more)

### Community 7 - "django_db_models_deletion"
Cohesion: 0.08
Nodes (14): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+6 more)

### Community 8 - "django_urls"
Cohesion: 0.20
Nodes (7): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), redirigir_a_origen()

### Community 10 - "clientes/views.py"
Cohesion: 0.20
Nodes (14): TelefonoContactoForm, Meta, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+6 more)

### Community 12 - "logistica/admin.py"
Cohesion: 0.14
Nodes (11): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+3 more)

### Community 13 - "Producto"
Cohesion: 0.16
Nodes (8): ItemCarrito, Meta, CategoriaAdmin, ProductoAdmin, ProductoForm, Meta, Categoria, Producto

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (14): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose (+6 more)

### Community 18 - "promociones/views.py"
Cohesion: 0.15
Nodes (9): PromocionForm, Meta, VenderPromocionForm, Promocion, Meta, crear_promocion(), editar_promocion(), _form_promocion() (+1 more)

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.26
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.13
Nodes (17): Hallazgos nuevos, actualizar_estado_entrega(), agregar_parada(), crear_ruta(), editar_camion(), editar_ruta(), eliminar_camion(), eliminar_parada() (+9 more)

### Community 22 - "Cliente"
Cohesion: 0.14
Nodes (4): ClienteForm, Meta, Cliente, Meta

### Community 23 - "Calendario de reparto"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "listar_clientes"
Cohesion: 0.17
Nodes (7): crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos(), listar_clientes(), _texto_buscable(), normalizar_texto()

### Community 25 - "seed_demo.py"
Cohesion: 0.11
Nodes (16): 5A — Historial de envases (RF-08) · ~4 h, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), carga_sugerida(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona() (+8 more)

### Community 26 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "permisos/signals.py"
Cohesion: 0.22
Nodes (3): _sincronizar(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 29 - "DireccionEntrega"
Cohesion: 0.08
Nodes (16): DireccionEntrega, Meta, ActualizarEstadoForm, Meta, AgregarParadaForm, BarrioForm, Meta, _etiqueta_direccion_cliente() (+8 more)

### Community 31 - "MovimientoCuenta"
Cohesion: 0.06
Nodes (13): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, CuentaCorriente, Meta, MovimientoCuenta, Meta, registrar_cargo() (+5 more)

### Community 32 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.09
Nodes (19): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original), 0. Qué falta (resumen) (+11 more)

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, LogisticaConfig, PromocionesConfig

### Community 35 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (5): puede_ver_nota_seguridad(), NotaDeSeguridadTests, Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 36 - "productos/views.py"
Cohesion: 0.24
Nodes (4): buscar_productos(), CategoriaForm, Meta, RF-07 · Buscador tolerante a tildes

### Community 37 - "pedidos/services.py"
Cohesion: 0.14
Nodes (8): _a_decimal(), aplicar_pago_mercadopago(), consultar_pago_mercadopago(), firma_webhook_valida(), pago_en_curso(), _firmar(), pago_exitoso(), webhook_mercadopago()

### Community 38 - "permisos/signals.py"
Cohesion: 0.33
Nodes (3): sincronizar_grupo_empleado(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado()

### Community 39 - "distribuidora/views.py"
Cohesion: 0.14
Nodes (7): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, csrf_failure(), inicio(), resumen_dashboard()

### Community 41 - "Zona"
Cohesion: 0.17
Nodes (4): Command, Zona, Meta, ZonaDiasRepartoTests

### Community 42 - "DetallePedido"
Cohesion: 0.27
Nodes (7): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, DetallePedido, Meta

### Community 43 - "confirmar_pedido"
Cohesion: 0.11
Nodes (8): fecha_estimada_para_direccion(), CheckoutForm, _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, checkout(), _cliente_puede_comprar(), confirmar_pedido()

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 48 - "autenticacion/views.py"
Cohesion: 0.27
Nodes (5): IngresarUsuarioForm, cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario()

### Community 51 - "RegistroUsuarioForm"
Cohesion: 0.13
Nodes (7): RegistroUsuarioForm, Meta, _solo_digitos(), AltaClienteConCuentaForm, Meta, BuscarClienteForm, EditarMiPerfilForm

### Community 52 - "Command"
Cohesion: 0.06
Nodes (15): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, MovimientoBidon, Meta (+7 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "VariasDireccionesTests"
Cohesion: 0.09
Nodes (5): AgregarDireccionTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "TransicionesManualesTests"
Cohesion: 0.13
Nodes (3): CheckoutRequiereTelefonosTests, PagosParcialesTests, TransicionesManualesTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 72 - "vencer_promociones"
Cohesion: 0.19
Nodes (4): FASE 7 — QA, producción y tesis 🎓, Command, saldo_vigente(), vencer_promociones()

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 74 - "CompraPromocion"
Cohesion: 0.25
Nodes (4): CompraPromocion, Meta, promociones_por_vencer(), listar_promociones()

### Community 75 - "registrar_cobro"
Cohesion: 0.14
Nodes (9): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 5. 🔗 Dependencias y archivos compartidos, 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18), Punto de partida real, metodo_pago_efectivo() (+1 more)

### Community 76 - "ZonaForm"
Cohesion: 0.23
Nodes (6): ZonaForm, Meta, ZonaFormTests, direcciones_sin_zona(), editar_zona(), listar_zonas()

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
Cohesion: 0.28
Nodes (8): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, confirmar_pago_qr()

### Community 101 - "logistica/tests.py"
Cohesion: 0.06
Nodes (13): CargaHojaRuta, Meta, confirmar_hoja(), ConfirmacionRegresoTests, EntregaCalleTests, GeneracionQuincenalTests, HojaRutaCapacidadTests, HojaSinChoferTests (+5 more)

### Community 102 - "es_admin_o_vendedor"
Cohesion: 0.21
Nodes (3): es_admin_o_vendedor(), es_admin_vendedor_o_repartidor(), EvaluacionDeRolesTests

### Community 103 - "roles.py"
Cohesion: 0.12
Nodes (18): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_repartidor_asignado(), es_vendedor() (+10 more)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "HojaRuta"
Cohesion: 0.18
Nodes (3): Command, generar_borradores_periodo(), pedidos_candidatos()

### Community 107 - "logistica/views.py"
Cohesion: 0.09
Nodes (24): CamionForm, Meta, Camion, Meta, botellon_por_defecto(), botellones_por_producto(), entregados_por_producto(), envase_de_reparto() (+16 more)

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 110 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 114 - "TelefonoContacto"
Cohesion: 0.22
Nodes (4): Detalle, TelefonoContacto, Meta, crear_perfil_cliente()

### Community 116 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 117 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 608 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **63 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `vender_promocion`, `Abono`, `clientes/views.py`, `Producto`, `AccesoAVistasLogisticasTests`, `promociones/tests.py`, `PROCEDURE.md`, `promociones/views.py`, `Planificación de reparto por zona`, `base_dashboard.html`, `listar_clientes`, `seed_demo.py`, `generar_cargos_mensuales`, `permisos/signals.py`, `HojaDeRutaUXTests`, `DireccionEntrega`, `Tests de abonos (RF-05)`, `MovimientoCuenta`, `puede_ver_nota_seguridad`, `pedidos/services.py`, `distribuidora/views.py`, `confirmar_pedido`, `Pedido`, `RegistroUsuarioForm`, `Command`, `VariasDireccionesTests`, `vencer_promociones`, `logistica/tests.py`, `logistica/views.py`, `Fase 4 · Cuentas corrientes y abonos`, `VistasCuentasTests`, `TelefonoContacto`, `Fase 5 · Bidones y promociones prepago`, `ClienteSinCuentaForm`, `registrar_movimiento_bidon`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 53 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pedido` be split into smaller, more focused modules?**
  _Cohesion score 0.14130434782608695 - nodes in this community are weakly interconnected._
- **Why does `Pedido` connect `Pedido` to `Pedido`, `empleados/views.py`, `vender_promocion`, `clientes/views.py`, `Producto`, `PROCEDURE.md`, `Planificación de reparto por zona`, `Cliente`, `seed_demo.py`, `HojaDeRutaUXTests`, `DireccionEntrega`, `🏁 Plan de Cierre — Fases 4.5 a 7`, `pedidos/services.py`, `distribuidora/views.py`, `PagosSegurosTests`, `DetallePedido`, `confirmar_pedido`, `Command`, `TransicionesManualesTests`, `EliminarProductoTests`, `vencer_promociones`, `registrar_cobro`, `registrar_cobro`, `logistica/tests.py`, `VistasPromocionesTests`, `HojaRuta`, `logistica/views.py`?**
  _High betweenness centrality (0.094) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `empleados/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.059298245614035086 - nodes in this community are weakly interconnected._