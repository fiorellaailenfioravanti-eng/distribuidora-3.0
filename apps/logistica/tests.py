from decimal import Decimal
from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import ZonaForm
from .models import (
    RutaReparto,
    Zona, CalendarioExcepcion, Camion, HojaRuta, DetalleHojaRuta, Barrio,
    CargaHojaRuta,
)
from apps.pedidos.services import resolver_pago_pendiente
from .services import (
    fecha_es_de_reparto, proxima_fecha_de_reparto,
    construir_borrador, crear_hoja_borrador,
    confirmar_hoja, registrar_regreso,
    registrar_entrega, registrar_cobro, crear_venta_calle,
    fecha_estimada_para_direccion, carga_sugerida,
)
from apps.clientes.models import Cliente, DireccionEntrega
from apps.pedidos.models import Pedido, DetallePedido, MetodoPago, PagoPedido
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
        from apps.pedidos.models import DetallePedido
        from apps.productos.models import Producto
        bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'),
                                        stock=50, es_botellon=True, es_retornable=True)
        pedido = self._pedido(self.cliente, self.direccion)
        DetallePedido.objects.create(pedido=pedido, producto=bidon, precio_unitario=bidon.precio,
                                     cantidad=3, subtotal=bidon.precio * 3)
        seleccion = {
            'pedidos': [{'pedido_id': pedido.id_pedido}],
            'frecuentes': [{'cliente_id': self.cliente.id, 'direccion_id': self.direccion.id, 'cantidad': 2}],
        }
        hoja = crear_hoja_borrador(date(2026, 3, 2), self.zona, self._usuario(), seleccion)
        self.assertEqual(hoja.estado, 'Borrador')
        self.assertEqual(hoja.zona, self.zona)
        self.assertEqual(hoja.total_paradas(), 2)
        parada_pedido = hoja.detalles.get(pedido=pedido)
        self.assertEqual(parada_pedido.cantidad_bidones, 3)  # lo que pidió el cliente
        parada_frecuente = hoja.detalles.get(es_frecuente=True)
        self.assertEqual(parada_frecuente.cantidad_bidones, 2)
        # El frecuente queda con un pedido real de botellones: cuenta para la carga del camión.
        self.assertEqual(parada_frecuente.pedido.total, Decimal('6000'))
        self.assertEqual(carga_sugerida(hoja), [{'producto': bidon, 'cantidad': 5}])
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

    def test_no_se_carga_mas_que_el_stock_del_deposito(self):
        with self.assertRaisesMessage(ValueError, 'No alcanza el stock'):
            confirmar_hoja(self.hoja, self.usuario, [
                {'producto_id': self.producto.id_producto, 'cantidad': 11},
            ])
        self.hoja.refresh_from_db()
        self.producto.refresh_from_db()
        self.assertEqual(self.hoja.estado, 'Borrador')
        self.assertEqual(self.producto.stock, 10)
        self.assertFalse(self.hoja.cargas.exists())

    def test_vista_confirmar_rechaza_carga_sin_stock_y_conserva_lo_tipeado(self):
        self.client.force_login(self.usuario)
        resp = self.client.post(reverse('apps.logistica:confirmar_ruta', args=[self.hoja.pk]),
                                {f'cantidad_producto_{self.producto.pk}': 15})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No alcanza el stock')
        self.hoja.refresh_from_db()
        self.assertEqual(self.hoja.estado, 'Borrador')

    def test_regreso_no_puede_superar_lo_cargado(self):
        confirmar_hoja(self.hoja, self.usuario, [
            {'producto_id': self.producto.id_producto, 'cantidad': 4},
        ])
        carga = self.hoja.cargas.get()
        with self.assertRaisesMessage(ValueError, 'se cargaron 4'):
            registrar_regreso(self.hoja, [
                {'carga_id': carga.id_carga, 'cantidad_entregada': 3, 'cantidad_retornada': 2},
            ])
        self.hoja.refresh_from_db()
        self.producto.refresh_from_db()
        self.assertEqual(self.hoja.estado, 'Confirmada')
        self.assertEqual(self.producto.stock, 6)


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

    def test_no_se_venden_mas_envases_que_botellones_entregados(self):
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            registrar_entrega(self.parada, 'Entregado', envases_retirados=0, envases_vendidos=3)
        self.envase.refresh_from_db()
        self.parada.refresh_from_db()
        self.assertEqual(self.envase.stock, 5)
        self.assertEqual(self.parada.estado, 'Pendiente')

    def test_registrar_entrega_dos_veces_no_duplica_envases(self):
        """H-28: volver a guardar la parada aplica sólo la diferencia."""
        registrar_entrega(self.parada, 'Entregado', envases_retirados=2, envases_vendidos=1)
        registrar_entrega(self.parada, 'Entregado', envases_retirados=2, envases_vendidos=1)
        self.envase.refresh_from_db()
        self.assertEqual(self.envase.stock, 6)
        # Corregir de 2 a 3 retirados suma sólo uno más.
        registrar_entrega(self.parada, 'Entregado', envases_retirados=3, envases_vendidos=1)
        self.envase.refresh_from_db()
        self.assertEqual(self.envase.stock, 7)

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
        # Lo cobrado queda por aprobar hasta que el administrador cuente el efectivo.
        self.assertFalse(parada.pedido.esta_pagado())
        self.assertEqual(parada.pedido.pago_por_verificar().monto, 200)
        resolver_pago_pendiente(parada.pedido, aprobar=True)
        self.assertTrue(parada.pedido.esta_pagado())
        self.assertTrue(parada.cliente.es_frecuente)
        self.assertEqual(parada.cliente.tipo_registro, 'pasajero')
        self.assertEqual(self.lleno.stock, 8)






