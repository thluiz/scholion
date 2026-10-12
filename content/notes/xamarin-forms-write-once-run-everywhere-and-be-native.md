---
title: "Xamarin.Forms - Write Once, Run Everywhere, AND Be Native? - Scott Hanselman"
date: '2014-07-10T08:44:42-03:00'
category: webclip
summary: 'Scott Hanselman argues that Xamarin.Forms lets shared C# code build native-looking mobile UIs by mapping high-level controls to native platform controls at runtime, while sharing most feed and tweet logic too.'
tags: ["xamarin-forms", "cross-platform", "native-ui", "c-sharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Xamarin.Forms - Write Once, Run Everywhere, AND Be Native? - Scott Hanselman"
    url: "http://www.hanselman.com/blog/XamarinFormsWriteOnceRunEverywhereANDBeNative.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/hanselman-com--xamarin-forms-write-once-run-everywhere-and-be-native.md"
    kind: repo
---

Scott Hanselman presents Xamarin.Forms as a way to share C# code across iOS, Android, and Windows Phone while still rendering native controls on each platform. He contrasts it with older Java-style cross-platform UIs that worked everywhere but did not integrate with the host platform.

The post shows a sample app where the navigation menu, blog list, and loading indicator are built from Xamarin.Forms controls and layouts, while the RSS and Twitter loading logic stays shared in async code and XML parsing. Hanselman’s main point is that the framework keeps the native look and feel without forcing separate UI and logic code for every platform.

## Reading notes

- Xamarin.Forms abstracts controls to a higher level but maps them to native controls at runtime.
- The same shared C# codebase can build UIs for iOS, Android, and Windows Phone.
- The sample Hanselman app aggregates the blog and tweets and runs natively on all three platforms.
- UI code uses shared concepts like StackLayout, ListView, DataTemplate, ActivityIndicator, and binding.
- The app’s feed loading and parsing logic is shared, using HttpClient, async and await, and Linq to XML.
- The post argues that native look comes from wrapping native controls, not from inventing new ones.
- Xamarin.Forms is presented as a way to hide repetitive cross-platform UI work while keeping the option to use platform specifics when needed.
