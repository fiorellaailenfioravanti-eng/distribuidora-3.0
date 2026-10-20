# 🌊 Aquadelluvia — Contexto Maestro del Proyecto
> **Distribuidora 3.0** · Sistema de Gestión Operativa, Logística y E-Commerce
>
> **⚠️ LEER PRIMERO:** Este archivo provee todo el contexto necesario para trabajar en este proyecto.
> Última actualización: 20/10/2026 — Versión 4.2 (Fases 4.5 y 4.6: consolidación y auditoría).

---

## 1. 📋 Información General

| Campo | Detalle |
|---|---|
| **Proyecto** | Sistema de Gestión Integral y Plataforma E-commerce |
| **Empresa cliente** | Distribuidora "Aquadelluvia" (Presidencia Roque Sáenz Peña, Chaco, Argentina) |
| **Institución** | Universidad Nacional del Chaco Austral (UNCAUS) – Ingeniería en Sistemas de Información |
| **Contexto** | Trabajo Final de Grado / Tesis (Cátedra de Gestión de Datos) |
| **Framework** | Django 5.0 (Python) |
| **Base de datos** | SQLite3 (desarrollo y despliegue académico) |

### 👥 Equipo de Desarrollo

| Integrante | L.U. | Módulo asignado |
|---|---|---|
| **Fiorella Ailén Fioravanti** | 15427 | Portal web e-commerce: autenticación, catálogo, carrito, seguridad, clientes |
| **Lucas Masson** | 37492 | Módulo logístico: hojas de ruta, agrupación geográfica, app para repartidores |

### 🏪 Negocio del cliente
Aquadelluvia comercializa y distribuye **domiciliariamente**:
- Agua mineral enriquecida (agua de mar con minerales insertados)
- Alquiler de dispensers frío/calor
- Accesorios y merchandising (mates, termos, bombillas, soportes)

Prioridades: atención personalizada, enfoque naturalista, creación de comunidad y escalamiento hacia múltiples camiones y zonas de reparto simultáneas.

---

## 2. 🩺 Problemática y Diagnóstico Operativo

La empresa coordinaba su operativa con herramientas totalmente informales:

| Proceso | Herramienta anterior | Problema |
|---|---|---|
| Toma de pedidos | WhatsApp | Sin trazabilidad ni historial estructurado |
| Registro de clientes | Google Sheets / Docs | Propenso a errores, sin validaciones |
| Logística y reparto | Fichas de papel físicas | Sin actualización en tiempo real |
| Cuentas corrientes / fiados | "De palabra" | Falta de alertas de morosidad y pérdida de cobros |
| Promociones prepago | Manual | Imposible controlar bidones pendientes y vencimientos |

> Anteriormente usaron el software *Henzai*, dado de baja por fallas en actualizaciones.

---

## 3. ⚙️ Arquitectura y Stack Tecnológico

### Patrón: Django MVT (Function-Based Views)

| Capa | Tecnología | Detalle |
|---|---|---|
| **Model** | Django ORM + SQLite 3 | Mapeo ORM, transacciones ACID, serverless, `db.sqlite3` local |
| **View** | Function-Based Views (FBV) | Lógica de negocio con decoradores `@login_required`. **No se usan CBV.** |
| **Template** | Django Template Language (DTL) | HTML5 + Bootstrap 5.3 (dark mode) |
| **Auth** | Django Auth (modelo custom) | `AbstractUser` extendido (`autenticacion.Usuario`) |
| **Media** | Pillow | Manejo de `ImageField` para productos y perfiles |
| **Búsqueda** | `unicodedata` (stdlib Python) | Normalización de tildes y búsqueda fuzzy |
| **Config** | `python-decouple` | `SECRET_KEY` y credenciales de MercadoPago fuera del repositorio |
| **Idioma/Zona** | `es-AR` / `America/Argentina/Buenos_Aires` | — |

### Estructura de Directorios

```
DISTRIBUIDORA-3.0/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .env.example                     # Plantilla de variables (SECRET_KEY, ALLOWED_HOSTS, MP)
├── distribuidora/
│   ├── urls.py                      # Router raíz
│   ├── views.py                     # Vista de inicio
│   └── settings/
│       ├── base.py                  # Config compartida (decouple, apps, i18n)
│       ├── local.py                 # Dev: DEBUG=True, SQLite, hosts abiertos
│       └── production.py            # ✅ Despliegue: DEBUG=False, HTTPS, hosts y credenciales
├── apps/
│   ├── autenticacion/               # ✅ Usuarios, login (respeta ?next=), perfil
│   ├── buscador/                    # ✅ Búsqueda tolerante a tildes
│   ├── carrito/                     # ✅ Carrito transaccional + validación stock
│   ├── productos/                   # ✅ CRUD catálogo y categorías
│   ├── clientes/                    # ✅ Gestión de clientes, teléfonos y direcciones
│   ├── pedidos/                     # ✅ Checkout, Pedido, Pagos, MercadoPago, webhook
│   ├── logistica/                   # ✅ Zonas, barrios, camiones, rutas y hojas de ruta
│   ├── empleados/                   # ✅ Empleados y roles (FUENTE ÚNICA del personal)
│   ├── cuentas/                     # ✅ Cuentas corrientes, fiado y semaforización (RF-14)
│   ├── abonos/                      # ✅ Alquiler de dispensers y facturación (RF-15)
│   ├── promociones/                 # ✅ Packs prepagos y caducidad a 30 días (RF-09, RF-10)
│   └── permisos/                    # ✅ Roles, sincronización rol→grupo, context processor
├── templates/
├── static/
└── media/
```

### Configuración clave (`base.py`)

