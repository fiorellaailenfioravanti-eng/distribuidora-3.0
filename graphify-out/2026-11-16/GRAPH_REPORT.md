# Graph Report - obsidian-vault-reinicio-2295d7  (2026-11-16)

## Corpus Check
- 301 files · ~345,166 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2436 nodes · 5646 edges · 188 communities (105 shown, 83 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 799 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cdd29eb8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- pedidos/views.py
- empleados/views.py
- promociones/tests.py
- django_db
- configuracion/views.py
- cuentas/views.py
- ProductoForm
- PedidoAutomaticoTests
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- seed_demo.py
- requiere
- clientes/models.py
- PROCEDURE.md
- Carrito
- buscador/views.py
- recortar_textos
- What You Must Do When Invoked
- puede
- clientes/services.py
- Pedido
- registrar_cargo
- pedidos/forms.py
- pedidos/tests.py
- CuentaCorriente
- 🏁 Plan de Cierre — Fases 4.5 a 7
- Command
- MovimientoCuenta
- EvaluacionDeRolesTests
- crear_cliente_con_cuenta
- django_apps
- GeneracionBorradorTests
- AccesoAVistasLogisticasTests
- base_tienda.html
- Empleado
- DetallePedido
- GenerarEnvaseTests
- Qué hice
- HojaDeRutaUXTests
- es_personal_interno
- Migración: unificar empleados
- ModeloEmpleadoUnicoTests
- 0003_sembrar_metodos_pago.py
- PerfilUsuarioForm
- logistica/admin.py
- aplicar_attrs
- ConfiguracionCorreoTests
- PagosSegurosTests
- Abono
- graphify reference: extra exports and benchmark
- RolSincronizaGrupoTests
- FuncionesPorRolTests
- django_contrib
- clientes/admin.py
- clientes/forms.py
- permisos/signals.py
- base.py
- RolEmpleadoForm
- DireccionEntregaForm
- BajaLogicaYFotoEmpleadoTests
- graphify reference: query, path, explain
- 0007_funciones_por_defecto.py
- RolEmpleado
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
- MetodoPago
- RegistroUsuarioForm
- RolBackend
- GuardsUnificadosTests
- FASE3_LOGISTICA.md
- BajaLogicaClienteTests
- QA-05 Zona sin días de reparto
- CobroManualTests
- puede_ver_nota_seguridad
- EnvaseForm
- 0013_detallehojaruta_es_venta_calle.py
- StockReservadoTests
- QA-06 Email de producción sin configurar
- VistasCuentasTests
- RF-05 · Clientes Normal/Premium; fiado solo Premium
- CarritoSoloPorPostTests
- permisos/apps.py
- InicioTests
- 0002_bidones_recargables_y_rol_recargador.py
- NuevaContrasenaForm
- QA campo a campo — 12/11/2026
- Producto
- AltaClienteConCuentaForm
- listar_clientes
- ItemCarrito
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- ClientesConfig
- carrito.md
- QA-07 Labels sin for en varios templates
- 🌊 Distribuidora 3.0 / Aguadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- EliminarProductoTests
- {{title}}
- DetalleHojaRuta
- cambios_sin_guardar.js
- abonos
- Cliente
- autenticacion
- {{title}}
- {{date}}
- Command
- CLAUDE.md
- 0004_asignar_grupo_permisos.py
- configuracion
- buscador
- clientes
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
- C-9 — Gastos por proveedor (RF-20)
- empleados
- logistica
- planta
- productos
- promociones
- Validaciones por campo
- tabla_ordenable.js
- TelefonoContacto
- 0008_remove_empleado_rol_remove_empleado_usuario_and_more.py
- 0003_grupos_base.py
- 0006_corregir_ayuda_desc_seguridad.py
- VariasDireccionesTests
- buscador/apps.py
- carrito/apps.py
- configuracion/apps.py
- cuentas/apps.py
- clientes/tests.py
- empleados/apps.py
- logistica/apps.py
- pedidos/apps.py
- DireccionEntrega
- productos/apps.py
- promociones/apps.py
- Usuario
- OrdenDirectorioClientesTests
- 0015_numero_cliente.py

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 113 edges
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
- `Correo de recuperación de contraseña` --references--> `ConfiguracionCorreo`  [INFERRED]
  notas/apps/configuracion.md → apps/configuracion/models.py
- `FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**` --references--> `Empleado`  [INFERRED]
  .agents/PLAN_CIERRE.md → apps/empleados/models.py
- `Días de reparto por zona → fecha estimada` --references--> `Zona`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/models.py
- `Ventas y paradas agregadas en la calle` --references--> `venta_calle()`  [INFERRED]
  .agents/FASE3_LOGISTICA.md → apps/logistica/views.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flujo de reparto (Fase 3)** — apps_logistica_views_planificar_reparto, apps_logistica_views_confirmar_ruta, apps_logistica_views_actualizar_estado_entrega, apps_logistica_views_registrar_regreso_ruta, apps_logistica_views_venta_calle [INFERRED 0.85]

## Communities (188 total, 83 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.11
Nodes (14): CodigoRecuperacionForm, IngresarUsuarioForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), recuperar_codigo(), recuperar_contrasena() (+6 more)

