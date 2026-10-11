from datetime import date

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import ZonaForm
from .models import (
    Zona, CalendarioExcepcion, Camion, HojaRuta, DetalleHojaRuta, Barrio,
    CargaHojaRuta,
)
from .services import (
    fecha_es_de_reparto, proxima_fecha_de_reparto,
    construir_borrador, crear_hoja_borrador,
    confirmar_hoja, registrar_regreso,
    registrar_entrega, registrar_cobro, crear_venta_calle,
    fecha_estimada_para_direccion,
)
from apps.clientes.models import Cliente, DireccionEntrega
from apps.pedidos.models import Pedido, DetallePedido, MetodoPago
from apps.productos.models import Producto


class ZonaDiasRepartoTests(TestCase):
    def test_set_y_get_dias_ordena_y_limpia(self):
        zona = Zona(nombre='Zona Test')
        zona.set_dias_reparto([4, 0, 4, 2])
        self.assertEqual(zona.dias_reparto, '0,2,4')
        self.assertEqual(zona.get_dias_reparto(), [0, 2, 4])

    def test_incluye_dia(self):
        zona = Zona(nombre='Zona Test', dias_reparto='1,4')
        self.assertTrue(zona.incluye_dia(1))
        self.assertTrue(zona.incluye_dia(4))
        self.assertFalse(zona.incluye_dia(0))

    def test_dias_reparto_display(self):
        zona = Zona(nombre='Zona Test', dias_reparto='1,4')
        self.assertEqual(zona.dias_reparto_display(), 'Martes, Viernes')


class CalendarioTests(TestCase):
    def setUp(self):
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='4')  # viernes

    def test_fecha_es_de_reparto_segun_dia(self):
        self.assertTrue(fecha_es_de_reparto(self.zona, date(2026, 3, 6)))   # viernes
        self.assertFalse(fecha_es_de_reparto(self.zona, date(2026, 3, 5)))  # jueves

    def test_excepcion_suspende(self):
        CalendarioExcepcion.objects.create(
            fecha=date(2026, 3, 6), zona=self.zona, tipo='suspende'
        )
        self.assertFalse(fecha_es_de_reparto(self.zona, date(2026, 3, 6)))

    def test_excepcion_global_suspende(self):
        CalendarioExcepcion.objects.create(
            fecha=date(2026, 3, 6), zona=None, tipo='suspende'
        )
        self.assertFalse(fecha_es_de_reparto(self.zona, date(2026, 3, 6)))

    def test_excepcion_agrega(self):
        zona = Zona.objects.create(nombre='Otra', dias_reparto='')
        self.assertFalse(fecha_es_de_reparto(zona, date(2026, 3, 10)))  # martes
        CalendarioExcepcion.objects.create(
            fecha=date(2026, 3, 10), zona=zona, tipo='agrega'
        )
        self.assertTrue(fecha_es_de_reparto(zona, date(2026, 3, 10)))

    def test_proxima_fecha_de_reparto(self):
        # Desde el lunes 2/3/2026 -> viernes 6/3/2026
        self.assertEqual(
            proxima_fecha_de_reparto(self.zona, date(2026, 3, 2)),
            date(2026, 3, 6)
        )

    def test_proxima_salta_dia_suspendido(self):
        CalendarioExcepcion.objects.create(
            fecha=date(2026, 3, 6), zona=self.zona, tipo='suspende'
        )
        self.assertEqual(
            proxima_fecha_de_reparto(self.zona, date(2026, 3, 2)),
            date(2026, 3, 13)
        )


class ZonaFormTests(TestCase):
    def test_guarda_dias_reparto(self):
        form = ZonaForm(data={'nombre': 'Norte', 'descripcion': '', 'dias_reparto': ['1', '4']})
        self.assertTrue(form.is_valid(), form.errors)
        zona = form.save()
        self.assertEqual(zona.dias_reparto, '1,4')

    def test_precarga_dias_en_edicion(self):
        zona = Zona.objects.create(nombre='Sur', dias_reparto='2')
        form = ZonaForm(instance=zona)
        self.assertEqual(form.fields['dias_reparto'].initial, [2])