```python
BASE_DIR            = Path(__file__).resolve().parent.parent.parent   # raíz del repo
AUTH_USER_MODEL     = 'autenticacion.Usuario'
LOGIN_URL           = '/auth/ingresar/'
LOGIN_REDIRECT_URL  = '/'
LOGOUT_REDIRECT_URL = '/auth/ingresar/'
LANGUAGE_CODE       = 'es-AR'
TIME_ZONE           = 'America/Argentina/Buenos_Aires'
SECRET_KEY          = config('SECRET_KEY', default=SECRET_KEY_FALLBACK)  # fallback solo dev
MERCADOPAGO_ACCESS_TOKEN   = config('MERCADOPAGO_ACCESS_TOKEN', default='')
MERCADOPAGO_WEBHOOK_SECRET = config('MERCADOPAGO_WEBHOOK_SECRET', default='')  # sin él no se valida la firma
```

Utilidades compartidas en `distribuidora/utils.py`: `normalizar_texto()` (búsquedas
tolerantes a tildes) y `redirigir_a_origen()` (vuelve a la página previa sólo si es del sitio).

> `production.py` **no** admite defaults: si falta `SECRET_KEY`, `ALLOWED_HOSTS`,
> `MERCADOPAGO_ACCESS_TOKEN` o `MERCADOPAGO_WEBHOOK_SECRET`, el arranque falla.

### Context Processors habilitados

```python
'apps.carrito.context_processors.carrito_total'    # Inyecta carrito_total_items globalmente
'apps.permisos.context_processors.roles_usuario'  # es_vendedor, es_repartidor, es_personal_interno
```

### Cómo correr el proyecto

```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env          # completar SECRET_KEY, ALLOWED_HOSTS y credenciales MP
python manage.py migrate --settings=distribuidora.settings.local
python manage.py createsuperuser --settings=distribuidora.settings.local
python manage.py seed_barrios --settings=distribuidora.settings.local     # barrios de Resistencia
python manage.py seed_demo --settings=distribuidora.settings.local       # datos de demo completos (usuarios en el docstring)
python manage.py runserver --settings=distribuidora.settings.local
# → http://127.0.0.1:8000/
```

---

## 4. ✅ LO QUE ESTÁ REALIZADO

### Módulo `apps.autenticacion` ✅

**Modelo `Usuario`** (extiende `AbstractUser`):
```python
class Usuario(AbstractUser):
    imagen_perfil = ImageField(upload_to='perfiles/', default='usuarios/default.jpg')
    email         = EmailField(unique=True)
    celular1      = CharField(max_length=20, nullable)
    celular2      = CharField(max_length=20, nullable)
```

> ⚠️ `celular1`/`celular2` se conservan por compatibilidad. La señal de `apps.clientes`
> los migra automáticamente a `TelefonoContacto` al crear el perfil.

**Vistas:** `registrar_usuario`, `ingresar_usuario` (respeta `?next=` interno),
`cerrar_sesion` (**sólo POST**), `perfil_usuario`.

> El filtro `has_group` se eliminó (auditoría R-5): los templates usan las variables
> del context processor `roles_usuario`, por ejemplo `{% if es_vendedor %}`.

**Migración de grupos base** (`autenticacion/migrations/0003_grupos_base.py`):
crea los grupos `Vendedor` y `Repartidor` en cada base nueva. La asignación de
permisos se centralizó en `apps.permisos`.

---

### Módulo `apps.productos` ✅

```python
class Categoria(models.Model):
    id_categoria = AutoField(primary_key=True)
    nombre       = CharField(max_length=150)
    descripcion  = TextField()

class Producto(models.Model):
    id_producto         = AutoField(primary_key=True)
    nombre              = CharField(max_length=150)
    descripcion         = TextField()
    categoria           = ManyToManyField(Categoria)
    precio              = DecimalField(max_digits=10, decimal_places=2)
    stock               = IntegerField()
    fecha_creacion      = DateTimeField(auto_now_add=True)
    fecha_actualizacion = DateTimeField(auto_now=True)
    imagen              = ImageField(upload_to='productos/', nullable)
    activo              = BooleanField(default=True)   # oculto en tienda/buscador/carrito si False
    es_envase, es_retornable, envase (FK self)          # envases retornables (Fase 3)
```

CRUD completo: listar (paginado 6/pág + filtro categoría), ver (404 real), crear, editar,
eliminar. Si el producto ya tiene pedidos (`DetallePedido` con `PROTECT`) **se desactiva**
en lugar de borrarse.

---

### Sistema de Roles y Permisos ✅ — MÓDULO CENTRAL `apps.permisos`

La lógica antes replicada en cinco apps vive ahora en `apps/permisos/roles.py`:

```python
def es_admin(user):                       # superusuario activo
def es_vendedor(user):                    # admin o grupo "Vendedor"
def es_repartidor(user):                  # grupo "Repartidor"
def es_admin_o_vendedor(user):            # escritura en el panel
def es_admin_vendedor_o_repartidor(user): # lectura de logística
def obtener_empleado(user):               # perfil_empleado o None
def puede_ver_nota_seguridad(user, direccion)  # RNF-02
```

`apps/permisos/signals.py` sincroniza los permisos de los grupos en `post_migrate`
(aditivo, idempotente): Vendedor administra productos, clientes, pedidos,
empleados y logística; Repartidor solo hojas de ruta y sus paradas.

**Un único sistema de roles (Fase 4.6.2):** `RolEmpleado.grupo_permisos`
(vacío / `Vendedor` / `Repartidor`) define el grupo de Django del empleado. Al crear o
editar un empleado o un rol, `sincronizar_grupo_empleado()` deja al usuario sólo en
ese grupo (o en ninguno si está inactivo). Ningún rol otorga superusuario.
En vistas: funciones de `roles.py` + `apps.permisos.views.sin_permiso()`.
En templates: `es_vendedor`, `es_repartidor`, `es_personal_interno`.

