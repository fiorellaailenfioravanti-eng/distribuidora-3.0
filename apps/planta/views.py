"""Pantallas de la planta: recarga diaria y stock de bidones."""
from datetime import timedelta

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils import timezone

from apps.permisos.roles import requiere
from .models import RecargaBidones
from .services import MAXIMO_POR_TIPO, bidones_recargables, guardar_recarga, recarga_de, resumen_stock


def _leer_cantidades(post, bidones):
    """{producto_id: cantidad} desde el formulario; errores por bidón."""
    cantidades, errores = {}, []
    for bidon in bidones:
        texto = (post.get(f'cantidad_{bidon.pk}') or '0').strip()
        if not texto.isdigit():
            errores.append(f'{bidon.nombre}: escribí un número entero (0 si no recargaste).')
            continue
        cantidades[bidon.pk] = int(texto)
    return cantidades, errores


@requiere('registrar_recargas')
def recarga_diaria(request):
    """El recargador anota cuántos bidones llenó hoy (se puede corregir durante el día)."""
    hoy = timezone.localdate()
    bidones = list(bidones_recargables())
    recarga = recarga_de(hoy)
    cargado = {d.producto_id: d.cantidad for d in recarga.detalles.all()} if recarga else {}

    if request.method == 'POST':
        cantidades, errores = _leer_cantidades(request.POST, bidones)
        if errores:
            for error in errores:
                messages.error(request, error)
        else:
            try:
                recarga = guardar_recarga(request.user, cantidades, fecha=hoy,
                                          observaciones=request.POST.get('observaciones', ''))
            except ValidationError as error:
                messages.error(request, ' '.join(error.messages))
            else:
                messages.success(request, f'Recarga de hoy guardada: {recarga.total()} bidones.')
                return redirect('apps.planta:recarga_diaria')
        cargado = {pk: request.POST.get(f'cantidad_{pk}', '') for pk in (b.pk for b in bidones)}

    ya_recargado = {d.producto_id: d.cantidad for d in recarga.detalles.all()} if recarga else {}
    filas = [{'bidon': b, 'cantidad': cargado.get(b.pk, ''), 'vacios': b.envase.stock,
              # Tope en pantalla: los vacíos de su envase + lo que ya se recargó hoy (corregir no consume
              # envases de nuevo). Si varios bidones comparten envase, el total lo controla el servidor.
              'maximo': max(0, min(MAXIMO_POR_TIPO, b.envase.stock + ya_recargado.get(b.pk, 0)))}
             for b in bidones]
    historial = (RecargaBidones.objects.filter(fecha__gte=hoy - timedelta(days=14))
                 .select_related('registrada_por').prefetch_related('detalles__producto'))
    return render(request, 'planta/recarga_diaria.html', {
        'hoy': hoy,
        'recarga': recarga,
        'filas': filas,
        'historial': historial,
        'maximo': MAXIMO_POR_TIPO,
    })


@requiere('ver_stock_bidones')
def stock_bidones(request):
    """Bidones llenos y vacíos por tamaño, y lo que está en manos de los clientes."""
    grupos, en_clientes = resumen_stock()
    hoy = timezone.localdate()
    return render(request, 'planta/stock_bidones.html', {
        'grupos': grupos,
        'en_clientes': en_clientes,
        'recarga_hoy': recarga_de(hoy),
        'ultimas': RecargaBidones.objects.prefetch_related('detalles__producto')[:7],
    })
