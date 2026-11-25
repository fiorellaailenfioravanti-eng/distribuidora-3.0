# Graph Report - distribuidora-3.0  (2026-11-25)

## Corpus Check
- 258 files · ~127,806 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 17 file(s) not represented in the graph (top: (none) 6, .css 4, .jfif 3)

## Summary
- 2488 nodes · 5747 edges · 198 communities (127 shown, 71 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 751 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fb8c81b6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- pedidos/views.py
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
- puede
- clientes/services.py
- Pedido
- SemaforizacionTests
- Producto
- pedidos/tests.py
- CuentaCorriente
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- importar_w3w.py
- MovimientoCuenta
- roles.py
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
- GruposBaseTests
- django_conf
- PerfilUsuarioForm
- CalendarioTests
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
- ver_cliente
- base.py
- crear_cliente_con_cuenta
- DireccionEntregaForm
- RolEmpleadoForm
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- DetalleHojaRuta
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
- PagoPorVerificarTests
- RegistroUsuarioForm
- RolBackend
- GuardsUnificadosTests
- FASE3_LOGISTICA.md
- RecorridoRepartidorTests
- QA-05 Zona sin días de reparto
- CobroManualTests
- puede_ver_nota_seguridad
- CompraPromocion
- 0013_detallehojaruta_es_venta_calle.py
- django_contrib
- configuracion.md
- VistasCuentasTests
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- 0003_sembrar_metodos_pago.py
- InicioTests
- 0002_bidones_recargables_y_rol_recargador.py
- 0003_grupos_base.py
- QA campo a campo — 12/11/2026
- 0004_asignar_grupo_permisos.py
- ClienteForm
- logistica/forms.py
- logistica/models.py
- autenticacion
- QA-01 Validaciones solo en formularios
- empleados
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- os
- DetallePedido
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
- vender_promocion
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- TelefonoContacto
- Barrio
- pedidos
- SuscripcionReposicion
- VariasDireccionesTests
- registrar_entrega
- vencer_promociones
- base_dashboard.html
- RecargaTests
- TestCase
- Camion
- ZonaForm
- BasePromociones
- PromocionForm
- PedidoEspontaneoTests
- autenticacion/forms.py
- promociones/admin.py
- EditarMiPerfilTests
- ModeloEmpleadoUnicoTests
- EnlaceGoogleMapsTests
- CheckoutRequiereTelefonosTests
- RolEmpleado
- OrdenDirectorioClientesTests
- Fase 6 · Pagos parciales y pedido automático
- con_stock_disponible
- 0015_numero_cliente.py
- Verificar cambios — Distribuidora 3.0
- Fase 5 · Bidones y promociones prepago
- Verificar cambios — Distribuidora 3.0
- 2026-11-16

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 117 edges
2. `puede()` - 102 edges
3. `Producto` - 92 edges
4. `Pedido` - 83 edges
5. `DireccionEntrega` - 64 edges
6. `Zona` - 62 edges
7. `HojaRuta` - 55 edges
8. `MetodoPago` - 49 edges
9. `Empleado` - 45 edges
10. `DetalleHojaRuta` - 40 edges

## Surprising Connections (you probably didn't know these)
- `Funciones y roles por defecto` --references--> `cambiar_tipo_cliente()`  [INFERRED]
  notas/Roles y permisos.md → apps/clientes/views.py
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `5. 🔗 Dependencias y archivos compartidos` --references--> `registrar_cobro()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/pedidos/services.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (198 total, 71 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.12
Nodes (14): IngresarUsuarioForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo(), recuperar_contrasena(), recuperar_listo() (+6 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.09
Nodes (17): 1. 🔴 Críticos — seguridad y dinero, RegistrarPagoForm, consultar_pago_mercadopago(), cambiar_estado_pago(), cambiar_estado_pedido(), confirmar_pago_qr(), detalle_pedido(), listar_pedidos() (+9 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.24
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (34): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+26 more)

### Community 5 - "distribuidora/views.py"
Cohesion: 0.27
Nodes (3): clientes_morosos(), resumen_morosidad(), resumen_dashboard()

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (8): ProductoForm, Meta, Categoria, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.09
Nodes (12): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), recarga_de() (+4 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.13
Nodes (20): BuscarClienteForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _columnas_ordenables(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+12 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.11
Nodes (11): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+3 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.15
Nodes (14): agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), confirmar_entrega_en_calle(), crear_hoja_borrador(), crear_venta_calle(), _fijar_botellones(), fijar_pedido_de_parada() (+6 more)

### Community 13 - "seed_demo.py"
Cohesion: 0.12
Nodes (3): obtener_o_crear_cuenta(), limite_largo(), H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 14 - "requiere"
Cohesion: 0.13
Nodes (16): requiere(), CategoriaForm, Meta, crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria() (+8 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (14): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose (+6 more)

### Community 17 - "Carrito"
Cohesion: 0.11
Nodes (15): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito() (+7 more)

### Community 18 - "base_tienda.html"
Cohesion: 0.14
Nodes (7): buscar_productos(), agotados_al_final(), eliminar_producto(), listar_productos(), ver_producto(), inicio(), RF-07 · Buscador tolerante a tildes

### Community 19 - "recortar_textos"
Cohesion: 0.11
Nodes (13): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+5 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "puede"
Cohesion: 0.10
Nodes (20): Hallazgos nuevos, actualizar_estado_entrega(), agregar_parada(), agregar_pedido_parada(), editar_camion(), editar_ruta(), eliminar_camion(), eliminar_parada() (+12 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.06
Nodes (20): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, MovimientoBidon, Meta (+12 more)

### Community 23 - "Pedido"
Cohesion: 0.12
Nodes (4): 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta

### Community 25 - "Producto"
Cohesion: 0.15
Nodes (6): CategoriaAdmin, ProductoAdmin, bidones_retornables(), EnvaseForm, Producto, Meta

### Community 26 - "pedidos/tests.py"
Cohesion: 0.12
Nodes (12): PagoPedido, Meta, _a_decimal(), ajustar_pagos_provisorios(), aplicar_pago_mercadopago(), firma_webhook_valida(), pago_en_curso(), registrar_cobro() (+4 more)

### Community 28 - "CuentaCorriente"
Cohesion: 0.14
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 29 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.29
Nodes (7): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`)

