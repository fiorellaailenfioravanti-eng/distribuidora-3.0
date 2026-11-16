from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from .models import Cliente


class BuscarClientesTests(TestCase):
    """H-22: la búsqueda no rompe con clientes sin cuenta y tolera tildes."""

    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.sin_cuenta = Cliente.objects.create(nombre='Ramón', apellido='Gutiérrez', dni='20111222')
        self.client.force_login(self.vendedor)

    def _buscar(self, q):
        respuesta = self.client.get(reverse('apps.clientes:listar_clientes'), {'q': q})
        self.assertEqual(respuesta.status_code, 200)
        return list(respuesta.context['clientes'])

    def test_encuentra_cliente_sin_cuenta_por_nombre_sin_tildes(self):
        self.assertIn(self.sin_cuenta, self._buscar('ramon gutierrez'))

    def test_encuentra_por_dni(self):
        self.assertIn(self.sin_cuenta, self._buscar('20111222'))

    def test_encuentra_cliente_con_cuenta_por_usuario(self):
        cliente_web = self.vendedor.perfil_cliente
        self.assertIn(cliente_web, self._buscar('vend'))


class AgregarDireccionTests(TestCase):
    def test_cliente_con_direccion_puede_agregar_otra_sin_500(self):
        """Antes daba NameError (`reverse` sin importar); con A-D4 muestra el formulario."""
        from .models import DireccionEntrega
        Usuario = get_user_model()
        vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        direccion = DireccionEntrega.objects.create(cliente=cliente, calle='Mitre', altura='10')
        self.client.force_login(vendedor)
        respuesta = self.client.get(reverse('apps.clientes:agregar_direccion', args=[cliente.pk]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(respuesta.context['form'].initial['es_principal'])


class VariasDireccionesTests(TestCase):
    """RF-03 (decisión A-D4): un cliente puede tener varias direcciones."""

    def setUp(self):
        Usuario = get_user_model()
        self.usuario = Usuario.objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        self.client.force_login(self.usuario)
        self.url = reverse('apps.clientes:agregar_direccion', args=[self.cliente.pk])
        from apps.logistica.models import Barrio, Zona
        self.barrio = Barrio.objects.create(nombre='Centro', ciudad='Resistencia',
                                            zona=Zona.objects.create(nombre='Centro', dias_reparto='0'))

    def _agregar(self, calle, url=None, **extra):
        return self.client.post(url or self.url, {'calle': calle, 'altura': '100', 'ciudad': 'Resistencia',
                                                  'barrio': self.barrio.pk, **extra})

    def test_agrega_una_segunda_direccion(self):
        self._agregar('Mitre')
        self._agregar('Belgrano')
        self.assertEqual(self.cliente.direcciones.count(), 2)

    def test_la_primera_es_principal_y_la_segunda_solo_si_se_marca(self):
        self._agregar('Mitre')
        self._agregar('Belgrano')
        self.assertEqual(self.cliente.direcciones.get(es_principal=True).calle, 'Mitre')
        self._agregar('Urquiza', es_principal='on')
        self.assertEqual(self.cliente.direcciones.get(es_principal=True).calle, 'Urquiza')

    def test_next_externo_se_ignora(self):
        respuesta = self._agregar('Mitre', url=self.url + '?next=https://sitio-malicioso.example/')
        self.assertEqual(respuesta.status_code, 302)
        self.assertNotIn('sitio-malicioso', respuesta.url)


class FiadoPremiumYExcepcionTests(TestCase):
    """RF-05 (decisión A-D6): Premium siempre; Normal sólo como excepción manual."""

    def test_bajar_de_premium_quita_el_fiado(self):
        cliente = Cliente.objects.create(nombre='Ex', apellido='Premium', tipo_cliente='Premium')
        cliente.tipo_cliente = 'Normal'
        cliente.save()
        self.assertFalse(cliente.permite_fiado)

    def test_excepcion_manual_se_conserva(self):
        cliente = Cliente.objects.create(nombre='Nor', apellido='Mal')
        cliente.permite_fiado = True
        cliente.save()
        cliente.notas_internas = 'cliente de confianza'
        cliente.save()
        cliente.refresh_from_db()
        self.assertTrue(cliente.permite_fiado)


class HistorialBidonesTests(TestCase):
    """RF-08: historial de envases y saldo derivado."""

    def setUp(self):
        from datetime import date
        from apps.logistica.models import DetalleHojaRuta, HojaRuta
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        hoja = HojaRuta.objects.create(fecha=date(2026, 10, 20))
        self.parada = DetalleHojaRuta.objects.create(hoja_ruta=hoja, cliente=self.cliente, orden=1, cantidad_bidones=3)

    def test_entrega_registra_prestamo_y_devolucion_sin_duplicar(self):
        from apps.logistica.services import registrar_entrega
        registrar_entrega(self.parada, 'Entregado', envases_retirados=2)
        registrar_entrega(self.parada, 'Entregado', envases_retirados=2)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.bidones_prestados, 1)
        self.assertEqual(self.cliente.movimientos_bidon.count(), 2)

    def test_devolucion_manual_no_deja_saldo_negativo(self):
        from django.core.exceptions import ValidationError
        from .services import registrar_movimiento_bidon
        registrar_movimiento_bidon(self.cliente, 'Prestamo', 2)
        with self.assertRaises(ValidationError):
            registrar_movimiento_bidon(self.cliente, 'Devolucion', 3)
        registrar_movimiento_bidon(self.cliente, 'Ajuste', -1, nota='Conteo físico')
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.bidones_prestados, 1)