### Community 1 - "pedidos/views.py"
Cohesion: 0.08
Nodes (19): 1. 🔴 Críticos — seguridad y dinero, CheckoutForm, consultar_pago_mercadopago(), cambiar_estado_pago(), cambiar_estado_pedido(), checkout(), _cliente_puede_comprar(), confirmar_pago_qr() (+11 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.23
Nodes (15): cambiar_estado_empleado(), crear_empleado(), crear_rol(), editar_empleado(), editar_rol(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol() (+7 more)

### Community 3 - "promociones/tests.py"
Cohesion: 0.15
Nodes (6): consumir_saldo(), revertir_consumos(), vender_promocion(), CheckoutConSaldoTests, EscenarioAceptacionTests, ReglasDeSaldoTests

### Community 4 - "django_db"
Cohesion: 0.02
Nodes (52): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+44 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.11
Nodes (8): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, configuracion(), probar_correo(), es_admin()

### Community 6 - "cuentas/views.py"
Cohesion: 0.20
Nodes (9): CargoCuentaForm, PagoCuentaForm, cuenta_de_cliente(), _cuentas_con_morosidad(), listar_cuentas(), registrar_cargo(), registrar_pago(), ver_cuenta() (+1 more)

### Community 7 - "ProductoForm"
Cohesion: 0.10
Nodes (6): ProductoForm, Meta, AltaProductoTests, CatalogoAgotadosAlFinalTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "PedidoAutomaticoTests"
Cohesion: 0.20
Nodes (3): Command, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.06
Nodes (15): AbonoAdmin, DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, guardar_recarga() (+7 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.13
Nodes (19): MovimientoBidonForm, agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), _contexto_suscripcion(), editar_cliente(), editar_direccion(), editar_mi_perfil() (+11 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.09
Nodes (13): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+5 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.07
Nodes (31): 5A — Historial de envases (RF-08) · ~4 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, _etiqueta_direccion_cliente(), agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido() (+23 more)

### Community 13 - "seed_demo.py"
Cohesion: 0.08
Nodes (15): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, obtener_o_crear_cuenta(), metodo_pago_efectivo(), registrar_cobro(), CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, Command (+7 more)

### Community 14 - "requiere"
Cohesion: 0.12
Nodes (17): requiere(), decorador(), envuelta(), crear_categoria(), crear_producto(), editar_categoria(), editar_producto(), eliminar_categoria() (+9 more)

### Community 15 - "clientes/models.py"
Cohesion: 0.12
Nodes (4): VigentesQuerySet, SinEliminadosManager, limite_largo(), H-10 · Suite de tests parcial (faltan carrito y buscador)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.12
Nodes (25): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 4 · Cuentas corrientes y abonos, Fase 5 · Bidones y promociones prepago, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba (+17 more)

### Community 17 - "Carrito"
Cohesion: 0.28
Nodes (7): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), solo_clientes()

### Community 18 - "buscador/views.py"
Cohesion: 0.15
Nodes (8): buscar_productos(), con_stock_disponible(), stock_reservado_por_producto(), agotados_al_final(), Notas, pedidos, Relaciones, RF-07 · Buscador tolerante a tildes

### Community 19 - "recortar_textos"
Cohesion: 0.13
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "puede"
Cohesion: 0.06
Nodes (47): Hallazgos nuevos, CamionForm, Meta, Camion, Meta, actualizar_estado_entrega(), agregar_parada(), agregar_pedido_parada() (+39 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.23
Nodes (6): MovimientoBidon, Meta, _cliente_de_parada(), recalcular_saldo_bidones(), registrar_movimiento_bidon(), sincronizar_bidones_de_parada()

### Community 23 - "Pedido"
Cohesion: 0.08
Nodes (17): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), 4. ❓ Decisiones a tomar antes de empezar, 5B — Promociones prepago (RF-09) · ~6 h, 6A — Pagos parciales (RF-13) · ~4 h, 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6C — Pedido automático quincenal (RF-18) · ~4 h (+9 more)

### Community 24 - "registrar_cargo"
Cohesion: 0.14
Nodes (4): registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests, SemaforizacionTests

### Community 25 - "pedidos/forms.py"
Cohesion: 0.11
Nodes (7): fecha_estimada_para_direccion(), _etiqueta_direccion_con_fecha(), metodos_pago_checkout_web(), RegistrarPagoForm, SuscripcionForm, Meta, CheckoutFechaEstimadaTests

### Community 26 - "pedidos/tests.py"
Cohesion: 0.12
Nodes (11): PagoPedido, Meta, _a_decimal(), aplicar_pago_mercadopago(), firma_webhook_valida(), pago_en_curso(), registrar_pago_manual(), resumen_caja() (+3 more)

### Community 28 - "CuentaCorriente"
Cohesion: 0.17
Nodes (3): CuentaCorriente, Meta, RF-14 · Semaforización de deuda

### Community 29 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.12
Nodes (15): 3. 🟡 Medios, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, 0. Qué falta (resumen) (+7 more)

### Community 31 - "MovimientoCuenta"
Cohesion: 0.16
Nodes (6): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, ReglaFiadoTests

### Community 33 - "crear_cliente_con_cuenta"
Cohesion: 0.20
Nodes (4): ClienteSinCuentaForm, crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta()

### Community 34 - "django_apps"
Cohesion: 0.20
Nodes (3): AbonosConfig, AutenticacionConfig, PlantaConfig

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.21
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), GeneracionBorradorTests

### Community 37 - "base_tienda.html"
Cohesion: 0.23
Nodes (5): mis_pedidos(), listar_productos(), ver_producto(), inicio(), Inicio de la tienda (rehecho)

### Community 38 - "Empleado"
Cohesion: 0.15
Nodes (3): Empleado, Meta, CuentaDeRepartidorTests

### Community 39 - "DetallePedido"
Cohesion: 0.25
Nodes (8): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido, Meta

### Community 41 - "Qué hice"
Cohesion: 0.18
Nodes (11): 2026-11-16, Baja lógica desde los listados de empleados y clientes, Bloqueos / dudas, Configuración, Envases asociados (nuevo), Ficha del cliente más simple, Más tarde, Pendiente (+3 more)

### Community 43 - "es_personal_interno"
Cohesion: 0.11
Nodes (13): perfil_usuario(), roles_usuario(), es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo), 2. Revisar convenciones del proyecto en lo que cambió, 3. Actualizar documentación y grafo, 4. Informe final, Verificar cambios — Distribuidora 3.0 (+5 more)

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.15
Nodes (5): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, validar_nombre()

