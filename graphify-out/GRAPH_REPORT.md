# Graph Report - distribuidora-3.0  (2026-10-20)

## Corpus Check
- 205 files · ~291,724 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 15 file(s) not represented in the graph (top: (none) 6, .jfif 3, .css 3)

## Summary
- 1609 nodes · 4007 edges · 149 communities (70 shown, 79 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 634 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dc8e34a3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- productos/views.py
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
- logistica/services.py
- productos/admin.py
- AccesoAVistasLogisticasTests
- Producto
- PROCEDURE.md
- Carrito
- CompraPromocion
- Planificación de reparto por zona
- What You Must Do When Invoked
- logistica/views.py
- Cliente
- logistica/admin.py
- crear_cliente_con_cuenta
- pedidos/tests.py
- generar_cargos_mensuales
- permisos/signals.py
- CarritoSoloPorPostTests
- DetalleHojaRuta
- Tests de abonos (RF-05)
- CuentaCorriente
- 🏁 Plan de Cierre — Fases 4.5 a 7
- django_apps
- ZonaForm
- Usuario
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- promociones/views.py
- distribuidora/views.py
- registrar_cargo
- logistica/tests.py
- DetallePedido
- MetodoPago
- Migración: unificar empleados
- GuardsUnificadosTests
- Migración: métodos de pago
- RolSincronizaGrupoTests
- RegistroUsuarioForm
- SemaforizacionTests
- 6A — Pagos parciales (RF-13) · ~4 h
- DireccionEntrega
- Command
- graphify reference: extra exports and benchmark
- SesionTests
- clientes/tests.py
- PagosSegurosTests
- base.py
- EliminarProductoTests
- base_tienda.html
- Abono
- graphify reference: query, path, explain
- ver_cliente
- MovimientoCuenta
- autenticacion/views.py
- 0004_asignar_grupo_permisos.py
- autenticacion/migrations/0001_initial.py
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
- Fase 3 · Logística ↔ Pedido
- BuscarClientesTests
- Barrio
- es_admin_o_vendedor
- roles.py
- VariasDireccionesTests
- FASE3_LOGISTICA.md
- generar_borradores_periodo
- .nivel_morosidad
- Fase 4 · Cuentas corrientes y abonos
- sincronizar_grupo_empleado
- django_contrib
- VistasCuentasTests
- TelefonoContacto
- 0007_marcar_botellones.py
- Fase 5 · Bidones y promociones prepago
- 0003_grupos_base.py
- buscador/views.py
- HistorialBidonesTests
- clientes/views.py
- AbonoForm
- 0010_saldo_inicial_bidones.py
- 0012_completar_pedidos_de_paradas.py
- 0006_corregir_ayuda_desc_seguridad.py
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- TelefonoContacto
- 0011_renumerar_paradas.py
- permisos/apps.py
- ClientesConfig
- DireccionEntregaForm
- autenticacion/apps.py
- perfil_usuario
- buscador/apps.py
- carrito/apps.py
- cuentas/apps.py
- empleados/apps.py
- pedidos/apps.py
- 0006_metodo_cuenta_corriente.py
- productos/apps.py
- H-10 · Suite de tests parcial (faltan carrito y buscador)
- empleados/migrations/0001_initial.py
- 0007_alter_hojaruta_empleado.py
- pedidos/migrations/0001_initial.py
- 0002_pagopedido_tarjeta_titular_and_more.py
- 0004_pedido_confirmado_por_empresa_pedido_fecha_entrega_and_more.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 95 edges
2. `es_admin_o_vendedor()` - 90 edges
3. `Pedido` - 74 edges
4. `Producto` - 67 edges
5. `Zona` - 50 edges
6. `DireccionEntrega` - 48 edges
7. `HojaRuta` - 47 edges
8. `MetodoPago` - 46 edges
9. `Command` - 38 edges
10. `DetalleHojaRuta` - 37 edges

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

## Communities (149 total, 79 thin omitted)

### Community 0 - "productos/views.py"
Cohesion: 0.18
Nodes (10): CategoriaForm, Meta, ProductoForm, Meta, Categoria, crear_categoria(), crear_producto(), editar_producto() (+2 more)

### Community 1 - "pedidos/urls.py"
Cohesion: 0.08
Nodes (19): 1. 🔴 Críticos — seguridad y dinero, Pedido, Meta, consultar_pago_mercadopago(), cambiar_estado_pago(), cambiar_estado_pedido(), checkout(), _cliente_puede_comprar() (+11 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.27
Nodes (12): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+4 more)

### Community 3 - "vender_promocion"
Cohesion: 0.09
Nodes (12): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, FASE 7 — QA, producción y tesis 🎓, Command, consumir_saldo(), revertir_consumos(), vencer_promociones(), vender_promocion(), BasePromociones (+4 more)

### Community 4 - "django_db"
Cohesion: 0.06
Nodes (15): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+7 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.29
Nodes (7): CargoCuentaForm, PagoCuentaForm, _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "django_db_models_deletion"
Cohesion: 0.08
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "abonos/views.py"
Cohesion: 0.40
Nodes (7): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono(), sin_permiso()

### Community 10 - "clientes/urls.py"
Cohesion: 0.20
Nodes (10): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+2 more)