| Rol | Acceso |
|---|---|
| Invitado | Ver catálogo, usar buscador |
| Cliente registrado | Todo lo anterior + carrito y sus pedidos |
| Vendedor (grupo Django) | Todo lo anterior + CRUD productos/clientes/pedidos/empleados/logística |
| Repartidor (grupo Django) | Ver e imprimir **sus** hojas de ruta; marcar entregas |
| Superusuario/Admin | Todo + `/admin/` |

---

### Módulo `apps.carrito` ✅

```python
class Carrito(models.Model):
    usuario     = OneToOneField(Usuario, on_delete=CASCADE)
    creado      = DateTimeField(auto_now_add=True)
    actualizado = DateTimeField(auto_now=True)
    # Métodos: total_items() → int, total_precio() → Decimal

class ItemCarrito(models.Model):
    carrito  = ForeignKey(Carrito, related_name='items')
    producto = ForeignKey(Producto)
    cantidad = PositiveIntegerField(default=1)
    class Meta:
        unique_together = ('carrito', 'producto')
    # Método: subtotal() → Decimal
```

**Lógica de agregar con validación de stock:**
1. `get_or_create(Carrito, usuario)` → `get_or_create(ItemCarrito)`
2. Si `stock >= nueva_cantidad` → incrementa cantidad → `messages.success`
3. Si no hay stock → elimina item si fue recién creado → `messages.error`
4. Redirección inteligente: vuelve al detalle del producto o al listado

**Vistas:** `ver_carrito`, `agregar_al_carrito`, `eliminar_del_carrito`, `vaciar_carrito`.
Las tres que modifican el carrito aceptan **sólo POST**; los productos inactivos no se agregan.

---

### Módulo `apps.buscador` ✅

**Algoritmo en dos etapas:**
```python
# Etapa 1: búsqueda exacta con normalización de tildes
# normalizar_texto("Bidón") → "bidon"
resultados = Producto.objects.filter(
    Q(nombre__icontains=query_original) | Q(nombre__icontains=query_limpia)
)

# Etapa 2 (si etapa 1 vacía): fuzzy por raíz
# Para cada palabra ≥ 3 chars → primeros 2 chars
# "coc" → icontains="co"
```
Resultados paginados (6/pág), ordenados por nombre.

---

### Módulo `apps.clientes` ✅

**Modelos implementados:**

```python
class Cliente(models.Model):
    usuario          = OneToOneField('autenticacion.Usuario',
                                     on_delete=SET_NULL, null=True, blank=True,
                                     related_name='perfil_cliente')
    nombre           = CharField(max_length=100, blank=True)
    apellido         = CharField(max_length=100, blank=True)
    email_contacto   = EmailField(blank=True)
    dni              = CharField(max_length=15, unique=True, null=True, blank=True)
    fecha_nacimiento = DateField(null=True, blank=True)
    tipo_cliente     = CharField(choices=['Normal','Premium'], default='Normal')
    bidones_prestados = PositiveIntegerField(default=0)
    permite_fiado    = BooleanField(default=False)  # Premium: siempre; Normal: excepción manual (A-D6)
    notas_internas   = TextField(blank=True)
    # Métodos: nombre_completo(), email_display(), tiene_cuenta(),
    #          es_premium(), tiene_datos_completos()

class TelefonoContacto(models.Model):
    cliente      = ForeignKey(Cliente, related_name='telefonos', on_delete=CASCADE)
    numero       = CharField(max_length=30)
    desc_relacion = CharField(max_length=60)
    es_principal = BooleanField(default=False)

class DireccionEntrega(models.Model):
    cliente        = ForeignKey(Cliente, related_name='direcciones', on_delete=CASCADE)
    calle          = CharField(max_length=150)
    numero         = CharField(max_length=10)
    piso_dpto      = CharField(max_length=30, blank=True)
    barrio         = ForeignKey('logistica.Barrio', null=True, blank=True, related_name='direcciones')
    localidad      = CharField(max_length=100)
    referencia     = TextField(blank=True)
    desc_seguridad = TextField(blank=True)  # RNF-02: visible Admin/Vendedor/repartidor ASIGNADO
    es_principal   = BooleanField(default=False)
```

> **C-6 corregido:** la nota de seguridad se etiqueta como **RNF-02**, no RF-03.

**Señal `post_save`** en `apps.clientes.signals`:
- Al registrarse un `Usuario` → crea `Cliente` automáticamente.
- Migra `celular1`/`celular2` a `TelefonoContacto`.
- Protegida contra duplicados.

**Tipos de alta:** sin cuenta web (presencial/telefónica) y con cuenta web (wizard de 2 pasos).

**Vistas:** `listar_clientes`, `crear_cliente[_sin_cuenta|_con_cuenta]`, `ver_cliente`,
`editar_cliente`, `cambiar_tipo_cliente`, `agregar/eliminar_telefono`,
`agregar/editar/eliminar_direccion`, `mi_perfil_cliente`.

**RNF-02 cerrado:** `desc_seguridad` solo se expone a superusuarios, vendedores y
al **repartidor asignado** a la parada que incluye esa dirección. Los templates
de logística (`mi_ruta_hoy`, `ver_ruta`, `imprimir_ruta`) reciben la lista
`paradas_con_nota_visible` calculada en la vista con `puede_ver_nota_seguridad()`.

---

### Módulo `apps.pedidos` ✅

**Modelos:** `Pedido`, `DetallePedido`, `PagoPedido`, `MetodoPago`.

- `Pedido`: estado (`Pendiente`, `Confirmado`, `En Camino`, `Entregado`, `Cancelado`),
  total, fecha, FK a `Cliente` y `DireccionEntrega`, FK a `MetodoPago`.