class HojaRutaCapacidadTests(TestCase):
    def test_total_botellones_y_capacidad(self):
        camion = Camion.objects.create(patente='AA000AA', capacidad_botellones=2)
        hoja = HojaRuta.objects.create(fecha=date(2026, 3, 6), camion=camion)
        DetalleHojaRuta.objects.create(hoja_ruta=hoja, orden=1, cantidad_bidones=1)
        DetalleHojaRuta.objects.create(hoja_ruta=hoja, orden=2, cantidad_bidones=1)
        self.assertEqual(hoja.total_botellones(), 2)
        self.assertFalse(hoja.supera_capacidad())

        DetalleHojaRuta.objects.create(hoja_ruta=hoja, orden=3, cantidad_bidones=1)
        self.assertTrue(hoja.supera_capacidad())


class GeneracionBorradorTests(TestCase):
    def setUp(self):
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,4')
        self.otra_zona = Zona.objects.create(nombre='Norte', dias_reparto='2')
        self.barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        self.otro_barrio = Barrio.objects.create(nombre='Norte', zona=self.otra_zona)
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')

        self.cliente = Cliente.objects.create(
            nombre='Ana', apellido='Pérez', es_frecuente=True,
            cantidad_recurrente_default=2
        )
        self.direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='San Martín', altura='100',
            barrio=self.barrio, es_principal=True
        )
        self.cliente_ajeno = Cliente.objects.create(
            nombre='Beto', apellido='Gómez', es_frecuente=True
        )
        DireccionEntrega.objects.create(
            cliente=self.cliente_ajeno, calle='Rivadavia', altura='50',
            barrio=self.otro_barrio, es_principal=True
        )

    def _pedido(self, cliente, direccion, estado='Confirmado'):
        return Pedido.objects.create(
            cliente=cliente, direccion_entrega=direccion,
            metodo_pago=self.efectivo, estado=estado, total=0
        )

    def test_borrador_lista_frecuentes_de_la_zona(self):
        borrador = construir_borrador(date(2026, 3, 2), self.zona)
        clientes = [f['cliente'] for f in borrador['frecuentes']]
        self.assertIn(self.cliente, clientes)
        self.assertNotIn(self.cliente_ajeno, clientes)
        self.assertEqual(borrador['frecuentes'][0]['cantidad_sugerida'], 2)

    def test_borrador_lista_pedidos_de_la_zona(self):
        pedido_zona = self._pedido(self.cliente, self.direccion)
        pedido_ajeno = self._pedido(self.cliente_ajeno, self.cliente_ajeno.direcciones.first())
        borrador = construir_borrador(date(2026, 3, 2), self.zona)
        self.assertIn(pedido_zona, borrador['pedidos'])
        self.assertNotIn(pedido_ajeno, borrador['pedidos'])

    def test_borrador_excluye_pedidos_ya_ruteados(self):
        pedido = self._pedido(self.cliente, self.direccion)
        hoja = HojaRuta.objects.create(fecha=date(2026, 3, 2), zona=self.zona)
        DetalleHojaRuta.objects.create(hoja_ruta=hoja, orden=1, pedido=pedido)
        borrador = construir_borrador(date(2026, 3, 2), self.zona)
        self.assertNotIn(pedido, borrador['pedidos'])

    def test_crear_hoja_borrador(self):
        pedido = self._pedido(self.cliente, self.direccion)
        seleccion = {
            'pedidos': [{'pedido_id': pedido.id_pedido, 'cantidad': 3}],
            'frecuentes': [{'cliente_id': self.cliente.id, 'direccion_id': self.direccion.id, 'cantidad': 2}],
        }
        hoja = crear_hoja_borrador(date(2026, 3, 2), self.zona, self._usuario(), seleccion)
        self.assertEqual(hoja.estado, 'Borrador')
        self.assertEqual(hoja.zona, self.zona)
        self.assertEqual(hoja.total_paradas(), 2)
        parada_pedido = hoja.detalles.get(pedido=pedido)
        self.assertEqual(parada_pedido.cantidad_bidones, 3)
        parada_frecuente = hoja.detalles.get(es_frecuente=True)
        self.assertEqual(parada_frecuente.cantidad_bidones, 2)
        pedido.refresh_from_db()
        self.assertEqual(pedido.fecha_entrega, date(2026, 3, 2))

    def _usuario(self):
        from apps.autenticacion.models import Usuario
        return Usuario.objects.create_user(username='admin_test', password='x')

    def test_fecha_estimada_para_direccion(self):
        fecha = fecha_estimada_para_direccion(self.direccion)
        self.assertIsNotNone(fecha)
        self.assertIn(fecha.weekday(), self.zona.get_dias_reparto())
        self.assertGreaterEqual(fecha, timezone.localdate())

    def test_fecha_estimada_sin_zona_es_none(self):
        barrio_sin_zona = Barrio.objects.create(nombre='Sin Zona')
        direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='Urquiza', altura='100', barrio=barrio_sin_zona
        )
        self.assertIsNone(fecha_estimada_para_direccion(direccion))


