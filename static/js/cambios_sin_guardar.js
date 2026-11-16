/*
 * Aviso de cambios sin guardar (toda la app).
 *
 * Si algún formulario que guarda datos (method="post") tiene cambios y el
 * usuario intenta irse de la página, se le pregunta antes:
 *   - al hacer clic en un enlace: ventana propia (AqPopup / SweetAlert);
 *   - al recargar, cerrar la pestaña o usar «Atrás»: aviso nativo del navegador.
 *
 * Un campo «cambió» si su valor actual difiere del que trajo la página, así
 * que volver a escribir lo original quita el aviso. No cuentan:
 *   - los buscadores y filtros (formularios GET);
 *   - los selects que se guardan solos al cambiar (onchange → submit);
 *   - formularios o campos con el atributo data-sin-aviso.
 */
(function () {
    'use strict';

    let enviando = false;

    function seGuardaSolo(campo) {
        const alCambiar = campo.getAttribute('onchange') || '';
        return alCambiar.indexOf('submit') !== -1;
    }

    function campoCambio(campo) {
        if (campo.disabled || campo.closest('[data-sin-aviso]') || seGuardaSolo(campo)) return false;
        const tipo = (campo.type || '').toLowerCase();
        if (['hidden', 'submit', 'button', 'reset', 'image', 'search'].includes(tipo)) return false;
        if (tipo === 'checkbox' || tipo === 'radio') return campo.checked !== campo.defaultChecked;
        if (tipo === 'file') return campo.files && campo.files.length > 0;
        if (campo.tagName === 'SELECT') {
            const opciones = Array.from(campo.options);
            if (campo.multiple) return opciones.some((op) => op.selected !== op.defaultSelected);
            // Sin opción marcada en el HTML, el navegador muestra la primera.
            const original = Math.max(opciones.findIndex((op) => op.defaultSelected), 0);
            return opciones.length > 0 && campo.selectedIndex !== original;
        }
        return campo.value !== campo.defaultValue;
    }

    function hayCambios() {
        if (enviando) return false;
        return Array.from(document.querySelectorAll('form')).some((form) => {
            if ((form.getAttribute('method') || 'get').toLowerCase() !== 'post') return false;
            if (form.hasAttribute('data-sin-aviso')) return false;
            return Array.from(form.elements).some(campoCambio);
        });
    }

    function preguntar() {
        const mensaje = 'Tenés cambios sin guardar. ¿Querés salir igual?';
        if (window.AqPopup && window.AqPopup.ventana) {
            // Mismo estilo que el resto de las confirmaciones de la app.
            return window.AqPopup.ventana({
                icon: 'warning',
                peligro: true,
                title: mensaje,
                text: 'Si salís, se pierden los cambios.',
                showCancelButton: true,
                confirmButtonText: 'Salir sin guardar',
                cancelButtonText: 'Seguir editando',
                reverseButtons: true,
            }).then((r) => r.isConfirmed);
        }
        return Promise.resolve(window.confirm(mensaje));
    }

    // Guardar no es «salir»: el envío del formulario no dispara el aviso.
    document.addEventListener('submit', (evento) => {
        if (!evento.defaultPrevented) enviando = true;
    });
    // Si el envío se cancela (validación, confirmación), se vuelve a vigilar.
    window.addEventListener('pageshow', () => { enviando = false; });

    // Enlaces internos
    document.addEventListener('click', (evento) => {
        const enlace = evento.target.closest('a[href]');
        if (!enlace || evento.defaultPrevented) return;
        if (evento.button !== 0 || evento.ctrlKey || evento.metaKey || evento.shiftKey || evento.altKey) return;
        if (enlace.target === '_blank' || enlace.hasAttribute('download') || enlace.hasAttribute('data-sin-aviso')) return;
        const href = enlace.getAttribute('href');
        if (!href || href.startsWith('#') || href.startsWith('javascript:') || enlace.dataset.bsToggle) return;
        if (!hayCambios()) return;
        evento.preventDefault();
        preguntar().then((salir) => {
            if (!salir) return;
            enviando = true;   // ya confirmó: que el navegador no vuelva a preguntar
            window.location.href = enlace.href;
        });
    });

    // Recargar, cerrar la pestaña, «Atrás» o escribir otra dirección
    window.addEventListener('beforeunload', (evento) => {
        if (!hayCambios()) return;
        evento.preventDefault();
        evento.returnValue = '';
    });
})();
