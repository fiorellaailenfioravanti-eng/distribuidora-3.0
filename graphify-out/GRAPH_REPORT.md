# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 205 files · ~289,586 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1589 nodes · 3945 edges · 132 communities (71 shown, 61 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 618 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4a14390d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- base_tienda.html
- pedidos/urls.py
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
- DetalleHojaRuta
- Producto
- AccesoAVistasLogisticasTests
- seed_demo.py
- PROCEDURE.md
- actualizar_estado_entrega
- promociones/views.py
- Planificación de reparto por zona
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- Calendario de reparto
- crear_cliente_con_cuenta
- logistica/services.py
- generar_cargos_mensuales
- permisos/signals.py
- HojaDeRutaUXTests
- ver_ruta
- Tests de abonos (RF-05)
- CuentaCorriente
- 🏁 Plan de Cierre — Fases 4.5 a 7
- Arranque Django (asgi/wsgi)
- django_apps
- puede_ver_nota_seguridad
- Usuario
- aplicar_pago_mercadopago
- django_contrib
- distribuidora/views.py
- registrar_cargo
- Zona
- DetallePedido
- pedidos/views.py
- Migración: unificar empleados
- GuardsUnificadosTests
- Migración: métodos de pago
- RolSincronizaGrupoTests
- RegistroUsuarioForm
- SemaforizacionTests
- Pedido
- DireccionEntrega
- Command
- graphify reference: extra exports and benchmark
- SesionTests
- VariasDireccionesTests
- PagosSegurosTests
- base.py
- EliminarProductoTests
- TestCase
- Abono
- graphify reference: query, path, explain
- ver_cliente
- MovimientoCuenta
- vencer_promociones
- 0004_asignar_grupo_permisos.py
- CompraPromocion
- PlanificarRepartoViewTests
- cuentas/admin.py
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- HojaRuta
- promociones/admin.py
- DetallePedido
- logistica/tests.py
- es_admin_o_vendedor
- roles.py
- VistasPromocionesTests
- FASE3_LOGISTICA.md
- generar_borradores_periodo
- logistica/views.py
- Fase 4 · Cuentas corrientes y abonos
- Verificar cambios — Distribuidora 3.0
- Fase 6 · Pagos parciales y pedido automático
- VistasCuentasTests
- TelefonoContacto
- 0007_marcar_botellones.py
- Fase 5 · Bidones y promociones prepago
- 0003_grupos_base.py
- ClienteSinCuentaForm
- Verificar cambios — Distribuidora 3.0
- clientes/views.py
- AbonoForm
- 0010_saldo_inicial_bidones.py
- 0012_completar_pedidos_de_paradas.py
- 0006_corregir_ayuda_desc_seguridad.py
- Distribuidora 3.0 / Aquadelluvia
- TelefonoContactoForm
- 0011_renumerar_paradas.py
- es_repartidor_asignado

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 94 edges
2. `es_admin_o_vendedor()` - 89 edges
3. `Pedido` - 74 edges
4. `Producto` - 66 edges
5. `Zona` - 49 edges
6. `DireccionEntrega` - 47 edges
7. `HojaRuta` - 46 edges
8. `MetodoPago` - 42 edges
9. `Command` - 38 edges
10. `DetalleHojaRuta` - 36 edges

