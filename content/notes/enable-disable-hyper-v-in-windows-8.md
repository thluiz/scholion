---
title: "Hyper-V - Enable and Disable in Windows 8"
date: '2014-06-24T10:36:44-03:00'
category: webclip
summary: 'Explains how to turn Hyper-V on or off in Windows 8 Pro or Enterprise through Windows Features, PowerShell, or DISM, and lists the admin, 64-bit, SLAT, and RAM requirements.'
tags: ["hyper-v", "windows-8", "powershell", "dism"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hyper-V - Enable and Disable in Windows 8"
    url: "http://www.eightforums.com/tutorials/42041-hyper-v-enable-disable-windows-8-a.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/eightforums-com--enable-disable-hyper-v-in-windows-8.md"
    kind: repo
---

The page explains how to enable or disable the built-in Hyper-V feature in Windows 8 Pro or Windows 8 Enterprise. It says the user must be signed in as an administrator, and that Hyper-V client support requires a 64-bit version of those editions, a 64-bit CPU with SLAT, and at least 4 GB of RAM.

## Reading notes

- Hyper-V can be turned on or off in Windows Features by expanding the Hyper-V section, checking or unchecking the options, then restarting the computer.
- In elevated PowerShell, `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V –All` enables Hyper-V, while `Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All` disables it.
- The `-All` switch is needed to install the Hyper-V GUI Management Tools and the Hyper-V Module for Windows PowerShell.
- In an elevated Command Prompt, `dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All` enables Hyper-V, and `dism.exe /Online /Disable-Feature:Microsoft-Hyper-V-All` disables it.
- After the PowerShell or DISM commands, the page says to type `Y` when prompted to restart the computer.
