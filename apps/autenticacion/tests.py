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


class RegistroTelefonosTests(TestCase):
    """RF-01 / H-40: el registro exige dos celulares con su relación."""

    url = None

    def setUp(self):
        self.url = reverse('apps.autenticacion:registrar')
        self.datos = {
            'username': 'nuevo', 'email': 'nuevo@x.com',
            'password1': 'Agua-Lluvia-2026', 'password2': 'Agua-Lluvia-2026',
            'celular1': '3624111111', 'relacion1': 'Titular',
            'celular2': '3624222222', 'relacion2': 'Esposa',
        }

    def test_registro_sin_celulares_se_rechaza(self):
        datos = {k: v for k, v in self.datos.items() if not k.startswith(('celular', 'relacion'))}
        self.client.post(self.url, datos)
        self.assertFalse(get_user_model().objects.filter(username='nuevo').exists())

    def test_celulares_iguales_se_rechazan(self):
        self.client.post(self.url, {**self.datos, 'celular2': '3624111111'})
        self.assertFalse(get_user_model().objects.filter(username='nuevo').exists())

    def test_registro_crea_dos_telefonos_con_la_relacion_declarada(self):
        self.client.post(self.url, self.datos)
        usuario = get_user_model().objects.get(username='nuevo')
        relaciones = set(usuario.perfil_cliente.telefonos.values_list('desc_relacion', flat=True))
        self.assertEqual(relaciones, {'Titular', 'Esposa'})
