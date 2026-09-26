---
url: "https://www.hanselman.com/blog/HowToReferenceANETCoreLibraryInWinFormsOrNETStandardExplained.aspx?utm_content=buffer58949&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer"
captured_at: "2026-09-27T00:37:42+01:00"
title: "How to reference a .NET Core library in WinForms - Or, .NET Standard Explained"
domain: "hanselman-com"
---

I got an interesting email today. The author said "I have a problem consuming a .net core class library in a winforms project and can't seem to find a solution." This was interesting for a few reasons. First, it's solvable, second, it's common, and third, it's a good opportunity to clear a few things up with a good example.

To start, I emailed back with "precision questioning." I needed to assert my assumptions and get a few very specific details to make sure this was, in fact, possible. I said. "What library are you trying to use? What versions of each side (core and winforms)? What VS version?"

The answer was "I am working with VS2017. The class library is on NETCoreApp 1.1 and the app is a Winforms project on .NET Framework 4.6.2."

Cool! Let's solve it.

### Referencing a .NET Core library from WinForms (running .NET Full Framework)

Before we parse this question. Let's level-set.

.NET is this big name. It's the name for the whole ecosystem, but it's overloaded in such a way that someone can say "I'm using .NET" and you only have a general idea of what that means. Are you using it on mobile? in docker? on windows?

Let's consider that ".NET" as a name is overloaded and note that there are a few "instances of .NET"

*   **.NET (full) Framework** - Ships with Windows. Runs ASP.NET, WPF, WinForms, and a TON of apps on Windows. Lots of businesses depend on it and have for a decade. Super powerful. Non-technical parent maybe downloads it if they want to run paint.net or a game.
*   **.NET Core** \- Small, fast, open source, and cross-platform. Runs not only on Windows but also Mac and a dozen flavors of Linux.
*   **Xamarin/Mono/Unity** - The .NET that makes it possible to write apps in C# or F# and run them on everything from an iPad to cheap Android phone to a Nintendo Switch.

All of these runtimes are .NET. If you learn C# or F# or VB, you're a .NET Programmer. If you do a little research and google around you can write code for Windows, Mac, Linux, Xbox, Playstation, Raspberry Pi, Android, iOS, and on and on. You can run apps on Azure, GCP, AWS - anywhere.

### What's .NET Standard?

.NET Standard isn't a runtime. It's not something you can install. It's not an "instance of .NET."  .NET Standard is an interface - a versioned list of APIs that you can call. Each newer version of .NET Standard adds more APIs but leaves older platforms/operating systems behind.

The runtimes then implement this standard. If someone comes out with a new .NET that runs on a device I've never heard of, BUT it "implements .NET Standard" then I just learned I can write code for it. I can even use my existing .NET Standard libraries. You can [see the full spread of .NET Standard versions to supported runtimes in this table](https://docs.microsoft.com/en-us/dotnet/standard/library?WT.mc_id=-blog-scottha).

Now, you _could_ target a runtime - a specific .NET - or you can be more flexible and target .NET Standard. Why lock yourself down to a single operating system or specific version of .NET? Why not target a list of APIs that are supported on a ton of platforms?

The person who emailed me wanted to "run a .NET Core Library on WinForms." Tease apart that statement. What they really want is to reuse code - a dll/library specifically.

When you make a new library in Visual Studio 2017 you get these choices. If you're making a brand new library that you might want to use in more than one place, you'll almost always want to choose .NET Standard.

**.NET Standard isn't a runtime or a platform. It's not an operating system choice. .NET Standard is a bunch of APIs.**

