---
tipo: referencia
tags:
  - qa
  - validaciones
---
# Validaciones por campo

Las reglas viven en `distribuidora/validadores.py` (servidor) y se reflejan en el HTML
(`inputmode`, `pattern`, `maxlength`, `min`/`max`) para que el campo no deje escribir otra cosa.
Los errores se muestran en un popup con el nombre del campo. Relacionado: [[QA 2026-11-12]].

| Dato | Dónde | Regla | Mensaje |
|---|---|---|---|
| DNI | Clientes, alta con cuenta, Empleados | Sólo números, **7 u 8 dígitos** (se aceptan puntos al pegar y se quitan). Único. | «El DNI debe tener 7 u 8 dígitos.» / «Ya hay un cliente registrado con ese DNI.» |
| Teléfono / celular | Registro, Teléfonos, Mi perfil, Empleados | Números, espacios, `-`, `()` o `+`; **mínimo 8 dígitos**; no repetido en el mismo cliente | «Ingresá un número válido (al menos 8 dígitos).» |
| Email | Registro, Empleados, Clientes | Formato válido; único sin distinguir mayúsculas | «Ya existe una cuenta con ese email.» |
| Usuario | Registro, Empleados | Único sin distinguir mayúsculas | «Ese nombre de usuario ya está en uso.» |
| Nombre / apellido de empleado | Empleados | Letras (con tildes), espacios, `'` y `-` | «El nombre sólo puede tener letras…» |
| Fecha de nacimiento | Clientes | No futura | «La fecha de nacimiento no puede ser futura.» |
| Altura | Direcciones, parada nueva | Número (con letra opcional) o `S/N` | «Ingresá el número de la calle (ej: 450) o "S/N".» |
| Coordenadas | Direcciones | `lat,lng` dentro de rango | «Usá el formato "latitud,longitud"…» |
| Patente | Camiones | `AB123CD` o `ABC123`, se guarda en mayúsculas; no editable | «Patente inválida…» |
| Capacidad del camión | Camiones | ≥ 1 | «La capacidad debe ser de al menos 1 botellón.» |
| Precio | Productos, Promociones | > 0 | «El precio debe ser mayor a cero.» |
| Stock | Productos | ≥ 0 | «El stock no puede ser negativo.» |
| Categoría (nombre) | Categorías | Única sin distinguir mayúsculas | «Ya existe una categoría con ese nombre.» |
| Montos | Cargos, pagos, cobros | > 0 | (validación del formulario) |
| Vencimiento de cargo | Cuentas | No anterior a hoy | «El vencimiento no puede ser anterior a hoy.» |
| Primer pedido automático | Pedido automático | No anterior a hoy | «La fecha no puede ser anterior a hoy.» |
| Unidades que paga / días de validez | Promociones | ≥ 1 | «Debe ser al menos 1.» |
| Cantidad de envases | Ficha del cliente | > 0 (en *Ajuste* ≠ 0); máximo 500 | «La cantidad debe ser mayor a cero…» |
| Cantidad al carrito | Tienda | > 0 | «La cantidad debe ser un número mayor a cero.» |
| Día de facturación | Abonos | 1 a 28 | (ya existía) |
