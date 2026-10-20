from datetime import timedelta
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from apps.clientes.models import Cliente
from apps.autenticacion.models import Usuario
from . import services
from .models import CuentaCorriente, MovimientoCuenta


class CuentaCorrienteModelTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre='Juan', apellido='Perez', tipo_cliente='Normal', permite_fiado=True
        )
        self.cuenta = CuentaCorriente.objects.create(cliente=self.cliente)

    def test_saldo_inicia_en_cero(self):
        self.assertEqual(self.cuenta.saldo, Decimal('0.00'))

    def test_cargo_y_pago_actualizan_saldo(self):
        services.registrar_cargo(self.cuenta, Decimal('1500.00'))
        services.registrar_pago(self.cuenta, Decimal('500.00'))
        self.cuenta.refresh_from_db()
        self.assertEqual(self.cuenta.saldo, Decimal('1000.00'))

    def test_monto_invalido_es_rechazado(self):
        with self.assertRaises(ValidationError):
            services.registrar_cargo(self.cuenta, Decimal('0'))
        with self.assertRaises(ValidationError):
            services.registrar_pago(self.cuenta, Decimal('-10'))


class ReglaFiadoTests(TestCase):
    """RF-05: solo los clientes habilitados pueden tener deuda."""

    def test_cargo_rechazado_sin_fiado(self):
        cliente = Cliente.objects.create(nombre='Ana', tipo_cliente='Normal')
        cliente.permite_fiado = False
        cliente.save()
        cuenta = CuentaCorriente.objects.create(cliente=cliente)

        with self.assertRaises(ValidationError):
            services.registrar_cargo(cuenta, Decimal('100.00'))
        self.assertEqual(cuenta.movimientos.count(), 0)

    def test_premium_permite_fiado_automaticamente(self):
        cliente = Cliente.objects.create(nombre='VIP', tipo_cliente='Premium')
        self.assertTrue(cliente.permite_fiado)

    def test_clean_bloquea_cargo_sin_fiado(self):
        cliente = Cliente.objects.create(nombre='Beto', tipo_cliente='Normal')
        cliente.permite_fiado = False
        cliente.save()
        cuenta = CuentaCorriente.objects.create(cliente=cliente)
        mov = MovimientoCuenta(cuenta=cuenta, tipo='Cargo', monto=Decimal('50'))
        with self.assertRaises(ValidationError):
            mov.full_clean(exclude=['fecha'])


class SemaforizacionTests(TestCase):
    """RF-14: 🟡 en plazo, 🟠 a los 10 días, 🔴 a los 15 días."""

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre='Mora', tipo_cliente='Normal', permite_fiado=True
        )
        self.cuenta = CuentaCorriente.objects.create(cliente=self.cliente)

    def _cargo_con_antiguedad(self, dias):
        mov = services.registrar_cargo(self.cuenta, Decimal('1000.00'))
        MovimientoCuenta.objects.filter(pk=mov.pk).update(
            fecha=timezone.now() - timedelta(days=dias)
        )
        self.cuenta.refresh_from_db()
        return self.cuenta

    def test_al_dia_sin_deuda(self):
        self.assertEqual(self.cuenta.nivel_morosidad(), 'al-dia')

    def test_amarillo_en_plazo(self):
        self._cargo_con_antiguedad(0)
        self.assertEqual(self.cuenta.nivel_morosidad(), 'amarillo')

    def test_naranja_a_los_10_dias(self):
        self._cargo_con_antiguedad(10)
        self.assertEqual(self.cuenta.nivel_morosidad(), 'naranja')

    def test_rojo_a_los_15_dias(self):
        self._cargo_con_antiguedad(15)
        self.assertEqual(self.cuenta.nivel_morosidad(), 'rojo')

    def test_pago_total_vuelve_a_al_dia(self):
        self._cargo_con_antiguedad(15)
        services.registrar_pago(self.cuenta, Decimal('1000.00'))
        self.cuenta.refresh_from_db()
        self.assertEqual(self.cuenta.nivel_morosidad(), 'al-dia')

    def test_clientes_morosos_ordenados_por_atraso(self):
        otro = Cliente.objects.create(nombre='Otro', tipo_cliente='Normal', permite_fiado=True)
        cuenta_otro = CuentaCorriente.objects.create(cliente=otro)
        # Cuenta propia: 15 días; la otra: 10 días.
        self._cargo_con_antiguedad(15)
        mov = services.registrar_cargo(cuenta_otro, Decimal('500.00'))
        MovimientoCuenta.objects.filter(pk=mov.pk).update(
            fecha=timezone.now() - timedelta(days=10)
        )

        morosos = services.clientes_morosos()
        self.assertEqual(morosos[0].cliente, self.cliente)
        self.assertIn(cuenta_otro, morosos)

    def test_resumen_morosidad(self):
        self._cargo_con_antiguedad(15)
        resumen = services.resumen_morosidad()
        self.assertEqual(resumen['rojo'], 1)
        self.assertEqual(resumen['total_deuda'], Decimal('1000.00'))


class VistasCuentasTests(TestCase):
    def setUp(self):
        self.admin = Usuario.objects.create_superuser('admin_c', 'admin_c@test.com', 'clave12345')
        self.client.force_login(self.admin)
        self.cliente = Cliente.objects.create(nombre='Juan', apellido='Perez', tipo_cliente='Normal', permite_fiado=True)
        self.cuenta = services.obtener_o_crear_cuenta(self.cliente)

    def test_listar_cuentas(self):
        self.assertEqual(self.client.get('/cuentas/').status_code, 200)

    def test_ver_cuenta(self):
        self.assertEqual(self.client.get(f'/cuentas/{self.cuenta.pk}/').status_code, 200)

    def test_cuenta_de_cliente_crea_y_redirige(self):
        resp = self.client.get(f'/cuentas/cliente/{self.cliente.pk}/')
        self.assertEqual(resp.status_code, 302)

    def test_registrar_cargo_post(self):
        resp = self.client.post(f'/cuentas/{self.cuenta.pk}/cargo/', {'monto': '1000'})
        self.assertEqual(resp.status_code, 302)
        self.cuenta.refresh_from_db()
        self.assertEqual(self.cuenta.saldo, Decimal('1000.00'))
