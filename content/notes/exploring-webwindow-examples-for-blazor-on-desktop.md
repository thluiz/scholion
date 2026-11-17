---
title: "Exploring WebWindow examples for Blazor on desktop"
date: '2026-11-16T15:49:13+00:00'
category: webclip
summary: 'The page explains how WebWindow lets Blazor WebAssembly run in a desktop window, then walks through sample apps that show local HTML hosting, message passing, and file-based data loading.'
tags: ["blazor-desktop", "webwindow", "webassembly", "dotnet-core"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Exploring WebWindow examples for Blazor on desktop"
    url: "https://web.archive.org/web/20200316004858id_/https://gunnarpeipman.com/blazor-on-desktop-webwindow-experiment/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--exploring-webwindow-examples-for-blazor-on-desktop.md"
    kind: repo
---

The page presents WebWindow as an experimental cross-platform .NET Core library for running HTML, JavaScript, and WebAssembly in a local browser window. It uses it to show how Blazor WebAssembly can run on desktop without a web server and how the same desktop support fits the Blazor-everywhere idea.

## Reading notes

- WebWindow is an experimental project by Steve Sanderson, with no stable packages, templates, or polished tooling yet.
- Blazor WebAssembly can run without a web server because it only needs a rendering engine with WebAssembly support.
- WebWindow uses an existing browser or web renderer to open a local window and load the web app there.
- The experimental implementation works on Windows with Chromium-based Edge, on Linux with WebKit, and on Mac with Safari.
- The sample solution includes HelloWorldApp, VueFileExplorer, and BlazorDesktopApp.
- HelloWorldApp creates a WebWindow, loads a local index.html file, and waits until the window closes.
- VueFileExplorer shows two-way communication between the web view and the hosting .NET Core process through OnWebMessageReceived and SendMessage.
- In VueFileExplorer, the JavaScript UI sends commands such as navigateTo and showFile, and the host responds with directory or file data.
- BlazorDesktopApp runs the default Blazor WebAssembly sample, including Counter and Fetch data views, inside a desktop window.
- The weather forecast data in the Blazor desktop sample is read from wwwroot/sample-data/weather.json instead of being fetched with HttpClient.
- The page treats WebWindow and desktop support as promising, while noting that the project is still early and experimental.
