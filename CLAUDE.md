# Distribuidora 3.0 / Aquadelluvia

Las reglas del workspace viven en `.agents/AGENTS.md` y se importan acá para que Claude Code las lea al abrir el proyecto:

@.agents/AGENTS.md

Resumen operativo:
- Antes de proponer cambios, revisar `.agents/CONTEXT.md` (qué existe) y `.agents/PROCEDURE.md` (fase actual). Fases 1–6 completadas (más 4.5/4.6 de auditoría); Fase 7 (QA, RF-07, producción y tesis) es la siguiente. Datos de demo: `manage.py seed_demo`.
- Todo en español: código, comentarios, templates y mensajes.
- Django 5.0 con Function-Based Views (no CBV). Settings de desarrollo: `--settings=distribuidora.settings.local`.
- Permisos: usar siempre `apps/permisos/roles.py` (`es_admin_o_vendedor`, `puede_ver_nota_seguridad`, etc.); no reimplementar chequeos de grupo en las apps.
- Al terminar una tarea, usar la skill `verificar-cambios`.

# graphify
- **graphify** (`.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.
- If the `graphify` command is not found, install it once with `pip install graphifyy` (outside the project venv, e.g. `py -m pip install --user graphifyy` or `pipx install graphifyy`), then retry.
- The graph also links each requirement (RF-xx / RNF-xx), phase and open finding from `.agents/PROCEDURE.md` to the code that implements it: `graphify explain "RF-14"` or `graphify query "Fase 5"`.
