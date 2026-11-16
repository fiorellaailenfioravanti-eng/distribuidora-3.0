# Graph Report - admin-user-password-913bce  (2026-11-14)

## Corpus Check
- 288 files · ~334,908 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 22 file(s) not represented in the graph (top: (none) 7, .css 4, .jfif 3)

## Summary
- 2231 nodes · 5213 edges · 167 communities (108 shown, 59 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 724 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f9a55050`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- pedidos/urls.py
- empleados/views.py
- vender_promocion
- django_db
- configuracion/views.py
- cuentas/views.py
- requiere
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- django_db_models_deletion
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
- aplicar_attrs
- pedidos/views.py
- DireccionEntregaForm
- Command
- logistica/admin.py
- base_tienda.html
- registrar_cargo
- EvaluacionDeRolesTests
- listar_clientes
- django_apps
- GeneracionBorradorTests
- Empleado
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- EmpleadoForm
- CompraPromocion
- CuentaCorriente
- DireccionEntrega
- HojaDeRutaUXTests
- roles.py
- Migración: unificar empleados
- promociones/views.py
- Migración: métodos de pago
- generar_cargos_mensuales
- CompraPromocion
- VistasAbonosTests
- Pedido
- confirmar_pedido
- abonos/views.py
- graphify reference: extra exports and benchmark
- PerfilPersonalTests
- AltaClienteValidacionesTests
- PagosSegurosTests
- clientes/forms.py
- permisos/signals.py
- base.py
- SemaforizacionTests
- puede_ver_nota_seguridad
- Usuario
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- GuardsUnificadosTests
- Qué hice
- FuncionesPorRolTests
- popups.js
- QA-02 Pago mayor a la deuda
- RegistroTelefonosTests
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
- MovimientoCuenta
- QA-05 Zona sin días de reparto
- AbonoForm
- clientes/signals.py
- autenticacion/migrations/0001_initial.py
- 0013_detallehojaruta_es_venta_calle.py
- VistasCuentasTests
- QA-06 Email de producción sin configurar
- ModeloEmpleadoUnicoTests
- Abono
- cuentas/admin.py
- QA-09 Recuperar contraseña usa vistas de clase
- permisos/views.py
- 0002_bidones_recargables_y_rol_recargador.py
- Command
- QA campo a campo — 12/11/2026
- CLAUDE.md
- 0011_renumerar_paradas.py
- 0007_marcar_botellones.py
- 0006_corregir_ayuda_desc_seguridad.py
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- Barrio
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- os
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- Verificar cambios — Distribuidora 3.0
- {{title}}
- 0012_completar_pedidos_de_paradas.py
- cambios_sin_guardar.js
- abonos
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
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
- SuscripcionForm
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- pedidos
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 109 edges
2. `puede()` - 94 edges
3. `Pedido` - 78 edges
4. `Producto` - 78 edges
5. `Zona` - 55 edges
6. `DireccionEntrega` - 51 edges
7. `HojaRuta` - 51 edges
8. `MetodoPago` - 47 edges
9. `Empleado` - 45 edges
10. `Command` - 38 edges

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

## Communities (167 total, 59 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.10
Nodes (11): IngresarUsuarioForm, NuevaContrasenaForm, RecuperarContrasenaForm, cerrar_sesion(), ingresar_usuario(), perfil_usuario(), registrar_usuario(), _ya_ingresado() (+3 more)

### Community 1 - "pedidos/urls.py"
Cohesion: 0.19
Nodes (5): cambiar_estado_pago(), cambiar_estado_pedido(), pago_fallido(), pago_qr(), redirigir_a_origen()

### Community 2 - "empleados/views.py"
Cohesion: 0.15
Nodes (16): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+8 more)

### Community 3 - "vender_promocion"
Cohesion: 0.09
Nodes (11): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, Command, consumir_saldo(), revertir_consumos(), vencer_promociones(), vender_promocion(), BasePromociones, CheckoutConSaldoTests (+3 more)

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (26): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+18 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.06
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "requiere"
Cohesion: 0.06
Nodes (23): requiere(), decorador(), envuelta(), CategoriaForm, Meta, ProductoForm, Meta, Categoria (+15 more)

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.05
Nodes (17): AbonoAdmin, DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables() (+9 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.12
Nodes (19): MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+11 more)

### Community 11 - "django_db_models_deletion"
Cohesion: 0.06
Nodes (17): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+9 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.07
Nodes (24): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), botellones_por_producto(), confirmar_entrega_en_calle() (+16 more)

### Community 13 - "limites.py"
Cohesion: 0.14
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "Producto"
Cohesion: 0.21
Nodes (5): MetodoPago, Meta, Producto, Meta, H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.10
Nodes (26): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba (+18 more)

### Community 17 - "Carrito"
Cohesion: 0.24
Nodes (8): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), stock_disponible(), solo_clientes()

### Community 18 - "CarritoSoloPorPostTests"
Cohesion: 0.18
Nodes (3): ItemCarrito, Meta, CarritoSoloPorPostTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "logistica/views.py"
Cohesion: 0.06
Nodes (43): Hallazgos nuevos, CamionForm, Meta, Camion, Meta, botellon_por_defecto(), envase_de_reparto(), productos_de_reparto() (+35 more)

### Community 22 - "Cliente"
Cohesion: 0.09
Nodes (7): ClienteForm, Meta, ClienteSinCuentaForm, _bloquear_cuenta(), Cliente, Meta, ValidacionesClienteTests

### Community 23 - "logistica/admin.py"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 25 - "pedidos/views.py"
Cohesion: 0.09
Nodes (16): CheckoutForm, RegistrarPagoForm, PagoPedido, Meta, _a_decimal(), aplicar_pago_mercadopago(), consultar_pago_mercadopago(), firma_webhook_valida() (+8 more)

### Community 26 - "DireccionEntregaForm"
Cohesion: 0.12
Nodes (7): DireccionEntregaForm, Meta, DireccionRegistroForm, Meta, ValidadoresTests, validar_altura(), validar_coordenadas()

### Community 28 - "Command"
Cohesion: 0.06
Nodes (15): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, MovimientoBidon, Meta (+7 more)

### Community 29 - "logistica/admin.py"
Cohesion: 0.18
Nodes (12): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+4 more)

### Community 30 - "base_tienda.html"
Cohesion: 0.25
Nodes (4): listar_pedidos(), mis_pedidos(), listar_productos(), inicio()

### Community 31 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 32 - "EvaluacionDeRolesTests"
Cohesion: 0.15
Nodes (6): puede(), EvaluacionDeRolesTests, Dónde está en el código, Funciones y roles por defecto, Reglas que no dependen de las casillas, Roles y permisos

### Community 33 - "listar_clientes"
Cohesion: 0.14
Nodes (8): BuscarClienteForm, _columnas_ordenables(), crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), listar_clientes(), _texto_buscable(), normalizar_texto()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.16
Nodes (5): carga_sugerida(), clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 36 - "Empleado"
Cohesion: 0.05
Nodes (16): 2. 🟠 Altos — errores funcionales, Usuario, Meta, EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta, RolEmpleado (+8 more)

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.16
Nodes (10): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, buscar_productos() (+2 more)

### Community 38 - "EmpleadoForm"
Cohesion: 0.11
Nodes (7): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, EmpleadoForm, Meta, validar_nombre()

### Community 39 - "CompraPromocion"
Cohesion: 0.12
Nodes (8): perfil_cliente_esta_vacio(), clientes_morosos(), resumen_morosidad(), CompraPromocion, Meta, promociones_por_vencer(), listar_promociones(), resumen_dashboard()

### Community 40 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 41 - "DireccionEntrega"
Cohesion: 0.07
Nodes (10): 4. ♻️ Redundancias, DireccionEntrega, Meta, TelefonoContacto, Meta, AgregarDireccionTests, CheckoutRequiereTelefonosTests, PagosParcialesTests (+2 more)

### Community 43 - "roles.py"
Cohesion: 0.23
Nodes (5): roles_usuario(), es_personal_interno(), usa_panel(), 2. Revisar convenciones del proyecto en lo que cambió, 2. Revisar convenciones del proyecto en lo que cambió

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "promociones/views.py"
Cohesion: 0.13
Nodes (9): PromocionForm, Meta, VenderPromocionForm, Promocion, Meta, crear_promocion(), editar_promocion(), _form_promocion() (+1 more)

### Community 47 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 48 - "CompraPromocion"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 50 - "Pedido"
Cohesion: 0.06
Nodes (27): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 0. Qué falta (resumen), 4. ❓ Decisiones a tomar antes de empezar, 5. 🔗 Dependencias y archivos compartidos, 5B — Promociones prepago (RF-09) · ~6 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, 6A — Pagos parciales (RF-13) · ~4 h (+19 more)

### Community 51 - "confirmar_pedido"
Cohesion: 0.25
Nodes (4): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, checkout(), _cliente_puede_comprar(), confirmar_pedido()

### Community 52 - "abonos/views.py"
Cohesion: 0.38
Nodes (6): cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono()

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "PerfilPersonalTests"
Cohesion: 0.10
Nodes (3): PerfilPersonalTests, RecuperarContrasenaTests, SesionTests

### Community 55 - "AltaClienteValidacionesTests"
Cohesion: 0.05
Nodes (7): AltaClienteValidacionesTests, BuscarClientesTests, EditarMiPerfilTests, FiadoPremiumYExcepcionTests, OrdenDirectorioClientesTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.09
Nodes (5): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, CobroManualTests, PagosSegurosTests

### Community 62 - "clientes/forms.py"
Cohesion: 0.12
Nodes (8): TelefonoContactoForm, Meta, _ValidarDatosPersonalesMixin, normalizar_patente(), solo_digitos(), validar_dni(), validar_fecha_no_futura(), validar_telefono()

### Community 63 - "permisos/signals.py"
Cohesion: 0.21
Nodes (6): retirar_perfil_cliente_vacio(), sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 68 - "Usuario"
Cohesion: 0.13
Nodes (3): BajaLogicaYFotoEmpleadoTests, PantallasDeRolesTests, RolSincronizaGrupoTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.18
Nodes (5): asignar(), Migration, _permisos(), Funcion, Meta

### Community 72 - "Qué hice"
Cohesion: 0.18
Nodes (11): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Panel y navegación, Pendiente (+3 more)

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
Nodes (14): HojaRutaForm, Meta, HojaRuta, Meta, confirmar_hoja(), ConfirmacionRegresoTests, GeneracionQuincenalTests, HojaRutaCapacidadTests (+6 more)

### Community 99 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.40
Nodes (4): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "pedidos/admin.py"
Cohesion: 0.21
Nodes (9): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido, Meta (+1 more)

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.14
Nodes (5): RegistroUsuarioForm, Meta, RegistroValidacionesTests, AltaClienteConCuentaForm, Meta

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.18
Nodes (8): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (6): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 106 - "MovimientoCuenta"
Cohesion: 0.22
Nodes (3): MovimientoCuenta, Meta, ReglaFiadoTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 108 - "AbonoForm"
Cohesion: 0.25
Nodes (3): AbonoForm, Meta, BajaLogicaClienteTests

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 117 - "ModeloEmpleadoUnicoTests"
Cohesion: 0.13
Nodes (3): obtener_empleado(), GruposBaseTests, ModeloEmpleadoUnicoTests

### Community 118 - "Abono"
Cohesion: 0.21
Nodes (3): Abono, Meta, RF-05 · Clientes Normal/Premium; fiado solo Premium

### Community 119 - "cuentas/admin.py"
Cohesion: 0.50
Nodes (3): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

### Community 120 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 127 - "0007_marcar_botellones.py"
Cohesion: 0.38
Nodes (3): marcar(), Migration, _normalizar()

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "Barrio"
Cohesion: 0.18
Nodes (8): ActualizarEstadoForm, Meta, AgregarParadaForm, BarrioForm, Meta, _etiqueta_direccion_cliente(), Barrio, Meta

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.11
Nodes (14): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aquadelluvia, 📚 Documentación del proyecto, 🧪 QA, Notas (+6 more)

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
Cohesion: 0.13
Nodes (9): ZonaForm, Meta, Zona, Meta, ZonaDiasRepartoTests, ZonaFormTests, direcciones_sin_zona(), editar_zona() (+1 more)

### Community 152 - "buscador"
Cohesion: 0.50
Nodes (3): buscador, Notas, Relaciones

### Community 153 - "clientes"
Cohesion: 0.67
Nodes (3): clientes, Notas, Relaciones

### Community 154 - "cuentas"
Cohesion: 0.67
Nodes (3): cuentas, Notas, Relaciones

### Community 155 - "SuscripcionForm"
Cohesion: 0.33
Nodes (3): SuscripcionForm, Meta, suscripcion_cliente()

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

### Community 164 - "Validaciones por campo"
Cohesion: 0.67
Nodes (3): Límites de caracteres (base de datos), Teléfonos en las altas, Validaciones por campo

### Community 165 - "tabla_ordenable.js"
Cohesion: 0.83
Nodes (3): iconoPara(), prepararTabla(), valorCelda()

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 958 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **59 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `vender_promocion`, `cuentas/views.py`, `planta/views.py`, `clientes/views.py`, `logistica/services.py`, `Producto`, `Producto`, `PROCEDURE.md`, `PedidoEspontaneoTests`, `logistica/views.py`, `pedidos/views.py`, `SuscripcionForm`, `Command`, `registrar_cargo`, `listar_clientes`, `GeneracionBorradorTests`, `Empleado`, `CompraPromocion`, `CuentaCorriente`, `DireccionEntrega`, `HojaDeRutaUXTests`, `promociones/views.py`, `generar_cargos_mensuales`, `VistasAbonosTests`, `Pedido`, `confirmar_pedido`, `AltaClienteValidacionesTests`, `PagosSegurosTests`, `clientes/forms.py`, `permisos/signals.py`, `SemaforizacionTests`, `puede_ver_nota_seguridad`, `logistica/tests.py`, `FASE3_LOGISTICA.md`, `MovimientoCuenta`, `AbonoForm`, `clientes/signals.py`, `VistasCuentasTests`, `Abono`?**
  _High betweenness centrality (0.164) - this node is a cross-community bridge._
- **Are the 68 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 68 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09655172413793103 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `vender_promocion`, `QA-01 Validaciones solo en formularios`, `requiere`, `PedidoAutomaticoTests`, `planta/views.py`, `logistica/services.py`, `Producto`, `Carrito`, `CarritoSoloPorPostTests`, `PedidoEspontaneoTests`, `logistica/views.py`, `pedidos/views.py`, `Command`, `base_tienda.html`, `GeneracionBorradorTests`, `🔎 Auditoría de coherencia — Distribuidora 3.0`, `CompraPromocion`, `DireccionEntrega`, `HojaDeRutaUXTests`, `promociones/views.py`, `generar_cargos_mensuales`, `VistasAbonosTests`, `Pedido`, `confirmar_pedido`, `logistica/tests.py`, `pedidos/admin.py`, `AbonoForm`, `Abono`, `permisos/views.py`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `Pedido` (e.g. with `2. 🟠 Altos — errores funcionales` and `5B — Promociones prepago (RF-09) · ~6 h`) actually correct?**
  _`Pedido` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Should `vender_promocion` be split into smaller, more focused modules?**
  _Cohesion score 0.09102564102564102 - nodes in this community are weakly interconnected._