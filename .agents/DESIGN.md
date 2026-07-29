# 🎨 Patrón de Diseño Visual — Aquadelluvia (Distribuidora 3.0)

Este documento establece las guías de estilo, paleta de colores, márgenes, bordes y principios visuales a utilizar en todo el frontend de la aplicación web (Django Templates + Bootstrap 5.3). 

**DEBE** ser consultado antes de crear o modificar cualquier componente visual para mantener la coherencia estética del proyecto.

---

## 1. 🌊 Identidad Visual y Concepto
**Agua de Lluvia** cuenta con un logotipo vibrante, amigable y familiar. El diseño web debe replicar esa calidez:
- **Amigable y Familiar:** Colores vivos extraídos de la mascota (rana verde) y el entorno otoñal (amarillos/naranjas).
- **Frescura:** El azul claro y luminoso de la tipografía del logo actúa como color principal para transmitir pureza y limpieza.
- **Fluidez:** Uso de micro-animaciones (hover, transiciones) simulando el movimiento del agua.

---

## 2. 🎨 Paleta de Colores (Basada en el Logo)

Se deben usar estas variables CSS personalizadas extendiendo Bootstrap 5.3.

### Tema Claro (Light Mode)
El tema claro prioriza la luz del entorno natural del logo.
- **Fondo Principal (`--bg-main`):** `#F4F7F6` (Blanco nube suave)
- **Fondo Tarjetas/Paneles (`--bg-surface`):** `#FFFFFF` (Blanco puro, como el banderín del logo)
- **Primario (`--color-primary`):** `#6CB4EE` (Azul Agua de Lluvia - Celeste brillante del texto del logo)
- **Secundario (`--color-secondary`):** `#8BC34A` (Verde Rana - Extraído de la mascota)
- **Acento (`--color-accent`):** `#F5B041` (Naranja/Amarillo Otoño - Extraído de los árboles de fondo)
- **Texto Principal (`--text-main`):** `#2C3E50` (Pizarra oscuro - Para legibilidad sin ser negro puro)
- **Texto Secundario (`--text-muted`):** `#7F8C8D`

### Tema Oscuro (Dark Mode) - *Por defecto según CONTEXT.md*
El tema oscuro contrasta los colores vivos del logo sobre un fondo elegante y moderno.
- **Fondo Principal (`--bg-main`):** `#1A252C` (Pizarra muy oscuro)
- **Fondo Tarjetas/Paneles (`--bg-surface`):** `#273746` (Pizarra superficie)
- **Primario (`--color-primary`):** `#5DADE2` (Azul Agua de Lluvia - Adaptado para brillar en fondo oscuro)
- **Secundario (`--color-secondary`):** `#7CB342` (Verde Rana)
- **Acento (`--color-accent`):** `#F39C12` (Naranja/Amarillo Otoño)
- **Texto Principal (`--text-main`):** `#EAEDED` (Blanco suave)
- **Texto Secundario (`--text-muted`):** `#95A5A6`

---

## 3. 📝 Tipografía (Fuentes y Títulos)

Para continuar con el enfoque familiar y amigable inspirado en el logo:
- **Títulos y Encabezados (`h1`, `h2`, `h3`, `navbar-brand`):** Se usa la fuente **Nunito** (peso `800` o `700`). Es una fuente redondeada y juguetona que evoca las burbujas y el tono infantil/amigable de la rana.
    - El `h1` usa un tamaño ampliado (`2.5rem`) y por defecto siempre toma el color Primario (Azul Agua de Lluvia) para impactar.
    - El `h2` (`2rem`) y `h3` (`1.75rem`) mantienen el color del texto principal.
- **Cuerpo del Texto (Párrafos, Tablas, Botones):** Se usa la fuente **Inter**, que es extremadamente legible en tamaños pequeños para mantener el panel de administración profesional y fácil de usar.

### Colores Semánticos (Ambos temas)
- **Éxito (Success):** `#20C997` (Verde agua/Teal)
- **Advertencia (Warning):** `#FFCA2C` (Amarillo sol)
- **Peligro (Danger):** `#E63946` (Rojo atenuado)
- **Información (Info):** `#0DCAF0` (Cyan)

---

## 3. 📐 Espaciado (Márgenes y Paddings)

El proyecto utiliza el sistema de espaciado de Bootstrap (0-5) con los siguientes principios:

- **Contenedores Principales:** Padding interno amplio para respirar. Clases sugeridas: `py-4 py-md-5`, `px-3 px-md-4`.
- **Tarjetas y Paneles (`.card`):** `p-3` o `p-4` dependiendo del contenido. Nunca pegar el texto a los bordes.
- **Separación de Secciones:** `mb-4` o `mb-5` para separar grandes bloques de contenido.
- **Elementos de Formularios y Botones:** Usar márgenes inferiores consistentes (`mb-3` para `.form-group`).

---

## 4. 🔲 Bordes y Sombras (Glassmorphism sutil)

Para dar un aspecto moderno y orgánico:

- **Radio de Borde (Border Radius):** 
  - Elementos pequeños (botones, inputs): `0.5rem` (`rounded-2` o `rounded-3`).
  - Tarjetas, modales y contenedores grandes: `1rem` o `1.25rem` (`rounded-4`).
  - Evitar bordes completamente rectos (`rounded-0`) salvo requerimiento específico.
- **Bordes (Borders):**
  - **Light mode:** Bordes muy sutiles (`border border-light-subtle`) o sin borde.
  - **Dark mode:** Borde semi-transparente para separar componentes (`border border-secondary-subtle` con baja opacidad, ej: `rgba(255,255,255,0.05)`).
- **Sombras (Shadows):**
  - **Light mode:** Sombras suaves y difusas (`shadow-sm` para inputs, `shadow` para tarjetas flotantes).
  - **Dark mode:** Sombras más oscuras y concentradas para dar profundidad sin ensuciar el diseño (`box-shadow: 0 4px 15px rgba(0,0,0,0.3)`), o resplandor sutil (glow) en botones primarios.

---

## 5. ✍️ Tipografía

- **Fuente Principal:** Preferentemente fuentes modernas sin serif como `Inter`, `Roboto` o similar (dependiendo de la importación).
- **Jerarquía:**
  - `h1` a `h3`: Grosores altos (`fw-bold` o `fw-semibold`), color primario o texto principal.
  - Párrafos: Grosor normal (`fw-normal`), color texto secundario (`text-muted` o `--text-muted`) para mejorar la lectura si el texto es extenso.
- **Botones y Badges:** Texto claro, si aplica en mayúsculas pequeñas o con `fw-semibold` o `fw-bold`.

---

## 6. 🪄 Interacciones y Animaciones (Micro-animaciones)

Las interacciones deben sentirse fluidas ("líquidas"):
- **Hover en Botones y Tarjetas:**
  - Transición suave: usar clase custom con `transition: all 0.3s ease;`.
  - Las tarjetas interactivas deben elevarse ligeramente al hacer hover (`transform: translateY(-3px);`).
- **Focus en Inputs:**
  - Al hacer foco en un input, el borde debe iluminarse, eliminando el outline fuerte por defecto y reemplazándolo por una sombra (box-shadow) del color Primario/Secundario transparente.

---

## 7. 🧩 Guía de Componentes Bootstrap Modificados

### Botones (`.btn`)
- **Acciones principales:** Botones con fondo sólido y esquinas redondeadas (`btn-primary rounded-pill` o `rounded-3`).
- **Acciones secundarias:** Botones outline (`btn-outline-primary` o `btn-outline-secondary`).
- No usar bordes rectos.

### Tarjetas (`.card`)
- Fondo adaptado según el tema (usar las clases de fondo o estilo custom).
- Borde eliminado o muy fino y sutil.
- Sombra sutil (`shadow-sm` o clase custom).
- `border-radius` amplio (`rounded-4`).

### Formularios (`.form-control`)
- Bordes redondeados (`rounded-3`).
- Padding confortable (`py-2 px-3`).
- En Dark Mode, fondo ligeramente distinto al fondo principal (ej. fondo de tarjeta) para diferenciar inputs.

### Badges (`.badge`)
- Usar colores semánticos suaves con `bg-opacity` (ej. `bg-success bg-opacity-25 text-success`) en lugar de fondos sólidos intensos, para lograr un look más moderno y prolijo.

---

**NOTA PARA AGENTES AI:** Cuando se deba crear o modificar vistas (`.html` / `.css`), se debe revisar e inyectar las clases de Bootstrap 5.3 que respeten estos radios, sombras y colores. Si se requiere CSS personalizado, crear o usar las variables documentadas aquí.