### Community 30 - "importar_w3w.py"
Cohesion: 0.19
Nodes (7): Command, _indice(), _leer_filas(), _normalizar(), marcar(), Migration, _normalizar()

### Community 31 - "MovimientoCuenta"
Cohesion: 0.18
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 32 - "roles.py"
Cohesion: 0.18
Nodes (5): confirmar_entrega(), es_repartidor_asignado(), obtener_empleado(), puede_operar_hoja(), usa_panel()

### Community 33 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 37 - "logistica/views.py"
Cohesion: 0.11
Nodes (18): botellones_por_producto(), carga_sugerida(), entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja(), inventario_camion(), registrar_regreso(), resumen_recorrido() (+10 more)

### Community 38 - "Empleado"
Cohesion: 0.15
Nodes (3): Empleado, Meta, CuentaDeRepartidorTests

### Community 39 - "BajaLogicaYFotoEmpleadoTests"
Cohesion: 0.13
Nodes (4): RolEmpleado, Meta, BajaLogicaYFotoEmpleadoTests, PantallasDeRolesTests

### Community 41 - "Qué hice"
Cohesion: 0.22
Nodes (9): Baja lógica desde los listados de empleados y clientes, Configuración, Envases asociados (nuevo), Ficha del cliente más simple, Inicio de la tienda (rehecho), Más tarde, Qué hice, Recuperar contraseña con código temporal (+1 more)

### Community 43 - "es_personal_interno"
Cohesion: 0.43
Nodes (4): roles_usuario(), es_personal_interno(), 2. Revisar convenciones del proyecto en lo que cambió, 2. Revisar convenciones del proyecto en lo que cambió

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 46 - "django_conf"
Cohesion: 0.05
Nodes (22): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+14 more)

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.10
Nodes (6): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, perfil_usuario(), validar_nombre()

### Community 48 - "CalendarioTests"
Cohesion: 0.20
Nodes (4): fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 49 - "aplicar_attrs"
Cohesion: 0.13
Nodes (4): DireccionRegistroForm, Meta, EditarMiPerfilForm, aplicar_attrs()

### Community 50 - "ConfiguracionCorreo"
Cohesion: 0.07
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 52 - "Abono"
Cohesion: 0.05
Nodes (17): AbonoAdmin, AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests (+9 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 56 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (7): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 57 - "DireccionEntrega"
Cohesion: 0.16
Nodes (5): DireccionEntrega, Meta, clientes, Notas, Relaciones

### Community 62 - "clientes/forms.py"
Cohesion: 0.07
Nodes (12): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin, ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas() (+4 more)

### Community 63 - "ver_cliente"
Cohesion: 0.11
Nodes (9): MovimientoBidonForm, TelefonoContactoForm, Meta, _contexto_suscripcion(), mi_perfil_cliente(), ver_cliente(), VenderPromocionForm, compras_vigentes() (+1 more)

### Community 66 - "crear_cliente_con_cuenta"
Cohesion: 0.21
Nodes (4): guardar_telefonos(), crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 67 - "DireccionEntregaForm"
Cohesion: 0.15
Nodes (4): DireccionEntregaForm, Meta, FichaDomiciliosTests, What3WordsTests

### Community 68 - "RolEmpleadoForm"
Cohesion: 0.18
Nodes (3): RolEmpleadoForm, Meta, BajaLogicaRolTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.18
Nodes (5): asignar(), Migration, _permisos(), Funcion, Meta

### Community 71 - "DetalleHojaRuta"
Cohesion: 0.14
Nodes (11): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+3 more)

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 73 - "HojaRuta"
Cohesion: 0.21
Nodes (4): HojaRuta, Meta, eliminar_ruta(), restaurar_ruta()

