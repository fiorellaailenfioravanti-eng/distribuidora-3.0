# Graph Report - vault-envases-generator-668120  (2026-11-16)

## Corpus Check
- 298 files · ~343,479 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 28 file(s) not represented in the graph (top: (none) 7, .canvas 5, .base 5)

## Summary
- 2396 nodes · 5583 edges · 180 communities (119 shown, 61 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 788 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `71c9e4f1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- autenticacion/views.py
- django_conf
- empleados/views.py
- Command
- django_db
- configuracion/views.py
- CuentaCorriente
- ProductoForm
- SuscripcionReposicion
- planta/views.py
- clientes/views.py
- recuperacion.py
- logistica/services.py
- limites.py
- productos/views.py
- Producto
- PROCEDURE.md
- Carrito
- base_tienda.html
- DireccionEntrega
- What You Must Do When Invoked
- base_dashboard.html
- clientes/services.py
- django_contrib
- aplicar_pago_mercadopago
- pedidos/views.py
- RecorridoRepartidorTests
- Command
- RolEmpleado
- RegistrarPagoForm
- ver_ruta
- puede
- listar_clientes
- django_apps
- GeneracionBorradorTests
- logistica/models.py
- CompraPromocion
- Empleado
- distribuidora/views.py
- generar_cargos_mensuales
- GenerarEnvaseTests
- HojaDeRutaUXTests
- autenticacion/tests.py
- Migración: unificar empleados
- seed_demo.py
- Migración: métodos de pago
- PerfilUsuarioForm
- DetalleHojaRuta
- aplicar_attrs
- Pedido
- ver_cliente
- Abono
- graphify reference: extra exports and benchmark
- 🏁 Plan de Cierre — Fases 4.5 a 7
- clientes/tests.py
- MetodoPago
- TelefonoContacto
- clientes/forms.py
- BajaLogicaYFotoEmpleadoTests
- base.py
- RolEmpleadoForm
- CobroManualTests
- Usuario
- graphify reference: query, path, explain
- es_personal_interno
- pedidos/forms.py
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
- permisos/tests.py
- QA-04 Abono con costo 0
- PagosSegurosTests
- RegistroUsuarioForm
- RolBackend
- editar_mi_perfil
- FASE3_LOGISTICA.md
- registrar_cargo
- QA-05 Zona sin días de reparto
- GuardsUnificadosTests
- FuncionesPorRolTests
- EnvaseForm
- 0013_detallehojaruta_es_venta_calle.py
- VistasCuentasTests
- QA-06 Email de producción sin configurar
- Usuario
- Fase 4 · Cuentas corrientes y abonos
- CarritoSoloPorPostTests
- pedidos/views.py
- PedidoEspontaneoTests
- 0002_bidones_recargables_y_rol_recargador.py
- productos/views.py
- QA campo a campo — 12/11/2026
- promociones/views.py
- AltaClienteConCuentaForm
- django_shortcuts
- DetallePedido
- 0005_quitar_perfil_cliente_del_personal.py
- QA-01 Validaciones solo en formularios
- logistica/views.py
- QA-03 El envase vacío se vende en la tienda
- QA-07 Labels sin for en varios templates
- os
- 🌊 Distribuidora 3.0 / Aquadelluvia
- QA-08 DNI de empleado y cliente no se cruzan
- ClienteForm
- {{title}}
- PerfilPersonalTests
- cambios_sin_guardar.js
- abonos
- Cliente
- autenticacion
- {{title}}
- {{date}}
- editar_rol
- carrito
- 0004_asignar_grupo_permisos.py
- Zona
- buscador
- clientes
- cuentas
- QA-09 Recuperar contraseña usa vistas de clase
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
- 🌊 Distribuidora 3.0 / Aguadelluvia
- 0006_corregir_ayuda_desc_seguridad.py
- agregar_pedido_parada
- Fase 5 · Bidones y promociones prepago
- ActualizarEstadoForm
- Notas
- InicioTests
- 0003_grupos_base.py
- Qué hice
- VigentesQuerySet

## God Nodes (most connected - your core abstractions)
1. `Cliente` - 110 edges
2. `puede()` - 102 edges
3. `Producto` - 89 edges
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

## Communities (180 total, 61 thin omitted)

### Community 0 - "autenticacion/views.py"
Cohesion: 0.10
Nodes (15): IngresarUsuarioForm, RecuperarContrasenaForm, buscar_usuario(), cerrar_sesion(), ingresar_usuario(), perfil_usuario(), recuperar_codigo(), recuperar_contrasena() (+7 more)

### Community 1 - "django_conf"
Cohesion: 0.05
Nodes (20): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+12 more)

### Community 2 - "empleados/views.py"
Cohesion: 0.31
Nodes (12): cambiar_estado_empleado(), crear_empleado(), editar_empleado(), eliminar_empleado(), eliminar_rol(), _funciones_por_rol(), listar_empleados(), listar_roles() (+4 more)

### Community 3 - "Command"
Cohesion: 0.09
Nodes (12): 5C — Caducidad a 30 días corridos (RF-10) · ~2 h, FASE 7 — QA, producción y tesis 🎓, Command, consumir_saldo(), revertir_consumos(), vencer_promociones(), vender_promocion(), BasePromociones (+4 more)

### Community 4 - "django_db"
Cohesion: 0.03
Nodes (32): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+24 more)

### Community 5 - "configuracion/views.py"
Cohesion: 0.07
Nodes (13): ConfiguracionCorreoForm, Meta, conexion_y_remitente(), ConfiguracionCorreo, Meta, ConfiguracionCorreoTests, configuracion(), probar_correo() (+5 more)

### Community 6 - "CuentaCorriente"
Cohesion: 0.07
Nodes (19): A-D6 — ¿El fiado es sólo Premium o admite excepciones? → **Decidido: (b)**, ▶️ Actualización (20/10/2026, después del control), Cobertura de tests por requisito (checklist §9 de PROCEDURE), ✅ Control de cumplimiento de requisitos — 20/10/2026, Cómo se reparte en el plan, Hallazgos y decisiones nuevas, Resumen (control original), CargoCuentaForm (+11 more)

### Community 7 - "ProductoForm"
Cohesion: 0.12
Nodes (5): ProductoForm, Meta, AltaProductoTests, CategoriasPanelTests, ProductoFormValidacionesTests

### Community 8 - "SuscripcionReposicion"
Cohesion: 0.14
Nodes (7): 4. ❓ Decisiones a tomar antes de empezar, 6C — Pedido automático quincenal (RF-18) · ~4 h, Command, SuscripcionReposicion, Meta, generar_pedidos_automaticos(), PedidoAutomaticoTests

### Community 9 - "planta/views.py"
Cohesion: 0.06
Nodes (14): DetalleRecargaInline, RecargaBidonesAdmin, DetalleRecarga, Meta, RecargaBidones, Meta, bidones_recargables(), guardar_recarga() (+6 more)

### Community 10 - "clientes/views.py"
Cohesion: 0.27
Nodes (12): agregar_direccion(), agregar_telefono(), cambiar_tipo_cliente(), editar_cliente(), editar_direccion(), eliminar_cliente(), eliminar_direccion(), eliminar_telefono() (+4 more)

### Community 11 - "recuperacion.py"
Cohesion: 0.11
Nodes (12): CodigoRecuperacion, Meta, cerrar_recuperacion(), codigo_verificado(), crear_codigo(), enmascarar_email(), enviar_correo(), _hash() (+4 more)

### Community 12 - "logistica/services.py"
Cohesion: 0.09
Nodes (18): Command, agregar_parada(), agregar_pedido_a_hoja(), bidones_de_pedido(), confirmar_entrega_en_calle(), crear_hoja_borrador(), crear_venta_calle(), direccion_en_zona() (+10 more)

### Community 13 - "limites.py"
Cohesion: 0.13
Nodes (12): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration (+4 more)

### Community 14 - "productos/views.py"
Cohesion: 0.15
Nodes (13): requiere(), decorador(), envuelta(), CategoriaForm, Meta, Categoria, Meta, crear_categoria() (+5 more)

### Community 15 - "Producto"
Cohesion: 0.10
Nodes (9): ItemCarrito, Meta, CategoriaAdmin, ProductoAdmin, Producto, Meta, CatalogoAgotadosAlFinalTests, limite_largo() (+1 more)

### Community 16 - "PROCEDURE.md"
Cohesion: 0.13
Nodes (19): Fase 1 · Desbloquear el sistema, Fase 2 · Modelo de datos y seguridad, Fase 3 · Logística ↔ Pedido, Fase 6 · Pagos parciales y pedido automático, Fase 7 · QA, producción y tesis, H-13 · Logística sin datos de prueba, H-14 · README vacío; scripts de raíz sin documentar, RF-04 · ≥2 teléfonos con relación explícita (+11 more)

### Community 17 - "Carrito"
Cohesion: 0.19
Nodes (10): carrito_total(), Carrito, agregar_al_carrito(), eliminar_del_carrito(), vaciar_carrito(), ver_carrito(), stock_comprometido(), stock_disponible() (+2 more)

### Community 18 - "base_tienda.html"
Cohesion: 0.20
Nodes (5): listar_pedidos(), mis_pedidos(), agotados_al_final(), listar_productos(), inicio()

### Community 19 - "DireccionEntrega"
Cohesion: 0.09
Nodes (10): DireccionEntrega, Meta, BarrioForm, Meta, Barrio, Meta, GeneracionBorradorTests, GeneracionQuincenalTests (+2 more)

### Community 20 - "What You Must Do When Invoked"
Cohesion: 0.07
Nodes (26): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+18 more)

### Community 21 - "base_dashboard.html"
Cohesion: 0.14
Nodes (15): Hallazgos nuevos, actualizar_estado_entrega(), agregar_parada(), crear_ruta(), direcciones_sin_zona(), editar_camion(), editar_ruta(), editar_zona() (+7 more)

### Community 22 - "clientes/services.py"
Cohesion: 0.05
Nodes (21): ClienteAdmin, DireccionEntregaAdmin, DireccionEntregaInline, MovimientoBidonAdmin, TelefonoContactoAdmin, TelefonoContactoInline, MovimientoBidon, Meta (+13 more)

### Community 23 - "django_contrib"
Cohesion: 0.16
Nodes (6): CalendarioExcepcion, Meta, fecha_es_de_reparto(), _hay_excepcion(), proxima_fecha_de_reparto(), CalendarioTests

### Community 24 - "aplicar_pago_mercadopago"
Cohesion: 0.13
Nodes (6): aplicar_pago_mercadopago(), consultar_pago_mercadopago(), pago_en_curso(), pago_exitoso(), webhook_mercadopago(), csrf_failure()

### Community 25 - "pedidos/views.py"
Cohesion: 0.13
Nodes (9): 1. 🔴 Críticos — seguridad y dinero, cambiar_estado_pago(), cambiar_estado_pedido(), confirmar_pago_qr(), detalle_pedido(), pago_fallido(), pago_pendiente(), pago_qr() (+1 more)

### Community 26 - "RecorridoRepartidorTests"
Cohesion: 0.10
Nodes (4): confirmar_hoja(), ConfirmacionRegresoTests, InventarioCamionTests, RecorridoRepartidorTests

### Community 29 - "RolEmpleado"
Cohesion: 0.18
Nodes (9): 2. 🟠 Altos — errores funcionales, 4. ♻️ Redundancias, 5. 📄 Incoherencias de documentación, 6. ✅ Lo que está bien (mantener), 7. 🗺️ Cómo entra en el plan, 🔎 Auditoría de coherencia — Distribuidora 3.0, Decisiones nuevas, RolEmpleado (+1 more)

### Community 31 - "ver_ruta"
Cohesion: 0.16
Nodes (8): AgregarParadaForm, botellon_por_defecto(), productos_de_reparto(), _ids_de_paradas_con_nota(), _parse_fecha(), planificar_reparto(), venta_calle(), ver_ruta()

### Community 32 - "puede"
Cohesion: 0.09
Nodes (12): eliminar_ruta(), restaurar_camion(), restaurar_ruta(), restaurar_zona(), es_repartidor_asignado(), obtener_empleado(), puede(), puede_alguna() (+4 more)

### Community 33 - "listar_clientes"
Cohesion: 0.14
Nodes (7): BuscarClienteForm, _columnas_ordenables(), crear_cliente(), crear_cliente_con_cuenta(), crear_cliente_sin_cuenta(), listar_clientes(), _texto_buscable()

### Community 34 - "django_apps"
Cohesion: 0.04
Nodes (14): AbonosConfig, AutenticacionConfig, BuscadorConfig, CarritoConfig, ClientesConfig, ConfiguracionConfig, CuentasConfig, EmpleadosConfig (+6 more)

### Community 35 - "GeneracionBorradorTests"
Cohesion: 0.18
Nodes (3): clientes_frecuentes_de_zona(), construir_borrador(), pedidos_candidatos()

### Community 36 - "logistica/models.py"
Cohesion: 0.11
Nodes (14): BarrioAdmin, CalendarioExcepcionAdmin, CamionAdmin, CargaHojaRutaAdmin, DetalleHojaRutaAdmin, DetalleHojaRutaInline, HojaRutaAdmin, RutaRepartoAdmin (+6 more)

### Community 37 - "CompraPromocion"
Cohesion: 0.16
Nodes (8): 5B — Promociones prepago (RF-09) · ~6 h, CompraPromocionAdmin, ConsumoPromocionInline, PromocionAdmin, CompraPromocion, Meta, ConsumoPromocion, Meta

### Community 38 - "Empleado"
Cohesion: 0.20
Nodes (4): EmpleadoAdmin, RolEmpleadoAdmin, Empleado, Meta

### Community 39 - "distribuidora/views.py"
Cohesion: 0.19
Nodes (6): clientes_morosos(), resumen_morosidad(), PagoPedido, Meta, resumen_caja(), resumen_dashboard()

### Community 40 - "generar_cargos_mensuales"
Cohesion: 0.19
Nodes (3): Command, generar_cargos_mensuales(), FacturacionTests

### Community 44 - "Migración: unificar empleados"
Cohesion: 0.40
Nodes (3): copiar_empleados_logistica(), Migration, _nombre_completo_de_usuario()

### Community 45 - "seed_demo.py"
Cohesion: 0.13
Nodes (3): obtener_o_crear_cuenta(), metodo_pago_efectivo(), registrar_cobro()

### Community 47 - "PerfilUsuarioForm"
Cohesion: 0.10
Nodes (7): PerfilUsuarioForm, Meta, RegistroClienteWebForm, Meta, EmpleadoForm, Meta, validar_nombre()

### Community 48 - "DetalleHojaRuta"
Cohesion: 0.12
Nodes (9): 5A — Historial de envases (RF-08) · ~4 h, 5D — Tests · ~2 h, FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, DetalleHojaRuta, Meta, _producto_envase_para(), registrar_entrega() (+1 more)

### Community 49 - "aplicar_attrs"
Cohesion: 0.12
Nodes (6): DireccionRegistroForm, Meta, EditarMiPerfilForm, CamionForm, Meta, aplicar_attrs()

### Community 50 - "Pedido"
Cohesion: 0.15
Nodes (5): ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`), 6A — Pagos parciales (RF-13) · ~4 h, pedidos_pendientes(), Pedido, Meta