- `DetallePedido`: congela precio unitario y cantidad del producto al comprar.
- `PagoPedido`: pagos parciales, estados y transacción de MercadoPago
  (`mercadopago_payment_id`, `mercadopago_status`).
- `MetodoPago`: `EFECTIVO`, `MERCADOPAGO`, `TARJETA`, `TRANSFERENCIA`, `BILLETERA`
  (sembrados por `pedidos/migrations/0003_sembrar_metodos_pago.py`).

**Checkout & transaccionalidad:**
- `confirmar_pedido` en `@transaction.atomic` valida stock; el stock se **descuenta al cargar
  el camión** (logística) y vuelve con el regreso.
- El checkout web ofrece los métodos activos salvo `TARJETA` (decisión A-D1: el sistema no
  procesa tarjetas) y `MERCADOPAGO` si no hay token. No modifica el catálogo de métodos.
- **`pedidos/services.py`** concentra los pagos: `pago_en_curso`, `registrar_cobro` (cobro
  presencial, usado por logística), `aplicar_pago_mercadopago` (aprueba sólo si el monto
  acreditado cubre lo esperado) y `firma_webhook_valida` (`x-signature`).
- Regla de seguridad: un pago pasa a `Aprobado` sólo por el webhook firmado, por consulta a
  la API de MercadoPago o por un Vendedor. El callback `pago_exitoso` y el aviso del cliente
  `confirmar_pago_qr` **no** aprueban (auditoría H-18/H-19).
- `Pedido.cambiar_estado_manual()` / `estados_manuales_posibles()`: transiciones permitidas
  desde la gestión; `En Camino`/`Entregado` de pedidos en hoja de ruta los fija logística.
- Panel de gestión para Vendedores (`/pedidos/gestion/`) e historial (`/pedidos/mis-pedidos/`).
- **Fase 6:** cobro manual con pagos parciales desde el detalle del pedido (`/pedidos/<pk>/registrar-pago/`,
  `registrar_pago_manual`); método `CUENTA` para dejar el importe en la cuenta corriente (sólo con fiado);
  caja de 30 días en el dashboard (`resumen_caja`). `stock_disponible` = stock − comprometido (RF-12).
  **Pedido automático** `SuscripcionReposicion` (RF-18): el cliente lo activa en «Mi perfil» (o el vendedor
  en la ficha, `/pedidos/automatico/<cliente>/`); el comando diario `generar_pedidos_automaticos` crea el
  pedido (origen `AUTOMATICO`, usa el saldo prepago) y adelanta la próxima fecha.

---

### Módulo `apps.empleados` ✅ — FUENTE ÚNICA DEL PERSONAL

```python
class RolEmpleado(models.Model):
    id_rol         = AutoField(primary_key=True)
    nombre         = CharField(max_length=60, unique=True)
    descripcion    = TextField(blank=True)
    grupo_permisos = CharField(choices=['', 'Vendedor', 'Repartidor'])  # grupo que otorga

class Empleado(models.Model):
    id_empleado = AutoField(primary_key=True)
    usuario     = OneToOneField(Usuario, on_delete=SET_NULL, null=True, blank=True,
                                related_name='perfil_empleado')
    nombre, apellido, dni (unique), celular, email
    rol         = ForeignKey(RolEmpleado, on_delete=PROTECT, related_name='empleados')
    activo      = BooleanField(default=True)
    notas, fecha_creacion, fecha_actualizacion
```

**H-2/H-3 corregidos:** `logistica` ya **no** define `Empleado` ni `RolEmpleado`
propios; los importa de `apps.empleados`. Se eliminaron las tablas
`logistica_empleado` y `logistica_rolempleado`. `HojaRuta.empleado` y
`RutaReparto.empleado_default` apuntan a `empleados.Empleado`.

---

### Módulo `apps.logistica` ✅ (Mes 9–10, parcial en RF-17/RF-19)

**Modelos:** `Zona`, `Barrio`, `Camion`, `RutaReparto`, `HojaRuta`, `DetalleHojaRuta`.

**Rediseño de la hoja de ruta (20/10/2026):**
- El reparto maneja sólo **botellones llenos** (`Producto.es_botellon`) y **envases vacíos** (`es_envase`).
- **Toda parada tiene un pedido con botellones**: los frecuentes de «Planificar reparto» y las paradas manuales
  generan un `Pedido` con su renglón; la carga sugerida del camión suma esos renglones («Encargado»).
- `ver_ruta`: cada parada se despliega en una subfila con su pedido (editable si no es web y la hoja está en
  Borrador: `parada/<pk>/pedido/`) y el registro de la entrega en línea. Pedidos pendientes de la zona y
  frecuentes sugeridos se agregan con un clic (`<pk>/parada/pedido/`).
- Alta manual: cliente existente o nuevo con **nombre, calle, altura y barrio obligatorios**; el **orden es
  automático** (`renumerar_paradas`).
- Planificar y Confirmar salida permiten elegir **repartidor y camión**. Registrar regreso precarga lo
  entregado y registra los **vacíos que bajaron** (`HojaRuta.vacios_recibidos`; la diferencia con lo retirado
  en las paradas ajusta el stock del envase).
- `marcar_estado` anota la hora en cada novedad (también «Reprogramado»).

- `Zona` con días de reparto (lunes…domingo) y `barrios` relacionados.
- `Barrio` FK a `Zona`.
- `Camion` (patente PK).
- `RutaReparto`: nombre, zona, día de semana, empleado y camión por defecto.
- `HojaRuta`: fecha, `RutaReparto`, `Empleado`, `Camion`, estado
  (`Abierta`/`En curso`/`Cerrada`), observaciones, `creado_por`.
