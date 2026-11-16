/* Secciones desplegables
   Una tarjeta con data-desplegable="clave" convierte su .card-header en un botón
   que pliega o despliega el resto de la tarjeta. Empiezan plegadas; cada sección
   recuerda si quedó abierta (por navegador). Si adentro hay un error de
   formulario, se abre sola. */
(function () {
    'use strict';

    function leer(clave) {
        try { return localStorage.getItem('seccion:' + clave); } catch (e) { return null; }
    }
    function guardar(clave, abierta) {
        try { localStorage.setItem('seccion:' + clave, abierta ? '1' : '0'); } catch (e) { /* sin almacenamiento */ }
    }

    document.querySelectorAll('.card[data-desplegable]').forEach(function (tarjeta, i) {
        const encabezado = tarjeta.querySelector(':scope > .card-header');
        if (!encabezado) return;
        const clave = tarjeta.dataset.desplegable || ('seccion-' + i);
        const id = 'desplegable-' + clave;

        // Todo lo que sigue al encabezado va dentro del panel que se pliega.
        const panel = document.createElement('div');
        panel.className = 'collapse';
        panel.id = id;
        while (encabezado.nextSibling) panel.appendChild(encabezado.nextSibling);
        tarjeta.appendChild(panel);

        const conError = panel.querySelector('.is-invalid, .invalid-feedback, .errorlist, .alert-danger');
        const abierta = conError ? true : leer(clave) === '1';
        if (abierta) panel.classList.add('show');

        encabezado.classList.add('seccion-desplegable__encabezado');
        encabezado.setAttribute('role', 'button');
        encabezado.setAttribute('tabindex', '0');
        encabezado.setAttribute('aria-controls', id);
        encabezado.setAttribute('aria-expanded', abierta ? 'true' : 'false');
        const flecha = document.createElement('i');
        flecha.className = 'fa-solid fa-chevron-down seccion-desplegable__flecha ms-3';
        flecha.setAttribute('aria-hidden', 'true');
        encabezado.appendChild(flecha);
        if (!abierta) tarjeta.classList.add('seccion-desplegable--plegada');

        const colapso = new bootstrap.Collapse(panel, { toggle: false });
        function alternar(evento) {
            if (evento.target.closest('a, button, input, select, textarea, label')) return;
            colapso.toggle();
        }
        encabezado.addEventListener('click', alternar);
        encabezado.addEventListener('keydown', function (evento) {
            if (evento.key === 'Enter' || evento.key === ' ') { evento.preventDefault(); colapso.toggle(); }
        });
        panel.addEventListener('show.bs.collapse', function (e) {
            if (e.target !== panel) return;
            encabezado.setAttribute('aria-expanded', 'true');
            tarjeta.classList.remove('seccion-desplegable--plegada');
            guardar(clave, true);
        });
        panel.addEventListener('hide.bs.collapse', function (e) {
            if (e.target !== panel) return;
            encabezado.setAttribute('aria-expanded', 'false');
            tarjeta.classList.add('seccion-desplegable--plegada');
            guardar(clave, false);
        });
    });
})();
