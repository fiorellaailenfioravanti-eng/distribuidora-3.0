# 🧭 Plan de Procedimiento — Distribuidora 3.0 / Aquadelluvia

> **Propósito:** Documento de trabajo que reconcilia el **código real**, el **contexto del workspace** (`.agents/CONTEXT.md`) y el **Informe de Avances de Tesis (Julio 2026) — MASSON, Lucas (L.U. 37492)**, y fija el procedimiento para cerrar los módulos restantes sin romper lo ya implementado.
>
> **Fecha de elaboración:** 30/09/2026
> **Base analizada:** commit `5362ab1` ("arreglo de algunos bugs")
> **Reglas del workspace:** ver [`.agents/AGENTS.md`](AGENTS.md) · [`.agents/CONTEXT.md`](CONTEXT.md) · [`.agents/DESIGN.md`](DESIGN.md)

---

## ▶️ Estado de ejecución — 30/09/2026

| Fase | Alcance ejecutado | Estado |
|:--:|---|:--:|
| **Fase 1** | Grupos base + permisos, `MetodoPago` sembrado, módulo `apps.permisos`, `BASE_DIR` corregido | ✅ **Completada** |
| **Fase 2** | `Empleado`/`RolEmpleado` unificados, RNF-02 cerrado, etiquetas RNF-02, `SECRET_KEY` a entorno, `production.py` | ✅ **Completada** |
| — | Tests de roles, unificación y RNF-02 (`apps/permisos/tests.py`, 29 tests) | ✅ |
| **Fase 3** | Logística ↔ Pedido (RF-16, RF-17, RF-19) | 🔴 Pendiente |
| **Fase 4–7** | Cuentas, abonos, bidones, promociones, pagos parciales, QA final | 🔴 Pendiente |

**Hallazgos cerrados:** H-1, H-2, H-3, H-5, H-6, H-7, H-8, H-9 y H-15.
**Hallazgos abiertos:** H-4 (logística ↔ Pedido), H-10 (suite parcial), H-13/H-14 (datos/README), H-16 (abonos).
**Además se corrigió un agujero no catalogado:** `ver_ruta` y `actualizar_estado_entrega`
permitían a **cualquier usuario autenticado** (incluido un cliente registrado) abrir o
modificar hojas de ruta ajenas. Se agregó el guard `es_admin_vendedor_o_repartidor`
y la restricción por asignación.

**Comandos verificados (30/09/2026):**
```powershell
.\venv\Scripts\python.exe manage.py check --settings=distribuidora.settings.local          # 0 issues
.\venv\Scripts\python.exe manage.py makemigrations --check --dry-run --settings=...local   # No changes detected
.\venv\Scripts\python.exe manage.py test --settings=distribuidora.settings.local            # 29 OK
.\venv\Scripts\python.exe manage.py check --deploy --settings=distribuidora.settings.production  # 0 issues
```

---

## 0. 📌 Aviso sobre el informe PDF

El informe se leyó **extrayendo el texto** del PDF (`pypdf`, 12 páginas, ~22.400 caracteres) porque el modelo no acepta PDF como entrada directa. **El texto fue extraído con éxito y está completo**, pero:

> ⚠️ Las **imágenes no se interpretaron**: el **Diagrama Entidad-Relación** (pág. 8, sección "DIAGRAMA ENTIDAD RELACIÓN") y los **árboles de directorio** (pág. 10–11) son figuras. El contenido de esos gráficos **no pudo ser leído** y no fue contrastado contra el código.

**Acción requerida:** validar manualmente que el DER del informe coincide con el esquema real de §6 de `CONTEXT.md` antes de entregar la memoria de tesis.

---

## 1. 🩺 Diagnóstico: hay tres fuentes de verdad y ninguna coincide

| # | Fuente | Fecha | Estado | Problema |
|:--:|---|---|---|---|
| 1 | **Código real** (`apps/`, commit `5362ab1`) | 30/09/2026 | ✅ `manage.py check` sin errores, 0 migraciones pendientes | — |
| 2 | **`.agents/CONTEXT.md`** v3.1 | 31/07/2026 | 🔴 **Desactualizado** | Declara `logistica` y `empleados` como inexistentes/pendientes. Ambos apps están completos con modelos, vistas, URLs y templates. También lista `pedidos` como "🔴 Pendiente" en la sección 5 y como "✅ Nuevo" en la sección 4 (contradicción interna, líneas 342–355 vs 524). |
| 3 | **Informe de Tesis (Julio 2026)** | Jul/2026 | 🔴 **Desactualizado + contradictorio internamente** | Ver §2. Describe 4 apps; el proyecto tiene 8. No menciona MercadoPago, ni `empleados`, ni `logistica` implementado. Su cronograma no coincide con el de `CONTEXT.md` ni con el código. |

> **Conclusión:** el código avanzó ~2 meses por encima de la documentación. Antes de escribir una sola línea de código nuevo, hay que **re-baseline** de la documentación (Fase 0).

---

## 2. 🔍 Contradicciones detectadas dentro del propio informe

Estas no son errores de código: son inconsistencias que **un jurado va a detectar**. Hay que decidirlas explícitamente y unificarlas.

