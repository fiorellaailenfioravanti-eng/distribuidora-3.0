# 🚚 Fase 3 — Plan de Logística: Rutas de Reparto, Repartidores y Camiones

> **Estado:** 📝 Plan v3 (incorpora decisiones del 30/09/2026) — **pendiente de aprobación. No implementado aún.**
> **Fases previas:** Fase 1 y Fase 2 ✅ completadas (ver `PROCEDURE.md`).
> **Objetivo:** cerrar **RF-16**, **RF-17** y **RF-19**, y habilitar la operación real de
> reparto: calendario por zona, clientes frecuentes, carga del camión, envases de bidón,
> ventas en la calle y cobro.

---

## 0. Definiciones del equipo (base del diseño)

1. Cada **zona tiene días de reparto predefinidos**; la fecha estimada de un pedido es el
   próximo día de reparto de su zona. La web la muestra como **estimativa** y la empresa
   luego la **confirma** (WhatsApp/SMS/teléfono).
2. La hoja de ruta se genera **por día + zona**, combinando **clientes frecuentes** de esa
   zona **+ pedidos** de esa zona. El administrador **elige manualmente** a quién llevar y
   **cuántos bidones**.
3. La hoja **se confirma manualmente** por el **administrador** recién al cargar el camión;
   hasta ese momento es editable. **El pedido pasa a «En Camino» al confirmarse la hoja**.
4. El camión puede llevar **más de lo pedido** → se registra la **carga** al salir y el
   **regreso** (sobrantes) al volver. Capacidad en **botellones** (no limita productos chicos).
5. El repartidor puede **agregar paradas/ventas en la calle** y **registrar el cobro**.
6. Los pedidos pueden pagarse **al repartidor en el momento o después**.
7. **Bidón retornable:** se entrega el bidón **lleno** y se **retira el vacío**. Si el
   cliente no lo devuelve, se **vende el envase** y se cobra. Todo se registra junto.

---

## 1. Modelo de datos objetivo

### 1.1 Calendario por zona

| Modelo / campo | Descripción |
|---|---|
| `Zona.dias_reparto` | Días de la semana de reparto de la zona (p. ej. martes y viernes). |
| `CalendarioExcepcion(fecha, zona, tipo, motivo)` | Feriados/suspensiones/días extra (`suspende` \| `agrega`), porque «puede variar por feriados o días no laborables». |

`proxima_fecha_de_reparto(zona, desde)` → próximo día según calendario menos excepciones.

### 1.2 Pedido

| Cambio | Descripción |
|---|---|
| `fecha_estimada_entrega` (Date) | Calculada en el checkout por zona. Estimativa, editable tras confirmar con el cliente. |
| `fecha_entrega` (Date) | Fecha real/confirmada (al confirmarse la hoja). |
| `origen` | `WEB` \| `ADMIN` \| `REPARTIDOR`. |
| `confirmado_por_empresa` (Bool) | La empresa validó la fecha con el cliente. |

Estados actuales sin cambios: `Pendiente`, `Confirmado`, `En Camino`, `Entregado`, `Cancelado`.

### 1.3 Cliente

| Cambio | Descripción |
|---|---|
| `tipo` | `registrado` (tiene cuenta) \| `pasajero` (creado por el repartidor, sin cuenta). Un pasajero puede registrarse luego. |
| `es_frecuente` (Bool) | Se marca para que aparezca en la **pregeneración** de hojas de ruta de su zona/día. |
| `cantidad_recurrente_default` (Int) | Botellones habituales (precarga la parada; el admin la ajusta). |

### 1.4 Producto y envases

| Cambio | Descripción |
|---|---|
| `Producto.es_envase` (Bool) | Marca el producto que representa al **bidón vacío** (envase). |
| `Producto.envase` FK self (null) | En el producto **lleno**, apunta al envase que debe retirarse al entregar. |
| `Producto.es_retornable` (Bool) | Producto cuyo envase se retira. |

### 1.5 Parada (`DetalleHojaRuta`) — pieza central

| Campo | Descripción |
|---|---|
| `pedido` FK → `Pedido` (`null`, `SET_NULL`, `related_name='paradas'`) | Vínculo real con el pedido. |
| `cliente` FK → `Cliente` (`null`) | Cliente de la parada. |
| `es_frecuente` (Bool) | Proviene de un cliente frecuente. |
| `cantidad_bidones` (Int) | Botellones **llenos** planeados. |
| `envases_retirados` (Int) | Bidones **vacíos** devueltos por el cliente. |
| `envases_vendidos` (Int) | Envases no devueltos (se cobran). |
| `pedido_ref` | Se **conserva** como referencia/observación manual. |

