# Graph Report - obsidian-vault-reinicio-2295d7  (2026-11-16)

## Corpus Check
- 299 files · ~341,851 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2371 nodes · 5536 edges · 178 communities (115 shown, 63 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 778 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ae016515`
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
- SuscripcionReposicion
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- limites.py
- clientes/tests.py
- Producto
- PROCEDURE.md
- Carrito
- productos/views.py
- DireccionEntrega
- What You Must Do When Invoked
- logistica/views.py
- clientes/services.py
- django_contrib
- DetalleHojaRuta
- pedidos/views.py
- vencer_promociones
- Command
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- pedidos/forms.py
- registrar_cargo
- EvaluacionDeRolesTests
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- clientes/models.py
- abonos/views.py
- Empleado
- distribuidora/views.py
- CuentaCorriente
- TelefonoContacto
- HojaDeRutaUXTests
- es_personal_interno
- Migración: unificar empleados
- promociones/tests.py
- Migración: métodos de pago
- PerfilUsuarioForm
- Promocion
- aplicar_attrs
- Pedido
- Barrio
- Abono
- graphify reference: extra exports and benchmark
- 🏁 Plan de Cierre — Fases 4.5 a 7
- AltaClienteValidacionesTests
- CheckoutRequiereTelefonosTests
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleadoForm
- puede_ver_nota_seguridad
- RolSincronizaGrupoTests
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
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
- pedidos/tests.py
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- MovimientoCuenta
- QA-05 Zona sin días de reparto
- AbonoForm
- FuncionesPorRolTests
- CobroManualTests
- 0013_detallehojaruta_es_venta_calle.py
- VistasCuentasTests
- QA-06 Email de producción sin configurar
- AccesoAVistasLogisticasTests
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- confirmar_pedido
- django_contrib
- 0002_bidones_recargables_y_rol_recargador.py
- 🌊 Distribuidora 3.0 / Aguadelluvia
- QA campo a campo — 12/11/2026
- TestCase
- AltaClienteConCuentaForm
- listar_clientes
- pedidos/admin.py
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- MetodoPago
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
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
- registrar_movimiento_bidon
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- Fase 3 · Logística ↔ Pedido
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- StockReservadoTests
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- BuscarClientesTests
- EditarMiPerfilTests
- VariasDireccionesTests
- OrdenDirectorioClientesTests
- VistaMovimientoBidonTests
- InicioTests
- 0003_grupos_base.py
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

## Communities (178 total, 63 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.09
Nodes (16): CodigoRecuperacionForm, IngresarUsuarioForm, NuevaContrasenaForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo() (+8 more)

### Community 1 - "django_conf"
Cohesion: 0.05
Nodes (20): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+12 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.23
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "vender_promocion"
Cohesion: 0.22
Nodes (4): consumir_saldo(), vender_promocion(), EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (33): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+25 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.08
Nodes (12): ConfiguracionCorreoForm, Meta, ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo(), es_admin() (+4 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.12
Nodes (9): 4. ❓ Decisiones a tomar antes de empezar, 6C — Pedido automático quincenal (RF-18) · ~4 h, SuscripcionForm, Meta, SuscripcionReposicion, Meta, generar_pedidos_automaticos(), PedidoAutomaticoTests (+1 more)

### Community 9 - "planta/views.py"
Cohesion: 0.07
Nodes (14): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+6 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.15
Nodes (18): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion(), editar_mi_perfil(), eliminar_direccion() (+10 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.10
Nodes (13): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+5 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.07
Nodes (24): 5A — Historial de envases (RF-08) · ~4 h, bidones_de_pedido(), botellones_por_producto(), carga_sugerida(), confirmar_entrega_en_calle(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona() (+16 more)

### Community 13 - "limites.py"
Cohesion: 0.13
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "clientes/tests.py"
Cohesion: 0.29
Nodes (4): ClienteForm, Meta, ClienteSinCuentaForm, ValidacionesClienteTests

### Community 15 - "Producto"
Cohesion: 0.10
Nodes (11): ItemCarrito, Meta, DetallePedido, Meta, CategoriaAdmin, ProductoAdmin, Categoria, Meta (+3 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.15
Nodes (14): Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-04 · ≥2 teléfonos con relación explícita, RF-06 · Catálogo por categorías, RF-09 · Promociones prepago "paga 3 lleva 4" (+6 more)

### Community 17 - "Carrito"
Cohesion: 0.18
Nodes (9): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), checkout(), solo_clientes() (+1 more)

### Community 18 - "productos/views.py"
Cohesion: 0.06
Nodes (34): buscar_productos(), con_stock_disponible(), stock_reservado_por_producto(), requiere(), decorador(), envuelta(), CategoriaForm, Meta (+26 more)

### Community 19 - "DireccionEntrega"
Cohesion: 0.17
Nodes (4): DireccionEntrega, Meta, PedidoEspontaneoTests, RF-03 · Multidirección de entrega

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "logistica/views.py"
Cohesion: 0.06
Nodes (42): Hallazgos nuevos, CamionForm, Meta, Camion, Meta, agregar_pedido_a_hoja(), fijar_pedido_de_parada(), actualizar_estado_entrega() (+34 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.13
Nodes (8): MovimientoBidon, Meta, _cliente_de_parada(), perfil_cliente_esta_vacio(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), HistorialBidonesTests

### Community 23 - "django_contrib"
Cohesion: 0.09
Nodes (18): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+10 more)

### Community 24 - "DetalleHojaRuta"
Cohesion: 0.07
Nodes (9): DetalleHojaRuta, Meta, agregar_parada(), confirmar_hoja(), renumerar_paradas(), _reubicar_extras(), ConfirmacionRegresoTests, RecorridoRepartidorTests (+1 more)

### Community 25 - "pedidos/views.py"
Cohesion: 0.11
Nodes (13): aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), listar_pedidos(), mis_pedidos() (+5 more)

### Community 26 - "vencer_promociones"
Cohesion: 0.20
Nodes (6): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, Command, vencer_promociones()

### Community 29 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.22
Nodes (10): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas (+2 more)

### Community 30 - "pedidos/forms.py"
Cohesion: 0.13
Nodes (6): fecha_estimada_para_direccion(), CheckoutForm, _etiqueta_direccion_con_fecha(), RegistrarPagoForm, CheckoutFechaEstimadaTests, registrar_pago()

### Community 31 - "registrar_cargo"
Cohesion: 0.13
Nodes (4): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, SemaforizacionTests

### Community 32 - "EvaluacionDeRolesTests"
Cohesion: 0.13
Nodes (7): puede(), EvaluacionDeRolesTests, crear_promocion(), editar_promocion(), _form_promocion(), listar_promociones(), vender_promocion()

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.22
Nodes (3): crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.26
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 36 - "clientes/models.py"
Cohesion: 0.13
Nodes (4): ZonaQuerySet, SinEliminadosManager, SinHojaEliminadaManager, limite_largo()

### Community 37 - "abonos/views.py"
Cohesion: 0.34
Nodes (6): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono()

### Community 38 - "Empleado"
Cohesion: 0.07
Nodes (12): 2. 🟠 Altos — errores funcionales, Usuario, Meta, EmpleadoAdmin, RolEmpleadoAdmin, EmpleadoForm, Meta, Empleado (+4 more)

### Community 39 - "distribuidora/views.py"
Cohesion: 0.17
Nodes (7): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, resumen_caja(), promociones_por_vencer(), resumen_dashboard()

### Community 40 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 41 - "TelefonoContacto"
Cohesion: 0.17
Nodes (5): TelefonoContactoForm, Meta, TelefonoContacto, Meta, BajaLogicaTelefonoDireccionTests

### Community 43 - "es_personal_interno"
Cohesion: 0.08
Nodes (16): roles_usuario(), Funcion, Meta, es_personal_interno(), sincronizar_grupo_empleado(), usa_panel(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió (+8 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "promociones/tests.py"
Cohesion: 0.12
Nodes (7): obtener_o_crear_cuenta(), metodo_pago_efectivo(), registrar_cobro(), CompraPromocion, Meta, revertir_consumos(), saldo_vigente()

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.18
Nodes (3): PerfilUsuarioForm, Meta, perfil_usuario()

### Community 48 - "Promocion"
Cohesion: 0.14
Nodes (8): 5B — Promociones prepago (RF-09) · ~6 h, CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta, Promocion, Meta

### Community 49 - "aplicar_attrs"
Cohesion: 0.13
Nodes (4): RegistroClienteWebForm, Meta, EditarMiPerfilForm, aplicar_attrs()

### Community 50 - "Pedido"
Cohesion: 0.16
Nodes (4): 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta

### Community 51 - "Barrio"
Cohesion: 0.15
Nodes (8): DireccionEntregaForm, Meta, DireccionRegistroForm, Meta, BarrioForm, Meta, Barrio, Meta

### Community 52 - "Abono"
Cohesion: 0.06
Nodes (9): AbonoAdmin, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests, VistasAbonosTests (+1 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.17
Nodes (8): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 7 — QA, producción y tesis 🎓, 🏁 Plan de Cierre — Fases 4.5 a 7, main()

### Community 56 - "CheckoutRequiereTelefonosTests"
Cohesion: 0.13
Nodes (3): CheckoutRequiereTelefonosTests, PagosParcialesTests, TransicionesManualesTests

### Community 57 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 62 - "clientes/forms.py"
Cohesion: 0.11
Nodes (10): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_fecha_no_futura() (+2 more)

### Community 63 - "permisos/signals.py"
Cohesion: 0.12
Nodes (7): retirar_perfil_cliente_vacio(), crear_perfil_cliente(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.20
Nodes (3): RolEmpleadoForm, Meta, BajaLogicaRolTests

### Community 67 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (5): puede_ver_nota_seguridad(), NotaDeSeguridadTests, Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 68 - "RolSincronizaGrupoTests"
Cohesion: 0.09
Nodes (4): BajaLogicaYFotoEmpleadoTests, GuardsUnificadosTests, PantallasDeRolesTests, RolSincronizaGrupoTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.40
Nodes (3): asignar(), Migration, _permisos()

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

### Community 99 - "CheckoutConSaldoTests"
Cohesion: 0.21
Nodes (3): BasePromociones, CheckoutConSaldoTests, VistasPromocionesTests

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "pedidos/tests.py"
Cohesion: 0.13
Nodes (7): _a_decimal(), firma_webhook_valida(), registrar_pago_manual(), stock_comprometido(), stock_disponible(), _firmar(), StockComprometidoTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.13
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
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

### Community 108 - "AbonoForm"
Cohesion: 0.25
Nodes (3): AbonoForm, Meta, BajaLogicaClienteTests

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.18
Nodes (10): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución, Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase (+2 more)

### Community 117 - "AccesoAVistasLogisticasTests"
Cohesion: 0.08
Nodes (4): obtener_empleado(), AccesoAVistasLogisticasTests, GruposBaseTests, ModeloEmpleadoUnicoTests

### Community 118 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 120 - "confirmar_pedido"
Cohesion: 0.25
Nodes (6): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, _cliente_puede_comprar(), confirmar_pedido()

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 123 - "🌊 Distribuidora 3.0 / Aguadelluvia"
Cohesion: 0.29
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 126 - "AltaClienteConCuentaForm"
Cohesion: 0.22
Nodes (3): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin

### Community 127 - "listar_clientes"
Cohesion: 0.19
Nodes (8): BuscarClienteForm, _columnas_ordenables(), listar_clientes(), _texto_buscable(), marcar(), Migration, _normalizar(), normalizar_texto()

### Community 128 - "pedidos/admin.py"
Cohesion: 0.36
Nodes (6): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "MetodoPago"
Cohesion: 0.11
Nodes (14): ActualizarEstadoForm, Meta, AgregarParadaForm, _etiqueta_direccion_cliente(), RutaRepartoForm, Meta, RutaReparto, Meta (+6 more)

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
Cohesion: 0.11
Nodes (5): Detalle, _bloquear_cuenta(), Cliente, Meta, eliminar_cliente()

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

### Community 151 - "Zona"
Cohesion: 0.11
Nodes (8): ZonaForm, Meta, Command, Zona, Meta, ZonaDiasRepartoTests, ZonaFormTests, restaurar_zona()

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

### Community 159 - "Fase 3 · Logística ↔ Pedido"
Cohesion: 0.25
Nodes (8): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, RF-16 · Hojas de ruta diarias, RF-17 · Agrupación automática y generación de hojas, RF-19 · Confirmación de entrega por repartidor, RNF-01 · Escalabilidad multi-camión/zona/chofer, RNF-02 · Ocultación de la nota de seguridad

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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1014 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **63 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `vender_promocion`, `cuentas/views.py`, `SuscripcionReposicion`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `clientes/tests.py`, `Producto`, `PROCEDURE.md`, `Carrito`, `DireccionEntrega`, `generar_borradores_periodo`, `logistica/views.py`, `clientes/services.py`, `DetalleHojaRuta`, `pedidos/views.py`, `registrar_movimiento_bidon`, `Command`, `pedidos/forms.py`, `registrar_cargo`, `EvaluacionDeRolesTests`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `clientes/models.py`, `Empleado`, `distribuidora/views.py`, `CuentaCorriente`, `TelefonoContacto`, `BuscarClientesTests`, `HojaDeRutaUXTests`, `OrdenDirectorioClientesTests`, `promociones/tests.py`, `VistaMovimientoBidonTests`, `Pedido`, `Abono`, `AltaClienteValidacionesTests`, `clientes/admin.py`, `clientes/forms.py`, `permisos/signals.py`, `puede_ver_nota_seguridad`, `logistica/tests.py`, `CheckoutConSaldoTests`, `pedidos/tests.py`, `FASE3_LOGISTICA.md`, `MovimientoCuenta`, `AbonoForm`, `CobroManualTests`, `VistasCuentasTests`, `AccesoAVistasLogisticasTests`, `Fase 4 · Cuentas corrientes y abonos`, `confirmar_pedido`, `TestCase`, `AltaClienteConCuentaForm`, `listar_clientes`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Are the 69 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 69 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09243697478991597 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `vender_promocion`, `QA-01 Validaciones solo en formularios`, `MetodoPago`, `ProductoForm`, `SuscripcionReposicion`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `PromocionForm`, `Carrito`, `productos/views.py`, `DireccionEntrega`, `DetalleHojaRuta`, `pedidos/views.py`, `vencer_promociones`, `Command`, `GeneracionBorradorTests`, `StockReservadoTests`, `distribuidora/views.py`, `HojaDeRutaUXTests`, `promociones/tests.py`, `InicioTests`, `Abono`, `CheckoutRequiereTelefonosTests`, `CheckoutConSaldoTests`, `pedidos/tests.py`, `AbonoForm`, `CarritoSoloPorPostTests`, `confirmar_pedido`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 58 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 58 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_conf` be split into smaller, more focused modules?**
  _Cohesion score 0.05353535353535353 - nodes in this community are weakly interconnected._