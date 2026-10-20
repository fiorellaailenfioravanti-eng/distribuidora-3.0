# 🌊 Aquadelluvia — Contexto Maestro del Proyecto
> **Distribuidora 3.0** · Sistema de Gestión Operativa, Logística y E-Commerce
>
> **⚠️ LEER PRIMERO:** Este archivo provee todo el contexto necesario para trabajar en este proyecto.
> Última actualización: 30/09/2026 — Versión 4.0.

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
│   ├── autenticacion/               # ✅ Usuarios, login, perfil, templatetag has_group
│   ├── buscador/                    # ✅ Búsqueda tolerante a tildes
│   ├── carrito/                     # ✅ Carrito transaccional + validación stock
│   ├── productos/                   # ✅ CRUD catálogo y categorías
│   ├── clientes/                    # ✅ Gestión de clientes, teléfonos y direcciones
│   ├── pedidos/                     # ✅ Checkout, Pedido, Pagos, MercadoPago, webhook
│   ├── logistica/                   # ✅ Zonas, barrios, camiones, rutas y hojas de ruta
│   ├── empleados/                   # ✅ Empleados y roles (FUENTE ÚNICA del personal)
│   ├── cuentas/                     # ✅ Cuentas corrientes, fiado y semaforización (RF-14)
│   ├── abonos/                      # ✅ Alquiler de dispensers y facturación (RF-15)
│   └── permisos/                    # ✅ Módulo central de roles + sincronización de grupos
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
MERCADOPAGO_ACCESS_TOKEN = config('MERCADOPAGO_ACCESS_TOKEN', default='')
```

> `production.py` **no** admite defaults: si falta `SECRET_KEY`, `ALLOWED_HOSTS`,
> `MERCADOPAGO_ACCESS_TOKEN` o `MERCADOPAGO_WEBHOOK_SECRET`, el arranque falla.

### Context Processors habilitados

```python
'apps.carrito.context_processors.carrito_total'  # Inyecta carrito_total_items globalmente
```

### Cómo correr el proyecto

```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env          # completar SECRET_KEY, ALLOWED_HOSTS y credenciales MP
python manage.py migrate --settings=distribuidora.settings.local
python manage.py createsuperuser --settings=distribuidora.settings.local
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

**Vistas:** `registrar_usuario`, `ingresar_usuario`, `cerrar_sesion`, `perfil_usuario`

**Template tag** (`autenticacion/templatetags/grupos.py`):
```python
@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
# Uso en templates: {% if user|has_group:"Vendedor" %}
```

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
```

CRUD completo: listar (paginado 6/pág + filtro categoría), ver, crear, editar, eliminar.

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

**Vistas:** `ver_carrito`, `agregar_al_carrito`, `eliminar_del_carrito`, `vaciar_carrito`

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
    permite_fiado    = BooleanField(default=False)  # auto True para Premium
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
- Operación en `@transaction.atomic` con validación y descuento de stock.
- Integración del SDK `mercadopago` con preferencias, callbacks y webhook
  (`/pedidos/webhook/mercadopago/`). El **token se lee del entorno** (no está en el código).
- Panel de gestión para Vendedores (`/pedidos/gestion/`) e historial (`/pedidos/mis-pedidos/`).

---

### Módulo `apps.empleados` ✅ — FUENTE ÚNICA DEL PERSONAL

```python
class RolEmpleado(models.Model):
    id_rol      = AutoField(primary_key=True)
    nombre      = CharField(max_length=60, unique=True)
    descripcion = TextField(blank=True)

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
> Comando de demo `seed_logistica`. **Detalle:** [`.agents/FASE3_LOGISTICA.md`](FASE3_LOGISTICA.md).

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

### Fase 5 — Bidones y promociones prepago 🔴
- [ ] Historial `MovimientoBidon` (entrada/salida) — reemplaza `bidones_prestados` (RF-08)
- [ ] `Promocion` / saldo de promoción "Paga 3 Lleva 4" (RF-09)
- [ ] Caducidad estricta a 30 días corridos (RF-10)

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
```

---

## 9. 📖 Historias de Usuario

| HU | Como | Quiero | Estado |
|---|---|---|---|
| HU-01 | Cliente nuevo | Registrarme con ≥2 teléfonos y relación explícita | ✅ Completa |
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
| `groups.all.0` en templates | 🔴 Alta | ✅ Resuelto (`has_group` + `apps.permisos`) |
| RNF-02 sin filtro por repartidor asignado | 🟠 Media | ✅ Resuelto (`puede_ver_nota_seguridad`) |
| Cero tests | 🟠 Media | 🟢 Avanzado (86 tests: permisos, cuentas, abonos, etc.) |
| Carrito no descuenta stock ni genera Pedido | 🟠 Media | 🟡 Pedidos ya descuentan; falta reserva en carrito (RF-12) |
| `celular1/celular2` en `Usuario` redundantes | 🟡 Baja | 🟡 Se migran vía señal |
| `DetalleHojaRuta` no vinculado a `Pedido` | 🔴 Alta | ✅ Resuelto (Fase 3) |

---

*Contexto actualizado: 14/10/2026 — Versión 4.1 (Fase 4: cuentas corrientes y abonos).*
*Actualizar este archivo ante cualquier cambio estructural significativo.*
