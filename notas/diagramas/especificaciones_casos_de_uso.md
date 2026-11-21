# Especificación de los casos de uso

Casos de uso del diagrama [`casos_de_uso.png`](casos_de_uso.png). En los flujos alternativos, «5a» es una variante del paso 5.

## CU-01 · Gestionar catálogo y categorías

- **Requerimiento:** RF-01
- **Actores:** Vendedor (principal). Administrador, por herencia.
- **Descripción:** Permite registrar, editar, categorizar y dar de baja los productos y accesorios que vende la distribuidora (bidones, dispensers, botellas, mates, etc.), con imagen y descripción.
- **Precondiciones:**
  - El actor inició sesión y tiene permiso para gestionar productos y categorías.
- **Flujo principal:**
  1. El actor ingresa a la sección Inventario.
  2. El sistema lista los productos (incluidos los inactivos) y las categorías.
  3. El actor elige «Nuevo producto» o edita uno existente.
  4. El sistema muestra el formulario: nombre, descripción, categoría, precio, stock e imagen.
  5. El actor completa los datos y confirma.
  6. El sistema valida los datos, guarda el producto y vuelve al listado con un mensaje de éxito.
- **Flujos alternativos:**
  - 5a. Hay datos inválidos (campos obligatorios vacíos, precio o stock negativos): el sistema marca los errores y no guarda.
  - 3a. El actor elige «Dar de baja»: el sistema pide confirmación y aplica una baja lógica; el producto deja de mostrarse en la tienda y puede restaurarse.
  - 3b. El actor gestiona categorías: crea, renombra o da de baja una categoría con el mismo esquema.
- **Postcondiciones:** El catálogo queda actualizado y los cambios se reflejan en la tienda web.
- **Relaciones:** —

## CU-02 · Gestionar envases retornables

- **Requerimiento:** RF-02
- **Actores:** Administrador.
- **Descripción:** Distingue el producto de consumo (el agua) de su envase físico retornable, marcando cada producto como envase, botellón o retornable y vinculando cada producto con el envase que usa, para seguir los bidones prestados y devueltos.
- **Precondiciones:**
  - El actor inició sesión como Administrador.
  - Existe en el catálogo el producto que representa al envase.
- **Flujo principal:**
  1. El actor abre la ficha de un producto.
  2. El actor marca si es envase, botellón o retornable y, si es un producto de consumo, elige su envase asociado.
  3. El sistema verifica que el envase elegido esté marcado como envase.
  4. El sistema guarda la relación producto–envase.
  5. A partir de ese momento, cada entrega y cada devolución actualizan el saldo de envases prestados del cliente.
- **Flujos alternativos:**
  - 3a. El envase elegido no es un envase: el sistema informa el error y no guarda.
- **Postcondiciones:** El producto queda vinculado a su envase; los envases no se muestran como productos destacados de la tienda.
- **Relaciones:** —

## CU-03 · Buscar productos

- **Requerimiento:** RF-03
- **Actores:** Cliente (también un visitante sin sesión).
- **Descripción:** Busca productos del catálogo tolerando mayúsculas, minúsculas, tildes y caracteres especiales.
- **Precondiciones:**
  - Ninguna: la búsqueda no requiere iniciar sesión.
- **Flujo principal:**
  1. El actor escribe un término en el buscador de la tienda.
  2. El sistema normaliza el término (minúsculas, sin tildes ni caracteres especiales).
  3. El sistema lo compara con los nombres normalizados de los productos activos.
  4. El sistema muestra los productos que coinciden, con precio e imagen.
- **Flujos alternativos:**
  - 4a. No hay coincidencias: el sistema muestra un mensaje y ofrece volver al catálogo completo.
- **Postcondiciones:** Ninguna (la búsqueda no modifica datos).
- **Relaciones:** —

## CU-04 · Gestionar carrito