- `DetalleHojaRuta`: orden, `direccion_entrega` (FK opcional), `direccion_texto`,
  `cliente_nombre`, `pedido_ref` (CharField temporal), estado de entrega y nota.

**Vistas:** `listar_rutas`, `planificar_reparto`, `crear/ver/editar/imprimir_ruta`,
`confirmar_ruta`, `registrar_regreso_ruta`, `venta_calle`, `agregar/eliminar_parada`,
`actualizar_estado_entrega`, `mi_ruta_hoy`, CRUD de zonas y camiones, `direcciones_sin_zona`.

> ✅ **Fase 3 completada (3A–3F):** `DetalleHojaRuta.pedido` vincula cada parada con
> `pedidos.Pedido`; `logistica/services.py` agrupa frecuentes + pedidos por zona, confirma
> la hoja (→ `En Camino`), registra carga/regreso (sobrantes a stock) y las ventas en calle.
> Comando `generar_borradores_reparto [--desde AAAA-MM-DD] [--dias 15]` (RF-17, A-D5): borradores por zona
> para el período, sin confirmar. Comando de datos de demo `seed_demo` (reemplaza a `seed_logistica`, que fallaba en una base nueva). **Detalle:** [`.agents/FASE3_LOGISTICA.md`](FASE3_LOGISTICA.md).

---

### Módulo `apps.cuentas` ✅ — Fase 4

**Modelos:**

```python
class CuentaCorriente(models.Model):
    cliente        = OneToOneField(Cliente, related_name='cuenta_corriente')
    saldo          = DecimalField(12, 2, default=0)   # positivo = debe
    limite_credito = DecimalField(12, 2, default=0)   # 0 = sin límite
    activa         = BooleanField(default=True)
    fecha_apertura = DateField(auto_now_add=True)
    # Métodos: calcular_saldo(), recalcular_saldo(), permite_fiado(),
    #          dias_de_atraso(), nivel_morosidad(), estado_morosidad(), tiene_deuda()

class MovimientoCuenta(models.Model):
    cuenta            = ForeignKey(CuentaCorriente, related_name='movimientos')
    tipo              = CharField(['Cargo', 'Pago'])
    monto             = DecimalField(12, 2)
    descripcion       = CharField(200, blank=True)
    fecha             = DateTimeField(auto_now_add=True)
    fecha_vencimiento = DateField(null=True, blank=True)
    pedido            = ForeignKey('pedidos.Pedido', null=True, SET_NULL)
    abono             = ForeignKey('abonos.Abono', null=True, SET_NULL)
    # clean() aplica RF-05; save()/delete() recalcula el saldo de la cuenta
```

**Semaforización (RF-14):** `nivel_morosidad()` devuelve `al-dia` 🟢 · `amarillo` 🟡
(en plazo) · `naranja` 🟠 (≥ 10 días desde el primer cargo) · `rojo` 🔴 (≥ 15 días).
`apps/cuentas/services.py`: `obtener_o_crear_cuenta`, `registrar_cargo` (valida RF-05),
`registrar_pago`, `clientes_morosos`, `resumen_morosidad`.

**Vistas:** `listar_cuentas`, `ver_cuenta`, `cuenta_de_cliente`, `registrar_cargo`,
`registrar_pago`. URL base `/cuentas/`.

---

### Módulo `apps.abonos` ✅ — Fase 4

**Modelo `Abono`** (RF-15): `cliente`, `producto` (dispenser), `fecha_inicio`,
`fecha_fin`, `costo_mensual`, `dia_facturacion` (1-28), `estado`
(`Activo`/`Suspendido`/`Finalizado`), `ultima_facturacion`, `observaciones`.

- **RF-05:** `costo_para_cliente()` aplica `DESCUENTO_PREMIUM` (10 %) a los clientes `Premium`.
- **Facturación:** `services.generar_cargos_mensuales(anio, mes)` crea un `MovimientoCuenta`
  de tipo `Cargo` por cada abono activo en la cuenta del cliente y actualiza
  `ultima_facturacion`; omite los que no tienen fiado. Comando
  `python manage.py generar_cargos_abonos [--anio --mes]`.

**Vistas:** `listar_abonos`, `crear/editar/ver_abono`, `cambiar_estado_abono`,
`generar_cargos`. URL base `/abonos/`.

### Envases prestados (RF-08) ✅ — Fase 5A, en `apps.clientes`

**Modelo `MovimientoBidon`:** `cliente`, `tipo` (`Prestamo`/`Devolucion`/`Venta`/`Ajuste`),
`cantidad` (efecto con signo sobre el saldo), `fecha`, `pedido`, `parada`, `registrado_por`, `nota`.
`Cliente.bidones_prestados` es la **suma del historial** (caché, decisión F-D2) y ya no se edita a mano.

- `clientes/services.py::sincronizar_bidones_de_parada(parada)`: lo llaman `registrar_entrega` y
  `crear_venta_calle`. Entregado → Préstamo de `cantidad_bidones`; vacíos retirados → Devolución;
  envases vendidos → Venta. Reconcilia por parada (idempotente).
- `registrar_movimiento_bidon(...)`: alta manual desde la ficha (`/clientes/<pk>/envases/movimiento/`);
  no deja el saldo negativo salvo en el registro de campo.

### Módulo `apps.promociones` ✅ — Fase 5B/5C (RF-09, RF-10)

- **`Promocion`:** `nombre`, `producto`, `cant_paga`, `cant_lleva`, `precio` (del pack), `dias_validez` (30), `activa`.
- **`CompraPromocion`:** pack de un cliente; `unid_totales` = `cant_lleva`, `unid_restantes`,
  `fecha_caducidad` = compra + 30 días corridos, `estado` (`Vigente`/`Agotada`/`Vencida`), `pedido` del pago.
