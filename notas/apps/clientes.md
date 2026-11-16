---
tipo: app
app: clientes
ruta: apps/clientes
modelos:
  - Cliente
  - TelefonoContacto
  - DireccionEntrega
  - MovimientoBidon
depende_de:
  - "[[autenticacion]]"
  - "[[logistica]]"
  - "[[pedidos]]"
tags:
  - app
---
# clientes

Clientes, teléfonos, direcciones de entrega e historial de envases (RF-08).

- Código: `apps/clientes/`
- Templates: `templates/clientes/`
- Grafo de código: `graphify query "clientes"`

## Relaciones
- Usa modelos de [[autenticacion]]
- Usa modelos de [[logistica]]
- Usa modelos de [[pedidos]]

## Notas
- Validaciones y correcciones: [[QA 2026-11-12]], [[Validaciones por campo]]
- 2026-11-14 ([[2026-11-14]]): baja lógica con «Clientes eliminados» y Restaurar (bloquea la cuenta web y lo saca de los selectores); orden por columnas en el directorio; teléfonos dinámicos (uno obligatorio + los que haga falta, validados) en registro y alta; límites de largo con CHECK en la base.
- 2026-11-14 ([[2026-11-14]]): teléfonos y direcciones con baja lógica (lista plegable en la ficha + Restaurar); al eliminar el principal, pasa a otro.
- 2026-11-16 ([[2026-11-16]]): **Nro de cliente** (`Cliente.numero`): los importados conservan su número del sistema anterior; los nuevos arrancan en 0000001. Se muestra en el directorio y la ficha y se puede buscar. Importados los clientes de la hoja W3W de «Recorridos 12-11-25».
- 2026-11-16 ([[2026-11-16]]): botones **Editar** y **Eliminar** en cada fila del directorio (con la función `registrar_clientes`; después de eliminar vuelve a la misma página y búsqueda), como en [[productos]]; los eliminados siguen debajo en «Clientes eliminados».
- 2026-11-16 ([[2026-11-16]]): botón **Ver en Google Maps** en cada domicilio de la ficha (abre en otra pestaña). Usa las coordenadas si están cargadas; si no, busca por calle, altura y ciudad (`DireccionEntrega.url_google_maps()`).
- 2026-11-16 ([[2026-11-16]]): ficha más limpia: «Agregar domicilio» desplegable con un botón; el formulario de domicilio ya no pide coordenadas (el campo sigue en la base y el seed lo usa); sin la tarjeta amarilla de notas internas (se ven y editan en «Editar cliente»); el mínimo de teléfonos que se muestra es 1 (antes decía «Mín. 2 requerido»).
- 2026-11-16 ([[2026-11-16]]): en la ficha, Pedido automático, Envases prestados, Promociones prepagas e Historial son **desplegables** (empiezan plegados y recuerdan si quedaron abiertos; `static/js/secciones_desplegables.js`, se activa con `data-desplegable` en la tarjeta).
- 2026-11-16 ([[2026-11-16]]): botón **Promover a Premium** legible (antes amarillo sobre amarillo; clase `.btn-premium`) y sólo visible con la función `cambiar_tipo_cliente`; insignia «VIP Premium» con mejor contraste.
