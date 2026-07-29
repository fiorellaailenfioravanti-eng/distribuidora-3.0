# 🌊 Aquadelluvia — Contexto Maestro del Proyecto
> **Distribuidora 3.0** · Sistema de Gestión Operativa, Logística y E-Commerce
>
> **⚠️ LEER PRIMERO:** Este archivo provee todo el contexto necesario para trabajar en este proyecto.
> Última actualización: 29/07/2026 — Versión 3.0.

---

## 1. 📋 Información General

| Campo | Detalle |
|---|---|
| **Proyecto** | Sistema de Gestión Integral y Plataforma E-commerce |
| **Empresa cliente** | Distribuidora "Aquadelluvia" (Presidencia Roque Sáenz Peña, Chaco, Argentina) |
| **Institución** | Universidad Nacional del Chaco Austral (UNCAUS) – Ingeniería en Sistemas de Información |
| **Contexto** | Trabajo Final de Grado / Tesis (Cátedra de Gestión de Datos) |
| **Framework** | Django 5.0 (Python) |
| **Base de datos** | SQLite3 (desarrollo) |

### 👥 Equipo de Desarrollo

| Integrante | L.U. | Módulo asignado |
|---|---|---|
| **Fiorella Ailén Fioravanti** | 15427 | Portal web e-commerce: autenticación, catálogo, carrito, seguridad, clientes |
| **Lucas** | — | Módulo logístico: hojas de ruta, agrupación geográfica, app para repartidores |

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

### Patrón: Django MVT

| Capa | Tecnología | Detalle |
|---|---|---|
| **Model** | Django ORM + SQLite 3 | Mapeo ORM, transacciones ACID, serverless, `db.sqlite3` local |
| **View** | Function-Based Views (FBV) | Lógica de negocio con decoradores `@login_required` |
| **Template** | Django Template Language (DTL) | HTML5 + Bootstrap 5.3 (dark mode) |
| **Auth** | Django Auth (modelo custom) | `AbstractUser` extendido (`autenticacion.Usuario`) |
| **Media** | Pillow | Manejo de `ImageField` para productos y perfiles |
| **Búsqueda** | `unicodedata` (stdlib Python) | Normalización de tildes y búsqueda fuzzy |
| **Idioma/Zona** | `es-AR` / `America/Argentina/Buenos_Aires` | — |

### Estructura de Directorios

```
DISTRIBUIDORA-3.0/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── distribuidora/
│   ├── urls.py                      # Router raíz
│   ├── views.py                     # Vista de inicio
│   └── settings/
│       ├── base.py                  # Config compartida
│       ├── local.py                 # Dev: DEBUG=True, SQLite
│       └── production.py            # [VACÍO — pendiente]
├── apps/
│   ├── autenticacion/               # ✅ Usuarios, roles, perfiles, login
│   ├── buscador/                    # ✅ Búsqueda tolerante a tildes
│   ├── carrito/                     # ✅ Carrito transaccional + validación stock
│   ├── productos/                   # ✅ CRUD catálogo y categorías
│   ├── clientes/                    # ✅ Gestión de clientes (Mes 7) — NUEVO
│   └── abonos/                      # 🔲 Alquileres de dispensers [PLANIFICADO]
├── templates/
├── static/
└── media/
```

### Configuración clave (`base.py`)

```python
AUTH_USER_MODEL     = 'autenticacion.Usuario'
LOGIN_URL           = '/auth/ingresar/'
LOGIN_REDIRECT_URL  = '/'
LOGOUT_REDIRECT_URL = '/auth/ingresar/'
LANGUAGE_CODE       = 'es-AR'
TIME_ZONE           = 'America/Argentina/Buenos_Aires'
```

### Context Processors habilitados

```python
'apps.carrito.context_processors.carrito_total'  # Inyecta carrito_total_items globalmente
```

### Cómo correr el proyecto

```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate --settings=distribuidora.settings.local
python manage.py createsuperuser --settings=distribuidora.settings.local
python manage.py runserver --settings=distribuidora.settings.local
# → http://127.0.0.1:8000/
```

---