## Surprising Connections (you probably didn't know these)
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `5. 🔗 Dependencias y archivos compartidos` --references--> `registrar_cobro()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/pedidos/services.py
- `Detalle` --references--> `Usuario`  [INFERRED]
  .agents/CONTROL_REQUISITOS.md → apps/autenticacion/models.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (132 total, 61 thin omitted)

### Community 0 - "base_tienda.html"
Cohesion: 0.05
Nodes (26): buscar_productos(), carrito_total(), Carrito, ItemCarrito, Meta, CarritoSoloPorPostTests, agregar_al_carrito(), eliminar_del_carrito() (+18 more)

### Community 1 - "pedidos/urls.py"
Cohesion: 0.10
Nodes (11): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr() (+3 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.27
Nodes (12): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+4 more)

### Community 3 - "vender_promocion"
Cohesion: 0.20
Nodes (4): consumir_saldo(), vender_promocion(), EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.04
Nodes (21): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+13 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.25
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "django_db_models_deletion"
Cohesion: 0.06
Nodes (18): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+10 more)

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.15
Nodes (7): 4. ❓ Decisiones a tomar antes de empezar, 6C — Pedido automático quincenal (RF-18) · ~4 h, Command, SuscripcionReposicion, Meta, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "abonos/views.py"
Cohesion: 0.40
Nodes (7): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono(), sin_permiso()

### Community 10 - "clientes/urls.py"
Cohesion: 0.32
Nodes (9): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+1 more)

### Community 11 - "Empleado"
Cohesion: 0.19
Nodes (6): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta

### Community 12 - "DetalleHojaRuta"
Cohesion: 0.06
Nodes (27): 5A — Historial de envases (RF-08) · ~4 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, HistorialBidonesTests, BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin (+19 more)

### Community 13 - "Producto"
Cohesion: 0.14
Nodes (6): CategoriaAdmin, ProductoAdmin, Categoria, Producto, revertir_consumos(), H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.16
Nodes (14): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose (+6 more)

### Community 17 - "actualizar_estado_entrega"
Cohesion: 0.17
Nodes (8): actualizar_estado_entrega(), agregar_parada(), agregar_pedido_parada(), _ids_de_paradas_con_nota(), imprimir_ruta(), mi_ruta_hoy(), _volver_a_hoja(), obtener_empleado()

### Community 18 - "promociones/views.py"
Cohesion: 0.15
Nodes (9): PromocionForm, Meta, VenderPromocionForm, Promocion, Meta, crear_promocion(), editar_promocion(), _form_promocion() (+1 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.18
Nodes (12): Hallazgos nuevos, crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_zona(), eliminar_camion(), eliminar_parada(), eliminar_zona() (+4 more)

### Community 22 - "Cliente"
Cohesion: 0.15
Nodes (3): Cliente, Meta, BasePromociones

### Community 23 - "Calendario de reparto"
Cohesion: 0.24
Nodes (3): fecha_es_de_reparto(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "crear_cliente_con_cuenta"
Cohesion: 0.21
Nodes (4): crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 25 - "logistica/services.py"
Cohesion: 0.09
Nodes (13): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), CalendarioExcepcion, Meta (+5 more)

### Community 26 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "permisos/signals.py"
Cohesion: 0.12
Nodes (7): crear_perfil_cliente(), sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 29 - "ver_ruta"
Cohesion: 0.10
Nodes (11): ActualizarEstadoForm, Meta, AgregarParadaForm, _etiqueta_direccion_cliente(), botellon_por_defecto(), clientes_frecuentes_de_zona(), construir_borrador(), direccion_en_zona() (+3 more)

### Community 31 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 32 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.25
Nodes (6): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, 🏁 Plan de Cierre — Fases 4.5 a 7

### Community 34 - "django_apps"
Cohesion: 0.05
Nodes (12): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, CuentasConfig, EmpleadosConfig, LogisticaConfig (+4 more)

### Community 36 - "Usuario"
Cohesion: 0.22
Nodes (4): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoForm, Meta

### Community 37 - "aplicar_pago_mercadopago"
Cohesion: 0.10
Nodes (16): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`) (+8 more)

### Community 39 - "distribuidora/views.py"
Cohesion: 0.15
Nodes (6): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, resumen_caja(), resumen_dashboard()

### Community 40 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 41 - "Zona"
Cohesion: 0.16
Nodes (6): ZonaForm, Meta, Zona, Meta, ZonaDiasRepartoTests, ZonaFormTests

### Community 42 - "DetallePedido"
Cohesion: 0.36
Nodes (6): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin

### Community 43 - "pedidos/views.py"
Cohesion: 0.16
Nodes (7): CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, checkout(), _cliente_puede_comprar(), saldo_vigente()

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 48 - "RegistroUsuarioForm"
Cohesion: 0.08
Nodes (16): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original), IngresarUsuarioForm, RegistroUsuarioForm (+8 more)

### Community 50 - "Pedido"
Cohesion: 0.11
Nodes (11): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real (+3 more)

