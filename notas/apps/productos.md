---
tipo: app
app: productos
ruta: apps/productos
modelos:
  - Categoria
  - Producto
depende_de: []
tags:
  - app
---
# productos

Catálogo: categorías y productos (con envase retornable).

- Código: `apps/productos/`
- Templates: `templates/productos/`
- Grafo de código: `graphify query "productos"`

## Relaciones
- Sin dependencias de modelos con otras apps.

## Notas
- Validaciones y correcciones: [[QA 2026-11-12]], [[Validaciones por campo]]
- 2026-11-14 ([[2026-11-14]]): interruptor único «Bidón retornable» (reparto + recarga, exige envase); sin tarjeta de consejos; inventario ordenable por columna.
- 2026-11-14 ([[2026-11-14]]): categorías con baja lógica («Categorías eliminadas» + Restaurar); catálogo con agotados al final.
- 2026-11-14 ([[2026-11-14]]): catálogo, ficha y buscador muestran el stock disponible (descuenta lo reservado); inventario con disponible, reservado y depósito; botón para cancelar la selección de cantidad.
- 2026-11-16 ([[2026-11-16]]): el inicio de la tienda muestra hasta 4 productos destacados con stock.
