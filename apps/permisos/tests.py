"""
Tests de la capa de permisos y roles.

Cubren los hallazgos que motivaron la unificación en `apps/permisos/roles.py`:

  H-1  → Los grupos base existen y tienen permisos asignados.
  H-2  → Solo existe UN modelo `Empleado` y UN `RolEmpleado`.
  H-5  → La pertenencia a un grupo no depende de la posición en la lista.
  RNF-02 → La nota de seguridad se filtra por dirección, no por rol.
"""

from django.contrib.auth.models import Group
from django.test import TestCase

from apps.empleados.models import Empleado, RolEmpleado
from apps.logistica.models import Barrio, Camion, DetalleHojaRuta, HojaRuta, RutaReparto, Zona
from apps.permisos.roles import (
    GRUPO_REPARTIDOR,
    GRUPO_VENDEDOR,
    es_admin_o_vendedor,
    es_admin_vendedor_o_repartidor,
    es_repartidor,
    obtener_empleado,
    puede_ver_nota_seguridad,
)
from apps.clientes.models import Cliente, DireccionEntrega


class GruposBaseTests(TestCase):
    """H-1: los grupos del sistema existen y están correctamente configurados."""

    def test_existen_los_grupos_vendedor_y_repartidor(self):
        self.assertTrue(Group.objects.filter(name=GRUPO_VENDEDOR).exists())
        self.assertTrue(Group.objects.filter(name=GRUPO_REPARTIDOR).exists())

    def test_grupo_vendedor_tiene_permisos_asignados(self):
        grupo = Group.objects.get(name=GRUPO_VENDEDOR)
        self.assertGreater(grupo.permissions.count(), 0)

    def test_grupo_repartidor_tiene_permisos_asignados(self):
        grupo = Group.objects.get(name=GRUPO_REPARTIDOR)
        self.assertGreater(grupo.permissions.count(), 0)

    def test_grupo_vendedor_puede_gestionar_pedidos(self):
        grupo = Group.objects.get(name=GRUPO_VENDEDOR)
        codigos = set(grupo.permissions.values_list('codename', flat=True))
        self.assertIn('add_pedido', codigos)
        self.assertIn('change_cliente', codigos)


class EvaluacionDeRolesTests(TestCase):
    """Verifica `roles.py` contra el grupo real de Django."""

    def setUp(self):
        from apps.autenticacion.models import Usuario

        self.vendedor = Usuario.objects.create_user(
            username='vendedor', password='x', email='vendedor@test.com'
        )
        self.repartidor = Usuario.objects.create_user(
            username='repartidor', password='x', email='repartidor@test.com'
        )
        self.cliente = Usuario.objects.create_user(
            username='comprador', password='x', email='comprador@test.com'
        )

        self.vendedor.groups.add(Group.objects.get(name=GRUPO_VENDEDOR))
        self.repartidor.groups.add(Group.objects.get(name=GRUPO_REPARTIDOR))

    def test_superusuario_es_admin(self):
        from apps.autenticacion.models import Usuario

        root = Usuario.objects.create_superuser(
            username='root', password='x', email='root@test.com'
        )
        self.assertTrue(es_admin_o_vendedor(root))
        self.assertTrue(es_admin_vendedor_o_repartidor(root))

    def test_vendedor_tiene_acceso_de_escritura(self):
        self.assertTrue(es_admin_o_vendedor(self.vendedor))
        self.assertFalse(es_repartidor(self.vendedor))

    def test_repartidor_no_tiene_acceso_de_escritura(self):
        self.assertFalse(es_admin_o_vendedor(self.repartidor))
        self.assertTrue(es_repartidor(self.repartidor))

    def test_repartidor_tiene_acceso_a_logistica(self):
        self.assertTrue(es_admin_vendedor_o_repartidor(self.repartidor))

    def test_cliente_registrado_no_es_personal_interno(self):
        self.assertFalse(es_admin_o_vendedor(self.cliente))
        self.assertFalse(es_repartidor(self.cliente))
        self.assertFalse(es_admin_vendedor_o_repartidor(self.cliente))

    def test_usuario_inactivo_pierde_los_permisos(self):
        self.vendedor.is_active = False
        self.vendedor.save()
        self.assertFalse(es_admin_o_vendedor(self.vendedor))

    def test_pertenencia_no_depende_del_orden_de_grupos(self):
        """
        H-5: el antiguo `user.groups.all.0.name == 'Vendedor'` en los templates
        solo miraba el PRIMER grupo. Con varios grupos el resultado era
        arbitrario. Cualquier orden debe devolver el mismo resultado.
        """
        from apps.autenticacion.models import Usuario

        multi = Usuario.objects.create_user(
            username='multi', password='x', email='multi@test.com'
        )
        # Orden deliberadamente inverso al natural.
        multi.groups.add(
            Group.objects.get(name=GRUPO_REPARTIDOR),
            Group.objects.get(name=GRUPO_VENDEDOR),
        )

        for _ in range(4):
            self.assertTrue(es_admin_o_vendedor(multi))
            self.assertTrue(es_repartidor(multi))


