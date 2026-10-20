# 🔎 Auditoría de coherencia — Distribuidora 3.0

> **Fecha:** 20/10/2026 · **Base:** `main` @ `50dc6b2` + cambios sin commitear de Fases 1–4
> **Alcance:** todo el código fuera de lo planificado en [`PLAN_CIERRE.md`](PLAN_CIERRE.md): errores,
> seguridad, redundancia e incoherencias entre módulos. Los IDs continúan la numeración de
> [`PROCEDURE.md`](PROCEDURE.md) §5 (H-1…H-17).
> **Método:** lectura de vistas, modelos, servicios y settings; script que resuelve todos los
> `{% url %}` / `redirect()` contra el URLconf real; `check` + 86 tests en verde.
>
> ⚠️ Los 86 tests **no cubren** el flujo de pagos de `pedidos` ni `clientes`, `productos` o `carrito`:
> por eso los hallazgos críticos de abajo pasan la suite.

---

## ▶️ Estado al 20/10/2026 (rama `cierre/fase-4.5-4.6`)

| Hallazgos | Estado | Commit |
|---|:--:|---|
| H-18, H-19, H-20, H-21, H-33, R-3 | ✅ | 4.6.1 — pagos seguros |
| H-23, H-24, H-25, H-26, H-36, R-2, R-5 | ✅ | 4.6.2 — roles unificados |
| H-22, H-27, H-28, H-29, R-1, H-37 (productos) | ✅ | 4.6.3 — errores 500 y datos |
| H-31, H-32, H-35, H-37, R-6, R-8 | ✅ | 4.6.4 — higiene |
| H-38 (nuevo) | ✅ | 4.6.5 — smoke de rutas |
| H-30 (`esta_pagado`) | ⏳ | Fase 6A |
| H-34 (buscador RF-07) | ⏳ | Fase 7 |
| H-39 (nuevo, una dirección por cliente) | ✅ | A-D4 aplicada: varias direcciones |
| R-4 (`celular1/2`, D-6), R-7 (skills en la raíz) | ⏳ | Fase 7 |

Decisiones aplicadas con la recomendación de este documento: **A-D1, A-D2, A-D3**.
Verificación: `check` 0 issues · sin migraciones pendientes · **128 tests OK** ·
`check --deploy` limpio · las 86 rutas GET responden sin 500 como administrador.

### Hallazgos nuevos

| ID | Severidad | Hallazgo | Estado |
|:--:|:--:|---|:--:|
| H-38 | 🟠 Alta | **Cinco errores 500 que el análisis estático no detectó** (sólo se ven con datos reales): `listar_roles` usaba `rol.id` (la PK es `id_rol`) y daba siempre 500; `listar_rutas`, `ver_ruta` e `imprimir_ruta` rompían con hojas sin chofer; `eliminar_zona` pasaba `url_cancelar` cuando el template espera `volver`, y una zona con rutas daba `ProtectedError`; `agregar_direccion` usaba `reverse()` sin importarlo. También `csrf_fallo.html` llenaba un bloque inexistente y se mostraba vacía. | ✅ |
| H-39 | 🟠 Media | **Incoherencia con RF-03 (multidirección):** `agregar_direccion` aplica la regla "cada cliente sólo puede tener 1 dirección" y redirige a editar la existente, pero la matriz marca RF-03 ✅ y el modelo admite varias (`es_principal`). | ❓ A-D4 |

| # | Pregunta | Recomendación |
|:--:|---|---|
| A-D4 ✅ varias | ¿El cliente puede tener varias direcciones de entrega (RF-03) o una sola? | **Varias**, como dice RF-03 y como ya soporta el modelo: quitar la restricción de la vista y elegir la dirección en el checkout (ya existe el selector) |

---

## 1. 🔴 Críticos — seguridad y dinero

