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

👉 [`.agents/PROCEDURE.md`](.agents/PROCEDURE.md)

Este archivo contiene:
- Diagnóstico de divergencia entre el código, `CONTEXT.md` y el Informe de Avances de Tesis
- Matriz de cobertura de los 22 Requerimientos (RF-01…RF-19, RNF-01…RNF-03)
- Hallazgos técnicos verificados con su severidad
- **Plan de procedimiento por fases (Fase 0 → Fase 7)** con tareas, dependencias y criterios de aceptación
- Decisiones de alcance pendientes de resolver por el equipo

👉 [`.agents/PLAN_CIERRE.md`](.agents/PLAN_CIERRE.md) — procedimiento detallado de las Fases 4.5 a 7.

👉 [`.agents/AUDITORIA.md`](.agents/AUDITORIA.md) — auditoría de coherencia (H-18…H-39, R-1…R-8) y su estado.


---

## 🧭 Reglas de Trabajo

1. **Contexto primero:** Antes de proponer cualquier cambio, verificar en `CONTEXT.md` si la funcionalidad ya existe o si está en el roadmap pendiente.
2. **Plan vigente:** Consultar `PROCEDURE.md` para saber en qué fase está el proyecto y qué tarea corresponde. No iniciar trabajo que pertenezca a una fase posterior a la actual.
3. **No romper lo existente:** Los módulos `autenticacion`, `productos`, `carrito` y `buscador` están funcionales. Cualquier cambio estructural requiere análisis de impacto.
4. **Idioma:** El proyecto es completamente en **español** (código, comentarios, templates, mensajes al usuario).
5. **Settings:** Usar siempre `--settings=distribuidora.settings.local` para desarrollo.
6. **Zona horaria:** `America/Argentina/Buenos_Aires` — tener en cuenta para fechas y vencimientos.
7. **Verificación obligatoria** antes de dar por terminada cualquier tarea:
   ```powershell
   .\venv\Scripts\python.exe manage.py check --settings=distribuidora.settings.local
   .\venv\Scripts\python.exe manage.py makemigrations --check --dry-run --settings=distribuidora.settings.local
   .\venv\Scripts\python.exe manage.py test --settings=distribuidora.settings.local
   ```
8. **Actualizar el contexto:** Si se implementa un módulo pendiente o se cambia la arquitectura, actualizar `.agents/CONTEXT.md` y `.agents/PROCEDURE.md` acordemente.
