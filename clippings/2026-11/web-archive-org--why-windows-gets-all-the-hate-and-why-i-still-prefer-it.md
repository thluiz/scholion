---
url: "https://web.archive.org/web/20200628090303id_/https://dev.to/rashil2000/why-windows-gets-all-the-hate-and-why-i-still-prefer-to-use-it-dlg"
captured_at: "2026-11-16T07:49:36+00:00"
title: "Why Windows gets all the hate... And why I still prefer to use it"
domain: "web-archive-org"
---

Let's clear one thing first. I use Windows 10 as a daily driver. Go ahead, judge me all you want, but I'm just too lazy to give up my comfort of state of the art software and ease of use. I've used on Ubuntu and Kali Linux on and often too, to be fair.

Now, the article. I was partly inspired by Tom Scott's video **Why You Can't Name A File CON In Windows**. The Windows operating system gets a ton of hate from the developer community nowadays, and this is an attempt to understand why. Key complains have always included sluggish performance and inconsistent user interface. As a bullet point, this article primarily talks about software compatibility that is available _out of the box_.

### [](#tldr)TL;DR

Two words: backwards compatibility.

### [](#why-the-hate)Why the hate

Microsoft has been extremely adamant about making its OS backward compatible, with all sorts programs written for it, ever. The reason why we still see legacy applications and user interfaces is that somewhere in the world someone is still using them, while being on the latest version of the OS. As expected from this approach, the OS (or its newer versions) are never really _completely rewritten_, because, well, the old programs would stop working then. This inevitably leads to the base OS installation being overly clunky in terms of source code, as each new version builds on top of the legacy codebase, and never really replaces it. This is quite understandable from Microsoft's perspective, as most of it's business comes from enterprise solutions where each single user companies have thousands of machines to use, and keeping them up to date isn't feasible on this scale. For instance, my dad's offices still use the enterprise version of Windows 7, and they just don't see the need for upgrading. It goes on with the popular saying:

> If it ain't broke, don't fix it.

Windows 7 was much beloved, and it was supported for almost 11 years as a result of this usage. Now, don't get me wrong, but Linux and MacOS usually don't support applications for that long. By contrast, LTS versions of RHEL last around 9 years, and those of Ubuntu last 5 years. In Linux's case, it is very much understandable, it's source code is clean and free from clunk, and that is how it manages to be extremely lightweight and hence efficient for it's use case. It stays minimal and you can install/configure stuff based on your requirements. The other day I was having trouble running a `.deb` package meant for Ubuntu 18.04 on Ubuntu 20.04, and it failed to install. It wasn't a big deal, there were some missing dependencies and it was sorted out in a matter of 15 minutes. A friend of mine had similar problems with some Python installation. On the other hand, I was looking for a niche application to execute a script on Windows, and I stumbled upon an `.exe` on the internet that was written in, well, 1999. And it ran. Just ran and did it's job, nothing else. And for MacOS's case, I'll let Tom from the video do the talking, "Good luck running apps/OSes more than 3 years old on a Mac".

From a technical perspective, Windows separates concerns for compatibilty by having some built-in layers, and these are Virtual DOS machines (particularly the **OS/2 MVDM** and the **NTVDM**), **Windows on Windows** and **WoW64**.

> In software engineering, a compatibility layer is an interface that allows binaries for a legacy or foreign system to run on a host system. This translates system calls for the foreign system into native system calls for the host system.

Most of these are implemented using dynamically-linked libraries (`.dll` as popularly known). For those curious, they can be found in the `C:\WINDOWS` directory. In recent times, Microsoft has been putting more efforts into streamlining it's UI and making things uniform, but all of this presents an understandable burden.

### [](#why-i-use-it)Why I use it

I've always been a design guy and I really like the Fluent Design language, and the subsequent turns Microsoft is making in the UI. It is open-source and extremely well-documented. I have a somewhat beefy machine so OS lagging is a non-existant issue, and yes I agree I might be biased in this regard as a result. Usage of certain software like Photoshop, Premiere Pro, AutoCAD, FL Studio, Visual Studio, SketchUp, Office apps etc. has kept me from using Linux full time. Most of my coding work consists of writing JavaScript, and I make extra efforts to use open-source tools wherever possible. I have included a list in the end for interested folks. I also have a basic GitHub repository, [Fluent-Customization](https://github.com/rashil2000/Fluent-Customization), for setting up and customizing workflows.