| ID | Hallazgo | Evidencia | Arreglo |
|:--:|---|---|---|
| H-18 | **Cualquier usuario logueado puede aprobar cualquier pedido.** `pago_exitoso` confía en los parámetros GET (`external_reference`, `status`) sin consultar a MercadoPago ni verificar que el pedido sea del usuario: `/pedidos/pago/exitoso/?external_reference=15` marca el pago `Aprobado` y el pedido `Confirmado`. | `apps/pedidos/views.py:243` | Filtrar por `cliente__usuario=request.user` y **no cambiar estados** en el callback: sólo mostrar mensaje; el estado lo fija el webhook (o una consulta a `sdk.payment().get(payment_id)`) |
| H-19 | **El cliente se auto-aprueba el pago.** `confirmar_pago_qr` (GET, sin verificación) pone `estado_pago='Aprobado'` y `Confirmado` sobre su propio pedido. | `apps/pedidos/views.py:497`; enlace en `templates/pedidos/pago_qr.html:46` | Eliminar la vista o convertirla en "Ya pagué → queda **Pendiente de verificación**" para que el Vendedor apruebe |
| H-20 | **Pago con tarjeta simulado como real.** El método `TARJETA` aprueba el pago sin pasarela y recibe el **número completo** de la tarjeta por un formulario propio (riesgo PCI, aunque sólo guarde los últimos 4). | `apps/pedidos/views.py:147` | Decisión **A-D1**: quitar `TARJETA` del checkout web (cobro con tarjeta = MercadoPago o posnet en la entrega) o rotularlo explícitamente como *simulación académica* |
| H-21 | Webhook sin firma ni control de monto (ya en `PLAN_CIERRE` 4.5.3); además el `except Exception` devuelve 500 sin log | `apps/pedidos/views.py:307` | Ver 4.5.3 |

## 2. 🟠 Altos — errores funcionales

| ID | Hallazgo | Evidencia | Arreglo |
|:--:|---|---|---|
| H-22 | **El buscador de clientes rompe (500) si existe algún cliente sin cuenta web** (`c.usuario` es `None` en clientes pasajeros / sin cuenta). Además no busca por `Cliente.nombre/apellido`, sólo por los datos del usuario. Filtra en Python sobre **toda** la tabla. | `apps/clientes/views.py:48-55` | Filtrar en la BD con `Q(nombre__icontains)…| Q(usuario__username__icontains)…`; normalizar con la utilidad común (R-1) |
| H-23 | **Dashboard: "pedidos pendientes" siempre 0**: filtra `estado='PENDIENTE'` pero el valor es `'Pendiente'`. | `distribuidora/views.py:27` | Usar `'Pendiente'` |
| H-24 | **Tres sistemas de roles que no se hablan:** (1) grupos `Vendedor`/`Repartidor` (los usa `apps.permisos.roles`), (2) `RolEmpleado.nombre` (lo usa el **dashboard** con su propio `es_admin_o_vendedor`), (3) un grupo `Admin` que crea `seed_logistica` y nadie consulta. Un Vendedor por grupo sin ficha `Empleado` **no ve el dashboard**, pero el carrito lo redirige a `dashboard` → rebota a `/`. | `distribuidora/views.py:9`; `apps/logistica/management/commands/seed_logistica.py:24`; `apps/carrito/views.py:14` | Dashboard con `apps.permisos.roles.es_admin_o_vendedor`; borrar la copia local y el grupo `Admin` |
| H-25 | **Dar de alta un empleado no le da permisos.** `EmpleadoForm.save()` crea el `Usuario` pero **no lo agrega al grupo** de su `RolEmpleado`; cambiar el rol tampoco. Un "Repartidor" creado por la UI no puede ver su hoja de ruta hasta que alguien edite grupos en `/admin`. | `apps/empleados/forms.py:74-100` | Señal o servicio `sincronizar_grupo(empleado)`: rol → grupo (`Vendedor`, `Repartidor`) al crear/editar/desactivar |
| H-26 | **`redirect('home')` no existe** → `NoReverseMatch` (500) cuando un usuario sin permiso entra a Empleados. | `apps/empleados/views.py:23` | `redirect('inicio')` |
| H-27 | **Borrar un producto con pedidos da 500**: `DetallePedido.producto` es `PROTECT` y la vista no captura `ProtectedError`. | `apps/productos/views.py:120`; `apps/pedidos/models.py:124` | Capturar y ofrecer "Desactivar" (campo `activo`) en lugar de borrar |
| H-28 | **`registrar_entrega` no es idempotente:** volver a guardar una parada ya entregada suma otra vez los envases al stock, y con monto vuelve a crear un `PagoPedido`. | `apps/logistica/services.py:355-403`; `apps/logistica/views.py:274-286` | Aplicar sólo el **delta** contra lo ya registrado, o bloquear la edición de paradas en estado terminal |
| H-29 | **`cambiar_estado_pedido` permite cualquier transición** (p. ej. `Entregado` sin `fecha_entrega`, `Cancelado` en un pedido ya cargado al camión, volver de `Entregado` a `Pendiente`). Rompe la coherencia con logística. | `apps/pedidos/views.py:422` | Máquina de estados mínima en `Pedido` (`transiciones_validas`) usada por esta vista y por `registrar_entrega` |
| H-30 | `Pedido.esta_pagado()` = "existe algún pago aprobado" (ya en `PLAN_CIERRE` 6A.1) | `apps/pedidos/models.py:111` | Ver 6A |