### Community 51 - "ver_cliente"
Cohesion: 0.18
Nodes (6): DireccionEntregaForm, Meta, _contexto_suscripcion(), mi_perfil_cliente(), ver_cliente(), compras_vigentes()

### Community 52 - "Abono"
Cohesion: 0.07
Nodes (14): AbonoAdmin, AbonoForm, Meta, Abono, Meta, CostoPreferencialTests, VistasAbonosTests, cambiar_estado_abono() (+6 more)

### Community 53 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 54 - "🏁 Plan de Cierre — Fases 4.5 a 7"
Cohesion: 0.25
Nodes (6): 0. Qué falta (resumen), 5. 🔗 Dependencias y archivos compartidos, 6. Rutina por sub-fase, FASE 4.5 — Consolidación 🧹 ✅ **COMPLETADA (20/10/2026)**, FASE 4.6 — Correcciones de auditoría 🛠️ ✅ **COMPLETADA (20/10/2026)**, 🏁 Plan de Cierre — Fases 4.5 a 7

### Community 55 - "clientes/tests.py"
Cohesion: 0.05
Nodes (8): AgregarDireccionTests, AltaClienteValidacionesTests, BuscarClientesTests, EditarMiPerfilTests, FiadoPremiumYExcepcionTests, OrdenDirectorioClientesTests, VariasDireccionesTests, VistaMovimientoBidonTests