| # | Ubicación | Contradicción | Resolución propuesta |
|:--:|---|---|---|
| C-1 | pág. 4, 9, 11 | "**CBV** (Vistas Basadas en Clases)" | El código usa **FBV** (`Function-Based Views`) en los 8 apps. **Decisión: reescribir el informe diciendo FBV.** Es la opción de menor costo y es defendible (decoradores `@login_required` / `@user_passes_test` sobre FBV). Si se quiere sostener CBV, hay que refactorizar `productos` y `pedidos` (alto riesgo, bajo beneficio). |
| C-2 | pág. 2 vs Conclusión | Cronograma: pág. 2 dice *Mes 8 = transacciones atómicas, Mes 9 = cuentas corrientes, Mes 10 = logística, Mes 11 = alertas, Mes 12 = QA*. La Conclusión dice *Mes 8 = semaforización de deudas, Mes 9 = flujo de caja*. | Adoptar el cronograma de `CONTEXT.md` §10 como **cronograma canónico** (§3 de este documento). |
| C-3 | pág. 2 | "Mes 6 = Módulo de Entregas", "Mes 7 = Segmentación de Clientes" | El código real muestra: Mes 6 = UX/buscador/carrito, Mes 7 = clientes, Mes 8 = pedidos, Mes 9–10 = logística + empleados. Reetiquetar. |
| C-4 | RF-05 (pág. 3) vs pág. 2 vs Conclusión | RF-05 dice **2** categorías ("Normales" y "Premium"). La pág. 2 y la Conclusión dicen **3** ("Normal, VIP, Premium"). | El código resolvió esto: `TIPO_CLIENTE_CHOICES = [('Normal',…), ('Premium','VIP / Premium')]` (`apps/clientes/models.py:7-10`). **Documentar que "VIP" se absorbió dentro de "Premium"** como etiqueta, no como tercer tipo. Unificar el informe a 2 tipos. |
| C-5 | pág. 1, 12 | Empresa = "**Agua de lluvia**" | `CONTEXT.md` = "**Aquadelluvia**". Unificar en **Aquadelluvia** (usar el nombre real en el informe, o aclarar "Agua de Lluvia" como nombre comercial original del logo). |
| C-6 | RF-03 vs RNF-02 | RF-03 = "Multidirección". `CONTEXT.md` etiqueta la nota de seguridad como "RF-03" (`apps/clientes/models.py:170,203`). | El ocultamiento de la nota de seguridad es **RNF-02**, no RF-03. **Corregir `help_text` y comentarios del código** (ver T-2.4). |
| C-7 | HU-1, criterio 3 (pág. 5) | "inicializa una nueva instancia de **Persona** y **Cliente**" | No existe el modelo `Persona`. El diseño real es `autenticacion.Usuario` + `clientes.Cliente` (OneToOne, nullable). Corregir el HU al esquema real — es **mejor** diseño (evita duplicar identidad). |
| C-8 | HU-2, criterio 3 (pág. 6) | "`Direccion_entrega` vinculándola mediante el **dni** del cliente" | El código usa **FK `cliente`** (`DireccionEntrega.cliente`). Vincular por DNI (`CharField`) sería una **violación de normalización** (clave natural →FK). Corregir el HU y **defender la FK en la tesis**. |
| C-9 | pág. 8 (Objetivos de BD) | "**Auditoría**: Registro detallado de **gastos operativos clasificados por proveedores**" | No tiene RF asignado y **no está en el roadmap** de `CONTEXT.md`. **Decisión de alcance:** (a) agregarlo como RF-20 y construirlo en Fase 4, o (b) declararlo explícitamente fuera del alcance. Hoy es un requisito "fantasma" que el jurado puede pedir. |
| C-10 | RF-13 (pág. 4) | Métodos: Efectivo, **Transferencia**, Tarjeta de Débito, **Billetera Digital** | `MetodoPago` es un catálogo libre ✅. Pero en `db.sqlite3` solo hay 3 filas y **`MERCADOPAGO` y `TARJETA` están en `activo=0`**; falta `TRANSFERENCIA` y `BILLETERA`. Ver T-1.5. |
| C-11 | RF-18 (pág. 4) | **Pedidos automáticos de reposición quincenal** activables por perfil | **No implementado Y ni siquiera está en `CONTEXT.md`.** RF huérfano. Ver T-6.2. |

---

## 3. 🗓️ Cronograma canónico reconciliado (propuesta)

Reemplaza al de `CONTEXT.md` §10 y al del informe. Refleja el **código real** a 30/09/2026.

| Mes | Hito | Estado real |
|:--:|---|---|
| 1–3 | Relevamiento, análisis, DER | ✅ Completado |
| 4 | CRUD core de productos + categorías | ✅ Completado |
| 5 | Seguridad, roles y validadores de claves | ✅ Completado |
| 6 | UX, buscador tolerante, carrito | ✅ Completado |
| 7 | Segmentación y gestión de clientes | ✅ Completado |
| 8 | Lógica transaccional: Pedidos, Pagos, MercadoPago | ✅ Completado |
| 9 | Empleados, roles y estructura logística (zonas, barrios, camiones) | ✅ Completado |
| 10 | Hojas de ruta + vista de repartidor | 🟡 **Parcial** — falta vínculo con `Pedido` y agrupamiento automático |
| 11 | Cuentas corrientes, morosidad, abonos, bidones, promociones | 🔴 Pendiente |
| 12 | RF-18, tests, `production.py`, memoria de tesis | 🔴 Pendiente |

