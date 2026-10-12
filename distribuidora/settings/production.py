"""
Entorno de PRODUCCIÓN.

Corrige el hallazgo H-9: el archivo estaba vacío (0 bytes), por lo que no había
ninguna configuración de despliegue y la `SECRET_KEY` hardcodeada de `base.py`
era la única credencial del proyecto.

Uso:
    python manage.py migrate --settings=distribuidora.settings.production
    python manage.py check --deploy --settings=distribuidora.settings.production

Antes de desplegar, defínase en el entorno (o en un `.env` no versionado):

    SECRET_KEY=<clave larga y aleatoria>
    ALLOWED_HOSTS=distribuidora.com,www.distribuidora.com
    MERCADOPAGO_ACCESS_TOKEN=APP_USR-...
    MERCADOPAGO_WEBHOOK_SECRET=<secreto del webhook>

`decouple` no admite valor por defecto en este módulo a propósito: si falta
alguna variable obligatoria, el arranque falla de forma explícita en lugar de
cargar un valor inseguro.
"""

from decouple import Csv, config

from .base import *  # noqa: F401,F403
from .base import INSTALLED_APPS, MIDDLEWARE, ROOT_URLCONF  # noqa: F401

# Sin defaults: una configuración incompleta debe fallar al arrancar.
SECRET_KEY = config('SECRET_KEY')  # noqa: F405
DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())  # noqa: F405

# URLs firmadas de archivos subidos (productos, fotos de perfil).
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # noqa: F405

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405

# El panel de administración exige HTTPS: es donde se gestionan datos
# personales de clientes, incluida la nota de acceso al domicilio (RNF-02).
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

X_FRAME_OPTIONS = 'DENY'

# Anti-CSRF en formularios de pago y logout.
CSRF_FAILURE_VIEW = 'apps.permisos.views.csrf_failure'

# ---------------------------------------------------------------------
# Base de datos
# ---------------------------------------------------------------------
# SQLite 3 es el motor justificado en la memoria de tesis (persistencia en un
# único archivo, soporte ACID, zero-configuración). Para un despliegue real con
# concurrencia de escritura se recomienda PostgreSQL:
#
#     pip install psycopg2-binary
#
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': config('DB_NAME'),
#             'USER': config('DB_USER'),
#             'PASSWORD': config('DB_PASSWORD'),
#             'HOST': config('DB_HOST', default='localhost'),
#             'PORT': config('DB_PORT', default='5432'),
#         }
#     }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
    }
}

# ---------------------------------------------------------------------
# Integraciones de pago
# ---------------------------------------------------------------------
MERCADOPAGO_ACCESS_TOKEN = config('MERCADOPAGO_ACCESS_TOKEN')  # noqa: F405
MERCADOPAGO_WEBHOOK_SECRET = config('MERCADOPAGO_WEBHOOK_SECRET')  # noqa: F405

# ---------------------------------------------------------------------
# Archivos subidos
# ---------------------------------------------------------------------
# `Empleado` y `Cliente` guardan imágenes. El tamaño máximo evita que un
# usuario suba un archivo arbitrario y agote el almacenamiento.
MAX_UPLOAD_SIZE_MB = 10
DATA_UPLOAD_MAX_MEMORY_SIZE = MAX_UPLOAD_SIZE_MB * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024
