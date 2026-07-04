#Requires -Version 7
# Wrapper agendado: git pull best-effort (nunca bloqueia) + deploy.ps1.
# Chamado por \Claude\ScholionPublish (6:15 e 20:15). Saida anexada em deploy-scheduled.log.
$ErrorActionPreference = "Continue"
Set-Location "E:\scholion"

Write-Host ""
Write-Host "===== $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ScholionPublish ====="

# git pull best-effort: falha aqui apenas avisa, jamais impede a publicacao.
$env:GIT_TERMINAL_PROMPT = "0"   # sem credencial -> falha rapido, nao pendura a tarefa
try {
    Write-Host "==> git pull --ff-only"
    git pull --ff-only 2>&1 | ForEach-Object { Write-Host $_ }
    if ($LASTEXITCODE -ne 0) {
        Write-Host "AVISO: git pull falhou (exit $LASTEXITCODE) - seguindo com o estado local" -ForegroundColor Yellow
    }
} catch {
    Write-Host "AVISO: git pull lancou excecao - $($_.Exception.Message) - seguindo com o estado local" -ForegroundColor Yellow
}

# Deploy: este sim reporta erro/exit code.
try {
    & "E:\scholion\deploy.ps1"
    $code = $LASTEXITCODE
    if ($null -eq $code) { $code = 0 }
} catch {
    Write-Host "ERRO: deploy.ps1 falhou - $($_.Exception.Message)" -ForegroundColor Red
    $code = 1
}
Write-Host "==> deploy.ps1 terminou (exit $code)"
exit $code
