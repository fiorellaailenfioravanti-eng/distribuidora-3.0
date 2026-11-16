# Graph Report - obsidian-vault-reinicio-2295d7  (2026-11-16)

## Corpus Check
- 300 files · ~342,210 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2381 nodes · 5550 edges · 187 communities (117 shown, 70 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 779 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `754a106c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- django_conf
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
- Carrito
- productos/views.py
- DireccionEntrega
- What You Must Do When Invoked
- puede
- clientes/services.py
- django_contrib
- DetalleHojaRuta
- pedidos/views.py
- vencer_promociones
- Command
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- CheckoutFechaEstimadaTests
- registrar_cargo
- puede_alguna
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- logistica/admin.py
- requiere
- Empleado
- distribuidora/views.py
- CuentaCorriente
- TelefonoContacto
- HojaDeRutaUXTests
- es_personal_interno
- Migración: unificar empleados
- CompraPromocion
- Migración: métodos de pago
- PerfilUsuarioForm
- promociones/admin.py
- aplicar_attrs
- Pedido
- Usuario
- Abono
- graphify reference: extra exports and benchmark
- 🏁 Plan de Cierre — Fases 4.5 a 7
- RecuperarContrasenaTests
- TransicionesManualesTests
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleado
- puede_ver_nota_seguridad
- RolSincronizaGrupoTests
- graphify reference: query, path, explain
- roles.py
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
- aplicar_pago_mercadopago
- clientes/forms.py
- RolBackend
- RecargaTests
- FASE3_LOGISTICA.md
- MovimientoCuenta
- QA-05 Zona sin días de reparto
- SemaforizacionTests
- FuncionesPorRolTests
- CobroManualTests
- 0013_detallehojaruta_es_venta_calle.py
- VistasCuentasTests
- QA-06 Email de producción sin configurar
- Barrio
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- confirmar_pedido
- pedidos/views.py
- 0002_bidones_recargables_y_rol_recargador.py
- RolSincronizaGrupoTests
- QA campo a campo — 12/11/2026
- clientes/tests.py
- AltaClienteConCuentaForm
- listar_clientes
- pedidos/admin.py
- Categoria
- QA-01 Validaciones solo en formularios
- venta_calle
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- EliminarProductoTests
- {{title}}
- promociones/views.py
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
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- ZonaForm
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- StockReservadoTests
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- BuscarClientesTests
- EntregaCalleTests
- VariasDireccionesTests
- OrdenDirectorioClientesTests
- PlanificarRepartoViewTests
- ModeloEmpleadoUnicoTests
- InicioTests
- 2026-11-16
- CheckoutRequiereTelefonosTests
- QA-09 Recuperar contraseña usa vistas de clase
- VigentesQuerySet
- NuevaContrasenaForm
- 0006_corregir_ayuda_desc_seguridad.py
- 0015_numero_cliente.py
- TestCase
- productos/admin.py
- Notas

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
- `Carga y regreso del camión (sobrantes a stock)` --references--> `CargaHojaRuta`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (187 total, 70 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.09
Nodes (18): CodigoRecuperacionForm, IngresarUsuarioForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo(), recuperar_contrasena() (+10 more)

### Community 1 - "django_conf"
Cohesion: 0.05
Nodes (22): Migration, Migration, Migration, Migration, ItemCarrito, Meta, Migration, Migration (+14 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.24
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "vender_promocion"
Cohesion: 0.19
Nodes (5): consumir_saldo(), revertir_consumos(), vender_promocion(), EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (34): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+26 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.07
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.21
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.09
Nodes (13): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+5 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.11
Nodes (22): DireccionEntregaForm, Meta, MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente() (+14 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.11
Nodes (12): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+4 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.07
Nodes (27): 5A — Historial de envases (RF-08) · ~4 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja() (+19 more)

### Community 13 - "limites.py"
Cohesion: 0.14
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "logistica/views.py"
Cohesion: 0.09
Nodes (20): carga_sugerida(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), resumen_recorrido(), agregar_parada(), agregar_pedido_parada(), _cargas_confirmacion_desde_post() (+12 more)

### Community 15 - "Producto"
Cohesion: 0.10
Nodes (13): obtener_o_crear_cuenta(), DetallePedido, Meta, MetodoPago, Meta, metodo_pago_efectivo(), registrar_cobro(), stock_comprometido() (+5 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.13
Nodes (20): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-03 · Multidirección de entrega (+12 more)

### Community 17 - "Carrito"
Cohesion: 0.16
Nodes (10): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), stock_disponible(), StockComprometidoTests (+2 more)

### Community 18 - "productos/views.py"
Cohesion: 0.13
Nodes (8): buscar_productos(), con_stock_disponible(), agotados_al_final(), eliminar_producto(), _filtrar_por_categoria(), listar_productos(), ver_producto(), RF-07 · Buscador tolerante a tildes

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "puede"
Cohesion: 0.11
Nodes (23): Hallazgos nuevos, confirmar_ruta(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona(), eliminar_camion() (+15 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.15
Nodes (7): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), HistorialBidonesTests

### Community 23 - "django_contrib"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "DetalleHojaRuta"
Cohesion: 0.11
Nodes (4): confirmar_hoja(), ConfirmacionRegresoTests, InventarioCamionTests, RecorridoRepartidorTests

### Community 25 - "pedidos/views.py"
Cohesion: 0.13
Nodes (9): cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos(), pago_fallido(), pago_pendiente(), pago_qr() (+1 more)

### Community 26 - "vencer_promociones"
Cohesion: 0.29
Nodes (4): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, FASE 7 — QA, producción y tesis 🎓, Command, vencer_promociones()

### Community 29 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.20
Nodes (10): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas (+2 more)

### Community 30 - "CheckoutFechaEstimadaTests"
Cohesion: 0.20
Nodes (3): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests

### Community 31 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 32 - "puede_alguna"
Cohesion: 0.12
Nodes (5): ActualizarEstadoForm, Meta, actualizar_estado_entrega(), puede_alguna(), EvaluacionDeRolesTests

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.20
Nodes (4): ClienteSinCuentaForm, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.21
Nodes (4): clientes_frecuentes_de_zona(), construir_borrador(), pedidos_candidatos(), GeneracionBorradorTests

### Community 36 - "logistica/admin.py"
Cohesion: 0.16
Nodes (12): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+4 more)

### Community 37 - "requiere"
Cohesion: 0.19
Nodes (11): requiere(), decorador(), envuelta(), crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria() (+3 more)

### Community 38 - "Empleado"
Cohesion: 0.12
Nodes (5): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, CuentaDeRepartidorTests

### Community 39 - "distribuidora/views.py"
Cohesion: 0.14
Nodes (7): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, resumen_caja(), inicio(), resumen_dashboard()

### Community 40 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 41 - "TelefonoContacto"
Cohesion: 0.11
Nodes (6): TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente(), AltaClienteValidacionesTests

### Community 43 - "es_personal_interno"
Cohesion: 0.08
Nodes (17): asignar(), Migration, _permisos(), roles_usuario(), Funcion, Meta, es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo) (+9 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "CompraPromocion"
Cohesion: 0.25
Nodes (4): CompraPromocion, Meta, promociones_por_vencer(), listar_promociones()

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.11
Nodes (6): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, perfil_usuario(), validar_nombre()

### Community 48 - "promociones/admin.py"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 49 - "aplicar_attrs"
Cohesion: 0.17
Nodes (3): CamionForm, Meta, aplicar_attrs()

### Community 50 - "Pedido"
Cohesion: 0.12
Nodes (8): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta

### Community 51 - "Usuario"
Cohesion: 0.18
Nodes (5): 2. 🟠 Altos — errores funcionales, Usuario, Meta, EmpleadoForm, Meta

### Community 52 - "Abono"
Cohesion: 0.06
Nodes (16): AbonoAdmin, AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests (+8 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.20
Nodes (7): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, 🏁 Plan de Cierre — Fases 4.5 a 7, main()

### Community 57 - "clientes/admin.py"
Cohesion: 0.14
Nodes (8): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, DireccionEntrega, Meta

### Community 62 - "clientes/forms.py"
Cohesion: 0.14
Nodes (5): ValidadoresTests, normalizar_patente(), validar_altura(), validar_coordenadas(), validar_dni()

### Community 63 - "permisos/signals.py"
Cohesion: 0.13
Nodes (7): perfil_cliente_esta_vacio(), retirar_perfil_cliente_vacio(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 66 - "RolEmpleado"
Cohesion: 0.13
Nodes (6): RolEmpleadoForm, Meta, RolEmpleado, Meta, BajaLogicaRolTests, sincronizar_grupo_empleado()

### Community 67 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (5): puede_ver_nota_seguridad(), NotaDeSeguridadTests, Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 68 - "RolSincronizaGrupoTests"
Cohesion: 0.11
Nodes (3): BajaLogicaYFotoEmpleadoTests, GuardsUnificadosTests, PantallasDeRolesTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "roles.py"
Cohesion: 0.19
Nodes (5): es_repartidor_asignado(), obtener_empleado(), puede_operar_hoja(), puede_ver_hoja(), usa_panel()

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 73 - "HojaRuta"
Cohesion: 0.19
Nodes (3): HojaRuta, Meta, EliminarBorradorRutaTests

### Community 74 - "popups.js"
Cohesion: 0.26
Nodes (15): actualizarTope(), avisar(), cerrarAviso(), confirmar(), contenedorAvisos(), erroresDelServidor(), escapar(), etiquetaDe() (+7 more)

### Community 75 - "QA-02 Pago mayor a la deuda"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-02 Pago mayor a la deuda, Qué pasa

### Community 76 - "RecuperarContrasenaTests"
Cohesion: 0.07
Nodes (4): PerfilPersonalTests, RegistroTelefonosTests, RegistroValidacionesTests, SesionTests

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
Cohesion: 0.11
Nodes (8): HojaRutaForm, Meta, BajaLogicaCamionTests, BajaLogicaZonaTests, HojaRutaCapacidadTests, HojaRutaZonaYLimitesTests, HojaSinChoferTests, SeedDemoTests

### Community 99 - "CheckoutConSaldoTests"
Cohesion: 0.21
Nodes (3): BasePromociones, CheckoutConSaldoTests, VistasPromocionesTests

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "aplicar_pago_mercadopago"
Cohesion: 0.20
Nodes (5): aplicar_pago_mercadopago(), consultar_pago_mercadopago(), firma_webhook_valida(), pago_exitoso(), webhook_mercadopago()

### Community 102 - "clientes/forms.py"
Cohesion: 0.13
Nodes (5): RegistroUsuarioForm, Meta, EditarMiPerfilForm, solo_digitos(), validar_telefono()

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.18
Nodes (7): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Carga y regreso del camión (sobrantes a stock), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 106 - "MovimientoCuenta"
Cohesion: 0.16
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 117 - "Barrio"
Cohesion: 0.08
Nodes (14): BarrioForm, Meta, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta, Barrio, Meta, Camion (+6 more)

### Community 118 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.22
Nodes (7): Fase 4 · Cuentas corrientes y abonos, Fase 5 · Bidones y promociones prepago, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 120 - "confirmar_pedido"
Cohesion: 0.18
Nodes (8): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, checkout(), _cliente_puede_comprar(), confirmar_pedido(), saldo_vigente()

### Community 121 - "pedidos/views.py"
Cohesion: 0.11
Nodes (6): CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, suscripcion_cliente(), csrf_failure()

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "clientes/tests.py"
Cohesion: 0.06
Nodes (10): ClienteForm, Meta, AgregarDireccionTests, BajaLogicaClienteTests, BajaLogicaTelefonoDireccionTests, EditarMiPerfilTests, FiadoPremiumYExcepcionTests, NumeroClienteTests (+2 more)

### Community 126 - "AltaClienteConCuentaForm"
Cohesion: 0.18
Nodes (4): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin, validar_fecha_no_futura()

### Community 127 - "listar_clientes"
Cohesion: 0.17
Nodes (8): BuscarClienteForm, _columnas_ordenables(), listar_clientes(), _texto_buscable(), marcar(), Migration, _normalizar(), normalizar_texto()

### Community 128 - "pedidos/admin.py"
Cohesion: 0.17
Nodes (10): 4. ❓ Decisiones a tomar antes de empezar, 6C — Pedido automático quincenal (RF-18) · ~4 h, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin (+2 more)

### Community 129 - "Categoria"
Cohesion: 0.24
Nodes (5): CategoriaForm, Meta, Categoria, Meta, listar_categorias()

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "venta_calle"
Cohesion: 0.18
Nodes (5): AgregarParadaForm, botellon_por_defecto(), fecha_estimada_para_direccion(), productos_de_reparto(), venta_calle()

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

### Community 141 - "promociones/views.py"
Cohesion: 0.13
Nodes (9): PromocionForm, Meta, VenderPromocionForm, Promocion, Meta, crear_promocion(), editar_promocion(), _form_promocion() (+1 more)

### Community 142 - "cambios_sin_guardar.js"
Cohesion: 0.60
Nodes (3): campoCambio(), hayCambios(), seGuardaSolo()

### Community 143 - "abonos"
Cohesion: 0.67
Nodes (3): abonos, Notas, Relaciones

### Community 144 - "Cliente"
Cohesion: 0.08
Nodes (10): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original), _bloquear_cuenta(), Cliente (+2 more)

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

### Community 157 - "empleados"
Cohesion: 0.67
Nodes (3): empleados, Notas, Relaciones

### Community 158 - "logistica"
Cohesion: 0.67
Nodes (3): logistica, Notas, Relaciones

### Community 159 - "ZonaForm"
Cohesion: 0.43
Nodes (3): ZonaForm, Meta, ZonaFormTests

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

### Community 176 - "2026-11-16"
Cohesion: 0.29
Nodes (7): 2026-11-16, Bloqueos / dudas, Configuración, Inicio de la tienda (rehecho), Pendiente, Qué hice, Recuperar contraseña con código temporal

### Community 178 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa, Resolución

### Community 186 - "Notas"
Cohesion: 0.67
Nodes (3): Notas, pedidos, Relaciones

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1020 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **70 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/admin.py`, `vender_promocion`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `promociones/views.py`, `logistica/views.py`, `Producto`, `PROCEDURE.md`, `DireccionEntrega`, `generar_borradores_periodo`, `clientes/services.py`, `DetalleHojaRuta`, `Command`, `CheckoutFechaEstimadaTests`, `registrar_cargo`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `Empleado`, `distribuidora/views.py`, `CuentaCorriente`, `TelefonoContacto`, `BuscarClientesTests`, `EntregaCalleTests`, `OrdenDirectorioClientesTests`, `HojaDeRutaUXTests`, `PlanificarRepartoViewTests`, `Pedido`, `Abono`, `clientes/admin.py`, `permisos/signals.py`, `puede_ver_nota_seguridad`, `logistica/tests.py`, `CheckoutConSaldoTests`, `clientes/forms.py`, `FASE3_LOGISTICA.md`, `MovimientoCuenta`, `SemaforizacionTests`, `CobroManualTests`, `VistasCuentasTests`, `Barrio`, `Fase 4 · Cuentas corrientes y abonos`, `confirmar_pedido`, `pedidos/views.py`, `clientes/tests.py`, `AltaClienteConCuentaForm`, `listar_clientes`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 70 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09047619047619047 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `pedidos/admin.py`, `django_conf`, `Categoria`, `vender_promocion`, `QA-01 Validaciones solo en formularios`, `venta_calle`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `promociones/views.py`, `logistica/views.py`, `Carrito`, `productos/views.py`, `DireccionEntrega`, `DetalleHojaRuta`, `Command`, `GeneracionBorradorTests`, `requiere`, `StockReservadoTests`, `distribuidora/views.py`, `EntregaCalleTests`, `HojaDeRutaUXTests`, `InicioTests`, `CheckoutRequiereTelefonosTests`, `Abono`, `productos/admin.py`, `logistica/tests.py`, `CheckoutConSaldoTests`, `RecargaTests`, `CarritoSoloPorPostTests`, `confirmar_pedido`, `pedidos/views.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 58 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 58 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_conf` be split into smaller, more focused modules?**
  _Cohesion score 0.0473469387755102 - nodes in this community are weakly interconnected._