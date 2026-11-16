---
url: "https://hanselman.com/blog/HostingYourOwnNuGetServerAndFeedForBuildArtifactsWithBaGet.aspx"
captured_at: "2026-11-16T02:21:02+00:00"
title: "Hosting your own NuGet Server and Feed for build artifacts with BaGet"
domain: "hanselman-com"
---

![BaGet is a great NuGet alternative](https://images.hanselman.com/blog/Windows-Live-Writer/3b81e72b42a1_7B70/50140219-d8409700-0258-11e9-94c9-dad24d2b48bb_d2353326-c7e1-4f48-8f6a-bedc11820428.png "BaGet is a great NuGet alternative")NuGet is the package management system underlying the .NET programming platform. Just like Ruby Gems or NPM Packages, you can bring in 3rd party packages or make your own. The public repository is hosted at [http://nuget.org](http://nuget.org/) **BUT the magic is that there's alternatives!** There are lots of alternative servers, as well as alterative clients like [Paket](https://fsprojects.github.io/Paket/index.html).

There's a whole ecosystem of NuGet servers. You can get filtered views, authenticated servers, special virus scanned repositories, your own custom servers where your CI/CD (Continuous Integration/Continuous Deployment) system can publish daily (hourly?) NuGet packages for other teams to consume.

Ideally in a team situation you'll have one team produce NuGet Packages and publish them to a private NuGet feed to be consumed by other teams.

Here's just a few cool NuGet servers or views on NuGet.org:

*   [FuGet.org](https://www.hanselman.com/blog/NuGetsFancyOlderSiblingFuGetGivesYouAWholeNewViewOfTheNETPackagingEcosystem.aspx)
    *   [FuGet](https://www.fuget.org/) is "pro nuget package browsing!" Creating by the amazing [Frank A. Krueger](https://github.com/praeclarum?WT.mc_id=-blog-scottha) - of whom I am an immense fan - FuGet offers a different view on the NuGet package library. NuGet is a repository of nearly 150,000 open source libraries and the NuGet Gallery does a decent job of letting one browse around. However, [https://github.com/praeclarum/FuGetGallery](https://github.com/praeclarum/FuGetGallery?WT.mc_id=-blog-scottha) is an alternative web UI with a lot more depth.
*   [Artifactory](https://www.jfrog.com/confluence/display/RTF/NuGet+Repositories)
    *   Artifactory is a, ahem, factory for build artifacts of all flavors, NuGet being just one of them. You can even make your own internal cache of NuGet.org. You can remove or block access to packages you don't want your devs to have.
*   [NuGet Gallery](https://github.com/NuGet/NuGetGallery?WT.mc_id=-blog-scottha)
    *   You can just run your OWN instance of the NuGet.org website! It's open source
*   [NuGet.Server](https://github.com/NuGet/NuGet.Server?WT.mc_id=-blog-scottha)
    *   NuGet.Server is an MVP (Minimum Viable Product) of a NuGet Server. It's small and super lightweight but it's VERY limited. [Consider using BaGet](https://loic-sharma.github.io/BaGet/tools/migrate/) (below) instead.
*   [GitHub Packages](https://github.com/features/packages?WT.mc_id=-blog-scottha)
    *   GitHub has a package repository with a small free tier, and it also scales up to Enterprise size if you want a "SaaS" offering (software as a service)
*   [Azure Artifacts](https://docs.microsoft.com/en-us/azure/devops/artifacts/get-started-nuget?view=azure-devops&WT.mc_id=-blog-scottha)
    *   Azure Artifacts can also provide a SaaS setup for your NuGet packages. Set it up and forget it. A simple place for your automated build to drop your build artifacts.
*   [MyGet](https://www.myget.org/)

*   MyGet can hold packages of all kinds, including NuGet.They are well known for their license compliance system, so you can make sure your devs and enterprise are only using the projects your org can support.\\

*   [Sleet](https://github.com/emgarten/sleet?WT.mc_id=-blog-scottha)

*   Sleet is a NuGet v3 static feed generator. It's a Nuget Server, that's totally STATIC. Just like a static site generator this means that you can make feeds and host them directly on Azure Storage or Amazon S3 with no compute required.

*   [LiGet](https://github.com/ai-traders/liget?WT.mc_id=-blog-scottha)
    *   A NuGet server with a Linux-first approach
*   [**BaGet**](https://loic-sharma.github.io/BaGet/) **(pronounced baguette)**
    *   This is one of my favorites. It's a new fresh NuGet server written entirely in ASP.NET Core 3.1. It's cross platform, open source, and runs in Azure, AWS, Google Cloud, behind IIS, or via Docker. Lovely!  It's also a great example of some thoughtfully architected code, good plugin model, nice separation of concerns, and a good test suite. If you are using NuGet.Server now, [move over to BaGet](https://loic-sharma.github.io/BaGet/tools/migrate/)!

Let's focus on BaGet for now! [Go give them some love/stars](https://github.com/loic-sharma/BaGet/?WT.mc_id=-blog-scottha) on GitHub!

### Setting up a cross platform personal NuGet Server with BaGet

BaGet is a lovely little server. So far it supports:

*   Cross-platform
*   [Dockerized](https://loic-sharma.github.io/BaGet/#running-baget-on-docker)
*   [Cloud ready](https://loic-sharma.github.io/BaGet/cloud/azure/)
*   [Supports read-through caching](https://loic-sharma.github.io/BaGet/configuration/#enabling-read-through-caching)
*   Can index the entirety of nuget.org. See [this documentation](https://loic-sharma.github.io/BaGet/tools/mirroring/)
*   Coming soon: Will supports private feeds

The most initially powerful feature in my opinion is the **Read-through caching.**

This lets you index packages from an upstream source. You can use [read-through caching](https://loic-sharma.github.io/BaGet/configuration/#enabling-read-through-caching) to:

1.  Speed up your builds if restores from [nuget.org](https://nuget.org/) are slow
2.  Enable package restores in offline scenarios

This can be great for folks on low bandwidth or remote scenarios. Put BaGet in front of your developers and effectively make a NuGet "edge CDN" that's private to you.

If you are familiar with Docker, you can [get a BaGet NuGet server up in minutes](https://loic-sharma.github.io/BaGet/quickstart/docker/). You can also use Azure or AWS or another cloud to store your artifacts in a scaleable way.

> **NOTE:** You'll notice that the docs for things like "[running BaGet on Azure](https://loic-sharma.github.io/BaGet/quickstart/azure/)" aren't complete. This is a great opportunity for YOU to help out and get involved in open source! Note that BaGet has a number of open issues on their GitHub \*and\* they've labeled some as "[Good First Issue](https://github.com/loic-sharma/BaGet/labels/good%20first%20issue?WT.mc_id=-blog-scottha)!"

If you want to try running BaGet without Docker, just

1.  Install [.NET Core SDK](https://www.microsoft.com/net/download?WT.mc_id=-blog-scottha)
2.  Download and extract [BaGet's latest release](https://github.com/loic-sharma/BaGet/releases?WT.mc_id=-blog-scottha)
3.  Start the service with `dotnet BaGet.dll`
4.  Browse `http://localhost:5000/` in your browser

That's it! All the details on Getting Started with [BaGet are on their GitHub](https://github.com/loic-sharma/BaGet?WT.mc_id=-blog-scottha). Go give them some love and stars.

#### About Scott

Scott Hanselman is a former professor, former Chief Architect in finance, now speaker, consultant, father, diabetic, and Microsoft employee. He is a failed stand-up comic, a cornrower, and a book author.

[![facebook](https://images.hanselman.com/main/icon-fb.png)](https://facebook.com/shanselman) [![bluesky](https://images.hanselman.com/main/icon-bluesky.png)](https://bsky.app/profile/scott.hanselman.com) [![subscribe](https://images.hanselman.com/main/icon-rss.png)](http://feeds.hanselman.com/ScottHanselman)  
[About](http://hanselman.com/about)   [Newsletter](http://www.hanselman.com/newsletter)

**Hosting By**  
[![Hosted on Linux using .NET in an Azure App Service](https://images.hanselman.com/main/azure-250x250.png)](https://azure.microsoft.com/free?WT.mc_id=-blog-scottha)