- **`ConsumoPromocion`:** unidades usadas por cada pedido.
- `services.py`: `vender_promocion` (cobro o cargo a cuenta, valida fiado), `consumir_saldo` (FIFO por
  vencimiento; ignora lo vencido aunque no haya corrido el comando), `revertir_consumos` (al cancelar;
  lo vencido no se reintegra, F-D5), `vencer_promociones`, `promociones_por_vencer`.
- **Checkout web:** las unidades cubiertas van en un renglón a $0; si cubre todo, el pedido queda
  `Confirmado` sin cobro. El checkout y «Mi perfil» muestran el saldo vigente.
- Comando diario `python manage.py vencer_promociones`. Dashboard: alerta de packs que vencen en ≤ 5 días.
- **Vistas:** `listar_promociones`, `crear/editar_promocion`, `vender_promocion` (desde la ficha del cliente).

---

### Frontend y Templates ✅

`base.html` tiene: Bootstrap 5.3 dark mode, Font Awesome 6, navbar con toggle dark/light,
buscador integrado, badge del carrito, menú `+ Crear` condicional (Vendedor/Admin),
mensajes Django **persistentes** (sin auto-dismiss).
El nombre de usuario en la navbar es un **link** a `/clientes/mi-perfil/`.

---

## 5. 🔲 LO QUE ESTÁ PENDIENTE (Fases 3–7)

### Fase 3 — Logística ↔ Pedido ✅
- [x] Vincular `DetalleHojaRuta` → `pedidos.Pedido` (FK); `pedido_ref` se conserva (H-4)
- [x] Agrupar pedidos `Confirmado` por zona y proponer carga (RF-17)
- [x] Generación de hojas de ruta (planificar + comando de datos de demo) (RF-17)
- [x] Al marcar entrega: actualizar `Pedido.estado` y stock en `transaction.atomic` (RF-19)

### Fase 4 — Cuentas corrientes, morosidad y abonos ✅
- [x] `apps.cuentas`: `CuentaCorriente`, `MovimientoCuenta` (RF-14)
- [x] Regla de fiado solo para clientes `Premium`/`permite_fiado` (RF-05)
- [x] Semaforización 🟡 en plazo · 🟠 10 días · 🔴 15 días
- [x] `apps.abonos`: alquiler de dispensers + facturación mensual (RF-15)
- [ ] Resolver C-9 (RF-20 gastos por proveedor: dentro o fuera de alcance)

### Fase 5 — Bidones y promociones prepago ✅
- [x] Historial `MovimientoBidon` (entrada/salida) — `bidones_prestados` pasa a ser su saldo (RF-08)
- [x] `Promocion` / saldo de promoción "Paga 3 Lleva 4" (RF-09)
- [x] Caducidad estricta a 30 días corridos (RF-10)

### Fase 6 — Pagos parciales y pedido automático 🔴
- [ ] Bloquear checkout con <2 teléfonos o 0 direcciones (RF-04)
- [ ] Vista de cobro manual con pagos parciales (RF-13, HU-05)
- [ ] `PedidoAutomatico` quincenal (RF-18)

### Fase 7 — QA, producción y tesis 🎓
- [x] Tests de permisos, roles y RNF-02 (`apps/permisos/tests.py`)
- [x] `settings/production.py` completo
- [x] `SECRET_KEY` y credenciales MP en entorno
- [ ] Suites de carrito, pedidos, logística, cuentas y buscador
- [ ] Verificar el DER del informe contra el esquema real
- [ ] Memoria final de tesis

---

## 6. 🗃️ Esquema Relacional Actual (Implementado)

```
autenticacion.Usuario (AbstractUser)
    ├── clientes.Cliente  [OneToOne, nullable]
    │       ├── TelefonoContacto [FK] → numero, desc_relacion, es_principal
    │       └── DireccionEntrega [FK] → calle, altura, barrio [FK→logistica.Barrio],
    │                                   desc_seguridad (RNF-02), es_principal
    ├── carrito.Carrito [OneToOne]
    │       └── ItemCarrito [FK→productos.Producto]
    └── empleados.Empleado [OneToOne, nullable, related_name=perfil_empleado]
            └── rol [FK→empleados.RolEmpleado]

productos.Producto [ManyToMany→ Categoria]

pedidos.Pedido [FK→Cliente, FK→DireccionEntrega, FK→MetodoPago]
    ├── DetallePedido [FK→Producto]
    └── PagoPedido

logistica.Zona
    └── Barrio [FK→Zona]
logistica.Camion
logistica.RutaReparto [FK→Zona, FK→Empleado, FK→Camion]
    └── HojaRuta [FK→RutaReparto, FK→Zona, FK→Empleado, FK→Camion, FK→Usuario(creado_por)]
            ├── DetalleHojaRuta [FK→pedidos.Pedido, FK→Cliente, FK→DireccionEntrega; pedido_ref manual]
            └── CargaHojaRuta [FK→Producto] → cantidad_cargada/entregada/retornada

cuentas.CuentaCorriente [OneToOne→Cliente]
    └── MovimientoCuenta [FK→Pedido?, FK→abonos.Abono?] → tipo Cargo/Pago, saldo (RF-14)
abonos.Abono [FK→Cliente, FK→Producto] → costo mensual, estado (RF-15)
```

---

## 7. 🗃️ Esquema Relacional Completo (Diseño Final Planificado)

```
Cliente
    ├── TelefonoContacto
    ├── DireccionEntrega [FK→Zona] ──────────────┐
    ├── Pedido                                     │
    │       ├── DetallePedido                      │
    │       ├── PagoPedido → MetodoPago            │
    │       └── DetalleHojaRuta → HojaRuta ────────┘
    ├── CuentaCorriente → MovimientoCuenta
    ├── Abono → Producto
    └── SaldoDispensadorPromocion → Promocion

Producto → Categoria
RolEmpleado ← Empleado → HojaRuta
Camion ← RutaReparto → Zona
```

