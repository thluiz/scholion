---
url: "https://devblogs.microsoft.com/commandline/the-windows-subsystem-for-linux-build-2020-summary"
captured_at: "2026-11-16T03:59:23+00:00"
title: "The Windows Subsystem for Linux BUILD 2020 Summary"
domain: "devblogs-microsoft-com"
---

May 19th, 2020

0 reactions

![](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2019/03/0-150x150.jpg)

Principal Product Manager

This year at an all virtual BUILD conference we had many exciting announcements for the Windows Subsystem for Linux (WSL)! This blog post gives you a summary of all the WSL news, including what’s available now and what you can expect in the future.

## WSL’s BUILD news at a glance

*   Available this month
    *   [Support for WSL 2 distros is coming this month in the Windows 10 May 2020 Update](#wsl2-availibility)
    *   [Docker Desktop released a new version using WSL 2 as their backend](#docker-desktop)
*   Current roadmap: What’s coming to WSL
    *   [You’ll soon be able to install WSL with a single command. Just open a Windows Terminal and enter `wsl.exe --install`](#wsl-install)
    *   [WSL 2 will be the new default when installing for the first time](#wsl2-default)
    *   [WSL will support GPU Compute workflows](#wsl-gpu)
    *   [Adding Linux GUI app support to WSL is on our roadmap](#wsl-gui)

Please read on below for the details for each item.

## Available this month

### Support for Windows Subsystem for Linux 2 (WSL 2) distros is coming this month in the Windows 10 May 2020 Update

4 years ago, at Build 2016, Microsoft surprised the world by announcing Windows Subsystem for Linux – WSL (also known at the time as “Bash on Ubuntu on Windows”). WSL enables Windows users to run native, unmodified Linux command-line tools and apps directly in Windows, alongside all their favorite Windows apps and tools. WSL usage has grown enormously from initially just a few thousand people downloading the first preview build to more than 3.5 million monthly active devices today!

However, we wanted WSL to do more – to run all Linux apps and tools, and to run apps and tools faster. At Build 2019, the WSL team unveiled the first preview of WSL 2, which utilizes new capabilities in Windows’ Hypervisor Platform to run distros and tools in containers, [atop a real Linux kernel image that is built and delivered by Microsoft](https://devblogs.microsoft.com/commandline/shipping-a-linux-kernel-with-windows/), hosted in a lightweight VM, which boots from cold in less than 2s! This means that WSL 2 delivers full system call compatibility with a real Linux kernel and is 3-6x faster compared to earlier versions of WSL. You can easily set the version of any WSL distro to be using WSL 2 with the command: `wsl.exe --set-version <distroName> 2`.

The response from the community has been huge and, frankly, positively overwhelming – sincerest thanks to everyone who ran WSL 2, filed issues, and asked for features, you’ve helped us make WSL2 even better than we hoped it could be!

### Docker Desktop released a new version using WSL 2 as their backend

WSL 2’s new capabilities have not gone unnoticed by our partners either!

Shortly after WSL 2 was announced, Docker Inc. [decided to host Docker Desktop for Windows atop WSL 2](https://www.docker.com/blog/docker-hearts-wsl-2/)! Following a successful preview period, Docker has announced that Docker Desktop for Windows will now default to run atop WSL 2 when installed on the Windows 10 May 2020 update, which will bring [Docker Desktop to Windows Home users as well](https://www.docker.com/blog/docker-desktop-for-windows-home-is-here/).

This change to host Docker on WSL 2 will result in containers booting up faster, while consuming fewer resources on the host machine due to WSL 2’s more lightweight footprint vs. full VMs.

You can learn more about the [Docker Desktop WSL 2 backend here](https://docs.docker.com/docker-for-windows/wsl-tech-preview/).

## Current roadmap: What’s coming to WSL

### You’ll soon be able to install WSL with a single command. Just open a Windows Terminal and enter \`wsl.exe –install\`

One common complaint about WSL is that it’s not easy to find and enable. We agree, which is why we’re working on some improvements to the wsl.exe command-line tool to help you install WSL. Soon you will be able to simply install WSL by entering: `wsl.exe --install` in your command-line!

[![Image WSLInstall](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2020/05/WSLInstall.png)](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2020/05/WSLInstall.png)

This command will be added to every Windows machine so that all you need to do is open a Terminal window elevated with administrator privileges and run `wsl.exe --install`. From there the WSL optional components will be enabled, and your specified distro will be downloaded and installed for you automatically upon restart.

You can expect to see initial releases of this feature in the next few months in the Windows Insiders Fast Ring.

### WSL 2 will be the new default when installing for the first time

We’re also introducing the change to make WSL 2 the new default distribution type when installing WSL for the first time. WSL 2 brings significant improvements and we found that the majority of our users on Insider branches are using WSL 2 distros. When developing `wsl.exe --install` it made sense for it to default to what people are using: WSL 2, and we’ve included this as well for any new installations of WSL when enabling the ‘Windows Subsystem for Linux’ optional component. You’ll see these changes in the Insiders Fast ring in the next few months alongside the `wsl.exe --install` improvement.

### WSL will support GPU Compute workflows

Adding [CUDA](https://github.com/microsoft/WSL/issues/327) and/or [GPU Compute support](https://github.com/microsoft/WSL/issues/829) to WSL has been our #1 most requested feature since our first release! Over the last 3+ years, the WSL, Virtualization, DirectX, Windows Driver teams, and our silicon partners have been working hard on a complex engineering feat to deliver this capability.

This is why we’re thrilled to announce that we will start previewing GPU compute support for WSL in Windows 10 Insider builds within the next few months!

Initially, the GPU compute capability will support two scenarios:

*   [NVIDIA CUDA](https://developer.nvidia.com/cuda/wsl)
    *   Supports existing Linux tools & workflows used by professionals
*   [DirectML](https://aka.ms/directml)
    *   Initially targeting beginners and students, leveraging DirectX 12 capable GPUs from several vendors
    *   The team will be releasing a preview package of TensorFlow with a DirectML backend enabling hardware agnostic acceleration of AI & ML workloads across the breadth of Windows hardware – DirectML will also support native Windows too, including TensorFlow on Windows!

Once this preview is released, you will simply need to ensure that you have the latest Windows Insider Fast build, WSL 2 installed, install the correct driver for your GPU from the hardware vendor, and then you’ll be ready to start developing, training and testing your machine learning and AI models inside of WSL!

WSL ML gif, image

This change will be released to the Windows Insiders Fast ring in the next few months. For all the details of what this change means and how it was made possible, please read [the DirectX Developer blog post](https://devblogs.microsoft.com/directx/directx-heart-linux/).

### Adding Linux GUI app support to WSL is on our roadmap

One of our other most prolific requests is to support not just command-line apps, but Linux GUI apps as well. For example, some users want to run their preferred Linux GUI text editor or IDE in a Linux environment and work on their code stored locally within their distro’s filesystem, or simply develop Linux GUI apps on their Windows machine.

Our goal is for you to be able to run Linux GUI apps on your desktop seamlessly alongside your Windows apps. This will enable you to use Linux apps to edit, build, and run your code, visualize data plots in Python, or even use applications that are optimized for a Linux environment.

At BUILD we demonstrated an early version of this work, running a few GUI sample apps directly from WSL such as `Eye of Gnome`, `gedit` and the `mpv` media player. These apps connected to a wayland server running inside of WSL, which communicated with a RDP client on the Windows host. You can see a screenshot of this in action below where we’re running the GNOME file manager in WSL and Outlook side by side.

[![Image WSLGUIApps](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2020/05/WSLGUIAppsNoName.png)](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2020/05/WSLGUIAppsNoName.png)

These changes are on the WSL’s team roadmap and you can expect to hear more about this work by holiday 2020.

## Stay Involved

To summarize, once you update to the Windows 10 May 2020 Update you’ll have full support for WSL 2 distros! If you join the Windows Insiders Fast Ring you’ll be ready to start receiving the latest WSL features including the new install experience and GPU compute within the next few months.

There’s lots of exciting news and features coming to WSL, so please stay tuned to this blog for the details of any big announcements. You can follow me on Twitter [@craigaloewen](https://twitter.com/craigaloewen) or [members of the WSL team](https://twitter.com/i/lists/1131397802204864512/members) that are on Twitter for any news there as well. Please check out [Kevin Gallo’s blog post](https://blogs.windows.com/windowsdeveloper/?p=55728) for all of the Windows developer focused news from BUILD. Thank you for supporting WSL!

## Author

![Craig Loewen](https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2019/03/0-150x150.jpg)

Principal Product Manager

Craig Loewen is a product manager working on Linux technologies on Windows.
