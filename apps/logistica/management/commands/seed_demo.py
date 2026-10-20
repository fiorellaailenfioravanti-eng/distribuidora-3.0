"""
Puebla la base con datos de demostración realistas de Aquadelluvia (Resistencia, Chaco).

    python manage.py seed_demo --settings=distribuidora.settings.local

Qué carga (todo con valores fijos, sin aleatoriedad):
- Catálogo: bidones, agua, soda, dispensers, accesorios y el envase retornable.
- 4 zonas con días de reparto, barrios asignados, 2 camiones y rutas por día.
- Personal: roles con su grupo de permisos y empleados con usuario.
- 16 clientes (Premium/Normal, con y sin cuenta web, frecuentes), cada uno con
  2 teléfonos y su dirección con nota de seguridad y coordenadas.
- Historial de las últimas 3 semanas generado con los servicios del sistema:
  hojas de ruta confirmadas, entregas, cobros, envases (RF-08) y regreso del
  camión; pedidos pendientes para los próximos días; cuentas corrientes con
  deudas en los tres colores del semáforo (RF-14); abonos de dispensers con su
  cargo mensual (RF-15); un feriado en el calendario.

Es idempotente: el catálogo, el personal y los clientes se buscan antes de
crearse, y el historial sólo se genera si todavía no existe (marca: el pedido
con la nota «[demo]»). Las fechas se calculan desde el día en que se corre.

Usuarios de prueba (sólo desarrollo local), todos con la contraseña
`Demo-Aquadelluvia-2026`:
  admin.demo (superusuario) · vendedor.demo · repartidor.norte · repartidor.sur
  · cliente: marta.gimenez, jorge.benitez, lucia.romero
"""
from datetime import datetime, time, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.clientes.models import Cliente, DireccionEntrega, MovimientoBidon, TelefonoContacto
from apps.clientes.services import registrar_movimiento_bidon
from apps.cuentas.models import MovimientoCuenta
from apps.cuentas.services import obtener_o_crear_cuenta, registrar_cargo, registrar_pago
from apps.abonos.models import Abono
from apps.abonos.services import generar_cargos_mensuales
from apps.empleados.models import Empleado, RolEmpleado
from apps.logistica.models import (
    Barrio, CalendarioExcepcion, Camion, HojaRuta, RutaReparto, Zona,
)
from apps.logistica.services import (
    carga_sugerida, confirmar_hoja, crear_hoja_borrador, generar_borradores_periodo,
    registrar_entrega, registrar_regreso,
)
from apps.pedidos.models import DetallePedido, MetodoPago, PagoPedido, Pedido
from apps.pedidos.services import registrar_cobro
from apps.productos.models import Categoria, Producto

CLAVE_DEMO = 'Demo-Aquadelluvia-2026'
MARCA_HISTORIAL = '[demo]'

CATEGORIAS = {
    'Agua en bidones': 'Bidones retornables de agua de mesa para dispenser.',
    'Agua y soda': 'Botellas y sifones para el consumo diario.',
    'Dispensers y accesorios': 'Equipos en venta o alquiler y sus repuestos.',
    'Envases': 'Envases retornables que se prestan con cada entrega.',
}

