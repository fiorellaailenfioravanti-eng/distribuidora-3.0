from datetime import timedelta
from decimal import Decimal
from io import StringIO

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.clientes.models import Cliente, DireccionEntrega, TelefonoContacto
from apps.pedidos.models import MetodoPago, Pedido
from apps.productos.models import Producto

from .forms import PromocionForm
from .models import CompraPromocion, Promocion
from .services import (
    consumir_saldo, revertir_consumos, saldo_vigente, vencer_promociones, vender_promocion,
)


class BasePromociones(TestCase):
    def setUp(self):
        self.hoy = timezone.localdate()
        self.bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'), stock=100)
        self.promo = Promocion.objects.create(nombre='Paga 3, lleva 4', producto=self.bidon,
                                              cant_paga=3, cant_lleva=4, precio=Decimal('9000'))
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')

    def _pedido(self):
        return Pedido.objects.create(cliente=self.cliente, metodo_pago=self.efectivo, total=0)


class EscenarioAceptacionTests(BasePromociones):
    """PROCEDURE Fase 5: el pack crea saldo a 30 días, entregas parciales lo
    consumen y al día 31 el comando lo vence."""

    def test_paga_3_lleva_4_con_entregas_parciales(self):
        compra = vender_promocion(self.cliente, self.promo, fecha=self.hoy)
        self.assertEqual(compra.unid_restantes, 4)
        self.assertEqual(compra.fecha_caducidad, self.hoy + timedelta(days=30))
        self.assertTrue(compra.pedido.esta_pagado())  # se cobró el pack

        for cantidad in (1, 2, 1):
            consumir_saldo(self.cliente, self.bidon, cantidad, self._pedido())
        compra.refresh_from_db()
        self.assertEqual((compra.unid_restantes, compra.estado), (0, 'Agotada'))

    def test_al_dia_31_vence(self):
        compra = vender_promocion(self.cliente, self.promo, fecha=self.hoy)
        consumir_saldo(self.cliente, self.bidon, 1, self._pedido())
        self.assertEqual(vencer_promociones(self.hoy + timedelta(days=30)), 0)  # día 30 sigue vigente
        self.assertEqual(vencer_promociones(self.hoy + timedelta(days=31)), 1)
        compra.refresh_from_db()
        self.assertEqual((compra.estado, compra.unid_restantes), ('Vencida', 0))

    def test_saldo_vencido_no_se_usa_aunque_no_corra_el_comando(self):
        vender_promocion(self.cliente, self.promo, fecha=self.hoy - timedelta(days=31))
        self.assertEqual(saldo_vigente(self.cliente, self.bidon), 0)
        self.assertEqual(consumir_saldo(self.cliente, self.bidon, 2, self._pedido()), 0)


class ReglasDeSaldoTests(BasePromociones):
    def test_consume_primero_lo_que_vence_antes(self):
        vieja = vender_promocion(self.cliente, self.promo, fecha=self.hoy - timedelta(days=20))
        nueva = vender_promocion(self.cliente, self.promo, fecha=self.hoy)
        consumir_saldo(self.cliente, self.bidon, 5, self._pedido())
        vieja.refresh_from_db(); nueva.refresh_from_db()
        self.assertEqual((vieja.unid_restantes, nueva.unid_restantes), (0, 3))

    def test_cancelar_devuelve_unidades_pero_no_si_vencio(self):
        compra = vender_promocion(self.cliente, self.promo, fecha=self.hoy)
        pedido = self._pedido()
        consumir_saldo(self.cliente, self.bidon, 3, pedido)
        self.assertEqual(revertir_consumos(pedido), 3)
        compra.refresh_from_db()
        self.assertEqual(compra.unid_restantes, 4)

        otro = self._pedido()
        consumir_saldo(self.cliente, self.bidon, 2, otro)
        self.assertEqual(revertir_consumos(otro, fecha=self.hoy + timedelta(days=31)), 0)  # F-D5

    def test_cancelar_el_pedido_a_mano_reintegra(self):
        compra = vender_promocion(self.cliente, self.promo, fecha=self.hoy)
        pedido = Pedido.objects.create(cliente=self.cliente, metodo_pago=self.efectivo, total=0, estado='Pendiente')
        consumir_saldo(self.cliente, self.bidon, 2, pedido)
        pedido.cambiar_estado_manual('Cancelado')
        compra.refresh_from_db()
        self.assertEqual(compra.unid_restantes, 4)

    def test_a_cuenta_respeta_el_fiado(self):
        with self.assertRaises(ValidationError):
            vender_promocion(self.cliente, self.promo, a_cuenta=True)
        premium = Cliente.objects.create(nombre='Pre', apellido='Mium', tipo_cliente='Premium')
        compra = vender_promocion(premium, self.promo, a_cuenta=True)
        self.assertEqual(premium.cuenta_corriente.saldo, Decimal('9000'))
        self.assertFalse(compra.pedido.esta_pagado())

    def test_otro_producto_no_usa_el_saldo(self):
        """F-D6: la promoción va atada a su producto."""
        vender_promocion(self.cliente, self.promo)
        soda = Producto.objects.create(nombre='Soda', descripcion='', precio=Decimal('900'), stock=10)
        self.assertEqual(consumir_saldo(self.cliente, soda, 2, self._pedido()), 0)

    def test_formulario_valida_y_calcula_precio(self):
        invalido = PromocionForm(data={'nombre': 'Mal', 'producto': self.bidon.pk, 'cant_paga': 4,
                                       'cant_lleva': 4, 'dias_validez': 30, 'activa': True})
        self.assertFalse(invalido.is_valid())
        valido = PromocionForm(data={'nombre': 'Paga 5 lleva 6', 'producto': self.bidon.pk, 'cant_paga': 5,
                                     'cant_lleva': 6, 'dias_validez': 30, 'activa': True})
        self.assertTrue(valido.is_valid(), valido.errors)
        self.assertEqual(valido.save().precio, Decimal('15000'))

    def test_comando_vencer_promociones(self):
        vender_promocion(self.cliente, self.promo, fecha=self.hoy - timedelta(days=40))
        salida = StringIO()
        call_command('vencer_promociones', stdout=salida)
        self.assertIn('1 compras de promoción vencidas', salida.getvalue())


