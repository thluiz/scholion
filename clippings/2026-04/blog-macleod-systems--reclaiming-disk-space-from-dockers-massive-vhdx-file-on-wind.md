---
url: "https://blog.macleod.systems/reclaiming-disk-space-from-dockers-massive-vhdx-file-on-windows/"
captured_at: "2026-04-22T17:26:08+01:00"
title: "Reclaiming Disk Space from Docker's Massive VHDX File on Windows"
domain: "blog-macleod-systems"
---

What is WSL 2 and Why Docker Loves It

WSL 2 (Windows Subsystem for Linux 2) is Microsoft's lightweight virtual machine tech that runs a real Linux kernel directly on Wi

---
Notice your PC's free space vanishing? You run [TreeSize](https://www.jam-software.com/treesize?ref=blog.macleod.systems) (or a similar tool) and spot the culprit: a ballooning VHDX file under Docker's folder, sometimes hitting 100GB+. Docker Desktop on Windows uses WSL 2, and this dynamic virtual hard disk (VHDX) stores images, containers, and volumes—eating the free space on your C: drive.

## What is WSL 2 and Why Docker Loves It

WSL 2 (Windows Subsystem for Linux 2) is Microsoft's lightweight virtual machine tech that runs a real Linux kernel directly on Windows—no heavy VM overhead. Docker Desktop switched to it by default for better performance: full Linux syscalls, faster file I/O, and seamless container isolation on your C: drive. The trade-off? That VHDX file holds the entire Linux distro state, bloating fast without maintenance.

## Why the VHDX File Grows Uncontrollably

Docker's ext4.vhdx (typically at %LOCALAPPDATA%\\Docker\\wsl\\disk\\docker\_data.vhdx) acts as the Linux filesystem for WSL 2. It's "dynamically expanding," growing as you pull images, run containers, or build caches—but it doesn't automatically shrink when you delete them. Unused layers linger until you prune and compact, leaving gigabytes trapped.

## Step 1: Prune Docker Junk with Commands

**Ensure Docker Desktop is running** (check system tray). Open PowerShell as admin and run these to remove unused resources:

```command
docker system prune -a --volumes
```

This removes dangling images, stopped containers, unused networks, and volumes. Follow with specifics if needed:

```command
docker image prune -a docker container prune docker volume prune
```

Check `docker system df`—you'll reclaim some space immediately.

## Step 2: Optimize the VHDX to Shrink It

Pruning alone won't shrink the VHDX; compact it manually. **Before optimizing**, ensure you're on WSL 2.5+ for better VHDX handling:

`wsl --update`

Verify: `wsl --version` (expect 2.5.10+). Restart Docker. Newer WSL improves disk compacting.

Let's optimize! In admin PowerShell:

1.  Shut down WSL: `wsl --shutdown`
2.  Find the file: Usually `%LOCALAPPDATA%\Docker\wsl\disk\docker_data.vhdx` (use TreeSize to confirm).
3.  Compact: `Optimize-VHD -Path "$env:LOCALAPPDATA\Docker\wsl\disk\docker_data.vhdx" -Mode Full`

It scans and reclaims unused blocks. Verify with TreeSize afterward.

**Pro Tip:** Set a WSL disk limit in `%USERPROFILE%\.wslconfig` (create if missing):

```config
[wsl2] memory=8GB # Caps WSL VM RAM at 8GB (default: 50% system RAM). swap=0 # Disables swap file to avoid extra VHDX growth. diskSize=100GB # ⚠️ Max VHDX size (default: 1TB)—choose wisely!
```

## What Happens When You Hit 100GB

WSL treats this as a **hard limit**. Docker builds fail with "no space left on device"—even with Windows free space. Fix by:

1.  Pruning Docker (`docker system prune -a --volumes`)
2.  Optimizing VHDX (`Optimize-VHD ... -Mode Full`)

**Start conservative (50-100GB) but monitor with `docker system df`.**Restart WSL/Docker Desktop to apply.

Schedule monthly maintenance to prevent bloat, and here is a script - remember to edit the file location of your VHDX file!

```ps1
#Requires -RunAsAdministrator param() $VHDX_PATH = "$env:LOCALAPPDATA\Docker\wsl\disk\docker_data.vhdx" Write-Host "Docker Cleanup Script Starting..." -ForegroundColor Green Write-Host "VHDX Target: $VHDX_PATH" -ForegroundColor Cyan # Check Docker is running try { docker info --format '{{.ServerVersion}}' | Out-Null Write-Host "Docker daemon running" -ForegroundColor Green } catch { Write-Host "Docker Desktop not running! Start it first." -ForegroundColor Red exit 1 } # Show space BEFORE Write-Host "`nSpace BEFORE prune:" -ForegroundColor Yellow docker system df # PRUNE (interactive) $confirm = Read-Host "Prune ALL unused images/volumes/containers? (y/N)" if ($confirm -match '^[Yy]$') { Write-Host "Pruning everything..." -ForegroundColor Red docker system prune -a --volumes -f Write-Host "Prune complete!" -ForegroundColor Green } else { Write-Host "Skipping prune" -ForegroundColor Yellow } # Shutdown WSL Write-Host "`nShutting down WSL..." -ForegroundColor Yellow wsl --shutdown Start-Sleep -Seconds 3 # Find VHDX if (-not (Test-Path $VHDX_PATH)) { $altPath = "$env:LOCALAPPDATA\Docker\wsl\data\docker_data.vhdx" if (Test-Path $altPath) { $VHDX_PATH = $altPath Write-Host "Found VHDX at: $VHDX_PATH" -ForegroundColor Cyan } else { Write-Host "VHDX not found! Check:" -ForegroundColor Red Write-Host " $env:LOCALAPPDATA\Docker\wsl\data\" -ForegroundColor Gray exit 1 } } # OPTIMIZE VHDX Write-Host "`nOptimizing VHDX..." -ForegroundColor Yellow try { $sizeBefore = (Get-Item $VHDX_PATH).Length / 1GB Write-Host "Size before: $([math]::Round($sizeBefore,1))GB" Optimize-VHD -Path $VHDX_PATH -Mode Full Write-Host "VHDX optimized! Check TreeSize." -ForegroundColor Green } catch { Write-Host "Optimize-VHD failed: $_" -ForegroundColor Red } Write-Host "`nDone! Restart Docker Desktop." -ForegroundColor Green
```
