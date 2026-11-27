"""Test runner del proyecto: los archivos que suben o generan los tests
(comprobantes, recibos en PDF, fotos) van a una carpeta temporal que se borra
al terminar, y no ensucian `media/` del desarrollador."""
import shutil
import tempfile

from django.test.runner import DiscoverRunner
from django.test.utils import override_settings


class RunnerConMediaTemporal(DiscoverRunner):
    def run_tests(self, *args, **kwargs):
        carpeta = tempfile.mkdtemp(prefix='aguadelluvia-media-')
        try:
            with override_settings(MEDIA_ROOT=carpeta):
                return super().run_tests(*args, **kwargs)
        finally:
            shutil.rmtree(carpeta, ignore_errors=True)