class HojaSinChoferTests(TestCase):
    """Una hoja sin chofer asignado rompía el listado, el detalle y la impresión."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        self.hoja = HojaRuta.objects.create(fecha=date(2026, 10, 20))
        admin = get_user_model().objects.create_superuser('root', 'root@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(admin)

    def test_pantallas_de_hoja_renderizan(self):
        from django.urls import reverse
        for nombre, args, texto in [('listar_rutas', [], 'Sin asignar'), ('ver_ruta', [self.hoja.pk], 'Sin repartidor'),
                                    ('imprimir_ruta', [self.hoja.pk], 'Sin asignar')]:
            respuesta = self.client.get(reverse(f'apps.logistica:{nombre}', args=args))
            self.assertEqual(respuesta.status_code, 200, nombre)
            self.assertContains(respuesta, texto)

    def test_eliminar_zona_con_rutas_no_da_500(self):
        from django.urls import reverse
        zona = Zona.objects.create(nombre='Con rutas', dias_reparto='0')
        RutaReparto.objects.create(nombre='Ruta Lunes', zona=zona, dia_semana=0)
        self.assertEqual(self.client.get(reverse('apps.logistica:eliminar_zona', args=[zona.pk])).status_code, 200)
        respuesta = self.client.post(reverse('apps.logistica:eliminar_zona', args=[zona.pk]))
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(Zona.objects.filter(pk=zona.pk).exists())


class GeneracionQuincenalTests(TestCase):
    """RF-17 (decisión A-D5): borradores de reparto para los próximos 15 días."""

    def setUp(self):
        from apps.clientes.models import Cliente, DireccionEntrega
        from apps.pedidos.models import MetodoPago, Pedido
        self.lunes = date(2026, 11, 2)  # lunes
        self.zona = Zona.objects.create(nombre='Lunes y jueves', dias_reparto='0,3')
        barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        direccion = DireccionEntrega.objects.create(cliente=cliente, calle='Mitre', altura='1', barrio=barrio)
        efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.p_lunes = Pedido.objects.create(cliente=cliente, direccion_entrega=direccion, metodo_pago=efectivo,
                                             estado='Confirmado', fecha_estimada_entrega=self.lunes)
        self.p_jueves = Pedido.objects.create(cliente=cliente, direccion_entrega=direccion, metodo_pago=efectivo,
                                              estado='Confirmado', fecha_estimada_entrega=self.lunes + timedelta(days=3))

    def test_crea_borradores_por_dia_de_reparto(self):
        from apps.logistica.services import generar_borradores_periodo
        hojas = generar_borradores_periodo(desde=self.lunes, dias=15)
        self.assertEqual([h.fecha for h in hojas], [self.lunes, self.lunes + timedelta(days=3)])
        self.assertTrue(all(h.estado == 'Borrador' for h in hojas))
        self.assertEqual(self.p_lunes.paradas.get().hoja_ruta, hojas[0])
        self.assertEqual(self.p_jueves.paradas.get().hoja_ruta, hojas[1])

    def test_es_idempotente(self):
        from django.core.management import call_command
        from io import StringIO
        call_command('generar_borradores_reparto', desde=self.lunes.isoformat(), stdout=StringIO())
        call_command('generar_borradores_reparto', desde=self.lunes.isoformat(), stdout=StringIO())
        self.assertEqual(HojaRuta.objects.count(), 2)


class SeedDemoTests(TestCase):
    """El seed de demostración corre sobre una base nueva y es idempotente."""

    def test_seed_demo_dos_veces(self):
        from io import StringIO
        from django.core.management import call_command
        from apps.clientes.models import Cliente
        from apps.pedidos.models import Pedido
        call_command('seed_demo', stdout=StringIO())
        pedidos, clientes = Pedido.objects.count(), Cliente.objects.count()
        call_command('seed_demo', stdout=StringIO())
        self.assertEqual(Pedido.objects.count(), pedidos)
        self.assertEqual(Cliente.objects.count(), clientes)
        self.assertEqual(Cliente.objects.filter(dni__isnull=True).count(), 0)  # el personal no es cliente
        self.assertTrue(all(c.cantidad_telefonos() >= 2 for c in Cliente.objects.all()))
        self.assertTrue(all(c.email_display() for c in Cliente.objects.all()))  # todos con correo
        self.assertTrue(Cliente.objects.filter(email_contacto='hugo.fernandez@correo.demo').exists())
        # Las instituciones de demo se cargan con un solo nombre.
        escuela = Cliente.objects.get(dni='30711013')
        self.assertTrue(escuela.es_institucion)
        self.assertEqual(escuela.apellido_nombre(), 'Escuela N° 1234 Sarmiento')
        self.assertEqual(Cliente.objects.filter(es_institucion=True).count(), 3)
        # Como en el checkout, todo pedido sin cobrar (web o armado por la empresa)
        # tiene un pago por verificar.
        sin_cobrar = [p for p in Pedido.objects.exclude(estado__in=['Entregado', 'Cancelado'])
                      if p.saldo_pendiente() > 0]
        self.assertTrue(any(p.origen == 'ADMIN' for p in sin_cobrar))
        self.assertTrue(all(p.pago_por_verificar() for p in sin_cobrar))
        # Y los entregados no quedan con un pago pendiente colgado.
        self.assertFalse(any(p.pago_por_verificar() for p in Pedido.objects.filter(estado='Entregado')))
        self.assertFalse(any(p.estado == 'Entregado' and not p.esta_pagado() for p in Pedido.objects.all()))



class HojaDeRutaUXTests(TestCase):
    """Rediseño de la hoja: paradas con pedido, orden automático, carga y regreso de botellones."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        from apps.empleados.models import Empleado, RolEmpleado
        from apps.productos.models import Producto
        self.admin = get_user_model().objects.create_superuser('root', 'root@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(self.admin)
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        self.barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        self.envase = Producto.objects.create(nombre='Envase bidón', descripcion='', precio=Decimal('9000'),
                                              stock=100, es_envase=True, es_retornable=True)
        self.bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'), stock=40,
                                             es_botellon=True, es_retornable=True, envase=self.envase)
        Producto.objects.create(nombre='Gaseosa', descripcion='', precio=Decimal('900'), stock=10)
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        self.direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='10', barrio=self.barrio)
        self.hoja = HojaRuta.objects.create(fecha=date(2026, 10, 21), zona=self.zona)
        rol = RolEmpleado.objects.create(nombre='Chofer', grupo_permisos='Repartidor')
        self.chofer = Empleado.objects.create(nombre='Ramón', apellido='Acosta', dni='1', rol=rol)
        self.camion = Camion.objects.create(patente='AD123CD', capacidad_botellones=100)

    def _agregar(self, **datos):
        return self.client.post(reverse('apps.logistica:agregar_parada', args=[self.hoja.pk]),
                                {'producto': self.bidon.pk, 'cantidad': 2, **datos})

    def test_no_se_agregan_paradas_vacias(self):
        self._agregar(direccion='')
        self._agregar(direccion='', nombre='Sin dirección')
        self.assertEqual(self.hoja.detalles.count(), 0)

    def test_parada_con_cliente_nuevo_y_orden_automatico(self):
        self._agregar(direccion=self.direccion.pk)
        self._agregar(direccion='', nombre='Kiosco Pepe', calle='Belgrano', altura='300', barrio=self.barrio.pk, cantidad=4)
        paradas = list(self.hoja.detalles.order_by('orden'))
        self.assertEqual([p.orden for p in paradas], [1, 2])
        self.assertEqual(paradas[1].cliente.nombre, 'Kiosco Pepe')
        self.assertEqual(paradas[1].cantidad_bidones, 4)
        self.assertEqual(paradas[1].pedido.total, Decimal('12000'))
        # Borrar la primera renumera.
        self.client.post(reverse('apps.logistica:eliminar_parada', args=[paradas[0].pk]))
        self.assertEqual(list(self.hoja.detalles.values_list('orden', flat=True)), [1])

    def test_pedido_de_la_parada_se_edita_en_la_subfila(self):
        self._agregar(direccion=self.direccion.pk)
        parada = self.hoja.detalles.get()
        self.client.post(reverse('apps.logistica:pedido_parada', args=[parada.pk]), {f'botellon_{self.bidon.pk}': 5})
        parada.refresh_from_db()
        self.assertEqual(parada.cantidad_bidones, 5)
        self.assertEqual(parada.resumen_pedido(), '5 × Bidón 20 L')
        respuesta = self.client.get(reverse('apps.logistica:ver_ruta', args=[self.hoja.pk]))
        self.assertContains(respuesta, 'Guardar pedido')
        self.assertContains(respuesta, 'Mitre 10')  # la dirección ya no sale vacía

    def test_pedido_web_no_se_modifica_desde_la_hoja(self):
        web = Pedido.objects.create(cliente=self.cliente, direccion_entrega=self.direccion, origen='WEB',
                                    estado='Confirmado', metodo_pago=MetodoPago.objects.get(codigo='EFECTIVO'))
        DetallePedido.objects.create(pedido=web, producto=self.bidon, precio_unitario=self.bidon.precio,
                                     cantidad=3, subtotal=self.bidon.precio * 3)
        self.client.post(reverse('apps.logistica:agregar_pedido_parada', args=[self.hoja.pk]), {'pedido_id': web.pk})
        parada = self.hoja.detalles.get()
        self.assertEqual(parada.cantidad_bidones, 3)
        self.client.post(reverse('apps.logistica:pedido_parada', args=[parada.pk]), {f'botellon_{self.bidon.pk}': 9})
        parada.refresh_from_db()
        self.assertEqual(parada.cantidad_bidones, 3)

    def test_confirmar_muestra_lo_encargado_y_asigna_equipo(self):
        self._agregar(direccion=self.direccion.pk, cantidad=6)
        respuesta = self.client.get(reverse('apps.logistica:confirmar_ruta', args=[self.hoja.pk]))
        nombres = [f['producto'].nombre for f in respuesta.context['productos']]
        self.assertEqual(nombres, ['Bidón 20 L', 'Envase bidón'])  # sólo llenos y vacíos
        self.assertEqual(respuesta.context['productos'][0]['cantidad'], 6)
        self.client.post(reverse('apps.logistica:confirmar_ruta', args=[self.hoja.pk]), {
            'empleado': self.chofer.pk, 'camion': self.camion.pk, f'cantidad_producto_{self.bidon.pk}': 6})
        self.hoja.refresh_from_db()
        self.assertEqual((self.hoja.estado, self.hoja.empleado, self.hoja.camion), ('Confirmada', self.chofer, self.camion))

    def test_regreso_con_vacios_ajusta_el_stock_del_envase(self):
        self._agregar(direccion=self.direccion.pk, cantidad=2)
        self.client.post(reverse('apps.logistica:confirmar_ruta', args=[self.hoja.pk]), {f'cantidad_producto_{self.bidon.pk}': 3})
        parada = self.hoja.detalles.get()
        registrar_entrega(parada, 'Entregado', envases_retirados=2)  # +2 al envase
        respuesta = self.client.get(reverse('apps.logistica:registrar_regreso_ruta', args=[self.hoja.pk]))
        self.assertEqual(respuesta.context['cargas'][0]['entregado'], 2)
        carga = self.hoja.cargas.get()
        self.client.post(reverse('apps.logistica:registrar_regreso_ruta', args=[self.hoja.pk]),
                         {f'entregada_{carga.pk}': 2, 'vacios_recibidos': 3})
        self.envase.refresh_from_db(); self.bidon.refresh_from_db(); self.hoja.refresh_from_db()
        self.assertEqual(self.envase.stock, 103)   # 100 + 2 de la parada + 1 de diferencia
        self.assertEqual(self.bidon.stock, 38)     # 40 − 3 cargados + 1 que volvió lleno
        self.assertEqual((self.hoja.estado, self.hoja.vacios_recibidos), ('Cerrada', 3))

    def test_reprogramar_registra_la_hora(self):
        self._agregar(direccion=self.direccion.pk)
        parada = self.hoja.detalles.get()
        registrar_entrega(parada, 'Reprogramado')
        parada.refresh_from_db()
        self.assertIsNotNone(parada.hora_registro)

    def test_planificar_asigna_camion_y_repartidor(self):
        self.cliente.es_frecuente = True
        self.cliente.cantidad_recurrente_default = 2
        self.cliente.save()
        url = reverse('apps.logistica:planificar_reparto')
        self.client.post(url, {'fecha': '2026-10-22', 'zona': self.zona.pk, 'confirmar': '1',
                               'empleado': self.chofer.pk, 'camion': self.camion.pk,
                               f'frecuente_{self.cliente.pk}': 'on', f'cantidad_frecuente_{self.cliente.pk}': 3,
                               f'producto_frecuente_{self.cliente.pk}': self.bidon.pk})
        hoja = HojaRuta.objects.get(fecha=date(2026, 10, 22))
        self.assertEqual((hoja.empleado, hoja.camion, hoja.total_botellones()), (self.chofer, self.camion, 3))