> **Regla unificadora:** *toda parada útil se respalda en un `Pedido`*. El cliente frecuente
> sin pedido genera un `Pedido` `origen='ADMIN'`; la venta en calle genera uno `origen='REPARTIDOR'`.
> Así stock, cobro, envases, capacidad e historial se calculan siempre igual.

### 1.6 Hoja de ruta (`HojaRuta`) — ciclo de vida

| Campo | Descripción |
|---|---|
| `zona` FK | Hoja **por día + zona**. |
| `estado` | `Borrador` → `Confirmada` (salió el camión) → `Cerrada`. |
| `confirmada_por`, `fecha_confirmacion` | Confirmación **solo del administrador**. |
| `fecha_salida`, `fecha_regreso` | Control del viaje. |
| `generada_automaticamente` (Bool) | Origen. |
| `fecha`, `creado_por` | Ya existen. |

`RutaReparto` (plantilla zona+día+repartidor+camión) se mantiene como **configuración por
defecto** para prellenar la hoja, pero la generación real es por **fecha + zona**.

### 1.7 Camión y carga

| Modelo / campo | Descripción |
|---|---|
| `Camion.capacidad_botellones` (Int, default 30) | Se registra con los datos del camión. **Solo limita botellones**, no productos chicos. |
| `CargaHojaRuta(hoja_ruta, producto, cantidad_cargada, cantidad_entregada, cantidad_retornada)` | Carga real al salir y sobrantes al volver. Permite cargar **más de lo pedido**. |

**Control de capacidad:** al confirmar se compara la suma de `cantidad_bidones` contra
`capacidad_botellones` y se **advierte** si se supera (no se bloquea).

### 1.8 Resumen de migraciones

| # | App | Cambio |
|:--:|---|---|
| M1 | `logistica` | `Zona.dias_reparto` + `CalendarioExcepcion` |
| M2 | `pedidos` | `fecha_estimada_entrega`, `fecha_entrega`, `origen`, `confirmado_por_empresa` |
| M3 | `clientes` | `tipo`, `es_frecuente`, `cantidad_recurrente_default` |
| M4 | `productos` | `es_envase`, `envase`, `es_retornable` |
| M5 | `logistica` | `DetalleHojaRuta.pedido` + `cliente` + `es_frecuente` + `cantidad_bidones` + `envases_retirados` + `envases_vendidos` |
| M6 | `logistica` | `HojaRuta.zona` + estados + fechas de confirmación/salida/regreso |
| M7 | `logistica` | `Camion.capacidad_botellones` + `CargaHojaRuta` |

> Tablas de logística vacías (H-13): sin backfill real; salvaguardas `RunPython` donde aplique.

---

## 2. Flujos

### 2.1 Cliente hace un pedido (checkout)
1. Elige dirección → barrio → zona.
2. El sistema calcula `fecha_estimada_entrega` (próximo día de reparto de la zona) y la
   muestra como **estimativa**.
3. La empresa **confirma** con el cliente → `confirmado_por_empresa=True`.

### 2.2 Administrador planifica el reparto («Planificar reparto»)
1. Elige **fecha** (p. ej. martes 10/03).
2. Elige **zona** (prellenada por el calendario; editable por feriados).
3. El sistema lista:
   - **Clientes frecuentes** de la zona (con cantidad sugerida).
   - **Pedidos** de clientes de la zona con `fecha_estimada_entrega ≤ fecha` y estado
     `Pendiente`/`Confirmado`, aún no asignados.
4. El admin **selecciona** a quién llevar y **cuántos botellones** (puede sumar clientes
   por otros medios).
5. Guarda la hoja en **Borrador** (editable). Queda en el **historial por fecha de entrega**.

### 2.3 Confirmación y salida del camión (manual, solo admin)
1. Se carga el camión; se ingresa la **carga real** por producto (`CargaHojaRuta`), que
   puede superar lo pedido.
2. Se **confirma**: pedidos → **En Camino**, `fecha_salida`, `fecha_entrega`, `confirmada_por`.
3. La hoja puede seguir recibiendo **paradas en la calle**.

### 2.4 Reparto en la calle (app del repartidor, mobile-first)
- Ver la hoja del día con la nota de seguridad filtrada (RNF-02 ✅).
- Marcar parada: `Entregado` / `Cancelado` / `Reprogramado`.
- Registrar por parada: botellones **llenos entregados**, **vacíos retirados**, **envases vendidos**.
- **Agregar parada/venta** (cliente existente, pasajero nuevo o marcado como frecuente) →
  crea `Pedido` `origen='REPARTIDOR'` + parada.
- **Registrar cobro** (efectivo/transferencia) → `PagoPedido`.
- **Registrar el regreso**: sobrantes → stock automáticamente; envases retirados → stock de envase.

### 2.5 Impacto en Pedido, stock y envases (RF-19)