---

## 4. 📊 Matriz de cobertura Requisitos ↔ Código

Leyenda: ✅ completo · 🟡 parcial · 🔴 no implementado · ⚠️ implementado con defecto

| ID | Requerimiento | Ubicación en código | Estado | Tarea |
|:--:|---|---|:--:|---|
| RF-01 | Registro con ≥2 celulares y descripción de relación | `autenticacion/models.py`, `clientes/signals.py` | ✅ | — |
| RF-02 | Validación de contraseñas (4 validadores Django) | `settings/base.py:82-92` | ✅ | — |
| RF-03 | Multidirección: calle, altura, zona, seguridad, coordenadas | `clientes/models.py:172-245` | ✅ | — |
| RF-04 | ≥2 teléfonos con relación explícita | `clientes/models.py:133-165` | 🟡 | T-6.1 |
| RF-05 | Normal/Premium; solo Premium con fiado | `clientes/models.py:7-10,122-126` | 🟡 | T-4.2 |
| RF-06 | Catálogo agrupado por categorías | `productos/` | ✅ | — |
| RF-07 | Buscador tolerante a tildes/errores | `buscador/` | ✅ | — |
| RF-08 | **Control de envases prestados** (entrada/salida) | solo `Cliente.bidones_prestados` (entero) | 🔴 | T-5.1 |
| RF-09 | **Promociones prepago** "paga 3 lleva 4" | — | 🔴 | T-5.2 |
| RF-10 | **Caducidad 30 días corridos** | — | 🔴 | T-5.3 |
| RF-11 | Pedido: fecha, total, estado, dirección, desglose | `pedidos/models.py:36-107` | ✅ | — |
| RF-12 | Carrito no excede stock | `carrito/views.py` | 🟡 | T-1.6 |
| RF-13 | **Pagos parciales** y múltiples métodos | `PagoPedido` existe; **no hay vista de cobro manual** | 🟡 | T-6.2 |
| RF-14 | **Semaforización de deuda** (🟡/🟠/🔴) | — (no hay modelo de cuenta corriente) | 🔴 | T-4.1 |
| RF-15 | **Contratos de alquiler de dispensers** | — (`apps.abonos` solo planificado) | 🔴 | T-4.3 |
| RF-16 | Hojas de ruta diarias (fecha, zona, camión, chofer) | `logistica/models.py:155-207` | 🟡 | T-3.1 |
| RF-17 | **Agrupación automática + generación quincenal** | — (`pedido_ref` es `CharField` temporal) | 🔴 | T-3.2, T-3.3 |
| RF-18 | **Pedido automático quincenal activable** | — (ausente incluso del roadmap) | 🔴 | T-6.3 |
| RF-19 | Confirmación de entrega en campo por repartidor | `logistica/views.py:244-307` | 🟡 | T-3.4 |
| RNF-01 | Escalabilidad multi-camión/multi-zona/multi-chofer | `logistica/models.py` | ⚠️ | T-2.1 |
| RNF-02 | Ocultación de info sensible | `clientes/views.py:91`, templates | ⚠️ | T-2.4, T-2.5 |
| RNF-03 | Dark mode sin autenticación | `base_tienda.html`, `base_dashboard.html` | ✅ | — |

**Balance: 9 completos · 8 parciales · 5 no implementados · 2 con defecto — 20 de 22 requisitos requieren trabajo.**

---

## 5. 🚨 Hallazgos técnicos (verificados ejecutando el proyecto)

Todos verificados con `manage.py check`, `manage.py makemigrations --check` y consultas directas a `db.sqlite3`.