### Community 74 - "popups.js"
Cohesion: 0.24
Nodes (16): actualizarTope(), avisar(), cerrarAviso(), confirmar(), contenedorAvisos(), erroresDelServidor(), escapar(), etiquetaDe() (+8 more)

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
Nodes (8): RutaReparto, Meta, BajaLogicaZonaTests, EliminarBorradorRutaTests, HojaRutaCapacidadTests, HojaRutaZonaYLimitesTests, HojaSinChoferTests, SeedDemoTests

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "PagoPorVerificarTests"
Cohesion: 0.11
Nodes (4): _etiqueta_direccion_con_fecha(), CheckoutFechaEstimadaTests, PagoPorVerificarTests, TransicionesManualesTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.21
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "RecorridoRepartidorTests"
Cohesion: 0.11
Nodes (6): CargaHojaRuta, Meta, confirmar_hoja(), ConfirmacionRegresoTests, RecorridoRepartidorTests, Carga y regreso del camión (sobrantes a stock)

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 108 - "CobroManualTests"
Cohesion: 0.13
Nodes (7): CheckoutForm, metodos_pago_checkout_web(), SuscripcionForm, Meta, MetodoPago, Meta, CobroManualTests

### Community 110 - "CompraPromocion"
Cohesion: 0.14
Nodes (7): 5B — Promociones prepago (RF-09) · ~6 h, CompraPromocion, Meta, Promocion, Meta, promociones_por_vencer(), listar_promociones()

### Community 114 - "django_contrib"
Cohesion: 0.15
Nodes (3): EmpleadoAdmin, RolEmpleadoAdmin, csrf_failure()

### Community 116 - "configuracion.md"
Cohesion: 0.18
Nodes (8): Notas, permisos, Relaciones, Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 118 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 126 - "ClienteForm"
Cohesion: 0.29
Nodes (4): ClienteForm, Meta, ClienteSinCuentaForm, ValidacionesClienteTests

### Community 127 - "logistica/forms.py"
Cohesion: 0.09
Nodes (15): ActualizarEstadoForm, Meta, AgregarParadaForm, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta, botellon_por_defecto(), clientes_frecuentes_de_zona() (+7 more)

### Community 128 - "logistica/models.py"
Cohesion: 0.14
Nodes (5): CalendarioExcepcion, Meta, ZonaQuerySet, SinEliminadosManager, SinHojaEliminadaManager

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

### Community 137 - "DetallePedido"
Cohesion: 0.14
Nodes (10): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido, Meta (+2 more)

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 141 - "Zona"
Cohesion: 0.17
Nodes (4): Command, Zona, Meta, ZonaDiasRepartoTests

### Community 142 - "cambios_sin_guardar.js"
Cohesion: 0.60
Nodes (3): campoCambio(), hayCambios(), seGuardaSolo()

### Community 143 - "abonos"
Cohesion: 0.67
Nodes (3): abonos, Notas, Relaciones

### Community 144 - "Cliente"
Cohesion: 0.11
Nodes (5): Detalle, _bloquear_cuenta(), Cliente, Meta, siguiente_numero_cliente()

### Community 145 - "Roles y permisos.md"
Cohesion: 0.11
Nodes (15): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA, Notas (+7 more)

### Community 146 - "{{title}}"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, Qué pasa, {{title}}

### Community 147 - "{{date}}"
Cohesion: 0.40
Nodes (4): Bloqueos / dudas, {{date}}, Pendiente, Qué hice

### Community 148 - "generar_borradores_periodo"
Cohesion: 0.18
Nodes (3): Command, generar_borradores_periodo(), GeneracionQuincenalTests

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

### Community 159 - "vender_promocion"
Cohesion: 0.23
Nodes (4): consumir_saldo(), vender_promocion(), EscenarioAceptacionTests, ReglasDeSaldoTests

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
Cohesion: 0.08
Nodes (7): 4. ♻️ Redundancias, TelefonoContacto, Meta, crear_perfil_cliente(), AltaClienteValidacionesTests, BajaLogicaTelefonoDireccionTests, RF-01 · Registro con ≥2 celulares

### Community 168 - "Barrio"
Cohesion: 0.12
Nodes (6): BarrioForm, Meta, Barrio, Meta, InventarioCamionTests, PlanificarRepartoViewTests