- **Requerimiento:** RF-04
- **Actores:** Cliente.
- **Descripción:** Permite agregar productos al carrito, modificar cantidades y quitar ítems, calculando subtotales y total en el momento.
- **Precondiciones:**
  - El cliente inició sesión.
- **Flujo principal:**
  1. El cliente elige un producto del catálogo y la cantidad, y pulsa «Agregar al carrito».
  2. El sistema ejecuta CU-05 Validar stock disponible.
  3. El sistema agrega el ítem (o suma la cantidad si ya estaba) y recalcula subtotales y total.
  4. El cliente revisa el carrito y puede cambiar cantidades o quitar ítems; el sistema recalcula en cada cambio.
- **Flujos alternativos:**
  - 2a. No hay stock suficiente: el sistema no agrega el ítem e informa la cantidad disponible.
  - 4a. El cliente vacía el carrito: el sistema elimina todos los ítems.
- **Postcondiciones:** El carrito queda guardado con sus ítems y el total actualizado.
- **Relaciones:** «include» CU-05 Validar stock disponible.

## CU-05 · Validar stock disponible

- **Requerimiento:** RF-05
- **Actores:** Ninguno directo (lo incluyen CU-04 y CU-07).
- **Descripción:** Verifica que la cantidad pedida de cada producto no supere el stock disponible, evitando la sobreventa aun con pedidos simultáneos.
- **Precondiciones:**
  - Se recibe un producto y una cantidad a validar.
- **Flujo principal:**
  1. El sistema bloquea el registro del producto hasta terminar la operación.
  2. El sistema calcula el stock disponible: stock físico menos lo comprometido por pedidos aún no despachados.
  3. El sistema compara la cantidad pedida con el disponible.
  4. Si alcanza, el caso que lo incluyó continúa.
- **Flujos alternativos:**
  - 4a. La cantidad supera el disponible: el sistema rechaza la operación e informa cuánto hay disponible.
- **Postcondiciones:** Ninguna; el resultado lo usa el caso que lo incluyó.
- **Relaciones:** Incluido por CU-04 y CU-07.

## CU-06 · Descontar stock

- **Requerimiento:** RF-06
- **Actores:** Ninguno directo (lo incluyen CU-07 y CU-17).
- **Descripción:** Descuenta el inventario físico cuando la mercadería sale de la planta: al despachar el pedido (confirmar la hoja de ruta y cargar el camión) o al vender en la calle algo que no estaba cargado.
- **Precondiciones:**
  - El pedido está registrado y comprometido (CU-07), o hay una venta en calle (CU-17).
- **Flujo principal:**
  1. El sistema recibe los productos y cantidades despachados.
  2. Dentro de una transacción atómica, resta esas cantidades del stock físico.
  3. Al registrar el regreso del camión, lo que no se entregó vuelve al stock.
- **Flujos alternativos:**
  - 2a. Falla la operación: la transacción se revierte y el stock no cambia.
- **Postcondiciones:** El stock físico refleja la mercadería que salió.
- **Relaciones:** Incluido por CU-07 y CU-17.

## CU-07 · Registrar pedido

- **Requerimiento:** RF-07
- **Actores:** Cliente (pedido web) y Vendedor (pedido por mostrador). Secundarios: Reloj (vía CU-21) y Mercado Pago (vía CU-18).
- **Descripción:** Registra un pedido desde cualquiera de sus cuatro orígenes: WEB, ADMIN (mostrador), REPARTIDOR (venta en calle) y AUTOMATICO (reposición).
- **Precondiciones:**
  - El cliente tiene al menos una dirección de entrega.
  - En un pedido web, el carrito tiene al menos un producto.
