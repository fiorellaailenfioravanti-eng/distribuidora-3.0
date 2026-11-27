"""Recibo de pago en efectivo que emite el repartidor al cobrar en la calle.

Cuando el repartidor marca «Pagó todo» o «Pagó una parte» en efectivo, se
genera un PDF con el monto cobrado, se guarda en el pago (`PagoPedido.comprobante`,
así queda en el historial del cliente) y se le envía por correo al cliente.

El PDF se arma a mano (texto y líneas, fuente Helvetica) para no sumar una
dependencia sólo por esto.
"""
import logging
from decimal import Decimal

from django.core.files.base import ContentFile
from django.db import transaction
from django.utils import timezone

log = logging.getLogger(__name__)

CODIGO_EFECTIVO = 'EFECTIVO'


# ── PDF mínimo ─────────────────────────────────────────────────────────────

def _texto_pdf(texto):
    """Texto escapado para un string PDF, en WinAnsi (admite tildes, ñ y «—»)."""
    crudo = str(texto).encode('cp1252', errors='replace')
    return crudo.replace(b'\\', b'\\\\').replace(b'(', b'\\(').replace(b')', b'\\)')


def _ancho_aproximado(texto, tamano, negrita=False):
    """Ancho aproximado en Helvetica (para alinear a la derecha)."""
    ancho = 0
    for caracter in texto:
        if caracter.isupper():
            em = 0.70 if negrita else 0.67
        elif caracter in ' .,:;|il':
            em = 0.28
        elif caracter.isdigit() or caracter in '$#°':
            em = 0.556
        else:
            em = 0.58 if negrita else 0.53
        ancho += em * tamano
    return ancho


class _Pagina:
    """Acumula las órdenes de dibujo de una página A4 (595 × 842 pt)."""
    ANCHO, ALTO = 595, 842

    def __init__(self):
        self.ordenes = []

    def texto(self, x, y, texto, tamano=10, negrita=False, color=(0.07, 0.13, 0.25), derecha=False):
        fuente = b'/F2' if negrita else b'/F1'
        if derecha:
            x -= _ancho_aproximado(str(texto), tamano, negrita)
        r, g, b = color
        self.ordenes.append(b'%.2f %.2f %.2f rg BT %s %d Tf %.1f %.1f Td (' % (r, g, b, fuente, tamano, x, y)
                            + _texto_pdf(texto) + b') Tj ET')

    def linea(self, x1, y1, x2, y2, grosor=0.6, color=(0.85, 0.88, 0.93)):
        r, g, b = color
        self.ordenes.append(b'%.2f %.2f %.2f RG %.1f w %.1f %.1f m %.1f %.1f l S' % (r, g, b, grosor, x1, y1, x2, y2))

    def rectangulo(self, x, y, ancho, alto, color):
        r, g, b = color
        self.ordenes.append(b'%.2f %.2f %.2f rg %.1f %.1f %.1f %.1f re f' % (r, g, b, x, y, ancho, alto))

    def pdf(self):
        contenido = b'\n'.join(self.ordenes)
        objetos = [
            b'<< /Type /Catalog /Pages 2 0 R >>',
            b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
            b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %d %d] /Contents 4 0 R '
            b'/Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>' % (self.ANCHO, self.ALTO),
            b'<< /Length %d >>\nstream\n' % len(contenido) + contenido + b'\nendstream',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>',
        ]
        salida = bytearray(b'%PDF-1.4\n')
        posiciones = []
        for numero, objeto in enumerate(objetos, start=1):
            posiciones.append(len(salida))
            salida += b'%d 0 obj\n' % numero + objeto + b'\nendobj\n'
        inicio_xref = len(salida)
        salida += b'xref\n0 %d\n0000000000 65535 f \n' % (len(objetos) + 1)
        for posicion in posiciones:
            salida += b'%010d 00000 n \n' % posicion
        salida += b'trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n' % (len(objetos) + 1, inicio_xref)
        return bytes(salida)


def _pesos(valor):
    """$1.234,50 (formato argentino)."""
    entero, decimales = f'{Decimal(valor):,.2f}'.split('.')
    return f"${entero.replace(',', '.')},{decimales}"


def numero_recibo(pago):
    return f'{pago.pk:08d}'


