/*
 * Popups de Aguadelluvia (SweetAlert2).
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

    // Íconos propios (Font Awesome) en lugar de los dibujos animados de SweetAlert.
    const ICONO_FA = {
        success: 'fa-check', error: 'fa-xmark', warning: 'fa-exclamation',
        info: 'fa-info', question: 'fa-question',
    };
    const iconoHtml = (tipo) => '<i class="fa-solid ' + (ICONO_FA[tipo] || ICONO_FA.info) + '"></i>';

    /** Ventana modal (errores, advertencias, confirmaciones). */
    function ventana(opciones) {
        const tipo = opciones.icon || 'info';
        const peligro = opciones.peligro;
        delete opciones.peligro;
        return Swal.fire(Object.assign({
            iconHtml: iconoHtml(tipo),
            buttonsStyling: false,
            confirmButtonText: 'Entendido',
            showClass: { popup: 'aq-entrar' },
            hideClass: { popup: 'aq-salir' },
            customClass: {
                popup: 'aq-popup aq-tipo-' + tipo,
                icon: 'aq-icono',
                confirmButton: 'btn ' + (peligro ? 'btn-danger' : 'btn-primary') + ' rounded-pill px-4 mx-1',
                cancelButton: 'btn btn-light rounded-pill px-4 mx-1',
                actions: 'aq-acciones',
            },
        }, opciones));
    }

    // Los avisos salen justo debajo del encabezado visible (su alto cambia con el ancho de pantalla).
    function actualizarTope() {
        const encabezado = document.querySelector('header, .top-header, nav.navbar');
        const borde = encabezado ? encabezado.getBoundingClientRect().bottom : 0;
        document.documentElement.style.setProperty('--aq-tope', Math.max(12, Math.round(borde) + 12) + 'px');
    }
    window.addEventListener('scroll', actualizarTope, { passive: true });
    window.addEventListener('resize', actualizarTope);

    /**
     * Aviso flotante (éxito, información): cada mensaje es su propia tarjeta,
     * apiladas debajo del encabezado. Se cierra sola (pausa al pasar el mouse)
     * o con la X. No usa SweetAlert: así varios avisos conviven sin taparse.
     */
    const DURACION_AVISO = 5000;
    function contenedorAvisos() {
        let c = document.getElementById('aq-avisos');
        if (!c) {
            c = document.createElement('div');
            c.id = 'aq-avisos';
            c.setAttribute('aria-live', 'polite');
            document.body.appendChild(c);
        }
        return c;
    }
    function cerrarAviso(aviso) {
        if (aviso.dataset.cerrando) return;
        aviso.dataset.cerrando = '1';
        aviso.classList.add('aq-aviso--saliendo');
        setTimeout(() => aviso.remove(), 200);
    }
    function avisar(opciones) {
        const tipo = opciones.icon || 'info';
        actualizarTope();
        const aviso = document.createElement('div');
        aviso.className = 'aq-aviso aq-tipo-' + tipo;
        aviso.setAttribute('role', tipo === 'error' ? 'alert' : 'status');
        aviso.innerHTML =
            '<span class="aq-aviso-icono">' + iconoHtml(tipo) + '</span>' +
            '<div class="aq-aviso-texto">' + (opciones.html || escapar(opciones.title || '')) + '</div>' +
            '<button type="button" class="aq-aviso-cerrar" aria-label="Cerrar"><i class="fa-solid fa-xmark"></i></button>' +
            '<span class="aq-aviso-barra" style="animation-duration:' + DURACION_AVISO + 'ms"></span>';
        aviso.querySelector('.aq-aviso-cerrar').addEventListener('click', () => cerrarAviso(aviso));
        aviso.querySelector('.aq-aviso-barra').addEventListener('animationend', () => cerrarAviso(aviso));
        const contenedor = contenedorAvisos();
        contenedor.appendChild(aviso);
        // Como máximo 4 a la vez: el más viejo se va.
        const avisos = contenedor.querySelectorAll('.aq-aviso:not(.aq-aviso--saliendo)');
        if (avisos.length > 4) cerrarAviso(avisos[0]);
        return Promise.resolve();
    }

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
        exito: (texto) => avisar({ icon: 'success', title: texto }),
        info: (texto) => avisar({ icon: 'info', title: texto }),
        advertencia: (texto) => ventana({ icon: 'warning', title: TITULOS.warning, text: texto }),
        error: (texto) => ventana({ icon: 'error', title: TITULOS.error, text: texto }),
        // Ventana con el estilo de la app (otros scripts: aviso de cambios sin guardar).
        ventana: ventana,
    };

    // ── 1. Mensajes de Django ──────────────────────────────────────────
    function leerMensajes() {
        const nodo = document.getElementById('mensajes-django');
        if (!nodo) return [];
        try { return JSON.parse(nodo.textContent); } catch (e) { return []; }
    }

    function mostrarAvisos(leves) {
        // Uno por mensaje, cada uno con su tipo, con un pequeño escalonado.
        leves.forEach((m, i) => setTimeout(() => avisar({ icon: ICONOS[m.nivel] || 'info', title: m.texto }), i * 120));
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
        ventana({
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

    // Nombre de un grupo de opciones: data-etiqueta, <legend> o el título de la tarjeta.
    function etiquetaDeGrupo(campo) {
        const marcado = campo.closest('[data-etiqueta]');
        if (marcado) return marcado.dataset.etiqueta;
        const leyenda = campo.closest('fieldset') && campo.closest('fieldset').querySelector('legend');
        if (leyenda && leyenda.textContent.trim()) return leyenda.textContent.trim().replace(/\s*\*$/, '');
        const titulo = campo.closest('.card') && campo.closest('.card').querySelector('.card-header');
        if (titulo && titulo.textContent.trim()) return titulo.textContent.replace(/\s+/g, ' ').trim().replace(/^\d+\s*/, '');
        return campo.name.replace(/_/g, ' ');
    }

    function mensajeDe(campo) {
        const v = campo.validity;
        if (v.customError) return campo.validationMessage;  // p. ej. tope de stock (main.js)
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
        const gruposVistos = new Set();
        form.querySelectorAll(SELECTOR_CAMPO).forEach((campo) => {
            if (campo.willValidate && !campo.validity.valid) {
                campo.classList.add('is-invalid');
                // Las opciones (radio) de un mismo campo son un solo error, no uno por opción.
                if (campo.type === 'radio') {
                    if (gruposVistos.has(campo.name)) return;
                    gruposVistos.add(campo.name);
                    const msj = campo.validity.valueMissing ? 'Elegí una opción.' : mensajeDe(campo);
                    items.push('<strong>' + escapar(etiquetaDeGrupo(campo)) + ':</strong> ' + escapar(msj));
                    return;
                }
                items.push('<strong>' + escapar(etiquetaDe(campo)) + ':</strong> ' + escapar(mensajeDe(campo)));
            }
        });
        ventana({ icon: 'error', title: 'Faltan datos o hay campos inválidos', html: listaHtml(items) })
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
        return ventana({
            icon: peligro ? 'warning' : 'question',
            peligro: peligro,
            title: mensaje,
            showCancelButton: true,
            confirmButtonText: peligro ? 'Sí, eliminar' : 'Sí, continuar',
            cancelButtonText: 'Cancelar',
            reverseButtons: true,
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
            if (!ok) {
                // Un desplegable que envía al cambiar vuelve a su opción inicial si se cancela.
                form.querySelectorAll('select[data-restablecer-al-cancelar]').forEach((s) => { s.selectedIndex = 0; });
                return;
            }
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
