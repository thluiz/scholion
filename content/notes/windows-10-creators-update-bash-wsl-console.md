---
title: "Windows 10 Creator’s Update: What’s new in Bash/WSL & Windows Console"
date: '2017-04-12T09:19:32-03:00'
category: webclip
summary: 'The post lists the main Bash/WSL and Windows Console improvements in Windows 10 Creators Update, including broader Linux compatibility, Ubuntu 16.04 support, interop, socket and filesystem notifications, and richer console rendering.'
tags: ["wsl", "windows-console", "creators-update", "linux-compatibility"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Windows 10 Creator’s Update: What’s new in Bash/WSL & Windows Console"
    url: "http://blogs.msdn.microsoft.com/commandline/?p=875"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-04/blogs-msdn-microsoft-com--windows-10-creators-update-bash-wsl-console.md"
    kind: repo
---

The post says the Windows 10 Creators Update brings a much improved Bash/WSL and Windows Console experience, built from user feedback and focused on developer tools. It groups the changes into broader Linux compatibility, Ubuntu 16.04 support, networking fixes, file change notifications, Windows-Linux interop, socket improvements, and Console rendering upgrades.

## Reading notes

- The release includes hundreds of WSL fixes and improvements collected during the Creators Update cycle.
- More Linux system call compatibility lets mainstream developer tools work as expected, including shells, editors, languages, servers, and other utilities.
- New Bash installs on Creators Update use Ubuntu 16.04, while existing Ubuntu 14.04 instances are not upgraded automatically.
- Users can remove and replace an old distro instance, or upgrade it in place with Ubuntu’s upgrade procedure.
- ifconfig network enumeration now works, which helps tools such as ifconfig, gulp, and npm.
- Non-administrators can ping network endpoints in Creators Update.
- WSL now supports inotify, so tools can react to file changes and trigger reloads or rebuilds.
- File change notifications also work for files on the Windows filesystem.
- Bash can launch Windows apps and tools, and Windows can launch Linux binaries, commands, and scripts.
- UNIX datagram sockets, Netlink sockets, additional TCP socket options, and improved IPv6 support were added.
- Linux processes show up in Windows process enumeration, and there are changes to help anti-malware and firewall tools understand Linux processes.
- Shared memory support was added for PostgreSQL and other tools.
- The Windows Console gained more VT sequence support, 24-bit color, mouse support, and the ability to create symlinks without admin rights when developer mode is enabled.
- WSL is still described as a beta feature in Creators Update, and the post asks users to keep sending feedback.