## 4. ✅ LO QUE ESTÁ REALIZADO (Meses 1–7)

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
Rutas de escritura protegidas con `@user_passes_test(es_vendedor_o_admin)`.

---

### Sistema de Roles y Permisos ✅

```python
def es_vendedor_o_admin(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists()
```

| Rol | Acceso |
|---|---|
| Invitado | Ver catálogo, usar buscador |
| Cliente registrado | Todo lo anterior + carrito |
| Vendedor (grupo Django) | Todo lo anterior + CRUD productos/categorías |
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

> ⚠️ El carrito valida stock pero **NO lo descuenta ni genera un Pedido**.
> El módulo de Pedidos (Mes 8) es la pieza central pendiente.

**Context Processor** (`apps.carrito.context_processors.carrito_total`):
Inyecta `carrito_total_items` en todos los templates → badge del carrito en navbar.

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

### Módulo `apps.clientes` ✅ — NUEVO (Mes 7)

**Modelos implementados:**

```python
class Cliente(models.Model):
    # Cuenta web (opcional — null si el cliente no compra online)
    usuario          = OneToOneField('autenticacion.Usuario',
                                     on_delete=SET_NULL, null=True, blank=True,
                                     related_name='perfil_cliente')
    # Datos propios (usados cuando no hay cuenta, o como complemento)
    nombre           = CharField(max_length=100, blank=True)
    apellido         = CharField(max_length=100, blank=True)
    email_contacto   = EmailField(blank=True)
    # Datos de negocio
    dni              = CharField(max_length=15, unique=True, null=True, blank=True)
    fecha_nacimiento = DateField(null=True, blank=True)
    tipo_cliente     = CharField(choices=['Normal','Premium'], default='Normal')
    bidones_prestados = PositiveIntegerField(default=0)
    permite_fiado    = BooleanField(default=False)  # auto True para Premium
    notas_internas   = TextField(blank=True)

    # Métodos clave:
    # nombre_completo() → str   (usa usuario o nombre+apellido propios)
    # email_display()   → str   (usa email del usuario o email_contacto)
    # tiene_cuenta()    → bool
    # es_premium()      → bool
    # tiene_datos_completos() → bool (≥2 teléfonos + ≥1 dirección)

class TelefonoContacto(models.Model):
    cliente      = ForeignKey(Cliente, related_name='telefonos', on_delete=CASCADE)
    numero       = CharField(max_length=30)
    desc_relacion = CharField(max_length=60)   # "Titular", "Familiar", etc.
    es_principal = BooleanField(default=False)  # solo 1 por cliente

class DireccionEntrega(models.Model):
    cliente        = ForeignKey(Cliente, related_name='direcciones', on_delete=CASCADE)
    calle          = CharField(max_length=150)
    numero         = CharField(max_length=10)
    piso_dpto      = CharField(max_length=30, blank=True)
    barrio         = CharField(max_length=100, blank=True)
    localidad      = CharField(max_length=100)
    referencia     = TextField(blank=True)
    desc_seguridad = TextField(blank=True)  # RF-03: solo visible Admin/Vendedor/Repartidor
    es_principal   = BooleanField(default=False)
```

**Señal `post_save`** en `apps.clientes.signals`:
- Al registrarse un `Usuario` → crea `Cliente` automáticamente (con nombre/apellido del usuario).
- Migra `celular1`/`celular2` a `TelefonoContacto`.
- Protegida contra duplicados.

**Tipos de alta de cliente:**
1. **Sin cuenta web** (`/clientes/nuevo/sin-cuenta/`) — Solo Admin/Vendedor. Para clientes presenciales/telefónicos.
2. **Con cuenta web** (`/clientes/nuevo/con-cuenta/`) — Wizard de 2 pasos: Paso 1 = Datos personales + teléfonos dinámicos, Paso 2 = Credenciales de acceso.

**Teléfonos dinámicos en alta:** El formulario permite agregar N teléfonos con descripción mediante tabla JavaScript (botón `+` agrega fila, botón 🗑️ elimina). Se procesan en `guardar_telefonos_dinamicos()` en `views.py`.

**Vistas y URLs:**

