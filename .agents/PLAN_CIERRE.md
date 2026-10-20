# 🏁 Plan de Cierre — Fases 4.5 a 7

> **Propósito:** procedimiento detallado para terminar lo que falta de Distribuidora 3.0 / Aquadelluvia
> después de la Fase 4. Complementa (no reemplaza) el plan general de [`PROCEDURE.md`](PROCEDURE.md) §6.
>
> **Fecha:** 20/10/2026 · **Base analizada:** `main` @ `50dc6b2` + cambios sin commitear de Fases 1–4
> **Estado verificado hoy:** `check` 0 issues · `makemigrations --check` sin cambios · **86 tests OK**

---

## 0. Qué falta (resumen)

| Bloque | Requisitos / hallazgos | Esfuerzo | Riesgo |
|---|---|:--:|:--:|
| **Fase 4.5 — Consolidación** | Commits pendientes, `db.sqlite3`, webhook MP, docs | ~3 h | Bajo |
| **Fase 4.6 — Correcciones de auditoría** | H-18…H-37, R-1…R-8 de [`AUDITORIA.md`](AUDITORIA.md): pagos, roles, errores 500 | ~15 h | Medio |
| **Fase 5 — Bidones y promociones** | RF-08, RF-09, RF-10 | ~14 h | Medio |
| **Fase 6 — Pagos, checkout y pedido automático** | RF-04, RF-12, RF-13, RF-18 | ~12 h | Medio |
| **Fase 7 — QA, producción y tesis** | H-10, H-13, H-14, C-9, DER | ~16 h | Bajo |
| **Total** | 9 requisitos + 24 hallazgos | **~60 h** | |

Orden obligatorio: **4.5 → 4.6 → 5 → 6 → 7**. Las fases 5 y 6 sólo comparten `pedidos/` (ver §5); si se
paralelizan, 5 es dueña de `logistica/services.py` y 6 de `pedidos/views.py`.

---

## FASE 4.5 — Consolidación 🧹 (antes de escribir código nuevo)

**Por qué primero:** hoy `apps/cuentas`, `apps/abonos`, `apps/permisos` y 12 migraciones están **sin
versionar**. Cualquier accidente las pierde, y las migraciones de Fase 5 van a depender de ellas.

| # | Tarea | Detalle | Archivo |
|:--:|---|---|---|
| 4.5.1 | **Commitear Fases 1–4** en commits temáticos | (a) `permisos` + grupos + métodos de pago (Fase 1); (b) unificación `Empleado` + migraciones `logistica/0005-0008` (Fase 2); (c) `logistica/0009`, `pedidos/0004`, `productos/0004`, `clientes/0007` + templates de logística (Fase 3); (d) `cuentas` + `abonos` + dashboard (Fase 4); (e) `.agents/`, `CLAUDE.md`, `graphify-out/` | git |
| 4.5.2 | **Decidir `db.sqlite3`** | Está en `.gitignore` pero versionada. Recomendado: `git rm --cached db.sqlite3` y reemplazarla por `seed_logistica` + fixtures (decisión **F-D1**) | `.gitignore` |
| 4.5.3 | **Endurecer el webhook de MercadoPago** | Validar la cabecera `x-signature` con `MERCADOPAGO_WEBHOOK_SECRET` (si está configurado); comparar `transaction_amount` con lo adeudado antes de confirmar; registrar la excepción con `logging` en vez de tragarla | `apps/pedidos/views.py:307` |
| 4.5.4 | **Limpiar `PROCEDURE.md`** | Borrar las líneas duplicadas de hallazgos (26–27), arreglar la nota truncada de Fase 3 (241–244), marcar ✅ las tareas 3.1–3.7 | `.agents/PROCEDURE.md` |
| 4.5.5 | **Migrar los guards locales que quedan** | `es_vendedor_o_admin` sigue definido en `pedidos/views.py`; reemplazar por `apps.permisos.roles` (H-11) | `apps/pedidos/views.py` |

✅ **Aceptación:** `git status` limpio; tests del webhook (firma inválida → 403, monto menor → no confirma) en verde.

---

## FASE 4.6 — Correcciones de auditoría 🛠️

Detalle, evidencia y arreglo de cada hallazgo en [`AUDITORIA.md`](AUDITORIA.md) §7. Va **antes** de la Fase 5
porque 5B y 6A construyen sobre `pedidos/services.py` (R-3) y los pagos seguros (H-18…H-21).

---

## FASE 5 — Bidones y promociones prepago 📦 (RF-08, RF-09, RF-10)