# nombre, categoría, descripción, precio, stock, retornable, es_envase
PRODUCTOS = [
    ('Envase bidón 20 L', 'Envases', 'Bidón retornable de policarbonato, sin contenido.', '9500', 180, True, True),
    ('Bidón 20 L agua de mesa', 'Agua en bidones', 'Agua de mesa purificada por ósmosis inversa en bidón retornable de 20 litros.', '3200', 240, True, False),
    ('Bidón 12 L agua de mesa', 'Agua en bidones', 'Bidón retornable de 12 litros, ideal para departamentos.', '2300', 90, True, False),
    ('Bidón 20 L agua mineralizada', 'Agua en bidones', 'Agua con sales minerales agregadas, bidón retornable de 20 litros.', '3700', 60, True, False),
    ('Pack agua sin gas 2 L x 6', 'Agua y soda', 'Seis botellas descartables de 2 litros de agua de mesa sin gas.', '4800', 75, False, False),
    ('Sifón de soda 1,5 L', 'Agua y soda', 'Soda en sifón plástico retornable de 1,5 litros.', '950', 160, True, False),
    ('Dispenser frío/calor de pie', 'Dispensers y accesorios', 'Dispenser eléctrico de pie con agua fría y caliente. Disponible en alquiler.', '185000', 12, False, False),
    ('Dispenser de mesada natural', 'Dispensers y accesorios', 'Dispenser de mesada sin electricidad, canilla a temperatura ambiente.', '38000', 15, False, False),
    ('Bomba manual para bidón', 'Dispensers y accesorios', 'Bomba a presión para servir agua directamente del bidón.', '7500', 30, False, False),
    ('Vasos descartables x 100', 'Dispensers y accesorios', 'Vasos plásticos de 180 cc para dispenser.', '2600', 50, False, False),
]

# zona: (descripción, días de reparto 0=lunes, barrios)
ZONAS = {
    'Centro': ('Microcentro y barrios lindantes a la plaza 25 de Mayo.', [0, 3],
               ['VILLA SAN MARTIN', 'BELGRANO', 'VILLA DEL PARQUE']),
    'Norte': ('Barrios al norte de Av. 25 de Mayo.', [1, 4],
              ['VILLA GHIO', 'VILLA LUISA', 'VILLA ALTA']),
    'Sur': ('Barrios al sur de Av. 9 de Julio, hasta el Río Arazá.', [2, 5],
            ['VILLA RIO ARAZA', 'SANTA INES', 'PROVINCIAS UNIDAS']),
    'Oeste': ('Barrios al oeste de Av. Sarmiento.', [0, 3],
              ['VILLA PROGRESO', 'SAN CAYETANO', 'VILLA DON ENRIQUE']),
}

# patente, descripción, capacidad
CAMIONES = [
    ('AD123CD', 'Iveco Daily 35S14 — caja cerrada', 120),
    ('AE456FG', 'Mercedes-Benz Sprinter 415 — utilitario', 80),
]

# username, nombre, apellido, dni, celular, rol, zona asignada (repartidores)
PERSONAL = [
    ('vendedor.demo', 'Carolina', 'Sosa', '29874512', '3624501122', 'Vendedor', None),
    ('repartidor.norte', 'Ramón', 'Acosta', '31258963', '3624557788', 'Repartidor', 'Norte'),
    ('repartidor.sur', 'Héctor', 'Leiva', '33698741', '3624663344', 'Repartidor', 'Sur'),
]