### Community 48 - "logistica/admin.py"
Cohesion: 0.10
Nodes (15): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+7 more)

### Community 49 - "aplicar_attrs"
Cohesion: 0.14
Nodes (4): DireccionRegistroForm, Meta, EditarMiPerfilForm, aplicar_attrs()

### Community 52 - "Abono"
Cohesion: 0.07
Nodes (15): AbonoForm, Meta, Command, Abono, Meta, generar_cargos_mensuales(), CostoPreferencialTests, FacturacionTests (+7 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 57 - "clientes/admin.py"
Cohesion: 0.21
Nodes (6): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline

### Community 62 - "clientes/forms.py"
Cohesion: 0.11
Nodes (9): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_fecha_no_futura() (+1 more)

### Community 63 - "permisos/signals.py"
Cohesion: 0.19
Nodes (6): retirar_perfil_cliente_vacio(), sincronizar_grupo_empleado(), _sincronizar(), sincronizar_grupo_al_cambiar_rol(), sincronizar_grupo_al_guardar_empleado(), sincronizar_permisos_grupos()

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.20
Nodes (3): RolEmpleadoForm, Meta, BajaLogicaRolTests

### Community 67 - "DireccionEntregaForm"
Cohesion: 0.25
Nodes (3): DireccionEntregaForm, Meta, FichaDomiciliosTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "0007_funciones_por_defecto.py"
Cohesion: 0.18
Nodes (5): asignar(), Migration, _permisos(), Funcion, Meta

### Community 71 - "RolEmpleado"
Cohesion: 0.29
Nodes (4): EmpleadoAdmin, RolEmpleadoAdmin, RolEmpleado, Meta

### Community 72 - "Qué hice"
Cohesion: 0.17
Nodes (12): 2026-11-14, Bloqueos / dudas, Clientes y empleados, Configuración, Logística, Límites de caracteres en la base de datos, Más tarde, Panel y navegación (+4 more)

### Community 73 - "HojaRuta"
Cohesion: 0.15
Nodes (5): HojaRuta, Meta, generar_borradores_periodo(), pedidos_candidatos(), GeneracionQuincenalTests

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
Cohesion: 0.04
Nodes (27): AgregarParadaForm, BarrioForm, Meta, HojaRutaForm, Meta, RutaRepartoForm, Meta, ZonaForm (+19 more)

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "MetodoPago"
Cohesion: 0.10
Nodes (6): MetodoPago, Meta, CheckoutRequiereTelefonosTests, PagosParcialesTests, StockComprometidoTests, TransicionesManualesTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.16
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.20
Nodes (6): Arquitectura visual dual: Tienda vs Dashboard, Bidón retornable (entrega lleno, retira vacío), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle, RF-08 · Control de envases prestados

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 109 - "puede_ver_nota_seguridad"
Cohesion: 0.16
Nodes (4): _ficha_de_parada(), _link_mapa(), puede_ver_nota_seguridad(), NotaDeSeguridadTests

### Community 110 - "EnvaseForm"
Cohesion: 0.14
Nodes (6): bidones_retornables(), CategoriaForm, Meta, EnvaseForm, Categoria, Meta

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "Producto"
Cohesion: 0.05
Nodes (20): clientes_morosos(), resumen_morosidad(), bidones_recargables(), resumen_stock(), Producto, Meta, PromocionForm, Meta (+12 more)

### Community 126 - "AltaClienteConCuentaForm"
Cohesion: 0.20
Nodes (3): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin

### Community 127 - "listar_clientes"
Cohesion: 0.17
Nodes (8): BuscarClienteForm, _columnas_ordenables(), listar_clientes(), _texto_buscable(), marcar(), Migration, _normalizar(), normalizar_texto()

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 134 - "carrito.md"
Cohesion: 0.22
Nodes (7): carrito, Notas, Relaciones, Arreglo propuesto, Cómo reproducir, QA-03 El envase vacío se vende en la tienda, Qué pasa

### Community 135 - "QA-07 Labels sin for en varios templates"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-07 Labels sin for en varios templates, Qué pasa

### Community 137 - "🌊 Distribuidora 3.0 / Aguadelluvia"
Cohesion: 0.11
Nodes (14): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA, Notas (+6 more)

### Community 138 - "QA-08 DNI de empleado y cliente no se cruzan"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-08 DNI de empleado y cliente no se cruzan, Qué pasa

### Community 140 - "{{title}}"
Cohesion: 0.33
Nodes (5): Consecuencias, Contexto, Decisión, Opciones, {{title}}

### Community 141 - "DetalleHojaRuta"
Cohesion: 0.08
Nodes (9): ActualizarEstadoForm, Meta, CargaHojaRuta, Meta, DetalleHojaRuta, Meta, EntregaCalleTests, Carga y regreso del camión (sobrantes a stock) (+1 more)

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

### Community 149 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 150 - "0004_asignar_grupo_permisos.py"
Cohesion: 0.67
Nodes (3): asignar(), _grupo_por_nombre(), Migration

### Community 151 - "configuracion"
Cohesion: 0.50
Nodes (4): configuracion, Correo de recuperación de contraseña, Notas, Relaciones

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
Cohesion: 0.33
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa, Resolución

### Community 157 - "empleados"
Cohesion: 0.67
Nodes (3): empleados, Notas, Relaciones

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
Cohesion: 0.09
Nodes (7): TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente(), AltaClienteValidacionesTests, RF-01 · Registro con ≥2 celulares

### Community 177 - "clientes/tests.py"
Cohesion: 0.05
Nodes (11): ClienteForm, Meta, AgregarDireccionTests, BajaLogicaTelefonoDireccionTests, EditarMiPerfilTests, EnlaceGoogleMapsTests, FiadoPremiumYExcepcionTests, HistorialBidonesTests (+3 more)

### Community 182 - "DireccionEntrega"
Cohesion: 0.07
Nodes (9): DireccionEntrega, Meta, confirmar_hoja(), resumen_recorrido(), ConfirmacionRegresoTests, InventarioCamionTests, PedidoEspontaneoTests, RecorridoRepartidorTests (+1 more)

### Community 189 - "Usuario"
Cohesion: 0.18
Nodes (5): 2. 🟠 Altos — errores funcionales, Usuario, Meta, EmpleadoForm, Meta

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1056 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **83 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `pedidos/views.py`, `promociones/tests.py`, `cuentas/views.py`, `clientes/views.py`, `logistica/services.py`, `seed_demo.py`, `DetalleHojaRuta`, `clientes/models.py`, `PROCEDURE.md`, `puede`, `clientes/services.py`, `Pedido`, `registrar_cargo`, `pedidos/forms.py`, `pedidos/tests.py`, `CuentaCorriente`, `Command`, `MovimientoCuenta`, `crear_cliente_con_cuenta`, `GeneracionBorradorTests`, `AccesoAVistasLogisticasTests`, `Empleado`, `TelefonoContacto`, `HojaDeRutaUXTests`, `clientes/tests.py`, `Abono`, `DireccionEntrega`, `clientes/admin.py`, `OrdenDirectorioClientesTests`, `clientes/forms.py`, `permisos/signals.py`, `DireccionEntregaForm`, `HojaRuta`, `logistica/tests.py`, `BuscarClientesTests`, `FASE3_LOGISTICA.md`, `BajaLogicaClienteTests`, `CobroManualTests`, `puede_ver_nota_seguridad`, `VistasCuentasTests`, `RF-05 · Clientes Normal/Premium; fiado solo Premium`, `Producto`, `AltaClienteConCuentaForm`, `listar_clientes`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Are the 72 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 72 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1103448275862069 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `ItemCarrito`, `pedidos/views.py`, `promociones/tests.py`, `QA-01 Validaciones solo en formularios`, `ProductoForm`, `PedidoAutomaticoTests`, `planta/views.py`, `EliminarProductoTests`, `logistica/services.py`, `seed_demo.py`, `DetalleHojaRuta`, `clientes/models.py`, `requiere`, `Carrito`, `buscador/views.py`, `Pedido`, `pedidos/tests.py`, `Command`, `GeneracionBorradorTests`, `base_tienda.html`, `DetallePedido`, `GenerarEnvaseTests`, `HojaDeRutaUXTests`, `Abono`, `DireccionEntrega`, `logistica/tests.py`, `MetodoPago`, `EnvaseForm`, `StockReservadoTests`, `CarritoSoloPorPostTests`, `InicioTests`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 65 INFERRED edges - model-reasoned connections that need verification._
- **Should `pedidos/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08309178743961353 - nodes in this community are weakly interconnected._