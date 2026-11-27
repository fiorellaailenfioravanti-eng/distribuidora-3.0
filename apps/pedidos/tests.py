from django.utils import timezone
from datetime import timedelta
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
from .models import DetallePedido, MetodoPago, PagoPedido, Pedido
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


class TransicionesManualesTests(TestCase):
    """H-29: el cambio manual de estado respeta el circuito de logística."""

    def setUp(self):
        self.pedido = Pedido.objects.create(
            metodo_pago=MetodoPago.objects.get(codigo='EFECTIVO'),
            total=Decimal('100'), estado='Pendiente',
        )

    def test_flujo_valido(self):
        self.assertTrue(self.pedido.cambiar_estado_manual('Confirmado'))
        self.assertTrue(self.pedido.cambiar_estado_manual('Entregado'))
        self.pedido.refresh_from_db()
        self.assertEqual(self.pedido.estado, 'Entregado')
        self.assertIsNotNone(self.pedido.fecha_entrega)

    def test_estados_terminales_no_vuelven_atras(self):
        self.pedido.cambiar_estado_manual('Cancelado')
        self.assertFalse(self.pedido.cambiar_estado_manual('Pendiente'))
        self.assertEqual(self.pedido.estados_manuales_posibles(), [])

    def test_no_se_marca_en_camino_a_mano(self):
        self.assertFalse(self.pedido.cambiar_estado_manual('En Camino'))

    def test_pedido_en_hoja_de_ruta_se_entrega_desde_logistica(self):
        from datetime import date
        from apps.logistica.models import DetalleHojaRuta, HojaRuta
        self.pedido.cambiar_estado_manual('Confirmado')
        hoja = HojaRuta.objects.create(fecha=date(2026, 10, 20))
        DetalleHojaRuta.objects.create(hoja_ruta=hoja, pedido=self.pedido, orden=1)
        self.assertNotIn('Entregado', self.pedido.estados_manuales_posibles())
        self.assertFalse(self.pedido.cambiar_estado_manual('Entregado'))


