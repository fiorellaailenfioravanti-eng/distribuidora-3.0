from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from apps.pedidos.models import DetallePedido, MetodoPago, Pedido

from .models import Producto


class EliminarProductoTests(TestCase):
    """H-27: un producto con pedidos se desactiva en lugar de dar error 500."""

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

    def test_sin_pedidos_se_borra(self):
        self._eliminar()
        self.assertFalse(Producto.objects.filter(pk=self.producto.pk).exists())

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
