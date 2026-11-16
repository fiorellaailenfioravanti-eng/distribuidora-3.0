# Graph Report - distribuidora-3.0  (2026-11-16)

## Corpus Check
- 299 files · ~344,147 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 27 file(s) not represented in the graph (top: (none) 6, .canvas 5, .base 5)

## Summary
- 2416 nodes · 5610 edges · 187 communities (108 shown, 79 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 792 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bd5bb487`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- base_tienda.html
- empleados/views.py
- promociones/tests.py
- django_db
- configuracion/views.py
- CuentaCorriente
- ProductoForm
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- vencer_promociones
- requiere
- Producto
- PROCEDURE.md
- Carrito
- base_tienda.html
- Barrio
- What You Must Do When Invoked
- base_dashboard.html
- clientes/services.py
- Pedido
- SuscripcionReposicion
- pedidos/views.py
- seed_demo.py
- RecargaTests
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- Command
- Camion
- puede
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- AccesoAVistasLogisticasTests
- StockComprometidoTests
- Empleado
- MetodoPago
- TestCase
- Qué hice
- HojaDeRutaUXTests
- es_personal_interno
- Migración: unificar empleados
- promociones/admin.py
- Migración: métodos de pago
- PerfilUsuarioForm
- logistica/admin.py
- aplicar_attrs
- confirmar_pedido
- DireccionEntrega
- Abono
- graphify reference: extra exports and benchmark
- RolSincronizaGrupoTests
- FuncionesPorRolTests
- django_contrib
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleadoForm
- ingresar_usuario
- RolEmpleado
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- RecorridoRepartidorTests
- Qué hice
- HojaRuta
- popups.js
- QA-02 Pago mayor a la deuda
- RecuperarContrasenaTests
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- Zona
- BuscarClientesTests
- QA-04 Abono con costo 0
- PagosSegurosTests
- RegistroUsuarioForm
- RolBackend
- ZonaForm
- FASE3_LOGISTICA.md
- CargaHojaRuta
- QA-05 Zona sin días de reparto
- PlanificarRepartoViewTests
- puede_ver_nota_seguridad
- EnvaseForm
- 0013_detallehojaruta_es_venta_calle.py
- 🌊 Distribuidora 3.0 / Aguadelluvia
- QA-06 Email de producción sin configurar
- CuentaDeRepartidorTests
- RF-05 · Clientes Normal/Premium; fiado solo Premium
- CarritoSoloPorPostTests
- VistasPromocionesTests
- Fase 6 · Pagos parciales y pedido automático
- 0002_bidones_recargables_y_rol_recargador.py
- 0011_renumerar_paradas.py
- QA campo a campo — 12/11/2026
- promociones/tests.py
- clientes/forms.py
- 0007_marcar_botellones.py
- EliminarBorradorRutaTests
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- logistica/views.py
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- os
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- EliminarProductoTests
- {{title}}
- DetalleHojaRuta
- cambios_sin_guardar.js
- abonos
- Cliente
- autenticacion
- {{title}}
- {{date}}
- GeneracionQuincenalTests
- carrito
- 0004_asignar_grupo_permisos.py
- HojaSinChoferTests
- buscador
- clientes
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- Fase 5 · Bidones y promociones prepago
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- AltaClienteValidacionesTests
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- 0003_grupos_base.py
- 0006_corregir_ayuda_desc_seguridad.py
- VariasDireccionesTests
- Command
- HojaRutaZonaYLimitesTests
- Notas
- 0010_saldo_inicial_bidones.py
- ZonaQuerySet
- clientes/tests.py
- 0006_metodo_cuenta_corriente.py
- envuelta
- PedidoEspontaneoTests
- PromocionForm
- Usuario
- OrdenDirectorioClientesTests
- 0015_numero_cliente.py
- 0012_completar_pedidos_de_paradas.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 112 edges
2. `puede()` - 102 edges
3. `Producto` - 89 edges
4. `Pedido` - 79 edges
5. `Zona` - 62 edges
6. `DireccionEntrega` - 59 edges
7. `HojaRuta` - 55 edges
8. `MetodoPago` - 48 edges
9. `Empleado` - 45 edges
10. `DetalleHojaRuta` - 40 edges

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

## Communities (187 total, 79 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.12
Nodes (11): CodigoRecuperacionForm, IngresarUsuarioForm, NuevaContrasenaForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), recuperar_codigo(), recuperar_contrasena() (+3 more)

### Community 1 - "base_tienda.html"
Cohesion: 0.13
Nodes (9): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr() (+1 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.22
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "promociones/tests.py"
Cohesion: 0.17
Nodes (6): consumir_saldo(), vender_promocion(), BasePromociones, CheckoutConSaldoTests, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.02
Nodes (60): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+52 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.07
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 6 - "CuentaCorriente"
Cohesion: 0.05
Nodes (23): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original), CuentaCorrienteAdmin (+15 more)

### Community 7 - "ProductoForm"
Cohesion: 0.08
Nodes (6): ProductoForm, Meta, AltaProductoTests, CategoriasPanelTests, GenerarEnvaseTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.23
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.09
Nodes (12): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), recarga_de() (+4 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.12
Nodes (21): DireccionEntregaForm, Meta, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion() (+13 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.09
Nodes (12): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+4 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.05
Nodes (32): 5A — Historial de envases (RF-08) · ~4 h, Command, CalendarioExcepcion, Meta, RutaReparto, Meta, agregar_parada(), agregar_pedido_a_hoja() (+24 more)

### Community 13 - "vencer_promociones"
Cohesion: 0.10
Nodes (14): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)** (+6 more)

### Community 14 - "requiere"
Cohesion: 0.14
Nodes (17): requiere(), CategoriaForm, Meta, Categoria, Meta, crear_categoria(), crear_producto(), editar_categoria() (+9 more)

### Community 15 - "Producto"
Cohesion: 0.10
Nodes (8): CategoriaAdmin, ProductoAdmin, Producto, Meta, VigentesQuerySet, CatalogoAgotadosAlFinalTests, InicioTests, H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.12
Nodes (18): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías (+10 more)

### Community 17 - "Carrito"
Cohesion: 0.15
Nodes (11): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito() (+3 more)

### Community 18 - "base_tienda.html"
Cohesion: 0.09
Nodes (11): buscar_productos(), clientes_morosos(), resumen_morosidad(), con_stock_disponible(), stock_reservado_por_producto(), agotados_al_final(), listar_productos(), ver_producto() (+3 more)

### Community 19 - "Barrio"
Cohesion: 0.15
Nodes (11): AgregarParadaForm, BarrioForm, Meta, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta, Barrio, Meta (+3 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.14
Nodes (15): Hallazgos nuevos, agregar_parada(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona(), eliminar_camion() (+7 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.23
Nodes (6): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 23 - "Pedido"
Cohesion: 0.15
Nodes (5): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta

### Community 24 - "SuscripcionReposicion"
Cohesion: 0.14
Nodes (9): 4. ❓ Decisiones a tomar antes de empezar, 5B — Promociones prepago (RF-09) · ~6 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, SuscripcionReposicion, Meta, CompraPromocion, Meta, promociones_por_vencer() (+1 more)

### Community 25 - "pedidos/views.py"
Cohesion: 0.12
Nodes (9): CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_exitoso(), registrar_pago() (+1 more)

### Community 26 - "seed_demo.py"
Cohesion: 0.07
Nodes (14): Migration, MovimientoCuenta, Meta, obtener_o_crear_cuenta(), registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, ReglaFiadoTests (+6 more)

### Community 29 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.22
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, pago_en_curso() (+1 more)

### Community 31 - "Camion"
Cohesion: 0.15
Nodes (8): CamionForm, Meta, HojaRutaForm, Meta, Camion, Meta, BajaLogicaCamionTests, restaurar_camion()

### Community 32 - "puede"
Cohesion: 0.09
Nodes (10): restaurar_zona(), es_repartidor_asignado(), obtener_empleado(), puede(), puede_alguna(), puede_operar_hoja(), puede_ver_hoja(), usa_panel() (+2 more)

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.11
Nodes (11): 4. ♻️ Redundancias, AltaClienteConCuentaForm, Meta, guardar_telefonos(), _columnas_ordenables(), crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta() (+3 more)

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 38 - "Empleado"
Cohesion: 0.18
Nodes (5): 2. 🟠 Altos — errores funcionales, EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta

### Community 39 - "MetodoPago"
Cohesion: 0.08
Nodes (16): EntregaCalleTests, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido (+8 more)

### Community 40 - "TestCase"
Cohesion: 0.13
Nodes (4): BajaLogicaZonaTests, ConfirmacionRegresoTests, HojaRutaCapacidadTests, SeedDemoTests

### Community 41 - "Qué hice"
Cohesion: 0.20
Nodes (10): 2026-11-16, Baja lógica desde los listados de empleados y clientes, Bloqueos / dudas, Configuración, Envases asociados (nuevo), Inicio de la tienda (rehecho), Pendiente, Qué hice (+2 more)

### Community 43 - "es_personal_interno"
Cohesion: 0.11
Nodes (13): perfil_usuario(), roles_usuario(), es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0 (+5 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "promociones/admin.py"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.14
Nodes (5): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, validar_nombre()

### Community 48 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 49 - "aplicar_attrs"
Cohesion: 0.20
Nodes (3): DireccionRegistroForm, Meta, aplicar_attrs()

### Community 50 - "confirmar_pedido"
Cohesion: 0.20
Nodes (7): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, checkout(), _cliente_puede_comprar(), confirmar_pedido()

### Community 51 - "DireccionEntrega"
Cohesion: 0.18
Nodes (3): DireccionEntrega, Meta, EnlaceGoogleMapsTests

### Community 52 - "Abono"
Cohesion: 0.05
Nodes (17): AbonoAdmin, AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests (+9 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 57 - "clientes/admin.py"
Cohesion: 0.13
Nodes (9): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, TelefonoContacto, Meta (+1 more)

### Community 62 - "clientes/forms.py"
Cohesion: 0.09
Nodes (8): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_telefono()

### Community 63 - "permisos/signals.py"
Cohesion: 0.12
Nodes (8): perfil_cliente_esta_vacio(), retirar_perfil_cliente_vacio(), sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.20
Nodes (3): RolEmpleadoForm, Meta, BajaLogicaRolTests

### Community 67 - "ingresar_usuario"
Cohesion: 0.36
Nodes (4): ingresar_usuario(), registrar_usuario(), _ya_ingresado(), destino_personal()

### Community 68 - "RolEmpleado"
Cohesion: 0.09
Nodes (5): RolEmpleado, Meta, BajaLogicaYFotoEmpleadoTests, GuardsUnificadosTests, PantallasDeRolesTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.18
Nodes (5): asignar(), Migration, _permisos(), Funcion, Meta

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 73 - "HojaRuta"
Cohesion: 0.21
Nodes (4): HojaRuta, Meta, eliminar_ruta(), restaurar_ruta()

### Community 74 - "popups.js"
Cohesion: 0.26
Nodes (15): actualizarTope(), avisar(), cerrarAviso(), confirmar(), contenedorAvisos(), erroresDelServidor(), escapar(), etiquetaDe() (+7 more)

### Community 75 - "QA-02 Pago mayor a la deuda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-02 Pago mayor a la deuda, Qué pasa

### Community 76 - "RecuperarContrasenaTests"
Cohesion: 0.07
Nodes (4): PerfilPersonalTests, RecuperarContrasenaTests, RegistroTelefonosTests, SesionTests

### Community 77 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 78 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 79 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 98 - "Zona"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "PagosSegurosTests"
Cohesion: 0.05
Nodes (9): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, CobroManualTests, PagosParcialesTests, PagosSegurosTests, StockReservadoTests (+1 more)

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.17
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "ZonaForm"
Cohesion: 0.43
Nodes (3): ZonaForm, Meta, ZonaFormTests

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "CargaHojaRuta"
Cohesion: 0.29
Nodes (4): CargaHojaRuta, Meta, Carga y regreso del camión (sobrantes a stock), SinHojaEliminadaManager

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 109 - "puede_ver_nota_seguridad"
Cohesion: 0.14
Nodes (6): _ids_de_paradas_con_nota(), puede_ver_nota_seguridad(), NotaDeSeguridadTests, Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 114 - "🌊 Distribuidora 3.0 / Aguadelluvia"
Cohesion: 0.29
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 121 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "promociones/tests.py"
Cohesion: 0.14
Nodes (8): VenderPromocionForm, Promocion, Meta, saldo_vigente(), crear_promocion(), editar_promocion(), _form_promocion(), vender_promocion()

### Community 126 - "clientes/forms.py"
Cohesion: 0.09
Nodes (8): BuscarClienteForm, ClienteSinCuentaForm, EditarMiPerfilForm, MovimientoBidonForm, TelefonoContactoForm, Meta, _ValidarDatosPersonalesMixin, validar_fecha_no_futura()

### Community 127 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "logistica/views.py"
Cohesion: 0.08
Nodes (25): botellones_por_producto(), clientes_frecuentes_de_zona(), entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja(), inventario_camion(), registrar_regreso(), resumen_recorrido() (+17 more)

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
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 141 - "DetalleHojaRuta"
Cohesion: 0.14
Nodes (5): ActualizarEstadoForm, Meta, DetalleHojaRuta, Meta, actualizar_estado_entrega()

### Community 142 - "cambios_sin_guardar.js"
Cohesion: 0.60
Nodes (3): campoCambio(), hayCambios(), seGuardaSolo()

### Community 143 - "abonos"
Cohesion: 0.67
Nodes (3): abonos, Notas, Relaciones

### Community 144 - "Cliente"
Cohesion: 0.11
Nodes (5): Detalle, _bloquear_cuenta(), Cliente, Meta, siguiente_numero_cliente()

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

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 153 - "clientes"
Cohesion: 0.40
Nodes (3): clientes, Notas, Relaciones

### Community 154 - "cuentas"
Cohesion: 0.67
Nodes (3): cuentas, Notas, Relaciones

### Community 155 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa, Resolución

### Community 157 - "empleados"
Cohesion: 0.67
Nodes (3): empleados, Notas, Relaciones

### Community 158 - "logistica"
Cohesion: 0.67
Nodes (3): logistica, Notas, Relaciones

### Community 159 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 160 - "productos"
Cohesion: 0.67
Nodes (3): Notas, productos, Relaciones

### Community 161 - "promociones"
Cohesion: 0.67
Nodes (3): Notas, promociones, Relaciones

### Community 164 - "Validaciones por campo"
Cohesion: 0.67
Nodes (3): Límites de caracteres (base de datos), Teléfonos en las altas, Validaciones por campo

### Community 165 - "tabla_ordenable.js"
Cohesion: 0.83
Nodes (3): iconoPara(), prepararTabla(), valorCelda()

### Community 177 - "clientes/tests.py"
Cohesion: 0.06
Nodes (10): ClienteForm, Meta, AgregarDireccionTests, BajaLogicaTelefonoDireccionTests, EditarMiPerfilTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests, NumeroClienteTests (+2 more)

### Community 189 - "Usuario"
Cohesion: 0.16
Nodes (5): Migration, Usuario, Meta, EmpleadoForm, Meta

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1044 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **79 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `base_tienda.html`, `promociones/tests.py`, `logistica/views.py`, `CuentaCorriente`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `PROCEDURE.md`, `base_tienda.html`, `GeneracionQuincenalTests`, `base_dashboard.html`, `clientes/services.py`, `Pedido`, `SuscripcionReposicion`, `pedidos/views.py`, `seed_demo.py`, `Command`, `Fase 5 · Bidones y promociones prepago`, `puede`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `AltaClienteValidacionesTests`, `TestCase`, `MetodoPago`, `HojaDeRutaUXTests`, `clientes/tests.py`, `confirmar_pedido`, `DireccionEntrega`, `Abono`, `PedidoEspontaneoTests`, `clientes/admin.py`, `OrdenDirectorioClientesTests`, `permisos/signals.py`, `RecorridoRepartidorTests`, `BuscarClientesTests`, `PagosSegurosTests`, `PlanificarRepartoViewTests`, `puede_ver_nota_seguridad`, `CuentaDeRepartidorTests`, `RF-05 · Clientes Normal/Premium; fiado solo Premium`, `promociones/tests.py`, `clientes/forms.py`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Are the 71 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 71 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11965811965811966 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `promociones/tests.py`, `QA-01 Validaciones solo en formularios`, `logistica/views.py`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `vencer_promociones`, `requiere`, `Carrito`, `base_tienda.html`, `Barrio`, `SuscripcionReposicion`, `pedidos/views.py`, `seed_demo.py`, `RecargaTests`, `Command`, `GeneracionBorradorTests`, `StockComprometidoTests`, `MetodoPago`, `TestCase`, `HojaDeRutaUXTests`, `confirmar_pedido`, `Abono`, `PedidoEspontaneoTests`, `PromocionForm`, `RecorridoRepartidorTests`, `PagosSegurosTests`, `EnvaseForm`, `CarritoSoloPorPostTests`, `promociones/tests.py`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 62 INFERRED edges - model-reasoned connections that need verification._
- **Should `base_tienda.html` be split into smaller, more focused modules?**
  _Cohesion score 0.12535612535612536 - nodes in this community are weakly interconnected._