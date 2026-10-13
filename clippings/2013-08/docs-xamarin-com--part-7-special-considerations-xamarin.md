---
url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_7_-_special_considerations"
captured_at: "2013-08-05T13:52:35-03:00"
title: "Part 7 - Special Considerations | xamarin"
domain: "docs-xamarin-com"
---

# **P**art 7 - Special Considerations

PDF for Offline Use:
:   - [Download PDF](http://docs.xamarin.com/sites/xamarin.com/files/pdfs/part_7_-_special_considerations-18632.pdf)

# 1**.** Things to Avoid

## 1**.**1. Code Generation

Generating code dynamically with System.Reflection.Emit should be avoided in
shared code**.** Although it is supported on some platforms (such as Android) it
will not work across all products**.**

Apple’s kernel prevents dynamic code generation on iPhone and iPad,
therefore emitting code on-the-fly will not work in Xamarin.iOS**.** Likewise the
Dynamic Language Runtime features cannot be used with Xamarin tools**.**

Some reflection features do work (eg**.** MonoTouch.Dialog uses it for the
ReflectionAPI), just not code generation**.**

## 1.2. Lowest-Common-Denominator User Interfaces

One of Xamarin’s strengths is the ability to build a native UI on each
platform**.** Avoid re-using the user-interface design across iOS, Android and
Windows Phone without tweaking it for each platform**.** For example, don’t build
a ‘Back’ button into your Android or Windows Phone applications, and don’t
build a custom tabbed-control for iOS where the tabs sit across the top of the
screen**.** Use the metaphors that the users on each platform are familiar with**.**
