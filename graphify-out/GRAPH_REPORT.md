# Graph Report - vault-envases-generator-668120  (2026-11-16)

## Corpus Check
- 299 files · ~344,067 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2415 nodes · 5609 edges · 181 communities (113 shown, 68 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 792 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d2714e92`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- django_conf
- empleados/views.py
- promociones/tests.py
- django_db
- ConfiguracionCorreo
- cuentas/views.py
- ProductoForm
- SuscripcionReposicion
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- limites.py
- requiere
- seed_demo.py
- PROCEDURE.md
- Carrito
- base_tienda.html
- logistica/tests.py
- What You Must Do When Invoked
- base_dashboard.html
- clientes/services.py
- django_contrib
- generar_cargos_mensuales
- Pedido
- seed_demo.py
- RecargaTests
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- Command
- registrar_cargo
- puede
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- AccesoAVistasLogisticasTests
- pedidos/tests.py
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
- VistasAbonosTests
- SemaforizacionTests
- abonos/views.py
- graphify reference: extra exports and benchmark
- ConfiguracionCorreoTests
- FuncionesPorRolTests
- StockReservadoTests
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleadoForm
- AbonoForm
- RolSincronizaGrupoTests
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
- PagosSegurosTests
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- MovimientoCuenta
- QA-05 Zona sin días de reparto
- cuentas/admin.py
- puede_ver_nota_seguridad
- Categoria
- 0013_detallehojaruta_es_venta_calle.py
- VistasCuentasTests
- QA-06 Email de producción sin configurar
- ModeloEmpleadoUnicoTests
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- AGENTS.md
- CLAUDE.md
- 0002_bidones_recargables_y_rol_recargador.py
- 0011_renumerar_paradas.py
- QA campo a campo — 12/11/2026
- roles.py
- AltaClienteConCuentaForm
- listar_clientes
- 2026-11-16
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
- buscador
- clientes
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- TelefonoContacto
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- 0006_corregir_ayuda_desc_seguridad.py
- VariasDireccionesTests
- Notas
- InicioTests
- clientes/tests.py
- PedidoEspontaneoTests
- PromocionForm
- Abono
- EditarMiPerfilTests
- autenticacion/migrations/0001_initial.py
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

## Communities (181 total, 68 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.09
Nodes (15): CodigoRecuperacionForm, IngresarUsuarioForm, NuevaContrasenaForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo() (+7 more)

### Community 1 - "django_conf"
Cohesion: 0.06
Nodes (17): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+9 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.19
Nodes (17): RolEmpleado, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+9 more)

### Community 3 - "promociones/tests.py"
Cohesion: 0.12
Nodes (7): consumir_saldo(), vender_promocion(), BasePromociones, CheckoutConSaldoTests, EscenarioAceptacionTests, ReglasDeSaldoTests, VistasPromocionesTests

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (31): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+23 more)

### Community 5 - "ConfiguracionCorreo"
Cohesion: 0.12
Nodes (8): ConfiguracionCorreoForm, Meta, ConfiguracionCorreo, Meta, configuracion, Correo de recuperación de contraseña, Notas, Relaciones

### Community 6 - "cuentas/views.py"
Cohesion: 0.24
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.06
Nodes (23): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h (+15 more)

### Community 9 - "planta/views.py"
Cohesion: 0.09
Nodes (12): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), recarga_de() (+4 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.12
Nodes (21): MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+13 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.10
Nodes (12): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+4 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.07
Nodes (22): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), confirmar_entrega_en_calle(), crear_hoja_borrador() (+14 more)

### Community 13 - "limites.py"
Cohesion: 0.13
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "requiere"
Cohesion: 0.14
Nodes (15): requiere(), decorador(), envuelta(), crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria() (+7 more)

### Community 15 - "seed_demo.py"
Cohesion: 0.12
Nodes (5): Producto, Meta, VigentesQuerySet, limite_largo(), H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.14
Nodes (18): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega (+10 more)

### Community 17 - "Carrito"
Cohesion: 0.30
Nodes (7): ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), solo_clientes()

### Community 18 - "base_tienda.html"
Cohesion: 0.11
Nodes (11): buscar_productos(), con_stock_disponible(), mis_pedidos(), csrf_failure(), agotados_al_final(), listar_productos(), ver_producto(), inicio() (+3 more)

### Community 19 - "logistica/tests.py"
Cohesion: 0.08
Nodes (17): AgregarParadaForm, BarrioForm, Meta, CamionForm, Meta, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta (+9 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.09
Nodes (20): Hallazgos nuevos, ZonaForm, Meta, ZonaFormTests, actualizar_estado_entrega(), crear_ruta(), direcciones_sin_zona(), editar_camion() (+12 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.19
Nodes (7): MovimientoBidon, Meta, _cliente_de_parada(), perfil_cliente_esta_vacio(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 23 - "django_contrib"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 25 - "Pedido"
Cohesion: 0.05
Nodes (31): 1. 🔴 Críticos — seguridad y dinero, 2. 🟠 Altos — errores funcionales, GuardsUnificadosTests, pedidos_pendientes(), CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta (+23 more)

### Community 26 - "seed_demo.py"
Cohesion: 0.11
Nodes (8): obtener_o_crear_cuenta(), registrar_cargo(), Command, CompraPromocion, Meta, revertir_consumos(), saldo_vigente(), vencer_promociones()

### Community 29 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.22
Nodes (7): 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`)

