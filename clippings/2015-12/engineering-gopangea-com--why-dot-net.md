---
url: "http://engineering.gopangea.com/2015/12/10/why-dot-net.html"
captured_at: "2015-12-23T14:49:36-03:00"
title: "Why .NET?"
domain: "engineering-gopangea-com"
---

# Why .NET?

Dec 10, 2015
by
[Omar Khudeira](http://engineering.gopangea.com/2015/12/10/why-dot-net.html#author)

We get asked “Why .NET?” a lot. It’s rare to find .NET startups these days and for good reason. Historically speaking, the .NET ecosystem was unattractive due to the high licensing cost of Windows and Visual Studio. In addition, .NET had poor interoperability with non-Microsoft products, which meant additional licensing costs for compatible products (like SQL Server). Lastly, Microsoft’s [aggressive anti-competitive stance](https://en.wikipedia.org/wiki/Embrace,_extend_and_extinguish) towards its competitors and open source software created a rift between their products and developers.

However, as technologies like Ruby on Rails, Django, and Node gained popularity and took market share from Microsoft, the business case was made and Microsoft had to change. As a company Microsoft is drastically different than it was ten years ago and the current .NET landscape is a clear indicator of that change.

Ten years ago you couldn’t download a [free and open source version of Visual Studio](https://code.visualstudio.com/) on your Mac, clone the [.NET git repository](https://github.com/dotnet/corefx), modify the source code, build a web app using the modified code, then deploy to a [Linux VM managed by Microsoft](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-tutorial/). Today you can.

Given that, let’s assume we’re starting a greenfield project today and we’re tasked with selecting a stack. Our ideal stack would need to:

1. Be *open source* to use the source when documentation is not enough.
2. Be *statically typed* to take advantage of static code analysis tools.
3. Be *mature yet modern* for stability and ease of use.
4. Have a *rich ecosystem* to allow the use of 3rd party software.
5. Have a *strong steward* to ensure the stack is maintained properly for at least ten years.

Based on that criteria, we have a few contenders:

- Microsoft’s `.NET` and `C#`.
- Oracle’s `Java`.
- Google’s `Go`.

While Go’s steward is a tech heartthrob, it’s [notorious](https://googleblog.blogspot.com/2011/09/fall-spring-clean.html) for [regularly](http://google-opensource.blogspot.com/2015/03/farewell-to-google-code.html) [sunsetting](https://googleblog.blogspot.com/2012/09/more-spring-cleaning.html) a [number](https://googleblog.blogspot.com/2012/12/winter-cleaning.html) of [its](https://googleblog.blogspot.com/2012/04/spring-cleaning-in-spring.html) [products](https://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html) and making [radical](http://angularjs.blogspot.com.es/2014/10/ng-europe-angular-13-and-beyond.html) [shifts](http://news.dartlang.org/2015/03/dart-for-entire-web.html) for its developer tooling. As a language, Go is rich but nascent with only [six years](https://blog.golang.org/6years) of development behind it as of November 2015 compared to C#’s fifteen and Java’s twenty. And while the Go ecosystem is bustling, it’s not as mature as .NET or Java.

On the other hand, Java’s ecosystem helped solidify the position of object-oriented programming in the software world. However, given Oracle’s poor stewardship of other technologies it adopted from the [Sun Microsystems acquisition](https://en.wikipedia.org/wiki/Sun_acquisition_by_Oracle) (namely [MySQL](https://en.wikipedia.org/wiki/Sun_acquisition_by_Oracle#MySQL_petition_and_forks) and [Hudson](https://en.wikipedia.org/wiki/Sun_acquisition_by_Oracle#Hudson.2FJenkins_fork)), Java’s future is worrying. In addition, although Java pioneered many language features, its slow release cycles has caused it to show its age relative to other languages.

Despite the fact that .NET and C# were created after Java, features like LINQ, nullable primitives, true generics, generators, and async/await make them a step ahead of where Java, Go, Python, and JavaScript/ECMAScript are headed. In addition, the recent push by Microsoft to [open source and support .NET cross platform](http://dotnet.github.io/) means .NET’s best days are ahead of it.

Although we built Pangea’s platform using .NET, **we are not a Microsoft shop**. We’re a technology shop and that means our tech stack is quite diverse. We use MySQL, Redis, RabbitMQ, git, TeamCity, EC2, S3, and Chef. You can see more details about our stack at [engineering.gopangea.com/stack](http://engineering.gopangea.com/stack).

When selecting a core development stack, you bet on two key things: the steward and the ecosystem. If both are sound, the future is bright for the stack. We bet on .NET and C# nearly three years ago based on [positive signals we saw](http://weblogs.asp.net/scottgu/asp-net-mvc-web-api-razor-and-open-source) during the development of ASP.NET MVC. Today that bet is paying off, but the pendulum is always swinging and no bet is correct forever. .NET meets our criteria *today* but no one knows *for certain* what the landscape will look like tomorrow. For that reason, we’ll always have a living [tech stack roadmap](http://engineering.gopangea.com/stack#roadmap).

Discuss at [Hacker News](https://news.ycombinator.com/item?id=10719534), [/r/programming](https://www.reddit.com/r/programming/comments/3w8ujm/why_net/), [/r/dotnet](https://www.reddit.com/r/dotnet/comments/3w8wrc/why_net/), and [/r/csharp](https://www.reddit.com/r/csharp/comments/3wammg/why_net/).

### Author

![689fa26019e243e4f4d84c138e418ea4.jpg](engineering-gopangea-com--why-dot-net/ccfd1fb25041ff65ac2f9f78ace3479c.jpg)
Omar Khudeira
-

Omar is currently the head of engineering at Pangea and the editor-in-chief of the engineering blog. Prior to leading the engineering team, Omar built the initial version of the platform that powers Pangea's global reach.

### Contributor

Carlos Rocha
-

Carlos is Pangea's resident JavaScript guru responsible for Pangea's web application. Upon joining Pangea, Carlos migrated the web application from AngularJS to React.
