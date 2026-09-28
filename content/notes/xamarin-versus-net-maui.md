---
title: "Xamarin Versus .NET MAUI"
date: '2022-05-31T08:35:09-03:00'
category: webclip
summary: 'The post compares Xamarin.Forms and .NET MAUI across architecture, project structure, platform support, build tooling, rendering, resources, hot reload, graphics, accessibility, patterns, Blazor, device APIs, and multi-window support.'
tags: ["net-maui", "xamarin-forms", "mobile", "microsoft"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Xamarin Versus .NET MAUI | Syncfusion Blogs"
    url: "https://www.syncfusion.com/blogs/post/xamarin-versus-net-maui.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/syncfusion-com--xamarin-versus-net-maui.md"
    kind: repo
---

The post says .NET MAUI is an evolution of Xamarin.Forms for building native cross-platform apps with .NET. It presents MAUI as part of the move to a unified .NET platform and says developers familiar with Xamarin can learn it quickly.

## Reading notes

- Xamarin.Forms is described as a layer that lets shared code interact with Android, iOS, and Windows, while .NET MAUI builds native cross-platform apps for Android, iOS, macOS, and Windows.
- The article says MAUI is built on top of Xamarin.Forms and is integrated with .NET 6.
- Xamarin.Forms uses separate projects per platform, while MAUI uses a single project with platform folders and multi-targeting.
- Xamarin supports UWP, while MAUI supports WinUI.
- MAUI runs on the .NET CLI, while Xamarin is described as using .NET Framework to build and run apps.
- Xamarin uses renderers, while MAUI uses handler architecture that is more loosely coupled to native assemblies.
- MAUI includes .NET 6 and C# 10 features such as source generators, record structs, interpolated string handlers, and global using directives.
- The article says MAUI simplifies resource maintenance, especially by using SVG images instead of separate platform-specific image sets.
- Xamarin has limited or no .NET hot reload support, while MAUI supports .NET hot reload and XAML hot reload.
- MAUI adds graphics APIs for drawing and painting shapes, which the post says Xamarin does not provide directly.
- MAUI uses the .NET Generic Host to initialize fonts, services, and third-party libraries from one place.
- For accessibility, the post says MAUI recommends semantic properties, while Xamarin typically uses automation properties and native APIs.
- Both frameworks support MVVM and ReactiveUI, and MAUI also lists MVU as experimental.
- The article says Blazor hybrid apps are not possible in Xamarin, but they can be built with .NET MAUI.
- Both frameworks provide cross-platform device APIs, with MAUI using the Microsoft.Maui.Essentials namespace.
- MAUI supports multiple windows on Android, iPadOS, Mac Catalyst, and Windows, while Xamarin does not.