---

## 8. 🗺️ Mapa de URLs Actual

```
/                              → inicio
/admin/                        → Django Admin

/productos/                    → listar_productos
/productos/producto/<pk>       → ver_producto
/productos/crear/              → crear_producto        [🔒 Vendedor/Admin]
/productos/categoria/crear/    → crear_categoria       [🔒 Vendedor/Admin]
/productos/editar/<pk>         → editar_producto       [🔒 Vendedor/Admin]
/productos/eliminar/<pk>       → eliminar_producto     [🔒 Vendedor/Admin]

/auth/registrar/               → registrar_usuario
/auth/ingresar/                → ingresar_usuario
/auth/cerrar_sesion/           → cerrar_sesion
/auth/perfil/                  → perfil_usuario        [🔒 Login]

/carrito/                      → ver_carrito           [🔒 Login]
/carrito/agregar/<id>/         → agregar_al_carrito    [🔒 Login]
/carrito/eliminar/<id>/        → eliminar_del_carrito  [🔒 Login]
/carrito/vaciar/               → vaciar_carrito        [🔒 Login]

/buscador/?q=<query>           → buscar_productos

/clientes/                     → listar_clientes       [🔒 Login]
/clientes/nuevo/               → selector tipo de alta [🔒 Admin/Vendedor]
/clientes/nuevo/sin-cuenta/    → alta sin cuenta web   [🔒 Admin/Vendedor]
/clientes/nuevo/con-cuenta/    → alta con cuenta web   [🔒 Admin/Vendedor]
/clientes/<pk>/                → ver_cliente           [🔒 Admin/Vendedor]
/clientes/<pk>/editar/         → editar_cliente        [🔒 Admin/Vendedor]
/clientes/<pk>/tipo/           → cambiar_tipo_cliente  [🔒 Admin/Vendedor]
/clientes/<pk>/telefono/nuevo/ → agregar_telefono      [🔒 Admin/Vendedor]
/clientes/telefono/<pk>/eliminar/ → eliminar_telefono  [🔒 Admin/Vendedor]
/clientes/<pk>/direccion/nueva/   → agregar_direccion  [🔒 Admin/Vendedor]
/clientes/direccion/<pk>/editar/  → editar_direccion   [🔒 Admin/Vendedor]
/clientes/direccion/<pk>/eliminar/→ eliminar_direccion [🔒 Admin/Vendedor]
/clientes/mi-perfil/           → mi_perfil_cliente     [🔒 Login]

/pedidos/checkout/             → checkout              [🔒 Login]
/pedidos/confirmar/            → confirmar_pedido      [🔒 Login]
/pedidos/pago/exitoso|pendiente|fallido/ → callbacks MP
/pedidos/webhook/mercadopago/  → webhook_mercadopago
/pedidos/<pk>/pago-qr/         → pago_qr               [🔒 Login]
/pedidos/<pk>/confirmar-qr/    → confirmar_pago_qr     [🔒 Login]
/pedidos/mis-pedidos/          → mis_pedidos           [🔒 Login]
/pedidos/gestion/              → listar_pedidos        [🔒 Admin/Vendedor]
/pedidos/<pk>/                 → detalle_pedido        [🔒 Login]
/pedidos/<pk>/cambiar-estado/  → cambiar_estado_pedido [🔒 Admin/Vendedor]
/pedidos/<pk>/cambiar-estado-pago/ → cambiar_estado_pago [🔒 Admin/Vendedor]

/logistica/                    → listar_rutas          [🔒 Admin/Vendedor/Repartidor]
/logistica/nueva/              → crear_ruta            [🔒 Admin/Vendedor]
/logistica/<pk>/               → ver_ruta              [🔒 Admin/Vendedor/Repartidor asignado]
/logistica/<pk>/editar/        → editar_ruta           [🔒 Admin/Vendedor]
/logistica/<pk>/imprimir/      → imprimir_ruta         [🔒 Admin/Vendedor/Repartidor asignado]
/logistica/<pk>/parada/agregar/→ agregar_parada        [🔒 Admin/Vendedor]
/logistica/parada/<pk>/eliminar/ → eliminar_parada     [🔒 Admin/Vendedor]
/logistica/parada/<pk>/estado/ → actualizar_estado_entrega [🔒 asignado]
/logistica/mi-ruta/            → mi_ruta_hoy           [🔒 Admin/Vendedor/Repartidor]
/logistica/zonas/              → listar_zonas          [🔒 Admin/Vendedor]
/logistica/camiones/           → listar_camiones       [🔒 Admin/Vendedor]

/empleados/                    → listar_empleados      [🔒 Admin/Vendedor]
/empleados/nuevo/              → crear_empleado        [🔒 Admin/Vendedor]
/empleados/<pk>/               → ver_empleado          [🔒 Admin/Vendedor]
/empleados/<pk>/editar/        → editar_empleado       [🔒 Admin/Vendedor]
/empleados/<pk>/estado/        → cambiar_estado        [🔒 Admin/Vendedor]
/empleados/<pk>/eliminar/      → eliminar_empleado     [🔒 Admin/Vendedor]
/empleados/roles/              → listar_roles          [🔒 Admin/Vendedor]
/empleados/roles/nuevo/        → crear_rol             [🔒 Admin/Vendedor]

/cuentas/                      → listar_cuentas        [🔒 Admin/Vendedor]
/cuentas/<pk>/                 → ver_cuenta            [🔒 Admin/Vendedor]
/cuentas/cliente/<pk>/         → cuenta_de_cliente     [🔒 Admin/Vendedor]
/cuentas/<pk>/cargo/           → registrar_cargo       [🔒 Admin/Vendedor]
/cuentas/<pk>/pago/            → registrar_pago        [🔒 Admin/Vendedor]

/abonos/                       → listar_abonos         [🔒 Admin/Vendedor]
/abonos/nuevo/                 → crear_abono           [🔒 Admin/Vendedor]
/abonos/<pk>/                  → ver_abono             [🔒 Admin/Vendedor]
/abonos/<pk>/editar/           → editar_abono          [🔒 Admin/Vendedor]
/abonos/<pk>/estado/           → cambiar_estado_abono  [🔒 Admin/Vendedor]
/abonos/generar-cargos/        → generar_cargos        [🔒 Admin/Vendedor]

/promociones/                  → listar_promociones    [🔒 Admin/Vendedor]
/promociones/nueva/            → crear_promocion       [🔒 Admin/Vendedor]
/promociones/<pk>/editar/      → editar_promocion      [🔒 Admin/Vendedor]
/promociones/vender/<cliente>/ → vender_promocion      [🔒 Admin/Vendedor, POST]
/clientes/<pk>/envases/movimiento/ → registrar_movimiento_bidon [🔒 Admin/Vendedor, POST]
```