| Evento | Pedido | Stock |
|---|---|---|
| Entrega bidón lleno | `Entregado`, `fecha_entrega` | −stock producto lleno |
| Retiro de vacío | — | +stock **envase** (reutilizable) |
| Envase vendido | suma cargo al pedido | −stock **envase** |
| Parada `Cancelado` | `Cancelado` | devuelve lo no entregado |
| `Reprogramado` | vuelve a `Confirmado` para otra hoja | — |
| Regreso del camión | — | devuelve sobrantes al stock automáticamente |
| Cobro | `PagoPedido` Aprobado | — |

---

## 3. Pantallas (URLs)

| Vista | URL | Quién |
|---|---|---|
| CRUD Zonas (+ días de reparto, excepciones) | `/logistica/zonas/` | Admin/Vendedor |
| CRUD Barrios | `/logistica/barrios/…` | Admin/Vendedor |
| Clientes frecuentes | `/clientes/frecuentes/` | Admin/Vendedor |
| CRUD Camiones (+ capacidad) | `/logistica/camiones/` | Admin/Vendedor |
| Envases / productos retornables | `/productos/envases/` | Admin |
| **Planificar reparto** | `/logistica/planificar/` | Admin/Vendedor |
| Vista previa | `/logistica/planificar/preview/` | Admin/Vendedor |
| **Confirmar / cargar camión** | `/logistica/hoja/<pk>/confirmar/` | **Solo Admin** |
| Registrar regreso | `/logistica/hoja/<pk>/regreso/` | Admin/Vendedor |
| Historial de hojas | `/logistica/rutas/` (por fecha/zona) | Admin/Vendedor |
| Mi ruta hoy | `/logistica/mi-ruta/` (existente) | Repartidor asignado |
| Agregar parada/venta en calle | `/logistica/hoja/<pk>/agregar-parada/` | Repartidor asignado |
| Imprimir hoja | `/logistica/hoja/<pk>/imprimir/` (existente) | Admin/Vendedor/Repartidor |

Permisos vía `apps/permisos/roles.py` (sin duplicar lógica).

---

## 4. Sub-fases de implementación

| Sub-fase | Contenido | Entregable | Estado |
|---|---|---|---|
| **3A · Modelo y calendario** | M1–M7, `proxima_fecha_de_reparto()`, admin | migraciones + tests | ✅ Hecho |
| **3B · Generación de hoja** | «Planificar reparto»: frecuentes + pedidos, selección y cantidades, historial | `logistica/services.py::construir_borrador()` | ✅ Hecho |
| **3C · Confirmación y viaje** | Carga real, confirmar (→ En Camino), salida/regreso, control de capacidad | `confirmar_hoja()`, `registrar_regreso()` | ✅ Hecho |
| **3D · Calle, envases y cobro** | Repartidor agrega parada/venta, cobra, retira/deposita envases | vistas repartidor | ✅ Hecho |
| **3E · Checkout** | Fecha estimada por zona mostrada al cliente | `pedidos/views.py` | ✅ Hecho |
| **3F · Datos y cierre** | Seed de demo, tests, docs | `apps/logistica/tests.py` | ✅ Hecho |

> **Progreso 3A–3D (30/09/2026).** Verificación: `check` sin issues, `makemigrations --check`
> sin cambios y **55 tests OK** (26 de `apps.logistica`). Decisión de stock: el descuento se hace
> **al cargar el camión** (se quitó del checkout) y el regreso devuelve **solo sobrantes**;
> el envase tiene **stock propio** (`es_envase`).

---

## 5. Decisiones tomadas

| # | Decisión |
|:--:|---|
| D1 | Calendario **por zona** con días predefinidos + excepciones; la empresa confirma la fecha al cliente. |
| D2 | Hoja **por día + zona**; combina frecuentes + pedidos; confirmación **manual del administrador**. |
| D3 | **1 pedido = 1 parada**. |
| D4 | El pedido pasa a **En Camino al confirmarse la hoja**. |
| D5 | Capacidad del camión en **botellones** (default ~30); solo afecta botellones; **advierte**, no bloquea. |
| D6 | `pedido_ref` se **conserva** como referencia manual. |
| D7 | Los pedidos pueden pagarse **al repartidor o después**. |
| D8 | El repartidor puede **agregar paradas/ventas** (guarda cliente + parada + venta) y marcarlo **frecuente**. |
| D9 | Al terminar se **registra el regreso** y los sobrantes vuelven al stock. |
| D10 | **Bidón retornable:** producto del catálogo; se entrega lleno y se retira el vacío; el envase no devuelto se **vende**. |
| D11 | Clientes: `registrado` o `pasajero` (creado por el repartidor); ambos pueden marcarse **frecuentes**. |
| D12 | Solo el **administrador** confirma la hoja. |
| D13 | Los clientes frecuentes **siempre** generan `Pedido`. |

---

