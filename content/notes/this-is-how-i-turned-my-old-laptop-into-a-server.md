---
title: "This is how I turned my old laptop into a server"
date: '2020-07-05T14:11:16+00:00'
category: webclip
summary: 'The post explains how to turn an old laptop into a personal home server with Ubuntu Server, including USB installation, SSH access, Wi‑Fi setup, and optional Webmin.'
tags: ["ubuntu-server", "home-server", "ssh", "webmin"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "This is how I turned my old laptop into a server."
    url: "https://dev.to/jayesh_w/this-is-how-i-turned-my-old-laptop-into-a-server-1elf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--this-is-how-i-turned-my-old-laptop-into-a-server.md"
    kind: repo
---

The post walks through turning an old laptop into a personal home server with Ubuntu Server. It assumes the whole disk will be used, recommends a Debian-based system for beginners, and uses OpenSSH so the machine can be managed inside a private network.

## Reading notes

- The author uses an old laptop with 4 GB RAM, an Intel Core 2 Duo processor, and a 512 GB HDD.
- The post recommends Linux for servers and says Debian-based systems are best for beginners.
- Ubuntu Server 20.04 is chosen because CentOS is described as trickier for beginners and the machine has low-end hardware.
- The installation uses a live bootable USB, with the entire HDD erased for the server.
- The setup includes language selection, keyboard configuration, network detection through DHCP, proxy setup if needed, and guided storage using the whole disk.
- The installer creates separate partitions for the operating system and the GRUB bootloader.
- During profile setup, the user enters a name, server name, username, and password.
- OpenSSH Server is selected so the machine can be reached inside a private network.
- After installation, the root password is changed with sudo and passwd.
- To use Wi‑Fi, the post installs rfkill, wireless-tools, net-tools, and wpasupplicant, then checks the private IP address with ifconfig.
- From another computer, the server can be accessed with Putty on Windows or ssh username@ip_addr on Linux and macOS.
- Webmin is described as a web-based interface for managing user accounts, Apache, file sharing, and system configuration.
- The server can be used for backups, LAMP sites, SMTP, database backups, testing apps, a private git repository, media streaming, machine learning data storage, FTP, nginx, and OwnCloud.