### Community 56 - "MetodoPago"
Cohesion: 0.10
Nodes (6): MetodoPago, Meta, CheckoutRequiereTelefonosTests, PagosParcialesTests, StockComprometidoTests, TransicionesManualesTests

### Community 57 - "TelefonoContacto"
Cohesion: 0.13
Nodes (6): TelefonoContactoForm, Meta, TelefonoContacto, Meta, crear_perfil_cliente(), BajaLogicaTelefonoDireccionTests

### Community 62 - "clientes/forms.py"
Cohesion: 0.10
Nodes (9): leer_telefonos(), ValidadoresTests, normalizar_patente(), solo_digitos(), validar_altura(), validar_coordenadas(), validar_dni(), validar_fecha_no_futura() (+1 more)

### Community 66 - "RolEmpleadoForm"
Cohesion: 0.20
Nodes (3): RolEmpleadoForm, Meta, BajaLogicaRolTests

### Community 69 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 70 - "es_personal_interno"
Cohesion: 0.08
Nodes (17): asignar(), Migration, _permisos(), roles_usuario(), Funcion, Meta, es_personal_interno(), 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo) (+9 more)

### Community 71 - "pedidos/forms.py"
Cohesion: 0.14
Nodes (6): fecha_estimada_para_direccion(), CheckoutForm, _etiqueta_direccion_con_fecha(), SuscripcionForm, Meta, CheckoutFechaEstimadaTests

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
Cohesion: 0.09
Nodes (3): RecuperarContrasenaTests, RegistroTelefonosTests, SesionTests

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
Nodes (15): _etiqueta_direccion_cliente(), HojaRutaForm, Meta, RutaRepartoForm, Meta, Camion, Meta, RutaReparto (+7 more)

