---
url: "https://www.hanselman.com/blog/CoolWSLWindowsSubsystemForLinuxTipsAndTricksYouOrIDidntKnowWerePossible.aspx"
captured_at: "2026-11-16T19:12:08+00:00"
title: "Cool WSL (Windows Subsystem for Linux) tips and tricks you (or I) didn't know were possible"
domain: "hanselman-com"
---

It's no secret I dig WSL (Windows Subsystem for Linux) and now that [WSL2](https://www.hanselman.com/blog/RubyOnRailsOnWindowsIsNotJustPossibleItsFabulousUsingWSL2AndVSCode.aspx) is available in [Windows Insiders Slow](https://insider.windows.com/) it's a great time to really explore the options that are available. What I'm finding is so interesting about WSL and how it relates to the Windows system around it is how you can cleanly move data between worlds. This isn't an experience you can easily have with full virtual machines, and it speaks to the tight integration of Linux and Windows.

Look at all this cool stuff you can do when you mix your peanut butter and chocolate!

### Run Windows Explorer from Linux and access your distro's files

When you're at the WSL/bash command line and you want to access your files visually, you can run "explorer.exe ." where . is the current directory, and you'll get a Windows Explorer window with your Linux files served to you over a local network plan9 server.

![Accessing WSL files from Explorer](https://images.hanselman.com/blog/Windows-Live-Writer/13aa5fd6017c_110EF/image_e370ffa0-eeb9-48a4-b8ac-490007201eff.png "Accessing WSL files from Explorer")

### Use Real Linux commands (not Cgywin) from Windows

I've blogged this before, but there are now aliases for PowerShell functions [that allow you to use real Linux commands](https://www.hanselman.com/blog/AWonderfullyUnholyAllianceRealLinuxCommandsForPowerShellWithWSLFunctionWrappers.aspx) from within Windows.

You can call any Linux command directly from DOS/Windows/whatever by just putting it after WSL.exe, like this!

C:\\temp> wsl ls -la | findstr "foo"  
\-rwxrwxrwx 1 root root     14 Sep 27 14:26 foo.bat

C:\\temp> dir | wsl grep foo  
09/27/2016  02:26 PM                14 foo.bat

C:\\temp> wsl ls -la > out.txt

C:\\temp> wsl ls -la /proc/cpuinfo  
\-r--r--r-- 1 root root 0 Sep 28 11:28 /proc/cpuinfo

C:\\temp> wsl ls -la "/mnt/c/Program Files"  
...contents of C:\\Program Files...

### Use Real Windows commands (not Wine) from Linux

Windows executables are callable/runnable from WSL/Linux because the the Windows Path is in the $PATH until Windows. All you have to do is call it with .exe at the end, explicitly. That's how "Explorer.exe ." works above. You can also notepad.exe, or whatever.exe!

### Run Visual Studio Code and access (and build!) your Linux apps natively on Windows

You can run "code ." when you're in a folder within WSL and you'll get prompted to [install the VS Remote extensions](https://code.visualstudio.com/blogs/2019/09/03/wsl2?WT.mc_id=-blog-scottha). That effectively splits Visual Studio Code in half and runs the headless VS Code Server inside Linux with the VS Code client in the Windows world.

> You'll also need to install [Visual Studio Code](https://code.visualstudio.com/download?WT.mc_id=-blog-scottha) and the [Remote - WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl&WT.mc_id=-blog-scottha). Optionally, check out the [beta Windows Terminal](https://www.microsoft.com/p/windows-terminal-preview/9n0dx20hk701?WT.mc_id=-blog-scottha) for the best possible terminal experience on Windows.

Here's a great series from the Windows Command LIne blog:

You can find the full series here:

*   Part 1 [Take your Linux development experience in Windows to the next level with WSL and Visual Studio Code Remote](https://devblogs.microsoft.com/commandline/take-your-linux-development-experience-in-windows-to-the-next-level-with-wsl-and-visual-studio-code-remote/?WT.mc_id=-blog-scottha)
*   Part 2 [An In Depth Tutorial on Linux Development on Windows with WSL and Visual Studio Code](https://devblogs.microsoft.com/commandline/an-in-depth-tutorial-on-linux-development-on-windows-with-wsl-and-visual-studio-code/?WT.mc_id=-blog-scottha)
*   Part 3 [Tips and Tricks for Linux development with WSL and Visual Studio Code](https://devblogs.microsoft.com/commandline/tips-and-tricks-for-linux-development-with-wsl-and-visual-studio-code/?WT.mc_id=-blog-scottha)

Here's the benefits of WSL 2

*   Virtual machines are resource intensive and create a very disconnected experience.
*   The original WSL was very connected, but had fairly poor performance compared to a VM.
*   WSL 2 brings a hybrid approach with a lightweight VM, a completely connected experience, and high performance.

Again, now available on Windows 10 Insiders Slow.

### Run multiple Linuxes in seconds, side by side

Here I'm running "wsl --list --all" and I have three Linuxes already on my system.

C:\\Users\\scott>wsl --list --all  
Windows Subsystem for Linux Distributions:  
Ubuntu-18.04 (Default)  
Ubuntu-16.04  
Pengwin

I can easily run them, and also assign a profile to each so they appear in my Windows Terminal dropdown.

### Run an X Windows Server under Windows using Pengwin

[Pengwin](https://www.pengwin.dev/) is a custom WSL-specific Linux distro that's worth the money. You can get it at the [Windows Store](https://afflnk.microsoft.com/c/1291904/433017/7593?u=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fp%2Fwlinux%2F9nv1gv1pxz6p&WT.mc_id=-blog-scottha). Combine Pengwin with an [X Server like X410](https://www.microsoft.com/en-us/p/x410/9nlp712zmn9q?WT.mc_id=-blog-scottha) and  you've got a very cool integrated system.

### Easily move WSL Distros between Windows systems

[Ana Betts points out this great technique](https://twitter.com/anaisbetts/status/1194386477855019008) where you can easily move your perfect WSL2 distro from one machine to _n_ machines.

wsl --export MyDistro ./distro.tar

\# put it somewhere, dropbox, onedrive, elsewhere

mkdir ~/AppData/Local/MyDistro  
wsl --import MyDistro ~/AppData/Local/MyDistro ./distro.tar --version 2 

That's it. Get your ideal Linux setup sync'ed on all your systems.

### Use the Windows Git Credential Provider within WSL

All of these things culminate in [this lovely blog post by Ana Betts](https://blog.anaisbetts.org/using-github-credentials-in-wsl2/) where she integrates the [Windows Git Credential Provider in WSL](https://blog.anaisbetts.org/using-github-credentials-in-wsl2/) by making /usr/bin/git-credential-manager into a shell script that calls the Windows git creds manager. Genius. This would only be possible given this clean and tight integration.

Now, go out there, install WSL, [Windows Terminal](https://www.hanselman.com/blog/HowToMakeAPrettyPromptInWindowsTerminalWithPowerlineNerdFontsCascadiaCodeWSLAndOhmyposh.aspx), and make yourself a [shiny Linux Environment on Windows](https://www.hanselman.com/blog/SettingUpAShinyDevelopmentEnvironmentWithinLinuxOnWindows10.aspx).

* * *

**Sponsor**: Like C#? We do too! That’s why we've developed a fast, smart, cross-platform .NET IDE which gives you even more coding power. Clever code analysis, rich code completion, instant search and navigation, an advanced debugger... With JetBrains Rider, everything you need is at your fingertips. Code C# at the speed of thought on Linux, Mac, or Windows. [Try JetBrains Rider today](https://hnsl.mn/2qeRmVA)!

#### About Scott

Scott Hanselman is a former professor, former Chief Architect in finance, now speaker, consultant, father, diabetic, and Microsoft employee. He is a failed stand-up comic, a cornrower, and a book author.

[![facebook](https://images.hanselman.com/main/icon-fb.png)](https://facebook.com/shanselman) [![bluesky](https://images.hanselman.com/main/icon-bluesky.png)](https://bsky.app/profile/scott.hanselman.com) [![subscribe](https://images.hanselman.com/main/icon-rss.png)](http://feeds.hanselman.com/ScottHanselman)  
[About](http://hanselman.com/about)   [Newsletter](http://www.hanselman.com/newsletter)

**Hosting By**  
[![Hosted on Linux using .NET in an Azure App Service](https://images.hanselman.com/main/azure-250x250.png)](https://azure.microsoft.com/free?WT.mc_id=-blog-scottha)
