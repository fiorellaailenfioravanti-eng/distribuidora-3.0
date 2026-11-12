from django.core import mail
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import RegistroUsuarioForm


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


class RecuperarContrasenaTests(TestCase):
    """«Olvidé mi contraseña»: enlace por email y nueva contraseña."""

    def setUp(self):
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')

    def test_flujo_completo(self):
        respuesta = self.client.post(reverse('apps.autenticacion:recuperar'), {'email': 'ANA@x.com'})
        self.assertRedirects(respuesta, reverse('apps.autenticacion:recuperar_enviado'))
        self.assertEqual(len(mail.outbox), 1)
        enlace = next(linea for linea in mail.outbox[0].body.splitlines() if '/auth/recuperar/' in linea)
        ruta = enlace.strip().split('testserver', 1)[1]
        # Django guarda el token en la sesión y redirige a la URL con "set-password".
        respuesta = self.client.get(ruta, follow=True)
        url_form = respuesta.redirect_chain[-1][0]
        respuesta = self.client.post(url_form, {'new_password1': 'Otra-Clave-2026x',
                                                'new_password2': 'Otra-Clave-2026x'})
        self.assertRedirects(respuesta, reverse('apps.autenticacion:recuperar_listo'))
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password('Otra-Clave-2026x'))

    def test_email_desconocido_no_revela_nada(self):
        respuesta = self.client.post(reverse('apps.autenticacion:recuperar'), {'email': 'nadie@x.com'})
        self.assertRedirects(respuesta, reverse('apps.autenticacion:recuperar_enviado'))
        self.assertEqual(len(mail.outbox), 0)


class RegistroValidacionesTests(TestCase):
    def _datos(self, **cambios):
        datos = dict(username='nuevo', email='nuevo@x.com', password1='Clave-Segura-2026x',
                     password2='Clave-Segura-2026x', celular1='3624111222', relacion1='Titular',
                     celular2='3624333444', relacion2='Esposa')
        datos.update(cambios)
        return datos

    def test_email_repetido_en_mayusculas(self):
        get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.assertIn('email', RegistroUsuarioForm(self._datos(email='ANA@X.COM')).errors)

    def test_celular_con_letras(self):
        self.assertIn('celular1', RegistroUsuarioForm(self._datos(celular1='llamame ya')).errors)

    def test_personal_no_es_enviado_al_carrito(self):
        from django.contrib.auth.models import Group
        vendedor = get_user_model().objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        respuesta = self.client.post(
            reverse('apps.autenticacion:ingresar') + '?next=/carrito/',
            {'username': 'vend', 'password': 'Agua-Lluvia-2026'},
        )
        self.assertNotIn('/carrito', respuesta.url)

    def test_usuario_logueado_no_ve_login_ni_registro(self):
        usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(usuario)
        for nombre in ('ingresar', 'registrar'):
            self.assertEqual(self.client.get(reverse(f'apps.autenticacion:{nombre}')).status_code, 302)