| ID | Severidad | Hallazgo | Evidencia |
|:--:|:--:|---|---|
| H-1 | 🔴 Crítica | **El grupo `Vendedor` NO EXISTE en la base.** `auth_group` contiene únicamente `('Repartidor',)`. Como `es_vendedor_o_admin()` se evalúa con `groups.filter(name='Vendedor').exists()`, **todo usuario no-superusuario pierde el acceso de Vendedor**: no puede crear productos, clientes, pedidos, rutas ni zonas. El sistema queda usable solo como superusuario. | `db.sqlite3` → `auth_group` = `['Repartidor']`; `apps/productos/views.py:15`, `apps/clientes/views.py:17`, `apps/pedidos/views.py:27`, `apps/logistica/views.py:15` |
| H-2 | 🔴 Crítica | **Modelos `Empleado` y `RolEmpleado` DUPLICADOS** en dos apps. Existen `empleados_empleado`, `empleados_rolempleado`, `logistica_empleado` **y** `logistica_rolempleado`. Además `logistica.Empleado.descripcion` es un rol descrito como texto libre, no como FK. | `apps/empleados/models.py:4,17` vs `apps/logistica/models.py:48,63` |
| H-3 | 🔴 Crítica | **La logística no puede asignar repartidor.** `logistica_empleado` tiene **0 filas** mientras `empleados_empleado` tiene 1. El formulario de `crear_ruta` ofrece `logistica.Empleado` → nunca hay repartidores seleccionables → **ninguna hoja de ruta puede crearse**. | `db.sqlite3`; `templates/logistica/crear_ruta.html:39` |
| H-4 | 🔴 Alta | **`DetalleHojaRuta.pedido_ref` es un `CharField` de relleno** ("hasta que exista el modelo `Pedido`"). El modelo `Pedido` **ya existe** (`apps/pedidos/`). La hoja de ruta **no está relacionada con el pedido** → RF-17 y RF-19 no cierran el circuito; el repartidor marca entregas que no actualizan ningún `Pedido`. | `apps/logistica/models.py:226-230` |
| H-5 | 🔴 Alta | **Control de permisos roto en templates por `groups.all.0`.** La expresión `user.groups.all.0.name == 'Vendedor'` solo mira el **primer** grupo del usuario. Con 2+ grupos el resultado es arbitrario. El filtro correcto `has_group` ya existe (`autenticacion/templatetags/grupos.py`) pero **no se usa ahí**. | `templates/pedidos/detalle_pedido.html:16,128`; `templates/clientes/agregar_direccion.html:42` |
| H-6 | ⚠️ Media | **Fuga potencial de RNF-02.** El template muestra `desc_seguridad` a **cualquier** usuario del grupo `Repartidor`, sin verificar que esté **asignado a la hoja de ruta** de esa dirección — algo que RNF-02 exige explícitamente. | `templates/clientes/ver_cliente.html:303`; `templates/pedidos/detalle_pedido.html:128` |
| H-7 | ⚠️ Media | **Precedencia de operadores mezclada** en `detalle_pedido.html:128`: `if pedido.direccion_entrega.desc_seguridad and request.user.is_superuser or request.user.groups.all.0.name == 'Vendedor' or ...` — el `and` liga más que el `or`, con lo que un Vendedor ve la nota **aunque `desc_seguridad` esté vacía**, y la lógica de visibilidad es incorrecta. | `templates/pedidos/detalle_pedido.html:128` |
| H-8 | ⚠️ Media | **`SECRET_KEY` hardcodeada** en el settings base. | `distribuidora/settings/base.py:24` |
| H-9 | ⚠️ Media | **`settings/production.py` tiene 0 bytes.** | `distribuidora/settings/production.py` |
| H-10 | ⚠️ Media | **Cero tests.** `manage.py test` → *"Found 0 test(s). NO TESTS RAN"*. `tests.py` en los 8 apps están vacíos. | `apps/*/tests.py` |
| H-11 | 🟡 Baja | **Lógica de permisos duplicada 5 veces:** `es_admin_o_vendedor` / `es_vendedor_o_admin` reimplementados en `clientes`, `logistica`, `productos`, `pedidos`, `carrito`. | `clientes/views.py:16`, `logistica/views.py:14`, `productos/views.py:14`, `pedidos/views.py:26`, `carrito/views.py:11` |
| H-12 | 🟡 Baja | **`Pedido.metodo_pago` es obligatorio** (`on_delete=PROTECT`, no `null`). Sin una fila `MetodoPago` activa, **ningún pedido puede crearse**. Hoy solo `EFECTIVO` está `activo=1`; `MERCADOPAGO` y `TARJETA` están `activo=0`. | `apps/pedidos/models.py:61-66`; `db.sqlite3` → `pedidos_metodopago` |
| H-13 | 🟡 Baja | **Logística sin datos de prueba**: `logistica_rutareparto`, `logistica_hojaruta`, `logistica_detallehojaruta` = **0 filas**. El módulo nunca se ejecutó de punta a punta. | `db.sqlite3` |
| H-14 | 🟡 Baja | **`README.md` vacío** (solo la línea `# dis-agua`). Los scripts `fix_icons.py` y `seed_barrios.py` están en la raíz sin documentar. | raíz del repo |
| H-15 | 🟡 Baja | **`base.py` vs `local.py` desalineados**: `BASE_DIR` en `base.py:17` es un nivel más arriba que el cálculo de `DATABASES`/`STATIC_ROOT` en `local.py`, que asume `dirname(BASE_DIR)`. Funciona por casualidad; es frágil ante mover archivos. | `settings/base.py:17`, `settings/local.py` |
| H-16 | 🟡 Baja | **El RF-15 es "abonos" pero no existe `apps/abonos`.** `CONTEXT.md` §5 lo lista como planificado; nada en el repo. | `.agents/CONTEXT.md:361` |
| H-17 | ℹ️ Info | **Buen estado base:** `manage.py check` → 0 issues; `makemigrations --check` → sin cambios pendientes. El diseño de `Cliente` (datos propios + `OneToOne` opcional a `Usuario`) y de `Barrio → Zona` son **sólidos y defendibles** en la tesis. Mantener. | verificado |

---

## 6. 🗺️ Plan de Procedimiento

> **Regla de oro:** cada fase deja el proyecto en estado **verificable y commiteable**. No se avanza de fase con `check` en rojo o migraciones pendientes.
> **Comando de verificación estándar (siempre):**
> ```powershell
> .\venv\Scripts\python.exe manage.py check --settings=distribuidora.settings.local
> .\venv\Scripts\python.exe manage.py makemigrations --check --dry-run --settings=distribuidora.settings.local
> .\venv\Scripts\python.exe manage.py test --settings=distribuidora.settings.local
> ```