![Pick .NET Standard](https://images.hanselman.com/blog/Windows-Live-Writer/3c7e17883db5_13BF9/image_86f8c192-79ae-441b-ae74-5efe2bf1b449.png "Pick .NET Standard")

Next, check properties and decide what version of .NET Standard you need.

![What version of .NET Standard?](https://images.hanselman.com/blog/Windows-Live-Writer/3c7e17883db5_13BF9/image_99f59a58-2b99-433b-bd2b-97b813721667.png "What version of .NET Standard?")

The [.NET Core docs are really quite good, and the API browser is awesome](https://docs.microsoft.com/en-us/dotnet/?WT.mc_id=-blog-scottha). You can find them at [https://docs.microsoft.com/dotnet/](https://docs.microsoft.com/dotnet/?WT.mc_id=-blog-scottha "https://docs.microsoft.com/dotnet/") 

The API browser has all the .NET Standard APIs versioned. You can put the version in the URL if you like, or use this nice interface. [https://docs.microsoft.com/en-us/dotnet/api/?view=netstandard-2.0](https://docs.microsoft.com/en-us/dotnet/api/?view=netstandard-2.0&WT.mc_id=-blog-scottha "https://docs.microsoft.com/en-us/dotnet/api/?view=netstandard-2.0")

[![API Browser](https://images.hanselman.com/blog/Windows-Live-Writer/3c7e17883db5_13BF9/image_222e826f-2493-4db3-a7e0-f8cdd90e4951.png "API Browser")](https://docs.microsoft.com/en-us/dotnet/api/?view=netstandard-2.0&WT.mc_id=-blog-scottha)

You can check out [.NET Standard 1.6](https://docs.microsoft.com/en-us/dotnet/api/?view=netstandard-1.6&WT.mc_id=-blog-scottha), for example, and see all the namespaces and methods it supports. It works on Windows 10, .NET Framework 4.6.1 and more. If you need to make a library that works on Windows 8 or an older .NET Framework like 4.5, you'll need to choose a lower .NET Standard version. The [table of supported platforms is here](https://docs.microsoft.com/en-us/dotnet/standard/library?WT.mc_id=-blog-scottha).

[From the docs](<http://When choosing a .NET Standard version, you should consider this trade-off:>) - When choosing a .NET Standard version, you should consider this trade-off:

*   The higher the version, the more APIs are available to you.
*   The lower the version, the more platforms implement it.

In general, we recommend you to target the _lowest_ version of .NET Standard possible. The goal here is reuse. You can also check out the [Portability Analyzer](https://marketplace.visualstudio.com/items?itemName=ConnieYau.NETPortabilityAnalyzer&WT.mc_id=-blog-scottha) and run it on your existing libraries to see if the APIs you need are available.

![.NET Portability Analyzer](https://images.hanselman.com/blog/Windows-Live-Writer/3c7e17883db5_13BF9/image_0bd040e2-629d-4f05-a374-9e6ccca5ad0f.png ".NET Portability Analyzer")

**.NET Standard is what you target for your libraries, and the apps that USE your library target a platform.**

![Diagram showing .NET Framework, Core, and Mono sitting on top the base of .NET Standard](https://images.hanselman.com/blog/Windows-Live-Writer/3c7e17883db5_13BF9/image_0eea508e-28ff-4909-b5b3-bdd87c7ab954.png "Diagram showing .NET Framework, Core, and Mono sitting on top the base of .NET Standard")

I emailed them back briefly, "Try making the library netstandard instead."

They emailed back just a short email, "Yes! That did the trick!"

* * *

**Sponsor:** Big thanks to [Raygun](http://hnsl.mn/2sSJ8ip)! Don't rely on your users to report the problems they experience. Automatically detect, diagnose and understand the root cause of errors, crashes and performance issues in your web and mobile apps. [Learn more](http://hnsl.mn/2sSJ8ip).

#### About Scott

Scott Hanselman is a former professor, former Chief Architect in finance, now speaker, consultant, father, diabetic, and Microsoft employee. He is a failed stand-up comic, a cornrower, and a book author.

[![facebook](https://images.hanselman.com/main/icon-fb.png)](https://facebook.com/shanselman) [![bluesky](https://images.hanselman.com/main/icon-bluesky.png)](https://bsky.app/profile/scott.hanselman.com) [![subscribe](https://images.hanselman.com/main/icon-rss.png)](http://feeds.hanselman.com/ScottHanselman)  
[About](http://hanselman.com/about)   [Newsletter](http://www.hanselman.com/newsletter)

**Hosting By**  
[![Hosted on Linux using .NET in an Azure App Service](https://images.hanselman.com/main/azure-250x250.png)](https://azure.microsoft.com/free?WT.mc_id=-blog-scottha)