### Community 99 - "permisos/tests.py"
Cohesion: 0.07
Nodes (7): puede_ver_nota_seguridad(), AccesoAVistasLogisticasTests, GruposBaseTests, NotaDeSeguridadTests, Distribuidora 3.0 / Aguadelluvia, graphify, graphify

### Community 100 - "QA-04 Abono con costo 0"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-04 Abono con costo 0, Qué pasa

### Community 101 - "PagosSegurosTests"
Cohesion: 0.19
Nodes (3): firma_webhook_valida(), _firmar(), PagosSegurosTests

### Community 102 - "RegistroUsuarioForm"
Cohesion: 0.16
Nodes (3): RegistroUsuarioForm, Meta, RegistroValidacionesTests

### Community 104 - "editar_mi_perfil"
Cohesion: 0.20
Nodes (4): MovimientoBidonForm, editar_mi_perfil(), registrar_movimiento_bidon(), errores_en_texto()

### Community 105 - "FASE3_LOGISTICA.md"
Cohesion: 0.22
Nodes (5): Arquitectura visual dual: Tienda vs Dashboard, Carga y regreso del camión (sobrantes a stock), Confirmar hoja al cargar el camión → Pedido «En Camino», Días de reparto por zona → fecha estimada, Ventas y paradas agregadas en la calle