class RecorridoRepartidorTests(TestCase):
    """El repartidor confirma cada entrega desde su recorrido del día."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        from django.contrib.auth.models import Group
        from apps.clientes.models import TelefonoContacto
        from apps.empleados.models import Empleado, RolEmpleado
        from apps.productos.models import Producto
        from .services import agregar_parada
        Usuario = get_user_model()
        self.hoy = timezone.localdate()
        self.usuario = Usuario.objects.create_user('chofer', 'ch@x.com', 'Agua-Lluvia-2026')
        self.usuario._es_empleado = True
        rol = RolEmpleado.objects.create(nombre='Chofer', grupo_permisos='Repartidor')
        self.empleado = Empleado.objects.create(usuario=self.usuario, nombre='Ramón', apellido='Acosta', dni='9', rol=rol)
        zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        barrio = Barrio.objects.create(nombre='Centro', zona=zona)
        envase = Producto.objects.create(nombre='Envase', descripcion='', precio=Decimal('9000'), stock=50, es_envase=True)
        self.bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'), stock=40,
                                             es_botellon=True, es_retornable=True, envase=envase)
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz', tipo_cliente='Premium')
        TelefonoContacto.objects.create(cliente=self.cliente, numero='3624111111', desc_relacion='Titular', es_principal=True)
        direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='10', barrio=barrio,
                                                    desc_seguridad='Perro suelto', coordenadas='-27.45,-58.98')
        self.hoja = HojaRuta.objects.create(fecha=self.hoy, zona=zona, empleado=self.empleado)
        self.parada = agregar_parada(self.hoja, self.cliente, direccion, {self.bidon.pk: 2})
        confirmar_hoja(self.hoja, None, [{'producto_id': self.bidon.pk, 'cantidad': 2}])
        self.client.force_login(self.usuario)
        self.url = reverse('apps.logistica:confirmar_entrega', args=[self.parada.pk])

    def test_recorrido_muestra_la_siguiente_parada_con_mapa_telefono_y_nota(self):
        respuesta = self.client.get(reverse('apps.logistica:mi_ruta_hoy'))
        self.assertContains(respuesta, 'Siguiente parada')
        self.assertContains(respuesta, 'tel:3624111111')
        self.assertContains(respuesta, 'google.com/maps')
        self.assertContains(respuesta, 'Perro suelto')  # RNF-02: es el repartidor asignado
        self.assertContains(respuesta, '$6000')

    def test_entregado_y_pagado(self):
        efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.client.post(self.url, {'resultado': 'entregado', 'envases_retirados': 2, 'cobro': 'total',
                                    'metodo_pago': efectivo.pk})
        self.parada.refresh_from_db()
        self.assertEqual(self.parada.estado, 'Entregado')
        # Queda pendiente hasta que el administrador cuente el efectivo.
        pedido = self.parada.pedido
        self.assertFalse(pedido.esta_pagado())
        self.assertEqual(pedido.pago_por_verificar().monto, Decimal('6000'))
        self.assertEqual(pedido.saldo_por_cobrar(), 0)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.bidones_prestados, 0)  # +2 prestados, −2 retirados
        from .services import resumen_recorrido
        self.assertEqual(resumen_recorrido(self.hoja)['efectivo'], Decimal('6000'))  # para rendir
        resolver_pago_pendiente(pedido, aprobar=True)
        self.assertTrue(pedido.esta_pagado())

    def test_pago_parcial_y_a_cuenta(self):
        efectivo = MetodoPago.objects.get(codigo='EFECTIVO')
        self.client.post(self.url, {'resultado': 'entregado', 'envases_retirados': 0, 'cobro': 'parcial',
                                    'monto': '2000', 'metodo_pago': efectivo.pk})
        pedido = self.parada.pedido
        self.assertEqual(pedido.saldo_por_cobrar(), Decimal('4000'))
        self.client.post(self.url, {'resultado': 'entregado', 'envases_retirados': 0, 'cobro': 'cuenta'})
        self.assertEqual(pedido.saldo_pendiente(), Decimal('2000'))   # los 2000 en efectivo, por aprobar
        resolver_pago_pendiente(pedido, aprobar=True)
        self.assertTrue(pedido.esta_pagado())
        self.assertEqual(self.cliente.cuenta_corriente.saldo, Decimal('4000'))

    def test_no_se_pudo_entregar(self):
        self.client.post(self.url, {'resultado': 'problema', 'motivo': 'No había nadie', 'accion': 'reprogramar'})
        self.parada.refresh_from_db()
        self.assertEqual(self.parada.estado, 'Reprogramado')
        self.assertIn('No había nadie', self.parada.nota_entrega)
        self.assertIsNotNone(self.parada.hora_registro)
        self.assertEqual(self.parada.pedido.total_pagado(), 0)

    def test_otro_repartidor_no_puede_confirmar(self):
        from django.contrib.auth import get_user_model
        otro = get_user_model().objects.create_user('otro', 'o@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(otro)
        self.client.post(self.url, {'resultado': 'entregado', 'cobro': 'ninguno'})
        self.parada.refresh_from_db()
        self.assertEqual(self.parada.estado, 'Pendiente')

    def test_hoja_en_borrador_no_admite_entregas(self):
        from .services import agregar_parada
        borrador = HojaRuta.objects.create(fecha=self.hoy, zona=self.hoja.zona, empleado=self.empleado)
        parada = agregar_parada(borrador, self.cliente, self.parada.direccion_entrega, {self.bidon.pk: 1})
        self.client.post(reverse('apps.logistica:confirmar_entrega', args=[parada.pk]),
                         {'resultado': 'entregado', 'cobro': 'ninguno'})
        parada.refresh_from_db()
        self.assertEqual(parada.estado, 'Pendiente')



class CuentaDeRepartidorTests(TestCase):
    """El repartidor no compra en la tienda; trabaja desde su recorrido."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        from apps.empleados.models import Empleado, RolEmpleado
        Usuario = get_user_model()
        self.usuario = Usuario.objects.create_user('ramon', 'r@x.com', 'Agua-Lluvia-2026')  # la señal le crea perfil de cliente
        rol = RolEmpleado.objects.create(nombre='Chofer', grupo_permisos='Repartidor')
        Empleado.objects.create(usuario=self.usuario, nombre='Ramón', apellido='Acosta', dni='77', rol=rol)

    def test_alta_de_empleado_quita_el_perfil_de_cliente_vacio(self):
        self.assertFalse(Cliente.objects.filter(usuario=self.usuario).exists())

    def test_no_accede_a_la_tienda_de_clientes(self):
        self.client.force_login(self.usuario)
        destino = reverse('apps.logistica:mi_ruta_hoy')
        for nombre in ('apps.carrito:ver_carrito', 'apps.pedidos:checkout', 'apps.pedidos:mis_pedidos',
                       'apps.clientes:mi_perfil'):
            respuesta = self.client.get(reverse(nombre))
            self.assertRedirects(respuesta, destino, fetch_redirect_response=False, msg_prefix=nombre)
        inicio = self.client.get(reverse('inicio'))
        self.assertNotContains(inicio, 'Mi Carrito')
        self.assertContains(inicio, 'Mi recorrido')

    def test_al_ingresar_va_a_su_recorrido(self):
        respuesta = self.client.post(reverse('apps.autenticacion:ingresar'),
                                     {'username': 'ramon', 'password': 'Agua-Lluvia-2026'})
        self.assertEqual(respuesta.url, reverse('apps.logistica:mi_ruta_hoy'))


