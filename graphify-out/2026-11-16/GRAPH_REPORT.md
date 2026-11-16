# Graph Report - obsidian-vault-reinicio-2295d7  (2026-11-16)

## Corpus Check
- 296 files · ~339,592 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2309 nodes · 5394 edges · 182 communities (106 shown, 76 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 772 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ae016515`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- base_tienda.html
- empleados/views.py
- vender_promocion
- django_db
- configuracion/views.py
- cuentas/views.py
- ProductoForm
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- logistica/views.py
- logistica/services.py
- limites.py
- clientes/tests.py
- Producto
- PROCEDURE.md
- Carrito
- productos/views.py
- DireccionEntrega
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- django_contrib
- DetalleHojaRuta
- Pedido
- vencer_promociones
- Command
- RolEmpleado
- listar_productos
- registrar_cargo
- EvaluacionDeRolesTests
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- logistica/models.py
- buscador/views.py
- Usuario
- distribuidora/views.py
- CuentaCorriente
- TelefonoContacto
- HojaDeRutaUXTests
- es_personal_interno
- Migración: unificar empleados
- promociones/views.py
- Migración: métodos de pago
- PerfilUsuarioForm
- CompraPromocion
- ConfiguracionCorreoTests
- registrar_cobro
- Empleado
- Abono
- graphify reference: extra exports and benchmark
- SesionTests
- AltaClienteValidacionesTests
- PagosSegurosTests
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleadoForm
- puede_ver_nota_seguridad
- Usuario
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- GuardsUnificadosTests
- Qué hice
- HojaRuta
- popups.js
- QA-02 Pago mayor a la deuda
- RegistroTelefonosTests
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- logistica/tests.py
- CheckoutConSaldoTests
- QA-04 Abono con costo 0
- pedidos/tests.py
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- MovimientoCuenta
- QA-05 Zona sin días de reparto
- AbonoForm
- clientes/signals.py
- BajaLogicaYFotoEmpleadoTests
- 0013_detallehojaruta_es_venta_calle.py
- VistasCuentasTests
- QA-06 Email de producción sin configurar
- ModeloEmpleadoUnicoTests
- RF-05 · Clientes Normal/Premium; fiado solo Premium
- RecuperarContrasenaForm
- QA-09 Recuperar contraseña usa vistas de clase
- permisos/views.py
- 0002_bidones_recargables_y_rol_recargador.py
- 🌊 Distribuidora 3.0 / Aguadelluvia
- QA campo a campo — 12/11/2026
- TestCase
- Categoria
- 0007_marcar_botellones.py
- 0006_corregir_ayuda_desc_seguridad.py
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- Barrio
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- os
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- EliminarProductoTests
- {{title}}
- PromocionForm
- cambios_sin_guardar.js
- abonos
- Detalle
- autenticacion
- {{title}}
- {{date}}
- generar_borradores_periodo
- carrito
- 0004_asignar_grupo_permisos.py
- Zona
- buscador
- clientes
- cuentas
- ver_cliente
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- pedidos
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- autenticacion/tests.py
- PerfilPersonalTests
- BuscarClientesTests
- EditarMiPerfilTests
- VariasDireccionesTests
- OrdenDirectorioClientesTests
- HistorialBidonesTests
- VistaMovimientoBidonTests
- InicioTests
- 0003_grupos_base.py
- BajaLogicaTelefonoDireccionTests
- VigentesQuerySet

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 110 edges
2. `puede()` - 102 edges
3. `Producto` - 85 edges
4. `Pedido` - 79 edges
5. `Zona` - 62 edges
6. `DireccionEntrega` - 57 edges
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

## Communities (182 total, 76 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.13
Nodes (10): 3. 🟡 Medios, IngresarUsuarioForm, NuevaContrasenaForm, RegistroClienteWebForm, Meta, cerrar_sesion(), ingresar_usuario(), registrar_usuario() (+2 more)

### Community 1 - "base_tienda.html"
Cohesion: 0.21
Nodes (4): mi_perfil_cliente(), detalle_pedido(), listar_pedidos(), mis_pedidos()

### Community 2 - "empleados/views.py"
Cohesion: 0.24
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "vender_promocion"
Cohesion: 0.17
Nodes (6): consumir_saldo(), revertir_consumos(), vender_promocion(), BasePromociones, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.02
Nodes (53): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+45 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.10
Nodes (9): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, configuracion(), probar_correo(), es_admin() (+1 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.07
Nodes (14): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+6 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.15
Nodes (18): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _columnas_ordenables(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion() (+10 more)

### Community 11 - "logistica/views.py"
Cohesion: 0.07
Nodes (25): carga_sugerida(), confirmar_entrega_en_calle(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), agregar_parada(), agregar_pedido_parada(), _cargas_confirmacion_desde_post() (+17 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.09
Nodes (21): 5A — Historial de envases (RF-08) · ~4 h, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellones_por_producto(), confirmar_hoja(), crear_hoja_borrador(), crear_venta_calle() (+13 more)

### Community 13 - "limites.py"
Cohesion: 0.14
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "clientes/tests.py"
Cohesion: 0.38
Nodes (3): ClienteForm, Meta, ValidacionesClienteTests

### Community 15 - "Producto"
Cohesion: 0.10
Nodes (7): obtener_o_crear_cuenta(), MetodoPago, Meta, Producto, Meta, limite_largo(), H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.11
Nodes (25): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba (+17 more)

### Community 17 - "Carrito"
Cohesion: 0.11
Nodes (11): carrito_total(), Carrito, ItemCarrito, Meta, CarritoSoloPorPostTests, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito() (+3 more)

### Community 18 - "productos/views.py"
Cohesion: 0.17
Nodes (12): requiere(), decorador(), envuelta(), crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria() (+4 more)

### Community 19 - "DireccionEntrega"
Cohesion: 0.10
Nodes (6): DireccionEntrega, Meta, resumen_recorrido(), PedidoEspontaneoTests, RecorridoRepartidorTests, RF-03 · Multidirección de entrega

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.09
Nodes (22): Hallazgos nuevos, ZonaForm, Meta, ZonaFormTests, actualizar_estado_entrega(), crear_ruta(), direcciones_sin_zona(), editar_camion() (+14 more)

### Community 22 - "Cliente"
Cohesion: 0.09
Nodes (10): Cliente, Meta, MovimientoBidon, Meta, _cliente_de_parada(), perfil_cliente_esta_vacio(), recalcular_saldo_bidones(), registrar_movimiento_bidon() (+2 more)

### Community 23 - "django_contrib"
Cohesion: 0.05
Nodes (24): AbonoAdmin, ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, BarrioAdmin (+16 more)

### Community 24 - "DetalleHojaRuta"
Cohesion: 0.10
Nodes (6): ActualizarEstadoForm, Meta, DetalleHojaRuta, Meta, EntregaCalleTests, restaurar_ruta()

### Community 25 - "Pedido"
Cohesion: 0.07
Nodes (23): 1. 🔴 Críticos — seguridad y dinero, fecha_estimada_para_direccion(), pedidos_pendientes(), CheckoutForm, RegistrarPagoForm, Pedido, Meta, aplicar_pago_mercadopago() (+15 more)

### Community 26 - "vencer_promociones"
Cohesion: 0.12
Nodes (13): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)** (+5 more)

### Community 29 - "RolEmpleado"
Cohesion: 0.17
Nodes (5): 7. 🗺️ Cómo entra en el plan, Decisiones nuevas, RolEmpleado, Meta, CuentaDeRepartidorTests

### Community 30 - "listar_productos"
Cohesion: 0.21
Nodes (5): eliminar_producto(), _filtrar_por_categoria(), listar_productos(), ver_producto(), inicio()

### Community 31 - "registrar_cargo"
Cohesion: 0.14
Nodes (4): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, SemaforizacionTests

### Community 32 - "EvaluacionDeRolesTests"
Cohesion: 0.12
Nodes (8): eliminar_cliente(), puede(), usa_panel(), EvaluacionDeRolesTests, Dónde está en el código, Funciones y roles por defecto, Reglas que no dependen de las casillas, Roles y permisos

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.14
Nodes (7): AltaClienteConCuentaForm, Meta, guardar_telefonos(), leer_telefonos(), crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.21
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 36 - "logistica/models.py"
Cohesion: 0.07
Nodes (12): Camion, Meta, CargaHojaRuta, Meta, RutaReparto, Meta, ZonaQuerySet, restaurar_camion() (+4 more)

### Community 37 - "buscador/views.py"
Cohesion: 0.24
Nodes (4): buscar_productos(), con_stock_disponible(), agotados_al_final(), RF-07 · Buscador tolerante a tildes

### Community 38 - "Usuario"
Cohesion: 0.14
Nodes (9): 2. 🟠 Altos — errores funcionales, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 🔎 Auditoría de coherencia — Distribuidora 3.0, Usuario, Meta, EmpleadoForm, Meta (+1 more)

### Community 39 - "distribuidora/views.py"
Cohesion: 0.27
Nodes (3): clientes_morosos(), resumen_morosidad(), resumen_dashboard()

### Community 40 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 41 - "TelefonoContacto"
Cohesion: 0.40
Nodes (3): 4. ♻️ Redundancias, TelefonoContacto, Meta

### Community 43 - "es_personal_interno"
Cohesion: 0.14
Nodes (12): roles_usuario(), es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0, 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo) (+4 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "promociones/views.py"
Cohesion: 0.12
Nodes (9): CompraPromocion, Meta, Promocion, Meta, promociones_por_vencer(), crear_promocion(), editar_promocion(), _form_promocion() (+1 more)

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.17
Nodes (3): PerfilUsuarioForm, Meta, perfil_usuario()

### Community 48 - "CompraPromocion"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 50 - "registrar_cobro"
Cohesion: 0.16
Nodes (7): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 6A — Pagos parciales (RF-13) · ~4 h, Punto de partida real, _a_decimal(), metodo_pago_efectivo(), registrar_cobro(), registrar_pago_manual()

### Community 51 - "Empleado"
Cohesion: 0.20
Nodes (4): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta

### Community 52 - "Abono"
Cohesion: 0.07
Nodes (15): AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests (+7 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 56 - "PagosSegurosTests"
Cohesion: 0.05
Nodes (9): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, CobroManualTests, PagosParcialesTests, PagosSegurosTests, StockReservadoTests (+1 more)

### Community 62 - "clientes/forms.py"
Cohesion: 0.05
Nodes (18): BuscarClienteForm, ClienteSinCuentaForm, DireccionEntregaForm, Meta, DireccionRegistroForm, Meta, EditarMiPerfilForm, TelefonoContactoForm (+10 more)

### Community 63 - "permisos/signals.py"
Cohesion: 0.22
Nodes (5): sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.18
Nodes (3): RolEmpleadoForm, Meta, BajaLogicaRolTests

### Community 67 - "puede_ver_nota_seguridad"
Cohesion: 0.07
Nodes (7): puede_ver_nota_seguridad(), FuncionesPorRolTests, GruposBaseTests, NotaDeSeguridadTests, Distribuidora 3.0 / Aguadelluvia, graphify, graphify

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
Cohesion: 0.26
Nodes (3): HojaRuta, Meta, eliminar_ruta()

### Community 74 - "popups.js"
Cohesion: 0.26
Nodes (15): actualizarTope(), avisar(), cerrarAviso(), confirmar(), contenedorAvisos(), erroresDelServidor(), escapar(), etiquetaDe() (+7 more)

### Community 75 - "QA-02 Pago mayor a la deuda"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-02 Pago mayor a la deuda, Qué pasa

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
Cohesion: 0.06
Nodes (12): HojaRutaForm, Meta, BajaLogicaCamionTests, BajaLogicaZonaTests, ConfirmacionRegresoTests, EliminarBorradorRutaTests, GeneracionQuincenalTests, HojaRutaCapacidadTests (+4 more)

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "pedidos/tests.py"
Cohesion: 0.07
Nodes (25): 4. ❓ Decisiones a tomar antes de empezar, 5B — Promociones prepago (RF-09) · ~6 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, DetallePedidoInline, MetodoPagoAdmin (+17 more)

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.21
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.20
Nodes (7): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (6): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 106 - "MovimientoCuenta"
Cohesion: 0.16
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 119 - "RecuperarContrasenaForm"
Cohesion: 0.22
Nodes (4): RecuperarContrasenaForm, configuracion, Correo de recuperación de contraseña, Notas

### Community 120 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 123 - "🌊 Distribuidora 3.0 / Aguadelluvia"
Cohesion: 0.22
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 126 - "Categoria"
Cohesion: 0.29
Nodes (4): CategoriaForm, Meta, Categoria, Meta

### Community 127 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "Barrio"
Cohesion: 0.13
Nodes (13): AgregarParadaForm, BarrioForm, Meta, CamionForm, Meta, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta (+5 more)

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.20
Nodes (7): Notas, permisos, Relaciones, Notas, planta, Reglas, Relaciones

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 142 - "cambios_sin_guardar.js"
Cohesion: 0.60
Nodes (3): campoCambio(), hayCambios(), seGuardaSolo()

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

### Community 148 - "generar_borradores_periodo"
Cohesion: 0.18
Nodes (3): Command, generar_borradores_periodo(), pedidos_candidatos()

### Community 149 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 151 - "Zona"
Cohesion: 0.14
Nodes (5): Command, Zona, Meta, ZonaDiasRepartoTests, restaurar_zona()

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 153 - "clientes"
Cohesion: 0.67
Nodes (3): clientes, Notas, Relaciones

### Community 154 - "cuentas"
Cohesion: 0.67
Nodes (3): cuentas, Notas, Relaciones

### Community 155 - "ver_cliente"
Cohesion: 0.11
Nodes (9): MovimientoBidonForm, _contexto_suscripcion(), ver_cliente(), SuscripcionForm, Meta, suscripcion_cliente(), VenderPromocionForm, compras_vigentes() (+1 more)

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

### Community 164 - "Validaciones por campo"
Cohesion: 0.67
Nodes (3): Límites de caracteres (base de datos), Teléfonos en las altas, Validaciones por campo

### Community 165 - "tabla_ordenable.js"
Cohesion: 0.83
Nodes (3): iconoPara(), prepararTabla(), valorCelda()

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 995 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **76 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `base_tienda.html`, `vender_promocion`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/views.py`, `logistica/services.py`, `clientes/tests.py`, `Producto`, `Detalle`, `PROCEDURE.md`, `DireccionEntrega`, `django_contrib`, `DetalleHojaRuta`, `Pedido`, `ver_cliente`, `Command`, `RolEmpleado`, `registrar_cargo`, `EvaluacionDeRolesTests`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `logistica/models.py`, `distribuidora/views.py`, `CuentaCorriente`, `BuscarClientesTests`, `HojaDeRutaUXTests`, `OrdenDirectorioClientesTests`, `HistorialBidonesTests`, `VistaMovimientoBidonTests`, `promociones/views.py`, `BajaLogicaTelefonoDireccionTests`, `Abono`, `AltaClienteValidacionesTests`, `PagosSegurosTests`, `clientes/forms.py`, `puede_ver_nota_seguridad`, `logistica/tests.py`, `pedidos/tests.py`, `FASE3_LOGISTICA.md`, `MovimientoCuenta`, `AbonoForm`, `clientes/signals.py`, `VistasCuentasTests`, `RF-05 · Clientes Normal/Premium; fiado solo Premium`, `TestCase`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Are the 69 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 69 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `vender_promocion`, `QA-01 Validaciones solo en formularios`, `Barrio`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `logistica/views.py`, `logistica/services.py`, `EliminarProductoTests`, `PromocionForm`, `Carrito`, `productos/views.py`, `DireccionEntrega`, `django_contrib`, `DetalleHojaRuta`, `Pedido`, `vencer_promociones`, `Command`, `listar_productos`, `GeneracionBorradorTests`, `buscador/views.py`, `distribuidora/views.py`, `HojaDeRutaUXTests`, `InicioTests`, `Abono`, `PagosSegurosTests`, `logistica/tests.py`, `pedidos/tests.py`, `Categoria`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Are the 58 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 58 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_db` be split into smaller, more focused modules?**
  _Cohesion score 0.020448179271708684 - nodes in this community are weakly interconnected._