---
title: "Part 3 - Setting Up A Xamarin Cross Platform Solution"
date: '2013-08-05T13:50:59-03:00'
category: webclip
summary: 'The page explains how Xamarin cross-platform solutions are organized around a blank solution, shared code, and platform-specific app projects, with references, build actions, and file naming kept aligned.'
tags: ["xamarin", "cross-platform", "code-sharing", "project-structure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 3 - Setting Up A Xamarin Cross Platform Solution | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_3_-_setting_up_a_xamarin_cross_platform_solution"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-3-setting-up-a-xamarin-cross-platform-solution.md"
    kind: repo
---

The page describes how a Xamarin cross-platform solution is built from a blank solution and then divided into shared code and platform-specific application projects. It outlines file-linking, platform-specific libraries, and portable class libraries as ways to share code, then shows a layered structure for core logic and UI code.

## Reading notes

- Xamarin projects use the same .SLN solution format across platforms, and solutions can be shared even when some projects cannot be loaded in a given environment.
- A new cross-platform application starts with a blank solution, then projects are added for the target mobile platforms.
- File-linking lets the same code files live in a separate directory and be included in each app project, but changes must be synchronized manually.
- Platform-specific library projects can share code at the C# file level, use compiler directives, and reference platform-specific assemblies when those references stay inside directive boundaries.
- Portable Class Libraries can be used across Xamarin.iOS, Xamarin.Android, and other .NET platforms, but they only expose a subset of the .NET framework.
- Xamarin’s support for Portable Class Libraries is described as currently under development.
- The solution should use a layered architecture that separates shared core code from platform-specific application projects.
- The Core project should hold reusable code and keep implementation details hidden where possible.
- Platform-specific application projects should consume the shared code with minimal coupling and add platform-only features there.
- Source within each project should be organized physically with directories and logically with namespaces.
- Shared code projects should reference only assemblies available across all platforms, such as System, System.Core, and System.Xml.
- The core layers described are Data Layer, Data Access Layer, Service Access Layer, and Business Layer.
- Platform-specific projects should reference the Core project and the platform SDK, and they should implement an Application Layer and a User Interface Layer.
- The example architecture shows a shared Core project alongside iOS and Android app projects.
- Project references express dependencies: core projects stay limited to common assemblies, while app projects add the platform SDKs they need.
- Shared-code files must be added or linked manually into each Core project, one for each platform.
- Platform-specific projects should manage code and resources independently, including images, XML, and other files.
- Build actions differ by file type, including Compile for C# files, Content for some images, InterfaceDefinition for XIB and Storyboard files, AndroidResource for Android images and AXML layouts, and Page for Windows Phone XAML files.
- The page warns that iOS and Android file systems can be case-sensitive, so file names in code must match the filesystem exactly.
