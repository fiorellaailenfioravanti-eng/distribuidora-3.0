# Graph Report - vault-envases-generator-668120  (2026-11-16)

## Corpus Check
- 299 files · ~344,208 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2421 nodes · 5619 edges · 185 communities (113 shown, 72 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 795 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bd5bb487`
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
- SuscripcionReposicion
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- limites.py
- requiere
- PROCEDURE.md
- Carrito
- base_tienda.html
- logistica/tests.py
- What You Must Do When Invoked
- Zona
- Pedido
- django_contrib
- Command
- pedidos/views.py
- pedidos/services.py
- permisos/views.py
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- Command
- aplicar_pago_mercadopago
- puede
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- AccesoAVistasLogisticasTests
- StockComprometidoTests
- Empleado
- distribuidora/views.py
- CuentaCorriente
- GenerarEnvaseTests
- HojaDeRutaUXTests
- Verificar cambios — Distribuidora 3.0
- Migración: unificar empleados
- CompraPromocion
- CheckoutConSaldoTests
- PerfilUsuarioForm
- logistica/admin.py
- aplicar_attrs
- vencer_promociones
- SemaforizacionTests
- abonos/views.py
- graphify reference: extra exports and benchmark
- confirmar_pedido
- FuncionesPorRolTests
- PagosSegurosTests
- AltaClienteValidacionesTests
- clientes/forms.py
- clientes/services.py
- base.py
- Usuario
- AbonoForm
- empleados/tests.py
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- DireccionEntregaForm
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
- GruposBaseTests
- QA-04 Abono con costo 0
- BuscarClientesTests
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- EnlaceGoogleMapsTests
- QA-05 Zona sin días de reparto
- Fase 6 · Pagos parciales y pedido automático
- puede_ver_nota_seguridad
- Categoria
- 0013_detallehojaruta_es_venta_calle.py
- Verificar cambios — Distribuidora 3.0
- QA-06 Email de producción sin configurar
- ModeloEmpleadoUnicoTests
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- registrar_movimiento_bidon
- CLAUDE.md
- 0002_bidones_recargables_y_rol_recargador.py
- VistaMovimientoBidonTests
- QA campo a campo — 12/11/2026
- promociones/views.py
- clientes/forms.py
- clientes/views.py
- RegistrarPagoForm
- con_stock_disponible
- QA-01 Validaciones solo en formularios
- logistica/views.py
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- 0007_marcar_botellones.py
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- EliminarProductoTests
- {{title}}
- ActualizarEstadoForm
- cambios_sin_guardar.js
- abonos
- Cliente
- autenticacion
- {{title}}
- {{date}}
- generar_borradores_periodo
- carrito
- 0004_asignar_grupo_permisos.py
- Fase 5 · Bidones y promociones prepago
- buscador
- clientes
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- 0003_grupos_base.py
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- TelefonoContacto
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- FiadoPremiumYExcepcionTests
- 0006_corregir_ayuda_desc_seguridad.py
- VariasDireccionesTests
- NumeroClienteTests
- Notas
- ZonaQuerySet
- H-10 · Suite de tests parcial (faltan carrito y buscador)
- TestCase
- PedidoEspontaneoTests
- PromocionForm
- Abono
- EditarMiPerfilTests
- OrdenDirectorioClientesTests
- 0015_numero_cliente.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 113 edges
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

## Communities (185 total, 72 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.11
Nodes (12): CodigoRecuperacionForm, IngresarUsuarioForm, NuevaContrasenaForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), perfil_usuario(), recuperar_codigo() (+4 more)

### Community 1 - "django_conf"
Cohesion: 0.05
Nodes (20): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+12 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.16
Nodes (17): Empleado, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+9 more)

### Community 3 - "promociones/tests.py"
Cohesion: 0.17
Nodes (6): consumir_saldo(), saldo_vigente(), vender_promocion(), BasePromociones, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.02
Nodes (36): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+28 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.07
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.11
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.05
Nodes (21): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, 6C — Pedido automático quincenal (RF-18) · ~4 h, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 7 — QA, producción y tesis 🎓 (+13 more)

### Community 9 - "planta/views.py"
Cohesion: 0.07
Nodes (14): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+6 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.15
Nodes (16): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion(), eliminar_telefono() (+8 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.10
Nodes (12): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+4 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.06
Nodes (25): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellones_por_producto(), confirmar_entrega_en_calle() (+17 more)

### Community 13 - "limites.py"
Cohesion: 0.14
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "requiere"
Cohesion: 0.15
Nodes (13): requiere(), decorador(), envuelta(), crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria() (+5 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (14): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose (+6 more)

### Community 17 - "Carrito"
Cohesion: 0.17
Nodes (10): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito() (+2 more)

### Community 18 - "base_tienda.html"
Cohesion: 0.16
Nodes (7): buscar_productos(), agotados_al_final(), listar_productos(), ver_producto(), inicio(), Inicio de la tienda (rehecho), RF-07 · Buscador tolerante a tildes

### Community 19 - "logistica/tests.py"
Cohesion: 0.06
Nodes (27): DireccionEntrega, Meta, BarrioForm, Meta, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta, Barrio (+19 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "Zona"
Cohesion: 0.13
Nodes (9): ZonaForm, Meta, Zona, Meta, ZonaDiasRepartoTests, ZonaFormTests, direcciones_sin_zona(), editar_zona() (+1 more)

### Community 22 - "Pedido"
Cohesion: 0.11
Nodes (13): 2. 🟠 Altos — errores funcionales, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 5D — Tests · ~2 h, 6A — Pagos parciales (RF-13) · ~4 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)** (+5 more)

### Community 23 - "django_contrib"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 25 - "pedidos/views.py"
Cohesion: 0.11
Nodes (13): CheckoutForm, pago_en_curso(), cambiar_estado_pago(), checkout(), _cliente_puede_comprar(), confirmar_pago_qr(), detalle_pedido(), listar_pedidos() (+5 more)

### Community 26 - "pedidos/services.py"
Cohesion: 0.09
Nodes (12): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, obtener_o_crear_cuenta(), registrar_cargo(), ReglaFiadoTests (+4 more)

### Community 28 - "permisos/views.py"
Cohesion: 0.14
Nodes (7): ingresar_usuario(), registrar_usuario(), _ya_ingresado(), guardar_telefonos(), es_personal_interno(), csrf_failure(), destino_personal()

### Community 29 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.33
Nodes (6): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas

### Community 31 - "aplicar_pago_mercadopago"
Cohesion: 0.18
Nodes (6): 1. 🔴 Críticos — seguridad y dinero, aplicar_pago_mercadopago(), consultar_pago_mercadopago(), firma_webhook_valida(), pago_exitoso(), webhook_mercadopago()

### Community 32 - "puede"
Cohesion: 0.12
Nodes (4): roles_usuario(), puede(), usa_panel(), EvaluacionDeRolesTests

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.17
Nodes (5): AltaClienteConCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.22
Nodes (3): construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 37 - "StockComprometidoTests"
Cohesion: 0.25
Nodes (3): stock_comprometido(), stock_disponible(), StockComprometidoTests

### Community 38 - "Empleado"
Cohesion: 0.15
Nodes (5): EmpleadoAdmin, RolEmpleadoAdmin, RolEmpleado, Meta, CuentaDeRepartidorTests

### Community 39 - "distribuidora/views.py"
Cohesion: 0.21
Nodes (7): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, resumen_caja(), promociones_por_vencer(), resumen_dashboard()

### Community 40 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 41 - "GenerarEnvaseTests"
Cohesion: 0.11
Nodes (11): GenerarEnvaseTests, 2026-11-16, Baja lógica desde los listados de empleados y clientes, Bloqueos / dudas, Configuración, Envases asociados (nuevo), Ficha del cliente más simple, Pendiente (+3 more)

### Community 43 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.33
Nodes (5): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "CompraPromocion"
Cohesion: 0.16
Nodes (7): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, CompraPromocion, Meta, ConsumoPromocion, Meta

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.14
Nodes (5): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, validar_nombre()

### Community 48 - "logistica/admin.py"
Cohesion: 0.27
Nodes (9): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+1 more)

### Community 49 - "aplicar_attrs"
Cohesion: 0.18
Nodes (3): DireccionRegistroForm, Meta, aplicar_attrs()

### Community 50 - "vencer_promociones"
Cohesion: 0.29
Nodes (3): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, Command, vencer_promociones()

### Community 51 - "SemaforizacionTests"
Cohesion: 0.10
Nodes (4): registrar_pago(), CuentaCorrienteModelTests, SemaforizacionTests, VistasCuentasTests

### Community 52 - "abonos/views.py"
Cohesion: 0.27
Nodes (8): AbonoForm, Meta, cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono()

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "confirmar_pedido"
Cohesion: 0.29
Nodes (5): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, confirmar_pedido()

### Community 56 - "PagosSegurosTests"
Cohesion: 0.05
Nodes (8): metodos_pago_checkout_web(), CheckoutRequiereTelefonosTests, CobroManualTests, _firmar(), PagosParcialesTests, PagosSegurosTests, StockReservadoTests, TransicionesManualesTests

### Community 62 - "clientes/forms.py"
Cohesion: 0.09
Nodes (8): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_telefono()

### Community 63 - "clientes/services.py"
Cohesion: 0.05
Nodes (20): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, MovimientoBidon, Meta (+12 more)

### Community 66 - "Usuario"
Cohesion: 0.13
Nodes (6): Usuario, Meta, EmpleadoForm, Meta, RolSincronizaGrupoTests, sincronizar_grupo_empleado()

### Community 68 - "empleados/tests.py"
Cohesion: 0.07
Nodes (6): RolEmpleadoForm, Meta, BajaLogicaRolTests, BajaLogicaYFotoEmpleadoTests, GuardsUnificadosTests, PantallasDeRolesTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.40
Nodes (3): asignar(), Migration, _permisos()

### Community 71 - "DireccionEntregaForm"
Cohesion: 0.25
Nodes (3): DireccionEntregaForm, Meta, FichaDomiciliosTests

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 73 - "HojaRuta"
Cohesion: 0.26
Nodes (3): HojaRuta, Meta, restaurar_ruta()

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
Cohesion: 0.06
Nodes (10): HojaRutaForm, Meta, BajaLogicaCamionTests, BajaLogicaZonaTests, EliminarBorradorRutaTests, HojaRutaCapacidadTests, HojaRutaZonaYLimitesTests, HojaSinChoferTests (+2 more)

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.21
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.33
Nodes (5): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 108 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 110 - "Categoria"
Cohesion: 0.10
Nodes (13): CategoriaAdmin, ProductoAdmin, bidones_retornables(), CategoriaForm, Meta, EnvaseForm, Categoria, Meta (+5 more)

### Community 114 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.33
Nodes (5): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 118 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 121 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "promociones/views.py"
Cohesion: 0.19
Nodes (8): VenderPromocionForm, Promocion, Meta, crear_promocion(), editar_promocion(), _form_promocion(), listar_promociones(), vender_promocion()

### Community 126 - "clientes/forms.py"
Cohesion: 0.13
Nodes (7): ClienteForm, Meta, ClienteSinCuentaForm, EditarMiPerfilForm, _ValidarDatosPersonalesMixin, ValidacionesClienteTests, validar_fecha_no_futura()

### Community 127 - "clientes/views.py"
Cohesion: 0.16
Nodes (8): BuscarClienteForm, _columnas_ordenables(), _contexto_suscripcion(), listar_clientes(), _texto_buscable(), SuscripcionForm, Meta, normalizar_texto()

### Community 129 - "con_stock_disponible"
Cohesion: 0.50
Nodes (3): con_stock_disponible(), stock_reservado_por_producto(), Notas

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "logistica/views.py"
Cohesion: 0.05
Nodes (48): Hallazgos nuevos, AgregarParadaForm, CamionForm, Meta, botellon_por_defecto(), clientes_frecuentes_de_zona(), envase_de_reparto(), pedidos_candidatos() (+40 more)

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 136 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.09
Nodes (18): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA, Notas (+10 more)

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
Cohesion: 0.13
Nodes (3): Command, Command, generar_borradores_periodo()

### Community 149 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 151 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

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
Cohesion: 0.18
Nodes (6): 4. ♻️ Redundancias, TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente()

### Community 182 - "PedidoEspontaneoTests"
Cohesion: 0.08
Nodes (7): confirmar_hoja(), envases_retirados_en_hoja(), registrar_regreso(), resumen_recorrido(), ConfirmacionRegresoTests, PedidoEspontaneoTests, RecorridoRepartidorTests

### Community 185 - "Abono"
Cohesion: 0.08
Nodes (7): AbonoAdmin, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests, VistasAbonosTests

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1048 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **72 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `promociones/tests.py`, `logistica/views.py`, `cuentas/views.py`, `SuscripcionReposicion`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `PROCEDURE.md`, `logistica/tests.py`, `Pedido`, `Fase 5 · Bidones y promociones prepago`, `pedidos/views.py`, `pedidos/services.py`, `Command`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `Empleado`, `TelefonoContacto`, `CuentaCorriente`, `FiadoPremiumYExcepcionTests`, `HojaDeRutaUXTests`, `distribuidora/views.py`, `NumeroClienteTests`, `TestCase`, `SemaforizacionTests`, `abonos/views.py`, `PedidoEspontaneoTests`, `confirmar_pedido`, `PagosSegurosTests`, `Abono`, `AltaClienteValidacionesTests`, `OrdenDirectorioClientesTests`, `clientes/services.py`, `AbonoForm`, `DireccionEntregaForm`, `logistica/tests.py`, `BuscarClientesTests`, `EnlaceGoogleMapsTests`, `puede_ver_nota_seguridad`, `Fase 4 · Cuentas corrientes y abonos`, `registrar_movimiento_bidon`, `VistaMovimientoBidonTests`, `promociones/views.py`, `clientes/forms.py`, `clientes/views.py`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Are the 72 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 72 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10574712643678161 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Categoria` to `con_stock_disponible`, `promociones/tests.py`, `QA-01 Validaciones solo en formularios`, `logistica/views.py`, `ProductoForm`, `SuscripcionReposicion`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `requiere`, `Carrito`, `base_tienda.html`, `logistica/tests.py`, `Pedido`, `pedidos/views.py`, `pedidos/services.py`, `Command`, `GeneracionBorradorTests`, `StockComprometidoTests`, `Empleado`, `distribuidora/views.py`, `GenerarEnvaseTests`, `HojaDeRutaUXTests`, `abonos/views.py`, `PedidoEspontaneoTests`, `confirmar_pedido`, `PagosSegurosTests`, `Abono`, `PromocionForm`, `CarritoSoloPorPostTests`, `promociones/views.py`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 62 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_conf` be split into smaller, more focused modules?**
  _Cohesion score 0.05353535353535353 - nodes in this community are weakly interconnected._