### Community 106 - "registrar_cargo"
Cohesion: 0.08
Nodes (10): CuentaCorrienteAdmin, MovimientoCuentaAdmin, MovimientoCuentaInline, MovimientoCuenta, Meta, registrar_cargo(), registrar_pago(), CuentaCorrienteModelTests (+2 more)

### Community 107 - "QA-05 Zona sin días de reparto"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-05 Zona sin días de reparto, Qué pasa

### Community 110 - "EnvaseForm"
Cohesion: 0.21
Nodes (3): bidones_retornables(), EnvaseForm, envases()

### Community 116 - "QA-06 Email de producción sin configurar"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-06 Email de producción sin configurar, Qué pasa, Resolución

### Community 117 - "Usuario"
Cohesion: 0.12
Nodes (4): Usuario, Meta, CuentaDeRepartidorTests, ModeloEmpleadoUnicoTests

### Community 118 - "Fase 4 · Cuentas corrientes y abonos"
Cohesion: 0.33
Nodes (4): Fase 4 · Cuentas corrientes y abonos, RF-05 · Clientes Normal/Premium; fiado solo Premium, RF-15 · Alquiler de dispensers (abonos), RF-20 · Gastos por proveedor (alcance sin decidir, C-9/D-3)

### Community 120 - "pedidos/views.py"
Cohesion: 0.18
Nodes (8): 6B — Checkout seguro (RF-04, RF-12) · ~3 h, 6D — Tests · ~1 h, FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18) ✅ **COMPLETADA (20/10/2026)**, Punto de partida real, checkout(), _cliente_puede_comprar(), confirmar_pedido(), saldo_vigente()