---

### FASE 0 — Congelar la verdad documental 🧊
**Objetivo:** una sola fuente de verdad. **Sin esto, cualquier trabajo posterior genera conflictos.**
**Esfuerzo:** ~3 h · **Riesgo:** nulo · **Dependencias:** ninguna

| # | Tarea | Archivo |
|:--:|---|---|
| 0.1 | Reescribir `CONTEXT.md`: marcar `logistica` y `empleados` como **✅ implementados**, corregir la sección 5 (eliminar `pedidos` de "pendiente"), actualizar §8 (mapa de URLs completo) y §10 (cronograma de §3 de este doc) | `.agents/CONTEXT.md` |
| 0.2 | Documentar el **DER real** de `logistica` (`Zona`, `Barrio`, `RolEmpleado`, `Empleado`, `Camion`, `RutaReparto`, `HojaRuta`, `DetalleHojaRuta`) y `pedidos` | `.agents/CONTEXT.md` §6 |
| 0.3 | Decidir y documentar las contradicciones **C-1 … C-11** de §2. Las que tocan el **código** (C-6) se arreglan en T-2.4 | este archivo |
| 0.4 | **Actualizar `AGENTS.md`** para que apunte a este `PROCEDURE.md` | `.agents/AGENTS.md` |
| 0.5 | Llenar `README.md`: qué es, cómo instalar, cómo correr, qué hace cada app | `README.md` |
| 0.6 | Documentar `fix_icons.py` y `seed_barrios.py` en el README | `README.md` |

✅ **Aceptación:** `CONTEXT.md` no afirma nada que el código contradiga. Versión 4.0.

---

### FASE 1 — Desbloquear el sistema (P0) 🚨
**Objetivo:** que el sistema sea **usable por alguien que no sea superusuario** y que los datos base existan.
**Esfuerzo:** ~4 h · **Riesgo:** bajo · **Dependencias:** Fase 0

| # | Tarea | Detalle |
|:--:|---|---|
| 1.1 ✅ | **Crear los grupos base** por migración de datos: `Vendedor`, `Repartidor` | `apps/autenticacion/migrations/0003_grupos_base.py` con `RunPython` |
| 1.2 ✅ | Migrar la creación del grupo `Repartidor` desde `apps.py` a la migración (dejar `apps.py` idempotente) | `apps/logistica/apps.py` |
| 1.3 ✅ | Asignar permisos al grupo `Vendedor` (productos, clientes, pedidos, empleados, logística) — 68 permisos; Repartidor: 6 | `apps/permisos/signals.py` (`post_migrate`, aditivo) |
| 1.4 ✅ | **Crear un módulo de permisos único** `apps/permisos/` con `es_admin_o_vendedor`, `es_repartidor`, `es_admin_vendedor_o_repartidor`, `puede_ver_nota_seguridad(user, direccion)` | nuevo; reemplaza H-11 |
| 1.5 ✅ | Sembrar `MetodoPago`: `EFECTIVO`, `MERCADOPAGO`, `TARJETA`, `TRANSFERENCIA` y `BILLETERA` activos (C-10 / H-12) | `apps/pedidos/migrations/0003_sembrar_metodos_pago.py` |
| 1.6 🔴 | **Reservar stock en el carrito** para evitar overselling entre dos sesiones concurrentes (RF-12 completo) — **PENDIENTE** | `apps/carrito/views.py` |
| 1.7 ✅ | Corregir `BASE_DIR`: `base.py` usa `Path(__file__).resolve().parent.parent.parent` y `local.py` apunta a `BASE_DIR / 'db.sqlite3'` (H-15) | `settings/` |

✅ **Aceptación:** crear un usuario, asignarlo al grupo `Vendedor`, y poder crear un producto, un cliente, un pedido (con los 4 métodos de pago) y una hoja de ruta **sin ser superusuario**.

---

### FASE 2 — Consolidar el modelo de datos y la seguridad 🔐
**Objetivo:** eliminar la duplicación de `Empleado` y cerrar RNF-02.
**Esfuerzo:** ~6 h · **Riesgo:** **medio** (migración de datos) · **Dependencias:** Fase 1