### Community 51 - "DireccionEntrega"
Cohesion: 0.12
Nodes (8): BuscarClienteForm, ClienteForm, Meta, DireccionEntregaForm, Meta, EditarMiPerfilForm, DireccionEntrega, Meta

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "VariasDireccionesTests"
Cohesion: 0.09
Nodes (5): AgregarDireccionTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.05
Nodes (10): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), firma_webhook_valida(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, CobroManualTests, _firmar(), PagosParcialesTests (+2 more)

### Community 67 - "TestCase"
Cohesion: 0.18
Nodes (3): HojaRutaCapacidadTests, HojaSinChoferTests, SeedDemoTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "ver_cliente"
Cohesion: 0.24
Nodes (4): _contexto_suscripcion(), mi_perfil_cliente(), ver_cliente(), compras_vigentes()

### Community 71 - "MovimientoCuenta"
Cohesion: 0.22
Nodes (3): MovimientoCuenta, Meta, ReglaFiadoTests

### Community 72 - "vencer_promociones"
Cohesion: 0.29
Nodes (4): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, FASE 7 — QA, producción y tesis 🎓, Command, vencer_promociones()

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 74 - "CompraPromocion"
Cohesion: 0.25
Nodes (4): CompraPromocion, Meta, promociones_por_vencer(), listar_promociones()

### Community 76 - "cuentas/admin.py"
Cohesion: 0.50
Nodes (3): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

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
Cohesion: 0.21
Nodes (5): HojaRutaForm, Meta, HojaRuta, Meta, editar_ruta()

### Community 99 - "promociones/admin.py"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 100 - "DetallePedido"
Cohesion: 0.40
Nodes (3): DetallePedido, Meta, stock_comprometido()

### Community 101 - "logistica/tests.py"
Cohesion: 0.09
Nodes (18): BarrioForm, Meta, RutaRepartoForm, Meta, Barrio, Meta, CargaHojaRuta, Meta (+10 more)

### Community 102 - "es_admin_o_vendedor"
Cohesion: 0.21
Nodes (3): es_admin_o_vendedor(), es_admin_vendedor_o_repartidor(), EvaluacionDeRolesTests

### Community 103 - "roles.py"
Cohesion: 0.29
Nodes (9): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_vendedor(), 2. Revisar convenciones del proyecto en lo que cambió (+1 more)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.29
Nodes (3): Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "generar_borradores_periodo"
Cohesion: 0.18
Nodes (3): Command, generar_borradores_periodo(), GeneracionQuincenalTests

### Community 107 - "logistica/views.py"
Cohesion: 0.11
Nodes (19): CamionForm, Meta, Camion, Meta, botellones_por_producto(), entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja() (+11 more)

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 109 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 110 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 114 - "TelefonoContacto"
Cohesion: 0.16
Nodes (8): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, TelefonoContacto, Meta

### Community 116 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 117 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 120 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 121 - "clientes/views.py"
Cohesion: 0.29
Nodes (5): MovimientoBidonForm, listar_clientes(), registrar_movimiento_bidon(), _texto_buscable(), normalizar_texto()

### Community 126 - "Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aquadelluvia, graphify, graphify

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 637 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **61 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/urls.py`, `vender_promocion`, `cuentas/views.py`, `SuscripcionReposicion`, `clientes/urls.py`, `Empleado`, `DetalleHojaRuta`, `Producto`, `AccesoAVistasLogisticasTests`, `seed_demo.py`, `PROCEDURE.md`, `actualizar_estado_entrega`, `promociones/views.py`, `Planificación de reparto por zona`, `crear_cliente_con_cuenta`, `logistica/services.py`, `generar_cargos_mensuales`, `permisos/signals.py`, `HojaDeRutaUXTests`, `ver_ruta`, `Tests de abonos (RF-05)`, `CuentaCorriente`, `puede_ver_nota_seguridad`, `distribuidora/views.py`, `registrar_cargo`, `pedidos/views.py`, `RegistroUsuarioForm`, `SemaforizacionTests`, `Pedido`, `DireccionEntrega`, `Command`, `VariasDireccionesTests`, `PagosSegurosTests`, `TestCase`, `Abono`, `ver_cliente`, `MovimientoCuenta`, `PlanificarRepartoViewTests`, `logistica/tests.py`, `generar_borradores_periodo`, `logistica/views.py`, `Fase 4 · Cuentas corrientes y abonos`, `VistasCuentasTests`, `TelefonoContacto`, `Fase 5 · Bidones y promociones prepago`, `ClienteSinCuentaForm`, `clientes/views.py`, `AbonoForm`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 56 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 56 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `base_tienda.html` be split into smaller, more focused modules?**
  _Cohesion score 0.05359937402190924 - nodes in this community are weakly interconnected._
- **Why does `es_admin_o_vendedor()` connect `es_admin_o_vendedor` to `base_tienda.html`, `pedidos/urls.py`, `empleados/views.py`, `cuentas/views.py`, `abonos/views.py`, `clientes/urls.py`, `Empleado`, `actualizar_estado_entrega`, `promociones/views.py`, `base_dashboard.html`, `crear_cliente_con_cuenta`, `ver_ruta`, `puede_ver_nota_seguridad`, `Usuario`, `distribuidora/views.py`, `pedidos/views.py`, `Pedido`, `ver_cliente`, `CompraPromocion`, `HojaRuta`, `roles.py`, `logistica/views.py`, `clientes/views.py`, `Distribuidora 3.0 / Aquadelluvia`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/urls.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1010752688172043 - nodes in this community are weakly interconnected._