---
name: verificar-cambios
description: Verificación obligatoria de Distribuidora 3.0 antes de dar por terminada una tarea (check, migraciones pendientes, tests) y actualización de CONTEXT.md / PROCEDURE.md y del grafo. Usar al cerrar cualquier cambio de código o modelos.
---

# Verificar cambios — Distribuidora 3.0

Usar esta skill al terminar cualquier cambio en el proyecto, antes de decir que la tarea está lista.
Las reglas vienen de `.agents/AGENTS.md` (regla 7 y 8).

## 1. Verificación de Django (Windows, PowerShell, desde la raíz del repo)

Correr los tres comandos, en este orden, y no seguir si alguno falla:

```powershell
.\venv\Scripts\python.exe manage.py check --settings=distribuidora.settings.local
.\venv\Scripts\python.exe manage.py makemigrations --check --dry-run --settings=distribuidora.settings.local
.\venv\Scripts\python.exe manage.py test --settings=distribuidora.settings.local
```

- `check` debe dar `0 issues`.
- `makemigrations --check` debe decir `No changes detected`. Si detecta cambios y el cambio de modelo era intencional, crear la migración con nombre descriptivo en español (`makemigrations <app> --name <descripcion>`) y volver a correr los tres comandos.
- `test` debe terminar en `OK`. Informar cuántos tests corrieron (la base al 20/10/2026 es 128).

Si el cambio toca despliegue o settings, correr además:

```powershell
.\venv\Scripts\python.exe manage.py check --deploy --settings=distribuidora.settings.production
```

## 2. Revisar convenciones del proyecto en lo que cambió

- Vistas como funciones (FBV), no clases.
- Chequeos de rol solo con `apps/permisos/roles.py`; en templates, las variables `es_vendedor`, `es_repartidor` y `es_personal_interno` del context processor `roles_usuario` (nunca `user.groups`).
- `desc_seguridad` (RNF-02) solo visible vía `puede_ver_nota_seguridad()`.
- Operaciones que mueven stock, pedidos o cuentas dentro de `transaction.atomic`.
- Textos, nombres y mensajes en español.
- Si se agregó lógica nueva, agregar tests en `apps/<app>/tests.py` (pendiente conocido: buscador, hallazgo H-10).

## 3. Actualizar documentación y grafo

- Si se implementó un requisito, una fase o cambió la arquitectura: actualizar `.agents/CONTEXT.md` (sección del módulo, mapa de URLs, esquema) y `.agents/PROCEDURE.md` (estado de ejecución, matriz de cobertura, hallazgos).
- Si existe `graphify-out/graph.json`, correr `graphify update .` para reflejar el código nuevo.

## 4. Informe final

Cerrar con: qué se cambió, resultado de cada comando (issues, migraciones, cantidad de tests) y qué documentos se actualizaron. Si algo no se pudo verificar, decirlo explícitamente.
