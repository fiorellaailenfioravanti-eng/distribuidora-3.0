"""
Entorno de DESARROLLO.

- DEBUG activado y `ALLOWED_HOSTS` abierto para trabajar en `127.0.0.1`.
- SQLite sobre el archivo local `db.sqlite3`.
- Las claves se leen de `.env` si existe; si no, se usa el valor de respaldo
  declarado en `base.py` para que el proyecto arranque sin configuración previa.
"""

from .base import *  # noqa: F401,F403

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
    }
}