class CheckoutConSaldoTests(BasePromociones):
    """5B.6: el checkout web descuenta las unidades prepagas."""

    def setUp(self):
        super().setUp()
        from apps.carrito.models import Carrito
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        self.direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='1')
        for numero, relacion in (('3624111111', 'Titular'), ('3624222222', 'Esposo')):
            TelefonoContacto.objects.create(cliente=self.cliente, numero=numero, desc_relacion=relacion)
        self.carrito = Carrito.objects.create(usuario=self.usuario)
        self.client.force_login(self.usuario)

    def _comprar(self, cantidad):
        self.carrito.items.all().delete()
        self.carrito.items.create(producto=self.bidon, cantidad=cantidad)
        self.client.post(reverse('apps.pedidos:confirmar_pedido'), {
            'direccion_entrega': self.direccion.pk, 'metodo_pago': self.efectivo.pk})
        return Pedido.objects.filter(cliente=self.cliente, origen='WEB').latest('id_pedido')

    def test_parte_cubierta_y_parte_cobrada(self):
        compra = vender_promocion(self.cliente, self.promo)
        consumir_saldo(self.cliente, self.bidon, 2, self._pedido())  # quedan 2
        pedido = self._comprar(3)
        renglones = sorted(pedido.detalles.values_list('cantidad', 'precio_unitario'))
        self.assertEqual(renglones, [(1, Decimal('3000')), (2, Decimal('0'))])
        self.assertEqual(pedido.total, Decimal('3000'))
        compra.refresh_from_db()
        self.assertEqual(compra.unid_restantes, 0)

    def test_pedido_cubierto_por_completo_queda_confirmado(self):
        vender_promocion(self.cliente, self.promo)
        pedido = self._comprar(2)
        self.assertEqual((pedido.total, pedido.estado), (Decimal('0'), 'Confirmado'))
        self.assertTrue(pedido.esta_pagado())


class VistasPromocionesTests(BasePromociones):
    def setUp(self):
        super().setUp()
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.cliente_web = Usuario.objects.create_user('cli', 'c@x.com', 'Agua-Lluvia-2026')

    def test_vendedor_vende_desde_la_ficha(self):
        self.client.force_login(self.vendedor)
        self.client.post(reverse('apps.promociones:vender_promocion', args=[self.cliente.pk]),
                         {'promocion': self.promo.pk, 'metodo_pago': self.efectivo.pk})
        self.assertEqual(CompraPromocion.objects.filter(cliente=self.cliente).count(), 1)
        for nombre, args in (('listar_promociones', []), ('crear_promocion', []), ('editar_promocion', [self.promo.pk])):
            self.assertEqual(self.client.get(reverse(f'apps.promociones:{nombre}', args=args)).status_code, 200)
        self.assertContains(self.client.get(reverse('apps.clientes:ver_cliente', args=[self.cliente.pk])), 'Paga 3, lleva 4')

    def test_cliente_no_puede_vender(self):
        self.client.force_login(self.cliente_web)
        self.client.post(reverse('apps.promociones:vender_promocion', args=[self.cliente.pk]),
                         {'promocion': self.promo.pk})
        self.assertFalse(CompraPromocion.objects.exists())
        self.assertEqual(self.client.get(reverse('apps.promociones:listar_promociones')).status_code, 302)
