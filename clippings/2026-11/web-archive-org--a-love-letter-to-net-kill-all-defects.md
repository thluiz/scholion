---
url: "https://web.archive.org/web/20191115212844id_/https://killalldefects.com/2019/09/23/a-love-letter-to-net/"
captured_at: "2026-11-16T07:56:49+00:00"
title: "A Love Letter to .NET - Kill All Defects"
domain: "web-archive-org"
---

With Microsoft’s [official release of .NET Core 3](https://devblogs.microsoft.com/dotnet/announcing-net-core-3-0/) today, I want to give you my perspective on .NET and tell you how the platform continues to innovate solutions to modern problems.

I’ve been using .NET since beta 2 of the framework back in 2001 and have seen a **lot** of change over the years. Sure, I’ve diversified into JavaScript and TypeScript development among others, but I keep coming back to .NET.

Let me tell you why.

### A Brief History Lesson

When Microsoft introduced .NET, they decided that they weren’t building a single language, but a managed framework that different languages would compile down to run in. This made sense given that one of the primary goals of .NET was to address “DLL hell” and simplify managed code interoperability by giving people a smarter alternative to [COM](https://en.wikipedia.org/wiki/Component_Object_Model) development.

This meant that you could code in VB .NET if you were used to Visual Basic or try the new C# programming language if you were more a fan of C++ or Java style syntax. This also gave Microsoft room to introduce new languages down the line such as [F#](https://fsharp.org/).

.NET was a huge success in terms of addressing the woes of COM and improving developer productivity and application quality.

But today’s world is vastly different than it was back in the early 2000’s.

### .NET in Today’s World

With .NET _starting_ as a productivity solution to Windows desktop and web development, it’s interesting how it has since radically embraced cross-platform and cloud development. Microsoft realizes that people want to run servers in things like Docker containers and on platforms other than Windows. This is not a grudging acknowledgement on their part, but a true open-arms embrace and sprint into the cross-platform open-source world.

The world has changed and cloud services are the norm. Microsoft technologies work extremely well in a wide variety of cloud hosting environments, with more capabilities coming every release. Sure Microsoft would love for you to use Azure, but it’s still awesome if your team prefers AWS.

### Front-End Solutions

Front-end technologies have changed more than perhaps anything else. This is evident in Microsoft’s stack just by looking at Windows Forms, WPF, XBAPs, Silverlight, Windows Phone, Windows Universal, ASP .NET WebForms, MVC, and now Blazor.

At the beginning of .NET, JavaScript was this little thing to validate a shopping cart before you clicked submit. Now, JavaScript is a major part of the technology stack and a key part of the user experience. Microsoft contributed some to this boom via giving us TypeScript to help bring compile-time type safety to JavaScript.

Microsoft has also released [VS Code](https://code.visualstudio.com/) an extremely capable — and free — cross-platform IDE that is fantastic for JavaScript development. Visual Studio also now runs on Mac, while we’re on the topic of cross-platform development.

Microsoft continues to innovate with [Blazor](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor) where they are taking compiled languages and generating Web Assembly to allow developers to write web applications in languages other than JavaScript. This is still an emerging technology and in its early stages, but the continued dedication and promise are there.

### What do I Love?

So, now that we’ve covered what the framework is and how it has changed, why do I personally love it?

It’s not right for every project, but for me .NET is fantastic for back-end code and desktop / mobile development. Sure the web aspects are great, but I personally gravitate more towards Angular and JavaScript / TypeScript SPAs for web presentation — paired with an extremely capable .NET back-end API solution.

C# gives you some very strong syntax for dealing with object-oriented problems.

.NET gives you a wide variety of built in libraries for solving known problems. On top of that, there are a multitude of libraries freely available via [NuGet](https://www.nuget.org/) to integrate other technologies into your application in less than a minute.

If you’re more functionally-minded, F# offers the capabilities of the .NET Framework mixed with functional programming. On top of that, F# code can talk to C# or VB .NET code — and vice versa — allowing you to mix functional and object-oriented code.

As far as actual language features, I’m particularly in love with .NET’s generics, extension methods, lambda expressions, and LINQ. EntityFramework makes database flexibility significantly easier and productive.

.NET Core web applications are very minimal in their boilerplate code, letting you focus on what matters and easily integrating various middleware components into your application.

### Conclusion

I’ve written before about [how .NET is like the Borg](https://dev.to/integerman/we-are-the-borg-2o1g) — slowly acquiring new features and capabilities. This remains relevant and is an incredibly strong reason for the framework — it adapts to new situations and offers new capabilities as the world changes.

I’m reminded of [a joke thread comparing various programming languages to boats](http://compsci.ca/blog/if-a-programming-language-was-a-boat/) from back in 2008. In the comments, a user named RJ said this of .NET:

> _.Net is undoubtedly a flotilla of mid-size ships in various states of dis-repair, with no one boat leading the others. At random intervals new boats, partially complete, will be added to the flotilla — but as these ships do the same as some of the other ships — nobody will bother to finish them. Sometimes, some of these ships sink never to be seen again, but nobody really notices._

RJ wasn’t too far off. Sure we’ve lost some ships, but .NET is now a glorious armada capable of taking on whatever seas the ocean has to offer.

* * *

If you’re considering learning .NET, give it a try. It’s a lot to take in, but you’ll be rewarded. I recommend you start somewhere small, like a console app or [building a .NET Core Web API](https://dev.to/integerman/creating-a-net-core-api-3n6d).

Reach out to the community if you get stuck. The .NET community is professional, courteous, and incredibly innovative and I am proud to be part of it.

.NET is not for every team or every problem, but it’s amazing to be a part of, and I do not regret investing my time in this technology over the years.
