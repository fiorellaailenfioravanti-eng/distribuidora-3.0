from datetime import date
from decimal import Decimal

from django.test import TestCase

from apps.clientes.models import Cliente
from apps.productos.models import Producto
from . import services
from .models import Abono, DESCUENTO_PREMIUM


class CostoPreferencialTests(TestCase):
    """RF-05: los clientes Premium acceden a un costo mensual preferencial."""

    def setUp(self):
        self.producto = Producto.objects.create(
            nombre='Dispenser frío/calor', descripcion='Equipo', precio=Decimal('0'),
            stock=10,
        )

    def test_cliente_normal_paga_precio_de_lista(self):
        cliente = Cliente.objects.create(nombre='Normal', tipo_cliente='Normal')
        abono = Abono.objects.create(
            cliente=cliente, producto=self.producto, fecha_inicio=date(2026, 1, 1),
            costo_mensual=Decimal('1000.00'),
        )
        self.assertEqual(abono.costo_para_cliente(), Decimal('1000.00'))

    def test_cliente_premium_obtiene_descuento(self):
        cliente = Cliente.objects.create(nombre='VIP', tipo_cliente='Premium')
        abono = Abono.objects.create(
            cliente=cliente, producto=self.producto, fecha_inicio=date(2026, 1, 1),
            costo_mensual=Decimal('1000.00'),
        )
        esperado = (Decimal('1000.00') * (Decimal('1') - DESCUENTO_PREMIUM)).quantize(Decimal('0.01'))
        self.assertEqual(abono.costo_para_cliente(), esperado)


class FacturacionTests(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre='Dispenser', descripcion='Equipo', precio=Decimal('0'), stock=5,
        )
        self.cliente = Cliente.objects.create(
            nombre='Fiado', apellido='Ok', tipo_cliente='Normal', permite_fiado=True,
        )
        self.abono = Abono.objects.create(
            cliente=self.cliente, producto=self.producto,
            fecha_inicio=date(2026, 3, 1), costo_mensual=Decimal('2000.00'),
            dia_facturacion=1, estado='Activo',
        )

    def test_genera_cargo_en_cuenta(self):
        generados, omitidos = services.generar_cargos_mensuales(anio=2026, mes=3)
        self.assertEqual(len(generados), 1)
        self.assertEqual(omitidos, [])

        cuenta = self.cliente.cuenta_corriente
        self.assertEqual(cuenta.movimientos.filter(tipo='Cargo').count(), 1)
        self.assertEqual(cuenta.saldo, Decimal('2000.00'))

        self.abono.refresh_from_db()
        self.assertEqual(self.abono.ultima_facturacion, date(2026, 3, 1))

    def test_no_factura_dos_veces_el_mismo_mes(self):
        services.generar_cargos_mensuales(anio=2026, mes=3)
        generados, _ = services.generar_cargos_mensuales(anio=2026, mes=3)
        self.assertEqual(generados, [])

    def test_omite_cliente_sin_fiado(self):
        cliente = Cliente.objects.create(nombre='SinFiado', tipo_cliente='Normal')
        cliente.permite_fiado = False
        cliente.save()
        Abono.objects.create(
            cliente=cliente, producto=self.producto,
            fecha_inicio=date(2026, 3, 1), costo_mensual=Decimal('1500.00'),
            dia_facturacion=1, estado='Activo',
        )
        generados, omitidos = services.generar_cargos_mensuales(anio=2026, mes=3)
        self.assertEqual(len(generados), 1)
        self.assertEqual(len(omitidos), 1)
        self.assertEqual(omitidos[0].cliente, cliente)

    def test_abono_suspendido_no_factura(self):
        self.abono.estado = 'Suspendido'
        self.abono.save(update_fields=['estado'])
        generados, _ = services.generar_cargos_mensuales(anio=2026, mes=3)
        self.assertEqual(generados, [])


class VistasAbonosTests(TestCase):
    def setUp(self):
        from apps.autenticacion.models import Usuario
        self.admin = Usuario.objects.create_superuser('admin_a', 'admin_a@test.com', 'clave12345')
        self.client.force_login(self.admin)
        self.producto = Producto.objects.create(nombre='Dispenser', descripcion='x', precio=Decimal('0'), stock=3)
        self.cliente = Cliente.objects.create(nombre='Cli', apellido='Abonado', tipo_cliente='Normal', permite_fiado=True)
        self.abono = Abono.objects.create(cliente=self.cliente, producto=self.producto, fecha_inicio=date(2026, 3, 1), costo_mensual=Decimal('1000'))

    def test_listar_abonos(self):
        self.assertEqual(self.client.get('/abonos/').status_code, 200)

    def test_ver_abono(self):
        self.assertEqual(self.client.get(f'/abonos/{self.abono.pk}/').status_code, 200)

    def test_form_crear(self):
        self.assertEqual(self.client.get('/abonos/nuevo/').status_code, 200)

    def test_generar_cargos_post(self):
        from apps.abonos.services import generar_cargos_mensuales
        resp = self.client.post('/abonos/generar-cargos/')
        self.assertEqual(resp.status_code, 302)