class PlanificarRepartoViewTests(TestCase):
    def setUp(self):
        from apps.autenticacion.models import Usuario
        self.admin = Usuario.objects.create_superuser(
            username='super', password='x', email='super@x.com'
        )
        self.client.force_login(self.admin)
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,4')
        self.barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        self.cliente = Cliente.objects.create(
            nombre='Ana', apellido='Pérez', es_frecuente=True,
            cantidad_recurrente_default=2
        )
        self.direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='San Martín', altura='100',
            barrio=self.barrio, es_principal=True
        )

    def test_get_muestra_frecuentes(self):
        url = reverse('apps.logistica:planificar_reparto')
        resp = self.client.get(url, {'fecha': '2026-03-02', 'zona': self.zona.id_zona})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Ana')

    def test_post_crea_hoja_borrador(self):
        url = reverse('apps.logistica:planificar_reparto')
        resp = self.client.post(url, {
            'fecha': '2026-03-02',
            'zona': self.zona.id_zona,
            'confirmar': '1',
            f'frecuente_{self.cliente.id}': 'on',
            f'direccion_frecuente_{self.cliente.id}': self.direccion.id,
            f'cantidad_frecuente_{self.cliente.id}': '2',
        })
        self.assertEqual(resp.status_code, 302)
        hoja = HojaRuta.objects.get(zona=self.zona, fecha=date(2026, 3, 2))
        self.assertEqual(hoja.estado, 'Borrador')
        self.assertEqual(hoja.total_paradas(), 1)

    def test_get_confirmar_ruta(self):
        hoja = HojaRuta.objects.create(fecha=date(2026, 3, 2), zona=self.zona, estado='Borrador')
        resp = self.client.get(reverse('apps.logistica:confirmar_ruta', args=[hoja.id_ruta]))
        self.assertEqual(resp.status_code, 200)

    def test_get_registrar_regreso(self):
        hoja = HojaRuta.objects.create(fecha=date(2026, 3, 2), zona=self.zona, estado='Confirmada')
        resp = self.client.get(reverse('apps.logistica:registrar_regreso_ruta', args=[hoja.id_ruta]))
        self.assertEqual(resp.status_code, 200)

    def test_get_venta_calle(self):
        hoja = HojaRuta.objects.create(fecha=date(2026, 3, 2), zona=self.zona, estado='Confirmada')
        resp = self.client.get(reverse('apps.logistica:venta_calle', args=[hoja.id_ruta]))
        self.assertEqual(resp.status_code, 200)