## 3. 🟡 Medios

| ID | Hallazgo | Evidencia |
|:--:|---|---|
| H-31 | **Acciones que modifican datos por GET** (vulnerables a CSRF con un simple `<img src>`): agregar/quitar/vaciar carrito, `cerrar_sesion`, `confirmar_pago_qr` | `apps/carrito/views.py`, `apps/autenticacion/views.py:41` |
| H-32 | Redirecciones a `HTTP_REFERER` sin validar (open redirect leve) | `apps/carrito/views.py:50`, `apps/pedidos/views.py:436,464` |
| H-33 | Si falla la creación de la preferencia de MP (`except: pass`), el pedido queda creado, el carrito vaciado y el usuario es enviado a la **home de MercadoPago** | `apps/pedidos/views.py:217-238` |
| H-34 | **RF-07 débil:** en SQLite `icontains` distingue tildes, así que "bidon" no encuentra "Bidón" por la vía principal; cae al "fuzzy" que busca sólo las **2 primeras letras** ("bi") y devuelve ruido. No busca en descripción ni categoría | `apps/buscador/views.py:24-38` |
| H-35 | Sin plantillas `404.html` / `500.html`: en producción (`DEBUG=False`) se ve la página genérica en inglés | `templates/` |
| H-36 | La contraseña del alta de empleado **no pasa por `AUTH_PASSWORD_VALIDATORS`** (incoherente con RF-02) | `apps/empleados/forms.py:91` |
| H-37 | El login ignora `?next=` y siempre manda a inicio; `ver_producto` devuelve página vacía en vez de 404; las vistas de `productos` usan `user_passes_test` sin `login_required` (un cliente logueado es enviado al login) | `apps/autenticacion/views.py:34`, `apps/productos/views.py` |

## 4. ♻️ Redundancias

| ID | Redundancia | Dónde | Propuesta |
|:--:|---|---|---|
| R-1 | **3 implementaciones** de "quitar tildes y pasar a minúsculas" | `buscador/views.py:8`, `clientes/views.py:21`, `empleados/views.py:13` | `apps/permisos/` no es su lugar: crear `distribuidora/utils.py::normalizar_texto` |
| R-2 | Guards duplicados: `_sin_permiso` en `abonos` y `cuentas`; `es_admin_o_vendedor` redefinido en `distribuidora/views.py`; alias distintos (`es_staff_or_admin`, `es_vendedor_o_admin`) para la misma función | varios | Un decorador `@requiere_rol(es_admin_o_vendedor)` en `apps/permisos/decorators.py` |
| R-3 | Patrón "`pedido.pagos.last()` o crear uno" copiado **4 veces**, más `registrar_cobro` en logística | `pedidos/views.py:252,325,447,500`; `logistica/services.py:391` | `pedidos/services.py` (coincide con `PLAN_CIERRE` 6A.2) |
| R-4 | `Usuario.celular1/celular2` vs `TelefonoContacto` (decisión D-6 abierta) | `autenticacion/models.py:10`, `clientes/signals.py` | Cerrar D-6: deprecar los campos |
| R-5 | `has_group` (templatetag) vs `apps.permisos.roles` en templates | `base_dashboard.html`, `base_tienda.html`, `listar_rutas.html`, `ver_producto.html` | Context processor con `es_vendedor`/`es_repartidor` |
| R-6 | Código muerto: `templates/empleados/crear_empleado.html` y `editar_empleado.html` (se usa `form_empleado.html`); `fix_icons.py` (script de una sola vez con ruta absoluta de otra PC); `pedido_ref` (D6, conservado) | raíz, `templates/empleados/` | Borrar los templates y `fix_icons.py`; `seed_barrios.py` → comando `manage.py seed_barrios` |
| R-7 | Herramientas de IA en la raíz del repo (`skills-claude/`, `instalar-skills.ps1`) mezcladas con el código entregable de la tesis | raíz | Mover a `.claude/` o `tools/`, o excluir del entregable |
| R-8 | Ruido: docstring de plantilla de Django en `distribuidora/urls.py`; imports a mitad de `distribuidora/views.py`; comentarios tipo "MI DECORADOR SERIA ESTE" en `productos/views.py` | | Limpieza en el mismo commit que R-2 |