- **Flujo principal:**
  1. El actor inicia el pedido: el cliente desde el checkout o el vendedor eligiendo al cliente.
  2. El sistema ejecuta CU-08 Validar teléfonos de contacto.
  3. El sistema muestra la dirección de entrega, la fecha estimada según el día de reparto de su zona y los métodos de pago.
  4. El actor elige dirección y método de pago, y confirma.
  5. El sistema ejecuta CU-05 Validar stock disponible para cada producto.
  6. El sistema crea el pedido en estado Pendiente con su origen, detalle y total, y aplica el saldo de packs prepagos si el cliente lo tiene (CU-14).
  7. Las unidades quedan comprometidas; el descuento físico se hace al despachar (CU-06).
  8. El sistema vacía el carrito y muestra el resumen del pedido.
- **Flujos alternativos:**
  - 2a. El cliente no tiene los teléfonos requeridos: el sistema no permite continuar (ver CU-08).
  - 4a. El cliente elige Mercado Pago: se ejecuta CU-18.
  - 5a. No hay stock suficiente de un producto: el sistema informa cuál y no crea el pedido.
- **Postcondiciones:** El pedido queda registrado en estado Pendiente y visible en «Mis pedidos» y en la gestión de pedidos.
- **Relaciones:** «include» CU-05, CU-06 y CU-08. Extendido por CU-18. Incluido por CU-21.

## CU-08 · Validar teléfonos de contacto

- **Requerimiento:** RF-08
- **Actores:** Ninguno directo (lo incluye CU-07).
- **Descripción:** Exige que el cliente tenga al menos dos teléfonos de contacto válidos, cada uno con su relación (por ejemplo, Titular y Esposa), antes de confirmar un pedido.
- **Precondiciones:**
  - Se inicia el registro de un pedido.
- **Flujo principal:**
  1. El sistema cuenta los teléfonos válidos del cliente.
  2. Si tiene dos o más con su relación, el pedido continúa.
- **Flujos alternativos:**
  - 2a. Tiene menos de dos: el sistema bloquea el checkout, explica el motivo y lleva al cliente a su perfil para cargarlos.
- **Postcondiciones:** Ninguna; habilita o bloquea el pedido.
- **Relaciones:** Incluido por CU-07.

## CU-09 · Cambiar estado del pedido

- **Requerimiento:** RF-09
- **Actores:** Vendedor y Repartidor.
- **Descripción:** Gestiona el ciclo de vida del pedido (Pendiente, Confirmado, En Camino, Entregado, Cancelado) y limita las transiciones según el rol y el flujo operativo.
- **Precondiciones:**
  - El pedido existe y no está Entregado ni Cancelado.
- **Flujo principal:**
  1. El vendedor abre el pedido.
  2. El sistema muestra el estado actual y solo las transiciones permitidas: de Pendiente a Confirmado o Cancelado; de Confirmado a Pendiente, Entregado o Cancelado.
  3. El vendedor elige el nuevo estado y confirma.
  4. El sistema registra el cambio.
- **Flujos alternativos:**
  - 1a. El pedido está en una hoja de ruta confirmada: el sistema lo pasa a En Camino automáticamente.
  - 1b. El repartidor confirma la entrega de la parada en su recorrido: el sistema pasa el pedido a Entregado y registra los vacíos retirados y el cobro.
  - 3a. El vendedor elige Cancelado: se ejecuta CU-10.
  - 3b. La transición no está permitida: el sistema la rechaza.
- **Postcondiciones:** El pedido queda en su nuevo estado.
- **Relaciones:** Extendido por CU-10.

## CU-10 · Cancelar pedido

- **Requerimiento:** RF-09 / RF-06
- **Actores:** Vendedor.
- **Descripción:** Anula un pedido de forma autorizada y devuelve lo que tenía reservado.
- **Precondiciones:**
  - El pedido está Pendiente o Confirmado.
  - El actor tiene permiso para gestionar pedidos.
- **Flujo principal:**
  1. El vendedor elige «Cancelar» en el pedido.
  2. El sistema pide confirmación.
  3. El vendedor confirma.
  4. El sistema pasa el pedido a Cancelado.
  5. El sistema ejecuta CU-19 Restituir stock.
  6. Si el pedido usó unidades de un pack que sigue vigente, el sistema las devuelve al saldo del cliente.