---

## 9. 📖 Historias de Usuario

| HU | Como | Quiero | Estado |
|---|---|---|---|
| HU-01 | Cliente nuevo | Registrarme con ≥2 teléfonos y relación explícita | ✅ Completa (H-40 corregido) |
| HU-02 | Cliente registrado | Guardar múltiples domicilios con zona y nota de seguridad | ✅ Completa |
| HU-03 | Visitante | Buscar sin tildes ni mayúsculas | ✅ Completa |
| HU-04 | Usuario no logueado | Al intentar agregar al carrito → redirige a login con alerta | ✅ Completa |
| HU-05 | Vendedor | Registrar pagos parciales → auto-actualiza estado pedido | 🔲 Pendiente |
| HU-06 | Repartidor | Marcar estado de entrega desde la app | ✅ Completa (impacta `Pedido`) |
| HU-07 | Vendedor | Dar de alta un cliente sin cuenta web para pedidos telefónicos | ✅ Completa |
| HU-08 | Admin | Ver ficha completa de cliente con teléfonos, domicilios y seguridad | ✅ Completa |

---

## 10. 📅 Cronograma Canónico (reconciliado)

| Mes | Hito | Estado real |
|:---:|---|:---:|
| 1–3 | Relevamiento, análisis, DER | ✅ Completado |
| 4 | CRUD core de productos + categorías | ✅ Completado |
| 5 | Seguridad, roles y validadores de claves | ✅ Completado |
| 6 | UX, buscador, carrito | ✅ Completado |
| 7 | Segmentación y gestión de clientes | ✅ Completado |
| 8 | Lógica transaccional: Pedidos, Pagos, MercadoPago | ✅ Completado |
| 9 | Empleados, roles y estructura logística | ✅ Completado |
| 10 | Hojas de ruta + vista de repartidor | ✅ Completado |
| 11 | Cuentas corrientes, morosidad, abonos; bidones, promociones | 🟡 Parcial (cuentas y abonos ✅) |
| 12 | RF-18, tests restantes, memoria de tesis | 🔴 Pendiente |

> Este cronograma reemplaza al del Informe de Avances (Julio 2026), que describe 4 apps
> y no menciona MercadoPago, `empleados` ni `logistica`.

---

## 11. ⚠️ Deuda Técnica y Estado de Correcciones

| Problema | Severidad | Estado |
|---|---|:---:|
| `SECRET_KEY` hardcodeada en `base.py` | 🔴 Alta | ✅ Resuelta (`python-decouple` + `.env`) |
| `production.py` vacío | 🔴 Alta | ✅ Resuelto (`DEBUG=False`, HTTPS, hosts, MP) |
| Grupo `Vendedor` inexistente | 🔴 Crítica | ✅ Resuelto (migración `0003_grupos_base`) |
| `Empleado`/`RolEmpleado` duplicados | 🔴 Crítica | ✅ Resuelto (fuente única en `apps.empleados`) |
| `groups.all.0` en templates | 🔴 Alta | ✅ Resuelto (context processor `roles_usuario`) |
| Pagos aprobables desde la URL / por el propio cliente (H-18/H-19) | 🔴 Crítica | ✅ Resuelto (Fase 4.6.1) |
| Tres sistemas de roles desconectados (H-24/H-25) | 🟠 Alta | ✅ Resuelto (`RolEmpleado.grupo_permisos`) |
| Errores 500 en roles, rutas, zonas, direcciones, clientes y productos | 🟠 Alta | ✅ Resueltos (Fases 4.6.3 y 4.6.5) |
| Una sola dirección por cliente vs RF-03 multidirección (H-39) | 🟠 Media | ✅ Resuelto (A-D4: varias direcciones) |
| RNF-02 sin filtro por repartidor asignado | 🟠 Media | ✅ Resuelto (`puede_ver_nota_seguridad`) |
| Cero tests | 🟠 Media | 🟢 Avanzado (160 tests; buscador sin suite propia) |
| Carrito no descuenta stock ni genera Pedido | 🟠 Media | 🟡 Pedidos ya descuentan; falta reserva en carrito (RF-12) |
| `celular1/celular2` en `Usuario` redundantes | 🟡 Baja | 🟡 Se migran vía señal |
| `DetalleHojaRuta` no vinculado a `Pedido` | 🔴 Alta | ✅ Resuelto (Fase 3) |

---

*Contexto actualizado: 20/10/2026 — Versión 4.2 (Fases 4.5 y 4.6: consolidación y auditoría).*
*Actualizar este archivo ante cualquier cambio estructural significativo.*
