---
title: "Introducing .NET Multi-platform App UI"
date: '2020-07-05T14:11:16+00:00'
category: webclip
summary: '.NET MAUI is presented as a new first-class UI framework for unified .NET, extending Xamarin.Forms to desktop and mobile with a single project, shared resources, and support for MVVM and MVU.'
tags: ["net-maui", "xamarin-forms", "multi-platform-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introducing .NET Multi-platform App UI"
    url: "https://devblogs.microsoft.com/dotnet/introducing-net-multi-platform-app-ui"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--introducing-net-multi-platform-app-ui.md"
    kind: repo
---

The post announces .NET MAUI as the next step in unified .NET, built to cover Android, iOS, macOS, and Windows from one framework. It extends Xamarin.Forms to desktop, keeps native platform features accessible, and aims to let developers share more code while building native apps.

## Reading notes

- .NET 5 starts the unification of .NET Core and Mono/Xamarin into one BCL and SDK.
- .NET MAUI is introduced as a first-class UI framework for multi-platform device apps.
- The framework is described as an evolution of Xamarin.Forms that also embraces desktop.
- It supports Android, iOS, macOS, and Windows through a single stack.
- The project model centers on one project for multiple targets.
- Resources such as images, fonts, and translation files live in one place.
- Platform-specific source can be added under platforms to reach native APIs.
- The post says .NET MAUI will work with Visual Studio 2019, Visual Studio for Mac, and Visual Studio Code.
- It keeps MVVM and XAML as first-class patterns.
- It also enables MVU in C#, and mentions Blazor as a future capability.
- Xamarin.Forms developers are meant to move into .NET MAUI with the same controls and APIs.
- The team plans try-convert support and migration guides.
- Previews are planned for later in 2020, with general availability targeted for .NET 6 in November 2021.
- Xamarin.iOS and Xamarin.Android will become part of .NET 6 as .NET for iOS and .NET for Android.
- Xamarin.Forms and Xamarin SDKs will continue with servicing during the transition.
- The post points readers to the dotnet/maui repository to follow proposals and development.
