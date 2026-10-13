---
title: "What to Use on the Microsoft Stack"
date: '2013-11-18T18:02:45-03:00'
category: webclip
summary: 'The guide maps Microsoft’s preferred technologies by scenario, steering developers away from Silverlight, Web Forms, and client-server designs toward native apps, MVC, Web API, WCF, SignalR, and layered architectures.'
tags: ["microsoft-stack", "asp.net-mvc", "web-api", "silverlight"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What to Use on the Microsoft Stack"
    url: "http://www.infoq.com/articles/Microsoft-Stack-2013"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/infoq-com--what-to-use-on-the-microsoft-stack.md"
    kind: repo
---

Microsoft’s guidance is organized by application type and business size. It favors native technologies for high-end apps, HTML5 for lower-end browser apps, and different choices for mobile, services, desktop, and modernization depending on performance, reuse, and team familiarity. Silverlight and Flash are treated as technologies to leave behind, while Web API, WCF, SignalR, WPF, WinForms, and C++ remain viable in different roles.

## Reading notes

- The article points readers to the .NET Technology Guide for Business Applications as a way to see where Microsoft intends to invest and what to avoid.
- Silverlight and Flash are presented as technologies Microsoft wants developers to move away from, with RIA containers expected to fade out by the end of 2015.
- For Windows 8 Store apps, .NET/XAML, C++, and JavaScript/HTML5 are described as equal options, with the main criterion being what the developer knows best.
- On Windows Phone, Microsoft recommends .NET and C++, and performance is treated as the main concern.
- For mobile web, ASP.NET MVC with Modernizr is the baseline recommendation, with ASP.NET SPA, Knockout, and Breeze as options.
- LightSwitch is presented as a fast way to build CRUD-style applications, but with limited control over HTML rendering.
- Web Forms is not recommended for mobile web because the generated HTML and JavaScript can be inefficient and view state can burden phone networks.
- For services, ASP.NET Web API is the default choice for new projects, especially for REST patterns, OData, and JSON.
- WCF is the more flexible service option when transport and message format matter, but it is harder to work with for JSON and non-SOAP formats.
- WCF Data Services is the suggested WCF-based option for CRUD-style service layers using OData.
- Workflow Services are recommended only when Windows Workflow is already part of the system.
- SignalR is presented as a good option for two-way communication across .NET and web clients, with WebSockets preferred when available.
- LightSwitch is also described as another way to expose OData-based services, though with less flexibility.
- For small and medium business applications, Microsoft’s goals are speed, lower cost, easier adoption, collaboration, and cloud savings.
- In that space, LightSwitch, Web Forms, and ASP.NET MVC are all mentioned, with MVC preferred when more control is needed.
- For desktop apps, WinForms and WPF are both viable, while WPF brings more flexibility and better-looking UI at the cost of greater complexity and slower runtime.
- If the goal is to target Windows Phone or Windows 8 Store as well, starting with WPF is presented as a way to make code sharing easier through XAML.
- Client-server designs that connect directly to the database are discouraged in favor of a service layer between client and database.
- Microsoft recommends modernizing desktop apps with MVVM, portable class libraries, updated UI, server-side business logic, and cloud extensions.
- Xamarin, iFactr, MonoCross, Mobilize.NET, and Citrix Mobile SDK are listed as partner options for extending .NET applications to iOS and Android.
- For large, mission critical applications, the focus shifts to complexity management and quality of service instead of cost and speed.
- In that setting, ASP.NET MVC is the web recommendation, while Web Forms and Web Pages are rejected for lacking control and testability.
- For enterprise desktops, WPF, WinForms, and C++ with Win32 or MFC are included, with C++ aimed at very large long-term projects.
- The patterns section emphasizes dependency injection, inversion of control, bounded contexts, asynchronous messaging, anti-corruption layers, and facades for legacy code.
- The conclusion says Microsoft is backing native, web, and communication frameworks for .NET except browser Silverlight and .NET Remoting, while also encouraging migration away from older platforms such as VB 6 and classic ASP.