- **Flujos alternativos:**
  - 1a. El pedido está En Camino o Entregado: el sistema no ofrece la cancelación.
  - 6a. El pack ya venció: las unidades no se reintegran.
- **Postcondiciones:** El pedido queda Cancelado, con el stock y el saldo de packs restituidos.
- **Relaciones:** «extend» CU-09. «include» CU-19.

## CU-11 · Configurar packs promocionales

- **Requerimiento:** RF-11
- **Actores:** Vendedor (Administrador, por herencia).
- **Descripción:** Configura promociones por volumen del tipo «Paga X, lleva Y» con un precio global bonificado.
- **Precondiciones:**
  - El actor tiene permiso para gestionar promociones.
- **Flujo principal:**
  1. El actor ingresa a Promociones y elige «Nueva promoción».
  2. El sistema muestra el formulario: nombre, producto, unidades que se pagan (X), unidades que se llevan (Y) y precio del pack.
  3. El actor completa los datos y confirma.
  4. El sistema valida y guarda la promoción como activa.
- **Flujos alternativos:**
  - 4a. Datos inválidos (Y no mayor que X, precio no positivo): el sistema marca los errores.
  - 1a. El actor edita o desactiva una promoción existente; los packs ya vendidos no cambian.
- **Postcondiciones:** La promoción queda disponible para la venta.
- **Relaciones:** —

## CU-12 · Comprar pack promocional

- **Requerimiento:** RF-11
- **Actores:** Cliente (quien compra) y Vendedor (registra la venta).
- **Descripción:** Registra la compra de un pack prepago y deja sus unidades como saldo del cliente.
- **Precondiciones:**
  - Existe una promoción activa.
  - El cliente está registrado en el sistema.
- **Flujo principal:**
  1. El cliente solicita un pack y el vendedor lo busca desde la ficha del cliente.
  2. El sistema muestra las promociones activas con su precio y sus unidades.
  3. El vendedor elige la promoción y la forma de pago.
  4. El sistema registra la compra con Y unidades de saldo y vencimiento a 30 días corridos.
  5. El sistema registra el cobro del precio del pack.
- **Flujos alternativos:**
  - 3a. Se elige «a cuenta corriente»: solo se permite si el cliente tiene habilitado el fiado (Premium); el importe se carga a su cuenta.
- **Postcondiciones:** El cliente tiene saldo prepago vigente para retirar en entregas posteriores.
- **Relaciones:** —

## CU-13 · Retirar unidades del pack

- **Requerimiento:** RF-12
- **Actores:** Cliente.
- **Descripción:** Permite retirar las unidades del pack en varias entregas, descontándolas del saldo sin generar nuevos cobros.
- **Precondiciones:**
  - El cliente tiene saldo prepago vigente del producto.
- **Flujo principal:**
  1. El cliente pide una entrega del producto (pedido web, por mostrador o automático).
  2. El sistema consulta su saldo prepago vigente.
  3. El sistema ejecuta CU-14 Consumir saldo (FIFO).
  4. Las unidades cubiertas por el saldo se cargan en el pedido a precio cero.
  5. El saldo restante queda disponible para próximas entregas.
- **Flujos alternativos:**
  - 4a. Pide más unidades que su saldo: el excedente se cobra a precio normal.
- **Postcondiciones:** El saldo del cliente disminuye en las unidades entregadas.
- **Relaciones:** «include» CU-14.

## CU-14 · Consumir saldo (FIFO)

- **Requerimiento:** RF-13
- **Actores:** Ninguno directo (lo incluye CU-13).
- **Descripción:** Descuenta unidades del saldo prepago usando primero el pack que vence antes.
- **Precondiciones:**
  - El cliente tiene uno o más packs vigentes del producto.