### Punto de partida real
- `Cliente.bidones_prestados` es un `PositiveIntegerField` editable a mano (`clientes/models.py:76`).
- `registrar_entrega()` (`logistica/services.py:355`) ya recibe `envases_retirados` / `envases_vendidos`
  y ajusta el **stock del envase**, pero **no** toca el saldo de bidones del cliente.
- `Producto` ya distingue `es_retornable`, `es_envase` y la FK `envase` (migración `productos/0004`).
- `bidones_de_pedido(pedido)` ya calcula los retornables de un pedido.

### 5A — Historial de envases (RF-08) · ~4 h
| # | Tarea | Detalle |
|:--:|---|---|
| 5A.1 | Modelo `MovimientoBidon` en `apps/clientes` | `cliente` FK, `tipo ∈ {Prestamo, Devolucion, Venta, Ajuste}`, `cantidad` (+), `fecha`, `pedido` FK null, `parada` FK null (`logistica.DetalleHojaRuta`), `registrado_por` FK `Usuario` null, `nota` |
| 5A.2 | Migración de datos | Por cada cliente con `bidones_prestados > 0` crear un `Ajuste` inicial con ese saldo (no se pierde el dato actual) |
| 5A.3 | `bidones_prestados` → derivado | Opción recomendada (**F-D2**): conservar el campo como **caché** actualizado sólo por el servicio, y sacarlo de `ClienteForm` y del admin editable. Evita romper `list_display`, filtros y templates |
| 5A.4 | Servicio `registrar_movimiento_bidon()` | En `clientes/services.py` (nuevo), `@transaction.atomic`, `select_for_update` sobre el cliente, no permite saldo negativo |
| 5A.5 | Integrar con el reparto | En `registrar_entrega()`: al `Entregado` → `Prestamo` por `bidones_de_pedido()`; `envases_retirados` → `Devolucion`; `envases_vendidos` → `Venta` (resta del saldo porque se cobra) |
| 5A.6 | UI | Pestaña "Envases" en `ver_cliente.html` con historial y saldo; botón "Registrar devolución" para Vendedor |

### 5B — Promociones prepago (RF-09) · ~6 h
| # | Tarea | Detalle |
|:--:|---|---|
| 5B.1 | Nueva app `apps/promociones` | Registrar en `INSTALLED_APPS`; permisos del grupo Vendedor vía `apps/permisos/signals.py` |
| 5B.2 | `Promocion` | `nombre`, `producto` FK, `cant_paga` (3), `cant_lleva` (4), `precio` (derivado de `cant_paga × producto.precio` o fijo), `dias_validez` (default **30**), `activa` |
| 5B.3 | `CompraPromocion` (≈ `IncluyePromocion` del DER) | `cliente`, `promocion`, `pedido` FK (el que la pagó), `fecha_compra`, `fecha_caducidad` (= compra + `dias_validez`, zona AR), `unid_totales`, `unid_restantes`, `estado ∈ {Vigente, Agotada, Vencida}` |
| 5B.4 | `ConsumoPromocion` | `compra` FK, `pedido` FK, `cantidad`, `fecha` — trazabilidad de cada entrega parcial |
| 5B.5 | Venta de la promoción | Vendedor la registra desde el perfil del cliente: crea `Pedido` (origen `ADMIN`) por el precio prepago + `PagoPedido` o `Cargo` a cuenta (si `permite_fiado`) + `CompraPromocion` |
| 5B.6 | Consumo en pedidos | `promociones/services.py::consumir_saldo(cliente, producto, cantidad, pedido)` — FIFO por `fecha_caducidad`; las unidades cubiertas por saldo van con `precio_unitario = 0` en `DetallePedido` y se documenta en `notas` |
| 5B.7 | Integración | Checkout web y `construir_borrador()` muestran "Saldo prepago: N unidades (vence dd/mm)" y lo aplican al confirmar |

### 5C — Caducidad a 30 días corridos (RF-10) · ~2 h
| # | Tarea | Detalle |
|:--:|---|---|
| 5C.1 | Comando `vencer_promociones` | Marca `Vencida` y pone `unid_restantes=0` en toda compra con `fecha_caducidad < hoy` (AR). Idempotente. Documentar su ejecución diaria en Task Scheduler/cron junto a `generar_cargos_abonos` |
| 5C.2 | Defensa en profundidad | `consumir_saldo()` ignora compras vencidas aunque el comando no haya corrido |
| 5C.3 | Alerta | Panel en el dashboard: "Promociones que vencen en ≤ 5 días" |

