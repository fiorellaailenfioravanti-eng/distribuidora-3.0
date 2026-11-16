"""Reglas de la recarga diaria de bidones."""
from collections import defaultdict

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from apps.productos.models import Producto
from .models import DetalleRecarga, RecargaBidones

MAXIMO_POR_TIPO = 5000  # tope de sentido común por bidón y por día


def bidones_recargables():
    """Bidones que se llenan en la planta (con su envase vacío)."""
    return (Producto.objects.filter(es_recargable=True, envase__isnull=False)
            .select_related('envase').order_by('envase__nombre', 'nombre'))


def recarga_de(fecha=None):
    fecha = fecha or timezone.localdate()
    return RecargaBidones.objects.filter(fecha=fecha).prefetch_related('detalles__producto').first()


@transaction.atomic
def guardar_recarga(usuario, cantidades, fecha=None, observaciones=''):
    """Registra (o corrige) la recarga del día.

    `cantidades` = {producto_id: cantidad total recargada ese día}. Si la
    recarga ya existía, sólo se mueve la diferencia: así corregir un número
    no descuenta dos veces los envases.

    Por cada bidón: +cantidad al stock lleno y −cantidad al stock de su envase
    vacío. No deja que el envase quede en negativo.
    """
    fecha = fecha or timezone.localdate()
    productos = {p.pk: p for p in Producto.objects.select_for_update().filter(
        pk__in=list(cantidades), es_recargable=True, envase__isnull=False)}
    if set(cantidades) - set(productos):
        raise ValidationError('Uno de los bidones no se puede recargar.')

    recarga, _ = RecargaBidones.objects.select_for_update().get_or_create(
        fecha=fecha, defaults={'registrada_por': usuario})
    anteriores = {d.producto_id: d for d in recarga.detalles.all()}

    # Diferencias contra lo ya registrado ese día.
    deltas = {}
    for pk, cantidad in cantidades.items():
        if cantidad < 0 or cantidad > MAXIMO_POR_TIPO:
            raise ValidationError(f'La cantidad de {productos[pk].nombre} debe estar entre 0 y {MAXIMO_POR_TIPO}.')
        anterior = anteriores[pk].cantidad if pk in anteriores else 0
        deltas[pk] = cantidad - anterior

    # Los bidones del mismo tamaño comparten envase: se controla el total por envase.
    por_envase = defaultdict(int)
    for pk, delta in deltas.items():
        por_envase[productos[pk].envase_id] += delta
    envases = {e.pk: e for e in Producto.objects.select_for_update().filter(pk__in=list(por_envase))}
    for envase_id, delta in por_envase.items():
        envase = envases[envase_id]
        if delta > envase.stock:
            raise ValidationError(
                f'No alcanzan los envases vacíos: hay {envase.stock} de «{envase.nombre}» '
                f'y la carga necesita {delta} más.')

    for pk, delta in deltas.items():
        if delta == 0 and pk in anteriores:
            continue
        producto = productos[pk]
        producto.stock += delta
        producto.save(update_fields=['stock'])
        envase = envases[producto.envase_id]
        envase.stock -= delta
        DetalleRecarga.objects.update_or_create(
            recarga=recarga, producto=producto, defaults={'cantidad': cantidades[pk]})
    for envase in envases.values():
        envase.save(update_fields=['stock'])

    recarga.registrada_por = usuario
    recarga.observaciones = (observaciones or '').strip()[:200]
    recarga.save()
    return recarga


def resumen_stock():
    """Stock de bidones por envase: llenos (cada marca), vacíos en planta y en manos de clientes."""
    from apps.clientes.models import Cliente

    grupos = []
    envases = Producto.objects.filter(es_envase=True, activo=True).order_by('nombre')  # sin los eliminados
    for envase in envases:
        llenos = list(Producto.objects.filter(envase=envase, activo=True).order_by('-es_recargable', 'nombre'))
        grupos.append({
            'envase': envase,
            'llenos': llenos,
            'total_llenos': sum(p.stock for p in llenos),
            'vacios': envase.stock,
        })
    en_clientes = Cliente.objects.aggregate(total=Sum('bidones_prestados'))['total'] or 0
    return grupos, en_clientes
