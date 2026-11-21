# Graph Report - obsidian-vault-reinicio-2295d7  (2026-11-16)

## Corpus Check
- 301 files · ~345,282 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2441 nodes · 5654 edges · 178 communities (108 shown, 70 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 801 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cdd29eb8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- pedidos/urls.py
- empleados/views.py
- promociones/tests.py
- django_db
- roles.py
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
- Producto
- base_tienda.html
- recortar_textos
- What You Must Do When Invoked
- base_dashboard.html
- clientes/services.py
- Pedido
- registrar_cargo
- pedidos/forms.py
- pedidos/tests.py
- CuentaCorriente
- 🏁 Plan de Cierre — Fases 4.5 a 7
- Command
- MovimientoCuenta
- puede
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- AccesoAVistasLogisticasTests
- logistica/views.py
- CuentaDeRepartidorTests
- DetallePedido
- EliminarEnvaseTests
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
- SuscripcionReposicion
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- VistasAbonosTests
- DireccionEntregaForm
- Empleado
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- RecargaTests
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
- BuscarClientesTests
- QA-04 Abono con costo 0
- StockReservadoTests
- RegistroUsuarioForm
- RolBackend
- GuardsUnificadosTests
- FASE3_LOGISTICA.md
- webhook_mercadopago
- QA-05 Zona sin días de reparto
- CobroManualTests
- puede_ver_nota_seguridad
- promociones/admin.py
- 0013_detallehojaruta_es_venta_calle.py
- PromocionForm
- QA-06 Email de producción sin configurar
- EditarMiPerfilTests
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- CheckoutRequiereTelefonosTests
- InicioTests
- 0002_bidones_recargables_y_rol_recargador.py
- NuevaContrasenaForm
- QA campo a campo — 12/11/2026
- BasePromociones
- AltaClienteConCuentaForm
- Promocion
- Fase 5 · Bidones y promociones prepago
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- Command
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- 🌊 Distribuidora 3.0 / Aguadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- EliminarProductoTests
- {{title}}
- Barrio
- cambios_sin_guardar.js
- abonos
- Cliente
- autenticacion.md
- {{title}}
- {{date}}
- Command
- CLAUDE.md
- Roles y permisos
- carrito
- buscador
- DireccionEntrega
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
- C-9 — Gastos por proveedor (RF-20)
- clientes
- logistica
- planta
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
- Usuario
- OrdenDirectorioClientesTests
- 0015_numero_cliente.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 114 edges
2. `puede()` - 102 edges
3. `Producto` - 92 edges
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
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py
- `Dónde está en el código` --references--> `puede()`  [INFERRED]
  notas/Roles y permisos.md → apps/permisos/roles.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (178 total, 70 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.11
Nodes (14): CodigoRecuperacionForm, IngresarUsuarioForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo(), recuperar_contrasena() (+6 more)

### Community 1 - "pedidos/urls.py"
Cohesion: 0.13
Nodes (8): cambiar_estado_pago(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr(), suscripcion_cliente()

### Community 2 - "empleados/views.py"
Cohesion: 0.21
Nodes (17): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+9 more)

### Community 3 - "promociones/tests.py"
Cohesion: 0.19
Nodes (5): consumir_saldo(), revertir_consumos(), vender_promocion(), EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.02
Nodes (38): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+30 more)

### Community 5 - "roles.py"
Cohesion: 0.08
Nodes (10): conexion_y_remitente(), configuracion(), probar_correo(), clientes_morosos(), resumen_morosidad(), es_admin(), CategoriaAdmin, ProductoAdmin (+2 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.24
Nodes (8): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta()

### Community 7 - "ProductoForm"
Cohesion: 0.08
Nodes (6): ProductoForm, Meta, AltaProductoTests, CategoriasPanelTests, GenerarEnvaseTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.09
Nodes (13): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+5 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.10
Nodes (24): BuscarClienteForm, MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _columnas_ordenables(), _contexto_suscripcion(), editar_cliente() (+16 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.10
Nodes (13): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+5 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.06
Nodes (27): 5A — Historial de envases (RF-08) · ~4 h, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, DetalleHojaRuta, Meta, agregar_parada() (+19 more)

### Community 13 - "seed_demo.py"
Cohesion: 0.08
Nodes (9): generar_cargos_mensuales(), FacturacionTests, obtener_o_crear_cuenta(), registrar_cargo(), Command, CompraPromocion, Meta, vencer_promociones() (+1 more)

### Community 14 - "requiere"
Cohesion: 0.09
Nodes (21): requiere(), bidones_retornables(), CategoriaForm, Meta, EnvaseForm, Categoria, Meta, crear_categoria() (+13 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.11
Nodes (21): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-10 · Suite de tests parcial (faltan carrito y buscador), H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar (+13 more)

### Community 17 - "Producto"
Cohesion: 0.13
Nodes (12): carrito_total(), Carrito, ItemCarrito, Meta, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito() (+4 more)

### Community 18 - "base_tienda.html"
Cohesion: 0.10
Nodes (12): buscar_productos(), con_stock_disponible(), stock_reservado_por_producto(), marcar(), Migration, _normalizar(), agotados_al_final(), listar_productos() (+4 more)

### Community 19 - "recortar_textos"
Cohesion: 0.12
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.11
Nodes (20): Hallazgos nuevos, actualizar_estado_entrega(), agregar_parada(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona() (+12 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.22
Nodes (6): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 23 - "Pedido"
Cohesion: 0.10
Nodes (10): 2. 🟠 Altos — errores funcionales, A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta (+2 more)

### Community 24 - "registrar_cargo"
Cohesion: 0.10
Nodes (4): registrar_pago(), CuentaCorrienteModelTests, SemaforizacionTests, VistasCuentasTests

### Community 25 - "pedidos/forms.py"
Cohesion: 0.11
Nodes (12): fecha_estimada_para_direccion(), CheckoutForm, metodos_pago_checkout_web(), RegistrarPagoForm, SuscripcionForm, Meta, MetodoPago, Meta (+4 more)

### Community 26 - "pedidos/tests.py"
Cohesion: 0.10
Nodes (10): PagoPedido, Meta, firma_webhook_valida(), pago_en_curso(), resumen_caja(), stock_comprometido(), stock_disponible(), _firmar() (+2 more)

### Community 28 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 29 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.09
Nodes (20): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas (+12 more)

### Community 31 - "MovimientoCuenta"
Cohesion: 0.16
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 32 - "puede"
Cohesion: 0.10
Nodes (9): puede(), usa_panel(), EvaluacionDeRolesTests, csrf_failure(), crear_promocion(), editar_promocion(), _form_promocion(), listar_promociones() (+1 more)

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.22
Nodes (4): ClienteSinCuentaForm, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.21
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 37 - "logistica/views.py"
Cohesion: 0.06
Nodes (34): ActualizarEstadoForm, Meta, AgregarParadaForm, CamionForm, Meta, _etiqueta_direccion_cliente(), Camion, Meta (+26 more)

### Community 39 - "DetallePedido"
Cohesion: 0.25
Nodes (8): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido, Meta

### Community 41 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-16, Baja lógica desde los listados de empleados y clientes, Bloqueos / dudas, Configuración, Envases asociados (nuevo), Ficha del cliente más simple, Inicio de la tienda (rehecho), Más tarde (+4 more)

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
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 49 - "aplicar_attrs"
Cohesion: 0.14
Nodes (4): DireccionRegistroForm, Meta, EditarMiPerfilForm, aplicar_attrs()

### Community 50 - "ConfiguracionCorreo"
Cohesion: 0.09
Nodes (9): ConfiguracionCorreoForm, Meta, ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion, Correo de recuperación de contraseña, Notas (+1 more)

### Community 51 - "PagosSegurosTests"
Cohesion: 0.18
Nodes (4): _a_decimal(), aplicar_pago_mercadopago(), registrar_pago_manual(), PagosSegurosTests

### Community 52 - "Abono"
Cohesion: 0.13
Nodes (11): AbonoAdmin, AbonoForm, Meta, Abono, Meta, cambiar_estado_abono(), crear_abono(), editar_abono() (+3 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "RolSincronizaGrupoTests"
Cohesion: 0.23
Nodes (3): EmpleadoForm, Meta, RolSincronizaGrupoTests

### Community 56 - "SuscripcionReposicion"
Cohesion: 0.15
Nodes (10): 4. ❓ Decisiones a tomar antes de empezar, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, perfil_cliente_esta_vacio(), SuscripcionReposicion (+2 more)

### Community 57 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 62 - "clientes/forms.py"
Cohesion: 0.10
Nodes (10): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_fecha_no_futura() (+2 more)

### Community 63 - "permisos/signals.py"
Cohesion: 0.14
Nodes (6): retirar_perfil_cliente_vacio(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 67 - "DireccionEntregaForm"
Cohesion: 0.25
Nodes (3): DireccionEntregaForm, Meta, FichaDomiciliosTests

### Community 68 - "Empleado"
Cohesion: 0.06
Nodes (12): EmpleadoAdmin, RolEmpleadoAdmin, RolEmpleadoForm, Meta, Empleado, Meta, RolEmpleado, Meta (+4 more)

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
Cohesion: 0.11
Nodes (7): HojaRuta, Meta, generar_borradores_periodo(), pedidos_candidatos(), GeneracionQuincenalTests, eliminar_ruta(), restaurar_ruta()

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

### Community 98 - "logistica/tests.py"
Cohesion: 0.05
Nodes (18): HojaRutaForm, Meta, ZonaForm, Meta, Zona, Meta, BajaLogicaCamionTests, BajaLogicaZonaTests (+10 more)

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "StockReservadoTests"
Cohesion: 0.11
Nodes (4): _etiqueta_direccion_con_fecha(), CheckoutFechaEstimadaTests, StockReservadoTests, TransicionesManualesTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.16
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "webhook_mercadopago"
Cohesion: 0.29
Nodes (3): consultar_pago_mercadopago(), pago_exitoso(), webhook_mercadopago()

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 109 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (4): _ficha_de_parada(), _link_mapa(), puede_ver_nota_seguridad(), NotaDeSeguridadTests

### Community 110 - "promociones/admin.py"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 118 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "BasePromociones"
Cohesion: 0.21
Nodes (3): BasePromociones, CheckoutConSaldoTests, VistasPromocionesTests

### Community 126 - "AltaClienteConCuentaForm"
Cohesion: 0.20
Nodes (3): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin

### Community 128 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

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
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 141 - "Barrio"
Cohesion: 0.05
Nodes (25): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+17 more)

### Community 142 - "cambios_sin_guardar.js"
Cohesion: 0.60
Nodes (3): campoCambio(), hayCambios(), seGuardaSolo()

### Community 143 - "abonos"
Cohesion: 0.67
Nodes (3): abonos, Notas, Relaciones

### Community 144 - "Cliente"
Cohesion: 0.08
Nodes (11): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original), _bloquear_cuenta(), Cliente (+3 more)

### Community 145 - "autenticacion.md"
Cohesion: 0.16
Nodes (9): autenticacion, Notas, Relaciones, empleados, Notas, Relaciones, Notas, permisos (+1 more)

### Community 146 - "{{title}}"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, Qué pasa, {{title}}

### Community 147 - "{{date}}"
Cohesion: 0.40
Nodes (4): Bloqueos / dudas, {{date}}, Pendiente, Qué hice

### Community 149 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 150 - "Roles y permisos"
Cohesion: 0.50
Nodes (4): Dónde está en el código, Funciones y roles por defecto, Reglas que no dependen de las casillas, Roles y permisos

### Community 151 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 153 - "DireccionEntrega"
Cohesion: 0.13
Nodes (5): DireccionEntrega, Meta, EnlaceGoogleMapsTests, Notas, RF-03 · Multidirección de entrega

### Community 154 - "cuentas"
Cohesion: 0.67
Nodes (3): cuentas, Notas, Relaciones

### Community 155 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa, Resolución

### Community 158 - "logistica"
Cohesion: 0.67
Nodes (3): logistica, Notas, Relaciones

### Community 159 - "planta"
Cohesion: 0.50
Nodes (4): Notas, planta, Reglas, Relaciones

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
Cohesion: 0.11
Nodes (6): TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente(), AltaClienteValidacionesTests

### Community 177 - "clientes/tests.py"
Cohesion: 0.05
Nodes (11): ClienteForm, Meta, AgregarDireccionTests, BajaLogicaClienteTests, BajaLogicaTelefonoDireccionTests, BotonPremiumTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests (+3 more)

### Community 182 - "DireccionEntrega"
Cohesion: 0.13
Nodes (3): resumen_recorrido(), PedidoEspontaneoTests, RecorridoRepartidorTests

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1060 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **70 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `Fase 5 · Bidones y promociones prepago`, `pedidos/urls.py`, `promociones/tests.py`, `roles.py`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `seed_demo.py`, `Barrio`, `PROCEDURE.md`, `base_dashboard.html`, `clientes/services.py`, `Pedido`, `registrar_cargo`, `DireccionEntrega`, `pedidos/forms.py`, `pedidos/tests.py`, `CuentaCorriente`, `Command`, `MovimientoCuenta`, `puede`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `logistica/views.py`, `CuentaDeRepartidorTests`, `TelefonoContacto`, `HojaDeRutaUXTests`, `clientes/tests.py`, `Abono`, `DireccionEntrega`, `SuscripcionReposicion`, `clientes/admin.py`, `OrdenDirectorioClientesTests`, `clientes/forms.py`, `permisos/signals.py`, `VistasAbonosTests`, `DireccionEntregaForm`, `HojaRuta`, `logistica/tests.py`, `BuscarClientesTests`, `StockReservadoTests`, `CobroManualTests`, `puede_ver_nota_seguridad`, `Fase 4 · Cuentas corrientes y abonos`, `BasePromociones`, `AltaClienteConCuentaForm`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Are the 73 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 73 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1053763440860215 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `promociones/tests.py`, `QA-01 Validaciones solo en formularios`, `roles.py`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `clientes/views.py`, `EliminarProductoTests`, `logistica/services.py`, `seed_demo.py`, `requiere`, `base_tienda.html`, `pedidos/forms.py`, `pedidos/tests.py`, `Command`, `GeneracionBorradorTests`, `logistica/views.py`, `DetallePedido`, `EliminarEnvaseTests`, `HojaDeRutaUXTests`, `Abono`, `DireccionEntrega`, `SuscripcionReposicion`, `VistasAbonosTests`, `RecargaTests`, `logistica/tests.py`, `StockReservadoTests`, `PromocionForm`, `CarritoSoloPorPostTests`, `CheckoutRequiereTelefonosTests`, `InicioTests`, `BasePromociones`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 65 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/urls.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._