### 5D — Tests · ~2 h
`apps/clientes/tests.py` (movimientos, saldo nunca negativo, integración con `registrar_entrega`) y
`apps/promociones/tests.py` (escenario de aceptación completo, FIFO, día 30 vs día 31, consumo de saldo vencido rechazado).

✅ **Aceptación (de `PROCEDURE.md`):** comprar "Paga 3 Lleva 4" crea un saldo con vencimiento a 30 días;
pedidos parciales lo consumen; al día 31 el comando lo expira. Además: entregar 2 bidones y retirar 1
deja `bidones_prestados` +1 con dos movimientos en el historial.

---

## FASE 6 — Pagos parciales, checkout y pedido automático 💳 (RF-04, RF-12, RF-13, RF-18)

### Punto de partida real
- `Pedido.esta_pagado()` devuelve `True` con **cualquier** pago aprobado → un pago parcial lo marca pagado. ⚠️ Bug.
- `registrar_cobro()` ya existe (`logistica/services.py:391`) pero sólo para cobro en calle.
- `confirmar_pedido` valida stock **sin** `select_for_update` y lo descuenta recién al cargar el camión.
- RF-18 está **parcialmente cubierto**: `Cliente.es_frecuente` + `cantidad_recurrente_default` ya
  sugieren al cliente en "Planificar reparto". Falta que sea **activable por el cliente** y **periódico**.

### 6A — Pagos parciales (RF-13) · ~4 h
| # | Tarea | Detalle |
|:--:|---|---|
| 6A.1 | Propiedades en `Pedido` | `total_pagado` (suma de pagos `Aprobado`), `saldo_pendiente`; `esta_pagado()` → `saldo_pendiente <= 0` |
| 6A.2 | Servicio `pedidos/services.py::registrar_pago_manual()` | Monto > 0 y ≤ saldo, método, `referencia_comprobante`; mover `registrar_cobro()` a este servicio y que logística lo llame |
| 6A.3 | Vista `registrar_pago` (FBV, `es_admin_o_vendedor`) | Formulario en `detalle_pedido.html` con barra de progreso pagado/total |
| 6A.4 | Pago a cuenta corriente | Opción "Cargar saldo a cuenta" → `cuentas.services.registrar_cargo()` (sólo `permite_fiado`) |
| 6A.5 | Panel de caja (T-6.4) | Dashboard: ingresos por método y por día (últimos 30 días) |

### 6B — Checkout seguro (RF-04, RF-12) · ~3 h
| # | Tarea | Detalle |
|:--:|---|---|
| 6B.1 | **RF-04:** bloquear checkout | Si `cliente.cantidad_telefonos() < 2` o `cantidad_direcciones() == 0` → redirigir a completar perfil (hoy sólo hay badge) |
| 6B.2 | **RF-12:** stock comprometido | `select_for_update` sobre los productos en `confirmar_pedido` y validar contra `stock − comprometido` (unidades en pedidos `Pendiente`/`Confirmado` aún no cargados). Recomendado sobre reservar en el carrito (**F-D3**): no deja stock bloqueado por carritos abandonados |
| 6B.3 | Carrito | `agregar_al_carrito` valida contra el mismo disponible |

### 6C — Pedido automático quincenal (RF-18) · ~4 h
| # | Tarea | Detalle |
|:--:|---|---|
| 6C.1 | Modelo `SuscripcionReposicion` en `pedidos` | `cliente`, `direccion`, `producto`, `cantidad`, `periodicidad_dias` (default 15), `proxima_fecha`, `activa`, `metodo_pago` |
| 6C.2 | Activación desde el perfil del cliente | Vista para el propio cliente (y para Vendedor): activar/pausar/cambiar cantidad |
| 6C.3 | Comando `generar_pedidos_automaticos` | Crea `Pedido` origen `AUTOMATICO` (nuevo valor en `ORIGENES_PEDIDO`) para las suscripciones con `proxima_fecha <= hoy`, aplica saldo de promoción (5B.6) y avanza `proxima_fecha`. Idempotente por (suscripción, fecha) |
| 6C.4 | Relación con `es_frecuente` | Decisión **F-D4**: recomendado que una suscripción activa marque `es_frecuente=True` y que `construir_borrador()` priorice el pedido real sobre la sugerencia (evita doble parada) |

### 6D — Tests · ~1 h
Escenario de aceptación (3 × $10.000 sobre $25.000 → no pagado hasta cubrir), checkout bloqueado por
RF-04, dos confirmaciones concurrentes del último stock, comando de suscripciones idempotente.