class NotaDeSeguridadTests(TestCase):
    """RNF-02: la nota de acceso al domicilio se filtra por asignación."""

    def setUp(self):
        from apps.autenticacion.models import Usuario

        self.rol = RolEmpleado.objects.create(nombre='Repartidor', grupo_permisos='Repartidor')

        self.admin = Usuario.objects.create_superuser(
            username='admin', password='x', email='admin@test.com'
        )
        self.vendedor = Usuario.objects.create_user(
            username='vend', password='x', email='vend@test.com'
        )
        self.vendedor.groups.add(Group.objects.get(name=GRUPO_VENDEDOR))

        self.repartidor_asignado = Usuario.objects.create_user(
            username='rep_si', password='x', email='repsi@test.com'
        )
        self.repartidor_asignado.groups.add(Group.objects.get(name=GRUPO_REPARTIDOR))

        self.repartidor_ajeno = Usuario.objects.create_user(
            username='rep_no', password='x', email='repno@test.com'
        )
        self.repartidor_ajeno.groups.add(Group.objects.get(name=GRUPO_REPARTIDOR))

        self.domicilio_cliente = Usuario.objects.create_user(
            username='dueno', password='x', email='dueno@test.com'
        )
        # La señal post_save de apps.clientes ya creó el perfil Cliente al
        # crear el Usuario; se reutiliza en lugar de duplicarlo.
        self.cliente = Cliente.objects.get(usuario=self.domicilio_cliente)
        self.cliente.dni = '11111111'
        self.cliente.save(update_fields=['dni'])
        self.direccion = DireccionEntrega.objects.create(
            cliente=self.cliente,
            calle='San Martín',
            altura='450',
            desc_seguridad='Deja el portón abierto.',
        )

        self._crear_hoja_ruta(self.repartidor_asignado)

    def _crear_hoja_ruta(self, usuario_repartidor):
        empleado = Empleado.objects.create(
            usuario=usuario_repartidor,
            nombre='Chofer',
            apellido='Prueba',
            dni='22222222',
            rol=self.rol,
        )
        zona = Zona.objects.create(nombre='Zona Test')
        barrio = Barrio.objects.create(nombre='Barrio Test', zona=zona)
        self.direccion.barrio = barrio
        self.direccion.save()

        camion = Camion.objects.create(patente='AB123CD')
        ruta = RutaReparto.objects.create(nombre='Ruta Test', zona=zona, dia_semana=0)
        self.hoja = HojaRuta.objects.create(
            fecha='2026-09-30',
            ruta_reparto=ruta,
            empleado=empleado,
            camion=camion,
        )
        DetalleHojaRuta.objects.create(
            hoja_ruta=self.hoja,
            orden=1,
            direccion_entrega=self.direccion,
        )
        return empleado

    def test_superusuario_ve_la_nota(self):
        self.assertTrue(puede_ver_nota_seguridad(self.admin, self.direccion))

    def test_vendedor_ve_la_nota(self):
        self.assertTrue(puede_ver_nota_seguridad(self.vendedor, self.direccion))

    def test_repartidor_asignado_ve_la_nota(self):
        self.assertTrue(puede_ver_nota_seguridad(self.repartidor_asignado, self.direccion))

    def test_repartidor_no_asignado_no_ve_la_nota(self):
        """El caso que RNF-02 exige y que el código anterior no cumplía."""
        self.assertTrue(es_repartidor(self.repartidor_ajeno))
        self.assertFalse(puede_ver_nota_seguridad(self.repartidor_ajeno, self.direccion))

    def test_cliente_propietario_no_ve_su_propia_nota(self):
        self.assertFalse(puede_ver_nota_seguridad(self.domicilio_cliente, self.direccion))

    def test_usuario_sin_direccion_no_rompe(self):
        self.assertFalse(puede_ver_nota_seguridad(self.repartidor_ajeno, None))