- **Flujo principal:**
  1. El sistema ordena los packs vigentes por fecha de vencimiento, del más próximo al más lejano.
  2. Toma unidades del primero hasta cubrir lo pedido o agotarlo.
  3. Si quedan unidades por cubrir, sigue con el siguiente pack.
  4. Registra cada consumo asociado al pedido y marca como Agotado el pack que llega a cero.
- **Flujos alternativos:**
  - 2a. Falla la operación: la transacción se revierte y el saldo no cambia.
- **Postcondiciones:** El saldo queda actualizado y cada consumo vinculado a su pedido.
- **Relaciones:** Incluido por CU-13.

## CU-15 · Caducar saldo vencido (30 días)

- **Requerimiento:** RF-13
- **Actores:** Reloj (proceso programado diario).
- **Descripción:** Vence automáticamente los packs cuyo plazo de 30 días corridos ya pasó.
- **Precondiciones:**
  - El proceso programado está activo.
- **Flujo principal:**
  1. Una vez por día, el Reloj dispara el proceso de vencimiento.
  2. El sistema busca los packs vigentes cuya fecha de vencimiento es anterior a hoy.
  3. El sistema los pasa a estado Vencido con saldo cero.
- **Flujos alternativos:**
  - 2a. No hay packs vencidos: el proceso termina sin cambios.
- **Postcondiciones:** Las unidades vencidas dejan de estar disponibles y no se reintegran ni se reembolsan.
- **Relaciones:** —

## CU-16 · Suscribirse a reposición automática

- **Requerimiento:** RF-14
- **Actores:** Cliente.
- **Descripción:** Programa pedidos recurrentes de agua cada 7, 15 o 30 días.
- **Precondiciones:**
  - El cliente inició sesión y tiene al menos una dirección de entrega.
- **Flujo principal:**
  1. El cliente abre la opción «Pedido automático» de su cuenta.
  2. El sistema muestra el formulario: producto, cantidad, frecuencia (7, 15 o 30 días), dirección y método de pago.
  3. El cliente completa los datos y activa la suscripción.
  4. El sistema calcula la fecha del primer pedido y guarda la suscripción activa.
- **Flujos alternativos:**
  - 3a. El cliente modifica o pausa una suscripción existente: el sistema actualiza los datos o la desactiva.
- **Postcondiciones:** La suscripción queda activa con su próxima fecha de pedido.
- **Relaciones:** —

## CU-17 · Registrar venta en calle

- **Requerimiento:** RF-10
- **Actores:** Repartidor.
- **Descripción:** Permite al repartidor registrar durante el recorrido ventas directas fuera del circuito programado.
- **Precondiciones:**
  - El repartidor tiene una hoja de ruta en reparto (confirmada).
- **Flujo principal:**
  1. El repartidor elige «Venta en calle» en su recorrido.
  2. Elige un cliente existente o carga uno nuevo (nombre, calle, altura y barrio).
  3. Indica productos y cantidades, envases vacíos retirados y forma de cobro.
  4. El sistema ejecuta CU-20 Verificar capacidad del camión.
  5. El sistema crea el pedido con origen REPARTIDOR, ya Entregado, como parada extra de la hoja.
  6. El sistema ejecuta CU-06 Descontar stock para lo que no estaba cargado en el camión.
  7. El sistema registra los vacíos y el cobro (total, a cuenta corriente o sin cobro).
- **Flujos alternativos:**
  - 1a. La hoja no está en reparto: el sistema no permite registrar ventas.
  - 4a. La cantidad supera lo que queda en el camión: el sistema rechaza la venta e informa cuánto queda.
  - 2a. Faltan datos obligatorios del cliente nuevo: el sistema los pide.
- **Postcondiciones:** La venta queda registrada como pedido entregado y suma a la rendición del día.
- **Relaciones:** «include» CU-06 y CU-20.

## CU-18 · Pagar con Mercado Pago