## 6. Puntos menores a confirmar durante la implementación

| # | Pregunta | Recomendación |
|:--:|---|---|
| P1 | Precio del **envase** (bidón vacío) y del agua por separado. | Cargar ambos como productos del catálogo. |
| P2 | Si el cliente devuelve más vacíos de los que se le entregan (stock previo). | Permitir `envases_retirados` distinto de llenos. |
| P3 | ¿Los envases retirados vuelven al stock de inmediato o pasan por «en revisión/lavado»? | Estado intermedio opcional. |
| P4 | ¿Se cobra el envase en el momento o queda como deuda del cliente? | En el momento, vía `PagoPedido`. |
| P5 | Recordatorio automático de confirmación a las 7 am. | A futuro (fuera de 3A–3F). |

> Nota: el control de envases **roza la Fase 5 (bidones)** del `PROCEDURE.md`; se implementa
> lo mínimo en 3D y se profundiza en Fase 5.

---

## 7. Criterios de aceptación

- [ ] Cada zona tiene días de reparto; el checkout muestra la **fecha estimada** correcta.
- [x] «Planificar reparto» lista frecuentes + pedidos de la zona y permite elegir paradas y
      cantidades; la hoja queda en **Borrador** y es editable.
- [x] Al **confirmar** (solo admin), los pedidos pasan a **En Camino**; se registran salida y carga.
- [x] Se puede **cargar más** de lo pedido y **registrar el regreso** (sobrantes → stock).
- [x] Se registran **llenos entregados / vacíos retirados / envases vendidos**, con el cobro.
- [x] El repartidor puede **agregar parada/venta**, marcar cliente frecuente y cobrar.
- [x] Historial de hojas consultable por fecha/zona.
- [x] `manage.py check`, `makemigrations --check` y `manage.py test` en verde.

---

## 8. Notas de alcance

Alcance **mucho mayor** que las ~10 h del Fase 3 original: calendario, recurrencia, envases,
carga/regreso y ventas en calle. Se implementa **por sub-fases (3A→3F)**, aprobando cada una.
Se recomienda empezar por **3A (modelo y calendario)**, que es la base de todo.

*Plan v3 — 30/09/2026. Al aprobarse, se implementa en el orden de §4 y se marca el avance en `PROCEDURE.md`.*

---

## 9. Plan de implementación detallado (checklist por archivo)

> Convenciones: código y comentarios en español; sin comentarios salvo los ya existentes;
> verificación obligatoria al cierre de cada sub-fase.

### 3A · Modelo y calendario

**`apps/logistica/models.py`**
- [ ] `Zona.dias_reparto` (`CharField`, ej. `"1,4"`) + `get_dias_reparto()`, `set_dias_reparto()`, `incluye_dia(w)`.
- [ ] `CalendarioExcepcion(fecha, zona=null, tipo∈{suspende,agrega}, motivo)`.
- [ ] `Camion.capacidad_botellones` (Int, default 30).
- [ ] `HojaRuta`: `zona` FK; `ruta_reparto` → `null=True, SET_NULL`; estados `Borrador/Confirmada/Cerrada`; `confirmada_por`, `fecha_confirmacion`, `fecha_salida`, `fecha_regreso`, `generada_automaticamente`.
- [ ] `DetalleHojaRuta`: `pedido` FK, `cliente` FK, `es_frecuente`, `cantidad_bidones`, `envases_retirados`, `envases_vendidos`.
- [ ] `CargaHojaRuta(hoja_ruta, producto, cantidad_cargada, cantidad_entregada, cantidad_retornada)`.

**`apps/pedidos/models.py`**
- [ ] `Pedido`: `fecha_estimada_entrega`, `fecha_entrega`, `origen∈{WEB,ADMIN,REPARTIDOR}`, `confirmado_por_empresa`.

**`apps/clientes/models.py`**
- [ ] `Cliente`: `tipo_registro∈{registrado,pasajero}`, `es_frecuente`, `cantidad_recurrente_default`.

**`apps/productos/models.py`**
- [ ] `Producto`: `es_envase`, `es_retornable`, `envase` (FK self).

**`apps/logistica/services.py` (nuevo)**
- [ ] `fecha_es_de_reparto(zona, fecha)` (weekday + excepciones).
- [ ] `proxima_fecha_de_reparto(zona, desde=None)`.
- [ ] `siguiente_dia_valido(zona, fecha)`.

**Forms / admin**
- [ ] `ZonaForm` con `dias_reparto` (MultipleChoice + widgets).
- [ ] `CamionForm` con `capacidad_botellones`.
- [ ] `admin.py`: registrar `CalendarioExcepcion`, `CargaHojaRuta`; inline/fields nuevos.

**Migraciones**
- [ ] `makemigrations logistica pedidos clientes productos`.