class CheckoutRequiereTelefonosTests(TestCase):
    """RF-04: sin un teléfono de contacto no se puede comprar."""

    def setUp(self):
        from apps.carrito.models import Carrito
        from apps.clientes.models import DireccionEntrega, TelefonoContacto
        from apps.productos.models import Producto
        self.usuario = get_user_model().objects.create_user('compra', 'c@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        self.direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='1')
        TelefonoContacto.objects.create(cliente=self.cliente, numero='3624111111', desc_relacion='Titular')
        producto = Producto.objects.create(nombre='Bidón', descripcion='', precio=Decimal('10'), stock=5)
        Carrito.objects.create(usuario=self.usuario).items.create(producto=producto, cantidad=1)
        self.client.force_login(self.usuario)
        self.TelefonoContacto = TelefonoContacto

    def _confirmar(self):
        return self.client.post(reverse('apps.pedidos:confirmar_pedido'), {
            'direccion_entrega': self.direccion.pk,
            'metodo_pago': MetodoPago.objects.get(codigo='EFECTIVO').pk,
            'telefonos_contacto': list(self.direccion.cliente.telefonos.values_list('pk', flat=True)),
        })

    def test_sin_telefono_no_compra(self):
        self.TelefonoContacto.objects.filter(cliente=self.cliente).delete()
        self.assertEqual(self.client.get(reverse('apps.pedidos:checkout')).url, reverse('apps.clientes:mi_perfil'))
        self._confirmar()
        self.assertFalse(Pedido.objects.filter(cliente=self.cliente).exists())

    def test_con_un_telefono_compra(self):
        self._confirmar()
        self.assertTrue(Pedido.objects.filter(cliente=self.cliente).exists())


class PagosParcialesTests(TestCase):
    """H-30 / RF-13: un pago parcial no marca el pedido como pagado."""

    def test_pagos_parciales(self):
        efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        pedido = Pedido.objects.create(metodo_pago=efectivo, total=Decimal('25000'))
        for _ in range(2):
            PagoPedido.objects.create(pedido=pedido, monto=Decimal('10000'), metodo_pago=efectivo, estado_pago='Aprobado')
        self.assertFalse(pedido.esta_pagado())
        self.assertEqual(pedido.saldo_pendiente(), Decimal('5000'))
        PagoPedido.objects.create(pedido=pedido, monto=Decimal('5000'), metodo_pago=efectivo, estado_pago='Aprobado')
        self.assertTrue(pedido.esta_pagado())



# ─────────────────────────────────────────────────────────────
# FASE 6 — cobro manual, stock disponible y pedido automático
# ─────────────────────────────────────────────────────────────
class CobroManualTests(TestCase):
    """RF-13 / HU-05 y aceptación de la Fase 6."""

    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        from django.contrib.auth.models import Group
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        self.pedido = Pedido.objects.create(cliente=self.cliente, metodo_pago=self.efectivo,
                                            total=Decimal('25000'), estado='Pendiente')
        self.client.force_login(self.vendedor)
        self.url = reverse('apps.pedidos:registrar_pago', args=[self.pedido.pk])

    def _pagar(self, monto, metodo=None):
        self.client.post(self.url, {'monto': monto, 'metodo_pago': (metodo or self.efectivo).pk})
        self.pedido.refresh_from_db()

    def test_tres_pagos_parciales_y_el_cuarto_salda(self):
        self._pagar('10000')
        self._pagar('10000')
        self.assertFalse(self.pedido.esta_pagado())
        self._pagar('10000')  # supera el saldo de 5.000: se rechaza
        self.assertEqual(self.pedido.saldo_pendiente(), Decimal('5000'))
        self.assertEqual(self.pedido.estado, 'Pendiente')
        self._pagar('5000')
        self.assertTrue(self.pedido.esta_pagado())
        self.assertEqual(self.pedido.estado, 'Confirmado')

    def test_a_cuenta_sólo_con_fiado(self):
        cuenta = MetodoPago.objects.get(codigo='CUENTA')
        self._pagar('5000', cuenta)
        self.assertEqual(self.pedido.total_pagado(), 0)  # Normal sin fiado: rechazado
        self.cliente.tipo_cliente = 'Premium'
        self.cliente.save()
        self._pagar('5000', cuenta)
        self.assertEqual(self.pedido.total_pagado(), Decimal('5000'))
        self.assertEqual(self.cliente.cuenta_corriente.saldo, Decimal('5000'))

    def test_la_web_no_ofrece_cuenta_corriente(self):
        from .forms import metodos_pago_checkout_web
        self.assertNotIn('CUENTA', set(metodos_pago_checkout_web().values_list('codigo', flat=True)))

    def test_caja_resume_por_medio_y_excluye_lo_fiado(self):
        from .services import resumen_caja
        self._pagar('10000')
        self.cliente.tipo_cliente = 'Premium'
        self.cliente.save()
        self._pagar('3000', MetodoPago.objects.get(codigo='CUENTA'))
        caja = resumen_caja(dias=30)
        self.assertEqual(caja['total'], Decimal('10000'))
        self.assertEqual(caja['por_dia'][-1]['total'], Decimal('10000'))
        respuesta = self.client.get(reverse('dashboard'))
        self.assertContains(respuesta, 'Caja de los últimos 30 días')


class PagoPorVerificarTests(TestCase):
    """«Cambiar estado del pago» sólo resuelve el pago pendiente, nunca un cobro ya hecho."""

    def setUp(self):
        from django.contrib.auth.models import Group
        self.vendedor = get_user_model().objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.client.force_login(self.vendedor)
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.pedido = Pedido.objects.create(metodo_pago=self.efectivo, total=Decimal('2000'), estado='Pendiente')
        # Pago provisorio que crea el checkout por el total.
        self.provisorio = PagoPedido.objects.create(pedido=self.pedido, monto=Decimal('2000'),
                                                    metodo_pago=self.efectivo, estado_pago='Pendiente')
        self.url_estado = reverse('apps.pedidos:cambiar_estado_pago', args=[self.pedido.pk])

    def _cobrar(self, monto):
        from .services import registrar_pago_manual
        registrar_pago_manual(self.pedido, monto, self.efectivo)
        self.pedido.refresh_from_db()

    def test_cobro_parcial_achica_el_provisorio_y_el_total_lo_quita(self):
        self._cobrar('500')
        self.provisorio.refresh_from_db()
        self.assertEqual(self.provisorio.monto, Decimal('1500'))
        self._cobrar('1500')
        self.assertFalse(PagoPedido.objects.filter(pk=self.provisorio.pk).exists())
        self.assertEqual(self.pedido.estado_cobro(), 'Pagado')

    def test_rechazar_no_anula_un_cobro_aprobado(self):
        self._cobrar('500')
        self.client.post(self.url_estado, {'estado_pago': 'Rechazado'})
        self.assertEqual(self.pedido.total_pagado(), Decimal('500'))
        self.provisorio.refresh_from_db()
        self.assertEqual(self.provisorio.estado_pago, 'Rechazado')

    def test_aprobar_sólo_cubre_el_saldo_y_confirma_si_salda(self):
        self._cobrar('500')
        self.client.post(self.url_estado, {'estado_pago': 'Aprobado'})
        self.pedido.refresh_from_db()
        self.assertEqual(self.pedido.total_pagado(), Decimal('2000'))
        self.assertEqual(self.pedido.estado, 'Confirmado')

    def test_sin_pago_pendiente_no_confirma_un_pedido_a_medias(self):
        self._cobrar('500')
        self.provisorio.delete()
        respuesta = self.client.post(self.url_estado, {'estado_pago': 'Aprobado'}, follow=True)
        self.pedido.refresh_from_db()
        self.assertEqual(self.pedido.estado, 'Pendiente')
        self.assertEqual(self.pedido.total_pagado(), Decimal('500'))
        self.assertContains(respuesta, 'no tiene pagos pendientes')

    def test_listado_muestra_el_estado_del_cobro(self):
        self._cobrar('500')
        respuesta = self.client.get(reverse('apps.pedidos:listar_pedidos'))
        self.assertContains(respuesta, 'Aprobar $1500')


class StockComprometidoTests(TestCase):
    """RF-12: lo pedido y no despachado no se vende dos veces."""

    def setUp(self):
        from apps.productos.models import Producto
        self.producto = Producto.objects.create(nombre='Bidón', descripcion='', precio=Decimal('100'), stock=3)
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')

    def test_disponible_descuenta_pedidos_que_no_salieron(self):
        from .services import stock_disponible
        pedido = Pedido.objects.create(metodo_pago=self.efectivo, total=0, estado='Confirmado')
        DetallePedido.objects.create(pedido=pedido, producto=self.producto, precio_unitario=100, cantidad=2, subtotal=200)
        self.assertEqual(stock_disponible(self.producto), 1)
        pedido.estado = 'En Camino'  # ya se descontó del stock al cargar el camión
        pedido.save()
        self.assertEqual(stock_disponible(self.producto), 3)

    def test_segundo_cliente_no_compra_lo_comprometido(self):
        from apps.carrito.models import Carrito
        compradores = []
        for n in (1, 2):
            u = get_user_model().objects.create_user(f'c{n}', f'c{n}@x.com', 'Agua-Lluvia-2026')
            cliente = u.perfil_cliente
            direccion = DireccionEntrega.objects.create(cliente=cliente, calle='Mitre', altura=str(n))
            from apps.clientes.models import TelefonoContacto
            for numero in ('3624111111', '3624222222'):
                TelefonoContacto.objects.create(cliente=cliente, numero=numero, desc_relacion='Titular')
            Carrito.objects.create(usuario=u).items.create(producto=self.producto, cantidad=2)
            compradores.append((u, direccion))
        for usuario, direccion in compradores:
            self.client.force_login(usuario)
            self.client.post(reverse('apps.pedidos:confirmar_pedido'),
                             {'direccion_entrega': direccion.pk, 'metodo_pago': self.efectivo.pk,
                              'telefonos_contacto': list(direccion.cliente.telefonos.values_list('pk', flat=True))})
        self.assertEqual(Pedido.objects.filter(origen='WEB').count(), 1)


class PedidoAutomaticoTests(TestCase):
    """RF-18: el cliente activa una reposición periódica."""

    def setUp(self):
        from apps.productos.models import Producto
        self.bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'),
                                             stock=50, es_botellon=True, es_retornable=True)
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        self.direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='1', es_principal=True)
        self.hoy = timezone.localdate()

    def _activar(self, **extra):
        self.client.force_login(self.usuario)
        datos = {'producto': self.bidon.pk, 'cantidad': 2, 'periodicidad_dias': 15, 'direccion': self.direccion.pk,
                 'metodo_pago': MetodoPago.objects.get(codigo='EFECTIVO').pk,
                 'proxima_fecha': self.hoy.isoformat(), 'activa': 'on', **extra}
        return self.client.post(reverse('apps.pedidos:suscripcion_cliente', args=[self.cliente.pk]), datos)

    def test_cliente_activa_y_se_genera_un_pedido_por_periodo(self):
        from .models import SuscripcionReposicion
        from .services import generar_pedidos_automaticos
        self._activar()
        sus = SuscripcionReposicion.objects.get(cliente=self.cliente)
        self.assertTrue(sus.activa)
        self.assertEqual(len(generar_pedidos_automaticos(self.hoy)), 1)
        self.assertEqual(len(generar_pedidos_automaticos(self.hoy)), 0)  # idempotente
        pedido = Pedido.objects.get(origen='AUTOMATICO')
        self.assertEqual((pedido.total, pedido.estado), (Decimal('6000'), 'Confirmado'))
        sus.refresh_from_db()
        self.assertEqual(sus.proxima_fecha, self.hoy + timedelta(days=15))
        self.assertEqual(len(generar_pedidos_automaticos(self.hoy + timedelta(days=15))), 1)

    def test_pausada_no_genera_y_otro_usuario_no_la_toca(self):
        from .services import generar_pedidos_automaticos
        self._activar(activa='')
        self.assertEqual(generar_pedidos_automaticos(self.hoy), [])
        intruso = get_user_model().objects.create_user('otro', 'o@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(intruso)
        self.client.post(reverse('apps.pedidos:suscripcion_cliente', args=[self.cliente.pk]),
                         {'producto': self.bidon.pk, 'cantidad': 9, 'periodicidad_dias': 7,
                          'direccion': self.direccion.pk, 'proxima_fecha': self.hoy.isoformat(), 'activa': 'on'})
        self.assertEqual(self.cliente.suscripcion.cantidad, 2)

    def test_usa_el_saldo_prepago(self):
        from apps.promociones.models import Promocion
        from apps.promociones.services import vender_promocion
        from .services import generar_pedidos_automaticos
        promo = Promocion.objects.create(nombre='3x4', producto=self.bidon, cant_paga=3, cant_lleva=4, precio=Decimal('9000'))
        vender_promocion(self.cliente, promo)
        self._activar()
        pedido = generar_pedidos_automaticos(self.hoy)[0]
        self.assertEqual(pedido.total, Decimal('0'))

    def test_comando(self):
        from io import StringIO
        from django.core.management import call_command
        self._activar()
        salida = StringIO()
        call_command('generar_pedidos_automaticos', stdout=salida)
        self.assertIn('1 pedidos automáticos generados', salida.getvalue())

    def test_frecuente_con_pedido_automatico_no_se_duplica_al_planificar(self):
        from apps.logistica.models import Barrio, Zona
        from apps.logistica.services import construir_borrador
        from .services import generar_pedidos_automaticos
        zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        self.direccion.barrio = Barrio.objects.create(nombre='Centro', zona=zona)
        self.direccion.save()
        self.cliente.es_frecuente = True
        self.cliente.save()
        self._activar()
        generar_pedidos_automaticos(self.hoy)
        borrador = construir_borrador(self.hoy + timedelta(days=1), zona)
        self.assertEqual(borrador['frecuentes'], [])
        self.assertEqual(len(borrador['pedidos']), 1)


class StockReservadoTests(TestCase):
    """Lo comprado en la web queda reservado: deja de ofrecerse en el catálogo
    mientras el pedido está Pendiente o Confirmado, y vuelve si se cancela."""

    def setUp(self):
        from apps.carrito.models import Carrito
        from apps.clientes.models import TelefonoContacto
        from apps.productos.models import Producto
        self.producto = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('10'), stock=3)
        self.usuario = get_user_model().objects.create_user('comprador', 'cmp@x.com', 'Agua-Lluvia-2026')
        cliente = self.usuario.perfil_cliente
        self.direccion = DireccionEntrega.objects.create(cliente=cliente, calle='Mitre', altura='1')
        TelefonoContacto.objects.create(cliente=cliente, numero='3624111111', desc_relacion='Titular')
        Carrito.objects.create(usuario=self.usuario).items.create(producto=self.producto, cantidad=2)
        self.client.force_login(self.usuario)

    def _comprar(self):
        self.client.post(reverse('apps.pedidos:confirmar_pedido'), {
            'direccion_entrega': self.direccion.pk,
            'metodo_pago': MetodoPago.objects.get(codigo='EFECTIVO').pk,
            'telefonos_contacto': list(self.direccion.cliente.telefonos.values_list('pk', flat=True)),
        })
        return Pedido.objects.get(cliente__usuario=self.usuario)

    def _disponible_en_catalogo(self):
        respuesta = self.client.get(reverse('apps.productos:listar_productos'))
        return next(p.disponible for p in respuesta.context['productos'] if p.pk == self.producto.pk)

    def test_comprar_reserva_y_cancelar_libera(self):
        self.assertEqual(self._disponible_en_catalogo(), 3)
        pedido = self._comprar()                       # Pendiente: reserva
        self.assertEqual(self._disponible_en_catalogo(), 1)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.stock, 3)        # sigue en el depósito hasta cargar el camión
        pedido.cambiar_estado_manual('Confirmado')      # confirmado por el administrador: sigue reservado
        self.assertEqual(self._disponible_en_catalogo(), 1)
        pedido.cambiar_estado_manual('Cancelado')       # vuelve a estar a la venta
        self.assertEqual(self._disponible_en_catalogo(), 3)

    def test_no_permite_sobreventa(self):
        from apps.carrito.models import Carrito
        self._comprar()                                 # quedan 1 disponible
        otro = get_user_model().objects.create_user('otro', 'otro@x.com', 'Agua-Lluvia-2026')
        from apps.clientes.models import TelefonoContacto
        TelefonoContacto.objects.create(cliente=otro.perfil_cliente, numero='3624999999', desc_relacion='Titular')
        direccion = DireccionEntrega.objects.create(cliente=otro.perfil_cliente, calle='Roca', altura='2')
        Carrito.objects.create(usuario=otro).items.create(producto=self.producto, cantidad=2)
        self.client.force_login(otro)
        self.client.post(reverse('apps.pedidos:confirmar_pedido'), {
            'direccion_entrega': direccion.pk, 'metodo_pago': MetodoPago.objects.get(codigo='EFECTIVO').pk,
            'telefonos_contacto': list(direccion.cliente.telefonos.values_list('pk', flat=True)),
        })
        self.assertFalse(Pedido.objects.filter(cliente__usuario=otro).exists())


