from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from apps.cuentas.services import DIAS_VENCIMIENTO_DEFAULT, obtener_o_crear_cuenta, registrar_cargo
from .models import Abono


@transaction.atomic
def generar_cargos_mensuales(anio=None, mes=None):
    """Genera el cargo mensual de cada abono activo en la cuenta del cliente.

    Devuelve (generados, omitidos):
      - `generados`: abonos a los que se les creó el cargo.
      - `omitidos`: abonos que no pudieron cargarse por no tener fiado (RF-05).
    """
    hoy = timezone.localdate()
    anio = anio or hoy.year
    mes = mes or hoy.month

    generados = []
    omitidos = []

    for abono in Abono.objects.select_related('cliente', 'producto').filter(estado='Activo'):
        if not abono.debe_facturarse_en(anio, mes):
            continue

        # RF-05: sin fiado habilitado no se puede cargar a cuenta corriente.
        if not abono.cliente.permite_fiado:
            omitidos.append(abono)
            continue

        cuenta = obtener_o_crear_cuenta(abono.cliente)
        monto = abono.costo_para_cliente()
        fecha_cargo = abono.fecha_facturacion_del_mes(anio, mes)
        registrar_cargo(
            cuenta,
            monto,
            descripcion=(
                f"Abono mensual #{abono.id_abono} — {abono.producto.nombre} "
                f"({mes:02d}/{anio})"
            ),
            abono=abono,
            fecha_vencimiento=fecha_cargo + timedelta(days=DIAS_VENCIMIENTO_DEFAULT),
        )

        abono.ultima_facturacion = fecha_cargo
        abono.save(update_fields=['ultima_facturacion'])
        generados.append(abono)

    return generados, omitidos
