#Requires -Version 7
# Wrapper agendado: chama deploy.ps1 (que ja faz git pull best-effort antes de publicar).
# Chamado por \Claude\ScholionPublish (a cada 30 min). Saida anexada em deploy-scheduled.log.
# A primeira execucao a partir das 03:00 de cada dia roda com -ForceFullSync
# (hash de todo o public/, upload so do que diferir). Se a maquina estiver
# desligada as 03:00, a primeira execucao depois disso faz o fullsync do dia.
$ErrorActionPreference = "Continue"
Set-Location "E:\scholion"

$FULL_SYNC_HOUR = 3
$FULL_SYNC_MARK = "E:\scholion\last-full-sync.txt"

Write-Host ""
Write-Host "===== $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ScholionPublish ====="

$now      = Get-Date
$today    = $now.ToString('yyyy-MM-dd')
$lastFull = if (Test-Path $FULL_SYNC_MARK) { (Get-Content $FULL_SYNC_MARK -Raw).Trim() } else { $null }
$fullSync = ($now.Hour -ge $FULL_SYNC_HOUR) -and ($lastFull -ne $today)
if ($fullSync) { Write-Host "==> fullsync diario (ultimo: $(if ($lastFull) { $lastFull } else { 'nunca' }))" }

# Deploy: este sim reporta erro/exit code. O git pull acontece dentro do deploy.ps1.
try {
    if ($fullSync) { & "E:\scholion\deploy.ps1" -ForceFullSync } else { & "E:\scholion\deploy.ps1" }
    $code = $LASTEXITCODE
    if ($null -eq $code) { $code = 0 }
} catch {
    Write-Host "ERRO: deploy.ps1 falhou - $($_.Exception.Message)" -ForegroundColor Red
    $code = 1
}

# So marca o dia quando o fullsync terminou bem; se falhar, a proxima execucao tenta de novo.
if ($fullSync -and $code -eq 0) { Set-Content -Path $FULL_SYNC_MARK -Value $today -NoNewline }

Write-Host "==> deploy.ps1 terminou (exit $code)"
exit $code
