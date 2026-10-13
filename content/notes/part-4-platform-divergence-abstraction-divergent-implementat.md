---
title: "Part 4 - Platform Divergence/Abstraction/Divergent Implementation | xamarin"
date: '2013-08-05T13:51:25-03:00'
category: webclip
summary: 'The page explains how Xamarin apps should handle platform divergence, compare abstraction with divergent implementation, and use interfaces, inheritance, libraries, or conditional compilation to share code across iOS, Android, and Windows Phone.'
tags: ["xamarin", "platform-divergence", "platform-abstraction", "conditional-compilation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 4 - Platform Divergence/Abstraction/Divergent Implementation | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_4_-_platform_divergence_abstraction_divergent_implementation"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-4-platform-divergence-abstraction-divergent-implementat.md"
    kind: repo
---

Platform divergence is treated as a normal part of mobile development, because even devices on the same platform can differ in screen size, input, navigation, sensors, notifications, and other capabilities. Xamarin recommends designing for graceful degradation and deciding early which features are required and which should vary by platform.

## Reading notes

- Mobile apps share some universal patterns, such as tabs or menus, scrolling lists, single-item views, editing single-item views, and back navigation.
- Design still has to account for platform-specific differences like screen sizes, navigation metaphors, keyboards, touch and gesture support, and push notification implementations.
- Devices may lack a camera, location support, sensors, or NFC, so code often needs feature detection and fallback behavior.
- One approach to shared code is platform abstraction, using interfaces or base classes to hide platform details behind a common API.
- Interfaces let platform-specific code be passed into shared libraries, but the shared code must receive and manage those implementations.
- Inheritance can also share behavior, though it limits API design because C# allows only single inheritance.
- MonoTouch.Dialog and MonoDroid.Dialog are presented as abstraction layers for list-based screens on iOS and Android.
- Xamarin.Mobile adds cross-platform APIs for media picking, geolocation, and address book access.
- Divergent implementation can be handled with conditional compilation when the same source file is used in projects with different symbols.
- Xamarin.iOS does not include built-in conditional symbols, so any custom symbols must be defined and maintained in project settings.
- Xamarin.Android uses symbols such as __ANDROID__ and API-level directives like __ANDROID_11__.
- Windows Phone 7 defines WINDOWS_PHONE and SILVERLIGHT symbols.
- The SQLite file path example shows different storage rules on iOS, Android, and Windows Phone, with conditional compilation producing a correct path for each platform.