# usuario web (o None), nombre, apellido, dni, tipo, frecuente, bidones habituales,
# zona, barrio, calle, altura, piso, nota de seguridad, coordenadas, teléfonos [(número, relación)]
CLIENTES = [
    ('marta.gimenez', 'Marta', 'Giménez', '27111001', 'Premium', True, 2, 'Centro', 'VILLA SAN MARTIN',
     'Av. Sarmiento', '845', '', 'Portón negro con candado; el perro es manso.', '-27.4512,-58.9856',
     [('3624400101', 'Titular'), ('3624400102', 'Esposo')]),
    ('jorge.benitez', 'Jorge', 'Benítez', '25111002', 'Normal', True, 1, 'Norte', 'VILLA GHIO',
     'Juan B. Justo', '1320', '', 'Tocar timbre 2 veces; si no atiende, dejar en la galería.', '-27.4380,-58.9902',
     [('3624400201', 'Titular'), ('3624400202', 'Hija')]),
    ('lucia.romero', 'Lucía', 'Romero', '34111003', 'Normal', False, 0, 'Sur', 'SANTA INES',
     'Av. Avalos', '2210', 'Dpto. 3B', 'Edificio con portero eléctrico, pedir por 3B.', '-27.4721,-58.9790',
     [('3624400301', 'Titular'), ('3624400302', 'Madre')]),
    (None, 'Hugo', 'Fernández', '20111004', 'Premium', True, 3, 'Centro', 'BELGRANO',
     'Pellegrini', '560', '', 'Comercio: entregar por la puerta lateral, de 8 a 12.', '-27.4549,-58.9875',
     [('3624400401', 'Titular'), ('3624400402', 'Encargado del local')]),
    (None, 'Silvia', 'Duarte', '23111005', 'Normal', True, 2, 'Oeste', 'VILLA PROGRESO',
     'Av. Alvear', '3150', '', 'Casa con rejas verdes; avisar por WhatsApp al llegar.', '-27.4602,-59.0105',
     [('3624400501', 'Titular'), ('3624400502', 'Vecina (deja llave)')]),
    (None, 'Oficina', 'Estudio Contable Ríos', '30711006', 'Premium', True, 4, 'Centro', 'VILLA DEL PARQUE',
     'Güemes', '190', 'Piso 2 Of. 4', 'Subir por escalera; ascensor fuera de servicio los sábados.', '-27.4530,-58.9841',
     [('3624400601', 'Recepción'), ('3624400602', 'Administración')]),
    (None, 'Ramiro', 'Ojeda', '28111007', 'Normal', False, 0, 'Norte', 'VILLA LUISA',
     'Av. Italia', '1478', '', 'Perros sueltos: esperar en la vereda y llamar.', '-27.4335,-58.9870',
     [('3624400701', 'Titular'), ('3624400702', 'Esposa')]),
    (None, 'Graciela', 'Medina', '17111008', 'Premium', True, 2, 'Sur', 'VILLA RIO ARAZA',
     'Ruta 11', 'km 1004', '', 'Entrada de ripio, el camión entra hasta la tranquera.', '-27.4870,-58.9712',
     [('3624400801', 'Titular'), ('3624400802', 'Hijo')]),
    (None, 'Diego', 'Cabrera', '32111009', 'Normal', True, 1, 'Oeste', 'SAN CAYETANO',
     'Calle 15', '742', '', '', '-27.4655,-59.0220',
     [('3624400901', 'Titular'), ('3624400902', 'Trabajo')]),
    (None, 'Gimnasio', 'Fuerza Chaco', '30711010', 'Premium', True, 6, 'Norte', 'VILLA ALTA',
     'Av. Castelli', '980', '', 'Entregar en recepción, horario 7 a 22.', '-27.4401,-58.9799',
     [('3624401001', 'Recepción'), ('3624401002', 'Dueño')]),
    (None, 'Norma', 'Aguirre', '14111011', 'Normal', False, 0, 'Sur', 'PROVINCIAS UNIDAS',
     'Av. Soberanía Nacional', '4120', '', 'Señora mayor, tocar fuerte y esperar.', '-27.4801,-58.9640',
     [('3624401101', 'Titular'), ('3624401102', 'Hija (Corrientes)')]),
    (None, 'Pablo', 'Villalba', '35111012', 'Normal', True, 2, 'Centro', 'VILLA SAN MARTIN',
     'Mitre', '1012', 'PB', '', '-27.4499,-58.9881',
     [('3624401201', 'Titular'), ('3624401202', 'Hermano')]),
    (None, 'Escuela', 'N° 1234 Sarmiento', '30711013', 'Premium', True, 8, 'Oeste', 'VILLA DON ENRIQUE',
     'Av. Wilde', '2600', '', 'Ingreso por portería; firmar remito con dirección.', '-27.4588,-59.0181',
     [('3624401301', 'Dirección'), ('3624401302', 'Portería')]),
    (None, 'Andrea', 'Quiroga', '31111014', 'Normal', False, 0, 'Norte', 'VILLA GHIO',
     'Ameghino', '455', '', '', '-27.4362,-58.9933',
     [('3624401401', 'Titular'), ('3624401402', 'Pareja')]),
    (None, 'Carlos', 'Maidana', '22111015', 'Normal', True, 1, 'Sur', 'SANTA INES',
     'Lavalle', '3301', '', 'Casa al fondo del pasillo, número pintado en la pared.', '-27.4744,-58.9811',
     [('3624401501', 'Titular'), ('3624401502', 'Esposa')]),
    (None, 'Sofía', 'Ledesma', '38111016', 'Normal', False, 0, 'Oeste', 'VILLA PROGRESO',
     'Av. Alvear', '2980', 'Dpto. 1', '', '-27.4597,-59.0090',
     [('3624401601', 'Titular'), ('3624401602', 'Padre')]),
]


