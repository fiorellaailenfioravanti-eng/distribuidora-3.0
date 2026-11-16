/*
 * Tablas ordenables del panel.
 *
 * Uso: <table data-ordenable> y en cada <th data-ordenar="texto|numero"> que se pueda ordenar.
 * El valor de cada celda sale de su atributo data-valor (si existe) o de su texto visible.
 * Un clic en el botón de la columna ordena A→Z (o menor→mayor); otro clic invierte el orden.
 */
(function () {
    'use strict';

    const comparadorTexto = new Intl.Collator('es', { numeric: true, sensitivity: 'base' });

    function valorCelda(fila, indice) {
        const celda = fila.cells[indice];
        if (!celda) return '';
        return (celda.dataset.valor ?? celda.textContent).trim();
    }

    function iconoPara(direccion) {
        if (direccion === 'asc') return 'fa-arrow-up-a-z';
        if (direccion === 'desc') return 'fa-arrow-down-z-a';
        return 'fa-sort';
    }

    function prepararTabla(tabla) {
        const cuerpo = tabla.tBodies[0];
        if (!cuerpo) return;
        const encabezados = Array.from(tabla.tHead.rows[0].cells);

        encabezados.forEach(function (th, indice) {
            const tipo = th.dataset.ordenar;
            if (!tipo) return;

            const boton = document.createElement('button');
            boton.type = 'button';
            boton.className = 'btn-ordenar';
            boton.title = 'Ordenar por ' + th.textContent.trim().toLowerCase();
            boton.setAttribute('aria-label', boton.title);
            boton.innerHTML = '<i class="fa-solid fa-sort"></i>';
            th.appendChild(boton);

            boton.addEventListener('click', function () {
                const direccion = th.getAttribute('aria-sort') === 'ascending' ? 'desc' : 'asc';

                // Reiniciar el resto de las columnas
                encabezados.forEach(function (otro) {
                    otro.removeAttribute('aria-sort');
                    const icono = otro.querySelector('.btn-ordenar i');
                    if (icono) icono.className = 'fa-solid ' + iconoPara(null);
                    otro.classList.remove('columna-ordenada');
                });

                th.setAttribute('aria-sort', direccion === 'asc' ? 'ascending' : 'descending');
                th.classList.add('columna-ordenada');
                boton.querySelector('i').className = 'fa-solid ' + iconoPara(direccion);

                const filas = Array.from(cuerpo.rows);
                const signo = direccion === 'asc' ? 1 : -1;
                filas.sort(function (a, b) {
                    const va = valorCelda(a, indice);
                    const vb = valorCelda(b, indice);
                    let resultado;
                    if (tipo === 'numero') {
                        resultado = (parseFloat(va) || 0) - (parseFloat(vb) || 0);
                    } else {
                        resultado = comparadorTexto.compare(va, vb);
                    }
                    return resultado * signo;
                });
                filas.forEach(function (fila) { cuerpo.appendChild(fila); });
            });
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        document.querySelectorAll('table[data-ordenable]').forEach(prepararTabla);
    });
})();
