---
title: "[Guide] Mac OS X 10.7 Lion on VirtualBox with Windows 7 and Intel PC"
date: '2012-02-16T14:24:57-03:00'
category: webclip
summary: 'The guide shows how to install and run Mac OS X 10.7 Lion in VirtualBox on a Windows 7 Intel PC, using a prebuilt bootable Lion disk and the HackBoot ISO, with several setup caveats.'
tags: ["virtualbox", "mac-os-x-lion", "windows-7", "intel-pc"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[Guide] Mac OS X 10.7 Lion on VirtualBox with Windows 7 and Intel PC"
    url: "http://www.sysprobs.com/guide-mac-os-x-10-7-lion-on-virtualbox-with-windows-7-and-intel-pc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-02/sysprobs-com--mac-os-x-10-7-lion-on-virtualbox-windows-7-intel-pc.md"
    kind: repo
---

The page explains a working method to install and run Mac OS X 10.7 Lion on Oracle VirtualBox with a normal Intel computer and a Windows 7 host. It says the process depends on a precreated bootable Lion disk, the HackBoot ISO, and VirtualBox settings such as 64-bit Mac OS X, IO APIC, VT-x or AMD-V, and enough memory and disk space.

It also notes that the method is for testing and learning only, not for production or long-term use. The installation may need a manually created partition in Disk Utility, a manual restart after installation, and reloading HackBoot to boot again. The page warns that shutdown and restart do not work automatically, and that “About the Mac” may crash the virtual machine.

## Reading notes

- A working method is described for Mac OS X 10.7 Lion on VirtualBox with a Windows 7 host and an Intel computer.
- The key requirement is a precreated bootable Lion installation disk, not the ordinary DMG file from Apple or torrents.
- The bootable Lion disk can be made as a VMDK or VDI file, or as an ISO file.
- The process requires a working Snow Leopard system to create the modified Lion installer disk.
- Oracle VirtualBox 4.1 or later is needed, along with the extension pack.
- The virtual machine should be set as Mac OS X with a 64-bit version.
- Memory should be at least 1 GB, with 2 GB recommended.
- A virtual hard disk of at least 20 GB should be created.
- In system settings, floppy can be deselected, IO APIC should be enabled, and EFI should be disabled.
- Acceleration should have VT-x or AMD-V and nested paging enabled.
- Processor settings may need to be reduced to one processor if the machine crashes during installation.
- HackBoot.iso must be attached to the CD drive to boot the installer.
- If installing from a VMDK, the bootable disk is selected after starting the VM.
- If installing from an ISO, the Lion bootable ISO is loaded from the VirtualBox CD icon during boot.
- If the virtual hard disk is not visible, Disk Utility should be used to create a partition during installation.
- After installation, the automatic restart does not work and the VM must be reset or closed manually.
- The HackBoot ISO may need to be loaded again after the restart.
- The page says Lion can reach a working desktop in VirtualBox, though with some drawbacks and issues.
- Shutdown and restart do not happen automatically.
- “About the Mac” may crash the virtual machine.
