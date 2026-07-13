#Requires -Version 7
# Wrapper agendado: chama deploy.ps1 (que ja faz git pull best-effort antes de publicar).
# Chamado por \Claude\ScholionPublish (6:15 e 20:15). Saida anexada em deploy-scheduled.log.
$ErrorActionPreference = "Continue"
Set-Location "E:\scholion"

Write-Host ""
Write-Host "===== $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ScholionPublish ====="

# Deploy: este sim reporta erro/exit code. O git pull acontece dentro do deploy.ps1.
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
