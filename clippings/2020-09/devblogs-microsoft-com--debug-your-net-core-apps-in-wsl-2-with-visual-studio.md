---
url: "https://devblogs.microsoft.com/dotnet/debug-your-net-core-apps-in-wsl-2-with-visual-studio/"
captured_at: "2020-09-18T09:10:23-03:00"
title: "Debug Your .NET Core Apps in WSL 2 with Visual Studio | .NET Blog"
domain: "devblogs-microsoft-com"
---

# Debug Your .NET Core Apps in WSL 2 with Visual Studio

![aedbc07ce2d62ae405c96b74c240ce8b](devblogs-microsoft-com--debug-your-net-core-apps-in-wsl-2-with-visual-studio/8bd2b6b412bff7b58783127f91f19370.png)

Nathan

September 17th, 2020

Are you a .NET Core developer who loves working in Windows and Visual Studio, but needs to test your app in Linux? Are you a cross-platform developer that needs an easy way to test more of your target environments? Have you already discovered the benefits of WSL 2, but need a way to integrate it into your inner loop? Have I got an extension for you! The [.NET Core Debugging with WSL 2 – Preview](https://aka.ms/wsldebug) extension gives you the ability to run and debug your .NET Core apps in WSL 2 without leaving Visual Studio.

## When would I want to debug in WSL 2?

For a Windows .NET user targeting Linux, WSL 2 lives in a sweet spot between production realism and productivity. In Visual Studio you can already debug in a remote Linux environment using the [Remote Debugger](https://docs.microsoft.com/en-us/visualstudio/debugger/remote-debugging-dotnet-core-linux-with-ssh), or with containers using the [Container Tools](https://docs.microsoft.com/en-us/visualstudio/containers/overview). When production realism is your main concern, you should use one of those. When an easy and fast inner-loop is more important, WSL 2 is a great option.

> You don’t have to choose just one! You can have a launch profile for Docker and WSL 2 in the same project and pick whichever is appropriate for a particular run. And once your app is deployed, you can always use the Remote Debugger to attach to it if there is an issue.

## Getting Started with .NET Core Debugging with WSL 2 – Preview

Before using the extension, be sure to install [WSL 2](https://aka.ms/wsl2) and the [distribution](https://aka.ms/wslstore) of your choice. After you have installed the extension, when you open an ASP.NET Core web app or .NET Core console app in Visual Studio, you’ll see a new Launch Profile named **WSL 2**:

[![Wsl2Profile.png](devblogs-microsoft-com--debug-your-net-core-apps-in-wsl-2-with-visual-studio/768ca8d4451f9cdce95d831d7866a485.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2020/09/Wsl2Profile.png)

Selecting this profile will add it to your launchSettings.json, and will look something like:

```
"WSL 2":{"commandName":"WSL2","launchBrowser":true,"launchUrl":"https://localhost:5001","environmentVariables":{"ASPNETCORE_URLS":"https://localhost:5001;http://localhost:5000","ASPNETCORE_ENVIRONMENT":"Development"},"distributionName":""}
```

Once the new profile is selected, the extension checks that your WSL 2 distribution is configured to run .NET Core apps, and helps you install any missing dependencies. Once all the dependencies are installed, you are ready to debug in WSL 2. Simply start Debugging as normal, and your app will now be running in your default WSL 2 distribution. An easy way to verify that you are running in Linux is to check the value of [`Environment.OSVersion`](https://docs.microsoft.com/dotnet/api/system.environment.osversion).

> Note: Only Ubuntu and Debian have been tested and are supported. Other distributions supported by .NET Core should work but require manually installing the [.NET Core Runtime](https://aka.ms/wsldotnet) and [Curl](https://curl.haxx.se/).

## Using a specific distribution

By default, the WSL 2 launch profile will use the default distribution as set in wsl.exe. If you want your launch profile to target a specific distribution, regardless of that default, you can modify your launch profile. For example, if you are debugging a web app and want to test it on Ubuntu 20.04, your launch profile would look like:

```
"WSL 2":{"commandName":"WSL2","launchBrowser":true,"launchUrl":"https://localhost:5001","environmentVariables":{"ASPNETCORE_URLS":"https://localhost:5001;http://localhost:5000","ASPNETCORE_ENVIRONMENT":"Development"},"distributionName":"Ubuntu-20.04"}
```

## Targeting multiple distributions

Going one step further, if you are working on an application that needs to run in multiple distributions and you want a quick way to test on each of them, you can have multiple launch profiles. For instance, if you need to test your console app on Debian, Ubuntu 18.04, and Ubuntu 20.04, you could use the following launch profiles:

```
"WSL 2 : Debian":{"commandName":"WSL2","distributionName":"Debian"},"WSL 2 : Ubuntu 18.04":{"commandName":"WSL2","distributionName":"Ubuntu-18.04"},"WSL 2 : Ubuntu 20.04":{"commandName":"WSL2","distributionName":"Ubuntu-20.04"}
```

With these launch profiles, you can easily switch back and forth between your target distributions, all without leaving the comfort of Visual Studio:

[![Wsl2Profiles.png](devblogs-microsoft-com--debug-your-net-core-apps-in-wsl-2-with-visual-studio/2203bfb258a9569a96658e8df20fe710.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2020/09/Wsl2Profiles.png)

## Give it a try today!

So, if you love working in Visual Studio, but need to test your app in Linux, go to the [Visual Studio Marketplace](https://aka.ms/wsldebug) to install the extension today. Please use the marketplace to ask any questions and give us your feedback to let us know how useful this extension is.

[Download and Install](https://aka.ms/wsldebug)

##### [Nathan Carlson](https://devblogs.microsoft.com/dotnet/author/ncarlsonmicrosoft-com/)

Principal Software Engineer, Cloud Native Tools

**Follow**
