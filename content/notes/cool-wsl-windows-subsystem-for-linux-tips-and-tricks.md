---
title: "Cool WSL (Windows Subsystem for Linux) tips and tricks you (or I) didn't know were possible"
date: '2019-11-15T10:30:35+00:00'
category: webclip
summary: 'The post lists practical WSL and WSL2 tricks: opening Explorer from Linux, running Linux commands in Windows, using Windows apps from Linux, launching VS Code in WSL, and moving distros between machines.'
tags: ["wsl", "wsl2", "windows-terminal", "vs-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Cool WSL (Windows Subsystem for Linux) tips and tricks you (or I) didn't know were possible"
    url: "https://www.hanselman.com/blog/CoolWSLWindowsSubsystemForLinuxTipsAndTricksYouOrIDidntKnowWerePossible.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hanselman-com--cool-wsl-windows-subsystem-for-linux-tips-and-tricks.md"
    kind: repo
---

The post collects several ways WSL and Windows work together closely. It shows how to open Windows Explorer from a WSL shell, run Linux commands from Windows with wsl.exe, and run Windows executables from Linux by calling .exe files directly.

It also describes using Visual Studio Code with Remote - WSL, the benefits of WSL 2, running multiple Linux distributions side by side, using Pengwin with an X server, exporting and importing distros between machines, and using the Windows Git Credential Provider inside WSL.

## Reading notes

- Run explorer.exe . from WSL to browse the current Linux directory in Windows Explorer.
- Use wsl.exe from Windows to call real Linux commands such as ls and grep.
- Call Windows programs from WSL by using the .exe suffix, including Explorer and Notepad.
- Run code . in a WSL folder to use VS Code with the Remote - WSL extension.
- WSL 2 is described as a lightweight VM with better performance and a more connected experience than the original WSL.
- wsl --list --all can show multiple installed Linux distributions, and each can have its own Windows Terminal profile.
- Pengwin plus an X server such as X410 gives an integrated WSL desktop-style setup.
- wsl --export and wsl --import can move a distro between Windows machines.
- The Windows Git Credential Provider can be integrated into WSL by wrapping git-credential-manager.