✅ **Aceptación:** la de `PROCEDURE.md` §Fase 6 + un cliente con suscripción quincenal recibe exactamente un pedido por período.

---

## FASE 7 — QA, producción y tesis 🎓

| # | Tarea | Detalle |
|:--:|---|---|
| 7.1 | Tests faltantes (H-10) | `carrito`, `buscador` (RF-07: tildes y fuzzy), `productos`, `autenticacion` (RF-01/RF-02), `pedidos` (checkout atómico, estados), `empleados` (no tiene `tests.py`) |
| 7.2 | Matriz RF ↔ test | Agregar columna "Test" a `PROCEDURE.md` §4; **cada RF con al menos un test** |
| 7.3 | Datos demo (H-13) | Extender `seed_logistica` (o comando `seed_demo`) con promociones, suscripciones, abonos y deudas en los 3 colores |
| 7.4 | README (H-14) | Instalación, `.env`, migraciones, seeds, comandos programados (`generar_cargos_abonos`, `vencer_promociones`, `generar_pedidos_automaticos`), roles y usuarios demo |
| 7.5 | Producción | `check --deploy` limpio; `LOGGING`; documentar el cron/Task Scheduler |
| 7.6 | Decisión C-9 / RF-20 | Declarar "gastos por proveedor" **fuera de alcance** en el informe (recomendado) o planificarlo |
| 7.7 | Tesis | Reescribir el informe con el cronograma de `PROCEDURE.md` §3 y las decisiones C-1…C-11; verificar el DER contra los modelos reales (incluye los nuevos de Fase 5/6) |
| 7.8 | Docs finales | `CONTEXT.md` v5.0, `PROCEDURE.md` con los 22 requisitos ✅, `graphify update .` |

✅ **Aceptación:** checklist §9 de `PROCEDURE.md` completo.

---

## 4. ❓ Decisiones a tomar antes de empezar

| # | Pregunta | Recomendación |
|:--:|---|---|
| F-D1 | ¿`db.sqlite3` sigue versionada? | **No**: sacarla del índice y depender de seeds reproducibles |
| F-D2 | ¿`bidones_prestados` se borra o queda como caché? | **Caché** actualizada sólo por el servicio (menor impacto en forms/admin/templates) |
| F-D3 | ¿RF-12 se resuelve reservando en el carrito o al confirmar? | **Al confirmar**, con stock comprometido + `select_for_update` |
| F-D4 | ¿RF-18 es un modelo nuevo o se extiende `es_frecuente`? | **Modelo nuevo** (`SuscripcionReposicion`) que alimenta a `es_frecuente`: el RF exige que lo active el cliente |
| F-D5 | ¿Una promoción vencida con unidades restantes se reintegra? | **No** (RF-10 dice caducidad estricta); dejarlo explícito en la tesis |
| F-D6 | ¿Las unidades de promoción se pueden usar con otro producto? | **No**: la promoción va atada a un `producto` |

---

## 5. 🔗 Dependencias y archivos compartidos

```
4.5 Consolidación
  └─► 5A Envases ──► 5B Promociones ──► 5C Caducidad
                          │
                          └──────────────► 6C Pedido automático (usa consumir_saldo)
  └─► 6A Pagos parciales   (independiente de 5)
  └─► 6B Checkout seguro   (toca pedidos/views.py: coordinar con 5B.7)
                                   └─► 7 QA + tesis
```

| Archivo | Lo tocan | Regla |
|---|---|---|
| `apps/logistica/services.py` | 5A.5, 5B.7, 6A.2 | Hacer 5 antes que 6A, o 6A sólo mueve `registrar_cobro` al final |
| `apps/pedidos/views.py` | 4.5.3, 5B.7, 6A.3, 6B | Secuencial |
| `apps/clientes/models.py` | 5A | — |
| `apps/permisos/signals.py` | 5B.1, 6C | Aditivo, sin conflicto |

---

## 6. Rutina por sub-fase

1. `graphify query` / `graphify explain "RF-xx"` antes de leer código.
2. Modelo + migración → servicio con `@transaction.atomic` → vista FBV con guard de `apps.permisos.roles` → template según `DESIGN.md` → tests.
3. Skill `verificar-cambios` (check, `makemigrations --check`, tests) y `graphify update .`.
4. Actualizar `PROCEDURE.md` (§4 matriz, §9 checklist) y `CONTEXT.md`.
5. Un commit por sub-fase (`feat(promociones): ... (5B)`).