## 5. 📄 Incoherencias de documentación

- `PROCEDURE.md` tiene líneas de hallazgos duplicadas y desactualizadas (26–27) y la nota de Fase 3 truncada (241–244) — ya en `PLAN_CIERRE` 4.5.4.
- La matriz §4 marca **RF-07 ✅** y **RF-02 ✅**: con H-34 y H-36 deberían ser 🟡.
- `MERCADOPAGO_WEBHOOK_SECRET` existe sólo en `production.py`; en `base.py` falta con `default=''`, aunque la vista lo lee con `getattr`.
- 103 atributos `style="…"` inline en templates: revisar contra `DESIGN.md` en la Fase 7 (no se verificó uno por uno).

---

## 6. ✅ Lo que está bien (mantener)

- `apps/permisos/roles.py` como fuente única **en las apps nuevas** (cuentas, abonos, logística) y RNF-02 por asignación.
- Servicios con `@transaction.atomic` + `select_for_update` en logística y cuentas.
- Todas las demás rutas de templates y `redirect()` resuelven (sólo falla `'home'`).
- Gestión de roles de empleado restringida a superusuario; vistas de logística con guard + control por asignación.

---

## 7. 🗺️ Cómo entra en el plan

Se agrega una **Fase 4.6 — Correcciones de auditoría** entre 4.5 y 5 (ver [`PLAN_CIERRE.md`](PLAN_CIERRE.md)):

| Paso | Contenido | Esfuerzo |
|:--:|---|:--:|
| 4.6.1 | **Pagos seguros:** H-18, H-19, H-20 (+ H-21 de 4.5.3), H-33 y R-3 → `pedidos/services.py` | ~4 h |
| 4.6.2 | **Roles unificados:** H-24, H-25, H-36, R-2, R-5 → `apps/permisos` | ~3 h |
| 4.6.3 | **Errores 500 y datos:** H-22, H-23, H-26, H-27, H-28, H-29 | ~3 h |
| 4.6.4 | **Higiene:** H-31, H-32, H-35, H-37, R-1, R-6, R-7, R-8 | ~2 h |
| 4.6.5 | **Tests de regresión** para cada H-18…H-30 (`pedidos/tests.py`, `clientes/tests.py`, `empleados/tests.py`, `productos/tests.py`) | ~3 h |

H-34 (buscador) se resuelve en la Fase 7 con la suite de RF-07. Total de esta fase: **~15 h**.

### Decisiones nuevas
| # | Pregunta | Recomendación |
|:--:|---|---|
| A-D1 | ¿Qué hacer con el pago `TARJETA` simulado? | Quitarlo del checkout web; tarjeta = MercadoPago o cobro en la entrega |
| A-D2 | ¿`confirmar_pago_qr` se elimina o queda como "avisé que pagué"? | Dejarlo como aviso: el pago queda `Pendiente` hasta que lo apruebe el webhook o un Vendedor |
| A-D3 | ¿El rol del empleado manda sobre el grupo de Django? | **Sí**: `RolEmpleado` es la fuente para la UI, el grupo se sincroniza automáticamente |
