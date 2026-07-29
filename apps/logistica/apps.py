from django.apps import AppConfig


class LogisticaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.logistica'
    verbose_name = 'Logística'

    def ready(self):
        """Crea el grupo 'Repartidor' automáticamente al iniciar la app."""
        from django.db.models.signals import post_migrate
        from django.dispatch import receiver

        @receiver(post_migrate, sender=self)
        def crear_grupo_repartidor(sender, **kwargs):
            from django.contrib.auth.models import Group
            Group.objects.get_or_create(name='Repartidor')
