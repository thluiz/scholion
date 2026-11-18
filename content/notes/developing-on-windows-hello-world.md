---
title: "Developing on Windows – Hello World"
date: '2019-11-19T10:23:23+00:00'
category: webclip
summary: 'The post surveys Windows developer updates, focusing on Windows Terminal, WSL2, VS Code integration, and new PowerToys utilities that aim to improve multitasking, Linux workflows, and productivity.'
tags: ["windows-terminal", "wsl2", "vs-code", "powertoys"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Developing on Windows – Hello World"
    url: "https://blogs.windows.com/windowsdeveloper/2019/11/18/developing-on-windows-hello-world/#SMUf7O9Fhj6o28mX.97"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blogs-windows-com--developing-on-windows-hello-world.md"
    kind: repo
---

The post introduces a Windows developer series and highlights tools meant to improve the end-to-end development experience. It focuses on Windows Terminal, WSL, WSL 2, VS Code, and PowerToys, with emphasis on multitasking, Linux commands on Windows, and developer productivity.

## Reading notes

- The series will cover Windows Terminal, Windows Subsystem for Linux, Windows Performance, VS Code and Visual Studio, VMs and containers, and Developer PowerToys.
- Windows Terminal supports changing window opacity with Ctrl+Shift+scroll, which helps when working on several tasks at once.
- Windows Terminal v0.6 automatically detects installed WSL distributions and adds them to profiles.json.
- WSL lets users run Linux commands on Windows, and the writer names Ubuntu as a favorite distro.
- WSL 2 offers full system call compatibility and significantly faster file system performance.
- From a WSL 2 prompt, typing code. opens the project in VS Code with the WSL remote extension.
- With WSL 2 and VS Code, the Windows side handles the UI while the debugger, interpreter, and extensions run in WSL.
- The post says files can be opened, edited, breakpointed, and debugged in that setup.
- Windows Terminal Preview v0.6 includes an updated tab UI and a new font.
- PowerToys preview includes FancyZones, Windows Shortcut Guide, and PowerRename, with the project code on GitHub.