class ConfirmacionRegresoTests(TestCase):
    def setUp(self):
        from apps.autenticacion.models import Usuario
        self.usuario = Usuario.objects.create_superuser(
            username='admin', password='x', email='a@a.com'
        )
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,4')
        self.barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Pérez')
        self.direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='San Martín', altura='100',
            barrio=self.barrio, es_principal=True
        )
        self.producto = Producto.objects.create(
            nombre='Bidón 20L', descripcion='', precio=100, stock=10
        )
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.pedido = Pedido.objects.create(
            cliente=self.cliente, direccion_entrega=self.direccion,
            metodo_pago=self.efectivo, estado='Confirmado', total=0
        )
        self.hoja = HojaRuta.objects.create(fecha=date(2026, 3, 2), zona=self.zona)
        DetalleHojaRuta.objects.create(
            hoja_ruta=self.hoja, orden=1, pedido=self.pedido,
            cliente=self.cliente, direccion_entrega=self.direccion,
            cantidad_bidones=4,
        )

    def test_confirmar_descuenta_stock_y_pasa_en_camino(self):
        confirmar_hoja(self.hoja, self.usuario, [
            {'producto_id': self.producto.id_producto, 'cantidad': 4},
        ])
        self.hoja.refresh_from_db()
        self.producto.refresh_from_db()
        self.pedido.refresh_from_db()
        self.assertEqual(self.hoja.estado, 'Confirmada')
        self.assertEqual(self.producto.stock, 6)
        self.assertEqual(self.pedido.estado, 'En Camino')
        self.assertTrue(self.hoja.cargas.filter(producto=self.producto, cantidad_cargada=4).exists())

    def test_regreso_devuelve_sobrantes_y_cierra(self):
        confirmar_hoja(self.hoja, self.usuario, [
            {'producto_id': self.producto.id_producto, 'cantidad': 4},
        ])
        carga = self.hoja.cargas.get()
        registrar_regreso(self.hoja, [
            {'carga_id': carga.id_carga, 'cantidad_entregada': 3, 'cantidad_retornada': None},
        ])
        self.hoja.refresh_from_db()
        carga.refresh_from_db()
        self.producto.refresh_from_db()
        self.assertEqual(self.hoja.estado, 'Cerrada')
        self.assertEqual(carga.cantidad_retornada, 1)
        self.assertEqual(self.producto.stock, 7)


class EntregaCalleTests(TestCase):
    def setUp(self):
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,4')
        self.barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Pérez')
        self.direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='San Martín', altura='100',
            barrio=self.barrio, es_principal=True
        )
        self.envase = Producto.objects.create(
            nombre='Bidón vacío', descripcion='', precio=0, stock=5, es_envase=True
        )
        self.lleno = Producto.objects.create(
            nombre='Bidón lleno', descripcion='', precio=100, stock=10,
            es_retornable=True, envase=self.envase
        )
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.pedido = Pedido.objects.create(
            cliente=self.cliente, direccion_entrega=self.direccion,
            metodo_pago=self.efectivo, estado='En Camino', total=200
        )
        DetallePedido.objects.create(
            pedido=self.pedido, producto=self.lleno,
            precio_unitario=100, cantidad=2, subtotal=200
        )
        self.hoja = HojaRuta.objects.create(
            fecha=date(2026, 3, 2), zona=self.zona, estado='Confirmada'
        )
        self.parada = DetalleHojaRuta.objects.create(
            hoja_ruta=self.hoja, orden=1, pedido=self.pedido,
            cliente=self.cliente, direccion_entrega=self.direccion,
        )

    def test_registrar_entrega_ajusta_envases_y_pedido(self):
        registrar_entrega(self.parada, 'Entregado', envases_retirados=2, envases_vendidos=1)
        self.parada.refresh_from_db()
        self.pedido.refresh_from_db()
        self.envase.refresh_from_db()
        self.assertEqual(self.parada.estado, 'Entregado')
        self.assertEqual(self.pedido.estado, 'Entregado')
        self.assertEqual(self.envase.stock, 6)

    def test_registrar_cobro_crea_pago_aprobado(self):
        pago = registrar_cobro(self.pedido, 200, self.efectivo)
        self.assertEqual(pago.estado_pago, 'Aprobado')
        self.assertTrue(self.pedido.esta_pagado())

    def test_crear_venta_calle(self):
        parada = crear_venta_calle(self.hoja, {
            'nombre': 'Juan', 'apellido': 'Pérez',
            'calle': 'Belgrano', 'altura': '10',
            'barrio_id': self.barrio.pk,
            'metodo_pago_id': self.efectivo.pk,
            'marcar_frecuente': True,
            'productos': [{'producto_id': self.lleno.pk, 'cantidad': 2}],
        })
        self.lleno.refresh_from_db()
        self.assertEqual(parada.estado, 'Entregado')
        self.assertEqual(parada.pedido.origen, 'REPARTIDOR')
        self.assertEqual(parada.pedido.total, 200)
        self.assertTrue(parada.pedido.esta_pagado())
        self.assertTrue(parada.cliente.es_frecuente)
        self.assertEqual(parada.cliente.tipo_registro, 'pasajero')
        self.assertEqual(self.lleno.stock, 8)