- **Requerimiento:** — (objetivo: integración de pagos)
- **Actores:** Cliente (principal) y Mercado Pago (secundario, sistema externo).
- **Descripción:** Permite pagar el pedido en línea con Mercado Pago y conciliar el pago automáticamente.
- **Precondiciones:**
  - Se está registrando un pedido web (CU-07).
- **Flujo principal:**
  1. El cliente elige Mercado Pago como método de pago.
  2. El sistema crea la orden de pago en Mercado Pago y redirige al cliente.
  3. El cliente paga en Mercado Pago.
  4. Mercado Pago notifica el resultado al sistema (webhook).
  5. El sistema verifica la firma criptográfica de la notificación y consulta el estado real del pago.
  6. Si el pago está aprobado, el sistema registra el monto y marca el pago como Aprobado.
- **Flujos alternativos:**
  - 6a. El pago queda pendiente o es rechazado: el pedido conserva el pago Pendiente o Rechazado y el cliente puede pagar al recibir.
  - 5a. La firma no es válida: el sistema descarta la notificación.
- **Postcondiciones:** El pago del pedido queda conciliado con Mercado Pago.
- **Relaciones:** «extend» CU-07.

## CU-19 · Restituir stock

- **Requerimiento:** RF-06
- **Actores:** Ninguno directo (lo incluye CU-10).
- **Descripción:** Devuelve al inventario las unidades de un pedido cancelado.
- **Precondiciones:**
  - Se canceló un pedido (CU-10).
- **Flujo principal:**
  1. El sistema libera las unidades que el pedido tenía comprometidas.
  2. Si alguna ya se había descontado del stock físico, la reintegra.
  3. Todo se hace en una única transacción atómica.
- **Flujos alternativos:**
  - 3a. Falla la operación: la transacción se revierte y el pedido no queda cancelado.
- **Postcondiciones:** El stock disponible vuelve a incluir esas unidades.
- **Relaciones:** Incluido por CU-10.

## CU-20 · Verificar capacidad del camión

- **Requerimiento:** RF-10
- **Actores:** Ninguno directo (lo incluye CU-17).
- **Descripción:** Controla que una venta en calle no supere lo que queda en el camión (capacidad máxima de 42 botellones).
- **Precondiciones:**
  - Hay una venta en calle en curso.
- **Flujo principal:**
  1. El sistema calcula lo que queda en el camión: lo cargado menos lo entregado y lo ya vendido.
  2. Compara esa cantidad con la de la venta.
  3. Si alcanza, la venta continúa.
- **Flujos alternativos:**
  - 3a. No alcanza: el sistema rechaza la venta e informa cuántas unidades quedan.
- **Postcondiciones:** Ninguna; habilita o bloquea la venta.
- **Relaciones:** Incluido por CU-17.

## CU-21 · Generar pedido automático

- **Requerimiento:** RF-14
- **Actores:** Reloj (proceso programado diario).
- **Descripción:** Crea los pedidos de las suscripciones de reposición cuya fecha llegó y adelanta la próxima fecha.
- **Precondiciones:**
  - Hay suscripciones activas (CU-16).
- **Flujo principal:**
  1. Una vez por día, el Reloj dispara la generación de pedidos automáticos.
  2. El sistema busca las suscripciones activas cuya próxima fecha es hoy o anterior.
  3. Por cada una, ejecuta CU-07 Registrar pedido con origen AUTOMATICO, la dirección y el método de pago de la suscripción.
  4. Si el cliente tiene saldo prepago, lo aplica al pedido.
  5. El sistema adelanta la próxima fecha en 7, 15 o 30 días según la frecuencia.
- **Flujos alternativos:**
  - 3a. La suscripción no tiene dirección o el producto está inactivo: el sistema la saltea.
  - 1a. El proceso se ejecuta dos veces el mismo día: no duplica pedidos porque la fecha ya se adelantó.
- **Postcondiciones:** Cada suscripción vencida tiene su pedido generado y su próxima fecha actualizada.
- **Relaciones:** «include» CU-07.
