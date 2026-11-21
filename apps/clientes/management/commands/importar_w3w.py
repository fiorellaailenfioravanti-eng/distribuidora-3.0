"""Importa las ubicaciones what3words de la planilla de recorridos.

Uso:
    manage.py importar_w3w "Recorridos.xlsx"            # simulación: solo informa
    manage.py importar_w3w "Recorridos.xlsx" --aplicar  # guarda los cambios

La planilla necesita una columna con el número de cliente (`NRO CLI`) y otra con
la ubicación (`UBICACIÓN`, con `///palabra.palabra.palabra` o el link w3w.co).
Se cruza por `Cliente.numero` y se guarda en la dirección principal del cliente
(o en la primera, si no tiene principal). Si un cliente aparece con más de una
ubicación distinta, se usa la primera y las demás se listan para revisar a mano.
También acepta un .csv con los mismos encabezados.
"""
import csv
import unicodedata
from pathlib import Path

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.clientes.models import Cliente, DireccionEntrega
from distribuidora.validadores import validar_w3w

COLUMNAS_NUMERO = ('NRO CLI', 'NRO CLIENTE', 'NUMERO', 'NRO')
COLUMNAS_W3W = ('UBICACION', 'W3W', 'WHAT3WORDS')


def _normalizar(texto):
    texto = unicodedata.normalize('NFKD', str(texto or '')).encode('ascii', 'ignore').decode()
    return texto.strip().upper()


def _leer_filas(ruta, hoja):
    if ruta.suffix.lower() == '.csv':
        with ruta.open(encoding='utf-8-sig', newline='') as archivo:
            return [list(fila) for fila in csv.reader(archivo)]
    try:
        import openpyxl
    except ImportError:
        raise CommandError('Falta openpyxl para leer .xlsx (pip install -r requirements.txt).')
    libro = openpyxl.load_workbook(ruta, read_only=True, data_only=True)
    if hoja not in libro.sheetnames:
        raise CommandError(f'La planilla no tiene la hoja "{hoja}". Hojas: {", ".join(libro.sheetnames)}.')
    return [list(fila) for fila in libro[hoja].iter_rows(values_only=True)]


def _indice(encabezado, candidatos):
    for candidato in candidatos:
        if candidato in encabezado:
            return encabezado.index(candidato)
    return None


class Command(BaseCommand):
    help = 'Carga las ubicaciones what3words de la planilla de recorridos en las direcciones de los clientes.'

    def add_arguments(self, parser):
        parser.add_argument('archivo', help='Planilla .xlsx (o .csv) con NRO CLI y UBICACIÓN.')
        parser.add_argument('--hoja', default='W3W', help='Hoja del .xlsx a leer (por defecto: W3W).')
        parser.add_argument('--aplicar', action='store_true',
                            help='Guarda los cambios. Sin esta opción solo muestra qué haría.')

    def handle(self, *args, **opciones):
        ruta = Path(opciones['archivo'])
        if not ruta.exists():
            raise CommandError(f'No existe el archivo {ruta}.')
        filas = _leer_filas(ruta, opciones['hoja'])
        if not filas:
            raise CommandError('La planilla está vacía.')

        encabezado = [_normalizar(c) for c in filas[0]]
        col_numero = _indice(encabezado, COLUMNAS_NUMERO)
        col_w3w = _indice(encabezado, COLUMNAS_W3W)
        if col_numero is None or col_w3w is None:
            raise CommandError('No encuentro las columnas "NRO CLI" y "UBICACIÓN" en la primera fila.')

        # numero de cliente -> lista de w3w en el orden de la planilla (sin repetir)
        por_numero, sin_numero, invalidos = {}, [], []
        for n_fila, fila in enumerate(filas[1:], start=2):
            numero = str(fila[col_numero] or '').strip() if col_numero < len(fila) else ''
            crudo = fila[col_w3w] if col_w3w < len(fila) else ''
            if not numero and not crudo:
                continue
            try:
                w3w = validar_w3w(str(crudo or ''))
            except ValidationError:
                invalidos.append((n_fila, numero, crudo))
                continue
            if not w3w:
                continue
            if not numero:
                sin_numero.append((n_fila, w3w))
                continue
            ubicaciones = por_numero.setdefault(numero, [])
            if w3w not in ubicaciones:
                ubicaciones.append(w3w)

        clientes = Cliente.objects.in_bulk(list(por_numero), field_name='numero')
        a_guardar, sin_cambio, no_encontrados, sin_direccion, varias = [], 0, [], [], []
        for numero, ubicaciones in por_numero.items():
            cliente = clientes.get(numero)
            if cliente is None:
                no_encontrados.append(numero)
                continue
            direccion = (DireccionEntrega.objects.filter(cliente=cliente)
                         .order_by('-es_principal', 'pk').first())
            if direccion is None:
                sin_direccion.append(cliente)
                continue
            if len(ubicaciones) > 1:
                varias.append((cliente, ubicaciones))
            if direccion.w3w == ubicaciones[0]:
                sin_cambio += 1
            else:
                a_guardar.append((direccion, ubicaciones[0]))

        if opciones['aplicar']:
            with transaction.atomic():
                for direccion, w3w in a_guardar:
                    DireccionEntrega.todos.filter(pk=direccion.pk).update(w3w=w3w)

        self._informe(opciones['aplicar'], a_guardar, sin_cambio, varias, sin_numero,
                      invalidos, no_encontrados, sin_direccion)

    def _informe(self, aplicar, a_guardar, sin_cambio, varias, sin_numero, invalidos,
                 no_encontrados, sin_direccion):
        escribir = self.stdout.write
        verbo = 'Actualizadas' if aplicar else 'Se actualizarían'
        escribir(self.style.SUCCESS(f'{verbo}: {len(a_guardar)} direcciones.') + f' Ya estaban al día: {sin_cambio}.')
        if varias:
            escribir(self.style.WARNING(f'\nClientes con más de una ubicación ({len(varias)}): se usó la primera.'))
            for cliente, ubicaciones in varias:
                otras = ', '.join(f'///{u}' for u in ubicaciones[1:])
                escribir(f'  {cliente.numero} {cliente.nombre_completo()}: ///{ubicaciones[0]}  (sin usar: {otras})')
        if sin_numero:
            escribir(self.style.WARNING(f'\nFilas sin número de cliente ({len(sin_numero)}):'))
            for n_fila, w3w in sin_numero:
                escribir(f'  fila {n_fila}: ///{w3w}')
        if invalidos:
            escribir(self.style.WARNING(f'\nUbicaciones con formato inválido ({len(invalidos)}):'))
            for n_fila, numero, crudo in invalidos:
                escribir(f'  fila {n_fila} (cliente {numero or "?"}): {crudo}')
        if no_encontrados:
            escribir(self.style.WARNING(f'\nNúmeros que no están en la base ({len(no_encontrados)}): '
                                        + ', '.join(no_encontrados)))
        if sin_direccion:
            escribir(self.style.WARNING(f'\nClientes sin dirección cargada ({len(sin_direccion)}):'))
            for cliente in sin_direccion:
                escribir(f'  {cliente.numero} {cliente.nombre_completo()}')
        if not aplicar:
            escribir('\nSimulación: no se guardó nada. Repetí con --aplicar para guardar.')
