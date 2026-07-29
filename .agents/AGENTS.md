# AGENTS.md — Reglas del Workspace: Distribuidora 3.0 / Aquadelluvia

## 📌 Contexto del Proyecto

**SIEMPRE** lee el archivo de contexto antes de comenzar cualquier tarea en este workspace:

👉 [`.agents/CONTEXT.md`](.agents/CONTEXT.md)

Este archivo contiene:
- Descripción completa del proyecto (tesis universitaria, empresa Aquadelluvia)
- Stack tecnológico y arquitectura Django MVT
- Todos los modelos de datos implementados y planificados
- Separación clara de **lo realizado** vs **lo pendiente**
- Mapa de URLs actual
- Deuda técnica crítica

👉 [`.agents/DESIGN.md`](.agents/DESIGN.md)

Este archivo contiene:
- Patrón de diseño visual de toda la aplicación (colores para tema oscuro y claro)
- Configuración de espaciados, bordes y tipografía
- Guía para componentes Bootstrap


---

## 🧭 Reglas de Trabajo

1. **Contexto primero:** Antes de proponer cualquier cambio, verificar en `CONTEXT.md` si la funcionalidad ya existe o si está en el roadmap pendiente.
2. **No romper lo existente:** Los módulos `autenticacion`, `productos`, `carrito` y `buscador` están funcionales. Cualquier cambio estructural requiere análisis de impacto.
3. **Idioma:** El proyecto es completamente en **español** (código, comentarios, templates, mensajes al usuario).
4. **Settings:** Usar siempre `--settings=distribuidora.settings.local` para desarrollo.
5. **Zona horaria:** `America/Argentina/Buenos_Aires` — tener en cuenta para fechas y vencimientos.
6. **Actualizar el contexto:** Si se implementa un módulo pendiente o se cambia la arquitectura, actualizar `.agents/CONTEXT.md` acordemente.
