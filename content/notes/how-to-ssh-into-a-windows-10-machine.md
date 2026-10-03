---
title: "How to SSH into a Windows 10 Machine from Linux OR Windows OR anywhere"
date: '2020-03-12T18:55:41-03:00'
category: webclip
summary: 'The post shows how to add the OpenSSH Server feature to Windows 10, start sshd as a service, change the default shell to PowerShell, and then connect from Linux, Windows, or even an iPad.'
tags: ["openssh", "windows-10", "powershell", "ssh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to SSH into a Windows 10 Machine from Linux OR Windows OR anywhere - Scott Hanselman"
    url: "https://www.hanselman.com/blog/HowToSSHIntoAWindows10MachineFromLinuxORWindowsORAnywhere.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-03/hanselman-com--how-to-ssh-into-a-windows-10-machine.md"
    kind: repo
---

The post explains that Windows 10 can act as an SSH server once the OpenSSH Server capability is installed. After that, sshd can be started as a Windows service and set to start automatically, which lets other machines connect to the Windows host over port 22.

It also shows that the default SSH session on Windows opens cmd.exe, and recommends changing the default shell by setting a registry key. In the example, the author points that key at PowerShell 7 so SSH sessions open directly in pwsh. The post closes by noting that this setup also works with scp, WinSCP, and PowerShell remoting over SSH.

## Reading notes

- Windows 10 already ships with the OpenSSH client, and the server component can be added through PowerShell or Windows Features.
- The server is started with sshd as a Windows service, and it can be configured to start automatically.
- SSH connections to the Windows machine use port 22, so firewall rules and authentication choices matter.
- A first SSH login into Windows opens the default cmd.exe shell.
- The default shell can be changed through the HKLM:\SOFTWARE\OpenSSH registry key.
- In the example, the default shell is set to C:\Program Files\PowerShell\7\pwsh.exe.
- After that change, SSH sessions open PowerShell 7 instead of cmd.exe.
- The setup also supports file transfer with scp and WinSCP.
- The post mentions WinRM and PowerShell Remoting over SSH as other options for remote access.