| Vista | URL | Acceso |
|---|---|---|
| `listar_clientes` | `/clientes/` | Login |
| `crear_cliente` | `/clientes/nuevo/` | Admin/Vendedor |
| `crear_cliente_sin_cuenta` | `/clientes/nuevo/sin-cuenta/` | Admin/Vendedor |
| `crear_cliente_con_cuenta` | `/clientes/nuevo/con-cuenta/` | Admin/Vendedor |
| `ver_cliente` | `/clientes/<pk>/` | Login |
| `editar_cliente` | `/clientes/<pk>/editar/` | Admin/Vendedor |
| `cambiar_tipo_cliente` | `/clientes/<pk>/tipo/` | Admin/Vendedor |
| `agregar_telefono` | `/clientes/<pk>/telefono/nuevo/` | Admin/Vendedor |
| `eliminar_telefono` | `/clientes/telefono/<pk>/eliminar/` | Admin/Vendedor |
| `agregar_direccion` | `/clientes/<pk>/direccion/nueva/` | Admin/Vendedor |
| `editar_direccion` | `/clientes/direccion/<pk>/editar/` | Admin/Vendedor |
| `eliminar_direccion` | `/clientes/direccion/<pk>/eliminar/` | Admin/Vendedor |
| `mi_perfil_cliente` | `/clientes/mi-perfil/` | Cliente propio |

**Comportamientos especiales:**
- 🟡 Badge amarillo en listado: cliente con menos de 2 teléfonos.
- 🔴 Badge rojo: sin teléfonos o sin dirección.
- ⭐ Toggle Normal↔Premium desde la ficha (auto-habilita fiado).
- 🛡️ `desc_seguridad` invisible para el propio cliente (RF-03 cumplido).
- Las notificaciones (alertas Django) **no desaparecen automáticamente** (timeout desactivado en `main.js`).

---

### Frontend y Templates ✅

`base.html` tiene: Bootstrap 5.3 dark mode, Font Awesome 6, navbar con toggle dark/light,
buscador integrado, badge del carrito, menú `+ Crear` condicional (Vendedor/Admin),
mensajes Django **persistentes** (sin auto-dismiss).

El nombre de usuario en la navbar es un **link** a `/clientes/mi-perfil/`.

---

## 5. 🔲 LO QUE ESTÁ PENDIENTE (Meses 8–12)

### Mes 8 — Lógica Transaccional Avanzada 🔴 PENDIENTE

- [ ] `@transaction.atomic` en vistas de pedidos, pagos y stock
- [ ] `Django Signals` (`post_save`) para actualizar estado pedido cuando suma pagos = total
- [ ] Módulo completo de **Pedidos**: estado (`Pendiente`, `Confirmado`, `Entregado`, `Cancelado`), dirección seleccionada, desglose de items
- [ ] Pagos parciales con múltiples métodos: Efectivo, Transferencia, Tarjeta de Débito, Billetera Digital

**Tablas planificadas:**
```
Pedido               (id_pedido [PK], estado, total, fecha, id_cliente [FK→Cliente])
Producto_incluye_pedido (id_pedido [PK,FK], id_producto [PK,FK], precio_unit, cantidad, subtotal)
Pago_pedido          (id_pago [PK], monto, fecha, id_metodo [FK], id_pedido [FK])
Metodo_pago          (id_metodo [PK], descripcion)
```

> ⚠️ El `Pedido` ahora referencia `Cliente.pk` (no DNI), consistente con el modelo implementado.

---

### Mes 9 — Cuentas Corrientes, Bidones y Promociones 🔴 PENDIENTE

- [ ] Trazabilidad de bidones prestados sin cargo (RF-08) — el campo `bidones_prestados` ya existe en `Cliente`
- [ ] `apps.abonos`: contratos de alquiler mensual con estado (`Activo`, `Suspendido`, `Finalizado`)
- [ ] Promociones prepago "Paga 3, lleva 4" con entregas parciales (RF-09)
- [ ] Caducidad estricta: saldo de promociones vence a los **30 días corridos** (RF-10)
- [ ] Semaforización de deuda en cuentas corrientes (RF-14):
  - 🟡 Amarillo: deuda al comenzar el mes
  - 🟠 Naranja: 10 días sin saldar
  - 🔴 Rojo: más de 15 días (+ notificación automatizada)

