from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from apps.pedidos.models import DetallePedido, MetodoPago, Pedido

from .forms import ProductoForm
from .models import Categoria, Producto


class EliminarProductoTests(TestCase):
    """«Eliminar» desactiva (no borra) y se puede restaurar; H-27: nunca da error 500."""

    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.producto = Producto.objects.create(
            nombre='Bidón 20L', descripcion='Agua', precio=Decimal('1500'), stock=10
        )

    def _eliminar(self):
        self.client.force_login(self.vendedor)
        return self.client.post(reverse('apps.productos:eliminar_producto', args=[self.producto.pk]))

    def test_eliminar_no_borra_sino_que_desactiva(self):
        self._eliminar()
        self.producto.refresh_from_db()
        self.assertFalse(self.producto.activo)

    def test_eliminado_aparece_en_la_lista_y_se_restaura(self):
        self._eliminar()
        respuesta = self.client.get(reverse('apps.productos:listar_productos_admin'))
        self.assertIn(self.producto, list(respuesta.context['eliminados']))
        self.assertNotIn(self.producto, list(respuesta.context['productos']))
        self.client.post(reverse('apps.productos:restaurar_producto', args=[self.producto.pk]))
        self.producto.refresh_from_db()
        self.assertTrue(self.producto.activo)

    def test_con_pedidos_se_desactiva(self):
        pedido = Pedido.objects.create(
            metodo_pago=MetodoPago.objects.get(codigo='EFECTIVO'), total=Decimal('1500')
        )
        DetallePedido.objects.create(
            pedido=pedido, producto=self.producto, precio_unitario=Decimal('1500'),
            cantidad=1, subtotal=Decimal('1500'),
        )
        respuesta = self._eliminar()
        self.assertEqual(respuesta.status_code, 302)
        self.producto.refresh_from_db()
        self.assertFalse(self.producto.activo)

    def test_inactivo_no_aparece_en_la_tienda(self):
        self.producto.activo = False
        self.producto.save()
        respuesta = self.client.get(reverse('apps.productos:listar_productos'))
        self.assertNotIn(self.producto, list(respuesta.context['productos']))
        detalle = self.client.get(reverse('apps.productos:ver_producto', args=[self.producto.pk]))
        self.assertEqual(detalle.status_code, 404)


