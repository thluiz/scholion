---
url: "https://blogs.windows.com/windowsdeveloper/2019/11/18/developing-on-windows-hello-world/#SMUf7O9Fhj6o28mX.97"
captured_at: "2026-11-16T19:13:26+00:00"
title: "Developing on Windows – Hello World"
domain: "blogs-windows-com"
---

Hello (Dev) World!

My name is Avri ??‍ and I’m a Program Manager here at Microsoft focused on improving the Windows developer experience! I’m a member of the engineering team here, where I get to collaborate with a bunch of other FANTASTIC people to create and improve Windows developer tools; and in this blog series, I’ll call out tons of ways to improve your end-to-end dev experience. Blogs in this series will include news on Windows Terminal, Windows Subsystem for Linux (WSL), Windows Performance, VS Code and Visual Studio, VM’s and Containers, Developer PowerToys, and more!

So, what’s new in the Windows Developer World?

## **Using Windows Terminal and WSL to build web applications**

If you’re anything like me, you’re a huge fan of multitasking. Well, with some of the new updates from Windows Terminal and WSL2, finding time to do it all is now a dream come true. You can start by creating your web application in the new Windows Terminal. Let’s say you’re running a script but want to keep an eye on some tasks you have open in the background. You can change the opacity of your window with “**Ctrl+Shift+scroll**” and be the multitasking champ! As a fresh-out of college grad, I distinctly remember the days (everyday) of working on more than one assignment at once. And now that I’m an FTE, the number of things I must do at one time has increased four fold. Cool updates like this one to Windows Terminal though help me stay on task(s).

In addition to being workload friendly, you can also run the Windows Subsystem for Linux (WSL) in Windows Terminal. And with the release of [Windows Terminal v0.6](https://devblogs.microsoft.com/commandline/windows-terminal-preview-1910-release/), any WSL distribution installed will be automatically detected and added to the profiles.json file! My favorite distro is Ubuntu, and with WSL, you can use your favorite Linux commands on Windows!

The next generation of WSL, called WSL 2, has released to Windows Insiders! WSL2 has full system call compatibility and significantly faster file system performance. WSL 2 also works great with VS Code! From a WSL 2 prompt, navigate to your project folder, enter “code.” and your project will open in VS Code using the WSL remote extension.

Here’s the cool thing about WSL2 and VS Code – the only thing happening on the Windows side is the UI, which means everything else (the debugger, interpreter, and installed extensions) are all running in WSL! For all files, you can open, edit, set break points and debug! **As Craig eloquently states in the video, “you can get the full debugging experience inside of Windows, inside of VS Code, running on Linux.”**

![Gif of man opening briefcase](https://blogs.windows.com/wp-content/uploads/prod/sites/3/2019/11/784d2e39e308e719af7a9305edeb610c.gif)

Check out the video here if you want to see how you can do even more with Windows Terminal and WSL2!

## **Updates to Windows Developer Tools** 

## Windows Terminal

[Terminal Preview v0.6 release](https://devblogs.microsoft.com/commandline/windows-terminal-preview-v0-4-release/)

In case you missed it, there have been many updates to the Windows Terminal (now [available in the Microsoft Store](https://www.microsoft.com/en-us/p/windows-terminal-preview/9n0dx20hk701) and [on Github](https://github.com/microsoft/terminal))! New features include and updated tab UI, [a new font](https://github.com/microsoft/cascadia-code/releases), and more!

## WSL2 – Windows Subsystem for Linux 2

[We recently announced](https://devblogs.microsoft.com/commandline/tips-and-tricks-for-linux-development-with-wsl-and-visual-studio-code/) some stellar updates to WSL2 as well. Checkout this [new blog](https://t.co/2pcudvMZmR?amp=1) on memory reclamation.

## PowerToys – Windows system utilities to maximize productivity

The newest preview release of PowerToys contains three utilities – FancyZones, Windows Shortcut Guide, and PowerRename – with all the code for the project on [GitHub](https://github.com/Microsoft/PowerToys). The repo also contains the information and tools you need to understand how the PowerToys’ utilities work together and how to create your own utilities. More information is available in the [Windows Insider blog post on PowerToys](https://insider.windows.com/en-us/articles/announcing-the-first-preview-and-code-release-of-powertoys/).

## Signing Off

It’s amazing what determined minds can make happen. The team is amped to ship all these great features, updates, and bug fixes to you all. Leave us some feedback below. I’m signing off for now but stay tuned and be sure to follow this blog series for all things dev on Windows!

Oh! And follow me on Twitter (@[AvriNichole](https://twitter.com/AvriNichole)) for more news. ✌?
