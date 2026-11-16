# Graph Report - obsidian-vault-reinicio-2295d7  (2026-11-16)

## Corpus Check
- 300 files · ~342,333 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2382 nodes · 5551 edges · 190 communities (113 shown, 77 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 779 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9d51365a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- abonos/views.py
- empleados/views.py
- vender_promocion
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
- logistica/views.py
- Producto
- PROCEDURE.md
- Producto
- buscador/views.py
- PedidoEspontaneoTests
- What You Must Do When Invoked
- puede
- clientes/services.py
- django_contrib
- generar_cargos_mensuales
- pedidos/views.py
- vencer_promociones
- AbonoForm
- RolEmpleado
- CheckoutFechaEstimadaTests
- requiere
- puede
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- DetalleHojaRuta
- requiere
- Empleado
- distribuidora/views.py
- CuentaCorriente
- TelefonoContacto
- HojaDeRutaUXTests
- 0007_funciones_por_defecto.py
- Migración: unificar empleados
- GuardsUnificadosTests
- Migración: métodos de pago
- PerfilUsuarioForm
- CompraPromocion
- aplicar_attrs
- Pedido
- Usuario
- Command
- graphify reference: extra exports and benchmark
- EditarMiPerfilTests
- 🌊 Distribuidora 3.0 / Aguadelluvia
- TransicionesManualesTests
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleadoForm
- roles.py
- RolSincronizaGrupoTests
- graphify reference: query, path, explain
- CuentaDeRepartidorTests
- PagosSegurosTests
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
- CheckoutConSaldoTests
- QA-04 Abono con costo 0
- firma_webhook_valida
- autenticacion/tests.py
- RolBackend
- Fase 6 · Pagos parciales y pedido automático
- FASE3_LOGISTICA.md
- MovimientoCuenta
- QA-05 Zona sin días de reparto
- permisos/apps.py
- FuncionesPorRolTests
- CobroManualTests
- 0013_detallehojaruta_es_venta_calle.py
- Verificar cambios — Distribuidora 3.0
- QA-06 Email de producción sin configurar
- AccesoAVistasLogisticasTests
- Fase 5 · Bidones y promociones prepago
- CarritoSoloPorPostTests
- Verificar cambios — Distribuidora 3.0
- django_contrib
- 0002_bidones_recargables_y_rol_recargador.py
- RolSincronizaGrupoTests
- QA campo a campo — 12/11/2026
- clientes/tests.py
- 0003_grupos_base.py
- 0007_marcar_botellones.py
- SuscripcionReposicion
- Categoria
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
- ClientesConfig
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- 0005_quitar_perfil_cliente_del_personal.py
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- StockReservadoTests
- SuscripcionForm
- BuscarClientesTests
- permisos/models.py
- CLAUDE.md
- OrdenDirectorioClientesTests
- buscador/apps.py
- ModeloEmpleadoUnicoTests
- InicioTests
- 2026-11-16
- CheckoutRequiereTelefonosTests
- QA-09 Recuperar contraseña usa vistas de clase
- carrito/apps.py
- configuracion/apps.py
- 0006_corregir_ayuda_desc_seguridad.py
- 0015_numero_cliente.py
- cuentas/apps.py
- empleados/apps.py
- logistica/apps.py
- pedidos/apps.py
- planta/apps.py
- promociones/apps.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 111 edges
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

## Communities (190 total, 77 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.10
Nodes (16): CodigoRecuperacionForm, IngresarUsuarioForm, NuevaContrasenaForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo() (+8 more)

### Community 1 - "abonos/views.py"
Cohesion: 0.34
Nodes (6): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono()

### Community 2 - "empleados/views.py"
Cohesion: 0.22
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "vender_promocion"
Cohesion: 0.23
Nodes (4): consumir_saldo(), vender_promocion(), EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.02
Nodes (55): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+47 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.09
Nodes (9): ConfiguracionCorreoForm, Meta, ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion, Correo de recuperación de contraseña, Notas (+1 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.23
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.07
Nodes (14): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+6 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.09
Nodes (27): BuscarClienteForm, DireccionEntregaForm, Meta, MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _columnas_ordenables() (+19 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.09
Nodes (12): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+4 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.08
Nodes (22): 5A — Historial de envases (RF-08) · ~4 h, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellones_por_producto(), confirmar_entrega_en_calle(), confirmar_hoja(), crear_hoja_borrador() (+14 more)

### Community 13 - "limites.py"
Cohesion: 0.14
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "logistica/views.py"
Cohesion: 0.08
Nodes (26): Camion, Meta, carga_sugerida(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), agregar_pedido_parada(), _cargas_confirmacion_desde_post() (+18 more)

### Community 15 - "Producto"
Cohesion: 0.10
Nodes (8): obtener_o_crear_cuenta(), _a_decimal(), aplicar_pago_mercadopago(), metodo_pago_efectivo(), registrar_cobro(), registrar_pago_manual(), stock_comprometido(), stock_reservado_por_producto()

### Community 16 - "PROCEDURE.md"
Cohesion: 0.13
Nodes (16): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega, RF-05 · Clientes Normal/Premium; fiado solo Premium (+8 more)

### Community 17 - "Producto"
Cohesion: 0.09
Nodes (10): DetallePedido, Meta, MetodoPago, Meta, StockComprometidoTests, Producto, Meta, VigentesQuerySet (+2 more)

### Community 18 - "buscador/views.py"
Cohesion: 0.14
Nodes (9): 3. 🟡 Medios, buscar_productos(), con_stock_disponible(), agotados_al_final(), ver_producto(), Notas, pedidos, Relaciones (+1 more)

### Community 19 - "PedidoEspontaneoTests"
Cohesion: 0.13
Nodes (3): resumen_recorrido(), PedidoEspontaneoTests, RecorridoRepartidorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "puede"
Cohesion: 0.11
Nodes (20): Hallazgos nuevos, actualizar_estado_entrega(), agregar_parada(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona() (+12 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.23
Nodes (6): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 23 - "django_contrib"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 25 - "pedidos/views.py"
Cohesion: 0.06
Nodes (31): 1. 🔴 Críticos — seguridad y dinero, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito() (+23 more)

### Community 26 - "vencer_promociones"
Cohesion: 0.18
Nodes (7): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, FASE 7 — QA, producción y tesis 🎓, Punto de partida real, Command, vencer_promociones()

### Community 28 - "AbonoForm"
Cohesion: 0.22
Nodes (3): AbonoForm, Meta, BajaLogicaClienteTests

### Community 29 - "RolEmpleado"
Cohesion: 0.18
Nodes (10): 2. 🟠 Altos — errores funcionales, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`) (+2 more)

### Community 30 - "CheckoutFechaEstimadaTests"
Cohesion: 0.20
Nodes (3): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests

### Community 31 - "requiere"
Cohesion: 0.22
Nodes (5): RegistrarPagoForm, registrar_pago(), requiere(), decorador(), envuelta()

### Community 32 - "puede"
Cohesion: 0.14
Nodes (7): puede(), EvaluacionDeRolesTests, crear_promocion(), editar_promocion(), _form_promocion(), listar_promociones(), vender_promocion()

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.18
Nodes (4): ClienteSinCuentaForm, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, AutenticacionConfig, ProductosConfig

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.18
Nodes (4): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 36 - "DetalleHojaRuta"
Cohesion: 0.08
Nodes (18): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+10 more)

### Community 37 - "requiere"
Cohesion: 0.17
Nodes (10): crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_producto(), _filtrar_por_categoria(), listar_productos(), listar_productos_admin() (+2 more)

### Community 38 - "Empleado"
Cohesion: 0.20
Nodes (4): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta

### Community 39 - "distribuidora/views.py"
Cohesion: 0.12
Nodes (13): clientes_morosos(), resumen_morosidad(), DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin (+5 more)

### Community 40 - "CuentaCorriente"
Cohesion: 0.06
Nodes (9): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, CuentaCorriente, Meta, CuentaCorrienteModelTests, SemaforizacionTests, VistasCuentasTests (+1 more)

### Community 41 - "TelefonoContacto"
Cohesion: 0.08
Nodes (7): TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente(), AltaClienteValidacionesTests, RF-01 · Registro con ≥2 celulares

### Community 43 - "0007_funciones_por_defecto.py"
Cohesion: 0.40
Nodes (3): asignar(), Migration, _permisos()

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.12
Nodes (6): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, perfil_usuario(), validar_nombre()

### Community 48 - "CompraPromocion"
Cohesion: 0.09
Nodes (11): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, CompraPromocion, Meta, ConsumoPromocion, Meta, Promocion (+3 more)

### Community 49 - "aplicar_attrs"
Cohesion: 0.12
Nodes (4): DireccionRegistroForm, Meta, EditarMiPerfilForm, aplicar_attrs()

### Community 50 - "Pedido"
Cohesion: 0.11
Nodes (8): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta, revertir_consumos()

### Community 51 - "Usuario"
Cohesion: 0.19
Nodes (4): Usuario, Meta, EmpleadoForm, Meta

### Community 52 - "Command"
Cohesion: 0.07
Nodes (7): AbonoAdmin, Abono, Meta, CostoPreferencialTests, VistasAbonosTests, _a_dt(), Command

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 55 - "🌊 Distribuidora 3.0 / Aguadelluvia"
Cohesion: 0.29
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 57 - "clientes/admin.py"
Cohesion: 0.11
Nodes (9): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, DireccionEntrega, Meta (+1 more)

### Community 62 - "clientes/forms.py"
Cohesion: 0.08
Nodes (12): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin, leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura() (+4 more)

### Community 63 - "permisos/signals.py"
Cohesion: 0.19
Nodes (6): perfil_cliente_esta_vacio(), retirar_perfil_cliente_vacio(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.20
Nodes (3): RolEmpleadoForm, Meta, BajaLogicaRolTests

### Community 67 - "roles.py"
Cohesion: 0.10
Nodes (8): roles_usuario(), es_personal_interno(), puede_ver_nota_seguridad(), sincronizar_grupo_empleado(), usa_panel(), NotaDeSeguridadTests, 2. Revisar convenciones del proyecto en lo que cambió, 2. Revisar convenciones del proyecto en lo que cambió

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 73 - "HojaRuta"
Cohesion: 0.13
Nodes (5): HojaRuta, Meta, EntregaCalleTests, eliminar_ruta(), restaurar_ruta()

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
Cohesion: 0.05
Nodes (15): HojaRutaForm, Meta, ZonaForm, Meta, BajaLogicaCamionTests, BajaLogicaZonaTests, ConfirmacionRegresoTests, EliminarBorradorRutaTests (+7 more)

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 102 - "autenticacion/tests.py"
Cohesion: 0.18
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.25
Nodes (4): Arquitectura visual dual: Tienda vs Dashboard, Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "MovimientoCuenta"
Cohesion: 0.16
Nodes (5): MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), ReglaFiadoTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 114 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 118 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 119 - "CarritoSoloPorPostTests"
Cohesion: 0.18
Nodes (3): ItemCarrito, Meta, CarritoSoloPorPostTests

### Community 120 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 121 - "django_contrib"
Cohesion: 0.11
Nodes (5): conexion_y_remitente(), configuracion(), probar_correo(), es_admin(), csrf_failure()

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "clientes/tests.py"
Cohesion: 0.07
Nodes (9): ClienteForm, Meta, AgregarDireccionTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests, NumeroClienteTests, ValidacionesClienteTests, VariasDireccionesTests (+1 more)

### Community 127 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 128 - "SuscripcionReposicion"
Cohesion: 0.15
Nodes (13): 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)** (+5 more)

### Community 129 - "Categoria"
Cohesion: 0.14
Nodes (9): CategoriaAdmin, ProductoAdmin, CategoriaForm, Meta, Categoria, Meta, eliminar_categoria(), listar_categorias() (+1 more)

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "Barrio"
Cohesion: 0.10
Nodes (15): ActualizarEstadoForm, Meta, AgregarParadaForm, BarrioForm, Meta, CamionForm, Meta, _etiqueta_direccion_cliente() (+7 more)

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.12
Nodes (11): Notas, permisos, Relaciones, Notas, planta, Reglas, Relaciones, Dónde está en el código (+3 more)

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
Cohesion: 0.08
Nodes (11): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original), _bloquear_cuenta(), Cliente (+3 more)

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
Cohesion: 0.22
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

### Community 171 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 176 - "2026-11-16"
Cohesion: 0.20
Nodes (8): inicio(), 2026-11-16, Bloqueos / dudas, Configuración, Inicio de la tienda (rehecho), Pendiente, Qué hice, Recuperar contraseña con código temporal

### Community 178 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa, Resolución

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1021 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **77 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `SuscripcionReposicion`, `vender_promocion`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `logistica/views.py`, `Producto`, `PROCEDURE.md`, `Producto`, `PedidoEspontaneoTests`, `puede`, `clientes/services.py`, `generar_cargos_mensuales`, `pedidos/views.py`, `AbonoForm`, `CheckoutFechaEstimadaTests`, `puede`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `DetalleHojaRuta`, `distribuidora/views.py`, `CuentaCorriente`, `TelefonoContacto`, `BuscarClientesTests`, `HojaDeRutaUXTests`, `OrdenDirectorioClientesTests`, `CompraPromocion`, `Pedido`, `Command`, `clientes/admin.py`, `clientes/forms.py`, `permisos/signals.py`, `roles.py`, `CuentaDeRepartidorTests`, `HojaRuta`, `logistica/tests.py`, `MovimientoCuenta`, `CobroManualTests`, `AccesoAVistasLogisticasTests`, `Fase 5 · Bidones y promociones prepago`, `clientes/tests.py`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 70 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10084033613445378 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `SuscripcionReposicion`, `Categoria`, `vender_promocion`, `QA-01 Validaciones solo en formularios`, `Barrio`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `PromocionForm`, `logistica/views.py`, `Producto`, `buscador/views.py`, `PedidoEspontaneoTests`, `generar_cargos_mensuales`, `pedidos/views.py`, `vencer_promociones`, `AbonoForm`, `GeneracionBorradorTests`, `requiere`, `StockReservadoTests`, `distribuidora/views.py`, `HojaDeRutaUXTests`, `InicioTests`, `CompraPromocion`, `CheckoutRequiereTelefonosTests`, `2026-11-16`, `Command`, `HojaRuta`, `logistica/tests.py`, `CarritoSoloPorPostTests`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 58 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 58 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_db` be split into smaller, more focused modules?**
  _Cohesion score 0.019741935483870966 - nodes in this community are weakly interconnected._