**Tests (`apps/logistica/tests.py`)**
- [ ] `fecha_es_de_reparto` con/sin excepciones.
- [ ] `proxima_fecha_de_reparto` salta domingos/feriados.
- [ ] Integridad de nuevos campos.

### 3B · Generación de hoja («Planificar reparto»)

- [ ] `services.construir_borrador(fecha, zona)` → lista de frecuentes + pedidos candidatos.
- [ ] `services.crear_hoja_borrador(fecha, zona, seleccion, empleado, camion, usuario)`.
- [ ] Vistas `planificar_reparto`, `preview_hoja`, `confirmar_borrador`.
- [ ] URLs + templates (`planificar.html`, `preview.html`); historial en `listar_rutas`.
- [ ] Tests: agrupación, dedup, pedido sin zona excluido.

### 3C · Confirmación y viaje

- [ ] `services.confirmar_hoja(hoja, usuario, cargas)` → `Confirmada`, pedidos `En Camino`, `fecha_salida`.
- [ ] `services.registrar_regreso(hoja, cargas)` → sobrantes a stock, `fecha_regreso`, `Cerrada`.
- [ ] Control de capacidad (advierte, no bloquea).
- [ ] Vistas + templates de carga/confirmación/regreso. Solo admin confirma.
- [ ] Tests de impacto en stock.

### 3D · Calle, envases y cobro

- [ ] Repartidor agrega parada/venta (`Pedido` origen REPARTIDOR + parada).
- [ ] Registro de llenos entregados / vacíos retirados / envases vendidos.
- [ ] Cobro (`PagoPedido`) efectivo/transferencia.
- [ ] Cliente pasajero / marcar frecuente.
- [ ] Impacto en `Pedido` y stock en `marcar_estado` (Entregado/Cancelado) atómico.
- [ ] Tests.

### 3F · Datos y cierre | Seed de demo, tests, docs | `apps/logistica/tests.py` | ✅ Hecho |

> **Progreso 3A–3D (30/09/2026).** Verificación: `check` sin issues, `makemigrations --check`
> sin cambios y **55 tests OK** (26 de `apps.logistica`). Decisión de stock: el descuento se hace
> **al cargar el camión** (se quitó del checkout) y el regreso devuelve **solo sobrantes**;
> el envase tiene **stock propio** (`es_envase`).

---

## 5. Decisiones tomadas

| # | Decisión |
|:--:|---|
| D1 | Calendario **por zona** con días predefinidos + excepciones; la empresa confirma la fecha al cliente. |
| D2 | Hoja **por día + zona**; combina frecuentes + pedidos; confirmación **manual del administrador**. |
| D3 | **1 pedido = 1 parada**. |
| D4 | El pedido pasa a **En Camino al confirmarse la hoja**. |
| D5 | Capacidad del camión en **botellones** (default ~30); solo afecta botellones; **advierte**, no bloquea. |
| D6 | `pedido_ref` se **conserva** como referencia manual. |
| D7 | Los pedidos pueden pagarse **al repartidor o después**. |
| D8 | El repartidor puede **agregar paradas/ventas** (guarda cliente + parada + venta) y marcarlo **frecuente**. |
| D9 | Al terminar se **registra el regreso** y los sobrantes vuelven al stock. |
| D10 | **Bidón retornable:** producto del catálogo; se entrega lleno y se retira el vacío; el envase no devuelto se **vende**. |
| D11 | Clientes: `registrado` o `pasajero` (creado por el repartidor); ambos pueden marcarse **frecuentes**. |
| D12 | Solo el **administrador** confirma la hoja. |
| D13 | Los clientes frecuentes **siempre** generan `Pedido`. |

---

## 6. Puntos menores a confirmar durante la implementación

| # | Pregunta | Recomendación |
|:--:|---|---|
| P1 | Precio del **envase** (bidón vacío) y del agua por separado. | Cargar ambos como productos del catálogo. |
| P2 | Si el cliente devuelve más vacíos de los que se le entregan (stock previo). | Permitir `envases_retirados` distinto de llenos. |
| P3 | ¿Los envases retirados vuelven al stock de inmediato o pasan por «en revisión/lavado»? | Estado intermedio opcional. |
| P4 | ¿Se cobra el envase en el momento o queda como deuda del cliente? | En el momento, vía `PagoPedido`. |
| P5 | Recordatorio automático de confirmación a las 7 am. | A futuro (fuera de 3A–3F). |

> Nota: el control de envases **roza la Fase 5 (bidones)** del `PROCEDURE.md`; se implementa
> lo mínimo en 3D y se profundiza en Fase 5.

---

## 7. Criterios de aceptación

- [ ] Cada zona tiene días de reparto; el checkout muestra la **fecha estimada** correcta.
- [x] «Planificar reparto» lista frecuentes + pedidos de la zona y permite elegir paradas y
      cantidades; la hoja queda en **Borrador** y es editable.
