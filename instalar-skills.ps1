# Instala las skills de Claude Code de este proyecto y el CLI de graphify.
# Uso (desde la raiz del repo, en PowerShell):
#   powershell -ExecutionPolicy Bypass -File .\instalar-skills.ps1

$ErrorActionPreference = 'Stop'
$raiz    = $PSScriptRoot
$origen  = Join-Path $raiz 'skills-claude'
$destino = Join-Path $raiz '.claude\skills'

if (-not (Test-Path $origen)) { throw "No se encontro la carpeta $origen" }

New-Item -ItemType Directory -Force -Path $destino | Out-Null
Get-ChildItem -Directory $origen | ForEach-Object {
    $dst = Join-Path $destino $_.Name
    if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
    Copy-Item -Recurse $_.FullName $dst
    Write-Host "Skill instalada: .claude\skills\$($_.Name)"
}

# CLI de graphify (fuera del venv del proyecto, para no tocar requirements.txt)
Write-Host "`nInstalando graphify (pip install --user graphifyy)..."
py -m pip install --user --upgrade graphifyy
if ($LASTEXITCODE -ne 0) { python -m pip install --user --upgrade graphifyy }

$scripts = & py -c "import sysconfig; print(sysconfig.get_path('scripts', 'nt_user'))"
if ($env:Path -notlike "*$scripts*") {
    Write-Host "`nAVISO: agrega esta carpeta al PATH para usar el comando 'graphify':"
    Write-Host "  $scripts"
}

Write-Host "`nListo. Abri Claude Code en esta carpeta y proba:  graphify query ""Fase 5"""