### Community 122 - "0002_bidones_recargables_y_rol_recargador.py"
Cohesion: 0.47
Nodes (4): _catalogo(), Migration, _permisos_y_roles(), preparar()

### Community 123 - "productos/views.py"
Cohesion: 0.17
Nodes (8): 3. 🟡 Medios, con_stock_disponible(), crear_producto(), editar_producto(), eliminar_producto(), _filtrar_por_categoria(), listar_productos_admin(), ver_producto()

### Community 124 - "QA campo a campo — 12/11/2026"
Cohesion: 0.40
Nodes (5): Cómo se probó, Errores encontrados y corregidos, Mejoras agregadas, Pendientes grandes, QA campo a campo — 12/11/2026

### Community 125 - "promociones/views.py"
Cohesion: 0.11
Nodes (11): PromocionForm, Meta, VenderPromocionForm, Promocion, Meta, promociones_por_vencer(), crear_promocion(), editar_promocion() (+3 more)

### Community 126 - "AltaClienteConCuentaForm"
Cohesion: 0.25
Nodes (3): AltaClienteConCuentaForm, Meta, _ValidarDatosPersonalesMixin

### Community 127 - "django_shortcuts"
Cohesion: 0.17
Nodes (6): buscar_productos(), marcar(), Migration, _normalizar(), normalizar_texto(), RF-07 · Buscador tolerante a tildes

### Community 128 - "DetallePedido"
Cohesion: 0.15
Nodes (9): DetallePedidoInline, MetodoPagoAdmin, PagoPedidoAdmin, PagoPedidoInline, PedidoAdmin, SuscripcionReposicionAdmin, DetallePedido, Meta (+1 more)

### Community 132 - "QA-01 Validaciones solo en formularios"
Cohesion: 0.50
Nodes (4): Arreglo propuesto, Cómo reproducir, QA-01 Validaciones solo en formularios, Qué pasa

### Community 133 - "logistica/views.py"
Cohesion: 0.09
Nodes (20): botellones_por_producto(), carga_sugerida(), entregados_por_producto(), envase_de_reparto(), envases_retirados_en_hoja(), inventario_camion(), registrar_regreso(), resumen_recorrido() (+12 more)

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

### Community 139 - "ClienteForm"
Cohesion: 0.29
Nodes (4): ClienteForm, Meta, ClienteSinCuentaForm, ValidacionesClienteTests

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
Cohesion: 0.12
Nodes (4): Detalle, _bloquear_cuenta(), Cliente, Meta

### Community 145 - "autenticacion"
Cohesion: 0.67
Nodes (3): autenticacion, Notas, Relaciones

### Community 146 - "{{title}}"
Cohesion: 0.40
Nodes (4): Arreglo propuesto, Cómo reproducir, Qué pasa, {{title}}

### Community 147 - "{{date}}"
Cohesion: 0.40
Nodes (4): Bloqueos / dudas, {{date}}, Pendiente, Qué hice

### Community 148 - "editar_rol"
Cohesion: 0.43
Nodes (3): crear_rol(), editar_rol(), _plantillas()

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

### Community 155 - "QA-09 Recuperar contraseña usa vistas de clase"
Cohesion: 0.40
Nodes (5): Arreglo propuesto, Cómo reproducir, QA-09 Recuperar contraseña usa vistas de clase, Qué pasa, Resolución

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

