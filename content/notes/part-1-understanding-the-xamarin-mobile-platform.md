---
title: "Part 1 - Understanding the Xamarin Mobile Platform"
date: '2013-08-05T13:48:19-03:00'
category: webclip
summary: 'The page explains Xamarin as a C# and .NET-based platform for iOS and Android, how compilation and SDK access differ by system, and how code, UI, and libraries can be reused across platforms.'
tags: ["xamarin", "cross-platform", "ios", "android"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 1 - Understanding the Xamarin Mobile Platform | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_1_-_understanding_the_xamarin_mobile_platform"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-1-understanding-the-xamarin-mobile-platform.md"
    kind: repo
---

Xamarin is presented as a platform built from C#, Mono .NET, a compiler, and IDE tools. The page says this setup lets developers write for iOS and Android with familiar C# syntax, share code across platforms, and reuse that code for Windows Phone in some cases.

## Reading notes

- Xamarin combines C#, Mono .NET, compiler support, and IDE tools for building iOS and Android apps.
- C# gives access to familiar syntax and features such as Generics, Linq, and the Parallel Task Library.
- The compiler targets each platform differently, producing native iOS apps or Android apps with MonoVM and JIT, while stripping unused code during linking.
- Platform SDKs are exposed through C# namespaces, including CocoaTouch on iOS and Android SDK namespaces on Android.
- Business logic, database access, network access, and other common functions can be written once and reused across platforms.
- Xamarin development can be done in Xamarin Studio or Visual Studio, depending on the target platforms.
- iOS development requires a Mac, Xcode, and Apple’s Developer Program for device testing and distribution.
- Android development requires Java and the Android SDK, and can be done on Mac or Windows with Xamarin Studio or Visual Studio.
- Windows Phone apps are built with Microsoft’s Visual Studio toolset, and C# code can still be shared with iOS and Android.
- Xamarin uses native UI controls, and screens can be built in code or with platform-specific visual designers.
- The page lists platform-specific UI patterns such as iOS hierarchical navigation, Android back button and action menu, and Windows Phone panorama layout and live tiles.
- Existing C# code and libraries can be reused, including SQLite-NET, NewtonSoft.JSON, and SharpZipLib.
- Xamarin.iOS can use Objective-C libraries through btouch bindings, and Xamarin.Android can use Java libraries through .jar bindings.
- P/Invoke can connect C# code to native C libraries, including SQLite on iOS and Android.
- C++ access is discussed through Cxxi or by wrapping C++ in C and binding through P/Invoke.
