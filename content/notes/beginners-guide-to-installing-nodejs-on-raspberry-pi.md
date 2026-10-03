---
title: "Beginner’s Guide to Installing Node.js on a Raspberry Pi"
date: '2016-03-05T18:06:42-03:00'
category: webclip
summary: 'The tutorial shows how to prepare a Raspberry Pi 2 or 3, install Raspbian, configure Wi-Fi and remote access, and then add Node.js from NodeSource so the system can run and be updated normally.'
tags: ["nodejs", "raspberry-pi", "raspbian", "windows-remote-access"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Guide to Installing Node.js on a Raspberry Pi 2 | thisDaveJ"
    url: "http://thisdavej.com/beginners-guide-to-installing-node-js-on-a-raspberry-pi/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/thisdavej-com--beginners-guide-to-installing-nodejs-on-raspberry-pi.md"
    kind: repo
---

The page walks through setting up a Raspberry Pi 2 or 3 with Raspbian, starting from writing the image to a microSD card and booting the hardware. It then covers basic configuration, Wi-Fi setup, updates, remote desktop access from Windows, and an optional Samba file share before installing Node.js from the NodeSource repository.

## Reading notes

- The guide targets Raspberry Pi 2 and Raspberry Pi 3, and notes that the Pi 3 does not need a separate USB Wi-Fi adapter.
- It lists the hardware needed, including a microSD card, power supply, HDMI monitor, keyboard, mouse, and Wi-Fi adapter for the Pi 2.
- Raspbian is written to the microSD card with Win32 Disk Imager after unzipping the downloaded image.
- In raspi-config, the tutorial expands the filesystem, suggests changing the default password, and adjusts locale, timezone, and keyboard layout.
- The hostname can be shortened, and SSH can be enabled for remote terminal access.
- Wi-Fi is configured from the desktop network icon, and the connection is tested with ping.
- The system is updated with sudo apt-get update and sudo apt-get dist-upgrade.
- xrdp is installed for Windows remote desktop access, and samba is installed so the Raspberry Pi can be reached by hostname from Windows.
- An optional Samba share is created at /home/pi/share by editing smb.conf and creating an SMB user with smbpasswd.
- Node.js is installed by adding the NodeSource repository with a curl command and then running sudo apt-get install -y nodejs.
- The tutorial checks the installation with node -v and a short REPL test.
