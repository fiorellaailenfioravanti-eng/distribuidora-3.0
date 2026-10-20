from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.productos.models import Producto

from .models import Carrito, ItemCarrito


class CarritoSoloPorPostTests(TestCase):
    """H-31 / H-32: el carrito sólo cambia por POST y no redirige fuera del sitio."""

    def setUp(self):
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.producto = Producto.objects.create(
            nombre='Bidón 20L', descripcion='Agua', precio=Decimal('1500'), stock=5
        )
        self.client.force_login(self.usuario)
        self.url_agregar = reverse('apps.carrito:agregar_al_carrito', args=[self.producto.pk])

    def _cantidad(self):
        item = ItemCarrito.objects.filter(carrito__usuario=self.usuario, producto=self.producto).first()
        return item.cantidad if item else 0

    def test_get_no_agrega(self):
        self.client.get(self.url_agregar)
        self.assertEqual(self._cantidad(), 0)

    def test_post_agrega_y_respeta_stock(self):
        self.client.post(self.url_agregar, {'cantidad': 2})
        self.assertEqual(self._cantidad(), 2)
        self.client.post(self.url_agregar, {'cantidad': 10})
        self.assertEqual(self._cantidad(), 2)

    def test_get_no_vacia(self):
        self.client.post(self.url_agregar, {'cantidad': 1})
        self.client.get(reverse('apps.carrito:vaciar_carrito'))
        self.assertEqual(self._cantidad(), 1)
        self.client.post(reverse('apps.carrito:vaciar_carrito'))
        self.assertEqual(self._cantidad(), 0)

    def test_no_redirige_a_otro_sitio(self):
        respuesta = self.client.post(
            self.url_agregar, {'cantidad': 1}, HTTP_REFERER='https://sitio-malicioso.example/'
        )
        self.assertEqual(respuesta.url, reverse('apps.productos:listar_productos'))

    def test_producto_inactivo_no_se_agrega(self):
        self.producto.activo = False
        self.producto.save()
        respuesta = self.client.post(self.url_agregar, {'cantidad': 1})
        self.assertEqual(respuesta.status_code, 404)
        self.assertFalse(Carrito.objects.filter(usuario=self.usuario, items__isnull=False).exists())