### Community 11 - "Empleado"
Cohesion: 0.32
Nodes (4): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta

### Community 12 - "logistica/services.py"
Cohesion: 0.10
Nodes (18): agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellones_por_producto(), confirmar_entrega_en_calle(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona() (+10 more)

### Community 15 - "Producto"
Cohesion: 0.15
Nodes (3): obtener_o_crear_cuenta(), Producto, saldo_vigente()

### Community 16 - "PROCEDURE.md"
Cohesion: 0.17
Nodes (10): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-04 · ≥2 teléfonos con relación explícita, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose, RF-12 · Carrito no excede stock (+2 more)

### Community 17 - "Carrito"
Cohesion: 0.22
Nodes (7): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), redirigir_a_origen()

### Community 18 - "CompraPromocion"
Cohesion: 0.08
Nodes (14): 5B — Promociones prepago (RF-09) · ~6 h, CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, PromocionForm, Meta, CompraPromocion, Meta (+6 more)

### Community 19 - "Planificación de reparto por zona"
Cohesion: 0.15
Nodes (5): carga_sugerida(), clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests, _productos_para_carga()

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "logistica/views.py"
Cohesion: 0.07
Nodes (39): Hallazgos nuevos, CamionForm, Meta, Camion, Meta, resumen_recorrido(), actualizar_estado_entrega(), agregar_parada() (+31 more)

### Community 23 - "logistica/admin.py"
Cohesion: 0.10
Nodes (15): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+7 more)

### Community 24 - "crear_cliente_con_cuenta"
Cohesion: 0.21
Nodes (4): crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 25 - "pedidos/tests.py"
Cohesion: 0.11
Nodes (13): PagoPedido, Meta, _a_decimal(), aplicar_pago_mercadopago(), firma_webhook_valida(), metodo_pago_efectivo(), pago_en_curso(), registrar_cobro() (+5 more)