- [x] Al **confirmar** (solo admin), los pedidos pasan a **En Camino**; se registran salida y carga.
- [x] Se puede **cargar más** de lo pedido y **registrar el regreso** (sobrantes → stock).
- [x] Se registran **llenos entregados / vacíos retirados / envases vendidos**, con el cobro.
- [x] El repartidor puede **agregar parada/venta**, marcar cliente frecuente y cobrar.
- [x] Historial de hojas consultable por fecha/zona.
- [x] `manage.py check`, `makemigrations --check` y `manage.py test` en verde.

---

## 8. Notas de alcance

Alcance **mucho mayor** que las ~10 h del Fase 3 original: calendario, recurrencia, envases,
carga/regreso y ventas en calle. Se implementa **por sub-fases (3A→3F)**, aprobando cada una.
Se recomienda empezar por **3A (modelo y calendario)**, que es la base de todo.

*Plan v3 — 30/09/2026. Al aprobarse, se implementa en el orden de §4 y se marca el avance en `PROCEDURE.md`.*

---

## 9. Plan de implementación detallado (checklist por archivo)

> Convenciones: código y comentarios en español; sin comentarios salvo los ya existentes;
> verificación obligatoria al cierre de cada sub-fase.

### 3A · Modelo y calendario

**`apps/logistica/models.py`**
- [ ] `Zona.dias_reparto` (`CharField`, ej. `"1,4"`) + `get_dias_reparto()`, `set_dias_reparto()`, `incluye_dia(w)`.
- [ ] `CalendarioExcepcion(fecha, zona=null, tipo∈{suspende,agrega}, motivo)`.
- [ ] `Camion.capacidad_botellones` (Int, default 30).
- [ ] `HojaRuta`: `zona` FK; `ruta_reparto` → `null=True, SET_NULL`; estados `Borrador/Confirmada/Cerrada`; `confirmada_por`, `fecha_confirmacion`, `fecha_salida`, `fecha_regreso`, `generada_automaticamente`.
- [ ] `DetalleHojaRuta`: `pedido` FK, `cliente` FK, `es_frecuente`, `cantidad_bidones`, `envases_retirados`, `envases_vendidos`.
- [ ] `CargaHojaRuta(hoja_ruta, producto, cantidad_cargada, cantidad_entregada, cantidad_retornada)`.

**`apps/pedidos/models.py`**
- [ ] `Pedido`: `fecha_estimada_entrega`, `fecha_entrega`, `origen∈{WEB,ADMIN,REPARTIDOR}`, `confirmado_por_empresa`.

**`apps/clientes/models.py`**
- [ ] `Cliente`: `tipo_registro∈{registrado,pasajero}`, `es_frecuente`, `cantidad_recurrente_default`.

**`apps/productos/models.py`**
- [ ] `Producto`: `es_envase`, `es_retornable`, `envase` (FK self).

**`apps/logistica/services.py` (nuevo)**
- [ ] `fecha_es_de_reparto(zona, fecha)` (weekday + excepciones).
- [ ] `proxima_fecha_de_reparto(zona, desde=None)`.
- [ ] `siguiente_dia_valido(zona, fecha)`.

**Forms / admin**
- [ ] `ZonaForm` con `dias_reparto` (MultipleChoice + widgets).
- [ ] `CamionForm` con `capacidad_botellones`.
- [ ] `admin.py`: registrar `CalendarioExcepcion`, `CargaHojaRuta`; inline/fields nuevos.

**Migraciones**
- [ ] `makemigrations logistica pedidos clientes productos`.

**Tests (`apps/logistica/tests.py`)**
- [ ] `fecha_es_de_reparto` con/sin excepciones.
- [ ] `proxima_fecha_de_reparto` salta domingos/feriados.
- [ ] Integridad de nuevos campos.

### 3B · Generación de hoja («Planificar reparto»)

- [ ] `services.construir_borrador(fecha, zona)` → lista de frecuentes + pedidos candidatos.
- [ ] `services.crear_hoja_borrador(fecha, zona, seleccion, empleado, camion, usuario)`.
- [ ] Vistas `planificar_reparto`, `preview_hoja`, `confirmar_borrador`.
- [ ] URLs + templates (`planificar.html`, `preview.html`); historial en `listar_rutas`.
- [ ] Tests: agrupación, dedup, pedido sin zona excluido.

### 3C · Confirmación y viaje

- [ ] `services.confirmar_hoja(hoja, usuario, cargas)` → `Confirmada`, pedidos `En Camino`, `fecha_salida`.
- [ ] `services.registrar_regreso(hoja, cargas)` → sobrantes a stock, `fecha_regreso`, `Cerrada`.
- [ ] Control de capacidad (advierte, no bloquea).
- [ ] Vistas + templates de carga/confirmación/regreso. Solo admin confirma.
- [ ] Tests de impacto en stock.