### Community 32 - "puede"
Cohesion: 0.18
Nodes (3): puede(), usa_panel(), EvaluacionDeRolesTests

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.18
Nodes (5): ClienteSinCuentaForm, guardar_telefonos(), crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.18
Nodes (4): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 37 - "pedidos/tests.py"
Cohesion: 0.13
Nodes (8): DetallePedido, Meta, firma_webhook_valida(), stock_comprometido(), stock_disponible(), stock_reservado_por_producto(), _firmar(), StockComprometidoTests

### Community 38 - "Empleado"
Cohesion: 0.12
Nodes (5): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, CuentaDeRepartidorTests

### Community 39 - "distribuidora/views.py"
Cohesion: 0.12
Nodes (13): clientes_morosos(), resumen_morosidad(), DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin (+5 more)

### Community 40 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 41 - "GenerarEnvaseTests"
Cohesion: 0.13
Nodes (7): GenerarEnvaseTests, Baja lógica desde los listados de empleados y clientes, Configuración, Envases asociados (nuevo), Qué hice, Recuperar contraseña con código temporal, Ver el domicilio en Google Maps

### Community 43 - "es_personal_interno"
Cohesion: 0.11
Nodes (13): perfil_usuario(), roles_usuario(), es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0 (+5 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "Promocion"
Cohesion: 0.11
Nodes (12): 5B — Promociones prepago (RF-09) · ~6 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin (+4 more)

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.08
Nodes (9): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, Usuario, Meta, EmpleadoForm, Meta (+1 more)

### Community 48 - "logistica/admin.py"
Cohesion: 0.15
Nodes (13): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+5 more)

### Community 52 - "abonos/views.py"
Cohesion: 0.34
Nodes (6): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono()

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 56 - "StockReservadoTests"
Cohesion: 0.08
Nodes (6): carrito_total(), Carrito, CheckoutRequiereTelefonosTests, PagosParcialesTests, StockReservadoTests, TransicionesManualesTests

### Community 57 - "clientes/admin.py"
Cohesion: 0.12
Nodes (9): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, DireccionEntrega, Meta (+1 more)

### Community 62 - "clientes/forms.py"
Cohesion: 0.10
Nodes (10): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_fecha_no_futura() (+2 more)

