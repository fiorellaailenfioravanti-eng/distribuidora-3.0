"""
Configuración compartida entre los entornos de desarrollo y producción.

Separación de responsabilidades:
  - `base.py`    → lo que no cambia: apps, plantillas, i18n, tiempo, rutas.
  - `local.py`   → desarrollo: DEBUG=True, SQLite, hosts abiertos.
  - `production.py` → despliegue: DEBUG=False, hosts reales, credenciales.

Regla de seguridad: ninguna clave real vive en el repositorio. La `SECRET_KEY`
y las credenciales de MercadoPago se leen del entorno mediante `decouple`, que
busca primero en el archivo `.env` y después en las variables de entorno.
"""

import os
from pathlib import Path
from decouple import config

# Ruta del proyecto: distribuidora/ -> raíz del repositorio.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ─────────────────────────────────────────────────────────────────────
# CLAVES
# ─────────────────────────────────────────────────────────────────────
# Fallback de desarrollo para que el proyecto arranque sin configurar nada.
# En producción `production.py` no usa este valor: exige la variable real.
SECRET_KEY_FALLBACK = 'django-insecure-i@3^lh1x@v88irxo^gsk=8srdbq+p^yrf0ht+vj%#4ylzx0ktg'

SECRET_KEY = config(
    'SECRET_KEY',
    default=SECRET_KEY_FALLBACK,
)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.productos',
    'apps.autenticacion',
    'apps.carrito',
    'apps.buscador',
    'apps.logistica',
    'apps.clientes',
    'apps.pedidos',
    'apps.empleados',
    'apps.cuentas',
    'apps.abonos',
    'apps.permisos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'distribuidora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.carrito.context_processors.carrito_total',
            ],
        },
    },
]

WSGI_APPLICATION = 'distribuidora.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'autenticacion.Usuario'  # Modelo de usuario personalizado
LOGIN_URL = '/auth/ingresar/'  # Ajusta al name que tengas en auth/urls.py
LOGIN_REDIRECT_URL = '/'  # Redirige al inicio después de iniciar sesión
LOGOUT_REDIRECT_URL = '/auth/ingresar/'  # Redirige al inicio de sesión después de cerrar sesión


# ─────────────────────────────────────────────────────────────────────
# MERCADOPAGO
# ─────────────────────────────────────────────────────────────────────
# En desarrollo funciona sin configurar nada (queda inactivo el checkout QR).
# En producción `production.py` exige el token real.
MERCADOPAGO_ACCESS_TOKEN = config('MERCADOPAGO_ACCESS_TOKEN', default='')
# Sin secreto no se valida la firma del webhook (sólo aceptable en desarrollo).
MERCADOPAGO_WEBHOOK_SECRET = config('MERCADOPAGO_WEBHOOK_SECRET', default='')