### 3D · Calle, envases y cobro

- [ ] Repartidor agrega parada/venta (`Pedido` origen REPARTIDOR + parada).
- [ ] Registro de llenos entregados / vacíos retirados / envases vendidos.
- [ ] Cobro (`PagoPedido`) efectivo/transferencia.
- [ ] Cliente pasajero / marcar frecuente.
- [ ] Impacto en `Pedido` y stock en `marcar_estado` (Entregado/Cancelado) atómico.
- [ ] Tests.

### 3F · Datos y cierre | Seed de demo, tests, docs | `apps/logistica/tests.py` | ✅ Hecho |

> **Progreso 3A–3D (30/09/2026).** Verificación: `check` sin issues, `makemigrations --check`
> sin cambios y **55 tests OK** (26 de `apps.logistica`). Decisión de stock: el descuento se hace
> **al cargar el camión** (se quitó del checkout) y el regreso devuelve **solo sobrantes**;
> el envase tiene **stock propio** (`es_envase`).

---

## 5. Decisiones tomadas

| # | Decisión |
|:--:|---|
| D1 | Calendario **por zona** con días predefinidos + excepciones; la empresa confirma la fecha al cliente. |
| D2 | Hoja **por día + zona**; combina frecuentes + pedidos; confirmación **manual del administrador**. |
| D3 | **1 pedido = 1 parada**. |
| D4 | El pedido pasa a **En Camino al confirmarse la hoja**. |
| D5 | Capacidad del camión en **botellones** (default ~30); solo afecta botellones; **advierte**, no bloquea. |
| D6 | `pedido_ref` se **conserva** como referencia manual. |
| D7 | Los pedidos pueden pagarse **al repartidor o después**. |
| D8 | El repartidor puede **agregar paradas/ventas** (guarda cliente + parada + venta) y marcarlo **frecuente**. |
| D9 | Al terminar se **registra el regreso** y los sobrantes vuelven al stock. |
| D10 | **Bidón retornable:** producto del catálogo; se entrega lleno y se retira el vacío; el envase no devuelto se **vende**. |
| D11 | Clientes: `registrado` o `pasajero` (creado por el repartidor); ambos pueden marcarse **frecuentes**. |
| D12 | Solo el **administrador** confirma la hoja. |
| D13 | Los clientes frecuentes **siempre** generan `Pedido`. |

---

## 6. Puntos menores a confirmar durante la implementación

| # | Pregunta | Recomendación |
|:--:|---|---|
| P1 | Precio del **envase** (bidón vacío) y del agua por separado. | Cargar ambos como productos del catálogo. |
| P2 | Si el cliente devuelve más vacíos de los que se le entregan (stock previo). | Permitir `envases_retirados` distinto de llenos. |
| P3 | ¿Los envases retirados vuelven al stock de inmediato o pasan por «en revisión/lavado»? | Estado intermedio opcional. |
| P4 | ¿Se cobra el envase en el momento o queda como deuda del cliente? | En el momento, vía `PagoPedido`. |
| P5 | Recordatorio automático de confirmación a las 7 am. | A futuro (fuera de 3A–3F). |

> Nota: el control de envases **roza la Fase 5 (bidones)** del `PROCEDURE.md`; se implementa
> lo mínimo en 3D y se profundiza en Fase 5.

---

## 7. Criterios de aceptación

- [ ] Cada zona tiene días de reparto; el checkout muestra la **fecha estimada** correcta.
- [x] «Planificar reparto» lista frecuentes + pedidos de la zona y permite elegir paradas y
      cantidades; la hoja queda en **Borrador** y es editable.
- [x] Al **confirmar** (solo admin), los pedidos pasan a **En Camino**; se registran salida y carga.
- [x] Se puede **cargar más** de lo pedido y **registrar el regreso** (sobrantes → stock).
- [x] Se registran **llenos entregados / vacíos retirados / envases vendidos**, con el cobro.
- [x] El repartidor puede **agregar parada/venta**, marcar cliente frecuente y cobrar.
- [x] Historial de hojas consultable por fecha/zona.
- [x] `manage.py check`, `makemigrations --check` y `manage.py test` en verde.

---

## 8. Notas de alcance

Alcance **mucho mayor** que las ~10 h del Fase 3 original: calendario, recurrencia, envases,
carga/regreso y ventas en calle. Se implementa **por sub-fases (3A→3F)**, aprobando cada una.
Se recomienda empezar por **3A (modelo y calendario)**, que es la base de todo.

*Plan v3 — 30/09/2026. Al aprobarse, se implementa en el orden de §4 y se marca el avance en `PROCEDURE.md`.*

---

## 9. Plan de implementación detallado (checklist por archivo)

