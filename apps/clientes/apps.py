from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clientes'
    verbose_name = 'Clientes'

    def ready(self):
        # Importa las señales para que se registren al iniciar la app
        import apps.clientes.signals  # noqa: F401