class PedidoEspontaneoTests(TestCase):
    """El repartidor agrega una venta durante el reparto."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        from apps.empleados.models import Empleado, RolEmpleado
        from apps.productos.models import Producto
        from .services import agregar_parada
        Usuario = get_user_model()
        self.usuario = Usuario.objects.create_user('ramon', 'r@x.com', 'Agua-Lluvia-2026')
        rol = RolEmpleado.objects.create(nombre='Chofer', grupo_permisos='Repartidor')
        self.empleado = Empleado.objects.create(usuario=self.usuario, nombre='Ramón', apellido='Acosta', dni='77', rol=rol)
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        self.barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        self.envase = Producto.objects.create(nombre='Envase', descripcion='', precio=Decimal('9000'), stock=50, es_envase=True)
        self.bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'), stock=40,
                                             es_botellon=True, es_retornable=True, envase=self.envase)
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz', tipo_cliente='Premium')
        self.direccion = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='1', barrio=self.barrio)
        self.hoja = HojaRuta.objects.create(fecha=timezone.localdate(), zona=self.zona, empleado=self.empleado)
        agregar_parada(self.hoja, self.cliente, self.direccion, {self.bidon.pk: 2})
        confirmar_hoja(self.hoja, None, [{'producto_id': self.bidon.pk, 'cantidad': 6}])  # 2 encargados + 4 extra
        self.client.force_login(self.usuario)
        self.url = reverse('apps.logistica:venta_calle', args=[self.hoja.pk])

    def _vender(self, **datos):
        return self.client.post(self.url, {f'cantidad_producto_{self.bidon.pk}': 2, 'cobro': 'total',
                                           'metodo_pago': MetodoPago.objects.get(codigo='EFECTIVO').pk, **datos})

    def test_cliente_nuevo_sin_direccion_se_rechaza(self):
        self._vender(nombre='Kiosco')
        self.assertEqual(self.hoja.detalles.count(), 1)

    def test_venta_a_cliente_nuevo_queda_entregada_y_cobrada(self):
        self._vender(nombre='Kiosco Pepe', calle='Belgrano', altura='300', barrio=self.barrio.pk, envases_retirados=1)
        parada = self.hoja.detalles.get(orden=2)
        self.assertEqual((parada.estado, parada.pedido.origen, parada.cantidad_bidones), ('Entregado', 'REPARTIDOR', 2))
        self.assertEqual(parada.pedido.saldo_por_cobrar(), 0)       # cobrada, por aprobar
        resolver_pago_pendiente(parada.pedido, aprobar=True)
        self.assertTrue(parada.pedido.esta_pagado())
        self.assertEqual(parada.cliente.bidones_prestados, 1)  # 2 prestados − 1 retirado

    def test_lo_que_salio_en_el_camion_no_se_descuenta_dos_veces(self):
        self._vender(direccion=self.direccion.pk)
        self.bidon.refresh_from_db()
        self.assertEqual(self.bidon.stock, 34)  # 40 − 6 cargados; la venta sale del camión
        registrar_entrega(self.hoja.detalles.get(orden=1), 'Entregado')
        from .services import entregados_por_producto
        entregados = entregados_por_producto(self.hoja)[self.bidon.pk]
        self.assertEqual(entregados, 4)  # 2 del pedido + 2 de la venta en la calle
        carga = self.hoja.cargas.get()
        registrar_regreso(self.hoja, [{'carga_id': carga.pk, 'cantidad_entregada': entregados}])  # vuelven 6 − 4 = 2
        self.bidon.refresh_from_db()
        self.assertEqual(self.bidon.stock, 36)  # 40 − 4 entregados

    def test_cliente_con_fiado_puede_quedar_a_cuenta(self):
        self._vender(direccion=self.direccion.pk, cobro='cuenta')
        self.assertEqual(self.cliente.cuenta_corriente.saldo, Decimal('6000'))

    def test_primero_se_elige_la_zona_y_filtra_clientes_y_barrios(self):
        otra = Zona.objects.create(nombre='Sur', dias_reparto='2')
        barrio_sur = Barrio.objects.create(nombre='Santa Inés', zona=otra)
        respuesta = self.client.get(self.url)
        self.assertEqual(set(respuesta.context['zonas']), {self.zona, otra})
        html = respuesta.content.decode()
        self.assertIn(f'value="{self.zona.pk}" selected', html)  # la zona de la hoja viene elegida
        self.assertIn(f'data-zona="{otra.pk}">Santa Inés', html)  # barrios marcados por zona
        self.assertIn(f'data-zona="{self.zona.pk}" data-fiado', html)  # clientes marcados por zona
        # Un cliente nuevo de otra zona se registra igual.
        self._vender(nombre='Kiosco Sur', calle='Lavalle', altura='9', barrio=barrio_sur.pk)
        self.assertEqual(self.hoja.detalles.get(orden=2).direccion_entrega.barrio, barrio_sur)

    def test_la_venta_es_un_extra_y_no_cuenta_como_parada(self):
        from .services import resumen_recorrido
        self._vender(direccion=self.direccion.pk)
        self.assertEqual(self.hoja.total_paradas(), 1)          # sólo la planificada
        self.assertEqual(self.hoja.paradas_entregadas(), 0)     # la venta no adelanta el recorrido
        self.assertEqual(self.hoja.porcentaje_completado(), 0)
        self.assertEqual(self.hoja.total_botellones(), 2)
        resumen = resumen_recorrido(self.hoja)
        self.assertEqual((resumen['extras'], resumen['botellones_extras']), (1, 2))
        respuesta = self.client.get(reverse('apps.logistica:mi_ruta_hoy') + f'?hoja={self.hoja.pk}')
        self.assertContains(respuesta, 'data-tab="tab-extras">1<')       # pestaña Extras
        self.assertContains(respuesta, 'data-tab="tab-pendientes">1<')   # la planificada sigue pendiente
        self.assertContains(respuesta, 'data-tab="tab-entregados">0<')   # la venta no cuenta como entrega del recorrido
        self.assertContains(respuesta, 'Siguiente parada')
        self.assertContains(respuesta, 'id="buscar-parada"')

    def test_no_se_vende_con_la_hoja_en_borrador(self):
        borrador = HojaRuta.objects.create(fecha=timezone.localdate(), zona=self.zona, empleado=self.empleado)
        self.client.post(reverse('apps.logistica:venta_calle', args=[borrador.pk]),
                         {f'cantidad_producto_{self.bidon.pk}': 1, 'direccion': self.direccion.pk})
        self.assertFalse(borrador.detalles.exists())


class InventarioCamionTests(TestCase):
    """El repartidor sabe qué lleva el camión: llenos, pedidos, libres y vacíos."""

    def setUp(self):
        from apps.productos.models import Producto
        from .services import agregar_parada
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        self.envase = Producto.objects.create(nombre='Envase', descripcion='', precio=Decimal('9000'), stock=50, es_envase=True)
        self.bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'), stock=40,
                                             es_botellon=True, es_retornable=True, envase=self.envase)
        self.hoja = HojaRuta.objects.create(fecha=timezone.localdate(), zona=self.zona)
        self.paradas = []
        for n, cantidad in ((1, 3), (2, 2)):
            cliente = Cliente.objects.create(nombre=f'Cliente {n}', apellido='X', tipo_cliente='Premium')
            direccion = DireccionEntrega.objects.create(cliente=cliente, calle='Mitre', altura=str(n), barrio=barrio)
            self.paradas.append(agregar_parada(self.hoja, cliente, direccion, {self.bidon.pk: cantidad}))
        confirmar_hoja(self.hoja, None, [{'producto_id': self.bidon.pk, 'cantidad': 8},
                                         {'producto_id': self.envase.pk, 'cantidad': 2}])

    def test_cuentas_del_camion_durante_el_reparto(self):
        from .services import inventario_camion
        c = inventario_camion(self.hoja)
        self.assertEqual((c['en_camion'], c['pendientes'], c['libres'], c['vacios']), (8, 5, 3, 2))
        registrar_entrega(self.paradas[0], 'Entregado', envases_retirados=3)
        c = inventario_camion(self.hoja)
        self.assertEqual((c['en_camion'], c['pendientes'], c['libres'], c['vacios']), (5, 2, 3, 5))
        crear_venta_calle(self.hoja, {'nombre': 'Kiosco', 'calle': 'Belgrano', 'altura': '1',
                                      'barrio_id': Barrio.objects.first().pk,
                                      'productos': [{'producto_id': self.bidon.pk, 'cantidad': 4}]})
        c = inventario_camion(self.hoja)
        self.assertEqual((c['en_camion'], c['pendientes'], c['libres'], c['faltan']), (1, 2, -1, 1))

    def test_venta_de_producto_no_cargado_respeta_el_stock_del_deposito(self):
        from apps.productos.models import Producto
        otro = Producto.objects.create(nombre='Bidón 12 L', descripcion='', precio=Decimal('2000'), stock=2,
                                       es_botellon=True, es_retornable=True, envase=self.envase)
        with self.assertRaisesMessage(ValueError, 'Hay 2 Bidón 12 L en stock'):
            crear_venta_calle(self.hoja, {'nombre': 'Kiosco', 'calle': 'Belgrano', 'altura': '1',
                                          'barrio_id': Barrio.objects.first().pk,
                                          'productos': [{'producto_id': otro.pk, 'cantidad': 3}]})
        otro.refresh_from_db()
        self.assertEqual(otro.stock, 2)

    def test_no_se_vende_mas_de_lo_que_hay_en_el_camion(self):
        with self.assertRaises(ValueError):
            crear_venta_calle(self.hoja, {'nombre': 'Kiosco', 'calle': 'Belgrano', 'altura': '1',
                                          'barrio_id': Barrio.objects.first().pk,
                                          'productos': [{'producto_id': self.bidon.pk, 'cantidad': 9}]})


class HojaRutaZonaYLimitesTests(TestCase):
    """La hoja de ruta se arma con una zona y la base rechaza textos demasiado largos."""

    def test_formulario_muestra_y_exige_zona(self):
        from django.utils import timezone
        from .forms import HojaRutaForm
        zona = Zona.objects.create(nombre='Centro')
        form = HojaRutaForm(data={'fecha': timezone.localdate(), 'estado': 'Borrador'})
        self.assertIn('zona', form.fields)
        self.assertFalse(form.is_valid())
        self.assertIn('zona', form.errors)
        form = HojaRutaForm(data={'fecha': timezone.localdate(), 'estado': 'Borrador', 'zona': zona.pk})
        self.assertTrue(form.is_valid(), form.errors)

    def test_base_rechaza_nombre_de_mas_de_64(self):
        from django.db import IntegrityError, transaction
        with self.assertRaises(IntegrityError), transaction.atomic():
            Zona.objects.create(nombre='x' * 65)


class EliminarBorradorRutaTests(TestCase):
    """Las hojas de ruta en Borrador se pueden eliminar; las confirmadas no."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        admin = get_user_model().objects.create_superuser('jefe_r', 'jr@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(admin)
        self.zona = Zona.objects.create(nombre='Centro')

    def test_borrador_se_elimina_con_sus_paradas(self):
        hoja = HojaRuta.objects.create(fecha=date(2026, 3, 6), zona=self.zona, estado='Borrador')
        DetalleHojaRuta.objects.create(hoja_ruta=hoja, orden=1, cantidad_bidones=1)
        self.client.post(reverse('apps.logistica:eliminar_ruta', args=[hoja.pk]))
        self.assertFalse(HojaRuta.objects.filter(pk=hoja.pk).exists())
        self.assertFalse(DetalleHojaRuta.objects.filter(hoja_ruta_id=hoja.pk).exists())
        # Baja lógica: sigue guardada y se puede restaurar
        self.assertTrue(HojaRuta.todos.filter(pk=hoja.pk, eliminado=True).exists())
        self.client.post(reverse('apps.logistica:restaurar_ruta', args=[hoja.pk]))
        self.assertTrue(HojaRuta.objects.filter(pk=hoja.pk).exists())
        self.assertEqual(hoja.detalles.count(), 1)

    def test_confirmada_no_se_elimina(self):
        hoja = HojaRuta.objects.create(fecha=date(2026, 3, 6), zona=self.zona, estado='Confirmada')
        self.client.post(reverse('apps.logistica:eliminar_ruta', args=[hoja.pk]))
        self.assertTrue(HojaRuta.objects.filter(pk=hoja.pk).exists())