> Convenciones: código y comentarios en español; sin comentarios salvo los ya existentes;
> verificación obligatoria al cierre de cada sub-fase.

### 3A · Modelo y calendario

**`apps/logistica/models.py`**
- [ ] `Zona.dias_reparto` (`CharField`, ej. `"1,4"`) + `get_dias_reparto()`, `set_dias_reparto()`, `incluye_dia(w)`.
- [ ] `CalendarioExcepcion(fecha, zona=null, tipo∈{suspende,agrega}, motivo)`.
- [ ] `Camion.capacidad_botellones` (Int, default 30).
- [ ] `HojaRuta`: `zona` FK; `ruta_reparto` → `null=True, SET_NULL`; estados `Borrador/Confirmada/Cerrada`; `confirmada_por`, `fecha_confirmacion`, `fecha_salida`, `fecha_regreso`, `generada_automaticamente`.
- [ ] `DetalleHojaRuta`: `pedido` FK, `cliente` FK, `es_frecuente`, `cantidad_bidones`, `envases_retirados`, `envases_vendidos`.
- [ ] `CargaHojaRuta(hoja_ruta, producto, cantidad_cargada, cantidad_entregada, cantidad_retornada)`.

**`apps/pedidos/models.py`**
- [ ] `Pedido`: `fecha_estimada_entrega`, `fecha_entrega`, `origen∈{WEB,ADMIN,REPARTIDOR}`, `confirmado_por_empresa`.

**`apps/clientes/models.py`**
- [ ] `Cliente`: `tipo_registro∈{registrado,pasajero}`, `es_frecuente`, `cantidad_recurrente_default`.

**`apps/productos/models.py`**
- [ ] `Producto`: `es_envase`, `es_retornable`, `envase` (FK self).

**`apps/logistica/services.py` (nuevo)**
- [ ] `fecha_es_de_reparto(zona, fecha)` (weekday + excepciones).
- [ ] `proxima_fecha_de_reparto(zona, desde=None)`.
- [ ] `siguiente_dia_valido(zona, fecha)`.

**Forms / admin**
- [ ] `ZonaForm` con `dias_reparto` (MultipleChoice + widgets).
- [ ] `CamionForm` con `capacidad_botellones`.
- [ ] `admin.py`: registrar `CalendarioExcepcion`, `CargaHojaRuta`; inline/fields nuevos.

**Migraciones**
- [ ] `makemigrations logistica pedidos clientes productos`.

**Tests (`apps/logistica/tests.py`)**
- [ ] `fecha_es_de_reparto` con/sin excepciones.
- [ ] `proxima_fecha_de_reparto` salta domingos/feriados.
- [ ] Integridad de nuevos campos.

### 3B · Generación de hoja («Planificar reparto»)

- [ ] `services.construir_borrador(fecha, zona)` → lista de frecuentes + pedidos candidatos.
- [ ] `services.crear_hoja_borrador(fecha, zona, seleccion, empleado, camion, usuario)`.
- [ ] Vistas `planificar_reparto`, `preview_hoja`, `confirmar_borrador`.
- [ ] URLs + templates (`planificar.html`, `preview.html`); historial en `listar_rutas`.
- [ ] Tests: agrupación, dedup, pedido sin zona excluido.

### 3C · Confirmación y viaje

- [ ] `services.confirmar_hoja(hoja, usuario, cargas)` → `Confirmada`, pedidos `En Camino`, `fecha_salida`.
- [ ] `services.registrar_regreso(hoja, cargas)` → sobrantes a stock, `fecha_regreso`, `Cerrada`.
- [ ] Control de capacidad (advierte, no bloquea).
- [ ] Vistas + templates de carga/confirmación/regreso. Solo admin confirma.
- [ ] Tests de impacto en stock.

### 3D · Calle, envases y cobro

- [ ] Repartidor agrega parada/venta (`Pedido` origen REPARTIDOR + parada).
- [ ] Registro de llenos entregados / vacíos retirados / envases vendidos.
- [ ] Cobro (`PagoPedido`) efectivo/transferencia.
- [ ] Cliente pasajero / marcar frecuente.
- [ ] Impacto en `Pedido` y stock en `marcar_estado` (Entregado/Cancelado) atómico.
- [ ] Tests.

### 3E · Checkout con fecha estimada

- [x] Calcular y guardar `fecha_estimada_entrega` al crear el pedido; mostrar en checkout/detalle.
- [x] Test.

### 3F · Datos y cierre

- [x] Extender `seed_barrios.py` / comando `seed_logistica` con datos de demo.
- [x] Suite integral en `apps/logistica/tests.py`.
- [x] Actualizar `CONTEXT.md` y `PROCEDURE.md` (Fase 3 ✅ / parcial).
- [x] `check` + `makemigrations --check` + `test` en verde.