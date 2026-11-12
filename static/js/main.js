// Botón de tema claro/oscuro: guarda la elección del usuario.
document.addEventListener("DOMContentLoaded", function () {
    const btns = document.querySelectorAll(".toggle-theme-btn");
    const html = document.documentElement;

    // El tema guardado ya lo aplica un script en el <head> de las plantillas base
    // (antes de dibujar la página, para que no destelle).

    btns.forEach(btn => {
        btn.addEventListener("click", function () {
            const current = html.getAttribute("data-bs-theme");
            const next = current === "dark" ? "light" : "dark";
            html.setAttribute("data-bs-theme", next);

            // Guardar el tema elegido en localStorage
            localStorage.setItem("theme", next);
        });
    });
});

// Efecto de encogimiento para la Navbar
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.classList.add('navbar-scrolled');
    } else {
        header.classList.remove('navbar-scrolled');
    }
});

// Función para cerrar alertas automáticamente desactivada a pedido del usuario
// document.addEventListener("DOMContentLoaded", function() {
//     const alerts = document.querySelectorAll('.alert');
//     alerts.forEach(function(alert) {
//         setTimeout(function() {
//             if (typeof bootstrap !== 'undefined' && bootstrap.Alert) {
//                 const bsAlert = new bootstrap.Alert(alert);
//                 bsAlert.close();
//             } else {
//                 alert.style.display = 'none';
//             }
//         }, 5000);
//     });
// });