class ModeloEmpleadoUnicoTests(TestCase):
    """H-2 y H-3: `apps.empleados` es la única fuente de verdad."""

    def test_existe_un_solo_modelo_empleado(self):
        from django.apps import apps as django_apps

        nombres = [
            model._meta.label
            for model in django_apps.get_models()
            if model.__name__ == 'Empleado'
        ]
        self.assertEqual(nombres, ['empleados.Empleado'])

    def test_existe_un_solo_rolempleado(self):
        from django.apps import apps as django_apps

        nombres = [
            model._meta.label
            for model in django_apps.get_models()
            if model.__name__ == 'RolEmpleado'
        ]
        self.assertEqual(nombres, ['empleados.RolEmpleado'])

    def test_hojaruta_apunta_al_empleado_canonico(self):
        campo = HojaRuta._meta.get_field('empleado')
        self.assertEqual(campo.related_model._meta.label, 'empleados.Empleado')

    def test_obtener_empleado_usa_el_related_name_canonico(self):
        from apps.autenticacion.models import Usuario

        usuario = Usuario.objects.create_user(
            username='chofer', password='x', email='chofer@test.com'
        )
        rol = RolEmpleado.objects.create(nombre='Chofer', grupo_permisos='Repartidor')
        empleado = Empleado.objects.create(
            usuario=usuario, nombre='Juan', apellido='Perez',
            dni='33333333', rol=rol,
        )
        self.assertEqual(obtener_empleado(usuario), empleado)

    def test_obtener_empleado_devuelve_none_sin_ficha(self):
        from apps.autenticacion.models import Usuario

        usuario = Usuario.objects.create_user(
            username='sinficha', password='x', email='sinficha@test.com'
        )
        self.assertIsNone(obtener_empleado(usuario))


