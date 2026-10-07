---
url: "http://www.infoq.com/news/2012/07/sqlite-metro-winmobile"
captured_at: "2012-07-09T19:55:22-03:00"
title: "SQLite On WinRT, Metro, Windows 8 Mobile"
domain: "infoq-com"
---

[SQLite](http://www.sqlite.org/index.html) is now supported on Windows RT, Windows 8 Metro Apps and will be supported on Windows Phone 8 for local application storage.

[SQLite version 3.7.13](http://www.sqlite.org/releaselog/3_7_13.html) adds support for WinRT and Metro style applications for Windows 8. [According to Microsoft](http://forwardthinking.pcmag.com/operating-systems/299394-microsoft-brings-windows-8-mobile), Windows 8 mobile will also support SQLite. Note though, that only the Engine will be available for you, without a client – you will have to [wrap it as a WinRT component](http://devhawk.net/tag/winrt-components/) (or use a library that does it for you) to actually use it in your .NET or JavaScript app.

.NET developers can use [sqlite-net](https://github.com/praeclarum/sqlite-net) which provides a LINQ wrapper for SQLite. A couple of useful walkthroughs to get you started with this -

*   [Using SQLite in your Windows 8 Metro style applications](http://wp.qmatteoq.com/using-sqlite-in-your-windows-8-metro-style-applications/) by Matteo Pagani
*   [Using SQLite in a Metro style app](http://timheuer.com/blog/archive/2012/05/20/using-sqlite-in-metro-style-app.aspx) by Tim Hueur

For JavaScript developers, there is [SQLite3-WinRT](https://github.com/doo/SQLite3-WinRT). And as Tim points out, C++ developers can use the sqlite.h header file and not really worry about WinRT wrappers.

There are a few restrictions to keep in mind, as explained in the announcement in the [SQLite website](http://www.sqlite.org/news.html). Other than that though, it should work just as it does for any other system.