| # | Tarea | Detalle |
|:--:|---|---|
| 2.1 ✅ | **Unificar `Empleado` y `RolEmpleado`** (H-2/H-3): una sola fuente de verdad en `apps.empleados`; `logistica` referencia `empleados.Empleado`. Ejecutado con las migraciones `logistica/0005` (copia de datos), `0006` (FK a `empleados`) y `0008` (elimina las tablas duplicadas con salvaguarda de datos) | migraciones de `logistica` |
| 2.2 ✅ | Reemplazar el rol-como-texto por **FK a `RolEmpleado`**: resuelto al eliminar el modelo duplicado; el rol canónico ya era FK | migración |
| 2.3 ✅ | Verificar `IntegrityError` y migrar datos (1 empleado en `empleados`, 0 en `logistica`). Verificado: la tabla duplicada quedó vacía y se eliminó sin pérdida | `python manage.py migrate --settings=distribuidora.settings.local` |
| 2.4 ✅ | **Corregir H-5/H-7:** reemplazado `user.groups.all.0.name` por `{% if user\|has_group:"Vendedor" %}` y contexto calculado en la vista | `templates/pedidos/detalle_pedido.html`; `templates/clientes/ver_cliente.html` |
| 2.5 ✅ | **Cerrar RNF-02 (H-6):** `puede_ver_nota_seguridad(user, direccion)` → solo superusuario, Vendedor, o Repartidor **asignado** a una parada con esa dirección. Expuesta en `mi_ruta_hoy`, `ver_ruta` e `imprimir_ruta` vía `paradas_con_nota_visible` | `apps/permisos/roles.py`, vistas y templates de logística |
| 2.6 ✅ | Corrección de la etiqueta RF → **RNF-02** en `help_text` y comentarios (C-6) | `apps/clientes/models.py` + migración `0006` |
| 2.7 ✅ | **`SECRET_KEY` → variable de entorno** con `python-decouple` + `.env.example`; `production.py` exige la clave real | `settings/base.py`, `settings/production.py`, `.env.example` |

✅ **Aceptación (cumplida):** solo existe **un** modelo `Empleado`; un repartidor **no asignado** a la dirección **no** ve su nota de seguridad (cubierto por tests); `SECRET_KEY` no está en el código.

> **Extra no catalogado, resuelto en esta fase:** las vistas `ver_ruta` y
> `actualizar_estado_entrega` no tenían guard global y permitían a un cliente
> registrado ver o modificar hojas de ruta ajenas. Se agregó
> `es_admin_vendedor_o_repartidor` + control por asignación.

---

### FASE 3 — Cerrar Logística: RF-16, RF-17, RF-19 🚚
**Objetivo:** que la hoja de ruta se conecte de verdad con `Pedido` y que el reparto actualice el pedido.
**Esfuerzo:** ~10 h · **Riesgo:** medio · **Dependencias:** Fase 2

> 📄 **Plan detallado:** ver [`.agents/FASE3_LOGISTICA.md`](FASE3_LOGISTICA.md) — modelo de
> datos objetivo, pantallas, algoritmo de generación, impacto en stock y decisiones D1–D7
> pendientes de aprobación.
>
> ⚙️ **Estado (30/09/2026):** sub-fases **3A–3D ✅ implementadas y verificadas** (modelo y
> calendario, generación de hoja «Planificar reparto», confirmación/carga/regreso, y calle,
> envases y cobro). Pendientes **3E** (fecha estimada en el checkout) y **3F** (seed, tests
> integrales y cierre de docs). `check` limpio, sin migraciones pendientes, **55 tests OK**.

| # | Tarea | Detalle |
|:--:|---|---|
| 3.1 | **Vincular `DetalleHojaRuta` → `Pedido`** con `ForeignKey('pedidos.Pedido', null=True, on_delete=SET_NULL, related_name='paradas')`. Migrar `pedido_ref` con un script de datos | `logistica/models.py:226-230` |
| 3.2 | **Generador de hojas de ruta (RF-17, parte 1):** agrupar `Pedido` con `estado='Confirmado'` por `zona` (vía `DireccionEntrega.barrio.zona`) y proposing carga | `logistica/services.py` (nuevo) |
| 3.3 | **Generación quincenal automática (RF-17, parte 2):** comando `python manage.py generar_hojas_ruta --fecha=YYYY-MM-DD` invocable desde cron/Task Scheduler | `logistica/management/commands/` (nuevo) |
| 3.4 | **Impacto en `Pedido` (cierre de RF-19):** al marcar `Entregado` → `Pedido.estado='Entregado'` + `fecha_entrega`; al marcar `Cancelado` → `Pedido.estado='Cancelado'` + **devolución del stock** dentro de `transaction.atomic` | `logistica/views.py:244` |
| 3.5 | Validar `HojaRuta` con zona/camión/chofer coherentes con `RutaReparto` | `logistica/forms.py` |
| 3.6 | Confirmar que `imprimir_ruta` (`logistica/urls.py:12`) y `mi_ruta_hoy` funcionan **mobile-first** (HU-6, pág. 7 del informe) | `templates/logistica/mi_ruta_hoy.html` |
| 3.7 | Cargar datos de demostración: 2 rutas, 2 camiones, 1 hoja de ruta con paradas (H-13) | extender `seed_barrios.py` |

✅ **Aceptación:** un pedido `Confirmado` en la Zona A aparece como parada en la hoja de ruta de la Zona A; el repartidor marca `Entregado`; el `Pedido` pasa a `Entregado` y el stock queda consistente.

---

### FASE 4 — Cuentas corrientes, morosidad y abonos 💰
**Objetivo:** RF-14 (semaforización) y RF-15 (alquiler de dispensers).
**Esfuerzo:** ~14 h · **Riesgo:** medio · **Dependencias:** Fase 3

