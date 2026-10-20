from django.test import TestCase

from apps.clientes.models import Cliente, DireccionEntrega
from apps.logistica.models import Barrio, Zona

from .forms import _etiqueta_direccion_con_fecha


class CheckoutFechaEstimadaTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Pérez')

    def test_etiqueta_incluye_fecha_estimada(self):
        zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        barrio = Barrio.objects.create(nombre='Centro', zona=zona)
        direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='Mitre', altura='100', barrio=barrio
        )
        etiqueta = _etiqueta_direccion_con_fecha(direccion)
        self.assertIn('entrega estimada', etiqueta)

    def test_etiqueta_sin_zona_no_agrega_fecha(self):
        barrio = Barrio.objects.create(nombre='Sin Zona')
        direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='Urquiza', altura='200', barrio=barrio
        )
        etiqueta = _etiqueta_direccion_con_fecha(direccion)
        self.assertNotIn('entrega estimada', etiqueta)


# ─────────────────────────────────────────────────────────────
# PAGOS SEGUROS (auditoría H-18…H-21, Fase 4.6.1)
# ─────────────────────────────────────────────────────────────
import hashlib
import hmac
from decimal import Decimal
from unittest import mock

from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import metodos_pago_checkout_web
from .models import MetodoPago, PagoPedido, Pedido
from .services import aplicar_pago_mercadopago, firma_webhook_valida


def _firmar(secreto, data_id, request_id, ts='1700000000'):
    manifiesto = f'id:{data_id};request-id:{request_id};ts:{ts};'
    v1 = hmac.new(secreto.encode(), manifiesto.encode(), hashlib.sha256).hexdigest()
    return f'ts={ts},v1={v1}'


class PagosSegurosTests(TestCase):
    def setUp(self):
        Usuario = get_user_model()
        self.duenio = Usuario.objects.create_user('duenio', 'duenio@x.com', 'clave-segura-123')
        self.otro = Usuario.objects.create_user('otro', 'otro@x.com', 'clave-segura-123')
        self.mp = MetodoPago.objects.get(codigo='MERCADOPAGO')
        self.pedido = Pedido.objects.create(
            cliente=self.duenio.perfil_cliente, metodo_pago=self.mp,
            total=Decimal('1000.00'), estado='Pendiente',
        )
        self.pago = PagoPedido.objects.create(
            pedido=self.pedido, monto=Decimal('1000.00'), metodo_pago=self.mp,
            estado_pago='Pendiente',
        )

    def _recargar(self):
        self.pedido.refresh_from_db()
        self.pago.refresh_from_db()

    # H-18
    def test_callback_exitoso_no_aprueba_pedido_ajeno(self):
        self.client.force_login(self.otro)
        url = reverse('apps.pedidos:pago_exitoso')
        self.client.get(url, {'external_reference': self.pedido.pk, 'status': 'approved'})
        self._recargar()
        self.assertEqual(self.pago.estado_pago, 'Pendiente')
        self.assertEqual(self.pedido.estado, 'Pendiente')

    def test_callback_exitoso_no_confia_en_la_url(self):
        self.client.force_login(self.duenio)
        url = reverse('apps.pedidos:pago_exitoso')
        self.client.get(url, {'external_reference': self.pedido.pk, 'status': 'approved'})
        self._recargar()
        self.assertEqual(self.pago.estado_pago, 'Pendiente')

    # H-19
    def test_confirmar_pago_qr_no_aprueba(self):
        self.client.force_login(self.duenio)
        url = reverse('apps.pedidos:confirmar_pago_qr', args=[self.pedido.pk])
        self.client.get(url)
        self.client.post(url)
        self._recargar()
        self.assertEqual(self.pago.estado_pago, 'Pendiente')
        self.assertEqual(self.pedido.estado, 'Pendiente')

    def test_confirmar_pago_qr_de_otro_usuario_da_404(self):
        self.client.force_login(self.otro)
        url = reverse('apps.pedidos:confirmar_pago_qr', args=[self.pedido.pk])
        self.assertEqual(self.client.post(url).status_code, 404)

    # Control de monto
    def test_aprobado_con_monto_completo_confirma(self):
        aplicar_pago_mercadopago(self.pedido, '99', 'approved', 1000)
        self._recargar()
        self.assertEqual(self.pago.estado_pago, 'Aprobado')
        self.assertEqual(self.pedido.estado, 'Confirmado')

    def test_aprobado_con_monto_menor_queda_pendiente(self):
        aplicar_pago_mercadopago(self.pedido, '99', 'approved', 10)
        self._recargar()
        self.assertEqual(self.pago.estado_pago, 'Pendiente')
        self.assertEqual(self.pedido.estado, 'Pendiente')

    # H-21
    def test_firma_webhook(self):
        firma = _firmar('secreto', '123', 'req-1')
        self.assertTrue(firma_webhook_valida('secreto', firma, 'req-1', '123'))
        self.assertFalse(firma_webhook_valida('secreto', firma, 'req-1', '124'))
        self.assertFalse(firma_webhook_valida('secreto', '', 'req-1', '123'))
        self.assertFalse(firma_webhook_valida('otro', firma, 'req-1', '123'))

    @mock.patch('apps.pedidos.views.MERCADOPAGO_ACCESS_TOKEN', 'TEST-token')
    @mock.patch('apps.pedidos.views.MERCADOPAGO_WEBHOOK_SECRET', 'secreto')
    def test_webhook_con_firma_invalida_responde_403(self):
        url = reverse('apps.pedidos:webhook_mercadopago') + '?type=payment&data.id=555'
        respuesta = self.client.post(url, HTTP_X_SIGNATURE='ts=1,v1=malo', HTTP_X_REQUEST_ID='r')
        self.assertEqual(respuesta.status_code, 403)
        self._recargar()
        self.assertEqual(self.pago.estado_pago, 'Pendiente')

    @mock.patch('apps.pedidos.views.MERCADOPAGO_ACCESS_TOKEN', 'TEST-token')
    @mock.patch('apps.pedidos.views.MERCADOPAGO_WEBHOOK_SECRET', 'secreto')
    @mock.patch('apps.pedidos.views.consultar_pago_mercadopago')
    def test_webhook_firmado_aprueba_segun_la_api(self, consultar):
        consultar.return_value = {
            'external_reference': str(self.pedido.pk),
            'status': 'approved',
            'transaction_amount': 1000,
        }
        url = reverse('apps.pedidos:webhook_mercadopago') + '?type=payment&data.id=555'
        respuesta = self.client.post(
            url, HTTP_X_SIGNATURE=_firmar('secreto', '555', 'r'), HTTP_X_REQUEST_ID='r'
        )
        self.assertEqual(respuesta.status_code, 200)
        self._recargar()
        self.assertEqual(self.pago.estado_pago, 'Aprobado')
        self.assertEqual(self.pago.mercadopago_payment_id, '555')
        self.assertEqual(self.pedido.estado, 'Confirmado')

    # H-20 (A-D1)
    def test_checkout_web_no_ofrece_tarjeta(self):
        codigos = set(metodos_pago_checkout_web().values_list('codigo', flat=True))
        self.assertNotIn('TARJETA', codigos)
        self.assertIn('EFECTIVO', codigos)
