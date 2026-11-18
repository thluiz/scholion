---
title: "Xamarin.Essentials: Now with Permissions, App Theme, & Authentication"
date: '2020-07-05T14:11:24+00:00'
category: webclip
summary: 'Overview of Xamarin.Essentials 1.5 updates: requested app theme support, simplified runtime permissions API, web authentication integration, and plans for macOS and new features.'
tags: ["xamarin-essentials", "mobile-development", "permissions", "authentication"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Get Permissions, App Theme, & Authentication | Xamarin Blog"
    url: "https://web.archive.org/web/20200812092316id_/https://devblogs.microsoft.com/xamarin/xamarin-essentials-now-with-permissions-app-theme-authentication/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--xamarin-essentials-1-5-permissions-theme-auth.md"
    kind: repo
---

The post outlines new capabilities added in Xamarin.Essentials 1.5, building on its role as a cross-platform library for native features across iOS, Android, UWP, Tizen, watchOS, and tvOS. Highlights include an API to query the system’s requested app theme for light/dark mode handling, a simplified permissions API for features like geolocation and camera, and web authentication support that works well with ASP.NET Core. The author also previews Xamarin.Essentials 1.6 with macOS support and several community-driven features, and points to documentation and samples for getting started.

## Reading notes

- Xamarin.Essentials simplifies access to complex native features in a single cross-platform library for iOS, Android, UWP, Tizen, watchOS, and tvOS.
- Version 1.5 adds more cross-platform capabilities that developers can start using immediately.
- Modern operating systems support dark mode, and apps often need to know the user’s default theme preference.
- A new API (`AppInfo.RequestedTheme`) lets apps read the requested app theme to react to light/dark mode changes when using dynamic themes.
- The MyContacts sample on GitHub demonstrates a real-world use of app theme handling with Xamarin.Essentials.
- Using geolocation, contacts, or the camera requires requesting user permissions.
- Xamarin.Essentials provides a simplified permissions API where developers declare permissions in app configuration and then check/request them from shared code.
- The example shows checking a permission’s status asynchronously and requesting it if it is not granted, with a note that users might also need prompting to enable it in settings.
- Web authentication support in Xamarin.Essentials helps add authentication to mobile apps.
- Web authentication pairs well with ASP.NET Core for building authenticated mobile experiences.
- Jon Dick wrote a separate, detailed blog post explaining how to set up web authentication with Xamarin.Essentials.
- Readers are encouraged to follow Jon’s blog post for setup steps and then return to this overview.
- At .NET Conf – Focus on Xamarin, the team announced plans for Xamarin.Essentials 1.6.
- Xamarin.Essentials 1.6 is planned to include official macOS support.
- The next release will incorporate community pull requests such as File Picker, Haptic Feedback, App Actions, Calendar, and additional features.
- The post encourages developers to like and follow the Xamarin.Essentials GitHub repository to track updates.
- Xamarin.Essentials is already included in every project template.
- Developers are advised to upgrade to the latest Xamarin.Essentials version via NuGet.
- Existing apps can integrate Xamarin.Essentials by following the official getting started documentation.
