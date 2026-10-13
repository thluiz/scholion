---
title: "Installing Linux in Hyper-V"
date: '2014-03-22T21:26:47-03:00'
category: webclip
summary: 'The post explains a simple way to install a Linux desktop VM in Hyper-V, with Fedora 19 as the example, and recommends a legacy network adapter before the first boot so networking works after installation.'
tags: ["linux", "hyper-v", "installation", "networking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Installing Linux in Hyper-V - Microsoft Visual Studio UK Team - Site Home - MSDN Blogs"
    url: "http://blogs.msdn.com/b/visualstudiouk/archive/2013/11/20/installing-linux-in-hyper-v.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/blogs-msdn-com--installing-linux-in-hyper-v.md"
    kind: repo
---

The post describes a straightforward Hyper-V setup for a Linux desktop virtual machine. The example uses Fedora 19, 2048 MB of dynamic RAM, a 20 GB virtual hard disk, and a bootable Linux ISO. It also notes that this setup was done to test TFS 2013 web test capabilities in a non-Windows environment.

## Reading notes

- Use a Linux distro ISO as the VM’s bootable DVD.
- Allocate 2048 MB of RAM and keep it dynamic.
- Leave networking disconnected during initial VM creation.
- Set the virtual disk size to 20 GB for a standard install with Eclipse.
- Before starting the VM, add a Legacy Network Adapter in Hyper-V Manager.
- Choose a virtual switch that provides the needed connectivity.
- Remove the non-legacy Network Adapter after adding the legacy one.
- After installation, eject the DVD and restart the VM.
- The result should be a clean Linux install with networking enabled and working.