class VistaMovimientoBidonTests(TestCase):
    """RF-08: el vendedor registra envases desde la ficha; el cliente no puede."""

    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        self.url = reverse('apps.clientes:registrar_movimiento_bidon', args=[self.cliente.pk])

    def test_vendedor_registra_y_la_ficha_lo_muestra(self):
        self.client.force_login(self.vendedor)
        self.client.post(self.url, {'tipo': 'Prestamo', 'cantidad': 3, 'nota': 'Retiró en el local'})
        self.client.post(self.url, {'tipo': 'Devolucion', 'cantidad': 1})
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.bidones_prestados, 2)
        self.assertContains(self.client.get(reverse('apps.clientes:ver_cliente', args=[self.cliente.pk])), 'Retiró en el local')

    def test_cliente_web_no_registra(self):
        otro = get_user_model().objects.create_user('cli', 'c@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(otro)
        self.client.post(self.url, {'tipo': 'Prestamo', 'cantidad': 3})
        self.assertFalse(self.cliente.movimientos_bidon.exists())


class EditarMiPerfilTests(TestCase):
    """La pantalla «Editar mi perfil» respondía 500 en cualquier envío."""

    def setUp(self):
        from django.contrib.auth import get_user_model
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(self.usuario)
        self.url = reverse('apps.clientes:editar_mi_perfil')

    def test_muestra_los_dos_formularios(self):
        respuesta = self.client.get(self.url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'name="celular"')
        self.assertContains(respuesta, 'name="old_password"')

    def test_actualiza_el_telefono_principal(self):
        respuesta = self.client.post(self.url, {'form_perfil': '1', 'celular': '3624 555666'})
        self.assertRedirects(respuesta, reverse('apps.clientes:mi_perfil'))
        cliente = self.usuario.perfil_cliente
        self.assertTrue(cliente.telefonos.filter(numero='3624 555666').exists())

    def test_rechaza_telefono_con_letras(self):
        respuesta = self.client.post(self.url, {'form_perfil': '1', 'celular': 'llamame'})
        self.assertEqual(respuesta.status_code, 200)

    def test_cambia_la_contrasena(self):
        respuesta = self.client.post(self.url, {
            'form_password': '1', 'old_password': 'Agua-Lluvia-2026',
            'new_password1': 'Otra-Clave-2026x', 'new_password2': 'Otra-Clave-2026x',
        })
        self.assertRedirects(respuesta, reverse('apps.clientes:mi_perfil'))
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password('Otra-Clave-2026x'))


class ValidacionesClienteTests(TestCase):
    def test_dni_y_telefono(self):
        from .forms import ClienteForm
        base = {'nombre': 'Ana', 'apellido': 'Paz', 'tipo_cliente': 'Normal'}
        self.assertTrue(ClienteForm({**base, 'dni': '30123456'}).is_valid())
        self.assertIn('dni', ClienteForm({**base, 'dni': 'abc'}).errors)
        Cliente.objects.create(nombre='Otro', dni='30123456')
        self.assertIn('dni', ClienteForm({**base, 'dni': '30.123.456'}).errors)


