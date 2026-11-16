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
- 2026-11-16 ([[2026-11-16]]): botones **Editar** y **Eliminar** en cada fila del directorio (con la función `registrar_clientes`), como en [[productos]]; los eliminados siguen debajo en «Clientes eliminados».
- 2026-11-16 ([[2026-11-16]]): botón **Ver en Google Maps** en cada domicilio de la ficha (abre en otra pestaña). Usa las coordenadas si están cargadas; si no, busca por calle, altura y ciudad (`DireccionEntrega.url_google_maps()`).
