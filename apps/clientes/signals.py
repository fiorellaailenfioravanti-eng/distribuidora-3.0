"""
Señales de la app clientes.

Al crear un nuevo Usuario, se crea automáticamente su perfil Cliente
y se migran celular1/celular2 como TelefonoContacto.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender='autenticacion.Usuario')
def crear_perfil_cliente(sender, instance, created, **kwargs):
    """
    Crea el perfil Cliente automáticamente cuando se registra un usuario nuevo.
    Migra celular1 y celular2 como TelefonoContacto si están informados.
    Solo crea el perfil si el usuario no tiene ya un perfil vinculado.
    """
    if not created:
        return

    # Si se marcó explícitamente como empleado antes de guardar, no creamos perfil de cliente
    if getattr(instance, '_es_empleado', False):
        return

    from apps.clientes.models import Cliente, TelefonoContacto

    # No crear si ya existe un perfil (evita duplicados)
    if Cliente.objects.filter(usuario=instance).exists():
        return

    # Usar nombre/apellido si están en el usuario
    cliente = Cliente.objects.create(
        usuario=instance,
        nombre=instance.first_name or '',
        apellido=instance.last_name or '',
    )

    # Migrar celular1 si existe
    if getattr(instance, 'celular1', None):
        TelefonoContacto.objects.create(
            cliente=cliente,
            numero=instance.celular1,
            desc_relacion='Titular',
            es_principal=True,
        )

    # Migrar celular2 si existe
    if getattr(instance, 'celular2', None):
        TelefonoContacto.objects.create(
            cliente=cliente,
            numero=instance.celular2,
            desc_relacion='Alternativo',
            es_principal=False,
        )
