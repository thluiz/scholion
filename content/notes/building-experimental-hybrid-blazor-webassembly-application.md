---
title: "Building experimental hybrid Blazor WebAssembly application"
date: '2026-11-16T15:49:49+00:00'
category: webclip
summary: 'The post describes a shared Blazor WebAssembly UI used by both desktop and web apps, notes the separate project setup and index.html differences, and reports that trimmed self-contained desktop publishing works well.'
tags: ["blazor-webassembly", "webwindow", "desktop-apps", "dotnet-publish"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building experimental hybrid Blazor WebAssembly application"
    url: "https://web.archive.org/web/20200305134438id_/https://gunnarpeipman.com/blazor-hybrid-application-experimental/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--building-experimental-hybrid-blazor-webassembly-application.md"
    kind: repo
---

The post describes an experiment to make a shared Blazor WebAssembly application run on desktop and in the browser. The UI lives in a shared project with pages, layouts, code-behind files, and shared interfaces, while the desktop and web projects mainly differ in hosting, dependency injection, and index.html setup.

It also says the desktop app can be published as a self-contained executable with assembly trimming, which reduces the output size and removes the separate JavaScript files from the publish folder.

## Reading notes

- WebWindow is presented as experimental technology for hosting Blazor WebAssembly apps in desktop windows through the local browser web view
- The author tried to make one single hybrid application, but ended up with a different architecture
- The shared project contains the UI artifacts, including pages, layouts, code-behind files, and shared interfaces
- The desktop and web projects are mainly used to build for the target environment and wire up dependency injection
- The application projects keep a wwwroot folder because static files are still needed
- App.razor was moved into the shared project, and the application projects no longer need _Imports.razor files
- Static assets in a shared library are not supported by Blazor on desktop, so they are copied during publishing
- The desktop project uses Microsoft.NET.Sdk.Razor, while the web project uses Microsoft.NET.Sdk.Web
- The desktop app starts through ComponentsDesktop.Run<Startup>
- The web app starts through BlazorWebAssemblyHost.CreateDefaultBuilder().UseBlazorStartup<Startup>()
- The desktop and web Startup classes differ in the IWeatherService implementation they register
- The desktop index.html loads styles directly and uses framework://blazor.desktop.js
- The web index.html loads styles from the _content folder and uses _framework/blazor.webassembly.js
- The desktop app runs inside an operating system window, while the web app runs in a browser
- Publishing the desktop app with PublishSingleFile and PublishTrimmed produces a much smaller executable
- The author says the desktop publish folder no longer contains the separate JavaScript files
