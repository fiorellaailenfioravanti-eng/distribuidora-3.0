# Graph Report - inicio-proyecto-087608  (2026-11-21)

## Corpus Check
- 305 files · ~346,515 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2472 nodes · 5717 edges · 177 communities (108 shown, 69 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 806 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9fc0e36e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- pedidos/urls.py
- empleados/views.py
- Command
- django_db
- distribuidora/views.py
- cuentas/views.py
- ProductoForm
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- seed_demo.py
- requiere
- VigentesQuerySet
- PROCEDURE.md
- Carrito
- base_tienda.html
- recortar_textos
- What You Must Do When Invoked
- base_dashboard.html
- clientes/services.py
- Pedido
- SemaforizacionTests
- Producto
- pedidos/services.py
- CuentaCorriente
- 🏁 Plan de Cierre — Fases 4.5 a 7
- importar_w3w.py
- MovimientoCuenta
- puede
- registrar_cargo
- django_apps
- GeneracionBorradorTests
- AccesoAVistasLogisticasTests
- logistica/views.py
- Empleado
- BajaLogicaYFotoEmpleadoTests
- GenerarEnvaseTests
- Qué hice
- HojaDeRutaUXTests
- es_personal_interno
- Migración: unificar empleados
- ModeloEmpleadoUnicoTests
- django_conf
- PerfilUsuarioForm
- logistica/admin.py
- aplicar_attrs
- ConfiguracionCorreo
- PagosSegurosTests
- Abono
- graphify reference: extra exports and benchmark
- RolSincronizaGrupoTests
- FuncionesPorRolTests
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- DireccionEntrega
- clientes/forms.py
- permisos/signals.py
- base.py
- ingresar_usuario
- DireccionEntregaForm
- RolEmpleadoForm
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- AltaClienteValidacionesTests
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
- StockReservadoTests
- QA-04 Abono con costo 0
- pedidos/tests.py
- RegistroUsuarioForm
- RolBackend
- GuardsUnificadosTests
- FASE3_LOGISTICA.md
- webhook_mercadopago
- QA-05 Zona sin días de reparto
- CobroManualTests
- puede_ver_nota_seguridad
- promociones/tests.py
- 0013_detallehojaruta_es_venta_calle.py
- permisos/views.py
- QA-06 Email de producción sin configurar
- VistasCuentasTests
- RF-05 · Clientes Normal/Premium; fiado solo Premium
- CarritoSoloPorPostTests
- 0003_sembrar_metodos_pago.py
- InicioTests
- 0002_bidones_recargables_y_rol_recargador.py
- 0003_grupos_base.py
- QA campo a campo — 12/11/2026
- 0004_asignar_grupo_permisos.py
- clientes/forms.py
- ActualizarEstadoForm
- ZonaQuerySet
- autenticacion
- QA-01 Validaciones solo en formularios
- empleados
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- 🌊 Distribuidora 3.0 / Aguadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- EliminarProductoTests
- {{title}}
- Zona
- cambios_sin_guardar.js
- abonos
- Cliente
- Roles y permisos.md
- {{title}}
- {{date}}
- generar_borradores_periodo
- CLAUDE.md
- envuelta
- carrito
- buscador
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
- C-9 — Gastos por proveedor (RF-20)
- logistica
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- TelefonoContacto
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- pedidos
- VariasDireccionesTests
- clientes/tests.py
- DireccionEntrega
- RolEmpleado
- OrdenDirectorioClientesTests
- 0015_numero_cliente.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 117 edges
2. `puede()` - 102 edges
3. `Producto` - 92 edges
4. `Pedido` - 79 edges
5. `DireccionEntrega` - 64 edges
6. `Zona` - 62 edges
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

## Communities (177 total, 69 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.09
Nodes (13): CodigoRecuperacionForm, NuevaContrasenaForm, RecuperarContrasenaForm, buscar_usuario(), codigo_verificado(), enmascarar_email(), normalizar_codigo(), cerrar_sesion() (+5 more)

### Community 1 - "pedidos/urls.py"
Cohesion: 0.08
Nodes (17): fecha_estimada_para_direccion(), CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, MetodoPago, Meta, cambiar_estado_pago() (+9 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.24
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "Command"
Cohesion: 0.06
Nodes (13): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, _a_dt(), Command, consumir_saldo(), vender_promocion() (+5 more)

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (34): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+26 more)

### Community 5 - "distribuidora/views.py"
Cohesion: 0.18
Nodes (5): clientes_morosos(), resumen_morosidad(), resumen_caja(), promociones_por_vencer(), resumen_dashboard()

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (8): ProductoForm, Meta, Categoria, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.23
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.06
Nodes (15): AbonoAdmin, DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables() (+7 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.08
Nodes (28): 4. ♻️ Redundancias, MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _columnas_ordenables(), _contexto_suscripcion(), crear_cliente() (+20 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.14
Nodes (9): CodigoRecuperacion, Meta, cerrar_recuperacion(), crear_codigo(), enviar_correo(), _hash(), puede_pedir_codigo(), solicitar_codigo() (+1 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.06
Nodes (26): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellon_por_defecto(), confirmar_entrega_en_calle() (+18 more)

### Community 13 - "seed_demo.py"
Cohesion: 0.10
Nodes (5): obtener_o_crear_cuenta(), SinEliminadosManager, SinHojaEliminadaManager, limite_largo(), H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 14 - "requiere"
Cohesion: 0.15
Nodes (13): requiere(), crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria(), eliminar_envase(), eliminar_producto() (+5 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.10
Nodes (26): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba (+18 more)

### Community 17 - "Carrito"
Cohesion: 0.14
Nodes (13): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), stock_disponible(), checkout() (+5 more)

### Community 18 - "base_tienda.html"
Cohesion: 0.11
Nodes (11): buscar_productos(), con_stock_disponible(), stock_reservado_por_producto(), agotados_al_final(), _filtrar_por_categoria(), listar_productos(), ver_producto(), inicio() (+3 more)

### Community 19 - "recortar_textos"
Cohesion: 0.12
Nodes (13): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+5 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.12
Nodes (18): Hallazgos nuevos, actualizar_estado_entrega(), agregar_parada(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona() (+10 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.23
Nodes (6): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 23 - "Pedido"
Cohesion: 0.08
Nodes (18): 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, perfil_cliente_esta_vacio(), DetallePedidoInline (+10 more)

### Community 25 - "Producto"
Cohesion: 0.12
Nodes (9): CategoriaAdmin, ProductoAdmin, bidones_retornables(), CategoriaForm, Meta, EnvaseForm, Producto, Meta (+1 more)

### Community 26 - "pedidos/services.py"
Cohesion: 0.12
Nodes (10): 5. 🔗 Dependencias y archivos compartidos, PagoPedido, Meta, _a_decimal(), aplicar_pago_mercadopago(), metodo_pago_efectivo(), pago_en_curso(), registrar_cobro() (+2 more)

### Community 28 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 29 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.12
Nodes (17): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`) (+9 more)

### Community 30 - "importar_w3w.py"
Cohesion: 0.15
Nodes (8): Command, _indice(), _leer_filas(), _normalizar(), marcar(), Migration, _normalizar(), validar_w3w()

### Community 31 - "MovimientoCuenta"
Cohesion: 0.16
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 32 - "puede"
Cohesion: 0.10
Nodes (11): restaurar_camion(), restaurar_zona(), venta_calle(), es_repartidor_asignado(), obtener_empleado(), puede(), puede_alguna(), puede_operar_hoja() (+3 more)

### Community 33 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.21
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 37 - "logistica/views.py"
Cohesion: 0.09
Nodes (23): AgregarParadaForm, _etiqueta_direccion_cliente(), botellones_por_producto(), carga_sugerida(), entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja(), productos_de_reparto() (+15 more)

### Community 38 - "Empleado"
Cohesion: 0.12
Nodes (5): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, CuentaDeRepartidorTests

### Community 41 - "Qué hice"
Cohesion: 0.18
Nodes (11): 2026-11-16, Baja lógica desde los listados de empleados y clientes, Bloqueos / dudas, Configuración, Envases asociados (nuevo), Ficha del cliente más simple, Más tarde, Pendiente (+3 more)

### Community 43 - "es_personal_interno"
Cohesion: 0.11
Nodes (13): perfil_usuario(), roles_usuario(), es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0 (+5 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 46 - "django_conf"
Cohesion: 0.05
Nodes (20): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+12 more)

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.14
Nodes (5): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, validar_nombre()

### Community 48 - "logistica/admin.py"
Cohesion: 0.09
Nodes (18): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+10 more)

### Community 49 - "aplicar_attrs"
Cohesion: 0.18
Nodes (3): DireccionRegistroForm, Meta, aplicar_attrs()

### Community 50 - "ConfiguracionCorreo"
Cohesion: 0.07
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 51 - "PagosSegurosTests"
Cohesion: 0.19
Nodes (3): firma_webhook_valida(), _firmar(), PagosSegurosTests

### Community 52 - "Abono"
Cohesion: 0.06
Nodes (16): AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests (+8 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 56 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.18
Nodes (8): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 57 - "DireccionEntrega"
Cohesion: 0.09
Nodes (11): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, DireccionEntrega, Meta (+3 more)

### Community 62 - "clientes/forms.py"
Cohesion: 0.10
Nodes (8): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_telefono()

### Community 63 - "permisos/signals.py"
Cohesion: 0.12
Nodes (7): retirar_perfil_cliente_vacio(), crear_perfil_cliente(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 66 - "ingresar_usuario"
Cohesion: 0.24
Nodes (6): IngresarUsuarioForm, ingresar_usuario(), registrar_usuario(), _ya_ingresado(), guardar_telefonos(), destino_personal()

### Community 67 - "DireccionEntregaForm"
Cohesion: 0.12
Nodes (5): DireccionEntregaForm, Meta, FichaDomiciliosTests, What3WordsTests, _link_mapa()

### Community 68 - "RolEmpleadoForm"
Cohesion: 0.15
Nodes (4): RolEmpleadoForm, Meta, BajaLogicaRolTests, sincronizar_grupo_empleado()

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
Nodes (20): CamionForm, Meta, HojaRutaForm, Meta, RutaRepartoForm, Meta, ZonaForm, Meta (+12 more)

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "pedidos/tests.py"
Cohesion: 0.08
Nodes (6): _etiqueta_direccion_con_fecha(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, PagosParcialesTests, StockComprometidoTests, TransicionesManualesTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.21
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (6): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 106 - "webhook_mercadopago"
Cohesion: 0.29
Nodes (3): consultar_pago_mercadopago(), pago_exitoso(), webhook_mercadopago()

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 109 - "puede_ver_nota_seguridad"
Cohesion: 0.19
Nodes (3): _ficha_de_parada(), puede_ver_nota_seguridad(), NotaDeSeguridadTests

### Community 110 - "promociones/tests.py"
Cohesion: 0.06
Nodes (21): 5B — Promociones prepago (RF-09) · ~6 h, CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, PromocionForm, Meta, VenderPromocionForm, Command (+13 more)

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 119 - "CarritoSoloPorPostTests"
Cohesion: 0.18
Nodes (3): ItemCarrito, Meta, CarritoSoloPorPostTests

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 126 - "clientes/forms.py"
Cohesion: 0.12
Nodes (7): AltaClienteConCuentaForm, Meta, BuscarClienteForm, ClienteSinCuentaForm, EditarMiPerfilForm, _ValidarDatosPersonalesMixin, validar_fecha_no_futura()

### Community 129 - "autenticacion"
Cohesion: 0.67
Nodes (3): autenticacion, Notas, Relaciones

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "empleados"
Cohesion: 0.67
Nodes (3): empleados, Notas, Relaciones

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aguadelluvia"
Cohesion: 0.29
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 141 - "Zona"
Cohesion: 0.08
Nodes (10): BarrioForm, Meta, Command, Barrio, Meta, Zona, Meta, ConfirmacionRegresoTests (+2 more)

### Community 142 - "cambios_sin_guardar.js"
Cohesion: 0.60
Nodes (3): campoCambio(), hayCambios(), seGuardaSolo()

### Community 143 - "abonos"
Cohesion: 0.67
Nodes (3): abonos, Notas, Relaciones

### Community 144 - "Cliente"
Cohesion: 0.09
Nodes (5): _bloquear_cuenta(), Cliente, Meta, siguiente_numero_cliente(), BuscarClientesTests

### Community 145 - "Roles y permisos.md"
Cohesion: 0.12
Nodes (11): Notas, permisos, Relaciones, Notas, planta, Reglas, Relaciones, Dónde está en el código (+3 more)

### Community 146 - "{{title}}"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, Qué pasa, {{title}}

### Community 147 - "{{date}}"
Cohesion: 0.40
Nodes (4): Bloqueos / dudas, {{date}}, Pendiente, Qué hice

### Community 148 - "generar_borradores_periodo"
Cohesion: 0.14
Nodes (4): Command, generar_borradores_periodo(), pedidos_candidatos(), GeneracionQuincenalTests

### Community 149 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 151 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 154 - "cuentas"
Cohesion: 0.67
Nodes (3): cuentas, Notas, Relaciones

### Community 155 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa, Resolución

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
Cohesion: 0.15
Nodes (5): TelefonoContactoForm, Meta, TelefonoContacto, Meta, BajaLogicaTelefonoDireccionTests

### Community 177 - "clientes/tests.py"
Cohesion: 0.05
Nodes (11): ClienteForm, Meta, AgregarDireccionTests, BotonPremiumTests, EditarMiPerfilTests, EnlaceGoogleMapsTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests (+3 more)

### Community 182 - "DireccionEntrega"
Cohesion: 0.13
Nodes (3): resumen_recorrido(), PedidoEspontaneoTests, RecorridoRepartidorTests

### Community 189 - "RolEmpleado"
Cohesion: 0.17
Nodes (7): 2. 🟠 Altos — errores funcionales, Usuario, Meta, EmpleadoForm, Meta, RolEmpleado, Meta

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1071 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **69 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/urls.py`, `Command`, `distribuidora/views.py`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `seed_demo.py`, `Zona`, `PROCEDURE.md`, `Carrito`, `generar_borradores_periodo`, `base_dashboard.html`, `clientes/services.py`, `Pedido`, `SemaforizacionTests`, `CuentaCorriente`, `importar_w3w.py`, `MovimientoCuenta`, `puede`, `registrar_cargo`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `logistica/views.py`, `Empleado`, `TelefonoContacto`, `HojaDeRutaUXTests`, `clientes/tests.py`, `Abono`, `DireccionEntrega`, `DireccionEntrega`, `OrdenDirectorioClientesTests`, `permisos/signals.py`, `DireccionEntregaForm`, `AltaClienteValidacionesTests`, `logistica/tests.py`, `pedidos/tests.py`, `FASE3_LOGISTICA.md`, `CobroManualTests`, `puede_ver_nota_seguridad`, `promociones/tests.py`, `VistasCuentasTests`, `RF-05 · Clientes Normal/Premium; fiado solo Premium`, `clientes/forms.py`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 75 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 75 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09090909090909091 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `pedidos/urls.py`, `Command`, `QA-01 Validaciones solo en formularios`, `distribuidora/views.py`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `seed_demo.py`, `Zona`, `requiere`, `Carrito`, `base_tienda.html`, `Pedido`, `pedidos/services.py`, `GeneracionBorradorTests`, `logistica/views.py`, `GenerarEnvaseTests`, `HojaDeRutaUXTests`, `Abono`, `DireccionEntrega`, `logistica/tests.py`, `StockReservadoTests`, `pedidos/tests.py`, `promociones/tests.py`, `CarritoSoloPorPostTests`, `InicioTests`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 65 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/urls.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08484848484848485 - nodes in this community are weakly interconnected._