class AltaProductoTests(TestCase):
    """El alta desde la pantalla deja el producto activo (el checkbox se muestra marcado)."""

    def test_producto_nuevo_queda_activo(self):
        from apps.productos.models import Categoria
        Usuario = get_user_model()
        vendedor = Usuario.objects.create_user('vend2', 'v2@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.client.force_login(vendedor)
        categoria = Categoria.objects.create(nombre='Agua', descripcion='')
        pantalla = self.client.get(reverse('apps.productos:crear_producto'))
        self.assertContains(pantalla, 'name="activo"')
        envase = Producto.objects.create(nombre='Envase 12 L', precio=1, stock=5, es_envase=True)
        self.client.post(reverse('apps.productos:crear_producto'), {
            'nombre': 'Bidón 12 L', 'descripcion': 'Agua', 'categoria': categoria.pk,
            'precio': '2300', 'stock': 10, 'activo': 'on', 'es_botellon': 'on', 'envase': envase.pk})
        producto = Producto.objects.get(nombre='Bidón 12 L')
        self.assertTrue(producto.activo and producto.es_botellon)
        # Un solo interruptor: el bidón retornable también se recarga en la planta.
        self.assertTrue(producto.es_recargable)

    def test_bidon_retornable_exige_envase(self):
        from apps.productos.forms import ProductoForm
        categoria = Categoria.objects.create(nombre='Agua', descripcion='')
        form = ProductoForm(data={'nombre': 'Bidón 20 L', 'categoria': categoria.pk, 'precio': '3000',
                                  'stock': 0, 'activo': 'on', 'es_botellon': 'on'})
        self.assertFalse(form.is_valid())
        self.assertIn('envase', form.errors)

    def test_sin_bidon_retornable_no_se_recarga(self):
        from apps.productos.forms import ProductoForm
        categoria = Categoria.objects.create(nombre='Vasos', descripcion='')
        form = ProductoForm(data={'nombre': 'Vasos x 100', 'categoria': categoria.pk, 'precio': '900',
                                  'stock': 3, 'activo': 'on'})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertFalse(form.save().es_recargable)


class CategoriasPanelTests(TestCase):
    """Las categorías se gestionan desde el panel, sin el admin de Django."""

    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.cliente = Usuario.objects.create_user('cli', 'c@x.com', 'Agua-Lluvia-2026')
        self.agua = Categoria.objects.create(nombre='Agua', descripcion='')

    def test_vendedor_crea_edita_y_borra(self):
        self.client.force_login(self.vendedor)
        self.client.post(reverse('apps.productos:listar_categorias'), {'nombre': '  Soda  ', 'descripcion': ''})
        soda = Categoria.objects.get(nombre='Soda')
        self.client.post(reverse('apps.productos:editar_categoria', args=[soda.pk]),
                         {'nombre': 'Sodas', 'descripcion': 'Sifones'})
        soda.refresh_from_db()
        self.assertEqual((soda.nombre, soda.descripcion), ('Sodas', 'Sifones'))
        self.client.post(reverse('apps.productos:eliminar_categoria', args=[soda.pk]))
        soda.refresh_from_db()
        self.assertTrue(soda.eliminada)  # baja lógica: no se borra
        lista = self.client.get(reverse('apps.productos:listar_categorias'))
        self.assertNotIn(soda, list(lista.context['categorias']))
        self.assertIn(soda, list(lista.context['eliminadas']))
        self.client.post(reverse('apps.productos:restaurar_categoria', args=[soda.pk]))
        soda.refresh_from_db()
        self.assertFalse(soda.eliminada)

    def test_nombre_repetido_sin_importar_mayusculas(self):
        self.client.force_login(self.vendedor)
        respuesta = self.client.post(reverse('apps.productos:listar_categorias'), {'nombre': 'AGUA'})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Categoria.objects.count(), 1)

    def test_eliminar_categoria_con_productos_no_los_toca(self):
        from apps.productos.forms import ProductoForm
        producto = Producto.objects.create(nombre='Bidón', descripcion='', precio=Decimal('10'), stock=1)
        producto.categoria.add(self.agua)
        self.client.force_login(self.vendedor)
        self.client.post(reverse('apps.productos:eliminar_categoria', args=[self.agua.pk]))
        self.agua.refresh_from_db()
        self.assertTrue(self.agua.eliminada)
        self.assertIn(self.agua, producto.categoria.all())
        self.assertNotIn(self.agua, ProductoForm().fields['categoria'].queryset)

    def test_cliente_no_accede(self):
        self.client.force_login(self.cliente)
        self.client.post(reverse('apps.productos:listar_categorias'), {'nombre': 'Hackeo'})
        self.assertFalse(Categoria.objects.filter(nombre='Hackeo').exists())


class ProductoFormValidacionesTests(TestCase):
    def test_precio_y_stock(self):
        cat = Categoria.objects.create(nombre='Agua', descripcion='')
        base = {'nombre': 'Bidón', 'descripcion': '', 'categoria': cat.pk, 'precio': '100', 'stock': '5'}
        self.assertTrue(ProductoForm(base).is_valid())
        self.assertIn('precio', ProductoForm({**base, 'precio': '0'}).errors)
        self.assertIn('stock', ProductoForm({**base, 'stock': '-1'}).errors)


class CatalogoAgotadosAlFinalTests(TestCase):
    """En la tienda, los productos agotados se listan después de los que tienen stock."""

    def test_agotados_al_final(self):
        Producto.objects.create(nombre='A agotado', descripcion='', precio=Decimal('10'), stock=0)
        Producto.objects.create(nombre='B con stock', descripcion='', precio=Decimal('10'), stock=5)
        Producto.objects.create(nombre='C con stock', descripcion='', precio=Decimal('10'), stock=1)
        respuesta = self.client.get(reverse('apps.productos:listar_productos'))
        nombres = [p.nombre for p in respuesta.context['productos']]
        self.assertEqual(nombres, ['B con stock', 'C con stock', 'A agotado'])


