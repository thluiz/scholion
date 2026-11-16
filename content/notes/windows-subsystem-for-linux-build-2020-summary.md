---
title: "The Windows Subsystem for Linux BUILD 2020 Summary"
date: '2026-11-16T03:59:23+00:00'
category: webclip
summary: 'The post summarizes BUILD 2020 WSL announcements: WSL 2 support in the May 2020 Windows update, Docker Desktop on WSL 2, a one-command install, WSL 2 by default, GPU compute, and Linux GUI apps.'
tags: ["windows-subsystem-for-linux", "wsl-2", "docker-desktop", "windows-10"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Windows Subsystem for Linux BUILD 2020 Summary"
    url: "https://devblogs.microsoft.com/commandline/the-windows-subsystem-for-linux-build-2020-summary"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--windows-subsystem-for-linux-build-2020-summary.md"
    kind: repo
---

The post collects the BUILD 2020 announcements for Windows Subsystem for Linux. It says WSL 2 support is arriving in the Windows 10 May 2020 Update, Docker Desktop is moving to WSL 2 as its backend, and future updates will focus on easier installation, WSL 2 as the default, GPU compute, and Linux GUI apps.

## Reading notes

- WSL 2 support for distros is coming in the Windows 10 May 2020 Update.
- WSL 2 runs Linux tools in a lightweight VM with a real Linux kernel, with full system call compatibility and faster performance than earlier WSL versions.
- Docker Desktop for Windows will default to WSL 2 on the Windows 10 May 2020 update, which should reduce resource use and speed up container startup.
- A future `wsl.exe --install` command will let users install WSL from a Terminal window, enabling components and downloading the distro automatically after restart.
- New WSL installations will default to WSL 2.
- WSL GPU compute support is planned for Insider builds, with initial support for NVIDIA CUDA and DirectML.
- Linux GUI app support is on the roadmap, with early demos showing apps like Eye of Gnome, gedit, and mpv running through Wayland inside WSL.
