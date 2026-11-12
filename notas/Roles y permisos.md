---
tipo: referencia
fecha: 2026-11-12
apps:
  - "[[permisos]]"
  - "[[empleados]]"
tags:
  - permisos
  - roles
---
# Roles y permisos

Cada pantalla del sistema exige una **función**. Las funciones se marcan por rol con checkboxes en
**Empleados y roles › Roles › (rol) › Permisos**. Los cambios valen al instante para todos los
empleados con ese rol. Sólo el superusuario o quien tenga *Gestionar empleados, roles y permisos*
entra a esa pantalla, y nadie puede quitarse esa función a sí mismo.

> [!tip] Ejemplo
> Para que un repartidor pueda registrar clientes: Roles › Repartidor › marcar
> «Registrar y editar clientes» (y «Ver la lista y la ficha de los clientes» para llegar a la lista).

## Funciones y roles por defecto
| Área | Función | Código | Administrador | Vendedor | Repartidor |
|---|---|---|:-:|:-:|:-:|
| Panel | Entrar al panel y ver el resumen general | `ver_panel` | ✅ | ✅ | — |
| Productos | Ver el inventario (incluye productos inactivos) | `ver_inventario` | ✅ | ✅ | — |
| Productos | Crear, editar y eliminar productos | `gestionar_productos` | ✅ | ✅ | — |
| Productos | Crear, editar y eliminar categorías | `gestionar_categorias` | ✅ | ✅ | — |
| Clientes | Ver la lista y la ficha de los clientes | `ver_clientes` | ✅ | ✅ | — |
| Clientes | Registrar y editar clientes (datos, teléfonos y direcciones) | `registrar_clientes` | ✅ | ✅ | — |
| Clientes | Pasar clientes a VIP / Normal (habilita el fiado) | `cambiar_tipo_cliente` | ✅ | ✅ | — |
| Clientes | Registrar movimientos de envases | `registrar_envases` | ✅ | ✅ | — |
| Clientes | Ver las notas de seguridad de todos los domicilios | `ver_notas_seguridad` | ✅ | ✅ | — |
| Pedidos | Ver los pedidos de todos los clientes | `ver_pedidos` | ✅ | ✅ | — |
| Pedidos | Cambiar el estado de los pedidos y el pedido automático | `gestionar_pedidos` | ✅ | ✅ | — |
| Pedidos | Registrar cobros y validar pagos | `cobrar_pedidos` | ✅ | ✅ | — |
| Cuentas corrientes | Ver cuentas corrientes y morosidad | `ver_cuentas` | ✅ | ✅ | — |
| Cuentas corrientes | Registrar cargos y pagos en las cuentas | `registrar_movimientos_cuenta` | ✅ | ✅ | — |
| Abonos | Ver y gestionar abonos de dispensers (y generar los cargos) | `gestionar_abonos` | ✅ | ✅ | — |
| Promociones | Crear y editar promociones | `gestionar_promociones` | ✅ | ✅ | — |
| Promociones | Vender packs de promoción a clientes | `vender_promociones` | ✅ | ✅ | — |
| Logística | Planificar repartos y armar o editar hojas de ruta | `planificar_repartos` | ✅ | ✅ | — |
| Logística | Ver todas las hojas de ruta (no sólo las propias) | `ver_todas_las_rutas` | ✅ | ✅ | — |
| Logística | Hacer el recorrido: entregar, cobrar y vender en la calle | `realizar_entregas` | ✅ | — | ✅ |
| Logística | Gestionar zonas, barrios y camiones | `gestionar_zonas_camiones` | ✅ | ✅ | — |
| Empleados | Gestionar empleados, roles y permisos | `gestionar_empleados` | ✅ | — | — |

## Reglas que no dependen de las casillas
- **Repartidor:** con *Hacer el recorrido* ve y opera **sólo sus** hojas de ruta; para ver todas necesita *Ver todas las hojas de ruta*.
- **Notas de seguridad (RNF-02):** con *Ver las notas de seguridad* las ve todas; un repartidor ve sólo las de los domicilios de sus hojas.
- **Superusuario:** tiene todas las funciones siempre.
- **Empleado inactivo:** no puede nada, aunque su rol tenga funciones.

## Dónde está en el código
- Catálogo: `apps/permisos/funciones.py` · helpers: `apps/permisos/roles.py` (`puede`, `@requiere`)
- Backend: `apps/permisos/backends.py` · migración de roles por defecto: `empleados/0007_funciones_por_defecto`
- Menú: `templates/includes/menu_panel.html` · pantalla: `templates/empleados/roles/form_rol.html`

Relacionado: [[QA 2026-11-12]]
