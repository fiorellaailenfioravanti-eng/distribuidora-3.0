---
tipo: indice
tags:
  - inicio
---
# 🌊 Distribuidora 3.0 / Aquadelluvia

> [!info] Estado
> Fases 1–6 completadas (más 4.5/4.6 de auditoría). **Fase 7** (QA, buscador RF-07, producción y tesis) es la siguiente.
> Detalle en [[PROCEDURE]] y [[PLAN_CIERRE]].

## 📚 Documentación del proyecto
Vive en `.agents/` (oculta para Obsidian) y se ve acá a través de la carpeta enlazada `Documentacion/`.

| Documento | Para qué |
|---|---|
| [[AGENTS]] | Reglas del workspace |
| [[CONTEXT]] | Qué existe: negocio, stack, modelos |
| [[PROCEDURE]] | Fases, requisitos ↔ código, hallazgos |
| [[PLAN_CIERRE]] | Plan de Fases 4.5 a 7 |
| [[AUDITORIA]] | Auditoría de coherencia |
| [[CONTROL_REQUISITOS]] | Control de cumplimiento de RF/RNF |
| [[DESIGN]] | Patrón visual (tienda y dashboard) |
| [[FASE3_LOGISTICA]] | Diseño de logística |
| [[graphify-out/GRAPH_REPORT\|GRAPH_REPORT]] | Reporte del grafo de código |

## 🧩 Apps Django
Mapa visual: [[Arquitectura.canvas|Arquitectura]]

![[Apps.base]]

## 🧪 QA
Último control: [[QA 2026-11-12]] · reglas: [[Validaciones por campo]] · [[Roles y permisos]]

![[Hallazgos.base#Abiertos]]

## 🧭 Decisiones
![[Decisiones.base#Abiertas]]

## ⚙️ Comandos frecuentes
```powershell
.\venv\Scripts\python.exe manage.py runserver --settings=distribuidora.settings.local
.\venv\Scripts\python.exe manage.py check --settings=distribuidora.settings.local
.\venv\Scripts\python.exe manage.py test --settings=distribuidora.settings.local
.\venv\Scripts\python.exe manage.py seed_demo --settings=distribuidora.settings.local
graphify update .
```

## 🗂️ Cómo está organizado el vault
- `Documentacion/` → enlace a `.agents/` (los docs que leen Claude y el equipo). Editar acá edita los originales.
- `notas/apps/` → una nota por app Django, con modelos y dependencias en las propiedades.
- `notas/decisiones/` → una nota por decisión (plantilla `Decision`).
- `notas/qa/` → controles de calidad; `notas/hallazgos/` → un problema por nota (plantilla `Hallazgo`).
- `notas/diario/` → notas diarias (botón de calendario o `Ctrl+P → Nota diaria`).
- `notas/plantillas/` → plantillas: Nota diaria, Decision, Hallazgo.
- Código, `venv/`, `static/` y `media/` quedan excluidos de búsqueda y grafo.
