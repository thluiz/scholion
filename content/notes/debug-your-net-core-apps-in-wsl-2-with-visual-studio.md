---
title: "Debug Your .NET Core Apps in WSL 2 with Visual Studio"
date: '2020-09-18T09:10:23-03:00'
category: webclip
summary: 'The .NET Core Debugging with WSL 2 – Preview extension lets you run and debug .NET Core apps in WSL 2 from Visual Studio, with launch profiles for the default or a chosen distribution.'
tags: ["dotnet-core", "wsl-2", "visual-studio", "debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Debug Your .NET Core Apps in WSL 2 with Visual Studio | .NET Blog"
    url: "https://devblogs.microsoft.com/dotnet/debug-your-net-core-apps-in-wsl-2-with-visual-studio/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/devblogs-microsoft-com--debug-your-net-core-apps-in-wsl-2-with-visual-studio.md"
    kind: repo
---

The post introduces a Visual Studio extension that lets .NET Core developers run and debug apps in WSL 2 without leaving Visual Studio. It positions WSL 2 as a middle ground between remote Linux debugging and containers when the goal is a fast inner loop for Linux testing.

## Reading notes

- The extension is called .NET Core Debugging with WSL 2 – Preview.
- It lets you run and debug .NET Core apps in WSL 2 from Visual Studio.
- The post says WSL 2 is useful for Windows developers targeting Linux when fast inner-loop testing matters.
- Visual Studio already supports remote debugging on Linux and debugging with containers.
- The post says remote debugging and containers are better when production realism is the main concern.
- To use the extension, you first need WSL 2 and a Linux distribution installed.
- After installation, Visual Studio adds a new WSL 2 launch profile for ASP.NET Core web apps and .NET Core console apps.
- Selecting the profile adds it to launchSettings.json.
- The extension checks whether the WSL 2 distribution is set up for .NET Core apps and helps install missing dependencies.
- Debugging starts normally after setup, and the app runs in the default WSL 2 distribution.
- The post suggests checking Environment.OSVersion to confirm the app is running in Linux.
- Only Ubuntu and Debian were tested and are supported.
- Other .NET Core-supported distributions may work if the .NET Core Runtime and Curl are installed manually.
- The launch profile can be edited to target a specific distribution such as Ubuntu 20.04.
- Multiple launch profiles can be used to test the same app across Debian, Ubuntu 18.04, and Ubuntu 20.04.
- This lets developers switch between target distributions from Visual Studio.
