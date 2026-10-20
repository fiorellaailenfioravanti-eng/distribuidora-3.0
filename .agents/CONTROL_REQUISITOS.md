# ✅ Control de cumplimiento de requisitos — 20/10/2026

> **Base:** rama `cierre/fase-4.5-4.6` @ `215dc45` (128 tests OK).
> **Método:** para cada requisito se revisó el código y se **ejecutó** el comportamiento en una base
> de prueba descartable (script fuera del repo, no toca `db.sqlite3`), como lo haría un usuario:
> registrarse, comprar, buscar, cobrar, repartir. Las definiciones salen de la matriz de
> [`PROCEDURE.md`](PROCEDURE.md) §4; el informe de tesis no está en el repositorio.

## Resumen

| Resultado | Cant. | Requisitos |
|---|:--:|---|
| ✅ Cumple | **10** | RF-02, RF-06, RF-11, RF-14, RF-15, RF-16, RF-19, RNF-01, RNF-02, RNF-03 |
| 🟡 Parcial | **6** | RF-03, RF-04, RF-07, RF-12, RF-13, RF-17 |
| ⚠️ Marcado ✅ pero **falla** | **2** | RF-01, RF-05 |
| 🔴 No implementado | **4** | RF-08, RF-09, RF-10, RF-18 |

La matriz anterior daba 13 ✅. La diferencia: **RF-01 y RF-05 figuraban completos y fallan** al
ejecutarlos, y **RF-17** no tiene la generación quincenal que pide su enunciado.

## Detalle

| ID | Requisito | Resultado | Evidencia (ejecutada) | Qué falta | Fase |
|:--:|---|:--:|---|---|:--:|
| RF-01 | Registro con ≥2 celulares y relación | ⚠️ | Un registro **sin ningún celular se acepta** (0 teléfonos). `celular1/2` son opcionales en `Usuario` y la relación no se pide: la señal pone "Titular"/"Alternativo" | Exigir 2 teléfonos + relación en `RegistroUsuarioForm` (o pasar a `TelefonoContacto` directo, D-6) — **H-40** | 6 |
| RF-02 | Validación de contraseñas | ✅ | "1234" rechazada en el registro y en el alta de empleado | — | — |
| RF-03 | Multidirección | 🟡 | El modelo tiene calle, altura, zona, nota de seguridad y coordenadas, pero la vista **redirige a editar** si ya hay una dirección | Decisión **A-D4** (H-39) | 6 |
| RF-04 | ≥2 teléfonos para operar | 🟡 | Cliente con **0 teléfonos compra** igual; sólo hay un badge | Bloquear checkout (T-6.1 / 6B.1) | 6 |
| RF-05 | Normal/Premium; fiado sólo Premium | ⚠️ | Normal → fiado rechazado ✔. Pero un **Premium bajado a Normal conserva `permite_fiado=True` y puede fiar**; el admin también permite activarlo a un Normal | `Cliente.save()`: `permite_fiado = es_premium()`; quitar el campo editable — **H-41** | 6 |
| RF-06 | Catálogo por categorías | ✅ | Filtro "Dispensers" devuelve sólo el dispenser | — | — |
| RF-07 | Buscador tolerante | 🟡 | Tildes/mayúsculas/errores ✔ ("bidn" → Bidón). Pero el respaldo por 2 letras trae **ruido** ("bidon" → también *Combo bienvenida*; "agua de mesa" → *Bebedero para mascotas*) y **no busca en la descripción** | Normalizar en Python sobre nombre+descripción+categoría con ranking (H-34) | 7 |
| RF-11 | Pedido completo | ✅ | Fecha, total, estado, dirección y detalle presentes | — | — |
| RF-12 | Carrito ≤ stock | 🟡 | Pedir 5 con stock 3 → rechazado ✔. Dos carritos suman 6 con stock 3: se valida recién al confirmar, sin bloqueo de fila | `select_for_update` + stock comprometido (6B.2) | 6 |
| RF-13 | Pagos parciales, varios métodos | 🟡 | 5 métodos activos ✔. **$10.000 de $25.000 → `esta_pagado()=True`** (H-30); no hay vista de cobro manual | 6A completo | 6 |
| RF-14 | Semaforización de deuda | ✅ | 1 día → amarillo · 11 → naranja · 16 → rojo | — | — |
| RF-15 | Alquiler de dispensers | ✅ | Premium paga 900 de 1000; la facturación mensual no duplica en la 2ª corrida | — | — |
| RF-16 | Hoja de ruta diaria | ✅ | Fecha, zona, camión y chofer | — | — |
| RF-17 | Agrupación automática + **generación quincenal** | 🟡 | El pedido confirmado de la zona aparece en el borrador ✔. **No existe generación periódica**: por la decisión D2 la planificación es asistida y manual | Decisión **A-D5** | 6/7 |
| RF-18 | Pedido automático quincenal | 🔴 | Sin modelo ni comando | 6C | 6 |
| RF-19 | Confirmación de entrega en campo | ✅ | Parada → `Entregado` pasa el pedido a `Entregado` con fecha | — | — |
| RF-08 | Control de envases (historial) | 🔴 | Sólo el entero `bidones_prestados` | 5A | 5 |
| RF-09 | Promociones prepago | 🔴 | Sin modelos | 5B | 5 |
| RF-10 | Caducidad 30 días | 🔴 | Sin comando | 5C | 5 |
| RNF-01 | Multi camión/zona/chofer | ✅ | Dos hojas el mismo día con distinta zona, camión y chofer | — | — |
| RNF-02 | Ocultar info sensible | ✅ | Vendedor la ve, el propio cliente no; repartidor asignado/no asignado en `apps/permisos/tests.py` | — | — |
| RNF-03 | Dark mode sin login | ✅ | Botón de tema para anónimos; preferencia en `localStorage` | — | — |

## Cobertura de tests por requisito (checklist §9 de PROCEDURE)

Con test automático que lo ejercita: RF-02, RF-05 (parcial), RF-12, RF-14, RF-15, RF-16, RF-17,
RF-19, RNF-02. **Sin test:** RF-01, RF-03, RF-04, RF-06, RF-07, RF-11, RF-13, RNF-01, RNF-03.

## Hallazgos y decisiones nuevas

| ID | Hallazgo |
|:--:|---|
| H-40 | RF-01: el registro web acepta usuarios sin teléfonos y no pide la relación de cada uno |
| H-41 | RF-05: bajar un cliente de Premium a Normal no le quita el fiado; el admin permite fiado a un Normal |

| # | Pregunta | Recomendación |
|:--:|---|---|
| A-D5 | RF-17 pide **generación quincenal**; la Fase 3 la reemplazó por planificación asistida (D2). ¿Se implementa o se justifica? | Agregar un comando `generar_borradores_reparto` que cree los **borradores** de los próximos 15 días por zona (sin confirmarlos, respetando D2). Es poco trabajo y cumple el enunciado |

## Cómo se reparte en el plan

- **Fase 6** absorbe RF-01 (H-40), RF-04, RF-05 (H-41), RF-12, RF-13, RF-18 y, según A-D4/A-D5, RF-03 y RF-17.
- **Fase 5**: RF-08, RF-09, RF-10.
- **Fase 7**: RF-07 y los tests faltantes de la lista de arriba.