### Community 63 - "permisos/signals.py"
Cohesion: 0.14
Nodes (6): retirar_perfil_cliente_vacio(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.15
Nodes (4): RolEmpleadoForm, Meta, BajaLogicaRolTests, sincronizar_grupo_empleado()

### Community 67 - "AbonoForm"
Cohesion: 0.22
Nodes (3): AbonoForm, Meta, BajaLogicaClienteTests

### Community 68 - "RolSincronizaGrupoTests"
Cohesion: 0.12
Nodes (3): BajaLogicaYFotoEmpleadoTests, PantallasDeRolesTests, RolSincronizaGrupoTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.18
Nodes (5): asignar(), Migration, _permisos(), Funcion, Meta

### Community 71 - "DireccionEntregaForm"
Cohesion: 0.25
Nodes (4): DireccionEntregaForm, Meta, DireccionRegistroForm, Meta

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 73 - "HojaRuta"
Cohesion: 0.16
Nodes (3): HojaRuta, Meta, PlanificarRepartoViewTests

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
Cohesion: 0.07
Nodes (11): HojaRutaForm, Meta, Zona, Meta, BajaLogicaCamionTests, BajaLogicaZonaTests, EliminarBorradorRutaTests, HojaRutaZonaYLimitesTests (+3 more)

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "PagosSegurosTests"
Cohesion: 0.09
Nodes (5): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, CobroManualTests, PagosSegurosTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.19
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (7): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (9): Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, Fase 3 · Logística ↔ Pedido, RF-08 · Control de envases prestados, RF-16 · Hojas de ruta diarias, RF-17 · Agrupación automática y generación de hojas (+1 more)

### Community 106 - "MovimientoCuenta"
Cohesion: 0.22
Nodes (3): MovimientoCuenta, Meta, ReglaFiadoTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 108 - "cuentas/admin.py"
Cohesion: 0.50
Nodes (3): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

### Community 110 - "Categoria"
Cohesion: 0.12
Nodes (8): CategoriaAdmin, ProductoAdmin, bidones_retornables(), CategoriaForm, Meta, EnvaseForm, Categoria, Meta

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

### Community 125 - "roles.py"
Cohesion: 0.09
Nodes (9): conexion_y_remitente(), configuracion(), probar_correo(), es_admin(), crear_promocion(), editar_promocion(), _form_promocion(), listar_promociones() (+1 more)

### Community 126 - "AltaClienteConCuentaForm"
Cohesion: 0.20
Nodes (3): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin

### Community 127 - "listar_clientes"
Cohesion: 0.17
Nodes (8): BuscarClienteForm, _columnas_ordenables(), listar_clientes(), _texto_buscable(), marcar(), Migration, _normalizar(), normalizar_texto()

### Community 128 - "2026-11-16"
Cohesion: 0.67
Nodes (3): 2026-11-16, Bloqueos / dudas, Pendiente

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "logistica/views.py"
Cohesion: 0.06
Nodes (36): botellon_por_defecto(), botellones_por_producto(), carga_sugerida(), entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja(), inventario_camion(), productos_de_reparto() (+28 more)

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

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
Cohesion: 0.09
Nodes (6): Detalle, _bloquear_cuenta(), Cliente, Meta, siguiente_numero_cliente(), BuscarClientesTests

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
Cohesion: 0.14
Nodes (4): Command, generar_borradores_periodo(), pedidos_candidatos(), GeneracionQuincenalTests

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
Cohesion: 0.10
Nodes (7): 4. ♻️ Redundancias, TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente(), AltaClienteValidacionesTests

### Community 174 - "Notas"
Cohesion: 0.67
Nodes (3): Notas, pedidos, Relaciones

### Community 177 - "clientes/tests.py"
Cohesion: 0.06
Nodes (10): ClienteForm, Meta, AgregarDireccionTests, BajaLogicaTelefonoDireccionTests, EnlaceGoogleMapsTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests, NumeroClienteTests (+2 more)

### Community 182 - "PedidoEspontaneoTests"
Cohesion: 0.10
Nodes (4): confirmar_hoja(), ConfirmacionRegresoTests, PedidoEspontaneoTests, RecorridoRepartidorTests

### Community 185 - "Abono"
Cohesion: 0.21
Nodes (3): AbonoAdmin, Abono, Meta

### Community 189 - "autenticacion/migrations/0001_initial.py"
Cohesion: 0.25
Nodes (3): Migration, Migration, Migration

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1043 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **68 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `promociones/tests.py`, `logistica/views.py`, `cuentas/views.py`, `SuscripcionReposicion`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `seed_demo.py`, `PROCEDURE.md`, `logistica/tests.py`, `generar_borradores_periodo`, `clientes/services.py`, `generar_cargos_mensuales`, `Pedido`, `seed_demo.py`, `Command`, `registrar_cargo`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `pedidos/tests.py`, `Empleado`, `TelefonoContacto`, `CuentaCorriente`, `distribuidora/views.py`, `HojaDeRutaUXTests`, `clientes/tests.py`, `VistasAbonosTests`, `SemaforizacionTests`, `PedidoEspontaneoTests`, `Abono`, `clientes/admin.py`, `OrdenDirectorioClientesTests`, `permisos/signals.py`, `clientes/forms.py`, `AbonoForm`, `HojaRuta`, `logistica/tests.py`, `PagosSegurosTests`, `FASE3_LOGISTICA.md`, `MovimientoCuenta`, `puede_ver_nota_seguridad`, `VistasCuentasTests`, `Fase 4 · Cuentas corrientes y abonos`, `roles.py`, `AltaClienteConCuentaForm`, `listar_clientes`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 71 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 71 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0907563025210084 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `seed_demo.py` to `promociones/tests.py`, `QA-01 Validaciones solo en formularios`, `logistica/views.py`, `ProductoForm`, `SuscripcionReposicion`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `requiere`, `Carrito`, `base_tienda.html`, `logistica/tests.py`, `generar_cargos_mensuales`, `Pedido`, `seed_demo.py`, `RecargaTests`, `Command`, `GeneracionBorradorTests`, `pedidos/tests.py`, `distribuidora/views.py`, `GenerarEnvaseTests`, `HojaDeRutaUXTests`, `Promocion`, `InicioTests`, `VistasAbonosTests`, `PedidoEspontaneoTests`, `StockReservadoTests`, `Abono`, `PromocionForm`, `AbonoForm`, `Categoria`, `CarritoSoloPorPostTests`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 62 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_conf` be split into smaller, more focused modules?**
  _Cohesion score 0.05555555555555555 - nodes in this community are weakly interconnected._