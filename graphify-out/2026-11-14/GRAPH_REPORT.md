# Graph Report - admin-user-password-913bce  (2026-11-14)

## Corpus Check
- 273 files · ~328,638 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 22 file(s) not represented in the graph (top: (none) 7, .css 4, .jfif 3)

## Summary
- 2100 nodes · 4964 edges · 166 communities (103 shown, 63 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 705 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f9a55050`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- django_contrib
- pedidos/views.py
- empleados/views.py
- vender_promocion
- django_db
- registrar_regreso_ruta
- cuentas/views.py
- ProductoForm
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- Empleado
- logistica/services.py
- limites.py
- Producto
- Producto
- PROCEDURE.md
- Carrito
- CarritoSoloPorPostTests
- PedidoEspontaneoTests
- What You Must Do When Invoked
- logistica/views.py
- Cliente
- logistica/admin.py
- ClienteForm
- registrar_pago_manual
- PromocionForm
- QA 2026-11-12.md
- Command
- CheckoutFechaEstimadaTests
- CheckoutConSaldoTests
- clientes/services.py
- EvaluacionDeRolesTests
- listar_clientes
- django_apps
- GeneracionBorradorTests
- permisos/tests.py
- registrar_cobro
- PerfilUsuarioForm
- roles.py
- Command
- CheckoutRequiereTelefonosTests
- HojaDeRutaUXTests
- vencer_promociones
- Migración: unificar empleados
- promociones/views.py
- Migración: métodos de pago
- generar_cargos_mensuales
- CompraPromocion
- VistasAbonosTests
- Pedido
- SuscripcionReposicion
- abonos/views.py
- graphify reference: extra exports and benchmark
- PerfilPersonalTests
- clientes/tests.py
- PagosSegurosTests
- clientes/forms.py
- permisos/signals.py
- base.py
- clientes/admin.py
- puede_ver_nota_seguridad
- Usuario
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- GuardsUnificadosTests
- TelefonoContacto
- FuncionesPorRolTests
- popups.js
- QA-02 Pago mayor a la deuda
- BuscarClientesTests
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- README.md
- extraction-spec.md
- logistica/tests.py
- Verificar cambios — Distribuidora 3.0
- QA-04 Abono con costo 0
- pedidos/admin.py
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- HojaRuta
- QA-05 Zona sin días de reparto
- EditarMiPerfilTests
- 🌊 Distribuidora 3.0 / Aquadelluvia
- VariasDireccionesTests
- 0013_detallehojaruta_es_venta_calle.py
- CobroManualTests
- QA-06 Email de producción sin configurar
- ModeloEmpleadoUnicoTests
- Abono
- CuentaDeRepartidorTests
- QA-09 Recuperar contraseña usa vistas de clase
- normalizar_texto
- 0002_bidones_recargables_y_rol_recargador.py
- RolEmpleado
- QA campo a campo — 12/11/2026
- MetodoPago
- 0003_grupos_base.py
- 0007_marcar_botellones.py
- 0006_corregir_ayuda_desc_seguridad.py
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- logistica/forms.py
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- Verificar cambios — Distribuidora 3.0
- {{title}}
- Promocion
- cambios_sin_guardar.js
- abonos
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- autenticacion
- {{title}}
- {{date}}
- Command
- carrito
- 0004_asignar_grupo_permisos.py
- Zona
- buscador
- clientes
- cuentas
- SuscripcionForm
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- pedidos
- productos
- promociones
- permisos/models.py
- tabla_ordenable.js

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 102 edges
2. `puede()` - 91 edges
3. `Pedido` - 78 edges
4. `Producto` - 78 edges
5. `Zona` - 55 edges
6. `DireccionEntrega` - 51 edges
7. `HojaRuta` - 51 edges
8. `MetodoPago` - 47 edges
9. `Empleado` - 40 edges
10. `Command` - 38 edges

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

## Communities (166 total, 63 thin omitted)

### Community 0 - "django_contrib"
Cohesion: 0.14
Nodes (13): IngresarUsuarioForm, cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario(), _ya_ingresado(), roles_usuario(), es_personal_interno() (+5 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.08
Nodes (14): 3. 🟡 Medios, RegistrarPagoForm, pago_en_curso(), cambiar_estado_pago(), cambiar_estado_pedido(), confirmar_pago_qr(), detalle_pedido(), listar_pedidos() (+6 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.16
Nodes (16): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+8 more)

### Community 3 - "vender_promocion"
Cohesion: 0.19
Nodes (5): consumir_saldo(), revertir_consumos(), vender_promocion(), EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (43): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+35 more)

### Community 5 - "registrar_regreso_ruta"
Cohesion: 0.18
Nodes (7): carga_sugerida(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), _productos_para_carga(), registrar_regreso_ruta(), _regreso_desde_post()

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.09
Nodes (6): ProductoForm, Meta, AltaProductoTests, CategoriasPanelTests, EliminarProductoTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.23
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.07
Nodes (14): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+6 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.13
Nodes (19): MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+11 more)

### Community 11 - "Empleado"
Cohesion: 0.32
Nodes (4): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta

### Community 12 - "logistica/services.py"
Cohesion: 0.08
Nodes (25): 5A — Historial de envases (RF-08) · ~4 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja() (+17 more)

### Community 13 - "limites.py"
Cohesion: 0.17
Nodes (9): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+1 more)

### Community 14 - "Producto"
Cohesion: 0.08
Nodes (23): ItemCarrito, Meta, CategoriaAdmin, ProductoAdmin, CategoriaForm, Meta, Categoria, Meta (+15 more)

### Community 15 - "Producto"
Cohesion: 0.12
Nodes (4): Migration, obtener_o_crear_cuenta(), saldo_vigente(), limite_largo()

### Community 16 - "PROCEDURE.md"
Cohesion: 0.11
Nodes (25): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba (+17 more)

### Community 17 - "Carrito"
Cohesion: 0.15
Nodes (10): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), checkout(), _cliente_puede_comprar() (+2 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "logistica/views.py"
Cohesion: 0.06
Nodes (42): Hallazgos nuevos, AgregarParadaForm, botellon_por_defecto(), clientes_frecuentes_de_zona(), pedidos_candidatos(), productos_de_reparto(), actualizar_estado_entrega(), agregar_parada() (+34 more)

### Community 23 - "logistica/admin.py"
Cohesion: 0.09
Nodes (18): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+10 more)

### Community 24 - "ClienteForm"
Cohesion: 0.20
Nodes (4): ClienteForm, Meta, ClienteSinCuentaForm, _ValidarDatosPersonalesMixin

### Community 25 - "registrar_pago_manual"
Cohesion: 0.15
Nodes (7): 1. 🔴 Críticos — seguridad y dinero, _a_decimal(), aplicar_pago_mercadopago(), consultar_pago_mercadopago(), registrar_pago_manual(), pago_exitoso(), webhook_mercadopago()

### Community 29 - "CheckoutFechaEstimadaTests"
Cohesion: 0.18
Nodes (4): CheckoutForm, _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests

### Community 30 - "CheckoutConSaldoTests"
Cohesion: 0.21
Nodes (3): BasePromociones, CheckoutConSaldoTests, VistasPromocionesTests

### Community 31 - "clientes/services.py"
Cohesion: 0.16
Nodes (8): MovimientoBidon, Meta, _cliente_de_parada(), perfil_cliente_esta_vacio(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), retirar_perfil_cliente_vacio(), sincronizar_bidones_de_parada()

### Community 33 - "listar_clientes"
Cohesion: 0.17
Nodes (6): AltaClienteConCuentaForm, Meta, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), guardar_telefonos_dinamicos()

### Community 34 - "django_apps"
Cohesion: 0.05
Nodes (13): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, CuentasConfig, EmpleadosConfig, LogisticaConfig (+5 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.22
Nodes (3): construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 36 - "permisos/tests.py"
Cohesion: 0.12
Nodes (5): RutaRepartoForm, Meta, RutaReparto, Meta, AccesoAVistasLogisticasTests

### Community 37 - "registrar_cobro"
Cohesion: 0.14
Nodes (13): 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 🔎 Auditoría de coherencia — Distribuidora 3.0, ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase (+5 more)

### Community 38 - "PerfilUsuarioForm"
Cohesion: 0.10
Nodes (5): NuevaContrasenaForm, PerfilUsuarioForm, Meta, RecuperarContrasenaForm, validar_nombre()

### Community 39 - "roles.py"
Cohesion: 0.08
Nodes (11): clientes_morosos(), resumen_morosidad(), es_admin(), requiere(), decorador(), envuelta(), sincronizar_grupo_empleado(), usa_panel() (+3 more)

### Community 40 - "Command"
Cohesion: 0.05
Nodes (13): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, CuentaCorriente, Meta, MovimientoCuenta, Meta, registrar_cargo() (+5 more)

### Community 41 - "CheckoutRequiereTelefonosTests"
Cohesion: 0.13
Nodes (3): CheckoutRequiereTelefonosTests, PagosParcialesTests, TransicionesManualesTests

### Community 43 - "vencer_promociones"
Cohesion: 0.29
Nodes (4): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, FASE 7 — QA, producción y tesis 🎓, Command, vencer_promociones()

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "promociones/views.py"
Cohesion: 0.17
Nodes (6): promociones_por_vencer(), crear_promocion(), editar_promocion(), _form_promocion(), listar_promociones(), vender_promocion()

### Community 47 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 48 - "CompraPromocion"
Cohesion: 0.16
Nodes (7): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, CompraPromocion, Meta, ConsumoPromocion, Meta

### Community 50 - "Pedido"
Cohesion: 0.11
Nodes (9): 2. 🟠 Altos — errores funcionales, A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta (+1 more)

### Community 51 - "SuscripcionReposicion"
Cohesion: 0.18
Nodes (9): 4. ❓ Decisiones a tomar antes de empezar, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, SuscripcionReposicion, Meta (+1 more)

### Community 52 - "abonos/views.py"
Cohesion: 0.27
Nodes (8): AbonoForm, Meta, cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono()

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "PerfilPersonalTests"
Cohesion: 0.08
Nodes (4): PerfilPersonalTests, RecuperarContrasenaTests, RegistroTelefonosTests, SesionTests

### Community 55 - "clientes/tests.py"
Cohesion: 0.12
Nodes (5): AgregarDireccionTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests, ValidacionesClienteTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.19
Nodes (3): firma_webhook_valida(), _firmar(), PagosSegurosTests

### Community 62 - "clientes/forms.py"
Cohesion: 0.07
Nodes (13): BuscarClienteForm, DireccionEntregaForm, Meta, EditarMiPerfilForm, ValidadoresTests, aplicar_attrs(), normalizar_patente(), solo_digitos() (+5 more)

### Community 63 - "permisos/signals.py"
Cohesion: 0.13
Nodes (6): crear_perfil_cliente(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos(), RF-01 · Registro con ≥2 celulares

### Community 66 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 67 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (5): puede_ver_nota_seguridad(), NotaDeSeguridadTests, Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 68 - "Usuario"
Cohesion: 0.23
Nodes (3): EmpleadoForm, Meta, RolSincronizaGrupoTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.40
Nodes (3): asignar(), Migration, _permisos()

### Community 72 - "TelefonoContacto"
Cohesion: 0.25
Nodes (4): TelefonoContactoForm, Meta, TelefonoContacto, Meta

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
Cohesion: 0.05
Nodes (16): DireccionEntrega, Meta, Barrio, Meta, confirmar_hoja(), generar_borradores_periodo(), ConfirmacionRegresoTests, EntregaCalleTests (+8 more)

### Community 99 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "pedidos/admin.py"
Cohesion: 0.25
Nodes (8): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, PagoPedido, Meta

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.21
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (6): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.22
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 109 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.25
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aquadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa

### Community 118 - "Abono"
Cohesion: 0.16
Nodes (4): AbonoAdmin, Abono, Meta, RF-05 · Clientes Normal/Premium; fiado solo Premium

### Community 119 - "CuentaDeRepartidorTests"
Cohesion: 0.18
Nodes (3): Usuario, Meta, CuentaDeRepartidorTests

### Community 120 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 123 - "RolEmpleado"
Cohesion: 0.33
Nodes (4): 7. 🗺️ Cómo entra en el plan, Decisiones nuevas, RolEmpleado, Meta

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "MetodoPago"
Cohesion: 0.10
Nodes (9): DetallePedido, Meta, MetodoPago, Meta, metodo_pago_efectivo(), resumen_caja(), stock_comprometido(), stock_disponible() (+1 more)

### Community 127 - "0007_marcar_botellones.py"
Cohesion: 0.60
Nodes (3): marcar(), Migration, _normalizar()

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "logistica/forms.py"
Cohesion: 0.10
Nodes (12): ActualizarEstadoForm, Meta, BarrioForm, Meta, CamionForm, Meta, _etiqueta_direccion_cliente(), HojaRutaForm (+4 more)

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.14
Nodes (11): Notas, permisos, Relaciones, Notas, planta, Reglas, Relaciones, Dónde está en el código (+3 more)

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 139 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

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

### Community 149 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 151 - "Zona"
Cohesion: 0.12
Nodes (7): ZonaForm, Meta, Command, Zona, Meta, ZonaDiasRepartoTests, ZonaFormTests

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

### Community 159 - "pedidos"
Cohesion: 0.67
Nodes (3): Notas, pedidos, Relaciones

### Community 160 - "productos"
Cohesion: 0.67
Nodes (3): Notas, productos, Relaciones

### Community 161 - "promociones"
Cohesion: 0.67
Nodes (3): Notas, promociones, Relaciones

### Community 165 - "tabla_ordenable.js"
Cohesion: 0.83
Nodes (3): iconoPara(), prepararTabla(), valorCelda()

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 885 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **63 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/views.py`, `vender_promocion`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `Producto`, `Producto`, `PROCEDURE.md`, `Carrito`, `PedidoEspontaneoTests`, `logistica/views.py`, `ClienteForm`, `Command`, `CheckoutFechaEstimadaTests`, `CheckoutConSaldoTests`, `clientes/services.py`, `listar_clientes`, `GeneracionBorradorTests`, `permisos/tests.py`, `roles.py`, `Command`, `HojaDeRutaUXTests`, `promociones/views.py`, `generar_cargos_mensuales`, `VistasAbonosTests`, `Pedido`, `SuscripcionReposicion`, `abonos/views.py`, `clientes/tests.py`, `clientes/forms.py`, `permisos/signals.py`, `clientes/admin.py`, `puede_ver_nota_seguridad`, `BuscarClientesTests`, `logistica/tests.py`, `✅ Control de cumplimiento de requisitos — 20/10/2026`, `FASE3_LOGISTICA.md`, `CobroManualTests`, `Abono`, `CuentaDeRepartidorTests`, `MetodoPago`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 63 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `django_contrib` be split into smaller, more focused modules?**
  _Cohesion score 0.13756613756613756 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `pedidos/views.py`, `vender_promocion`, `QA-01 Validaciones solo en formularios`, `registrar_regreso_ruta`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `logistica/services.py`, `Producto`, `Carrito`, `CarritoSoloPorPostTests`, `PedidoEspontaneoTests`, `logistica/views.py`, `PromocionForm`, `Command`, `CheckoutConSaldoTests`, `GeneracionBorradorTests`, `roles.py`, `CheckoutRequiereTelefonosTests`, `HojaDeRutaUXTests`, `generar_cargos_mensuales`, `VistasAbonosTests`, `SuscripcionReposicion`, `abonos/views.py`, `logistica/tests.py`, `Abono`, `normalizar_texto`, `MetodoPago`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `Pedido` (e.g. with `2. 🟠 Altos — errores funcionales` and `5B — Promociones prepago (RF-09) · ~6 h`) actually correct?**
  _`Pedido` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08305647840531562 - nodes in this community are weakly interconnected._