class MisPedidosComprasEsporadicasTests(TestCase):
    """Las ventas en la calle se le muestran al cliente como «compras esporádicas»."""

    def setUp(self):
        self.usuario = get_user_model().objects.create_user('esporadico', 'e@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.web = Pedido.objects.create(cliente=self.cliente, metodo_pago=efectivo, origen='WEB', total=10)
        self.calle = Pedido.objects.create(cliente=self.cliente, metodo_pago=efectivo, origen='REPARTIDOR',
                                           estado='Entregado', total=20,
                                           notas_cliente='Venta en la calle durante el reparto.')
        self.client.force_login(self.usuario)

    def test_listado_separa_compras_esporadicas(self):
        respuesta = self.client.get(reverse('apps.pedidos:mis_pedidos'))
        self.assertEqual(list(respuesta.context['pedidos']), [self.web])
        self.assertEqual(list(respuesta.context['compras_esporadicas']), [self.calle])
        self.assertContains(respuesta, 'Compras esporádicas')
        self.assertNotContains(respuesta, 'en calle')

    def test_detalle_se_titula_compra_esporadica(self):
        respuesta = self.client.get(reverse('apps.pedidos:detalle_pedido', args=[self.calle.pk]))
        self.assertContains(respuesta, 'Compra esporádica #')
        self.assertNotContains(respuesta, 'Venta en la calle')


import shutil
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings

_MEDIA_PRUEBAS = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=_MEDIA_PRUEBAS)
class CheckoutTransferenciaTests(TestCase):
    """Checkout web: sólo efectivo o transferencia, y la transferencia exige comprobante."""

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(_MEDIA_PRUEBAS, ignore_errors=True)

    def setUp(self):
        from apps.carrito.models import Carrito
        from apps.clientes.models import DireccionEntrega, TelefonoContacto
        from apps.productos.models import Producto
        self.usuario = get_user_model().objects.create_user('transfiere', 't@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        self.direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='1')
        TelefonoContacto.objects.create(cliente=self.cliente, numero='3624111111', desc_relacion='Titular')
        producto = Producto.objects.create(nombre='Bidón', descripcion='', precio=Decimal('10'), stock=5)
        Carrito.objects.create(usuario=self.usuario).items.create(producto=producto, cantidad=1)
        self.client.force_login(self.usuario)
        self.transferencia = MetodoPago.objects.get(codigo='TRANSFERENCIA')

    def _confirmar(self, metodo, **extra):
        return self.client.post(reverse('apps.pedidos:confirmar_pedido'), {
            'direccion_entrega': self.direccion.pk, 'metodo_pago': metodo.pk,
            'telefonos_contacto': list(self.direccion.cliente.telefonos.values_list('pk', flat=True)), **extra,
        })

    def test_checkout_ofrece_solo_efectivo_y_transferencia(self):
        codigos = list(metodos_pago_checkout_web().values_list('codigo', flat=True))
        self.assertEqual(sorted(codigos), ['EFECTIVO', 'TRANSFERENCIA'])
        respuesta = self.client.get(reverse('apps.pedidos:checkout'))
        self.assertContains(respuesta, 'Datos para transferir')
        self.assertNotContains(respuesta, 'Billetera Digital')

    def test_transferencia_sin_comprobante_no_crea_pedido(self):
        self._confirmar(self.transferencia)
        self.assertFalse(Pedido.objects.filter(cliente=self.cliente).exists())

    def test_transferencia_rechaza_archivo_que_no_es_imagen_ni_pdf(self):
        self._confirmar(self.transferencia, comprobante=SimpleUploadedFile('x.exe', b'MZ'))
        self.assertFalse(Pedido.objects.filter(cliente=self.cliente).exists())

    def test_transferencia_con_comprobante_queda_por_verificar(self):
        pdf = SimpleUploadedFile('comprobante.pdf', b'%PDF-1.4 prueba', content_type='application/pdf')
        self._confirmar(self.transferencia, comprobante=pdf)
        pedido = Pedido.objects.get(cliente=self.cliente)
        pago = pedido.pago_por_verificar()
        self.assertTrue(pago.comprobante.name.startswith('comprobantes/'))
        self.assertEqual(pago.metodo_pago, self.transferencia)
        # El dueño lo puede ver; otro cliente no.
        url = reverse('apps.pedidos:ver_comprobante', args=[pago.pk])
        self.assertEqual(self.client.get(url).status_code, 200)
        otro = get_user_model().objects.create_user('otro', 'o@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(otro)
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_efectivo_no_pide_comprobante(self):
        self._confirmar(MetodoPago.objects.get(codigo='EFECTIVO'))
        pago = Pedido.objects.get(cliente=self.cliente).pago_por_verificar()
        self.assertFalse(pago.comprobante)

    def test_ficha_del_cliente_muestra_el_comprobante_al_admin(self):
        pdf = SimpleUploadedFile('comprobante.pdf', b'%PDF-1.4 prueba', content_type='application/pdf')
        self._confirmar(self.transferencia, comprobante=pdf)
        pago = Pedido.objects.get(cliente=self.cliente).pago_con_comprobante()
        admin = get_user_model().objects.create_superuser('jefa', 'j@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(admin)
        respuesta = self.client.get(reverse('apps.clientes:ver_cliente', args=[self.cliente.pk]))
        url = reverse('apps.pedidos:ver_comprobante', args=[pago.pk])
        self.assertContains(respuesta, url)
        self.assertEqual(self.client.get(url).status_code, 200)


class CheckoutTelefonosDeContactoTests(TestCase):
    """El cliente confirma a qué teléfonos lo llaman, igual que la dirección."""

    def setUp(self):
        from apps.carrito.models import Carrito
        from apps.clientes.models import DireccionEntrega, TelefonoContacto
        from apps.productos.models import Producto
        self.usuario = get_user_model().objects.create_user('llamame', 'l@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        self.direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='1')
        self.titular = TelefonoContacto.objects.create(cliente=self.cliente, numero='3624111111',
                                                       desc_relacion='Titular', es_principal=True)
        self.vecino = TelefonoContacto.objects.create(cliente=self.cliente, numero='3624222222',
                                                      desc_relacion='Vecino')
        producto = Producto.objects.create(nombre='Bidón', descripcion='', precio=Decimal('10'), stock=5)
        Carrito.objects.create(usuario=self.usuario).items.create(producto=producto, cantidad=1)
        self.client.force_login(self.usuario)

    def _confirmar(self, telefonos):
        return self.client.post(reverse('apps.pedidos:confirmar_pedido'), {
            'direccion_entrega': self.direccion.pk,
            'metodo_pago': MetodoPago.objects.get(codigo='EFECTIVO').pk,
            'telefonos_contacto': [t.pk for t in telefonos],
        })

    def test_checkout_lista_los_telefonos_con_el_principal_marcado(self):
        respuesta = self.client.get(reverse('apps.pedidos:checkout'))
        self.assertContains(respuesta, 'Teléfono de Contacto')
        self.assertContains(respuesta, '3624222222 — Vecino')
        self.assertEqual(respuesta.context['form']['telefonos_contacto'].value(), [self.titular.pk])

    def test_sin_telefono_marcado_no_crea_pedido(self):
        self._confirmar([])
        self.assertFalse(Pedido.objects.filter(cliente=self.cliente).exists())

    def test_guarda_los_telefonos_elegidos_y_los_muestra(self):
        self._confirmar([self.titular, self.vecino])
        pedido = Pedido.objects.get(cliente=self.cliente)
        self.assertEqual(set(pedido.telefonos_contacto.all()), {self.titular, self.vecino})
        respuesta = self.client.get(reverse('apps.pedidos:detalle_pedido', args=[pedido.pk]))
        self.assertContains(respuesta, 'tel:3624222222')

    def test_no_acepta_telefonos_de_otro_cliente(self):
        from apps.clientes.models import TelefonoContacto
        ajeno = TelefonoContacto.objects.create(cliente=get_user_model().objects.create_user(
            'ajeno', 'a@x.com', 'Agua-Lluvia-2026').perfil_cliente, numero='3624999999', desc_relacion='Titular')
        self._confirmar([ajeno])
        self.assertFalse(Pedido.objects.filter(cliente=self.cliente).exists())

    def test_el_repartidor_llama_al_telefono_elegido(self):
        from apps.logistica.views import _ficha_de_parada
        from apps.logistica.models import DetalleHojaRuta
        self._confirmar([self.vecino])
        pedido = Pedido.objects.get(cliente=self.cliente)
        parada = DetalleHojaRuta(pedido=pedido, cliente=self.cliente, direccion_entrega=self.direccion,
                                 direccion_texto='Mitre 1')
        self.assertEqual(_ficha_de_parada(parada, self.usuario)['telefono'], self.vecino)


class PagoPendienteEnPedidosDeLaEmpresaTests(TestCase):
    """Los pedidos que no pasan por el checkout también quedan con su pago por verificar."""

    def setUp(self):
        from apps.productos.models import Producto
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.producto = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('1000'),
                                                stock=50, es_botellon=True)
        self.pedido = Pedido.objects.create(cliente=self.cliente, metodo_pago=self.efectivo, origen='ADMIN',
                                            estado='Confirmado', total=0)

    def test_al_fijar_botellones_queda_con_pago_pendiente_por_el_total(self):
        from apps.logistica.services import _fijar_botellones
        _fijar_botellones(self.pedido, {self.producto.pk: 2})
        pago = self.pedido.pago_por_verificar()
        self.assertEqual(pago.monto, Decimal('2000'))
        # Si cambian los botellones, el pago pendiente acompaña el total (no se duplica).
        _fijar_botellones(self.pedido, {self.producto.pk: 3})
        self.assertEqual(self.pedido.pagos.count(), 1)
        self.assertEqual(self.pedido.pago_por_verificar().monto, Decimal('3000'))

    def test_al_cobrarlo_desaparece_el_pendiente(self):
        from apps.logistica.services import _fijar_botellones
        from .services import registrar_cobro
        _fijar_botellones(self.pedido, {self.producto.pk: 2})
        registrar_cobro(self.pedido, Decimal('2000'), self.efectivo)
        self.assertIsNone(self.pedido.pago_por_verificar())
        self.assertTrue(self.pedido.esta_pagado())

    def test_no_toca_un_pago_de_mercadopago_en_curso(self):
        from .services import sincronizar_pago_pendiente
        self.pedido.total = Decimal('500')
        self.pedido.save()
        PagoPedido.objects.create(pedido=self.pedido, monto=Decimal('500'), metodo_pago=self.efectivo,
                                  estado_pago='Pendiente', mercadopago_payment_id='123')
        sincronizar_pago_pendiente(self.pedido)
        self.assertEqual(self.pedido.pagos.count(), 1)


class CorregirPagoResueltoTests(TestCase):
    """El administrador puede corregir un pago que aprobó o rechazó por error."""

    def setUp(self):
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        self.pedido = Pedido.objects.create(cliente=self.cliente, metodo_pago=self.efectivo, total=Decimal('2000'),
                                            estado='Entregado')
        self.pago = PagoPedido.objects.create(pedido=self.pedido, monto=Decimal('2000'), metodo_pago=self.efectivo,
                                              estado_pago='Aprobado', referencia_comprobante='Cobro en calle — hoja #1')
        self.admin = get_user_model().objects.create_superuser('jefa', 'j@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(self.admin)
        self.url = reverse('apps.pedidos:cambiar_estado_pago', args=[self.pedido.pk])

    def test_la_gestion_ofrece_corregir_un_pedido_pagado(self):
        respuesta = self.client.get(reverse('apps.pedidos:listar_pedidos'))
        self.assertContains(respuesta, 'Volver a pendiente')
        self.assertContains(respuesta, 'Marcar rechazado')

    def test_volver_a_pendiente(self):
        self.client.post(self.url, {'corregir': 'Pendiente'})
        self.pago.refresh_from_db()
        self.assertEqual(self.pago.estado_pago, 'Pendiente')
        self.assertFalse(self.pedido.esta_pagado())
        self.assertEqual(self.pedido.pago_por_verificar(), self.pago)  # se puede volver a aprobar

    def test_marcar_rechazado_y_volver_a_pendiente(self):
        self.client.post(self.url, {'corregir': 'Rechazado'})
        self.pago.refresh_from_db()
        self.assertEqual(self.pago.estado_pago, 'Rechazado')
        self.assertEqual(self.pedido.estado_cobro(), 'Rechazado')
        self.client.post(self.url, {'corregir': 'Pendiente'})
        self.pago.refresh_from_db()
        self.assertEqual(self.pago.estado_pago, 'Pendiente')

    def test_no_corrige_lo_cargado_a_cuenta_corriente(self):
        self.pago.metodo_pago = MetodoPago.objects.get(codigo='CUENTA')
        self.pago.save()
        self.client.post(self.url, {'corregir': 'Pendiente'})
        self.pago.refresh_from_db()
        self.assertEqual(self.pago.estado_pago, 'Aprobado')

    def test_requiere_permiso_de_cobro(self):
        cliente_web = get_user_model().objects.create_user('cli', 'c@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(cliente_web)
        self.client.post(self.url, {'corregir': 'Pendiente'})
        self.pago.refresh_from_db()
        self.assertEqual(self.pago.estado_pago, 'Aprobado')
