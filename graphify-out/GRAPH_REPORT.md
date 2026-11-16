# Graph Report - distribuidora-3.0  (2026-11-16)

## Corpus Check
- 299 files · ~343,500 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 27 file(s) not represented in the graph (top: (none) 6, .canvas 5, .base 5)

## Summary
- 2402 nodes · 5589 edges · 202 communities (120 shown, 82 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 789 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `71c9e4f1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- django_conf
- empleados/views.py
- promociones/tests.py
- django_db
- configuracion/views.py
- cuentas/views.py
- ProductoForm
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- limites.py
- requiere
- seed_demo.py
- PROCEDURE.md
- Carrito
- productos/views.py
- Barrio
- What You Must Do When Invoked
- base_dashboard.html
- clientes/services.py
- django_contrib
- MetodoPago
- pedidos/views.py
- vencer_promociones
- RecargaTests
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- Command
- registrar_cargo
- puede
- listar_clientes
- django_apps
- GeneracionBorradorTests
- AccesoAVistasLogisticasTests
- pedidos/services.py
- Empleado
- distribuidora/views.py
- CuentaCorriente
- GenerarEnvaseTests
- HojaDeRutaUXTests
- es_personal_interno
- Migración: unificar empleados
- Promocion
- Migración: métodos de pago
- PerfilUsuarioForm
- logistica/admin.py
- aplicar_attrs
- Pedido
- SemaforizacionTests
- Abono
- graphify reference: extra exports and benchmark
- SuscripcionReposicion
- AltaClienteValidacionesTests
- StockReservadoTests
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleadoForm
- RolEmpleado
- Usuario
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- SuscripcionReposicion
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
- logistica/tests.py
- DireccionEntrega
- QA-04 Abono con costo 0
- PagosSegurosTests
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- MovimientoCuenta
- QA-05 Zona sin días de reparto
- BajaLogicaYFotoEmpleadoTests
- puede_ver_nota_seguridad
- Producto
- 0013_detallehojaruta_es_venta_calle.py
- VistasCuentasTests
- QA-06 Email de producción sin configurar
- ModeloEmpleadoUnicoTests
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- pedidos/views.py
- permisos/views.py
- 0002_bidones_recargables_y_rol_recargador.py
- registrar_entrega
- QA campo a campo — 12/11/2026
- vender_promocion
- clientes/forms.py
- 0007_marcar_botellones.py
- pedidos/admin.py
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
- generar_borradores_periodo
- carrito
- 0004_asignar_grupo_permisos.py
- Zona
- buscador
- clientes
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- ver_ruta
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- TelefonoContacto
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- BuscarClientesTests
- 0006_corregir_ayuda_desc_seguridad.py
- VariasDireccionesTests
- Categoria
- CheckoutConSaldoTests
- Notas
- InicioTests
- 0003_grupos_base.py
- TestCase
- envuelta
- VigentesQuerySet
- registrar_regreso_ruta
- PedidoEspontaneoTests
- base_tienda.html
- PromocionForm
- django_contrib
- EditarMiPerfilTests
- CobroManualTests
- DetalleRecarga
- autenticacion/migrations/0001_initial.py
- OrdenDirectorioClientesTests
- HistorialBidonesTests
- VistaMovimientoBidonTests
- 0015_numero_cliente.py
- BajaLogicaTelefonoDireccionTests
- _ficha_de_parada
- abonos/migrations/0001_initial.py
- 0012_completar_pedidos_de_paradas.py
- ZonaQuerySet
- 0006_metodo_cuenta_corriente.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 111 edges
2. `puede()` - 102 edges
3. `Producto` - 89 edges
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
- `Carga y regreso del camión (sobrantes a stock)` --references--> `CargaHojaRuta`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `5D — Tests · ~2 h` --references--> `registrar_entrega()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/logistica/services.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (202 total, 82 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.09
Nodes (16): CodigoRecuperacionForm, IngresarUsuarioForm, NuevaContrasenaForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo() (+8 more)

### Community 1 - "django_conf"
Cohesion: 0.07
Nodes (17): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+9 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.24
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "promociones/tests.py"
Cohesion: 0.14
Nodes (8): metodo_pago_efectivo(), consumir_saldo(), revertir_consumos(), saldo_vigente(), vender_promocion(), BasePromociones, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (30): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+22 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.07
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.23
Nodes (8): CargoCuentaForm, PagoCuentaForm, _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta(), validar_fecha_no_pasada()

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.15
Nodes (8): RecargaBidones, Meta, bidones_recargables(), recarga_de(), resumen_stock(), _leer_cantidades(), recarga_diaria(), stock_bidones()

### Community 10 - "clientes/views.py"
Cohesion: 0.14
Nodes (19): DireccionEntregaForm, Meta, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+11 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.09
Nodes (12): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+4 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.10
Nodes (16): _etiqueta_direccion_cliente(), agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellon_por_defecto(), confirmar_hoja(), crear_hoja_borrador(), crear_venta_calle() (+8 more)

### Community 13 - "limites.py"
Cohesion: 0.13
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "requiere"
Cohesion: 0.17
Nodes (11): requiere(), crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria(), eliminar_producto(), _filtrar_por_categoria() (+3 more)

### Community 15 - "seed_demo.py"
Cohesion: 0.12
Nodes (3): SinEliminadosManager, limite_largo(), H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.10
Nodes (24): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar (+16 more)

### Community 17 - "Carrito"
Cohesion: 0.15
Nodes (11): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito() (+3 more)

### Community 18 - "productos/views.py"
Cohesion: 0.15
Nodes (6): buscar_productos(), con_stock_disponible(), stock_reservado_por_producto(), agotados_al_final(), ver_producto(), Notas

### Community 19 - "Barrio"
Cohesion: 0.14
Nodes (6): AgregarParadaForm, BarrioForm, Meta, Barrio, Meta, PlanificarRepartoViewTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.13
Nodes (16): actualizar_estado_entrega(), agregar_parada(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona(), eliminar_camion() (+8 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.23
Nodes (6): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 23 - "django_contrib"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "MetodoPago"
Cohesion: 0.13
Nodes (8): EntregaCalleTests, _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), DetallePedido, Meta, MetodoPago, Meta, CheckoutFechaEstimadaTests

### Community 25 - "pedidos/views.py"
Cohesion: 0.09
Nodes (15): RegistrarPagoForm, aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos() (+7 more)

### Community 26 - "vencer_promociones"
Cohesion: 0.12
Nodes (13): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)** (+5 more)

### Community 29 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.24
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas (+1 more)

### Community 31 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 32 - "puede"
Cohesion: 0.12
Nodes (8): cuenta_de_cliente(), puede(), usa_panel(), EvaluacionDeRolesTests, Dónde está en el código, Funciones y roles por defecto, Reglas que no dependen de las casillas, Roles y permisos

### Community 33 - "listar_clientes"
Cohesion: 0.13
Nodes (9): AltaClienteConCuentaForm, Meta, _columnas_ordenables(), crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), listar_clientes(), _texto_buscable() (+1 more)

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.15
Nodes (5): carga_sugerida(), clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 36 - "AccesoAVistasLogisticasTests"
Cohesion: 0.10
Nodes (6): RutaRepartoForm, Meta, RutaReparto, Meta, HojaSinChoferTests, AccesoAVistasLogisticasTests

### Community 37 - "pedidos/services.py"
Cohesion: 0.18
Nodes (5): obtener_o_crear_cuenta(), _a_decimal(), registrar_cobro(), registrar_pago_manual(), stock_comprometido()

### Community 38 - "Empleado"
Cohesion: 0.12
Nodes (5): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, CuentaDeRepartidorTests

### Community 39 - "distribuidora/views.py"
Cohesion: 0.17
Nodes (6): clientes_morosos(), PagoPedido, Meta, resumen_caja(), promociones_por_vencer(), resumen_dashboard()

### Community 40 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 41 - "GenerarEnvaseTests"
Cohesion: 0.14
Nodes (6): GenerarEnvaseTests, Configuración, Envases asociados (nuevo), Inicio de la tienda (rehecho), Qué hice, Recuperar contraseña con código temporal

### Community 43 - "es_personal_interno"
Cohesion: 0.11
Nodes (13): perfil_usuario(), roles_usuario(), es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0 (+5 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "Promocion"
Cohesion: 0.14
Nodes (8): 5B — Promociones prepago (RF-09) · ~6 h, CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta, Promocion, Meta

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.14
Nodes (5): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, validar_nombre()

### Community 48 - "logistica/admin.py"
Cohesion: 0.16
Nodes (12): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+4 more)

### Community 49 - "aplicar_attrs"
Cohesion: 0.13
Nodes (5): DireccionRegistroForm, Meta, CamionForm, Meta, aplicar_attrs()

### Community 50 - "Pedido"
Cohesion: 0.15
Nodes (5): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta

### Community 52 - "Abono"
Cohesion: 0.06
Nodes (16): AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests (+8 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "SuscripcionReposicion"
Cohesion: 0.15
Nodes (7): 4. ❓ Decisiones a tomar antes de empezar, 6C — Pedido automático quincenal (RF-18) · ~4 h, perfil_cliente_esta_vacio(), SuscripcionReposicion, Meta, CompraPromocion, Meta

### Community 56 - "StockReservadoTests"
Cohesion: 0.08
Nodes (5): CheckoutRequiereTelefonosTests, PagosParcialesTests, StockComprometidoTests, StockReservadoTests, TransicionesManualesTests

### Community 57 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 62 - "clientes/forms.py"
Cohesion: 0.10
Nodes (8): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_telefono()

### Community 63 - "permisos/signals.py"
Cohesion: 0.14
Nodes (6): retirar_perfil_cliente_vacio(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.15
Nodes (4): RolEmpleadoForm, Meta, BajaLogicaRolTests, sincronizar_grupo_empleado()

### Community 67 - "RolEmpleado"
Cohesion: 0.18
Nodes (7): 2. 🟠 Altos — errores funcionales, Usuario, Meta, EmpleadoForm, Meta, RolEmpleado, Meta

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.18
Nodes (5): asignar(), Migration, _permisos(), Funcion, Meta

### Community 71 - "SuscripcionReposicion"
Cohesion: 0.25
Nodes (4): _contexto_suscripcion(), SuscripcionForm, Meta, suscripcion_cliente()

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 74 - "popups.js"
Cohesion: 0.26
Nodes (15): actualizarTope(), avisar(), cerrarAviso(), confirmar(), contenedorAvisos(), erroresDelServidor(), escapar(), etiquetaDe() (+7 more)

### Community 75 - "QA-02 Pago mayor a la deuda"
Cohesion: 0.40
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

### Community 98 - "logistica/tests.py"
Cohesion: 0.08
Nodes (15): HojaRutaForm, Meta, ZonaForm, Meta, Camion, Meta, BajaLogicaCamionTests, BajaLogicaZonaTests (+7 more)

### Community 99 - "DireccionEntrega"
Cohesion: 0.12
Nodes (4): DireccionEntrega, Meta, AgregarDireccionTests, RecorridoRepartidorTests

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "PagosSegurosTests"
Cohesion: 0.19
Nodes (3): firma_webhook_valida(), _firmar(), PagosSegurosTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.21
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (7): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.18
Nodes (7): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Carga y regreso del camión (sobrantes a stock), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 106 - "MovimientoCuenta"
Cohesion: 0.16
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 108 - "BajaLogicaYFotoEmpleadoTests"
Cohesion: 0.11
Nodes (3): BajaLogicaYFotoEmpleadoTests, GuardsUnificadosTests, PantallasDeRolesTests

### Community 109 - "puede_ver_nota_seguridad"
Cohesion: 0.07
Nodes (7): puede_ver_nota_seguridad(), FuncionesPorRolTests, GruposBaseTests, NotaDeSeguridadTests, Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 110 - "Producto"
Cohesion: 0.19
Nodes (5): bidones_retornables(), EnvaseForm, Producto, Meta, envases()

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.21
Nodes (8): 2026-11-16, Bloqueos / dudas, Pendiente, Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 118 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 120 - "pedidos/views.py"
Cohesion: 0.19
Nodes (8): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, CheckoutForm, checkout(), _cliente_puede_comprar(), confirmar_pedido()

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 123 - "registrar_entrega"
Cohesion: 0.14
Nodes (6): 5A — Historial de envases (RF-08) · ~4 h, botellones_por_producto(), entregados_por_producto(), inventario_camion(), _producto_envase_para(), registrar_entrega()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "vender_promocion"
Cohesion: 0.31
Nodes (6): VenderPromocionForm, crear_promocion(), editar_promocion(), _form_promocion(), listar_promociones(), vender_promocion()

### Community 126 - "clientes/forms.py"
Cohesion: 0.10
Nodes (9): BuscarClienteForm, ClienteForm, Meta, ClienteSinCuentaForm, EditarMiPerfilForm, MovimientoBidonForm, _ValidarDatosPersonalesMixin, ValidacionesClienteTests (+1 more)

### Community 127 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 128 - "pedidos/admin.py"
Cohesion: 0.36
Nodes (6): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "logistica/views.py"
Cohesion: 0.09
Nodes (20): confirmar_entrega_en_calle(), productos_de_reparto(), agregar_pedido_parada(), _cargas_confirmacion_desde_post(), confirmar_entrega(), confirmar_ruta(), eliminar_ruta(), _int_o_none() (+12 more)

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.11
Nodes (14): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA, Notas (+6 more)

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 141 - "DetalleHojaRuta"
Cohesion: 0.14
Nodes (5): ActualizarEstadoForm, Meta, DetalleHojaRuta, Meta, restaurar_ruta()

### Community 142 - "cambios_sin_guardar.js"
Cohesion: 0.60
Nodes (3): campoCambio(), hayCambios(), seGuardaSolo()

### Community 143 - "abonos"
Cohesion: 0.67
Nodes (3): abonos, Notas, Relaciones

### Community 144 - "Cliente"
Cohesion: 0.10
Nodes (6): Detalle, _bloquear_cuenta(), Cliente, Meta, siguiente_numero_cliente(), eliminar_cliente()

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
Cohesion: 0.15
Nodes (3): Command, generar_borradores_periodo(), GeneracionQuincenalTests

### Community 149 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 151 - "Zona"
Cohesion: 0.15
Nodes (4): Command, Zona, Meta, ZonaDiasRepartoTests

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 153 - "clientes"
Cohesion: 0.67
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

### Community 159 - "ver_ruta"
Cohesion: 0.22
Nodes (7): Hallazgos nuevos, pedidos_candidatos(), _ids_de_paradas_con_nota(), imprimir_ruta(), ver_ruta(), puede_alguna(), puede_ver_hoja()

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

### Community 167 - "TelefonoContacto"
Cohesion: 0.17
Nodes (5): TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente()

### Community 172 - "Categoria"
Cohesion: 0.18
Nodes (7): CategoriaAdmin, ProductoAdmin, CategoriaForm, Meta, Categoria, Meta, listar_categorias()

### Community 181 - "registrar_regreso_ruta"
Cohesion: 0.28
Nodes (5): envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), resumen_recorrido(), registrar_regreso_ruta()

### Community 188 - "DetalleRecarga"
Cohesion: 0.33
Nodes (4): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1033 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **82 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `promociones/tests.py`, `logistica/views.py`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `seed_demo.py`, `PROCEDURE.md`, `Barrio`, `generar_borradores_periodo`, `base_dashboard.html`, `clientes/services.py`, `MetodoPago`, `pedidos/views.py`, `Command`, `registrar_cargo`, `puede`, `listar_clientes`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `Empleado`, `TelefonoContacto`, `CuentaCorriente`, `BuscarClientesTests`, `HojaDeRutaUXTests`, `distribuidora/views.py`, `TestCase`, `Pedido`, `SemaforizacionTests`, `Abono`, `PedidoEspontaneoTests`, `AltaClienteValidacionesTests`, `SuscripcionReposicion`, `clientes/admin.py`, `CobroManualTests`, `OrdenDirectorioClientesTests`, `HistorialBidonesTests`, `VistaMovimientoBidonTests`, `permisos/signals.py`, `BajaLogicaTelefonoDireccionTests`, `SuscripcionReposicion`, `logistica/tests.py`, `DireccionEntrega`, `FASE3_LOGISTICA.md`, `MovimientoCuenta`, `puede_ver_nota_seguridad`, `VistasCuentasTests`, `Fase 4 · Cuentas corrientes y abonos`, `pedidos/views.py`, `vender_promocion`, `clientes/forms.py`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 70 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09309309309309309 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `promociones/tests.py`, `QA-01 Validaciones solo en formularios`, `logistica/views.py`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `requiere`, `seed_demo.py`, `Carrito`, `productos/views.py`, `MetodoPago`, `pedidos/views.py`, `vencer_promociones`, `RecargaTests`, `Command`, `GeneracionBorradorTests`, `pedidos/services.py`, `distribuidora/views.py`, `GenerarEnvaseTests`, `HojaDeRutaUXTests`, `Categoria`, `InicioTests`, `Abono`, `registrar_regreso_ruta`, `PedidoEspontaneoTests`, `SuscripcionReposicion`, `StockReservadoTests`, `base_tienda.html`, `PromocionForm`, `logistica/tests.py`, `DireccionEntrega`, `CarritoSoloPorPostTests`, `pedidos/views.py`, `registrar_entrega`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 62 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_conf` be split into smaller, more focused modules?**
  _Cohesion score 0.06825396825396825 - nodes in this community are weakly interconnected._