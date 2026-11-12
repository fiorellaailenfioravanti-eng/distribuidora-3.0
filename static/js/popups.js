/*
 * Popups de Aquadelluvia (SweetAlert2).
 *
 * 1. Mensajes de Django (messages framework): éxito e info como aviso flotante
 *    que se cierra solo; advertencias y errores como ventana que hay que cerrar.
 * 2. Errores de validación que devuelve el servidor: se juntan los de todos los
 *    campos del formulario, se marcan los campos y se muestran en una ventana.
 * 3. Validación del navegador antes de enviar (campos obligatorios, mínimos,
 *    formato de email...): misma ventana, sin recargar la página.
 * 4. Confirmaciones: cualquier <form data-confirmar="¿...?"> o
 *    <a|button data-confirmar="¿...?"> pide confirmación antes de seguir.
 */
(function () {
    'use strict';

    if (typeof Swal === 'undefined') {
        return; // Sin la librería (sin conexión) quedan los mensajes en línea de cada formulario.
    }

    const ICONOS = { success: 'success', error: 'error', warning: 'warning', info: 'info', debug: 'info' };
    const TITULOS = { success: 'Listo', error: 'Hubo un problema', warning: 'Atención', info: 'Información' };

    const popup = Swal.mixin({
        customClass: {
            popup: 'aq-popup',
            confirmButton: 'btn btn-primary rounded-pill px-4 mx-1',
            cancelButton: 'btn btn-light rounded-pill px-4 mx-1',
        },
        buttonsStyling: false,
        confirmButtonText: 'Entendido',
    });

    const aviso = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 4500,
        timerProgressBar: true,
        customClass: { popup: 'aq-popup aq-toast' },
        didOpen: (t) => {
            t.addEventListener('mouseenter', Swal.stopTimer);
            t.addEventListener('mouseleave', Swal.resumeTimer);
        },
    });

    function escapar(texto) {
        const div = document.createElement('div');
        div.textContent = texto;
        return div.innerHTML;
    }

    function listaHtml(items) {
        return '<ul class="aq-popup-lista">' + items.map((i) => '<li>' + i + '</li>').join('') + '</ul>';
    }

    // Exponer para usar desde otros scripts: AqPopup.exito('...'), AqPopup.error('...').
    window.AqPopup = {
        exito: (texto) => aviso.fire({ icon: 'success', title: texto }),
        info: (texto) => aviso.fire({ icon: 'info', title: texto }),
        advertencia: (texto) => popup.fire({ icon: 'warning', title: TITULOS.warning, text: texto }),
        error: (texto) => popup.fire({ icon: 'error', title: TITULOS.error, text: texto }),
    };

    // ── 1. Mensajes de Django ──────────────────────────────────────────
    function leerMensajes() {
        const nodo = document.getElementById('mensajes-django');
        if (!nodo) return [];
        try { return JSON.parse(nodo.textContent); } catch (e) { return []; }
    }

    function mostrarAvisos(leves) {
        if (!leves.length) return;
        const nivel = leves.some((m) => /success/.test(m.nivel)) ? 'success' : 'info';
        const textos = leves.map((m) => escapar(m.texto));
        aviso.fire({ icon: ICONOS[nivel], title: textos.length > 1 ? '' : textos[0],
                     html: textos.length > 1 ? listaHtml(textos) : undefined });
    }

    /* Un solo popup para los mensajes graves y los errores de campo;
       los avisos de éxito/info salen después como toast. */
    function mostrarTodo() {
        const mensajes = leerMensajes();
        const graves = mensajes.filter((m) => /error|warning/.test(m.nivel));
        const leves = mensajes.filter((m) => !/error|warning/.test(m.nivel));
        const errores = [];
        document.querySelectorAll('form').forEach((form) => errores.push(...erroresDelServidor(form)));

        if (!graves.length && !errores.length) return mostrarAvisos(leves);

        const nivel = errores.length || graves.some((m) => /error/.test(m.nivel)) ? 'error' : 'warning';
        const items = graves.map((m) => escapar(m.texto)).concat(errores);
        popup.fire({
            icon: ICONOS[nivel],
            title: errores.length ? 'Revisá los datos ingresados' : TITULOS[nivel],
            html: items.length > 1 ? listaHtml(items) : items[0],
        }).then(() => {
            const primero = document.querySelector('.is-invalid');
            if (primero) primero.focus();
            mostrarAvisos(leves);
        });
    }

    // ── 2 y 3. Errores de formularios ──────────────────────────────────
    const SELECTOR_CAMPO = 'input:not([type=hidden]):not([type=submit]):not([type=button]), select, textarea';
    const SELECTOR_ERROR = '.errorlist, .invalid-feedback, div.text-danger, span.text-danger, small.text-danger';

    function etiquetaDe(campo) {
        if (campo.id) {
            const label = document.querySelector('label[for="' + CSS.escape(campo.id) + '"]');
            if (label && label.textContent.trim()) return label.textContent.trim().replace(/\s*\*$/, '');
        }
        // Label sin "for": el del mismo bloque del formulario.
        let bloque = campo.parentElement;
        for (let i = 0; bloque && i < 3; i++, bloque = bloque.parentElement) {
            const label = bloque.querySelector('label:not(.form-check-label)');
            if (label && label.textContent.trim() && bloque.querySelectorAll(SELECTOR_CAMPO).length === 1) {
                return label.textContent.trim().replace(/\s*\*$/, '');
            }
        }
        return campo.getAttribute('aria-label') || campo.name || 'Campo';
    }

    function mensajeDe(campo) {
        const v = campo.validity;
        if (v.valueMissing) return 'Es obligatorio.';
        if ((v.patternMismatch || v.typeMismatch) && campo.title) return campo.title;
        if (v.tooShort) return 'Debe tener al menos ' + campo.minLength + ' caracteres.';
        if (v.rangeUnderflow) return 'El mínimo es ' + campo.min + '.';
        if (v.rangeOverflow) return 'El máximo es ' + campo.max + '.';
        if (v.typeMismatch && campo.type === 'email') return 'Escribí un email válido (ej: nombre@correo.com).';
        return campo.validationMessage;
    }

    function erroresDelServidor(form) {
        const items = [];
        const vistos = new Set();
        form.querySelectorAll(SELECTOR_ERROR).forEach((nodo) => {
            const texto = nodo.textContent.replace(/\s+/g, ' ').trim();
            if (!texto || vistos.has(nodo) || nodo.closest('button, a, label, table')) return;
            if (nodo.parentElement && nodo.parentElement.closest(SELECTOR_ERROR)) return; // anidado
            // El campo es el control del mismo bloque que el mensaje.
            const bloque = nodo.parentElement;
            const campo = bloque ? bloque.querySelector(SELECTOR_CAMPO) : null;
            const esMensajeDeError = nodo.matches('.errorlist, .invalid-feedback');
            if (!campo && !esMensajeDeError) return; // texto rojo decorativo, no un error
            vistos.add(nodo);
            if (campo) {
                campo.classList.add('is-invalid');
                items.push('<strong>' + escapar(etiquetaDe(campo)) + ':</strong> ' + escapar(texto));
            } else {
                items.push(escapar(texto));
            }
        });
        form.querySelectorAll('.alert-danger').forEach((alerta) => {
            const texto = alerta.textContent.replace(/\s+/g, ' ').trim();
            if (texto) items.unshift(escapar(texto));
        });
        return items;
    }

    function validarAntesDeEnviar(evento) {
        const form = evento.target;
        // checkValidity() sigue evaluando required/pattern/min aunque el form sea novalidate.
        if (!(form instanceof HTMLFormElement) || form.dataset.aqValidar !== '1' || form.checkValidity()) return;
        evento.preventDefault();
        evento.stopImmediatePropagation();
        const items = [];
        form.querySelectorAll(SELECTOR_CAMPO).forEach((campo) => {
            if (campo.willValidate && !campo.validity.valid) {
                campo.classList.add('is-invalid');
                items.push('<strong>' + escapar(etiquetaDe(campo)) + ':</strong> ' + escapar(mensajeDe(campo)));
            }
        });
        popup.fire({ icon: 'error', title: 'Faltan datos o hay campos inválidos', html: listaHtml(items) })
            .then(() => { const p = form.querySelector('.is-invalid'); if (p) p.focus(); });
    }

    // Filtro mientras se escribe: el campo no acepta caracteres de otro tipo.
    const FILTROS = {
        soloNumeros: /\D/g,                 // DNI y otros códigos numéricos
        soloTelefono: /[^\d\s()+-]/g,       // teléfonos
    };
    function filtroDe(campo) {
        if (!(campo instanceof HTMLInputElement)) return null;
        if (campo.dataset.soloNumeros !== undefined) return FILTROS.soloNumeros;
        if (campo.dataset.soloTelefono !== undefined) return FILTROS.soloTelefono;
        return null;
    }
    // Bloquea la tecla antes de que entre (así no ocupa lugar del maxlength).
    document.addEventListener('beforeinput', (e) => {
        const filtro = filtroDe(e.target);
        if (filtro && e.data && e.data.replace(filtro, '') !== e.data) {
            e.preventDefault();
            const limpio = e.data.replace(filtro, '');
            if (limpio) {
                const c = e.target;
                const max = c.maxLength > 0 ? c.maxLength : Infinity;
                const sinSeleccion = c.value.length - (c.selectionEnd - c.selectionStart);
                c.setRangeText(limpio.slice(0, Math.max(0, max - sinSeleccion)), c.selectionStart, c.selectionEnd, 'end');
            }
        }
    }, true);
    // Limpieza final (autocompletar, arrastrar texto) y patente en mayúsculas.
    document.addEventListener('input', (e) => {
        const campo = e.target;
        const filtro = filtroDe(campo);
        if (filtro) {
            const limpio = campo.value.replace(filtro, '');
            if (limpio !== campo.value) campo.value = limpio;
        }
        if (campo instanceof HTMLInputElement && campo.style.textTransform === 'uppercase') {
            campo.value = campo.value.toUpperCase();
        }
    }, true);

    // Al corregir un campo se le quita la marca roja.
    document.addEventListener('input', (e) => {
        if (e.target.classList && e.target.classList.contains('is-invalid')) e.target.classList.remove('is-invalid');
    });
    document.addEventListener('change', (e) => {
        if (e.target.classList && e.target.classList.contains('is-invalid')) e.target.classList.remove('is-invalid');
    });

    // ── 4. Confirmaciones ──────────────────────────────────────────────
    function confirmar(mensaje, peligro) {
        return popup.fire({
            icon: peligro ? 'warning' : 'question',
            title: mensaje,
            showCancelButton: true,
            confirmButtonText: 'Sí, continuar',
            cancelButtonText: 'Cancelar',
            reverseButtons: true,
            customClass: {
                popup: 'aq-popup',
                confirmButton: 'btn ' + (peligro ? 'btn-danger' : 'btn-primary') + ' rounded-pill px-4 mx-1',
                cancelButton: 'btn btn-light rounded-pill px-4 mx-1',
            },
        }).then((r) => r.isConfirmed);
    }

    document.addEventListener('submit', (evento) => {
        const form = evento.target;
        validarAntesDeEnviar(evento);
        if (evento.defaultPrevented) return;
        const mensaje = form.dataset.confirmar;
        if (!mensaje || form.dataset.confirmado === '1') return;
        evento.preventDefault();
        confirmar(mensaje, form.dataset.peligro !== undefined).then((ok) => {
            if (!ok) return;
            form.dataset.confirmado = '1';
            const boton = evento.submitter;
            if (form.requestSubmit) form.requestSubmit(boton || undefined); else form.submit();
        });
    }, true);

    document.addEventListener('click', (evento) => {
        const disparador = evento.target.closest('a[data-confirmar], button[data-confirmar]');
        if (!disparador || disparador.dataset.confirmado === '1') return;
        evento.preventDefault();
        evento.stopPropagation();
        confirmar(disparador.dataset.confirmar, disparador.dataset.peligro !== undefined).then((ok) => {
            if (!ok) return;
            disparador.dataset.confirmado = '1';
            disparador.click();
            delete disparador.dataset.confirmado;
        });
    }, true);

    document.addEventListener('DOMContentLoaded', () => {
        // El navegador mostraría su globo nativo y no dispararía 'submit':
        // tomamos la validación (los formularios con novalidate quedan como están).
        document.querySelectorAll('form').forEach((form) => {
            if (!form.noValidate) {
                form.dataset.aqValidar = '1';
                form.noValidate = true;
            }
        });
        mostrarTodo();
    });
})();
