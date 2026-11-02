#Requires -Version 7
# Registra a task \Claude\KindleImport (diária, 04:00). Rodar uma vez, pelo autor:
#   pwsh -NoProfile -File E:\scholion\.claude\skills\import-kindle-highlights\scripts\register-task.ps1
# Verificar:  schtasks /Query /TN "Claude\KindleImport" /FO LIST
# Rodar já:   schtasks /Run /TN "Claude\KindleImport"
$script = Join-Path $PSScriptRoot 'auto-import.ps1'
$action   = New-ScheduledTaskAction -Execute 'pwsh' -Argument "-NoProfile -WindowStyle Hidden -File `"$script`""
$trigger  = New-ScheduledTaskTrigger -Daily -At 04:00
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 30) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskPath '\Claude\' -TaskName 'KindleImport' -Action $action -Trigger $trigger -Settings $settings `
  -Description 'Importa destaques novos do Kindle como notas quote no Scholion (livros de books.json)' -Force | Out-Null
schtasks /Query /TN 'Claude\KindleImport' /FO LIST | Select-String 'TaskName|Next Run Time|Status'