def _a_dt(fecha, hora=9, minuto=0):
    return timezone.make_aware(datetime.combine(fecha, time(hora, minuto)))


class Command(BaseCommand):
    help = 'Carga datos de demostración realistas (catálogo, zonas, personal, clientes e historial). Idempotente.'

    def handle(self, *args, **options):
        self.hoy = timezone.localdate()
        call_command('seed_barrios', stdout=self.stdout)
        with transaction.atomic():
            self.metodos = {m.codigo: m for m in MetodoPago.objects.all()}
            self._catalogo()
            self._zonas_y_flota()
            self._personal()
            self._clientes()
            if Pedido.objects.filter(notas_cliente__startswith=MARCA_HISTORIAL).exists():
                self.stdout.write(self.style.WARNING('El historial de demo ya existe: no se vuelve a generar.'))
            else:
                self._historial_reparto()
                self._pedidos_proximos()
                self._cuentas_corrientes()
                self._abonos()
        self._resumen()

    # ── Catálogo ──────────────────────────────────────────────
    def _catalogo(self):
        self.categorias = {
            nombre: Categoria.objects.get_or_create(nombre=nombre, defaults={'descripcion': desc})[0]
            for nombre, desc in CATEGORIAS.items()
        }
        self.productos = {}
        for nombre, cat, desc, precio, stock, retornable, es_envase in PRODUCTOS:
            producto, _ = Producto.objects.get_or_create(nombre=nombre, defaults={
                'descripcion': desc, 'precio': Decimal(precio), 'stock': stock,
                'es_retornable': retornable, 'es_envase': es_envase,
            })
            producto.categoria.add(self.categorias[cat])
            self.productos[nombre] = producto
        envase = self.productos['Envase bidón 20 L']
        for nombre in ('Bidón 20 L agua de mesa', 'Bidón 20 L agua mineralizada', 'Bidón 12 L agua de mesa'):
            Producto.objects.filter(pk=self.productos[nombre].pk, envase__isnull=True).update(envase=envase)

    # ── Zonas, barrios, camiones, rutas y calendario ──────────
    def _zonas_y_flota(self):
        self.zonas = {}
        self.barrios = {}
        for nombre, (desc, dias, barrios) in ZONAS.items():
            zona, creada = Zona.objects.get_or_create(nombre=nombre, defaults={'descripcion': desc})
            if creada or not zona.get_dias_reparto():
                zona.set_dias_reparto(dias)
                zona.save(update_fields=['dias_reparto'])
            self.zonas[nombre] = zona
            for nombre_barrio in barrios:
                barrio, _ = Barrio.objects.get_or_create(
                    nombre=nombre_barrio, ciudad='Resistencia', defaults={'zona': zona})
                # Sólo se reasignan barrios que estaban en la zona genérica.
                if barrio.zona_id is None or barrio.zona.nombre == 'Sin Asignar':
                    barrio.zona = zona
                    barrio.save(update_fields=['zona'])
                self.barrios[nombre_barrio] = barrio

        self.camiones = [
            Camion.objects.get_or_create(patente=patente, defaults={
                'descripcion': desc, 'capacidad_botellones': capacidad, 'activo': True})[0]
            for patente, desc, capacidad in CAMIONES
        ]

        # Feriado nacional: 8 de diciembre (Inmaculada Concepción), sin reparto.
        anio = self.hoy.year if self.hoy <= self.hoy.replace(month=12, day=8) else self.hoy.year + 1
        CalendarioExcepcion.objects.get_or_create(
            fecha=self.hoy.replace(year=anio, month=12, day=8), zona=None, tipo='suspende',
            defaults={'motivo': 'Feriado nacional — Inmaculada Concepción'},
        )

    # ── Personal ──────────────────────────────────────────────
    def _usuario_interno(self, username, nombre, apellido, **extra):
        """Usuario del personal: se marca antes de guardar para que la señal
        de `apps.clientes` no le cree un perfil de cliente."""
        Usuario = get_user_model()
        usuario = Usuario.objects.filter(username=username).first()
        if usuario is None:
            usuario = Usuario(username=username, email=f'{username}@aquadelluvia.local',
                              first_name=nombre, last_name=apellido, **extra)
            usuario.set_password(CLAVE_DEMO)
            usuario._es_empleado = True
            usuario.save()
        return usuario

    def _personal(self):
        self.admin = self._usuario_interno('admin.demo', 'Admin', 'Aquadelluvia', is_staff=True, is_superuser=True)

        roles = {
            'Vendedor': RolEmpleado.objects.get_or_create(
                nombre='Vendedor', defaults={'descripcion': 'Atención al cliente, ventas y planificación.',
                                             'grupo_permisos': 'Vendedor'})[0],
            'Repartidor': RolEmpleado.objects.get_or_create(
                nombre='Repartidor', defaults={'descripcion': 'Reparto y cobro en calle.',
                                               'grupo_permisos': 'Repartidor'})[0],
        }
        for rol, grupo in (('Vendedor', 'Vendedor'), ('Repartidor', 'Repartidor')):
            if roles[rol].grupo_permisos != grupo:
                roles[rol].grupo_permisos = grupo
                roles[rol].save(update_fields=['grupo_permisos'])

        self.repartidores = {}
        for username, nombre, apellido, dni, celular, rol, zona in PERSONAL:
            usuario = self._usuario_interno(username, nombre, apellido)
            empleado = Empleado.objects.filter(dni=dni).first() or Empleado.objects.filter(usuario=usuario).first()
            if empleado is None:
                empleado = Empleado.objects.create(
                    usuario=usuario, nombre=nombre, apellido=apellido, dni=dni, celular=celular,
                    email=usuario.email, rol=roles[rol], activo=True)
            if zona:
                self.repartidores[zona] = empleado
        # Centro y Oeste los cubre el repartidor de Norte y Sur respectivamente.
        self.repartidores.setdefault('Centro', self.repartidores.get('Norte'))
        self.repartidores.setdefault('Oeste', self.repartidores.get('Sur'))

        for nombre, zona in self.zonas.items():
            camion = self.camiones[0] if nombre in ('Centro', 'Norte') else self.camiones[1]
            for dia in zona.get_dias_reparto():
                RutaReparto.objects.get_or_create(
                    zona=zona, dia_semana=dia,
                    defaults={'nombre': f'Ruta {nombre}', 'empleado_default': self.repartidores.get(nombre),
                              'camion_default': camion})

    # ── Clientes ──────────────────────────────────────────────
    def _clientes(self):
        Usuario = get_user_model()
        self.clientes = []
        for (usuario_web, nombre, apellido, dni, tipo, frecuente, habituales, zona, barrio,
             calle, altura, piso, nota, coords, telefonos) in CLIENTES:
            cliente = Cliente.objects.filter(dni=dni).first()
            if cliente is None:
                usuario = None
                if usuario_web:
                    usuario = Usuario.objects.filter(username=usuario_web).first()
                    if usuario is None:
                        usuario = Usuario(username=usuario_web, email=f'{usuario_web}@correo.demo',
                                          first_name=nombre, last_name=apellido)
                        usuario.set_password(CLAVE_DEMO)
                        usuario.save()  # la señal crea el perfil de cliente
                    cliente = usuario.perfil_cliente
                else:
                    cliente = Cliente(nombre=nombre, apellido=apellido)
                cliente.nombre, cliente.apellido, cliente.dni = nombre, apellido, dni
                cliente.tipo_cliente = tipo
                cliente.es_frecuente = frecuente
                cliente.cantidad_recurrente_default = habituales
                cliente.save()
                cliente.telefonos.all().delete()
                for i, (numero, relacion) in enumerate(telefonos):
                    TelefonoContacto.objects.create(cliente=cliente, numero=numero,
                                                    desc_relacion=relacion, es_principal=(i == 0))
                DireccionEntrega.objects.create(
                    cliente=cliente, calle=calle, altura=altura, piso_depto=piso,
                    barrio=self.barrios[barrio], ciudad='Resistencia', desc_seguridad=nota,
                    coordenadas=coords, es_principal=True)
            self.clientes.append(cliente)
        # Segundo domicilio (RF-03): el estudio contable también recibe en la casa del titular.
        estudio = self.clientes[5]
        if estudio.direcciones.count() == 1:
            DireccionEntrega.objects.create(
                cliente=estudio, calle='French', altura='1520', barrio=self.barrios['BELGRANO'],
                ciudad='Resistencia', desc_seguridad='Casa particular del contador; sólo sábados.',
                coordenadas='-27.4561,-58.9902')
        # Excepción de fiado autorizada para un cliente Normal (A-D6).
        jorge = self.clientes[1]
        if not jorge.permite_fiado:
            jorge.permite_fiado = True
            jorge.notas_internas = 'Fiado autorizado por la gerencia: cliente desde 2019, paga a fin de mes.'
            jorge.save()

    # ── Pedidos ───────────────────────────────────────────────
    def _crear_pedido(self, cliente, items, fecha_pedido, metodo='EFECTIVO', estado='Confirmado',
                      origen='WEB', nota=''):
        direccion = cliente.direcciones.filter(es_principal=True).first() or cliente.direcciones.first()
        total = sum(self.productos[n].precio * c for n, c in items)
        pedido = Pedido.objects.create(
            cliente=cliente, direccion_entrega=direccion, metodo_pago=self.metodos[metodo],
            total=total, estado=estado, origen=origen, fecha_estimada_entrega=fecha_pedido + timedelta(days=1),
            notas_cliente=f'{MARCA_HISTORIAL} {nota}'.strip())
        for nombre, cantidad in items:
            producto = self.productos[nombre]
            DetallePedido.objects.create(pedido=pedido, producto=producto, precio_unitario=producto.precio,
                                         cantidad=cantidad, subtotal=producto.precio * cantidad)
        Pedido.objects.filter(pk=pedido.pk).update(fecha_pedido=_a_dt(fecha_pedido, 10, 30))
        return pedido

    def _items_habituales(self, cliente):
        bidones = max(cliente.cantidad_recurrente_default, 1)
        items = [('Bidón 20 L agua de mesa', bidones)]
        if cliente.dni in ('27111001', '20111004'):
            items.append(('Sifón de soda 1,5 L', 4))
        return items

    def _historial_reparto(self):
        """Tres semanas de reparto: pedidos, hoja confirmada, entregas, cobros y regreso."""
        fechas = [self.hoy - timedelta(days=d) for d in range(21, 0, -1)]
        hojas = 0
        for fecha in fechas:
            for nombre, zona in self.zonas.items():
                if not zona.incluye_dia(fecha.weekday()):
                    continue
                clientes_zona = [c for c in self.clientes
                                 if c.direcciones.filter(barrio__zona=zona).exists()]
                # Los frecuentes piden en cada visita; los demás, una vez por semana.
                del_dia = [c for c in clientes_zona
                           if c.es_frecuente or (fecha.isocalendar()[1] + int(c.dni[-2:])) % 2 == 0]
                if not del_dia:
                    continue
                pedidos = []
                for c in del_dia:
                    metodo = 'MERCADOPAGO' if c.usuario_id and int(c.dni[-1]) % 2 else 'EFECTIVO'
                    pedidos.append(self._crear_pedido(c, self._items_habituales(c), fecha - timedelta(days=1),
                                                      metodo=metodo, origen='WEB' if c.usuario_id else 'ADMIN'))
                hoja = crear_hoja_borrador(fecha, zona, self.admin,
                                           {'pedidos': [{'pedido_id': p.pk} for p in pedidos]})
                cargas = [{'producto_id': x['producto'].pk, 'cantidad': x['cantidad'] + 2}
                          for x in carga_sugerida(hoja)]
                confirmar_hoja(hoja, self.admin, cargas)
                for i, parada in enumerate(hoja.detalles.select_related('pedido__cliente').order_by('orden')):
                    pedido = parada.pedido
                    if (fecha.day + i) % 11 == 0:
                        registrar_entrega(parada, 'Cancelado', nota='No había nadie en el domicilio.')
                        continue
                    retirados = max(parada.cantidad_bidones - (1 if i % 5 == 0 else 0), 0)
                    vendidos = 1 if (fecha.day + i) % 13 == 0 else 0
                    registrar_entrega(parada, 'Entregado', envases_retirados=retirados,
                                      envases_vendidos=vendidos)
                    if pedido.metodo_pago.codigo == 'MERCADOPAGO':
                        PagoPedido.objects.create(pedido=pedido, monto=pedido.total, metodo_pago=pedido.metodo_pago,
                                                  estado_pago='Aprobado', mercadopago_status='approved',
                                                  mercadopago_payment_id=f'DEMO{pedido.pk:06d}')
                    else:
                        registrar_cobro(pedido, pedido.total, self.metodos['EFECTIVO'])
                cargas_regreso = [
                    {'carga_id': carga.pk,
                     'cantidad_entregada': sum(d.cantidad for p in hoja.detalles.filter(estado='Entregado')
                                               for d in p.pedido.detalles.filter(producto=carga.producto))}
                    for carga in hoja.cargas.all()
                ]
                registrar_regreso(hoja, cargas_regreso)
                HojaRuta.objects.filter(pk=hoja.pk).update(
                    fecha_confirmacion=_a_dt(fecha, 7, 30), fecha_salida=_a_dt(fecha, 7, 45),
                    fecha_regreso=_a_dt(fecha, 14, 10))
                MovimientoBidon.objects.filter(parada__hoja_ruta=hoja).update(fecha=_a_dt(fecha, 11))
                hojas += 1
        # Saldo histórico de envases de los clientes antiguos (antes del sistema).
        for cliente in self.clientes:
            if cliente.es_frecuente and not cliente.movimientos_bidon.filter(tipo='Ajuste').exists():
                mov = registrar_movimiento_bidon(cliente, 'Ajuste', cliente.cantidad_recurrente_default,
                                                 usuario=self.admin, nota='Saldo inicial al pasar al sistema',
                                                 permitir_negativo=True)
                MovimientoBidon.objects.filter(pk=mov.pk).update(fecha=_a_dt(self.hoy - timedelta(days=30), 9))
        self.stdout.write(f'  Historial: {hojas} hojas de ruta cerradas.')

    def _pedidos_proximos(self):
        """Pedidos pendientes y confirmados para los próximos días, más un pedido MP sin acreditar."""
        lucia, ramiro, norma, andrea, sofia = (self.clientes[i] for i in (2, 6, 10, 13, 15))
        self._crear_pedido(lucia, [('Bidón 12 L agua de mesa', 2), ('Vasos descartables x 100', 1)],
                           self.hoy, estado='Pendiente', nota='Si no estoy, dejar con el portero.')
        self._crear_pedido(ramiro, [('Bidón 20 L agua de mesa', 2)], self.hoy, estado='Confirmado', origen='ADMIN')
        self._crear_pedido(norma, [('Bidón 20 L agua de mesa', 1), ('Bomba manual para bidón', 1)],
                           self.hoy, estado='Confirmado', origen='ADMIN', nota='Pedido por teléfono.')
        self._crear_pedido(andrea, [('Pack agua sin gas 2 L x 6', 2)], self.hoy, estado='Pendiente')
        mp = self._crear_pedido(self.clientes[0], [('Bidón 20 L agua mineralizada', 2)], self.hoy,
                                metodo='MERCADOPAGO', estado='Pendiente')
        PagoPedido.objects.create(pedido=mp, monto=mp.total, metodo_pago=mp.metodo_pago, estado_pago='Pendiente',
                                  mercadopago_preference_id='DEMO-PREF-0001')
        self._crear_pedido(sofia, [('Dispenser de mesada natural', 1), ('Bidón 20 L agua de mesa', 1)],
                           self.hoy, estado='Confirmado', metodo='TRANSFERENCIA')
        hojas = generar_borradores_periodo(desde=self.hoy + timedelta(days=1), dias=7, usuario=self.admin)
        self.stdout.write(f'  Próximos días: 6 pedidos nuevos y {len(hojas)} borradores de reparto.')

    # ── Cuentas corrientes (RF-14) ────────────────────────────
    def _cuentas_corrientes(self):
        """Deudas con antigüedad distinta para ver los tres colores del semáforo."""
        casos = [  # cliente, monto, días de antigüedad, pago parcial
            (self.clientes[3], '18400', 20, '6000'),   # rojo
            (self.clientes[9], '25600', 12, None),     # naranja
            (self.clientes[5], '12800', 4, None),      # amarillo
            (self.clientes[1], '6400', 6, '3200'),     # Normal con excepción de fiado
        ]
        for cliente, monto, dias, pago in casos:
            cuenta = obtener_o_crear_cuenta(cliente)
            fecha = self.hoy - timedelta(days=dias)
            cargo = registrar_cargo(cuenta, Decimal(monto), descripcion=f'Bidones del {fecha:%d/%m} (fiado)',
                                    fecha_vencimiento=fecha + timedelta(days=10))
            MovimientoCuenta.objects.filter(pk=cargo.pk).update(fecha=_a_dt(fecha, 12))
            if pago:
                mov = registrar_pago(cuenta, Decimal(pago), descripcion='Pago parcial en efectivo')
                MovimientoCuenta.objects.filter(pk=mov.pk).update(fecha=_a_dt(fecha + timedelta(days=2), 17))
            cuenta.recalcular_saldo()

    # ── Abonos de dispensers (RF-15) ──────────────────────────
    def _abonos(self):
        dispenser = self.productos['Dispenser frío/calor de pie']
        contratos = [  # cliente, meses desde el inicio, costo
            (self.clientes[5], 8, '14500'),   # estudio contable (Premium)
            (self.clientes[9], 5, '14500'),   # gimnasio (Premium)
            (self.clientes[12], 14, '14500'),  # escuela (Premium)
            (self.clientes[1], 2, '14500'),   # Normal con excepción de fiado
        ]
        for cliente, meses, costo in contratos:
            inicio = (self.hoy.replace(day=1) - timedelta(days=30 * meses)).replace(day=1)
            Abono.objects.get_or_create(cliente=cliente, producto=dispenser, defaults={
                'fecha_inicio': inicio, 'costo_mensual': Decimal(costo), 'dia_facturacion': 1,
                'estado': 'Activo', 'observaciones': 'Incluye mantenimiento y sanitización trimestral.'})
        generados, omitidos = generar_cargos_mensuales(self.hoy.year, self.hoy.month)
        self.stdout.write(f'  Abonos: {len(generados)} cargos mensuales generados, {len(omitidos)} omitidos.')

    def _resumen(self):
        self.stdout.write(self.style.SUCCESS(
            f'Datos de demo listos: {Producto.objects.count()} productos, {Zona.objects.count()} zonas, '
            f'{Empleado.objects.count()} empleados, {Cliente.objects.count()} clientes, '
            f'{Pedido.objects.count()} pedidos, {HojaRuta.objects.count()} hojas de ruta, '
            f'{MovimientoBidon.objects.count()} movimientos de envases, {Abono.objects.count()} abonos.'
        ))
        self.stdout.write('Usuarios de prueba: ver el docstring de apps/logistica/management/commands/seed_demo.py')
