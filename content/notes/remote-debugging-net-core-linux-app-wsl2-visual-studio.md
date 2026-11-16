---
title: "Remote Debugging a .NET Core Linux app in WSL2 from Visual Studio on Windows"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'The post shows how to debug a .NET Core web app running in WSL2 from Visual Studio 2019 on Windows, using vsdbg, a launch.json file, and a Command Window launch.'
tags: ["wsl2", "visual-studio", "dotnet-core", "remote-debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Remote Debugging a .NET Core Linux app in WSL2 from Visual Studio on Windows"
    url: "https://hanselman.com/blog/RemoteDebuggingANETCoreLinuxAppInWSL2FromVisualStudioOnWindows.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hanselman-com--remote-debugging-net-core-linux-app-wsl2-visual-studio.md"
    kind: repo
---

The post describes a workable but manual setup for remote debugging a .NET Core app running in WSL2 from Visual Studio on Windows. It uses Ubuntu 18.04 under WSL2, a .NET Core web app, a debugger installed in Linux with vsdbg, and a launch.json file to connect the pieces.

The author says Visual Studio can reach the project if it is stored under c:\temp and accessed from Linux through /mnt/c/temp, since opening projects across the Linux path boundary causes issues. To start debugging, he uses a Visual Studio automation command from the Command Window instead of an F5 button, and notes that Visual Studio would need new work to make this automatic.

## Reading notes

- Visual Studio Code already supports a split setup where Windows runs the editor and Linux runs the language services and debugger through VS Code Server.
- The author still wants Visual Studio on Windows because VS Code is a code editor rather than a full IDE.
- The setup uses WSL2 on Windows 10, Visual Studio 2019 Community, and .NET Core with C#.
- He creates a .NET Core app with dotnet new razor and runs it in Linux.
- Visual Studio has trouble opening projects across the Linux network boundary, so he keeps the project in c:\temp and accesses it from Linux through /mnt/c/temp.
- He installs vsdbg in WSL with a curl command.
- The launch.json includes $adapter and $adapterArgs, plus program, cwd, serverReadyAction, env, sourceFileMap, pipeTransport, and logging settings.
- Visual Studio and Visual Studio Code use launch.json files to give the debugger enough information.
- Starting debugging requires a Visual Studio automation command typed in the Command Window.
- The author says the process works, but it is not automatic yet.
- He asks whether Visual Studio should support this setup with easier WSL debugging, similar to the F5 experience in VS Code.
