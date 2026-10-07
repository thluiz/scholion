---
title: "SQLite On WinRT, Metro, Windows 8 Mobile"
date: '2012-07-09T19:55:22-03:00'
category: webclip
summary: 'SQLite 3.7.13 now supports Windows RT and Windows 8 Metro apps, and Windows Phone 8 is expected to support it for local storage. Developers may need a WinRT wrapper, depending on the platform and language.'
tags: ["sqlite", "winrt", "windows-8", "windows-phone-8"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SQLite On WinRT, Metro, Windows 8 Mobile"
    url: "http://www.infoq.com/news/2012/07/sqlite-metro-winmobile"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/infoq-com--sqlite-on-winrt-metro-windows-8-mobile.md"
    kind: repo
---

SQLite 3.7.13 adds support for Windows RT and Windows 8 Metro-style apps, and Microsoft says Windows 8 mobile will also support SQLite. For actual use in .NET or JavaScript apps, the engine must be wrapped as a WinRT component or accessed through a library that does that work.

.NET developers can use sqlite-net for a LINQ wrapper. JavaScript developers can use SQLite3-WinRT, and C++ developers can work with sqlite.h without worrying about WinRT wrappers. The announcement also mentions some restrictions, but otherwise SQLite should work like it does on other systems.

## Reading notes

- SQLite is supported on Windows RT, Windows 8 Metro apps, and will be supported on Windows Phone 8 for local application storage.
- SQLite 3.7.13 adds support for WinRT and Metro style applications for Windows 8.
- Windows 8 mobile will also support SQLite, according to Microsoft.
- Only the engine is available; .NET or JavaScript apps need a WinRT component wrapper or a library that provides one.
- .NET developers can use sqlite-net, which provides a LINQ wrapper for SQLite.
- JavaScript developers can use SQLite3-WinRT.
- C++ developers can use the sqlite.h header file without WinRT wrappers.
- The SQLite announcement mentions a few restrictions, but says it should otherwise work like on other systems.