class OrdenDirectorioClientesTests(TestCase):
    """Los encabezados ordenan a todos los clientes (no sólo la página visible)."""

    def setUp(self):
        vendedor = get_user_model().objects.create_user('vend_orden', 'vo@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.client.force_login(vendedor)
        for i, nombre in enumerate(['Bruno', 'Ana', 'Carla'] + [f'Zoe{n:02d}' for n in range(10)]):
            Cliente.objects.create(nombre=nombre, apellido='Test', dni=str(40000000 + i))

    def _nombres(self, **params):
        respuesta = self.client.get(reverse('apps.clientes:listar_clientes'), params)
        return [c.nombre for c in respuesta.context['clientes']]

    def test_ordena_por_nombre_en_ambos_sentidos(self):
        self.assertEqual(self._nombres(orden='cliente', dir='asc')[:3], ['Ana', 'Bruno', 'Carla'])
        self.assertEqual(self._nombres(orden='cliente', dir='desc')[0], 'Zoe09')

    def test_la_paginacion_conserva_el_orden(self):
        respuesta = self.client.get(reverse('apps.clientes:listar_clientes'), {'orden': 'cliente', 'dir': 'desc'})
        self.assertContains(respuesta, 'orden=cliente&amp;dir=desc')
        self.assertEqual(self._nombres(orden='cliente', dir='desc', page=2)[-1], 'Ana')


class BajaLogicaClienteTests(TestCase):
    """Eliminar un cliente no lo borra: sale del directorio y de los selectores, y se restaura."""

    def setUp(self):
        Usuario = get_user_model()
        vendedor = Usuario.objects.create_user('vend_baja', 'vb@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.client.force_login(vendedor)
        self.usuario = Usuario.objects.create_user('cli_baja', 'cb@x.com', 'Agua-Lluvia-2026')
        self.cliente = Cliente.objects.get(usuario=self.usuario)

    def test_eliminar_oculta_y_bloquea_la_cuenta(self):
        from apps.abonos.forms import AbonoForm
        self.client.post(reverse('apps.clientes:eliminar_cliente', args=[self.cliente.pk]))
        self.cliente.refresh_from_db()
        self.usuario.refresh_from_db()
        self.assertTrue(self.cliente.eliminado)
        self.assertFalse(self.usuario.is_active)
        lista = self.client.get(reverse('apps.clientes:listar_clientes'))
        self.assertNotIn(self.cliente, list(lista.context['clientes']))
        self.assertIn(self.cliente, list(lista.context['eliminados']))
        self.assertNotIn(self.cliente, AbonoForm().fields['cliente'].queryset)

    def test_el_listado_tiene_boton_eliminar_en_la_fila(self):
        lista = self.client.get(reverse('apps.clientes:listar_clientes'))
        self.assertContains(lista, reverse('apps.clientes:eliminar_cliente', args=[self.cliente.pk]))

    def test_restaurar(self):
        self.cliente.dar_de_baja()
        self.client.post(reverse('apps.clientes:restaurar_cliente', args=[self.cliente.pk]))
        self.cliente.refresh_from_db()
        self.usuario.refresh_from_db()
        self.assertFalse(self.cliente.eliminado)
        self.assertTrue(self.usuario.is_active)


class AltaClienteValidacionesTests(TestCase):
    """Alta por el vendedor: teléfonos validados (uno obligatorio) y largos limitados en la base."""

    def setUp(self):
        vendedor = get_user_model().objects.create_user('vend_alta', 'va@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.client.force_login(vendedor)
        self.url = reverse('apps.clientes:crear_sin_cuenta')

    def test_sin_telefono_no_se_crea(self):
        self.client.post(self.url, {'nombre': 'Rita', 'apellido': 'Gil', 'tipo_cliente': 'Normal'})
        self.assertFalse(Cliente.objects.filter(nombre='Rita').exists())

    def test_telefono_invalido_no_se_crea(self):
        self.client.post(self.url, {'nombre': 'Rita', 'apellido': 'Gil', 'tipo_cliente': 'Normal',
                                    'telefono_numero[]': ['llamame'], 'telefono_relacion[]': ['Titular']})
        self.assertFalse(Cliente.objects.filter(nombre='Rita').exists())

    def test_con_varios_telefonos_se_crea(self):
        self.client.post(self.url, {'nombre': 'Rita', 'apellido': 'Gil', 'tipo_cliente': 'Normal',
                                    'telefono_numero[]': ['3624111111', '3624222222'],
                                    'telefono_relacion[]': ['Titular', 'Hijo']})
        self.assertEqual(Cliente.objects.get(nombre='Rita').telefonos.count(), 2)

    def test_nombre_largo_se_rechaza(self):
        self.client.post(self.url, {'nombre': 'R' * 70, 'apellido': 'Gil', 'tipo_cliente': 'Normal',
                                    'telefono_numero[]': ['3624111111'], 'telefono_relacion[]': ['Titular']})
        self.assertFalse(Cliente.objects.filter(apellido='Gil').exists())

    def test_la_base_rechaza_un_telefono_largo(self):
        from django.db import IntegrityError, transaction
        from .models import TelefonoContacto
        cliente = Cliente.objects.create(nombre='Rita', apellido='Gil')
        with self.assertRaises(IntegrityError), transaction.atomic():
            TelefonoContacto.objects.create(cliente=cliente, numero='1' * 21, desc_relacion='Titular')


class BajaLogicaTelefonoDireccionTests(TestCase):
    def setUp(self):
        from .models import DireccionEntrega, TelefonoContacto
        vendedor = get_user_model().objects.create_user('vend_td', 'vtd@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.client.force_login(vendedor)
        self.cliente = Cliente.objects.create(nombre='Rita', apellido='Gil')
        self.t1 = TelefonoContacto.objects.create(cliente=self.cliente, numero='3624111111', desc_relacion='Titular', es_principal=True)
        self.t2 = TelefonoContacto.objects.create(cliente=self.cliente, numero='3624222222', desc_relacion='Hijo')
        self.dir = DireccionEntrega.objects.create(cliente=self.cliente, calle='Mitre', altura='1', es_principal=True)

    def test_telefono_principal_pasa_al_otro_y_se_restaura(self):
        from .models import TelefonoContacto
        self.client.post(reverse('apps.clientes:eliminar_telefono', args=[self.t1.pk]))
        self.assertEqual(list(self.cliente.telefonos.all()), [self.t2])
        self.t2.refresh_from_db()
        self.assertTrue(self.t2.es_principal)
        self.assertTrue(TelefonoContacto.todos.get(pk=self.t1.pk).eliminado)
        self.client.post(reverse('apps.clientes:restaurar_telefono', args=[self.t1.pk]))
        self.assertEqual(self.cliente.telefonos.count(), 2)

    def test_direccion_eliminada_no_se_ofrece(self):
        self.client.post(reverse('apps.clientes:eliminar_direccion', args=[self.dir.pk]))
        self.assertEqual(self.cliente.direcciones.count(), 0)
        ficha = self.client.get(reverse('apps.clientes:ver_cliente', args=[self.cliente.pk]))
        self.assertIn(self.dir.pk, [d.pk for d in ficha.context['direcciones_eliminadas']])
        self.client.post(reverse('apps.clientes:restaurar_direccion', args=[self.dir.pk]))
        self.assertEqual(self.cliente.direcciones.count(), 1)


class NumeroClienteTests(TestCase):
    """Nro de cliente: los importados conservan el suyo y los nuevos arrancan en 0000001."""

    def test_nuevos_desde_cero_y_respeta_importados(self):
        from .models import Cliente
        importado = Cliente.objects.create(nombre='Leonardo', apellido='Fuentecilla', numero='1003389')
        primero = Cliente.objects.create(nombre='Ana', apellido='Pérez')
        segundo = Cliente.objects.create(nombre='Juan', apellido='Gómez')
        self.assertEqual(importado.numero, '1003389')
        self.assertEqual((primero.numero, segundo.numero), ('0000001', '0000002'))

    def test_saltea_numeros_importados_que_empiezan_con_cero(self):
        from .models import Cliente
        Cliente.objects.create(nombre='Natalia', apellido='Enciso', numero='0000002')
        Cliente.objects.create(nombre='Otra', apellido='Importada', numero='0010059')
        nuevo = Cliente.objects.create(nombre='Ana', apellido='Pérez')
        siguiente = Cliente.objects.create(nombre='Juan', apellido='Gómez')
        self.assertEqual((nuevo.numero, siguiente.numero), ('0000003', '0000004'))
