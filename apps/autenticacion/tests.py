from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SesionTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')

    def test_cerrar_sesion_por_get_no_desloguea(self):
        """H-31: un simple enlace no puede cerrar la sesión."""
        self.client.force_login(self.usuario)
        self.client.get(reverse('apps.autenticacion:cerrar_sesion'))
        self.assertIn('_auth_user_id', self.client.session)
        self.client.post(reverse('apps.autenticacion:cerrar_sesion'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_ingresar_respeta_next_interno(self):
        """H-37: después del login vuelve a la página pedida."""
        destino = reverse('apps.carrito:ver_carrito')
        respuesta = self.client.post(
            reverse('apps.autenticacion:ingresar') + f'?next={destino}',
            {'username': 'ana', 'password': 'Agua-Lluvia-2026'},
        )
        self.assertEqual(respuesta.url, destino)

    def test_ingresar_ignora_next_externo(self):
        respuesta = self.client.post(
            reverse('apps.autenticacion:ingresar') + '?next=https://sitio-malicioso.example/',
            {'username': 'ana', 'password': 'Agua-Lluvia-2026'},
        )
        self.assertEqual(respuesta.url, reverse('inicio'))
