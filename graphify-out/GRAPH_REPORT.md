# Graph Report - distribuidora-3.0  (2026-10-31)

## Corpus Check
- 207 files · ~293,978 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1647 nodes · 4122 edges · 122 communities (62 shown, 60 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 655 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6ae94e21`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- base_tienda.html
- pedidos/views.py
- empleados/views.py
- vender_promocion
- django_db
- ModeloEmpleadoUnicoTests
- cuentas/views.py
- logistica/tests.py
- SuscripcionReposicion
- abonos/views.py
- clientes/urls.py
- Empleado
- logistica/services.py
- django_urls
- AccesoAVistasLogisticasTests
- seed_demo.py
- PROCEDURE.md
- Carrito
- promociones/views.py
- logistica/views.py
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- logistica/admin.py
- crear_cliente_con_cuenta
- pedidos/tests.py
- generar_cargos_mensuales
- TelefonoContacto
- Abono
- Producto
- Tests de abonos (RF-05)
- CuentaCorriente
- vencer_promociones
- django_apps
- promociones/admin.py
- Usuario
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- registrar_regreso_ruta
- distribuidora/views.py
- registrar_cargo
- Zona
- pedidos/admin.py
- SuscripcionReposicion
- Migración: unificar empleados
- GuardsUnificadosTests
- Migración: métodos de pago
- RolSincronizaGrupoTests
- PedidoEspontaneoTests
- CalendarioTests
- 6A — Pagos parciales (RF-13) · ~4 h
- MetodoPago
- Command
- graphify reference: extra exports and benchmark
- SesionTests
- clientes/services.py
- PagosSegurosTests
- base.py
- EliminarProductoTests
- HojaDeRutaUXTests
- RecorridoRepartidorTests
- graphify reference: query, path, explain
- ver_cliente
- django_contrib
- permisos/views.py
- 0004_asignar_grupo_permisos.py
- webhook_mercadopago
- DireccionEntrega
- TestCase
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- HojaRuta
- Command
- confirmar_pedido
- Barrio
- PlanificarRepartoViewTests
- roles.py
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- generar_borradores_periodo
- CuentaDeRepartidorTests
- Fase 4 · Cuentas corrientes y abonos
- clientes/services.py
- Fase 5 · Bidones y promociones prepago
- 0013_detallehojaruta_es_venta_calle.py
- clientes/admin.py
- 0007_marcar_botellones.py
- clientes/views.py
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- DireccionEntregaForm

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 98 edges
2. `es_admin_o_vendedor()` - 87 edges
3. `Pedido` - 76 edges
4. `Producto` - 66 edges
5. `Zona` - 52 edges
6. `DireccionEntrega` - 50 edges
7. `HojaRuta` - 50 edges
8. `MetodoPago` - 47 edges
9. `Command` - 38 edges
10. `DetalleHojaRuta` - 37 edges

## Surprising Connections (you probably didn't know these)
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Carga y regreso del camión (sobrantes a stock)` --references--> `CargaHojaRuta`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `5D — Tests · ~2 h` --references--> `registrar_entrega()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/logistica/services.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (122 total, 60 thin omitted)

### Community 0 - "base_tienda.html"
Cohesion: 0.06
Nodes (26): IngresarUsuarioForm, RegistroUsuarioForm, Meta, _solo_digitos(), cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario() (+18 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.13
Nodes (10): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr() (+2 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.27
Nodes (12): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+4 more)

### Community 3 - "vender_promocion"
Cohesion: 0.11
Nodes (8): consumir_saldo(), revertir_consumos(), vender_promocion(), BasePromociones, CheckoutConSaldoTests, EscenarioAceptacionTests, ReglasDeSaldoTests, VistasPromocionesTests

### Community 4 - "django_db"
Cohesion: 0.02
Nodes (42): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+34 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.25
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "logistica/tests.py"
Cohesion: 0.08
Nodes (23): BarrioForm, Meta, CamionForm, Meta, HojaRutaForm, Meta, RutaRepartoForm, Meta (+15 more)

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.23
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "abonos/views.py"
Cohesion: 0.40
Nodes (7): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono(), sin_permiso()

### Community 10 - "clientes/urls.py"
Cohesion: 0.33
Nodes (10): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+2 more)

### Community 11 - "Empleado"
Cohesion: 0.19
Nodes (6): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta

### Community 12 - "logistica/services.py"
Cohesion: 0.09
Nodes (21): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), clientes_frecuentes_de_zona(), confirmar_entrega_en_calle() (+13 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (18): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-04 · ≥2 teléfonos con relación explícita (+10 more)

### Community 17 - "Carrito"
Cohesion: 0.08
Nodes (14): carrito_total(), Carrito, ItemCarrito, Meta, CarritoSoloPorPostTests, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito() (+6 more)

### Community 18 - "promociones/views.py"
Cohesion: 0.10
Nodes (13): PromocionForm, Meta, VenderPromocionForm, CompraPromocion, Meta, Promocion, Meta, promociones_por_vencer() (+5 more)

### Community 19 - "logistica/views.py"
Cohesion: 0.11
Nodes (17): agregar_parada(), agregar_pedido_parada(), _cargas_confirmacion_desde_post(), confirmar_entrega(), confirmar_ruta(), _ficha_de_parada(), _int_o_none(), _link_mapa() (+9 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.13
Nodes (16): Hallazgos nuevos, actualizar_estado_entrega(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona(), eliminar_camion() (+8 more)

### Community 23 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 24 - "crear_cliente_con_cuenta"
Cohesion: 0.12
Nodes (8): AltaClienteConCuentaForm, Meta, ClienteSinCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 25 - "pedidos/tests.py"
Cohesion: 0.13
Nodes (10): PagoPedido, Meta, _a_decimal(), aplicar_pago_mercadopago(), firma_webhook_valida(), metodo_pago_efectivo(), registrar_cobro(), registrar_pago_manual() (+2 more)

### Community 26 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "TelefonoContacto"
Cohesion: 0.17
Nodes (6): Detalle, TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente()

### Community 28 - "Abono"
Cohesion: 0.18
Nodes (4): AbonoForm, Meta, Abono, Meta

### Community 29 - "Producto"
Cohesion: 0.08
Nodes (11): Punto de partida real, carga_sugerida(), confirmar_hoja(), _producto_envase_para(), registrar_entrega(), ConfirmacionRegresoTests, EntregaCalleTests, GeneracionBorradorTests (+3 more)

### Community 34 - "django_apps"
Cohesion: 0.05
Nodes (12): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, CuentasConfig, EmpleadosConfig, LogisticaConfig (+4 more)

### Community 35 - "promociones/admin.py"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 36 - "Usuario"
Cohesion: 0.20
Nodes (4): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoForm, Meta

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.22
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, pago_en_curso() (+1 more)

### Community 38 - "registrar_regreso_ruta"
Cohesion: 0.18
Nodes (7): botellones_por_producto(), entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), resumen_recorrido(), registrar_regreso_ruta()

### Community 39 - "distribuidora/views.py"
Cohesion: 0.13
Nodes (4): clientes_morosos(), resumen_morosidad(), SemaforizacionTests, resumen_dashboard()

### Community 40 - "registrar_cargo"
Cohesion: 0.10
Nodes (7): MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, ReglaFiadoTests, VistasCuentasTests

### Community 41 - "Zona"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 42 - "pedidos/admin.py"
Cohesion: 0.36
Nodes (6): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin

### Community 43 - "SuscripcionReposicion"
Cohesion: 0.12
Nodes (15): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)** (+7 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 49 - "CalendarioTests"
Cohesion: 0.24
Nodes (3): fecha_es_de_reparto(), proxima_fecha_de_reparto(), CalendarioTests

### Community 50 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.12
Nodes (11): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6A — Pagos parciales (RF-13) · ~4 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)** (+3 more)

### Community 51 - "MetodoPago"
Cohesion: 0.11
Nodes (9): fecha_estimada_para_direccion(), CheckoutForm, _etiqueta_direccion_con_fecha(), RegistrarPagoForm, SuscripcionForm, Meta, MetodoPago, Meta (+1 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "clientes/services.py"
Cohesion: 0.09
Nodes (5): AgregarDireccionTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.07
Nodes (6): metodos_pago_checkout_web(), CheckoutRequiereTelefonosTests, CobroManualTests, PagosParcialesTests, PagosSegurosTests, TransicionesManualesTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "ver_cliente"
Cohesion: 0.24
Nodes (4): _contexto_suscripcion(), mi_perfil_cliente(), ver_cliente(), compras_vigentes()

### Community 71 - "django_contrib"
Cohesion: 0.20
Nodes (4): AbonoAdmin, CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 74 - "webhook_mercadopago"
Cohesion: 0.29
Nodes (3): consultar_pago_mercadopago(), pago_exitoso(), webhook_mercadopago()

### Community 75 - "DireccionEntrega"
Cohesion: 0.18
Nodes (4): DireccionEntrega, Meta, GeneracionQuincenalTests, RF-03 · Multidirección de entrega

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 100 - "confirmar_pedido"
Cohesion: 0.25
Nodes (4): checkout(), _cliente_puede_comprar(), confirmar_pedido(), saldo_vigente()

### Community 101 - "Barrio"
Cohesion: 0.12
Nodes (9): ActualizarEstadoForm, Meta, AgregarParadaForm, _etiqueta_direccion_cliente(), botellon_por_defecto(), productos_de_reparto(), _ids_de_paradas_con_nota(), venta_calle() (+1 more)

### Community 103 - "roles.py"
Cohesion: 0.06
Nodes (24): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_admin_vendedor_o_repartidor(), es_personal_interno(), es_repartidor(), es_vendedor() (+16 more)

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.33
Nodes (5): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.22
Nodes (5): Arquitectura visual dual: Tienda vs Dashboard, Carga y regreso del camión (sobrantes a stock), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.29
Nodes (5): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-14 · Semaforización de deuda, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 109 - "clientes/services.py"
Cohesion: 0.07
Nodes (15): MovimientoBidon, Meta, _cliente_de_parada(), perfil_cliente_esta_vacio(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), retirar_perfil_cliente_vacio(), sincronizar_bidones_de_parada() (+7 more)

### Community 110 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 114 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 116 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 121 - "clientes/views.py"
Cohesion: 0.15
Nodes (9): BuscarClienteForm, ClienteForm, Meta, EditarMiPerfilForm, MovimientoBidonForm, listar_clientes(), registrar_movimiento_bidon(), _texto_buscable() (+1 more)

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 667 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **60 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/views.py`, `vender_promocion`, `cuentas/views.py`, `logistica/tests.py`, `clientes/urls.py`, `Empleado`, `logistica/services.py`, `django_urls`, `AccesoAVistasLogisticasTests`, `seed_demo.py`, `promociones/views.py`, `logistica/views.py`, `crear_cliente_con_cuenta`, `pedidos/tests.py`, `generar_cargos_mensuales`, `TelefonoContacto`, `Abono`, `Producto`, `Tests de abonos (RF-05)`, `CuentaCorriente`, `distribuidora/views.py`, `registrar_cargo`, `SuscripcionReposicion`, `PedidoEspontaneoTests`, `6A — Pagos parciales (RF-13) · ~4 h`, `MetodoPago`, `Command`, `clientes/services.py`, `PagosSegurosTests`, `HojaDeRutaUXTests`, `RecorridoRepartidorTests`, `ver_cliente`, `DireccionEntrega`, `TestCase`, `confirmar_pedido`, `PlanificarRepartoViewTests`, `roles.py`, `CuentaDeRepartidorTests`, `Fase 4 · Cuentas corrientes y abonos`, `clientes/services.py`, `Fase 5 · Bidones y promociones prepago`, `clientes/admin.py`, `clientes/views.py`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 60 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 60 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `base_tienda.html` be split into smaller, more focused modules?**
  _Cohesion score 0.06001984126984127 - nodes in this community are weakly interconnected._
- **Why does `Pedido` connect `6A — Pagos parciales (RF-13) · ~4 h` to `pedidos/views.py`, `vender_promocion`, `logistica/tests.py`, `SuscripcionReposicion`, `logistica/services.py`, `django_urls`, `seed_demo.py`, `PROCEDURE.md`, `Carrito`, `logistica/views.py`, `Cliente`, `pedidos/tests.py`, `Producto`, `Usuario`, `🔎 Auditoría de coherencia — Distribuidora 3.0`, `distribuidora/views.py`, `pedidos/admin.py`, `SuscripcionReposicion`, `GuardsUnificadosTests`, `MetodoPago`, `Command`, `PagosSegurosTests`, `EliminarProductoTests`, `HojaDeRutaUXTests`, `ver_cliente`, `webhook_mercadopago`, `DireccionEntrega`, `TestCase`, `confirmar_pedido`, `clientes/services.py`, `clientes/views.py`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12643678160919541 - nodes in this community are weakly interconnected._