### Community 170 - "SuscripcionReposicion"
Cohesion: 0.14
Nodes (14): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)** (+6 more)

### Community 173 - "registrar_entrega"
Cohesion: 0.15
Nodes (8): 5A — Historial de envases (RF-08) · ~4 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, _producto_envase_para(), registrar_entrega(), EntregaCalleTests

### Community 174 - "vencer_promociones"
Cohesion: 0.13
Nodes (4): FASE 7 — QA, producción y tesis 🎓, Command, revertir_consumos(), vencer_promociones()

### Community 175 - "base_dashboard.html"
Cohesion: 0.14
Nodes (4): crear_ruta(), _ficha_de_parada(), _link_mapa(), mi_ruta_hoy()

### Community 177 - "TestCase"
Cohesion: 0.08
Nodes (6): AgregarDireccionTests, BotonPremiumTests, BuscarClientesTests, FiadoPremiumYExcepcionTests, NumeroClienteTests, VistaMovimientoBidonTests

### Community 178 - "Camion"
Cohesion: 0.16
Nodes (7): CamionForm, Meta, HojaRutaForm, Meta, Camion, Meta, BajaLogicaCamionTests

### Community 179 - "ZonaForm"
Cohesion: 0.23
Nodes (6): ZonaForm, Meta, ZonaFormTests, direcciones_sin_zona(), editar_zona(), listar_zonas()

### Community 180 - "BasePromociones"
Cohesion: 0.21
Nodes (3): BasePromociones, CheckoutConSaldoTests, VistasPromocionesTests

### Community 181 - "PromocionForm"
Cohesion: 0.21
Nodes (5): PromocionForm, Meta, crear_promocion(), editar_promocion(), _form_promocion()

### Community 183 - "autenticacion/forms.py"
Cohesion: 0.20
Nodes (3): CodigoRecuperacionForm, NuevaContrasenaForm, normalizar_codigo()

### Community 184 - "promociones/admin.py"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 189 - "RolEmpleado"
Cohesion: 0.21
Nodes (5): 2. 🟠 Altos — errores funcionales, Usuario, Meta, EmpleadoForm, Meta

### Community 191 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 192 - "con_stock_disponible"
Cohesion: 0.50
Nodes (3): con_stock_disponible(), stock_reservado_por_producto(), Notas

### Community 194 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 195 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 196 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 197 - "2026-11-16"
Cohesion: 0.67
Nodes (3): 2026-11-16, Bloqueos / dudas, Pendiente

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1077 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **71 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `logistica/models.py`, `pedidos/views.py`, `Command`, `distribuidora/views.py`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `seed_demo.py`, `PROCEDURE.md`, `Carrito`, `generar_borradores_periodo`, `puede`, `clientes/services.py`, `Pedido`, `SemaforizacionTests`, `pedidos/tests.py`, `CuentaCorriente`, `importar_w3w.py`, `MovimientoCuenta`, `vender_promocion`, `registrar_cargo`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `logistica/views.py`, `Empleado`, `TelefonoContacto`, `Barrio`, `HojaDeRutaUXTests`, `SuscripcionReposicion`, `registrar_entrega`, `TestCase`, `Abono`, `BasePromociones`, `PedidoEspontaneoTests`, `EnlaceGoogleMapsTests`, `OrdenDirectorioClientesTests`, `clientes/forms.py`, `ver_cliente`, `crear_cliente_con_cuenta`, `Fase 5 · Bidones y promociones prepago`, `DireccionEntregaForm`, `logistica/tests.py`, `PagoPorVerificarTests`, `RecorridoRepartidorTests`, `CobroManualTests`, `puede_ver_nota_seguridad`, `VistasCuentasTests`, `Fase 4 · Cuentas corrientes y abonos`, `ClienteForm`, `logistica/forms.py`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Are the 75 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 75 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12169312169312169 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `pedidos/views.py`, `Command`, `QA-01 Validaciones solo en formularios`, `distribuidora/views.py`, `ProductoForm`, `PedidoAutomaticoTests`, `DetallePedido`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `seed_demo.py`, `requiere`, `Carrito`, `base_tienda.html`, `pedidos/tests.py`, `vender_promocion`, `GeneracionBorradorTests`, `logistica/views.py`, `Barrio`, `GenerarEnvaseTests`, `HojaDeRutaUXTests`, `SuscripcionReposicion`, `registrar_entrega`, `RecargaTests`, `Abono`, `PromocionForm`, `PedidoEspontaneoTests`, `BasePromociones`, `CheckoutRequiereTelefonosTests`, `con_stock_disponible`, `logistica/tests.py`, `StockReservadoTests`, `RecorridoRepartidorTests`, `CarritoSoloPorPostTests`, `InicioTests`, `logistica/forms.py`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 65 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08562367864693446 - nodes in this community are weakly interconnected._