### Community 26 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "permisos/signals.py"
Cohesion: 0.22
Nodes (3): _sincronizar(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 28 - "CarritoSoloPorPostTests"
Cohesion: 0.18
Nodes (3): ItemCarrito, Meta, CarritoSoloPorPostTests

### Community 29 - "DetalleHojaRuta"
Cohesion: 0.17
Nodes (4): ActualizarEstadoForm, Meta, DetalleHojaRuta, Meta

### Community 32 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.25
Nodes (7): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, 🏁 Plan de Cierre — Fases 4.5 a 7, main()

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, LogisticaConfig, PromocionesConfig

### Community 35 - "ZonaForm"
Cohesion: 0.23
Nodes (6): ZonaForm, Meta, ZonaFormTests, direcciones_sin_zona(), editar_zona(), listar_zonas()

### Community 36 - "Usuario"
Cohesion: 0.17
Nodes (6): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoForm, Meta, RolEmpleado, Meta

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.29
Nodes (7): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`)

### Community 38 - "promociones/views.py"
Cohesion: 0.18
Nodes (4): csrf_failure(), crear_promocion(), editar_promocion(), _form_promocion()

### Community 39 - "distribuidora/views.py"
Cohesion: 0.21
Nodes (3): clientes_morosos(), resumen_morosidad(), resumen_dashboard()

### Community 40 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 41 - "logistica/tests.py"
Cohesion: 0.06
Nodes (11): Zona, Meta, confirmar_hoja(), ConfirmacionRegresoTests, EntregaCalleTests, GeneracionQuincenalTests, HojaRutaCapacidadTests, HojaSinChoferTests (+3 more)

### Community 42 - "DetallePedido"
Cohesion: 0.16
Nodes (9): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido, Meta (+1 more)

### Community 43 - "MetodoPago"
Cohesion: 0.09
Nodes (17): 4. ❓ Decisiones a tomar antes de empezar, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, fecha_estimada_para_direccion(), CheckoutForm (+9 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 48 - "RegistroUsuarioForm"
Cohesion: 0.18
Nodes (5): RegistroUsuarioForm, Meta, _solo_digitos(), AltaClienteConCuentaForm, Meta

### Community 50 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.15
Nodes (8): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original), 6A — Pagos parciales (RF-13) · ~4 h

### Community 51 - "DireccionEntrega"
Cohesion: 0.33
Nodes (3): DireccionEntrega, Meta, RF-03 · Multidirección de entrega

### Community 52 - "Command"
Cohesion: 0.06
Nodes (15): 5A — Historial de envases (RF-08) · ~4 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones() (+7 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "clientes/tests.py"
Cohesion: 0.16
Nodes (3): AgregarDireccionTests, FiadoPremiumYExcepcionTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.06
Nodes (7): metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, CobroManualTests, PagosParcialesTests, PagosSegurosTests, TransicionesManualesTests

### Community 67 - "base_tienda.html"
Cohesion: 0.29
Nodes (4): listar_productos(), ver_producto(), inicio(), RNF-03 · Dark mode sin autenticación

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "ver_cliente"
Cohesion: 0.32
Nodes (4): _contexto_suscripcion(), mi_perfil_cliente(), ver_cliente(), compras_vigentes()

### Community 71 - "MovimientoCuenta"
Cohesion: 0.22
Nodes (3): MovimientoCuenta, Meta, ReglaFiadoTests

### Community 72 - "autenticacion/views.py"
Cohesion: 0.31
Nodes (4): IngresarUsuarioForm, cerrar_sesion(), ingresar_usuario(), registrar_usuario()

### Community 73 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 74 - "autenticacion/migrations/0001_initial.py"
Cohesion: 0.25
Nodes (3): Migration, Migration, Migration

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
Cohesion: 0.24
Nodes (4): HojaRutaForm, Meta, HojaRuta, Meta

### Community 99 - "Fase 3 · Logística ↔ Pedido"
Cohesion: 0.25
Nodes (8): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, RF-16 · Hojas de ruta diarias, RF-17 · Agrupación automática y generación de hojas, RF-19 · Confirmación de entrega por repartidor, RNF-01 · Escalabilidad multi-camión/zona/chofer, RNF-02 · Ocultación de la nota de seguridad

### Community 101 - "Barrio"
Cohesion: 0.09
Nodes (16): AgregarParadaForm, BarrioForm, Meta, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta, Command, Barrio (+8 more)

### Community 102 - "es_admin_o_vendedor"
Cohesion: 0.17
Nodes (4): es_admin_o_vendedor(), EvaluacionDeRolesTests, VenderPromocionForm, vender_promocion()

### Community 103 - "roles.py"
Cohesion: 0.08
Nodes (22): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_vendedor(), puede_ver_nota_seguridad() (+14 more)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "generar_borradores_periodo"
Cohesion: 0.20
Nodes (3): Command, generar_borradores_periodo(), pedidos_candidatos()

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 109 - "sincronizar_grupo_empleado"
Cohesion: 0.33
Nodes (3): sincronizar_grupo_empleado(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado()

### Community 114 - "TelefonoContacto"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 116 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 117 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 121 - "clientes/views.py"
Cohesion: 0.14
Nodes (11): BuscarClienteForm, ClienteForm, Meta, ClienteSinCuentaForm, Meta, EditarMiPerfilForm, MovimientoBidonForm, listar_clientes() (+3 more)

### Community 127 - "TelefonoContacto"
Cohesion: 0.17
Nodes (6): Detalle, TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente()

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 648 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **79 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/urls.py`, `vender_promocion`, `cuentas/views.py`, `clientes/urls.py`, `logistica/services.py`, `AccesoAVistasLogisticasTests`, `Producto`, `PROCEDURE.md`, `Planificación de reparto por zona`, `logistica/views.py`, `crear_cliente_con_cuenta`, `pedidos/tests.py`, `generar_cargos_mensuales`, `permisos/signals.py`, `Tests de abonos (RF-05)`, `CuentaCorriente`, `Usuario`, `promociones/views.py`, `distribuidora/views.py`, `registrar_cargo`, `logistica/tests.py`, `MetodoPago`, `SemaforizacionTests`, `Command`, `clientes/tests.py`, `PagosSegurosTests`, `Abono`, `ver_cliente`, `MovimientoCuenta`, `PlanificarRepartoViewTests`, `BuscarClientesTests`, `es_admin_o_vendedor`, `roles.py`, `Fase 4 · Cuentas corrientes y abonos`, `VistasCuentasTests`, `TelefonoContacto`, `Fase 5 · Bidones y promociones prepago`, `HistorialBidonesTests`, `clientes/views.py`, `AbonoForm`, `TelefonoContacto`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Are the 57 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 57 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `pedidos/urls.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07619738751814223 - nodes in this community are weakly interconnected._
- **Why does `Pedido` connect `pedidos/urls.py` to `vender_promocion`, `SuscripcionReposicion`, `logistica/services.py`, `Producto`, `PROCEDURE.md`, `CompraPromocion`, `Planificación de reparto por zona`, `logistica/views.py`, `Cliente`, `pedidos/tests.py`, `Usuario`, `distribuidora/views.py`, `logistica/tests.py`, `DetallePedido`, `MetodoPago`, `GuardsUnificadosTests`, `6A — Pagos parciales (RF-13) · ~4 h`, `DireccionEntrega`, `Command`, `PagosSegurosTests`, `EliminarProductoTests`, `ver_cliente`, `generar_borradores_periodo`, `clientes/views.py`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `vender_promocion` be split into smaller, more focused modules?**
  _Cohesion score 0.08780487804878048 - nodes in this community are weakly interconnected._