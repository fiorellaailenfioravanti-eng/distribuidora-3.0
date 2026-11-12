"""Validaciones de campos compartidas por los formularios de todas las apps.

Se usan desde los `clean_<campo>` de cada formulario: devuelven el valor
normalizado o levantan `ValidationError` con un mensaje para el usuario.
"""
import re

from django.core.exceptions import ValidationError
from django.utils import timezone

MIN_DIGITOS_TELEFONO = 8


def solo_digitos(valor):
    return ''.join(c for c in (valor or '') if c.isdigit())


def validar_dni(valor):
    """DNI argentino: 7 u 8 dígitos (se aceptan puntos y espacios al escribirlo)."""
    valor = (valor or '').strip()
    if not valor:
        return valor
    if re.search(r'[^\d.\s]', valor):
        raise ValidationError('El DNI sólo puede tener números.')
    digitos = solo_digitos(valor)
    if not 7 <= len(digitos) <= 8:
        raise ValidationError('El DNI debe tener 7 u 8 dígitos.')
    return digitos


def validar_telefono(valor, obligatorio=False):
    """Teléfono: dígitos con espacios, guiones, paréntesis o '+'; al menos 8 dígitos."""
    valor = (valor or '').strip()
    if not valor:
        if obligatorio:
            raise ValidationError('Ingresá un número de teléfono.')
        return valor
    if re.search(r'[^\d\s()+-]', valor):
        raise ValidationError('El teléfono sólo puede tener números, espacios, guiones, paréntesis o "+".')
    if len(solo_digitos(valor)) < MIN_DIGITOS_TELEFONO:
        raise ValidationError(f'Ingresá un número válido (al menos {MIN_DIGITOS_TELEFONO} dígitos).')
    return valor


def validar_fecha_no_futura(fecha, mensaje='La fecha no puede ser posterior a hoy.'):
    if fecha and fecha > timezone.localdate():
        raise ValidationError(mensaje)
    return fecha


def validar_fecha_no_pasada(fecha, mensaje='La fecha no puede ser anterior a hoy.'):
    if fecha and fecha < timezone.localdate():
        raise ValidationError(mensaje)
    return fecha


def validar_coordenadas(valor):
    """Formato 'lat,lng' con latitud entre -90 y 90 y longitud entre -180 y 180."""
    valor = (valor or '').strip()
    if not valor:
        return valor
    try:
        lat, lng = (float(p) for p in valor.split(','))
    except ValueError:
        raise ValidationError('Usá el formato "latitud,longitud" (ej: -27.4511,-58.9867).')
    if not (-90 <= lat <= 90 and -180 <= lng <= 180):
        raise ValidationError('Las coordenadas están fuera de rango.')
    return f'{lat},{lng}'


def validar_altura(valor):
    """Altura de la calle: número positivo (con letra opcional) o 'S/N'."""
    valor = (valor or '').strip()
    if valor.upper() in ('S/N', 'SN'):
        return 'S/N'
    if not re.fullmatch(r'\d{1,6}( ?[A-Za-z])?', valor):
        raise ValidationError('Ingresá el número de la calle (ej: 450) o "S/N".')
    return valor


def normalizar_patente(valor):
    """Patente argentina en mayúsculas y sin espacios: AB123CD (Mercosur) o ABC123."""
    valor = re.sub(r'[\s-]', '', valor or '').upper()
    if not re.fullmatch(r'[A-Z]{2}\d{3}[A-Z]{2}|[A-Z]{3}\d{3}', valor):
        raise ValidationError('Patente inválida: usá el formato AB123CD o ABC123.')
    return valor


# ─────────────────────────────────────────────────────────────
# Atributos HTML por tipo de dato: restringen lo que se puede escribir
# en el navegador (teclado numérico en celulares, largo máximo, patrón).
# El servidor valida igual con las funciones de arriba.
# ─────────────────────────────────────────────────────────────
ATTRS_DNI = {
    'inputmode': 'numeric', 'pattern': r'\d{7,8}', 'maxlength': '8', 'minlength': '7',
    'data-solo-numeros': '', 'title': 'Sólo números: 7 u 8 dígitos, sin puntos.',
    'placeholder': 'Ej: 30123456', 'autocomplete': 'off',
}
ATTRS_TELEFONO = {
    'type': 'tel', 'inputmode': 'tel', 'pattern': r'[\d\s\(\)\+\-]{8,20}', 'maxlength': '20',
    'data-solo-telefono': '', 'title': 'Sólo números (puede llevar espacios, guiones o +). Mínimo 8 dígitos.',
    'placeholder': 'Ej: 362 4123456',
}
ATTRS_ALTURA = {
    'pattern': r'(\d{1,6}( ?[A-Za-z])?|[Ss]/?[Nn])', 'maxlength': '8',
    'title': 'Número de la calle (ej: 450) o S/N.', 'placeholder': 'Ej: 450 o S/N',
}
ATTRS_COORDENADAS = {
    'pattern': r'\s*-?\d{1,2}(\.\d+)?\s*,\s*-?\d{1,3}(\.\d+)?\s*', 'inputmode': 'decimal',
    'title': 'Latitud,longitud (ej: -27.4511,-58.9867).', 'placeholder': '-27.4511,-58.9867 (opcional)',
}
ATTRS_PATENTE = {
    'pattern': r'([A-Za-z]{2}\s?\d{3}\s?[A-Za-z]{2}|[A-Za-z]{3}\s?\d{3})', 'maxlength': '9',
    'style': 'text-transform: uppercase;', 'title': 'Formato AB123CD o ABC123.', 'placeholder': 'Ej: AB123CD',
    'autocomplete': 'off',
}
ATTRS_NOMBRE = {
    'pattern': r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ' .\-]+", 'maxlength': '100',
    'title': 'Sólo letras, espacios, apóstrofo o guión.',
}
ATTRS_MONTO = {'inputmode': 'decimal', 'min': '0.01', 'step': '0.01'}
ATTRS_ENTERO_POSITIVO = {'inputmode': 'numeric', 'min': '1', 'step': '1'}


def aplicar_attrs(form, campo, attrs):
    """Suma `attrs` al widget de `campo` si el formulario lo tiene."""
    if campo in form.fields:
        form.fields[campo].widget.attrs.update(attrs)
        if attrs.get('type'):
            form.fields[campo].widget.input_type = attrs['type']


def validar_nombre(valor, etiqueta='El nombre'):
    """Nombres y apellidos: letras (con tildes), espacios, apóstrofo y guión."""
    valor = ' '.join((valor or '').split())
    if valor and not re.fullmatch(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ' .\-]+", valor):
        raise ValidationError(f'{etiqueta} sólo puede tener letras, espacios, apóstrofo o guión.')
    return valor
