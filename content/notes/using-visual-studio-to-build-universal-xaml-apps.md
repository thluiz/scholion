---
title: "Using Visual Studio to build Universal XAML Apps"
date: '2014-04-28T21:44:17-03:00'
category: webclip
summary: 'The post explains how Visual Studio Update 2 RC supports universal XAML apps for Windows 8.1 and Windows Phone 8.1, including templates, shared projects, conditional code, and debugging tools.'
tags: ["visual-studio", "universal-apps", "xaml", "windows-phone-8-1"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using Visual Studio to build Universal XAML Apps - The Visual Studio Blog - Site Home - MSDN Blogs"
    url: "http://blogs.msdn.com/b/visualstudio/archive/2014/04/14/using-visual-studio-to-build-universal-xaml-apps.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-04/blogs-msdn-com--using-visual-studio-to-build-universal-xaml-apps.md"
    kind: repo
---

The post says Visual Studio Update 2 RC adds features for building universal XAML and HTML apps that run on both Windows 8.1 and Windows Phone 8.1. It also points readers to a blog post or a Build talk for more detail.

## Reading notes

- New project templates provide the basic structure and configuration needed to share code and content across universal apps in C#, C++, and JavaScript.
- Existing Windows 8.1 apps can use the Add Windows Phone 8.1 command to add a Windows Phone 8.1 project and a shared project, and the reverse is also available.
- A universal app is made of a Windows Store project, a Windows Phone project, and a Shared project, with the platform projects producing the .appx packages.
- The Shared project holds content used by both platforms, supports item types such as .cs, xaml, .xml, .png, and .resw, and does not produce a binary output on its own.
- Shared code can use #if and #endif directives, and Visual Studio defines conditional compilation constants for C# and C++ to separate platform-specific code.
- In a Shared project, the project context switcher changes the active target and affects IntelliSense in the editor.
- The debug target dropdown can switch startup projects and lists the projects in the solution that can be deployed to a device or emulator or simulator.
- Code can be shared across universal apps with class libraries; for C# and Visual Basic, the post says Portable Class Libraries now support Windows Runtime and XAML for Windows 8.1 and Windows Phone 8.1.
- For C++, new Class Library project templates under Universal Apps can be used with shared projects to share code between Windows 8.1 and Windows Phone 8.1 class libraries.
