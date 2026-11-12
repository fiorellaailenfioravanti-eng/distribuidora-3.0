# Graph Report - obsidian-vault-setup-9a38f1  (2026-11-12)

## Corpus Check
- 261 files · ~326,610 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 22 file(s) not represented in the graph (top: (none) 7, .css 4, .jfif 3)

## Summary
- 2052 nodes · 4854 edges · 164 communities (108 shown, 56 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 696 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ccba0a51`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- django_contrib
- pedidos/views.py
- empleados/views.py
- vender_promocion
- django_db
- logistica/views.py
- cuentas/views.py
- venta_calle
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- Empleado
- logistica/services.py
- H-10 · Suite de tests parcial (faltan carrito y buscador)
- productos/views.py
- Producto
- PROCEDURE.md
- Carrito
- CarritoSoloPorPostTests
- PedidoEspontaneoTests
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- logistica/admin.py
- ClienteForm
- EntregaCalleTests
- Promocion
- QA 2026-11-12.md
- django_db_models_deletion
- SuscripcionReposicion
- CheckoutConSaldoTests
- CuentaCorriente
- puede
- listar_clientes
- django_apps
- construir_borrador
- base_tienda.html
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- PerfilUsuarioForm
- distribuidora/views.py
- Command
- DireccionEntrega
- HojaDeRutaUXTests
- SuscripcionReposicion
- Migración: unificar empleados
- ver_ruta
- Migración: métodos de pago
- logistica/admin.py
- CompraPromocion
- mi_ruta_hoy
- 6A — Pagos parciales (RF-13) · ~4 h
- confirmar_pedido
- Command
- graphify reference: extra exports and benchmark
- PerfilPersonalTests
- VariasDireccionesTests
- PagosSegurosTests
- clientes/forms.py
- clientes/services.py
- base.py
- RolEmpleadoForm
- puede_ver_nota_seguridad
- Usuario
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- GuardsUnificadosTests
- TelefonoContacto
- Fase 6 · Pagos parciales y pedido automático
- popups.js
- QA-02 Pago mayor a la deuda
- autenticacion/migrations/0001_initial.py
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- RecorridoRepartidorTests
- Verificar cambios — Distribuidora 3.0
- QA-04 Abono con costo 0
- pedidos/admin.py
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- generar_borradores_periodo
- QA-05 Zona sin días de reparto
- Fase 4 · Cuentas corrientes y abonos
- 🌊 Distribuidora 3.0 / Aquadelluvia
- Fase 5 · Bidones y promociones prepago
- 0013_detallehojaruta_es_venta_calle.py
- actualizar_estado_entrega
- QA-06 Email de producción sin configurar
- ModeloEmpleadoUnicoTests
- django_contrib
- CuentaDeRepartidorTests
- QA-09 Recuperar contraseña usa vistas de clase
- permisos/views.py
- 0002_bidones_recargables_y_rol_recargador.py
- CalendarioExcepcion
- QA campo a campo — 12/11/2026
- StockComprometidoTests
- 0003_grupos_base.py
- 0007_marcar_botellones.py
- 0006_corregir_ayuda_desc_seguridad.py
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- Camion
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- os
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- Verificar cambios — Distribuidora 3.0
- {{title}}
- 0010_saldo_inicial_bidones.py
- 0011_renumerar_paradas.py
- abonos
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- autenticacion
- {{title}}
- {{date}}
- NuevaContrasenaForm
- carrito
- 0004_asignar_grupo_permisos.py
- logistica/tests.py
- buscador
- clientes
- cuentas
- 0012_completar_pedidos_de_paradas.py
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- pedidos
- productos
- promociones

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 102 edges
2. `puede()` - 91 edges
3. `Producto` - 77 edges
4. `Pedido` - 76 edges
5. `Zona` - 53 edges
6. `DireccionEntrega` - 51 edges
7. `HojaRuta` - 51 edges
8. `MetodoPago` - 47 edges
9. `Empleado` - 40 edges
10. `Command` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Funciones y roles por defecto` --references--> `cambiar_tipo_cliente()`  [INFERRED]
  notas/Roles y permisos.md → apps/clientes/views.py
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `5D — Tests · ~2 h` --references--> `registrar_entrega()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/logistica/services.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (164 total, 56 thin omitted)

### Community 0 - "django_contrib"
Cohesion: 0.11
Nodes (11): IngresarUsuarioForm, RecuperarContrasenaForm, ingresar_usuario(), perfil_usuario(), registrar_usuario(), _ya_ingresado(), roles_usuario(), es_personal_interno() (+3 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.10
Nodes (13): RegistrarPagoForm, aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), pago_exitoso() (+5 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.26
Nodes (13): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+5 more)

### Community 3 - "vender_promocion"
Cohesion: 0.20
Nodes (5): consumir_saldo(), vender_promocion(), BasePromociones, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.04
Nodes (22): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+14 more)

### Community 5 - "logistica/views.py"
Cohesion: 0.11
Nodes (15): AgregarParadaForm, envases_retirados_en_hoja(), resumen_recorrido(), agregar_parada(), agregar_pedido_parada(), _cargas_confirmacion_desde_post(), confirmar_entrega(), confirmar_ruta() (+7 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "venta_calle"
Cohesion: 0.17
Nodes (8): _etiqueta_direccion_cliente(), botellon_por_defecto(), envase_de_reparto(), productos_de_reparto(), _parse_fecha(), planificar_reparto(), _productos_para_carga(), venta_calle()

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.23
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.07
Nodes (14): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+6 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.15
Nodes (16): MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+8 more)

### Community 11 - "Empleado"
Cohesion: 0.16
Nodes (7): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado, Meta, PantallasDeRolesTests

### Community 12 - "logistica/services.py"
Cohesion: 0.08
Nodes (22): 5A — Historial de envases (RF-08) · ~4 h, Punto de partida real, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), confirmar_entrega_en_calle() (+14 more)

### Community 14 - "productos/views.py"
Cohesion: 0.05
Nodes (24): requiere(), decorador(), envuelta(), CategoriaAdmin, ProductoAdmin, CategoriaForm, Meta, ProductoForm (+16 more)

### Community 15 - "Producto"
Cohesion: 0.09
Nodes (9): obtener_o_crear_cuenta(), DetallePedido, Meta, MetodoPago, Meta, metodo_pago_efectivo(), stock_comprometido(), Producto (+1 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (14): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose (+6 more)

### Community 17 - "Carrito"
Cohesion: 0.15
Nodes (11): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito() (+3 more)

### Community 19 - "PedidoEspontaneoTests"
Cohesion: 0.13
Nodes (4): confirmar_hoja(), registrar_regreso(), ConfirmacionRegresoTests, PedidoEspontaneoTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.20
Nodes (9): crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_zona(), eliminar_camion(), eliminar_zona(), listar_camiones(), listar_rutas() (+1 more)

### Community 22 - "Cliente"
Cohesion: 0.11
Nodes (4): Cliente, Meta, HistorialBidonesTests, vender_promocion()

### Community 23 - "logistica/admin.py"
Cohesion: 0.24
Nodes (3): fecha_es_de_reparto(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "ClienteForm"
Cohesion: 0.18
Nodes (4): ClienteForm, Meta, ClienteSinCuentaForm, _ValidarDatosPersonalesMixin

### Community 25 - "EntregaCalleTests"
Cohesion: 0.15
Nodes (4): EntregaCalleTests, _a_decimal(), registrar_cobro(), registrar_pago_manual()

### Community 26 - "Promocion"
Cohesion: 0.14
Nodes (7): PromocionForm, Meta, Promocion, Meta, crear_promocion(), editar_promocion(), _form_promocion()

### Community 28 - "django_db_models_deletion"
Cohesion: 0.07
Nodes (16): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+8 more)

### Community 29 - "SuscripcionReposicion"
Cohesion: 0.10
Nodes (9): fecha_estimada_para_direccion(), CheckoutForm, _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), SuscripcionForm, Meta, SuscripcionReposicion, Meta (+1 more)

### Community 31 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 32 - "puede"
Cohesion: 0.11
Nodes (9): es_admin(), es_repartidor_asignado(), obtener_empleado(), puede(), puede_alguna(), puede_operar_hoja(), puede_ver_hoja(), usa_panel() (+1 more)

### Community 33 - "listar_clientes"
Cohesion: 0.12
Nodes (10): AltaClienteConCuentaForm, Meta, BuscarClienteForm, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos(), listar_clientes() (+2 more)

### Community 34 - "django_apps"
Cohesion: 0.05
Nodes (13): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, CuentasConfig, EmpleadosConfig, LogisticaConfig (+5 more)

### Community 36 - "base_tienda.html"
Cohesion: 0.22
Nodes (5): listar_pedidos(), mis_pedidos(), listar_productos(), ver_producto(), inicio()

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.24
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, cerrar_sesion() (+1 more)

### Community 38 - "PerfilUsuarioForm"
Cohesion: 0.18
Nodes (3): PerfilUsuarioForm, Meta, validar_nombre()

### Community 39 - "distribuidora/views.py"
Cohesion: 0.16
Nodes (8): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, resumen_caja(), promociones_por_vencer(), listar_promociones(), resumen_dashboard()

### Community 40 - "Command"
Cohesion: 0.05
Nodes (13): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests (+5 more)

### Community 41 - "DireccionEntrega"
Cohesion: 0.13
Nodes (6): DireccionEntrega, Meta, AgregarDireccionTests, carga_sugerida(), GeneracionBorradorTests, CheckoutFechaEstimadaTests

### Community 43 - "SuscripcionReposicion"
Cohesion: 0.09
Nodes (17): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 5B — Promociones prepago (RF-09) · ~6 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, 6C — Pedido automático quincenal (RF-18) · ~4 h (+9 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "ver_ruta"
Cohesion: 0.19
Nodes (8): Hallazgos nuevos, clientes_frecuentes_de_zona(), pedidos_candidatos(), editar_ruta(), eliminar_parada(), _ids_de_paradas_con_nota(), imprimir_ruta(), ver_ruta()

### Community 47 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 48 - "CompraPromocion"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 49 - "mi_ruta_hoy"
Cohesion: 0.18
Nodes (6): botellones_por_producto(), entregados_por_producto(), inventario_camion(), _ficha_de_parada(), _link_mapa(), mi_ruta_hoy()

### Community 50 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.15
Nodes (8): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, Pedido, Meta

### Community 51 - "confirmar_pedido"
Cohesion: 0.25
Nodes (4): checkout(), _cliente_puede_comprar(), confirmar_pedido(), saldo_vigente()

### Community 52 - "Command"
Cohesion: 0.07
Nodes (15): AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests (+7 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "PerfilPersonalTests"
Cohesion: 0.08
Nodes (4): PerfilPersonalTests, RecuperarContrasenaTests, RegistroTelefonosTests, SesionTests

### Community 55 - "VariasDireccionesTests"
Cohesion: 0.07
Nodes (6): BuscarClientesTests, EditarMiPerfilTests, FiadoPremiumYExcepcionTests, ValidacionesClienteTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.07
Nodes (7): firma_webhook_valida(), CheckoutRequiereTelefonosTests, CobroManualTests, _firmar(), PagosParcialesTests, PagosSegurosTests, TransicionesManualesTests

### Community 62 - "clientes/forms.py"
Cohesion: 0.08
Nodes (12): DireccionEntregaForm, Meta, EditarMiPerfilForm, ValidadoresTests, aplicar_attrs(), normalizar_patente(), solo_digitos(), validar_altura() (+4 more)

### Community 63 - "clientes/services.py"
Cohesion: 0.05
Nodes (20): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, MovimientoBidon, Meta (+12 more)

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.20
Nodes (3): RolEmpleadoForm, Meta, sincronizar_grupo_empleado()

### Community 67 - "puede_ver_nota_seguridad"
Cohesion: 0.06
Nodes (8): puede_ver_nota_seguridad(), AccesoAVistasLogisticasTests, FuncionesPorRolTests, GruposBaseTests, NotaDeSeguridadTests, Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 68 - "Usuario"
Cohesion: 0.16
Nodes (5): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoForm, Meta, RolSincronizaGrupoTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.18
Nodes (5): asignar(), Migration, _permisos(), Funcion, Meta

### Community 72 - "TelefonoContacto"
Cohesion: 0.22
Nodes (5): 4. ♻️ Redundancias, TelefonoContactoForm, Meta, TelefonoContacto, Meta

### Community 73 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 74 - "popups.js"
Cohesion: 0.26
Nodes (15): actualizarTope(), avisar(), cerrarAviso(), confirmar(), contenedorAvisos(), erroresDelServidor(), escapar(), etiquetaDe() (+7 more)

### Community 75 - "QA-02 Pago mayor a la deuda"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-02 Pago mayor a la deuda, Qué pasa

### Community 76 - "autenticacion/migrations/0001_initial.py"
Cohesion: 0.25
Nodes (3): Migration, Migration, Migration

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 98 - "RecorridoRepartidorTests"
Cohesion: 0.10
Nodes (4): HojaRutaCapacidadTests, PlanificarRepartoViewTests, RecorridoRepartidorTests, SeedDemoTests

### Community 99 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "pedidos/admin.py"
Cohesion: 0.36
Nodes (6): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.15
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.17
Nodes (8): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "generar_borradores_periodo"
Cohesion: 0.13
Nodes (5): Command, HojaRuta, Meta, generar_borradores_periodo(), GeneracionQuincenalTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 109 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.25
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aquadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 110 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 114 - "actualizar_estado_entrega"
Cohesion: 0.29
Nodes (3): ActualizarEstadoForm, Meta, actualizar_estado_entrega()

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa

### Community 120 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa

### Community 121 - "permisos/views.py"
Cohesion: 0.17
Nodes (3): buscar_productos(), csrf_failure(), RF-07 · Buscador tolerante a tildes

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 123 - "CalendarioExcepcion"
Cohesion: 0.40
Nodes (3): CalendarioExcepcion, Meta, _hay_excepcion()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 127 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "Camion"
Cohesion: 0.18
Nodes (6): CamionForm, Meta, HojaRutaForm, Meta, Camion, Meta

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.14
Nodes (11): Notas, permisos, Relaciones, Notas, planta, Reglas, Relaciones, Dónde está en el código (+3 more)

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 139 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 143 - "abonos"
Cohesion: 0.67
Nodes (3): abonos, Notas, Relaciones

### Community 145 - "autenticacion"
Cohesion: 0.67
Nodes (3): autenticacion, Notas, Relaciones

### Community 146 - "{{title}}"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, Qué pasa, {{title}}

### Community 147 - "{{date}}"
Cohesion: 0.40
Nodes (4): Bloqueos / dudas, {{date}}, Pendiente, Qué hice

### Community 149 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 151 - "logistica/tests.py"
Cohesion: 0.07
Nodes (19): BarrioForm, Meta, RutaRepartoForm, Meta, ZonaForm, Meta, Command, Barrio (+11 more)

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 153 - "clientes"
Cohesion: 0.67
Nodes (3): clientes, Notas, Relaciones

### Community 154 - "cuentas"
Cohesion: 0.67
Nodes (3): cuentas, Notas, Relaciones

### Community 157 - "empleados"
Cohesion: 0.67
Nodes (3): empleados, Notas, Relaciones

### Community 158 - "logistica"
Cohesion: 0.67
Nodes (3): logistica, Notas, Relaciones

### Community 159 - "pedidos"
Cohesion: 0.67
Nodes (3): Notas, pedidos, Relaciones

### Community 160 - "productos"
Cohesion: 0.67
Nodes (3): Notas, productos, Relaciones

### Community 161 - "promociones"
Cohesion: 0.67
Nodes (3): Notas, promociones, Relaciones

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 864 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **56 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/views.py`, `vender_promocion`, `logistica/views.py`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `Producto`, `PROCEDURE.md`, `PedidoEspontaneoTests`, `logistica/tests.py`, `ClienteForm`, `EntregaCalleTests`, `SuscripcionReposicion`, `CuentaCorriente`, `listar_clientes`, `distribuidora/views.py`, `Command`, `DireccionEntrega`, `HojaDeRutaUXTests`, `ver_ruta`, `6A — Pagos parciales (RF-13) · ~4 h`, `confirmar_pedido`, `Command`, `VariasDireccionesTests`, `PagosSegurosTests`, `clientes/forms.py`, `clientes/services.py`, `puede_ver_nota_seguridad`, `RecorridoRepartidorTests`, `✅ Control de cumplimiento de requisitos — 20/10/2026`, `generar_borradores_periodo`, `Fase 4 · Cuentas corrientes y abonos`, `Fase 5 · Bidones y promociones prepago`, `CuentaDeRepartidorTests`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 63 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `django_contrib` be split into smaller, more focused modules?**
  _Cohesion score 0.10837438423645321 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `pedidos/views.py`, `vender_promocion`, `QA-01 Validaciones solo en formularios`, `venta_calle`, `PedidoAutomaticoTests`, `planta/views.py`, `logistica/services.py`, `productos/views.py`, `Carrito`, `CarritoSoloPorPostTests`, `PedidoEspontaneoTests`, `logistica/tests.py`, `EntregaCalleTests`, `Promocion`, `SuscripcionReposicion`, `base_tienda.html`, `distribuidora/views.py`, `Command`, `DireccionEntrega`, `HojaDeRutaUXTests`, `mi_ruta_hoy`, `confirmar_pedido`, `Command`, `PagosSegurosTests`, `RecorridoRepartidorTests`, `permisos/views.py`, `StockComprometidoTests`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0960960960960961 - nodes in this community are weakly interconnected._