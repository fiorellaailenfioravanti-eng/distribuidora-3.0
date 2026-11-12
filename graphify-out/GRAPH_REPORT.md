# Graph Report - obsidian-vault-setup-9a38f1  (2026-11-12)

## Corpus Check
- 247 files · ~322,461 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 22 file(s) not represented in the graph (top: (none) 7, .css 4, .jfif 3)

## Summary
- 1979 nodes · 4705 edges · 163 communities (103 shown, 60 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 682 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f6274c77`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- django_contrib
- pedidos/views.py
- empleados/views.py
- vender_promocion
- django_db
- logistica/views.py
- cuentas/views.py
- logistica/forms.py
- PedidoAutomaticoTests
- abonos/views.py
- clientes/views.py
- Empleado
- logistica/services.py
- Producto
- productos/views.py
- seed_demo.py
- PROCEDURE.md
- Carrito
- CarritoSoloPorPostTests
- PedidoEspontaneoTests
- What You Must Do When Invoked
- base_dashboard.html
- Cliente
- logistica/admin.py
- AltaClienteConCuentaForm
- pedidos/views.py
- promociones/views.py
- QA 2026-11-12.md
- FuncionesPorRolTests
- SemaforizacionTests
- CheckoutConSaldoTests
- CuentaCorriente
- puede
- puede_ver_nota_seguridad
- django_apps
- GeneracionBorradorTests
- base_tienda.html
- 🔎 Auditoría de coherencia — Distribuidora 3.0
- PerfilUsuarioForm
- distribuidora/views.py
- registrar_cargo
- Zona
- pedidos/admin.py
- SuscripcionReposicion
- Migración: unificar empleados
- MovimientoCuenta
- Migración: métodos de pago
- PromocionForm
- CompraPromocion
- sincronizar_grupo_empleado
- 6A — Pagos parciales (RF-13) · ~4 h
- confirmar_pedido
- Command
- graphify reference: extra exports and benchmark
- PerfilPersonalTests
- VariasDireccionesTests
- PagosSegurosTests
- validadores.py
- clientes/services.py
- base.py
- DireccionEntregaForm
- AccesoAVistasLogisticasTests
- RolSincronizaGrupoTests
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- cuentas/admin.py
- TelefonoContactoForm
- Fase 6 · Pagos parciales y pedido automático
- popups.js
- QA-02 Pago mayor a la deuda
- permisos/apps.py
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
- ClientesConfig
- RegistroUsuarioForm
- RolBackend
- ✅ Control de cumplimiento de requisitos — 20/10/2026
- FASE3_LOGISTICA.md
- generar_borradores_periodo
- QA-05 Zona sin días de reparto
- Fase 4 · Cuentas corrientes y abonos
- permisos/signals.py
- Fase 5 · Bidones y promociones prepago
- 0013_detallehojaruta_es_venta_calle.py
- clientes/admin.py
- QA-06 Email de producción sin configurar
- Distribuidora 3.0 / Aquadelluvia
- buscador/apps.py
- carrito/apps.py
- QA-09 Recuperar contraseña usa vistas de clase
- listar_clientes
- logistica/apps.py
- HojaRuta
- QA campo a campo — 12/11/2026
- validar_telefono
- 0003_grupos_base.py
- obtener_o_crear_cuenta
- 0006_corregir_ayuda_desc_seguridad.py
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- aplicar_attrs
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- os
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- cuentas/apps.py
- {{title}}
- empleados/apps.py
- pedidos/apps.py
- abonos
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- autenticacion
- {{title}}
- {{date}}
- autenticacion/forms.py
- carrito
- 0004_asignar_grupo_permisos.py
- Barrio
- buscador
- clientes
- cuentas
- promociones/apps.py
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- pedidos
- productos
- promociones

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 100 edges
2. `puede()` - 91 edges
3. `Pedido` - 76 edges
4. `Producto` - 70 edges
5. `Zona` - 53 edges
6. `DireccionEntrega` - 51 edges
7. `HojaRuta` - 51 edges
8. `MetodoPago` - 47 edges
9. `Empleado` - 38 edges
10. `Command` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Funciones y roles por defecto` --references--> `cambiar_tipo_cliente()`  [INFERRED]
  notas/Roles y permisos.md → apps/clientes/views.py
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Carga y regreso del camión (sobrantes a stock)` --references--> `CargaHojaRuta`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `5D — Tests · ~2 h` --references--> `registrar_entrega()`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/logistica/services.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (163 total, 60 thin omitted)

### Community 0 - "django_contrib"
Cohesion: 0.08
Nodes (12): IngresarUsuarioForm, ingresar_usuario(), registrar_usuario(), _ya_ingresado(), roles_usuario(), Funcion, Meta, es_personal_interno() (+4 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.10
Nodes (12): CheckoutForm, RegistrarPagoForm, SuscripcionForm, Meta, cambiar_estado_pago(), cambiar_estado_pedido(), detalle_pedido(), pago_fallido() (+4 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.17
Nodes (15): RolEmpleadoForm, Meta, cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado() (+7 more)

### Community 3 - "vender_promocion"
Cohesion: 0.17
Nodes (6): consumir_saldo(), revertir_consumos(), vender_promocion(), BasePromociones, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (41): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+33 more)

### Community 5 - "logistica/views.py"
Cohesion: 0.09
Nodes (23): Camion, Meta, carga_sugerida(), envase_de_reparto(), envases_retirados_en_hoja(), registrar_regreso(), agregar_parada(), agregar_pedido_parada() (+15 more)

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "logistica/forms.py"
Cohesion: 0.10
Nodes (14): DireccionEntrega, Meta, ActualizarEstadoForm, Meta, AgregarParadaForm, BarrioForm, Meta, _etiqueta_direccion_cliente() (+6 more)

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "abonos/views.py"
Cohesion: 0.27
Nodes (8): AbonoForm, Meta, cambiar_estado_abono(), crear_abono(), editar_abono(), generar_cargos(), listar_abonos(), ver_abono()

### Community 10 - "clientes/views.py"
Cohesion: 0.08
Nodes (29): BuscarClienteForm, ClienteForm, Meta, ClienteSinCuentaForm, MovimientoBidonForm, TelefonoContacto, Meta, agregar_direccion() (+21 more)

### Community 11 - "Empleado"
Cohesion: 0.08
Nodes (13): 2. 🟠 Altos — errores funcionales, Usuario, EmpleadoAdmin, RolEmpleadoAdmin, EmpleadoForm, Meta, Empleado, Meta (+5 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.08
Nodes (20): 5A — Historial de envases (RF-08) · ~4 h, DetalleHojaRuta, Meta, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), confirmar_entrega_en_calle(), crear_hoja_borrador() (+12 more)

### Community 13 - "Producto"
Cohesion: 0.15
Nodes (5): MetodoPago, Meta, Producto, VenderPromocionForm, H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 14 - "productos/views.py"
Cohesion: 0.06
Nodes (21): requiere(), CategoriaAdmin, ProductoAdmin, CategoriaForm, Meta, ProductoForm, Meta, Categoria (+13 more)

### Community 15 - "seed_demo.py"
Cohesion: 0.16
Nodes (4): obtener_o_crear_cuenta(), firma_webhook_valida(), metodo_pago_efectivo(), _firmar()

### Community 16 - "PROCEDURE.md"
Cohesion: 0.15
Nodes (13): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-06 · Catálogo por categorías, RF-11 · Pedido con fecha, total, estado y desglose, RF-16 · Hojas de ruta diarias (+5 more)

### Community 17 - "Carrito"
Cohesion: 0.14
Nodes (11): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), stock_disponible(), StockComprometidoTests (+3 more)

### Community 18 - "CarritoSoloPorPostTests"
Cohesion: 0.18
Nodes (3): ItemCarrito, Meta, CarritoSoloPorPostTests

### Community 19 - "PedidoEspontaneoTests"
Cohesion: 0.09
Nodes (5): confirmar_hoja(), resumen_recorrido(), ConfirmacionRegresoTests, PedidoEspontaneoTests, RecorridoRepartidorTests

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.12
Nodes (17): Hallazgos nuevos, actualizar_estado_entrega(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona(), eliminar_camion() (+9 more)

### Community 22 - "Cliente"
Cohesion: 0.14
Nodes (3): Cliente, Meta, AgregarDireccionTests

### Community 23 - "logistica/admin.py"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "AltaClienteConCuentaForm"
Cohesion: 0.18
Nodes (4): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin, validar_fecha_no_futura()

### Community 25 - "pedidos/views.py"
Cohesion: 0.12
Nodes (9): 4. ♻️ Redundancias, _a_decimal(), aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), registrar_cobro(), registrar_pago_manual(), pago_exitoso() (+1 more)

### Community 26 - "promociones/views.py"
Cohesion: 0.12
Nodes (10): CompraPromocion, Meta, Promocion, Meta, promociones_por_vencer(), crear_promocion(), editar_promocion(), _form_promocion() (+2 more)

### Community 31 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 32 - "puede"
Cohesion: 0.10
Nodes (11): es_admin(), es_repartidor_asignado(), puede(), puede_alguna(), puede_operar_hoja(), puede_ver_hoja(), decorador(), envuelta() (+3 more)

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, AutenticacionConfig, ProductosConfig

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.18
Nodes (4): clientes_frecuentes_de_zona(), construir_borrador(), fecha_estimada_para_direccion(), GeneracionBorradorTests

### Community 36 - "base_tienda.html"
Cohesion: 0.22
Nodes (5): listar_pedidos(), mis_pedidos(), listar_productos(), ver_producto(), inicio()

### Community 37 - "🔎 Auditoría de coherencia — Distribuidora 3.0"
Cohesion: 0.24
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, 3. 🟡 Medios, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, cerrar_sesion() (+1 more)

### Community 38 - "PerfilUsuarioForm"
Cohesion: 0.18
Nodes (3): PerfilUsuarioForm, Meta, validar_nombre()

### Community 39 - "distribuidora/views.py"
Cohesion: 0.17
Nodes (6): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, resumen_caja(), resumen_dashboard()

### Community 40 - "registrar_cargo"
Cohesion: 0.23
Nodes (3): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests

### Community 41 - "Zona"
Cohesion: 0.24
Nodes (3): Zona, Meta, ZonaDiasRepartoTests

### Community 42 - "pedidos/admin.py"
Cohesion: 0.11
Nodes (10): HojaDeRutaUXTests, DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido (+2 more)

### Community 43 - "SuscripcionReposicion"
Cohesion: 0.12
Nodes (13): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, 5D — Tests · ~2 h, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)** (+5 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "MovimientoCuenta"
Cohesion: 0.22
Nodes (3): MovimientoCuenta, Meta, ReglaFiadoTests

### Community 48 - "CompraPromocion"
Cohesion: 0.32
Nodes (5): CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, ConsumoPromocion, Meta

### Community 49 - "sincronizar_grupo_empleado"
Cohesion: 0.21
Nodes (5): retirar_perfil_cliente_vacio(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 50 - "6A — Pagos parciales (RF-13) · ~4 h"
Cohesion: 0.12
Nodes (9): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 4. ❓ Decisiones a tomar antes de empezar, 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, 6C — Pedido automático quincenal (RF-18) · ~4 h, Pedido (+1 more)

### Community 51 - "confirmar_pedido"
Cohesion: 0.25
Nodes (6): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, _cliente_puede_comprar(), confirmar_pedido()

### Community 52 - "Command"
Cohesion: 0.05
Nodes (10): AbonoAdmin, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests, VistasAbonosTests (+2 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "PerfilPersonalTests"
Cohesion: 0.08
Nodes (4): PerfilPersonalTests, RecuperarContrasenaTests, RegistroTelefonosTests, SesionTests

### Community 55 - "VariasDireccionesTests"
Cohesion: 0.06
Nodes (7): BuscarClientesTests, EditarMiPerfilTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests, ValidacionesClienteTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "PagosSegurosTests"
Cohesion: 0.06
Nodes (8): _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), CheckoutFechaEstimadaTests, CheckoutRequiereTelefonosTests, CobroManualTests, PagosParcialesTests, PagosSegurosTests, TransicionesManualesTests

### Community 62 - "validadores.py"
Cohesion: 0.20
Nodes (4): normalizar_patente(), solo_digitos(), validar_altura(), validar_dni()

### Community 63 - "clientes/services.py"
Cohesion: 0.15
Nodes (9): MovimientoBidon, Meta, _cliente_de_parada(), perfil_cliente_esta_vacio(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada(), SuscripcionReposicion (+1 more)

### Community 66 - "DireccionEntregaForm"
Cohesion: 0.29
Nodes (3): DireccionEntregaForm, Meta, validar_coordenadas()

### Community 68 - "RolSincronizaGrupoTests"
Cohesion: 0.12
Nodes (3): GuardsUnificadosTests, PantallasDeRolesTests, RolSincronizaGrupoTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.40
Nodes (3): asignar(), Migration, _permisos()

### Community 71 - "cuentas/admin.py"
Cohesion: 0.50
Nodes (3): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline

### Community 73 - "Fase 6 · Pagos parciales y pedido automático"
Cohesion: 0.33
Nodes (6): Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, RF-04 · ≥2 teléfonos con relación explícita, RF-12 · Carrito no excede stock, RF-13 · Pagos parciales y múltiples métodos, RF-18 · Pedido automático quincenal

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
Cohesion: 0.07
Nodes (11): ZonaForm, Meta, botellones_por_producto(), entregados_por_producto(), inventario_camion(), HojaRutaCapacidadTests, HojaSinChoferTests, InventarioCamionTests (+3 more)

### Community 99 - "Verificar cambios — Distribuidora 3.0"
Cohesion: 0.18
Nodes (8): 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0, 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.19
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "✅ Control de cumplimiento de requisitos — 20/10/2026"
Cohesion: 0.25
Nodes (6): Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Detalle, Hallazgos y decisiones nuevas, Resumen (control original)

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.22
Nodes (5): Arquitectura visual dual: Tienda vs Dashboard, Carga y regreso del camión (sobrantes a stock), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "generar_borradores_periodo"
Cohesion: 0.13
Nodes (4): Command, generar_borradores_periodo(), pedidos_candidatos(), GeneracionQuincenalTests

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 108 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 110 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 114 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa

### Community 117 - "Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aquadelluvia, graphify, graphify

### Community 120 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa

### Community 121 - "listar_clientes"
Cohesion: 0.21
Nodes (6): buscar_productos(), marcar(), Migration, _normalizar(), normalizar_texto(), RF-07 · Buscador tolerante a tildes

### Community 123 - "HojaRuta"
Cohesion: 0.23
Nodes (4): HojaRutaForm, Meta, HojaRuta, Meta

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "aplicar_attrs"
Cohesion: 0.15
Nodes (4): EditarMiPerfilForm, CamionForm, Meta, aplicar_attrs()

### Community 134 - "QA-03 El envase vacío se vende en la tienda"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aquadelluvia"
Cohesion: 0.12
Nodes (14): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aquadelluvia, 📚 Documentación del proyecto, 🧪 QA, Notas (+6 more)

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

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

### Community 148 - "autenticacion/forms.py"
Cohesion: 0.15
Nodes (3): NuevaContrasenaForm, RecuperarContrasenaForm, perfil_usuario()

### Community 149 - "carrito"
Cohesion: 0.67
Nodes (3): carrito, Notas, Relaciones

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 151 - "Barrio"
Cohesion: 0.10
Nodes (16): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+8 more)

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

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 829 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **60 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/views.py`, `vender_promocion`, `logistica/views.py`, `cuentas/views.py`, `abonos/views.py`, `clientes/views.py`, `Empleado`, `logistica/services.py`, `Producto`, `seed_demo.py`, `PROCEDURE.md`, `Carrito`, `PedidoEspontaneoTests`, `AltaClienteConCuentaForm`, `promociones/views.py`, `SemaforizacionTests`, `CuentaCorriente`, `puede_ver_nota_seguridad`, `GeneracionBorradorTests`, `distribuidora/views.py`, `registrar_cargo`, `pedidos/admin.py`, `MovimientoCuenta`, `sincronizar_grupo_empleado`, `6A — Pagos parciales (RF-13) · ~4 h`, `confirmar_pedido`, `Command`, `VariasDireccionesTests`, `PagosSegurosTests`, `clientes/services.py`, `AccesoAVistasLogisticasTests`, `logistica/tests.py`, `✅ Control de cumplimiento de requisitos — 20/10/2026`, `generar_borradores_periodo`, `Fase 4 · Cuentas corrientes y abonos`, `permisos/signals.py`, `Fase 5 · Bidones y promociones prepago`, `clientes/admin.py`, `obtener_o_crear_cuenta`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 62 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `django_contrib` be split into smaller, more focused modules?**
  _Cohesion score 0.08403361344537816 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `pedidos/views.py`, `vender_promocion`, `QA-01 Validaciones solo en formularios`, `logistica/views.py`, `logistica/forms.py`, `PedidoAutomaticoTests`, `abonos/views.py`, `logistica/services.py`, `productos/views.py`, `seed_demo.py`, `Carrito`, `CarritoSoloPorPostTests`, `PedidoEspontaneoTests`, `GeneracionBorradorTests`, `base_tienda.html`, `distribuidora/views.py`, `pedidos/admin.py`, `SuscripcionReposicion`, `PromocionForm`, `confirmar_pedido`, `Command`, `PagosSegurosTests`, `clientes/services.py`, `logistica/tests.py`, `listar_clientes`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Pedido` (e.g. with `2. 🟠 Altos — errores funcionales` and `5B — Promociones prepago (RF-09) · ~6 h`) actually correct?**
  _`Pedido` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10227272727272728 - nodes in this community are weakly interconnected._