class GenerarEnvaseTests(TestCase):
    """Mini apartado «Envases asociados»: genera el envase vacío y lo asocia a los bidones."""

    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.bidon = Producto.objects.create(
            nombre='Bidón 20 L primera marca', descripcion='Agua', precio=Decimal('1500'),
            stock=10, es_botellon=True, es_recargable=True)
        self.otro = Producto.objects.create(
            nombre='Bidón 20 L segunda marca', descripcion='Agua', precio=Decimal('1200'),
            stock=5, es_botellon=True, es_recargable=True)
        self.url = reverse('apps.productos:envases')
        self.client.force_login(self.vendedor)

    def test_lista_bidones_sin_envase(self):
        respuesta = self.client.get(self.url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context['sin_envase'], [self.bidon, self.otro])

    def test_preselecciona_el_bidon_de_la_url(self):
        respuesta = self.client.get(f'{self.url}?bidon={self.bidon.pk}')
        self.assertContains(respuesta, f'value="{self.bidon.pk}"')
        self.assertEqual(respuesta.context['form'].initial['bidones'], [str(self.bidon.pk)])

    def test_genera_envase_y_lo_asocia(self):
        respuesta = self.client.post(self.url, {
            'nombre': '  Envase   bidón 20 L ', 'precio': '9500', 'stock': '40',
            'bidones': [self.bidon.pk, self.otro.pk]})
        self.assertRedirects(respuesta, self.url)
        envase = Producto.objects.get(es_envase=True)
        self.assertEqual(envase.nombre, 'Envase bidón 20 L')
        self.assertEqual(envase.stock, 40)
        self.assertTrue(envase.es_retornable)
        self.assertEqual(envase.categoria.get().nombre, 'Envases')
        self.bidon.refresh_from_db()
        self.otro.refresh_from_db()
        self.assertEqual(self.bidon.envase, envase)
        self.assertEqual(self.otro.envase, envase)
        # El envase generado ya se puede elegir en el formulario del producto.
        self.assertIn(envase, ProductoForm().fields['envase'].queryset)

    def test_reutiliza_la_categoria_envases(self):
        Categoria.objects.create(nombre='envases', descripcion='')
        self.client.post(self.url, {'nombre': 'Envase 10 L', 'precio': '6000', 'stock': '0'})
        self.assertEqual(Categoria.objects.filter(nombre__iexact='envases').count(), 1)

    def test_no_repite_nombre_ni_acepta_precio_cero(self):
        Producto.objects.create(nombre='Envase bidón 20 L', descripcion='', precio=1, stock=0, es_envase=True)
        respuesta = self.client.post(self.url, {'nombre': 'envase bidón 20 l', 'precio': '0', 'stock': '-1'})
        form = respuesta.context['form']
        self.assertIn('nombre', form.errors)
        self.assertIn('precio', form.errors)
        self.assertIn('stock', form.errors)
        self.assertEqual(Producto.objects.filter(es_envase=True).count(), 1)

    def test_cliente_no_puede_entrar(self):
        cliente = get_user_model().objects.create_user('cli', 'c@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(cliente)
        self.client.post(self.url, {'nombre': 'Envase X', 'precio': '10', 'stock': '1'})
        self.assertFalse(Producto.objects.filter(es_envase=True).exists())


class EliminarEnvaseTests(GenerarEnvaseTests):
    """Eliminar un envase desde «Envases asociados»: sale de ahí y de Stock de bidones."""

    def _envase(self, nombre='Envase 20 L', **extra):
        return Producto.objects.create(nombre=nombre, descripcion='Vacío', precio=Decimal('8500'),
                                       stock=17, es_envase=True, **extra)

    def test_eliminar_y_restaurar(self):
        from apps.planta.services import resumen_stock
        envase = self._envase()
        self.client.post(reverse('apps.productos:eliminar_envase', args=[envase.pk]))
        envase.refresh_from_db()
        self.assertFalse(envase.activo)
        respuesta = self.client.get(self.url)
        self.assertNotIn(envase, list(respuesta.context['envases']))
        self.assertIn(envase, list(respuesta.context['eliminados']))
        self.assertNotIn(envase, [g['envase'] for g in resumen_stock()[0]])
        self.client.post(reverse('apps.productos:restaurar_envase', args=[envase.pk]))
        envase.refresh_from_db()
        self.assertTrue(envase.activo)
        self.assertIn(envase, [g['envase'] for g in resumen_stock()[0]])

    def test_no_se_elimina_si_un_bidon_lo_usa(self):
        envase = self._envase()
        self.bidon.envase = envase
        self.bidon.save()
        self.client.post(reverse('apps.productos:eliminar_envase', args=[envase.pk]))
        envase.refresh_from_db()
        self.assertTrue(envase.activo)

    def test_no_elimina_productos_que_no_son_envases(self):
        respuesta = self.client.post(reverse('apps.productos:eliminar_envase', args=[self.bidon.pk]))
        self.assertEqual(respuesta.status_code, 404)