The following is a (incomplete) list of nifty little things that are available by default, in no particular order, and can decide between making or breaking a normal day. In my experience, almost all of these things require at least a commandline install or manual configuration in Linux distros. For MacOS, I can't really say, as I haven't used it personally.

*   Installing and managing multiple fonts through GUI
*   Taking screenshots and screencaptures
*   Scheduling tasks using GUI
*   Manage windows and virtual desktops fluidly
*   Phone calls and text messages
*   Sharing content and web pages on PC instantly through the Your Phone app
*   Projecting wirelessly
*   Making 3D renders
*   Editing images and videos
*   Unified touch and keyboard-mouse UI
*   Taking Sticky notes on the go
*   Doodle on the screen while working at the same time
*   Slick Notification and Action Centre with Focus Assist keep annoying notifications away while working, but display them when required
*   Intuitive Settings and Control Panel interface
*   Thousands of apps and games on the Store
*   Daily rotating images on the lockscreen and browser homepage
*   Separate keyboard shortcuts to access quick settings like Multi-monitor setups, Night light, Magnifier, Invert Colours, Language Switch, Emoticons, American Sign Language (ASL) and VPN
*   Battery management profiles that can be used to customize usage and generate reports on the fly
*   Touchpad gestures for multitasking
*   PowerShell, an extremely advanced shell and scripting language and more than an alternative to good old CMD
*   Decent chatbot and text-to-speech/speak-to-type through Cortana
*   State-of-the-art Terminal with tons of customizable options and configurations
*   An easy-to-use package manager, winget, that automatically syncs with native Programs and Features
*   Sign In protection using fingerprint, iris scan and facial recognition
*   Sufficiently advanced antivirus and malware tracker, Defender Securtiy, eliminating the need for third-party applications and subscriptions
*   Support for building desktop apps and games using Visual Studio, integrates really well with Unreal Engine and Unity 3D
*   ...

Another compatibilty layer, called the Windows Subsystem for Linux (or WSL) that runs the Linux kernel natively without virtualization, has been in the works for the past few years. Latest updates to WSL have somewhat eliminated need for dual-boots (well, dual-boots for those who used Windows primarily, not the other way round).

#### [](#sources)Sources

*   [Why You Can't Name A File CON In Windows - Tom Scott](https://youtu.be/bC6tngl0PTI)
*   [Red Hat Enterprise Linux Life Cycle - RHEL](https://access.redhat.com/support/policy/updates/errata/)
*   [Ubuntu kernel lifecycle and enablement stack - Ubuntu](https://ubuntu.com/kernel/lifecycle)
*   [Virtual DOS machine - Wikipedia](https://en.wikipedia.org/wiki/Virtual_DOS_machine)
*   [Windows on Windows - Wikipedia](https://en.wikipedia.org/wiki/Windows_on_Windows)
*   [WoW64 - Wikipedia](https://en.wikipedia.org/wiki/WoW64)
*   [Windows Subsystem for Linux - Wikipedia](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)
*   [Compatibility layer - Wikipedia](https://en.wikipedia.org/wiki/Compatibility_layer)

#### [](#links-to-oss-i-use)Links to OSS I use

*   [PowerShell](https://github.com/PowerShell/Powershell)
*   [Visual Studio Code](https://github.com/microsoft/vscode)
*   [Windows Terminal](https://github.com/microsoft/terminal)
*   [Scoop](https://github.com/lukesampson/scoop)
*   [winget](https://github.com/microsoft/winget-cli)
*   [Microsoft Edge](https://www.microsoft.com/en-us/edge) - The source code for components used in the browser can be found [here](https://thirdpartysource.microsoft.com/)

##### [](#edit)Edit:

Some people might have interpreted it such, partly due to my mistake owing probably to the language. I did not intend to do a Linux vs Windows comparison myself, I just wanted this post to reflect on what Windows has historically been doing wrong/incorrect/annoying, and include my personal experience as well. I do not intend to convert people out there, that would be stupid. Thanks for pointing this out!
