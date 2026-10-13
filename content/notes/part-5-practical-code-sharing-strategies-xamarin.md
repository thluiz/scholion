---
title: "Part 5 - Practical Code Sharing Strategies | xamarin"
date: '2013-08-05T13:51:58-03:00'
category: webclip
summary: 'The page outlines cross-platform sharing strategies for data, files, network access, web services, threading, and capability handling in Xamarin apps, using common APIs and shared code where possible.'
tags: ["xamarin", "cross-platform", "shared-code", "mobile-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 5 - Practical Code Sharing Strategies | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_5_-_practical_code_sharing_strategies"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-5-practical-code-sharing-strategies-xamarin.md"
    kind: repo
---

The page reviews practical ways to share code across Xamarin.iOS, Xamarin.Android, and Windows Phone. It recommends common approaches for data storage, file access, network operations, web services, and threading, while noting where platform-specific APIs still differ.

## Reading notes

- The data layer is described as a storage engine plus read and write methods, and SQLite is recommended for Xamarin cross-platform apps because it is flexible and runs on many platforms.
- SQLite is available natively on iOS and Android, while Windows Phone can use the open-source C# SQLite assembly shipped with the app.
- Native database APIs do not share code well, except perhaps the SQL strings themselves.
- Xamarin.iOS and Xamarin.Android support System.Data and Mono.Data.Sqlite, which lets you write ADO.NET code that works on both platforms.
- The example shows creating a database file, opening a SqliteConnection, creating a table on first run, inserting sample data, and reading rows back.
- SQLite-NET is presented as a cross-platform ORM that maps classes to tables and lets code insert, query, and delete objects without writing SQL statements.
- SQLite-NET uses attributes on model classes, a SQLiteConnection subclass for the database instance, and supports basic Linq queries.
- Windows Phone 7 does not include a compatible database engine, so the case studies use a ported C# SQLite assembly to share the same database code across all three platforms.
- File access is treated as a common part of applications, including SQLite files, user-generated content, and cached downloads.
- System.IO can be used on Xamarin.iOS and Xamarin.Android, but each platform has different restrictions on filesystem access.
- iOS runs in a sandbox, Android restricts certain directories but allows external media and shared data, and Windows Phone 7 only allows isolated storage.
- Path.Combine and consistent filename casing are recommended when writing cross-platform file code.
- Isolated Storage is described as a common API for saving and loading files across all three platforms and as the default file mechanism for Windows Phone.
- Most mobile apps need networking for downloads, uploads, and access to web services or third-party APIs.
- WebClient provides a simple API for remote data, and Windows Phone operations must be asynchronous.
- WebClient also supports downloading binary data through DownloadFileCompleted and DownloadFileAsync.
- HttpWebRequest offers more customization than WebClient but requires more code.
- Reachability is recommended before connecting to remote servers so apps can detect whether the network is available and what type of connection is present.
- The page lists app responses for unavailable networks, 3G connections, and server connectivity checks before requests are sent.
- Web services can be accessed through hand-crafted requests and parsing, or through libraries such as RestSharp and ServiceStack.
- RestSharp is presented as a .NET REST client library with simple request and response parsing.
- ServiceStack is described as both a server-side web service solution and a client library for mobile apps.
- Xamarin tools can consume WCF services, especially the client subset that matches Silverlight runtime support, but WCF support is considered in preview.
- Threading is presented as necessary for responsiveness so the UI thread is not blocked by long-running work.
- The Parallel Task Library is shown as a way to run asynchronous tasks and return to the calling thread.
- TaskScheduler.FromCurrentSynchronizationContext() is used to marshal callbacks back to the UI thread.
- For code that does not use the task library, platform-specific UI thread calls are listed for iOS, Android, and Windows.
- The shared-code example defines an IDispatchOnUIThread interface and platform-specific DispatchAdapter implementations.
- The final section points to platform capability documentation for graceful degradation when an app cannot use all device features.