### Community 169 - "🌊 Distribuidora 3.0 / Aguadelluvia"
Cohesion: 0.29
Nodes (7): 🧩 Apps Django, ⚙️ Comandos frecuentes, 🗂️ Cómo está organizado el vault, 🧭 Decisiones, 🌊 Distribuidora 3.0 / Aguadelluvia, 📚 Documentación del proyecto, 🧪 QA

### Community 171 - "agregar_pedido_parada"
Cohesion: 0.40
Nodes (3): agregar_pedido_parada(), pedido_parada(), _volver_a_hoja()

### Community 172 - "Fase 5 · Bidones y promociones prepago"
Cohesion: 0.40
Nodes (5): Bidón retornable (entrega lleno, retira vacío), Fase 5 · Bidones y promociones prepago, RF-08 · Control de envases prestados, RF-09 · Promociones prepago "paga 3 lleva 4", RF-10 · Caducidad 30 días corridos

### Community 174 - "Notas"
Cohesion: 0.40
Nodes (4): stock_reservado_por_producto(), Notas, pedidos, Relaciones

### Community 177 - "Qué hice"
Cohesion: 0.22
Nodes (9): 2026-11-16, Baja lógica desde los listados de empleados y clientes, Bloqueos / dudas, Configuración, Envases asociados (nuevo), Inicio de la tienda (rehecho), Pendiente, Qué hice (+1 more)

## Knowledge Gaps
- **2 isolated node(s):** `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1031 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **61 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cliente` connect `Cliente` to `Command`, `logistica/views.py`, `CuentaCorriente`, `SuscripcionReposicion`, `planta/views.py`, `clientes/views.py`, `ClienteForm`, `logistica/services.py`, `Producto`, `PROCEDURE.md`, `DireccionEntrega`, `base_dashboard.html`, `clientes/services.py`, `aplicar_pago_mercadopago`, `pedidos/views.py`, `RecorridoRepartidorTests`, `Command`, `listar_clientes`, `GeneracionBorradorTests`, `distribuidora/views.py`, `generar_cargos_mensuales`, `HojaDeRutaUXTests`, `Fase 5 · Bidones y promociones prepago`, `seed_demo.py`, `DetalleHojaRuta`, `Pedido`, `ver_cliente`, `Abono`, `clientes/tests.py`, `TelefonoContacto`, `clientes/forms.py`, `CobroManualTests`, `pedidos/forms.py`, `logistica/tests.py`, `permisos/tests.py`, `editar_mi_perfil`, `registrar_cargo`, `VistasCuentasTests`, `Usuario`, `Fase 4 · Cuentas corrientes y abonos`, `pedidos/views.py`, `PedidoEspontaneoTests`, `promociones/views.py`, `AltaClienteConCuentaForm`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 69 inferred relationships involving `Cliente` (e.g. with `AbonoForm` and `Abono`) actually correct?**
  _`Cliente` has 69 INFERRED edges - model-reasoned connections that need verification._
- **What connects `H-13 · Logística sin datos de prueba`, `H-14 · README vacío; scripts de raíz sin documentar` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `autenticacion/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1028225806451613 - nodes in this community are weakly interconnected._
- **Why does `Producto` connect `Producto` to `DetallePedido`, `Command`, `QA-01 Validaciones solo en formularios`, `logistica/views.py`, `ProductoForm`, `SuscripcionReposicion`, `planta/views.py`, `logistica/services.py`, `productos/views.py`, `Carrito`, `base_tienda.html`, `DireccionEntrega`, `aplicar_pago_mercadopago`, `RecorridoRepartidorTests`, `Command`, `ver_ruta`, `StockReservadoTests`, `generar_cargos_mensuales`, `GenerarEnvaseTests`, `HojaDeRutaUXTests`, `distribuidora/views.py`, `seed_demo.py`, `Notas`, `InicioTests`, `DetalleHojaRuta`, `Abono`, `MetodoPago`, `logistica/tests.py`, `EnvaseForm`, `CarritoSoloPorPostTests`, `pedidos/views.py`, `PedidoEspontaneoTests`, `productos/views.py`, `promociones/views.py`, `django_shortcuts`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Producto` (e.g. with `Punto de partida real` and `AbonoForm`) actually correct?**
  _`Producto` has 62 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_conf` be split into smaller, more focused modules?**
  _Cohesion score 0.05353535353535353 - nodes in this community are weakly interconnected._