def generar_pdf_recibo(pago, repartidor=''):
    """Bytes del PDF del recibo de `pago` (lo que cobró el repartidor)."""
    pedido = pago.pedido
    cliente = pedido.cliente
    fecha = timezone.localtime(pago.fecha or timezone.now())
    azul, verde, gris = (0.12, 0.31, 0.57), (0.37, 0.55, 0.09), (0.33, 0.40, 0.50)
    p = _Pagina()
    margen, derecha = 50, _Pagina.ANCHO - 50

    p.rectangulo(0, _Pagina.ALTO - 8, _Pagina.ANCHO, 8, azul)
    p.texto(margen, 780, 'Aguadelluvia', tamano=24, negrita=True, color=azul)
    p.texto(margen, 762, 'Distribuidora de agua · Resistencia, Chaco', tamano=9, color=gris)
    p.texto(derecha, 784, 'COMPROBANTE DE PAGO', tamano=12, negrita=True, derecha=True)
    p.texto(derecha, 768, f'N° {numero_recibo(pago)}', tamano=11, derecha=True)
    p.texto(derecha, 754, fecha.strftime('%d/%m/%Y %H:%M'), tamano=9, color=gris, derecha=True)
    p.linea(margen, 740, derecha, 740)

    y = 716
    datos = [
        ('Cliente', cliente.nombre_completo() if cliente else 'Sin cliente'),
        ('DNI', (cliente.dni if cliente else '') or '—'),
        ('Domicilio', pedido.direccion_entrega.direccion_completa() if pedido.direccion_entrega_id else '—'),
        ('Pedido', f'#{pedido.pk}'),
        ('Medio de pago', 'Efectivo'),
        ('Cobrado por', repartidor or '—'),
    ]
    for etiqueta, valor in datos:
        p.texto(margen, y, etiqueta, tamano=9, color=gris)
        p.texto(margen + 95, y, str(valor)[:80], tamano=10)
        y -= 18

    y -= 8
    p.linea(margen, y + 6, derecha, y + 6)
    p.texto(margen, y - 10, 'Detalle del pedido', tamano=10, negrita=True)
    y -= 30
    for detalle in pedido.detalles.select_related('producto'):
        p.texto(margen, y, f'{detalle.cantidad} × {detalle.producto.nombre}'[:70], tamano=10)
        p.texto(derecha, y, _pesos(detalle.subtotal), tamano=10, derecha=True)
        y -= 16
    p.linea(margen, y + 4, derecha, y + 4)
    y -= 14
    p.texto(margen, y, 'Total del pedido', tamano=10)
    p.texto(derecha, y, _pesos(pedido.total), tamano=10, derecha=True)

    y -= 34
    p.rectangulo(margen, y - 14, derecha - margen, 40, (0.93, 0.96, 0.89))
    p.texto(margen + 14, y, 'MONTO PAGADO', tamano=11, negrita=True, color=verde)
    p.texto(derecha - 14, y - 2, _pesos(pago.monto), tamano=18, negrita=True, color=verde, derecha=True)

    y -= 40
    saldo = pedido.saldo_por_cobrar()  # descuenta este pago aunque espere la aprobación
    if saldo > 0:
        p.texto(margen, y, f'Saldo pendiente del pedido: {_pesos(saldo)}', tamano=10, negrita=True)
    else:
        p.texto(margen, y, 'El pedido quedó totalmente pagado.', tamano=10, negrita=True, color=verde)

    p.linea(margen, 90, derecha, 90)
    p.texto(margen, 74, 'Comprobante generado automáticamente al registrar el cobro. No válido como factura.',
            tamano=8, color=gris)
    p.texto(margen, 62, 'Guardalo para futuros controles: también queda registrado en tu historial de pedidos.',
            tamano=8, color=gris)
    return p.pdf()


# ── Emisión ────────────────────────────────────────────────────────────────

def emitir_recibo_efectivo(pago, repartidor=''):
    """Genera el recibo del cobro en efectivo, lo guarda en el pago y lo envía al cliente.

    Sólo actúa sobre cobros en efectivo (pendientes de que el administrador cuente
    el efectivo, o ya aprobados). El correo se manda cuando se confirma la
    transacción (si falla el envío, el recibo igual queda guardado).
    Devuelve el pago.
    """
    if pago.estado_pago == 'Rechazado' or pago.metodo_pago.codigo != CODIGO_EFECTIVO or pago.monto <= 0:
        return pago
    contenido = generar_pdf_recibo(pago, repartidor)
    pago.comprobante.save(f'recibo-{numero_recibo(pago)}.pdf', ContentFile(contenido), save=False)
    pago.save(update_fields=['comprobante'])

    cliente = pago.pedido.cliente
    correo = cliente.email_display() if cliente else ''
    if correo:
        transaction.on_commit(lambda: _enviar_recibo(pago, correo, contenido))
    return pago


def _enviar_recibo(pago, correo, contenido):
    from apps.autenticacion.recuperacion import enviar_correo
    pedido = pago.pedido
    try:
        enviar_correo(
            correo, f'Comprobante de pago N° {numero_recibo(pago)}', 'pedidos/correos/recibo', {
                'pago': pago, 'pedido': pedido, 'cliente': pedido.cliente,
                'numero': numero_recibo(pago), 'monto': _pesos(pago.monto),
                'saldo': _pesos(pedido.saldo_por_cobrar()), 'debe': pedido.saldo_por_cobrar() > 0,
            },
            adjuntos=[(f'comprobante-{numero_recibo(pago)}.pdf', contenido, 'application/pdf')],
        )
    except Exception:
        log.exception('No se pudo enviar el recibo del pago %s', pago.pk)