**Tablas planificadas:**
```
Cliente_alquila_producto (id_cliente [PK,FK], id_producto [PK,FK], fecha_inicio, costo_mensual, estado)
Promociones              (id_promo [PK], nombre, cant_articulos, plazo_validez)
Incluye_promo            (id_promo [PK,FK], id_pedido [PK,FK], cant_comprada, subtotal)
Saldo_disp_promocion     (id_cliente [FK], id_promo [FK], id_pedido [FK], unid_restantes, fecha_caducidad)
```

---

### Mes 10 — Logística y Hojas de Ruta 🔴 PENDIENTE (módulo Lucas)

- [ ] Creación de Hojas de Ruta diarias (fecha, zona, camión, chofer)
- [ ] Algoritmo de ordenamiento de pedidos por dirección/zona
- [ ] Generación quincenal automática de rutas (RF-17)
- [ ] Interfaz para repartidores: `Entregado` / `Cancelado` en tiempo real (RF-19)

**Tablas planificadas:**
```
Empleado         (id_empleado [PK], dni [FK→Persona], id_rol [FK→Rol_empleado])
Rol_empleado     (id_rol [PK], descripcion)
Camion           (patente [PK], descripcion)
Zona             (id_zona [PK], nombre)
Hoja_ruta        (id_ruta [PK], fecha, id_empleado [FK], patente [FK], id_zona [FK])
Detalle_hoja_ruta(id_pedido [PK,FK], id_ruta [PK,FK], estado)
```

---

### Mes 11 — Alertas y Automatizaciones 🔴 PENDIENTE

- [ ] Panel visual de morosidad con semaforización
- [ ] Notificaciones automáticas para deuda > 15 días
- [ ] Alertas de vencimiento de saldos de promociones

---

### Mes 12 — QA, Testing y Memoria Final 🔴 PENDIENTE

- [ ] Tests unitarios e integración (`pytest-django` / `unittest`)
- [ ] Completar `distribuidora/settings/production.py`
- [ ] Mover `SECRET_KEY` a variable de entorno (`.env`)
- [ ] Redacción del documento final de Tesis

---

## 6. 🗃️ Esquema Relacional Actual (Implementado)

```
autenticacion.Usuario (AbstractUser)
    └── clientes.Cliente  [OneToOne, nullable → usuario puede ser NULL]
            ├── nombre, apellido, email_contacto  (campos propios si no tiene cuenta)
            ├── dni, fecha_nacimiento, tipo_cliente, bidones_prestados, permite_fiado
            ├── TelefonoContacto  [FK, multiple] → numero, desc_relacion, es_principal
            └── DireccionEntrega  [FK, multiple] → calle, numero, barrio, localidad,
                                                    desc_seguridad (RF-03), es_principal

productos.Producto  [ManyToMany→ Categoria]
carrito.Carrito     [OneToOne→ Usuario]
    └── ItemCarrito [FK→ Producto]
```

---

## 7. 🗃️ Esquema Relacional Completo (Diseño Final Planificado)

```
Cliente (id [PK], usuario_id [FK→Usuario, nullable], nombre, apellido, ...)
    ├── TelefonoContacto (id, cliente [FK], numero, desc_relacion, es_principal)
    ├── DireccionEntrega (id, cliente [FK], calle, desc_seguridad, coordenadas, id_zona [FK])
    ├── Pedido (id_pedido [PK], estado, total, fecha, cliente [FK])
    │       ├── Producto_incluye_pedido
    │       ├── Pago_pedido → Metodo_pago
    │       ├── Detalle_hoja_ruta → Hoja_ruta
    │       └── Incluye_promo → Promociones
    ├── Cliente_alquila_producto → Producto
    └── Saldo_disp_promocion

Producto (id_producto [PK], nombre, precio, costo_alquiler, capacidad, id_categoria [FK])
    └── Categoria (id_categoria [PK], nombre)

Hoja_ruta   (id_ruta [PK], fecha, id_empleado [FK], patente [FK→Camion], id_zona [FK→Zona])
Camion      (patente [PK], descripcion)
Zona        (id_zona [PK], nombre)
Empleado    (id_empleado [PK], dni, id_rol [FK→Rol_empleado])
```

