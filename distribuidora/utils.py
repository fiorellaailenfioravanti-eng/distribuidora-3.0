"""Utilidades compartidas por las apps del proyecto."""
import unicodedata


def normalizar_texto(texto):
    """Quita tildes, pasa a minúsculas y recorta espacios ("Bidón " → "bidon").

    Base de las búsquedas tolerantes (RF-07) de productos, clientes y
    empleados. Antes había una copia en cada app (auditoría R-1).
    """
    if not texto:
        return ''
    texto = unicodedata.normalize('NFD', str(texto))
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn').lower().strip()