class BajaLogicaZonaTests(TestCase):
    """Eliminar una zona no la borra: queda en «Zonas eliminadas» y se restaura."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        self.client.force_login(get_user_model().objects.create_superuser('jefe_z', 'jz@x.com', 'Agua-Lluvia-2026'))
        self.zona = Zona.objects.create(nombre='Norte')

    def test_eliminar_y_restaurar(self):
        from .forms import HojaRutaForm
        self.client.post(reverse('apps.logistica:eliminar_zona', args=[self.zona.pk]))
        self.zona.refresh_from_db()
        self.assertTrue(self.zona.eliminada)
        self.assertNotIn(self.zona, HojaRutaForm().fields['zona'].queryset)
        lista = self.client.get(reverse('apps.logistica:listar_zonas'))
        self.assertIn(self.zona, list(lista.context['eliminadas']))
        self.client.post(reverse('apps.logistica:restaurar_zona', args=[self.zona.pk]))
        self.zona.refresh_from_db()
        self.assertFalse(self.zona.eliminada)

    def test_sin_asignar_no_se_elimina(self):
        defecto = Zona.objects.create(nombre='Sin Asignar')
        self.client.post(reverse('apps.logistica:eliminar_zona', args=[defecto.pk]))
        defecto.refresh_from_db()
        self.assertFalse(defecto.eliminada)


class BajaLogicaCamionTests(TestCase):
    def setUp(self):
        from django.contrib.auth import get_user_model
        self.client.force_login(get_user_model().objects.create_superuser('jefe_c', 'jc@x.com', 'Agua-Lluvia-2026'))
        self.camion = Camion.objects.create(patente='AB123CD', capacidad_botellones=50)

    def test_eliminar_y_restaurar(self):
        from .forms import HojaRutaForm
        self.client.post(reverse('apps.logistica:eliminar_camion', args=[self.camion.pk]))
        self.assertFalse(Camion.objects.filter(pk='AB123CD').exists())
        self.assertNotIn('AB123CD', [c.pk for c in HojaRutaForm().fields['camion'].queryset])
        self.client.post(reverse('apps.logistica:restaurar_camion', args=['AB123CD']))
        self.assertTrue(Camion.objects.get(pk='AB123CD').activo)


import shutil as _shutil
import tempfile as _tempfile

from django.core import mail
from django.test import override_settings

_MEDIA_RECIBOS = _tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=_MEDIA_RECIBOS, EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class ReciboCobroEfectivoTests(TestCase):
    """Al cobrar en efectivo en la calle se emite un recibo PDF, se guarda y se manda por correo."""

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        _shutil.rmtree(_MEDIA_RECIBOS, ignore_errors=True)

    def setUp(self):
        RecorridoRepartidorTests.setUp(self)
        self.cliente.email_contacto = 'ana@correo.demo'
        self.cliente.save()
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')

    def _cobrar(self, **datos):
        with self.captureOnCommitCallbacks(execute=True):
            self.client.post(self.url, {'resultado': 'entregado', 'envases_retirados': 0,
                                        'metodo_pago': self.efectivo.pk, **datos})
        return self.parada.pedido

    def test_pago_total_genera_recibo_y_lo_manda_por_correo(self):
        pedido = self._cobrar(cobro='total')
        pago = pedido.pago_por_verificar()
        self.assertTrue(pago.comprobante.name.startswith('comprobantes/'))
        contenido = pago.comprobante.open('rb').read()
        self.assertTrue(contenido.startswith(b'%PDF-1.4'))
        self.assertIn(b'6.000,00', contenido)        # monto pagado
        self.assertIn(b'Ram\xf3n Acosta', contenido)   # quién cobró (WinAnsi)
        self.assertEqual(len(mail.outbox), 1)
        correo = mail.outbox[0]
        self.assertEqual(correo.to, ['ana@correo.demo'])
        self.assertIn('Comprobante de pago', correo.subject)
        nombre, adjunto, tipo = correo.attachments[0]
        self.assertEqual(tipo, 'application/pdf')
        self.assertEqual(adjunto, contenido)

    def test_pago_parcial_recibo_con_el_monto_cobrado_y_saldo(self):
        pedido = self._cobrar(cobro='parcial', monto='2000')
        pago = pedido.pago_por_verificar()
        contenido = pago.comprobante.open('rb').read()
        self.assertIn(b'2.000,00', contenido)
        self.assertIn(b'4.000,00', contenido)        # saldo pendiente
        self.assertIn('$4.000,00', mail.outbox[0].body)

    def test_queda_en_el_historial_del_cliente(self):
        from django.contrib.auth import get_user_model
        pedido = self._cobrar(cobro='total')
        pago = pedido.pago_por_verificar()
        self.client.force_login(get_user_model().objects.create_superuser('jefa', 'j@x.com', 'Agua-Lluvia-2026'))
        respuesta = self.client.get(reverse('apps.clientes:ver_cliente', args=[self.cliente.pk]))
        self.assertContains(respuesta, reverse('apps.pedidos:ver_comprobante', args=[pago.pk]))

    def test_sin_cobro_o_a_cuenta_no_hay_recibo(self):
        pedido = self._cobrar(cobro='ninguno')
        self.assertFalse(any(p.comprobante for p in pedido.pagos.all()))
        self.assertEqual(len(mail.outbox), 0)

    def test_cliente_sin_correo_igual_guarda_el_recibo(self):
        self.cliente.email_contacto = ''
        self.cliente.save()
        pedido = self._cobrar(cobro='total')
        self.assertTrue(pedido.pago_por_verificar().comprobante)
        self.assertEqual(len(mail.outbox), 0)


class CobroSoloEfectivoTests(TestCase):
    """Si el pedido es en efectivo, el repartidor no puede cobrarlo con otro medio."""

    def setUp(self):
        RecorridoRepartidorTests.setUp(self)

    def test_el_formulario_no_ofrece_otros_medios(self):
        respuesta = self.client.get(reverse('apps.logistica:mi_ruta_hoy'))
        self.assertContains(respuesta, 'El cliente eligió pagar en efectivo')
        self.assertNotContains(respuesta, 'Billetera Digital')

    def test_aunque_llegue_otro_medio_se_cobra_en_efectivo(self):
        billetera = MetodoPago.objects.get(codigo='BILLETERA')
        self.client.post(self.url, {'resultado': 'entregado', 'envases_retirados': 0, 'cobro': 'total',
                                    'metodo_pago': billetera.pk})
        pago = self.parada.pedido.pago_por_verificar()
        self.assertEqual(pago.metodo_pago.codigo, 'EFECTIVO')

    def test_pedido_por_transferencia_sigue_mostrando_los_medios(self):
        pedido = self.parada.pedido
        pedido.metodo_pago = MetodoPago.objects.get(codigo='TRANSFERENCIA')
        pedido.save()
        respuesta = self.client.get(reverse('apps.logistica:mi_ruta_hoy'))
        self.assertContains(respuesta, 'Billetera Digital')


class CobroPorAprobarTests(TestCase):
    """Lo que cobra el repartidor queda pendiente hasta que el administrador lo aprueba."""

    def setUp(self):
        RecorridoRepartidorTests.setUp(self)
        self.efectivo = MetodoPago.objects.get(codigo='EFECTIVO')

    def _entregar(self, **datos):
        self.client.post(self.url, {'resultado': 'entregado', 'envases_retirados': 0,
                                    'metodo_pago': self.efectivo.pk, **datos})
        return self.parada.pedido

    def test_corregir_la_parada_no_cobra_dos_veces(self):
        pedido = self._entregar(cobro='total')
        self._entregar(cobro='total')
        self.assertEqual(pedido.pagos.filter(estado_pago='Pendiente').count(), 1)
        self.assertEqual(pedido.saldo_por_cobrar(), 0)

    def test_en_la_gestion_el_entregado_se_ve_pendiente_para_aprobar(self):
        from django.contrib.auth import get_user_model
        pedido = self._entregar(cobro='total')
        self.client.force_login(get_user_model().objects.create_superuser('jefa', 'j@x.com', 'Agua-Lluvia-2026'))
        respuesta = self.client.get(reverse('apps.pedidos:listar_pedidos') + '?estado=Entregado')
        self.assertContains(respuesta, f'action="{reverse("apps.pedidos:cambiar_estado_pago", args=[pedido.pk])}"')

    def test_si_el_administrador_lo_rechaza_vuelve_a_deberse(self):
        pedido = self._entregar(cobro='total')
        resolver_pago_pendiente(pedido, aprobar=False)
        self.assertFalse(pedido.esta_pagado())
        self.assertEqual(pedido.saldo_por_cobrar(), Decimal('6000'))


@override_settings(MEDIA_ROOT=_MEDIA_RECIBOS)
class ParadaYaTransferidaTests(TestCase):
    """Si el cliente ya transfirió y subió el comprobante, el repartidor no le cobra."""

    def setUp(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        RecorridoRepartidorTests.setUp(self)
        pedido = self.parada.pedido
        pedido.metodo_pago = MetodoPago.objects.get(codigo='TRANSFERENCIA')
        pedido.save()
        pedido.pagos.filter(estado_pago='Pendiente').delete()
        PagoPedido.objects.create(pedido=pedido, monto=pedido.total, metodo_pago=pedido.metodo_pago,
                                  estado_pago='Pendiente', referencia_comprobante='Comprobante subido por el cliente',
                                  comprobante=SimpleUploadedFile('t.pdf', b'%PDF-1.4'))
        self.pedido = pedido

    def test_el_recorrido_no_lo_muestra_a_cobrar(self):
        respuesta = self.client.get(reverse('apps.logistica:mi_ruta_hoy'))
        self.assertContains(respuesta, 'Transferencia enviada')
        self.assertNotContains(respuesta, 'Pagó todo')

    def test_al_entregar_no_se_registra_otro_cobro(self):
        self.client.post(self.url, {'resultado': 'entregado', 'envases_retirados': 0, 'cobro': 'total',
                                    'metodo_pago': MetodoPago.objects.get(codigo='EFECTIVO').pk})
        self.parada.refresh_from_db()
        self.assertEqual(self.parada.estado, 'Entregado')
        self.assertEqual(self.pedido.pagos.count(), 1)          # sólo la transferencia, por verificar
        self.assertTrue(self.pedido.pago_por_verificar().comprobante)


class TelefonosEnLaParadaTests(TestCase):
    """La parada muestra todos los teléfonos del cliente, cada uno con su botón «Llamar»."""

    def setUp(self):
        from apps.clientes.models import TelefonoContacto
        RecorridoRepartidorTests.setUp(self)
        self.vecino = TelefonoContacto.objects.create(cliente=self.cliente, numero='3624999888',
                                                      desc_relacion='Vecino')

    def test_lista_cada_telefono_con_su_boton(self):
        respuesta = self.client.get(reverse('apps.logistica:mi_ruta_hoy'))
        self.assertContains(respuesta, 'href="tel:3624111111"')
        self.assertContains(respuesta, 'href="tel:3624999888"')
        self.assertContains(respuesta, 'Vecino')

    def test_primero_los_elegidos_para_el_pedido(self):
        from .views import _ficha_de_parada
        self.parada.pedido.telefonos_contacto.set([self.vecino])
        telefonos = _ficha_de_parada(self.parada, self.usuario)['telefonos']
        self.assertEqual([t['telefono'].numero for t in telefonos], ['3624999888', '3624111111'])
        self.assertEqual([t['elegido'] for t in telefonos], [True, False])



class PromocionesAlPlanificarTests(TestCase):
    """RF-09: los clientes de la zona con bidones de promoción se ofrecen al armar la hoja."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        from apps.productos.models import Producto
        from apps.promociones.models import Promocion
        from apps.promociones.services import vender_promocion
        self.fecha = timezone.localdate()
        self.fecha_txt = self.fecha.isoformat()
        self.client.force_login(get_user_model().objects.create_superuser('jefa', 'j@x.com', 'Agua-Lluvia-2026'))
        self.zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        barrio = Barrio.objects.create(nombre='Centro', zona=self.zona)
        otro = Barrio.objects.create(nombre='Norte', zona=Zona.objects.create(nombre='Norte', dias_reparto='0'))
        self.bidon = Producto.objects.create(nombre='Bidón 20 L', descripcion='', precio=Decimal('3000'), stock=50,
                                             es_botellon=True)
        promo = Promocion.objects.create(nombre='Paga 3, lleva 4', producto=self.bidon, cant_paga=3, cant_lleva=4,
                                         precio=Decimal('9000'))
        self.ana = Cliente.objects.create(nombre='Ana', apellido='Paz')
        self.dir_ana = DireccionEntrega.objects.create(cliente=self.ana, calle='Mitre', altura='1', barrio=barrio,
                                                       es_principal=True)
        vender_promocion(self.ana, promo, fecha=self.fecha)
        lejos = Cliente.objects.create(nombre='Lejos', apellido='Norte')
        DireccionEntrega.objects.create(cliente=lejos, calle='Roca', altura='2', barrio=otro, es_principal=True)
        vender_promocion(lejos, promo, fecha=self.fecha)
        self.url = reverse('apps.logistica:planificar_reparto')

    def _crear(self, cantidad):
        self.client.post(self.url, {
            'fecha': self.fecha_txt, 'zona': self.zona.id_zona, 'confirmar': '1',
            f'frecuente_{self.ana.pk}': 'on', f'direccion_frecuente_{self.ana.pk}': self.dir_ana.pk,
            f'producto_frecuente_{self.ana.pk}': self.bidon.pk, f'cantidad_frecuente_{self.ana.pk}': str(cantidad),
            f'saldo_frecuente_{self.ana.pk}': 'on',
            f'nota_frecuente_{self.ana.pk}': 'Retira bidones de su promoción prepaga.',
        })
        return HojaRuta.objects.get(zona=self.zona, fecha=self.fecha).detalles.get()

    def test_el_borrador_ofrece_solo_los_saldos_de_la_zona(self):
        from .services import construir_borrador
        borrador = construir_borrador(self.fecha, self.zona)
        self.assertEqual([f['cliente'] for f in borrador['promociones']], [self.ana])
        self.assertEqual(borrador['promociones'][0]['cantidad_sugerida'], 4)
        respuesta = self.client.get(self.url, {'fecha': self.fecha_txt, 'zona': self.zona.id_zona})
        self.assertContains(respuesta, 'Bidones de promoción de la zona')
        self.assertContains(respuesta, 'Saldo: 4 × Bidón 20 L')

    def test_cargarlo_usa_el_saldo_y_no_cobra(self):
        from apps.promociones.services import saldo_vigente
        parada = self._crear(4)
        self.assertEqual(parada.cantidad_bidones, 4)
        self.assertEqual(parada.pedido.total, 0)
        self.assertEqual(saldo_vigente(self.ana, self.bidon, fecha=self.fecha), 0)

    def test_si_lleva_mas_que_el_saldo_cobra_la_diferencia(self):
        parada = self._crear(5)
        self.assertEqual(parada.pedido.total, Decimal('3000'))

    def test_quitar_la_parada_devuelve_el_saldo(self):
        from apps.promociones.services import saldo_vigente
        parada = self._crear(4)
        self.client.post(reverse('apps.logistica:eliminar_parada', args=[parada.pk]))
        self.assertEqual(saldo_vigente(self.ana, self.bidon, fecha=self.fecha), 4)

    def test_editar_la_cantidad_recalcula_con_el_saldo(self):
        from apps.promociones.services import saldo_vigente
        from .services import _fijar_botellones
        parada = self._crear(4)
        _fijar_botellones(parada.pedido, {self.bidon.pk: 2})
        self.assertEqual(parada.pedido.total, 0)
        self.assertEqual(saldo_vigente(self.ana, self.bidon, fecha=self.fecha), 2)

    def test_un_frecuente_con_saldo_figura_como_ya_incluido(self):
        from .services import construir_borrador
        self.ana.es_frecuente = True
        self.ana.save()
        borrador = construir_borrador(self.fecha, self.zona)
        self.assertEqual(borrador['promociones'][0]['ya_en'], 'frecuente')
        self.assertEqual(borrador['frecuentes'][0]['saldos'][0]['unidades'], 4)
        respuesta = self.client.get(self.url, {'fecha': self.fecha_txt, 'zona': self.zona.id_zona})
        # Se tilda o destilda desde la sección de promociones (una sola casilla).
        self.assertContains(respuesta, f'name="saldo_frecuente_{self.ana.pk}" id="promo_{self.ana.pk}"')
        self.assertContains(respuesta, f'name="saldo_frecuente_{self.ana.pk}"', count=1)

    def _crear_frecuente(self, usar_saldo):
        datos = {'fecha': self.fecha_txt, 'zona': self.zona.id_zona, 'confirmar': '1',
                 f'frecuente_{self.ana.pk}': 'on', f'direccion_frecuente_{self.ana.pk}': self.dir_ana.pk,
                 f'producto_frecuente_{self.ana.pk}': self.bidon.pk, f'cantidad_frecuente_{self.ana.pk}': '2'}
        if usar_saldo:
            datos[f'saldo_frecuente_{self.ana.pk}'] = 'on'
        self.client.post(self.url, datos)
        return HojaRuta.objects.get(zona=self.zona, fecha=self.fecha).detalles.get()

    def test_frecuente_tildado_usa_el_saldo(self):
        self.ana.es_frecuente = True
        self.ana.save()
        self.assertEqual(self._crear_frecuente(usar_saldo=True).pedido.total, 0)

    def test_frecuente_destildado_no_usa_el_saldo(self):
        from apps.promociones.services import saldo_vigente
        self.ana.es_frecuente = True
        self.ana.save()
        self.assertEqual(self._crear_frecuente(usar_saldo=False).pedido.total, Decimal('6000'))
        self.assertEqual(saldo_vigente(self.ana, self.bidon, fecha=self.fecha), 4)

    def test_bidones_de_promocion_no_superan_el_saldo_pendiente(self):
        self.client.post(self.url, {
            'fecha': self.fecha_txt, 'zona': self.zona.id_zona, 'confirmar': '1',
            f'frecuente_{self.ana.pk}': 'on', f'direccion_frecuente_{self.ana.pk}': self.dir_ana.pk,
            f'producto_frecuente_{self.ana.pk}': self.bidon.pk, f'cantidad_frecuente_{self.ana.pk}': '9',
            f'saldo_frecuente_{self.ana.pk}': 'on', f'solo_saldo_frecuente_{self.ana.pk}': 'on',
        })
        parada = HojaRuta.objects.get(zona=self.zona, fecha=self.fecha).detalles.get()
        self.assertEqual(parada.cantidad_bidones, 4)   # el saldo pendiente, no 9
        self.assertEqual(parada.pedido.total, 0)

    def test_la_cantidad_tiene_tope_en_pantalla(self):
        respuesta = self.client.get(self.url, {'fecha': self.fecha_txt, 'zona': self.zona.id_zona})
        self.assertContains(respuesta, 'max="4"')
        self.assertContains(respuesta, 'de 4 pendientes')
