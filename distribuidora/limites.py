"""
Límites de largo de los campos de texto, aplicados en la base de datos.

- `max_length` en el modelo: lo usan los formularios (atributo maxlength y
  validación) y PostgreSQL (varchar(n)).
- `limite_largo(...)`: agrega restricciones CHECK para que la base rechace un
  texto más largo aunque no pase por un formulario. Hace falta porque SQLite
  no respeta el largo de varchar ni de text.
- `recortar_textos(...)`: operación de migración que recorta lo que ya estaba
  guardado antes de crear la restricción (si no, la migración fallaría).
"""
from django.db import migrations, models
from django.db.models.functions import Length, Substr
from django.db.models.lookups import GreaterThan, LessThanOrEqual

LARGO_NOMBRE = 64   # nombres, apellidos y títulos
LARGO_TEXTO = 500   # descripciones, observaciones y notas


def limite_largo(**campos):
    """Restricciones CHECK `largo(campo) <= n` para cada `campo=n`."""
    return [
        models.CheckConstraint(
            check=LessThanOrEqual(Length(campo), largo),
            name=f'%(app_label)s_%(class)s_{campo}_max_{largo}',
        )
        for campo, largo in campos.items()
    ]


def recortar_textos(modelo, **campos):
    """RunPython que recorta los textos guardados que superan el nuevo límite."""
    app_label, nombre_modelo = modelo.split('.')

    def recortar(apps, schema_editor):
        Modelo = apps.get_model(app_label, nombre_modelo)
        for campo, largo in campos.items():
            Modelo.objects.filter(GreaterThan(Length(campo), largo)).update(
                **{campo: Substr(campo, 1, largo)})

    return migrations.RunPython(recortar, migrations.RunPython.noop)
