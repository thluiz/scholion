---
title: "Building Cross Platform Applications | Xamarin"
date: '2013-08-05T13:47:44-03:00'
category: webclip
summary: 'The guide explains how Xamarin supports cross-platform mobile apps by combining shared C# and .NET code with native UIs on iOS, Android, and Windows Phone, using a layered architecture and core library for reuse.'
tags: ["xamarin", "cross-platform", "mobile-apps", "architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Cross Platform Applications | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--building-cross-platform-applications-xamarin.md"
    kind: repo
---

The guide says Xamarin lets teams share a single C# and .NET codebase across iOS, Android, and Windows while still building native user interfaces for each platform. It recommends separating platform-agnostic core code from UI code so business logic, storage, and services can be reused without forcing a generic interface.

## Reading notes

- Xamarin is presented as a way to keep one modern language and framework across three major mobile platforms while still accessing native SDKs and device capabilities.
- The document focuses on productivity and utility apps, not games.
- “Write-once, run everywhere” is treated as too limiting because it can produce lowest-common-denominator features and generic UI.
- The key architectural idea is to keep the model and shared services in a reusable core and build platform-specific user interfaces on top of it.
- The guide recommends C# for app code.
- It recommends MVC or MVVM with a clear separation between the model and the rest of the app.
- Native UI layers are listed for iOS, Android, Windows Phone, and Windows 8.
- The document points to shared components such as SQLite-NET for local storage, Xamarin.Mobile for device features, and framework features for networking, web services, and IO.
- Two case studies are named: Tasky Pro and MWC 2012.
- Tasky Pro is described as a simple to-do app for iOS, Android, and Windows Phone using a local SQLite database.
- MWC 2012 is described as a conference schedule app with SQLite support, remote data download, image caching, separate UI for iPad and iPhone, Android and Windows Phone support, and Live Tiles on Windows Phone.
- The summary says the document also briefly covers testing and links to the case studies.