class AccesoAVistasLogisticasTests(TestCase):
    """Cierra el agujero detectado en `ver_ruta` y `actualizar_estado_entrega`:
    un cliente registrado (sin ningún grupo interno) podía abrir una hoja de
    ruta ajena porque la vista solo validaba el caso "repartidor" y dejaba pasar
    a cualquier otro usuario autenticado."""

    def setUp(self):
        from apps.autenticacion.models import Usuario
        from django.urls import reverse

        self.reverse = reverse
        self.Usuario = Usuario

        self.cliente = Usuario.objects.create_user(
            username='cliente_comun', password='x', email='cliente_comun@test.com'
        )
        self.repartidor = Usuario.objects.create_user(
            username='repartidor_x', password='x', email='repartidor_x@test.com'
        )
        self.repartidor.groups.add(Group.objects.get(name=GRUPO_REPARTIDOR))

        rol = RolEmpleado.objects.create(nombre='Chofer Logistica', grupo_permisos='Repartidor')
        self.empleado = Empleado.objects.create(
            usuario=self.repartidor, nombre='Ana', apellido='Gomez',
            dni='44444444', rol=rol,
        )

        zona = Zona.objects.create(nombre='Zona Log')
        barrio = Barrio.objects.create(nombre='Barrio Log', zona=zona)

        duenio = Usuario.objects.create_user(
            username='duenio_dir', password='x', email='duenio_dir@test.com'
        )
        cliente = Cliente.objects.get(usuario=duenio)
        direccion = DireccionEntrega.objects.create(
            cliente=cliente, calle='Belgrano', altura='100',
            barrio=barrio, desc_seguridad='Llamar al timbre 3B.',
        )

        camion = Camion.objects.create(patente='ZZ999ZZ')
        ruta = RutaReparto.objects.create(nombre='Ruta Log', zona=zona, dia_semana=0)
        self.hoja = HojaRuta.objects.create(
            fecha='2026-09-30', ruta_reparto=ruta,
            empleado=self.empleado, camion=camion,
        )
        self.parada = DetalleHojaRuta.objects.create(
            hoja_ruta=self.hoja, orden=1,
            direccion_entrega=direccion, direccion_texto='Belgrano 100',
        )

    def test_cliente_registrado_no_puede_ver_hoja_de_ruta(self):
        self.client.force_login(self.cliente)
        respuesta = self.client.get(
            self.reverse('apps.logistica:ver_ruta', args=[self.hoja.id_ruta])
        )
        self.assertEqual(respuesta.status_code, 302)

    def test_repartidor_no_asignado_no_puede_ver_hoja_de_ruta(self):
        otro = self.Usuario.objects.create_user(
            username='otro_rep', password='x', email='otro_rep@test.com'
        )
        otro.groups.add(Group.objects.get(name=GRUPO_REPARTIDOR))
        rol = RolEmpleado.objects.create(nombre='Otro chofer', grupo_permisos='Repartidor')
        Empleado.objects.create(
            usuario=otro, nombre='Leo', apellido='Diaz', dni='55555555', rol=rol,
        )

        self.client.force_login(otro)
        respuesta = self.client.get(
            self.reverse('apps.logistica:ver_ruta', args=[self.hoja.id_ruta])
        )
        self.assertEqual(respuesta.status_code, 302)

    def test_repartidor_asignado_puede_ver_hoja_de_ruta(self):
        self.client.force_login(self.repartidor)
        respuesta = self.client.get(
            self.reverse('apps.logistica:ver_ruta', args=[self.hoja.id_ruta])
        )
        self.assertEqual(respuesta.status_code, 200)

    def test_repartidor_asignado_ve_su_alerta_en_la_hoja(self):
        self.client.force_login(self.repartidor)
        respuesta = self.client.get(
            self.reverse('apps.logistica:ver_ruta', args=[self.hoja.id_ruta])
        )
        self.assertContains(respuesta, 'Llamar al timbre 3B.')

    def test_repartidor_no_asignado_no_ve_la_alerta(self):
        otro = self.Usuario.objects.create_user(
            username='otro_rep2', password='x', email='otro_rep2@test.com'
        )
        otro.groups.add(Group.objects.get(name=GRUPO_REPARTIDOR))
        rol = RolEmpleado.objects.create(nombre='Otro chofer 2', grupo_permisos='Repartidor')
        Empleado.objects.create(
            usuario=otro, nombre='Sofia', apellido='Ruiz', dni='66666666', rol=rol,
        )

        self.client.force_login(otro)
        respuesta = self.client.get(
            self.reverse('apps.logistica:imprimir_ruta', args=[self.hoja.id_ruta])
        )
        # No es su ruta: lo redirige antes de renderizar.
        self.assertEqual(respuesta.status_code, 302)

    def test_cliente_registrado_no_puede_actualizar_entregas(self):
        self.client.force_login(self.cliente)
        respuesta = self.client.get(
            self.reverse(
                'apps.logistica:actualizar_estado_entrega',
                args=[self.parada.id_detalle],
            )
        )
        self.assertEqual(respuesta.status_code, 302)

    def test_repartidor_no_asignado_no_puede_actualizar_entregas(self):
        otro = self.Usuario.objects.create_user(
            username='otro_rep3', password='x', email='otro_rep3@test.com'
        )
        otro.groups.add(Group.objects.get(name=GRUPO_REPARTIDOR))
        rol = RolEmpleado.objects.create(nombre='Otro chofer 3', grupo_permisos='Repartidor')
        Empleado.objects.create(
            usuario=otro, nombre='Pablo', apellido='Lopez', dni='77777777', rol=rol,
        )

        self.client.force_login(otro)
        respuesta = self.client.get(
            self.reverse(
                'apps.logistica:actualizar_estado_entrega',
                args=[self.parada.id_detalle],
            )
        )
        self.assertEqual(respuesta.status_code, 302)