| # | Tarea | Detalle |
|:--:|---|---|
| 4.1 | **App `apps/cuentas`:** `CuentaCorriente` (saldo), `MovimientoCuenta` (`Cargo`/`Abono`, origen FK a `Pedido`/`Abono`) | nuevo app |
| 4.2 | **Regla de negocio RF-05/RF-14:** un `Cargo` a cuenta corriente solo se permite si `Cliente.permite_fiado=True` (validación en modelo y en vista) | `cuentas/models.py` |
| 4.3 | **Semaforización:** campo calculado `nivel_morosidad` → 🟡 deuda al inicio de mes · 🟠 a 10 días · 🔴 a 15 días. **Zona horaria `America/Argentina/Buenos_Aires`** (regla 5 de `AGENTS.md`) | `cuentas/models.py` |
| 4.4 | **Panel de morosidad** en el dashboard (`templates/dashboard/resumen.html`) con los tres colores de `DESIGN.md` | `templates/` |
| 4.5 | **App `apps.abonos`:** `Abono` (`Cliente_alquila_producto`): `fecha_inicio`, `costo_mensual`, `estado ∈ {Activo, Suspendido, Finalizado}`, FK a `Cliente` y `Producto` | nuevo app |
| 4.6 | Generación automática del **cargo mensual** de cada abono activo y sus **facturas** | `cuentas/services.py` |
| 4.7 | Validar que un cliente **Premium** obtiene costo preferencial (RF-05) | `cuentas/services.py` |
| 4.8 | Resolver **C-9**: agregar RF-20 (gastos por proveedor) al alcance, o declararlo fuera de alcance en el informe | este archivo |

✅ **Aceptación:** un cliente `Normal` con `permite_fiado=False` es rechazado al generar cargo; un `Premium` con deuda de 11 días aparece en 🟠 y a 16 días en 🔴.

---

### FASE 5 — Bidones y promociones prepago 📦
**Objetivo:** RF-08, RF-09, RF-10.
**Esfuerzo:** ~12 h · **Riesgo:** medio · **Dependencias:** Fase 4 (los abonos generan saldo)

| # | Tarea | Detalle |
|:--:|---|---|
| 5.1 | **RF-08:** reemplazar el entero `Cliente.bidones_prestados` por un **historial** `MovimientoBidon` (`Prestamo`/`Devolucion`, cantidad, fecha, pedido, usuario que registró). `bidones_prestados` pasa a ser un `@property` derivado | `clientes/models.py:67` |
| 5.2 | **RF-09:** `Promocion` (`nombre`, `cant_articulos`, `plazo_validez`), `IncluyePromocion` (pedido que la pagó), `SaldoDispensadorPromocion` (`unid_restantes`, `fecha_caducidad`) | `promociones/models.py` |
| 5.3 | **RF-10:** caducidad estricta a los **30 días corridos**; comando diario `vencer_promociones` que pone `unid_restantes=0` | `promociones/management/commands/` |
| 5.4 | Entregas parciales: cada pedido de reposición consume saldo de promoción y actualiza `unid_restantes` | `pedidos/services.py` |
| 5.5 | Descontar bidones del `Cliente` al entregar y sumarlos al devolver (integrado con T-3.4) | `logistica/services.py` |

✅ **Aceptación:** comprar "Paga 3 Lleva 4" crea un saldo de 1 bidón con vencimiento a 30 días; tres pedidos parciales lo consumen; al día 31 el comando lo expira.

---

### FASE 6 — Pagos parciales y pedido automático 💳
**Objetivo:** RF-13 y RF-18 (completar la HU-5 del informe).
**Esfuerzo:** ~8 h · **Riesgo:** bajo · **Dependencias:** Fase 4

| # | Tarea | Detalle |
|:--:|---|---|
| 6.1 | **RF-04 completo:** bloquear (no solo marcar con badge) el checkout de clientes con **<2 teléfonos o 0 direcciones** | `pedidos/views.py:checkout` |
| 6.2 | **RF-13 completo:** vista de **cobro manual**: registrar pago parcial con monto, fecha, método y comprobante. Al cubrir el total → estado `Pagado` (HU-5, criterio 3 del informe) | `pedidos/views.py` + template |
| 6.3 | **RF-18:** `PedidoAutomatico` en el perfil del cliente (producto, cantidad, periodicidad quincenal, activo sí/no, fecha de próximo envío) + comando generador | `pedidos/models.py` |
| 6.4 | Panel de caja: ingresos por método de pago y por día | `templates/dashboard/` |

✅ **Aceptación:** 3 pagos parciales de $10.000 sobre un pedido de $25.000 dejan saldo $5.000 y **no** lo marcan pagado; el cuarto sí.

---

### FASE 7 — QA, producción y tesis 🎓
**Objetivo:** Mes 12.
**Esfuerzo:** ~16 h · **Riesgo:** bajo · **Dependencias:** todas

