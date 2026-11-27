/*
 * Casilla «Institución o empresa» en el alta y la edición de clientes.
 *
 * Al marcarla se oculta el campo «Nombre» (y se vacía al enviar) y queda sólo el
 * «Apellido», rotulado como nombre de la institución. La casilla lleva:
 *   data-institucion, data-nombre="id del nombre", data-apellido="id del apellido",
 *   data-etiqueta="texto del rótulo para la institución".
 * El contenedor que se oculta es el `[data-contenedor-campo]` más cercano al nombre
 * (o su padre directo); el rótulo es el <label for="id del apellido">.
 */
(function () {
    function preparar(casilla) {
        var nombre = document.getElementById(casilla.dataset.nombre);
        var apellido = document.getElementById(casilla.dataset.apellido);
        if (!nombre || !apellido) return;
        var contenedor = nombre.closest('[data-contenedor-campo]') || nombre.parentElement;
        var rotulo = document.querySelector('label[for="' + apellido.id + '"]');
        var columnaApellido = apellido.closest('.col-md-6');  // en las altas, a todo el ancho
        var textoOriginal = rotulo ? rotulo.innerHTML : '';
        var placeholderOriginal = apellido.getAttribute('placeholder') || '';

        function aplicar() {
            var esInstitucion = casilla.checked;
            contenedor.hidden = esInstitucion;
            nombre.disabled = esInstitucion;  // no se envía
            apellido.required = esInstitucion;
            if (columnaApellido) columnaApellido.classList.toggle('col-md-12', esInstitucion);
            if (rotulo) {
                rotulo.innerHTML = esInstitucion
                    ? casilla.dataset.etiqueta + ' <span class="text-danger">*</span>'
                    : textoOriginal;
            }
            apellido.setAttribute('placeholder', esInstitucion ? 'Ej: Escuela N° 1234 Sarmiento' : placeholderOriginal);
        }
        casilla.addEventListener('change', aplicar);
        aplicar();
    }
    document.querySelectorAll('input[data-institucion]').forEach(preparar);
})();