---

## 8. 🗺️ Mapa de URLs Actual

```
/                              → inicio
/admin/                        → Django Admin

/productos/                    → listar_productos  (paginado + filtro categoría)
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
/clientes/<pk>/                → ver_cliente           [🔒 Login]
/clientes/<pk>/editar/         → editar_cliente        [🔒 Admin/Vendedor]
/clientes/<pk>/tipo/           → cambiar_tipo_cliente  [🔒 Admin/Vendedor]
/clientes/<pk>/telefono/nuevo/ → agregar_telefono      [🔒 Admin/Vendedor]
/clientes/telefono/<pk>/eliminar/ → eliminar_telefono  [🔒 Admin/Vendedor]
/clientes/<pk>/direccion/nueva/   → agregar_direccion  [🔒 Admin/Vendedor]
/clientes/direccion/<pk>/editar/  → editar_direccion   [🔒 Admin/Vendedor]
/clientes/direccion/<pk>/eliminar/→ eliminar_direccion [🔒 Admin/Vendedor]
/clientes/mi-perfil/           → mi_perfil_cliente     [🔒 Login]
```

---

## 9. 📖 Historias de Usuario

| HU | Como | Quiero | Estado |
|---|---|---|:---:|
| HU-01 | Cliente nuevo | Registrarme con ≥2 teléfonos y relación explícita | ✅ Completa |
| HU-02 | Cliente registrado | Guardar múltiples domicilios con zona y nota de seguridad | ✅ Completa |
| HU-03 | Visitante | Buscar sin tildes ni mayúsculas | ✅ Completa |
| HU-04 | Usuario no logueado | Al intentar agregar al carrito → redirige a login con alerta | ✅ Completa |
| HU-05 | Vendedor | Registrar pagos parciales → auto-actualiza estado pedido | 🔲 Pendiente |
| HU-06 | Repartidor | Marcar estado de entrega desde la app | 🔲 Pendiente |
| HU-07 | Vendedor | Dar de alta un cliente sin cuenta web para pedidos telefónicos | ✅ Completa |
| HU-08 | Admin | Ver ficha completa de cliente con teléfonos, domicilios y seguridad | ✅ Completa |

---

## 10. 📅 Cronograma Resumido

| Mes | Hito | Estado |
|:---:|---|:---:|
| 1–3 | Relevamiento, análisis, diseño | ✅ Completado |
| 4 | CRUD core de productos | ✅ Completado |
| 5 | Seguridad y roles | ✅ Completado |
| 6 | UX, buscador, carrito | ✅ Completado |
| 7 | Segmentación y gestión de clientes | ✅ Completado |
| 8 | Lógica transaccional (Pedidos, Pagos) | 🔴 Pendiente |
| 9 | Cuentas corrientes, bidones, promociones | 🔴 Pendiente |
| 10 | Logística y hojas de ruta | 🔴 Pendiente |
| 11 | Alertas y semaforización | 🔴 Pendiente |
| 12 | QA, Testing, Memoria de Tesis | 🔴 Pendiente |

---

## 11. ⚠️ Deuda Técnica Crítica

| Problema | Severidad | Solución |
|---|---|---|
| `SECRET_KEY` hardcodeada en `base.py` | 🔴 Alta | Mover a `.env` con `python-decouple` |
| `production.py` vacío | 🔴 Alta | Completar con `ALLOWED_HOSTS`, PostgreSQL, storage |
| Carrito no descuenta stock ni genera Pedido | 🟠 Media | Implementar módulo Pedidos (Mes 8) |
| `celular1/celular2` en `Usuario` son redundantes | 🟡 Baja | Se migran via señal, evaluar deprecación futura |

---

*Contexto actualizado: 29/07/2026 — Versión 3.0*
*Actualizar este archivo ante cualquier cambio estructural significativo.*