| # | Tarea | Detalle |
|:--:|---|---|
| 7.1 | **Tests** (H-10): escribir la suite que hoy no existe | |
| 7.2 | └ `test_permisos.py` — matriz de roles × vistas (detecta H-5 si vuelve) | `apps/autenticacion/tests.py` |
| 7.3 | └ `test_carrito.py` — RF-12 stock y concurrencia | `apps/carrito/tests.py` |
| 7.4 | └ `test_pedidos.py` — `transaction.atomic`, descuento de stock, estados | `apps/pedidos/tests.py` |
| 7.5 | └ `test_logistica.py` — RF-17 agrupación, RF-19 impacto en `Pedido` | `apps/logistica/tests.py` |
| 7.6 | └ `test_cuentas.py` — RF-05 y RF-14 semaforización | `apps/cuentas/tests.py` |
| 7.7 | └ `test_buscador.py` — RF-07 normalización y fuzzy | `apps/buscador/tests.py` |
| 7.8 | **`settings/production.py`** (H-9): `DEBUG=False`, `ALLOWED_HOSTS` reales, `SECRET_KEY` y credenciales de MP por entorno, `STATIC_ROOT`, `MEDIA_ROOT` | `settings/production.py` |
| 7.9 | `python manage.py check --deploy --settings=distribuidora.settings.production` limpio | |
| 7.10 | Reescribir el informe de avances con el cronograma de §3 y las decisiones C-1…C-11 | informe |
| 7.11 | **Verificar el DER del informe contra el esquema real** (ver §0) | informe |
| 7.12 | Bump de `CONTEXT.md` a v5.0 final | `.agents/CONTEXT.md` |

✅ **Aceptación:** `manage.py test` ejecuta **todas** las suites en verde y `check --deploy` no reporta problemas de seguridad.

---

## 7. 🔗 Dependencias entre fases

```
FASE 0 (documentación)
   └─► FASE 1 (desbloqueo: grupos, pagos, permisos)
          └─► FASE 2 (unificar Empleado + RNF-02)
                 └─► FASE 3 (logística ↔ Pedido)
                        └─► FASE 4 (cuentas corrientes + abonos)
                               ├─► FASE 5 (bidones + promociones)
                               └─► FASE 6 (pagos parciales + RF-18)
                                      └─► FASE 7 (QA + tesis)
```

> ⚠️ **Fase 2 y Fase 3 son las de mayor riesgo.** Son la única oportunidad de corregir el modelo antes de que haya datos reales. No conviene saltearlas.

---

## 8. ❓ Decisiones que requieren criterio del equipo

Estas **no** son técnicas: cambian el alcance de la tesis y las debe decidir el equipo.

| # | Pregunta | Opciones | Recomendación |
|:--:|---|---|---|
| D-1 | ¿"VIP" es un tipo de cliente o una etiqueta de "Premium"? | (a) 2 tipos, "VIP" como etiqueta **(código actual)** · (b) 3 tipos reales | **(a)** — ya implementado, y el informe RF-05 lo avala |
| D-2 | ¿CBV o FBV? | (a) FBV, reescribir el informe **(código actual)** · (b) refactorizar a CBV | **(a)** |
| D-3 | ¿RF-20 "gastos por proveedor" entra en el alcance? | (a) sí, Mes 11 · (b) fuera de alcance, declarado | **(b)** si el tiempo es corto; declararlo es mejor que dejarlo fantasma |
| D-4 | ¿MercadoPago es indispensable para la entrega? | (a) obligatorio · (b) opcional | **(b)** — ya está implementado; dejarlo como canal opcional evita que un corte de red bloquee la operatoria. El webhook se conserva, pero no debe ser condición para emitir el pedido. |
| D-5 | ¿Qué SGBD para producción? | (a) SQLite (ya justificadísimo en el informe, págs. 9–10) · (b) PostgreSQL | **(a)** — la justificación del informe es sólida y es coherente con el uso académico |
| D-6 | ¿Se migra `celular1`/`celular2` de `Usuario`? | (a) deprecar y migrar a `TelefonoContacto` **(deuda técnica de `CONTEXT.md` §11)** · (b) mantener | **(a)** — la señal ya lo migra; cerrar la deuda elimina una ambigüedad en el RF-01 |

---

## 9. ✅ Checklist de cierre del proyecto

- [x] `manage.py check` → 0 issues
- [x] `makemigrations --check --dry-run` → sin cambios
- [ ] `manage.py test` → todas las suites en verde *(hoy: 29 tests de permisos/RNF-02)*
- [x] `manage.py check --deploy --settings=distribuidora.settings.production` → limpio
- [ ] RF-01 … RF-19 + RNF-01 … RNF-03 con estado ✅ en la matriz de §4
- [ ] Cada RF tiene **al menos un test** que lo cubra
- [x] `SECRET_KEY` fuera del repositorio
- [ ] `CONTEXT.md` v5.0 refleja el código final *(hoy: v4.0)*
- [ ] Los 9 `tests.py` tienen contenido *(hoy: solo `apps/permisos/tests.py`)*
- [ ] El informe de avances usa el cronograma de §3 y no contradice al código
- [ ] El DER del informe fue verificado contra el esquema real (§0)
- [ ] Ningún hallazgo **H-1 … H-16** sigue abierto *(cerrados: H-1, H-2, H-3, H-5, H-6, H-7, H-8, H-9, H-15)*

---

*Documento generado el 30/09/2026 a partir del commit `5362ab1`, del texto extraído del Informe de Avances (Julio 2026) de MASSON Lucas (L.U. 37492) y de `.agents/CONTEXT.md` v3.1.*
*Actualizar este archivo tras cada fase completada.*
