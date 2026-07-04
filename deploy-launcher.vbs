' Launcher oculto para a tarefa \Claude\ScholionPublish.
' Roda o pwsh com janela invisivel (0) e espera terminar (True),
' evitando o flash de console quando a sessao esta logada.
Set sh = CreateObject("WScript.Shell")
cmd = "pwsh.exe -NoProfile -Command ""& 'E:\scholion\deploy-scheduled.ps1' *>> 'E:\scholion\deploy-scheduled.log'"""
sh.Run cmd, 0, True
