---
title: "Reclaiming Disk Space from Docker's Massive VHDX File on Windows"
date: '2026-04-22T17:26:08+01:00'
category: webclip
summary: 'The post explains why Docker Desktop on Windows can leave a large WSL 2 VHDX file that keeps growing, and shows how to prune Docker data, compact the disk, and set limits.'
tags: ["docker", "wsl2", "windows-storage", "vhdx"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Reclaiming Disk Space from Docker's Massive VHDX File on Windows"
    url: "https://blog.macleod.systems/reclaiming-disk-space-from-dockers-massive-vhdx-file-on-windows/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-04/blog-macleod-systems--reclaiming-disk-space-from-dockers-massive-vhdx-file-on-wind.md"
    kind: repo
---

The post says Docker Desktop on Windows uses WSL 2, and that this creates a dynamic VHDX file that stores images, containers, and volumes. Because the file expands as Docker use grows but does not shrink on its own, free space on the C: drive can disappear even after items are deleted.

## Reading notes

- WSL 2 is described as Microsoft’s lightweight virtual machine tech that runs a real Linux kernel on Windows.
- Docker Desktop uses WSL 2 by default for better performance, including Linux syscalls, faster file I/O, and container isolation.
- The Docker ext4.vhdx file, usually under %LOCALAPPDATA%\Docker\wsl\disk\docker_data.vhdx, acts as the Linux filesystem for WSL 2.
- The VHDX grows when images, containers, and caches are added, but it does not automatically shrink after they are removed.
- The post recommends running Docker Desktop, opening PowerShell as admin, and using docker system prune -a --volumes to remove unused images, stopped containers, networks, and volumes.
- It says pruning can reclaim space immediately, and docker system df can be used to check usage.
- It also says pruning alone does not shrink the VHDX, so the disk must be compacted manually with Optimize-VHD -Path "$env:LOCALAPPDATA\Docker\wsl\disk\docker_data.vhdx" -Mode Full after wsl --shutdown.
- Before optimizing, the post recommends updating to WSL 2.5+ with wsl --update and checking wsl --version.
- It suggests setting a WSL disk limit in %USERPROFILE%\.wslconfig, including memory, swap, and diskSize settings.
- When the VHDX reaches 100GB, Docker builds can fail with no space left on device, and the post says to fix that by pruning Docker and optimizing the VHDX.
- The post ends with a PowerShell script that checks Docker, shows disk usage before pruning, optionally prunes unused resources, shuts down WSL, finds the VHDX path, and runs Optimize-VHD.
