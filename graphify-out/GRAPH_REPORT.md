# Graph Report - obsidian-vault-setup-9a38f1  (2026-11-12)

## Corpus Check
- 228 files · ~300,642 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 20 file(s) not represented in the graph (top: (none) 7, .css 4, .jfif 3)

## Summary
- 1844 nodes · 4471 edges · 157 communities (79 shown, 78 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 676 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e9a39d47`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- pedidos/views.py
- empleados/views.py
- vender_promocion
- django_db
- ModeloEmpleadoUnicoTests
- cuentas/views.py
- logistica/forms.py
- PedidoAutomaticoTests
- abonos/views.py
- clientes/views.py
- Empleado
- logistica/services.py
- Producto
- productos/views.py
- seed_demo.py
- PROCEDURE.md
- Carrito
- CarritoSoloPorPostTests
- PedidoEspontaneoTests
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- logistica/admin.py
- crear_cliente_con_cuenta
- pedidos/views.py
- generar_cargos_mensuales
- clientes.md
- Abono
- pedidos/tests.py
- Tests de abonos (RF-05)
- CuentaCorriente
- es_admin_vendedor_o_repartidor
- puede_ver_nota_seguridad
- django_apps
- GeneracionBorradorTests
- base_tienda.html
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- Usuario
- distribuidora/views.py
- registrar_cargo
- Zona
- pedidos/admin.py
- SuscripcionReposicion
- Migración: unificar empleados
- StockComprometidoTests
- Migración: métodos de pago
- ProductoForm
- CompraPromocion
- sincronizar_grupo_empleado
- 6A — Pagos parciales (RF-13) · ~4 h
- MetodoPago
- Command
- graphify reference: extra exports and benchmark
- SesionTests
- clientes/tests.py
- PagosSegurosTests
- validadores.py
- clientes/services.py
- base.py
- EliminarProductoTests
- AccesoAVistasLogisticasTests
- GuardsUnificadosTests
- graphify reference: query, path, explain
- base_dashboard.html
- django_contrib
- django_urls
- Fase 6 · Pagos parciales y pedido automático
- popups.js
- TelefonoContacto
- permisos/apps.py
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- logistica/tests.py
- Verificar cambios — Distribuidora 3.0
- Verificar cambios — Distribuidora 3.0
- ClientesConfig
- RegistroUsuarioForm
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
- RolSincronizaGrupoTests
- Distribuidora 3.0 / Aquadelluvia
- buscador/apps.py
- carrito/apps.py
- seed_barrios.py
- listar_clientes
- logistica/apps.py
- HojaRuta
- productos/apps.py
- validar_telefono
- django_db_models_deletion
- obtener_o_crear_cuenta
- registrar_movimiento_bidon
- BuscarClientesTests
- EditarMiPerfilTests
- clientes/forms.py
- VariasDireccionesTests
- validar_dni
- 🌊 Distribuidora 3.0 / Aquadelluvia
- RegistroTelefonosTests
- CuentaDeRepartidorTests
- {{title}}
- RecuperarContrasenaTests
- HistorialBidonesTests
- VistaMovimientoBidonTests
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- {{title}}
- {{date}}
- NuevaContrasenaForm
- RecuperarContrasenaForm
- 0004_asignar_grupo_permisos.py
- Command
- buscador
- permisos
- autenticacion/apps.py
- promociones/apps.py
- C-9 — Gastos por proveedor (RF-20)

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 100 edges
2. `es_admin_o_vendedor()` - 87 edges
3. `Pedido` - 76 edges
4. `Producto` - 69 edges
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

## Communities (157 total, 78 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.19
Nodes (6): IngresarUsuarioForm, ingresar_usuario(), perfil_usuario(), registrar_usuario(), _ya_ingresado(), destino_personal()

### Community 1 - "pedidos/views.py"
Cohesion: 0.11
Nodes (11): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr() (+3 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.27
Nodes (12): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+4 more)

### Community 3 - "vender_promocion"
Cohesion: 0.06
Nodes (17): PromocionForm, Meta, VenderPromocionForm, Promocion, Meta, consumir_saldo(), vender_promocion(), BasePromociones (+9 more)

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (24): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+16 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "logistica/forms.py"
Cohesion: 0.08
Nodes (15): ActualizarEstadoForm, Meta, AgregarParadaForm, BarrioForm, Meta, CamionForm, Meta, _etiqueta_direccion_cliente() (+7 more)

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.23
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "abonos/views.py"
Cohesion: 0.40
Nodes (7): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono(), sin_permiso()

### Community 10 - "clientes/views.py"
Cohesion: 0.22
Nodes (13): DireccionEntregaForm, Meta, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion() (+5 more)

### Community 11 - "Empleado"
Cohesion: 0.22
Nodes (6): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta

### Community 12 - "logistica/services.py"
Cohesion: 0.08
Nodes (21): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellones_por_producto(), confirmar_entrega_en_calle() (+13 more)

### Community 13 - "Producto"
Cohesion: 0.21
Nodes (5): CategoriaAdmin, ProductoAdmin, Categoria, Producto, AltaProductoTests

### Community 14 - "productos/views.py"
Cohesion: 0.17
Nodes (11): CategoriaForm, Meta, crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria(), eliminar_producto() (+3 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (9): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, H-10 · Suite de tests parcial (faltan carrito y buscador), H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose, RNF-01 · Escalabilidad multi-camión/zona/chofer (+1 more)

### Community 17 - "Carrito"
Cohesion: 0.20
Nodes (7): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito()

### Community 19 - "PedidoEspontaneoTests"
Cohesion: 0.13
Nodes (7): entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), resumen_recorrido(), PedidoEspontaneoTests, registrar_regreso_ruta()

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.07
Nodes (39): Hallazgos nuevos, HojaRutaForm, Meta, Camion, Meta, carga_sugerida(), actualizar_estado_entrega(), agregar_parada() (+31 more)

### Community 23 - "logistica/admin.py"
Cohesion: 0.10
Nodes (15): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+7 more)

### Community 24 - "crear_cliente_con_cuenta"
Cohesion: 0.16
Nodes (6): AltaClienteConCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 25 - "pedidos/views.py"
Cohesion: 0.14
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), checkout(), _cliente_puede_comprar(), pago_exitoso(), webhook_mercadopago() (+1 more)

### Community 26 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 27 - "clientes.md"
Cohesion: 0.06
Nodes (30): abonos, Notas, Relaciones, autenticacion, Notas, Relaciones, carrito, Notas (+22 more)

### Community 28 - "Abono"
Cohesion: 0.18
Nodes (4): AbonoForm, Meta, Abono, Meta

### Community 29 - "pedidos/tests.py"
Cohesion: 0.11
Nodes (11): 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, PagoPedido, Meta, _a_decimal(), firma_webhook_valida(), metodo_pago_efectivo(), registrar_cobro() (+3 more)

### Community 34 - "django_apps"
Cohesion: 0.15
Nodes (4): AbonosConfig, CuentasConfig, EmpleadosConfig, PedidosConfig

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.26
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 36 - "base_tienda.html"
Cohesion: 0.22
Nodes (4): csrf_failure(), listar_productos(), ver_producto(), inicio()

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.17
Nodes (8): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, confirmar_pago_qr(), main()

### Community 38 - "Usuario"
Cohesion: 0.13
Nodes (6): 2. 🟠 Altos — errores funcionales, Migration, Usuario, EmpleadoForm, Meta, validar_nombre()

### Community 39 - "distribuidora/views.py"
Cohesion: 0.19
Nodes (4): clientes_morosos(), resumen_morosidad(), promociones_por_vencer(), resumen_dashboard()

### Community 40 - "registrar_cargo"
Cohesion: 0.09
Nodes (7): MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, ReglaFiadoTests, SemaforizacionTests

### Community 41 - "Zona"
Cohesion: 0.16
Nodes (6): ZonaForm, Meta, Zona, Meta, ZonaDiasRepartoTests, ZonaFormTests

### Community 42 - "pedidos/admin.py"
Cohesion: 0.11
Nodes (10): HojaDeRutaUXTests, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido (+2 more)

### Community 43 - "SuscripcionReposicion"
Cohesion: 0.11
Nodes (18): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h (+10 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 47 - "ProductoForm"
Cohesion: 0.13
Nodes (4): ProductoForm, Meta, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 48 - "CompraPromocion"
Cohesion: 0.16
Nodes (7): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, CompraPromocion, Meta, ConsumoPromocion, Meta

### Community 49 - "sincronizar_grupo_empleado"
Cohesion: 0.24
Nodes (5): sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 50 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.13
Nodes (5): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), Punto de partida real, SeedDemoTests, Pedido, Meta

### Community 51 - "MetodoPago"
Cohesion: 0.13
Nodes (6): fecha_estimada_para_direccion(), CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, confirmar_pedido()

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "clientes/tests.py"
Cohesion: 0.17
Nodes (5): ClienteForm, Meta, AgregarDireccionTests, FiadoPremiumYExcepcionTests, ValidacionesClienteTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.06
Nodes (8): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, CobroManualTests, PagosParcialesTests, PagosSegurosTests, TransicionesManualesTests

### Community 62 - "validadores.py"
Cohesion: 0.21
Nodes (3): normalizar_patente(), validar_altura(), validar_coordenadas()

### Community 63 - "clientes/services.py"
Cohesion: 0.23
Nodes (6): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "base_dashboard.html"
Cohesion: 0.19
Nodes (8): cerrar_sesion(), buscar_productos(), ver_carrito(), editar_mi_perfil(), mi_perfil_cliente(), solo_clientes(), Arquitectura visual dual: Tienda vs Dashboard, RNF-03 · Dark mode sin autenticación

### Community 71 - "django_contrib"
Cohesion: 0.20
Nodes (4): AbonoAdmin, CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

### Community 73 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 74 - "popups.js"
Cohesion: 0.36
Nodes (9): erroresDelServidor(), escapar(), etiquetaDe(), leerMensajes(), listaHtml(), mensajeDe(), mostrarAvisos(), mostrarTodo() (+1 more)

### Community 75 - "TelefonoContacto"
Cohesion: 0.22
Nodes (4): Detalle, TelefonoContacto, Meta, crear_perfil_cliente()

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 98 - "logistica/tests.py"
Cohesion: 0.05
Nodes (21): DireccionEntrega, Meta, Barrio, Meta, CargaHojaRuta, Meta, RutaReparto, Meta (+13 more)

### Community 99 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 100 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.25
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 103 - "roles.py"
Cohesion: 0.29
Nodes (9): 4. ♻️ Redundancias, roles_usuario(), _en_grupo(), es_admin(), es_personal_interno(), es_repartidor(), es_vendedor(), 2. Revisar convenciones del proyecto en lo que cambió (+1 more)

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (7): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (7): Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, Fase 3 · Logística ↔ Pedido, RF-16 · Hojas de ruta diarias, RF-17 · Agrupación automática y generación de hojas, RF-19 · Confirmación de entrega por repartidor

### Community 106 - "generar_borradores_periodo"
Cohesion: 0.20
Nodes (3): Command, generar_borradores_periodo(), pedidos_candidatos()

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.29
Nodes (5): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-14 · Semaforización de deuda, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 110 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 114 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 117 - "Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 121 - "listar_clientes"
Cohesion: 0.21
Nodes (7): BuscarClienteForm, listar_clientes(), _texto_buscable(), marcar(), Migration, _normalizar(), normalizar_texto()

### Community 126 - "django_db_models_deletion"
Cohesion: 0.06
Nodes (17): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+9 more)

### Community 128 - "registrar_movimiento_bidon"
Cohesion: 0.29
Nodes (3): MovimientoBidonForm, registrar_movimiento_bidon(), errores_en_texto()

### Community 133 - "clientes/forms.py"
Cohesion: 0.11
Nodes (7): ClienteSinCuentaForm, EditarMiPerfilForm, TelefonoContactoForm, Meta, _ValidarDatosPersonalesMixin, aplicar_attrs(), validar_fecha_no_futura()

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.29
Nodes (6): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aquadelluvia, 📚 Documentación del proyecto

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 146 - "{{title}}"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, Qué pasa, {{title}}

### Community 147 - "{{date}}"
Cohesion: 0.40
Nodes (4): Bloqueos / dudas, {{date}}, Pendiente, Qué hice

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 153 - "permisos"
Cohesion: 0.50
Nodes (3): Notas, permisos, Relaciones

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 760 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **78 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `registrar_movimiento_bidon`, `BuscarClientesTests`, `pedidos/views.py`, `vender_promocion`, `clientes/forms.py`, `cuentas/views.py`, `clientes/views.py`, `CuentaDeRepartidorTests`, `logistica/services.py`, `HistorialBidonesTests`, `seed_demo.py`, `VistaMovimientoBidonTests`, `PROCEDURE.md`, `PedidoEspontaneoTests`, `base_dashboard.html`, `crear_cliente_con_cuenta`, `pedidos/views.py`, `generar_cargos_mensuales`, `Abono`, `pedidos/tests.py`, `Tests de abonos (RF-05)`, `CuentaCorriente`, `es_admin_vendedor_o_repartidor`, `puede_ver_nota_seguridad`, `GeneracionBorradorTests`, `distribuidora/views.py`, `registrar_cargo`, `pedidos/admin.py`, `SuscripcionReposicion`, `6A — Pagos parciales (RF-13) · ~4 h`, `MetodoPago`, `Command`, `clientes/tests.py`, `PagosSegurosTests`, `clientes/services.py`, `AccesoAVistasLogisticasTests`, `base_dashboard.html`, `TelefonoContacto`, `logistica/tests.py`, `perfil_cliente_esta_vacio`, `Fase 4 · Cuentas corrientes y abonos`, `permisos/signals.py`, `Fase 5 · Bidones y promociones prepago`, `clientes/admin.py`, `listar_clientes`, `obtener_o_crear_cuenta`?**
  _High betweenness centrality (0.163) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 62 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10804597701149425 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `vender_promocion`, `logistica/forms.py`, `PedidoAutomaticoTests`, `logistica/services.py`, `productos/views.py`, `seed_demo.py`, `Carrito`, `CarritoSoloPorPostTests`, `PedidoEspontaneoTests`, `base_dashboard.html`, `pedidos/views.py`, `generar_cargos_mensuales`, `Abono`, `pedidos/tests.py`, `Tests de abonos (RF-05)`, `GeneracionBorradorTests`, `base_tienda.html`, `distribuidora/views.py`, `pedidos/admin.py`, `SuscripcionReposicion`, `StockComprometidoTests`, `ProductoForm`, `MetodoPago`, `Command`, `PagosSegurosTests`, `EliminarProductoTests`, `base_dashboard.html`, `django_urls`, `logistica/tests.py`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `es_admin_o_vendedor()` (e.g. with `2. 🟠 Altos — errores funcionales` and `4. ♻️ Redundancias`) actually correct?**
  _`es_admin_o_vendedor()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `vender_promocion` be split into smaller, more focused modules?**
  _Cohesion score 0.06493506493506493 - nodes in this community are weakly interconnected._