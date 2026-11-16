---
url: "https://devblogs.microsoft.com/premier-developer/understanding-how-to-port-your-asp-net-web-apps-to-asp-net-core"
captured_at: "2026-11-16T02:29:25+00:00"
title: "Understanding how to port your ASP.NET web apps to ASP.NET Core"
domain: "devblogs-microsoft-com"
---

January 20th, 2020

0 reactions

![](https://devblogs.microsoft.com/premier-developer/wp-content/uploads/sites/31/2021/08/devsupport-96x96.jpg)

Cloud Solution Architects

In this post, App Dev Manager [Mike Finley](https://www.linkedin.com/in/finleymike/) explains the factors when migrating an ASP.NET Web App to ASP.NET Core.

* * *

There are several reasons that developers and architects may consider moving to ASP.NET Core. Here are a few of the primary design requirements that you may want to consider for an application being upgraded:

*   Cross-platform needs.
*   Targeting microservices.
*   Using Docker containers.
*   Require high-performance and scalable systems.
*   Require side-by-side .NET versions per application

There are 3 fundamental areas of review in the upgrade process when moving from ASP.NET to ASP.NET Core. (The following details relate to upgrading web applications using MVC and Entity Framework)

[![](https://devblogs.microsoft.com/premier-developer/wp-content/uploads/sites/31/2020/01/word-image-20.png)](https://devblogs.microsoft.com/premier-developer/wp-content/uploads/sites/31/2020/01/word-image-20.png)

## **Model/Data Layer – Entity Framework to EF Core Migration Strategy**

## Guidance for new applications

Consider using EF Core for a new application if both of the following conditions are true:

*   The app needs the capabilities of .NET Core. For more information, see Choosing between .NET Core and .NET Framework for server apps.
*   EF Core supports all of the features that the app requires. If a desired feature is missing, check the EF Core Roadmap to find out if there are plans to support it in the future.

Consider using EF6 if both of the following conditions are true:

*   The app will run on Windows and the .NET Framework 4.0 or later.
*   EF6 supports all of the features that the app requires.

## Guidance for existing EF6 applications

If you want to move to EF Core to use new features, make sure you’re aware of its limitations. However, EF Core works well with legacy .NET Framework apps. The app doesn’t need to be Core to run EF Core. There are many reasons to move to EF Core, but the primary one is that EF Core is **significantly** more performant that EF 6. For more information, see Porting from EF6 to EF Core. The move from EF6 to EF Core is straightforward and more a port than an upgrade.

## Missing features

Make sure that EF Core has all the features you need to use in your application. See the feature comparison table (reference below) for a detailed comparison of how the feature set in EF Core compares to EF6. If any required features are missing, ensure that you can compensate for the lack of these features before porting to EF Core

## Using EF Core and EF6 in the Same Application

It is possible to use EF Core and EF6 in the same application or library by installing both NuGet packages. Some types have the same names in EF Core and EF6 and differ only by namespace, which may complicate using both EF Core and EF6 in the same code file. The ambiguity can be easily removed using namespace alias directives.

## **Controller/Business Layer — .NET to .NET Core Migration Strategy**

Both .NET and .NET Core share many of the same components and you can share code across the two. However, there are fundamental differences between the two and your choice depends on what you want to accomplish.

## Use .NET Core for your server application when:

*   You have cross-platform needs.
*   You are targeting microservices.
*   You are using Docker containers.
*   You need high-performance and scalable systems.
*   You need side-by-side .NET versions per application.

## Use .NET Framework for your server application when:

*   Your app currently uses .NET Framework (recommendation is to extend instead of migrating).
*   Your app uses third-party .NET libraries or NuGet packages not available for .NET Core.
*   Your app uses .NET technologies that aren’t available for .NET Core.
*   Your app uses a platform that doesn’t support .NET Core. Windows, macOS, and Linux support .NET Core.

There are a few tools and processes that can be used to make the conversion from .NET to .NET Core for Controller or Business layer components go a bit smoother. For more details see references below.

[![](https://devblogs.microsoft.com/premier-developer/wp-content/uploads/sites/31/2020/01/word-image-21.png)](https://devblogs.microsoft.com/premier-developer/wp-content/uploads/sites/31/2020/01/word-image-21.png)

## View/UI — ASP.NET to ASP.NET Core Migration Strategy

Moving from ASP.NET to ASP.NET Core is more of a port than migration. Some of the notable changes within ASP.NET Core are as follows:

*   ASP.NET Core projects offer developers the flexibility of targeting .NET Core, .NET Framework, or both however targeting .NET Core allows you to eliminate numerous explicit package references thanks to the **ASP.NET Core metapackage feature**.
*   The .csproj file format has been simplified in ASP.NET Core.
*   **Global.asax is no longer used** in ASP.NET Core. It uses the Program.cs Main method (similar to console applications) and the startup function handles the MVC, HTTP and error configurations.
*   ASP.NET Core **stores configuration data** for the application in any file and loads them as part of middleware bootstrapping. The default file used in the project templates is appsettings.json.
*   **Dependency Injection is now native** in ASP.NET Core. Because Dependency Injection is part of ASP.NET Core, you can add your DI service in the Configure Services method of Startup.
*   In ASP.NET Core, **static files are stored in the “web root”** (<content root>/wwwroot), unless configured otherwise. The files are loaded into the request pipeline by invoking the UseStaticFiles extension method from Startup Configuration.
*   **Multi-value cookies aren’t supported** in ASP.NET Core. Create one cookie per value.
*   **Partial App migration is supported**. One approach to partial app migration is to create an IIS sub-application and only move certain routes from ASP.NET 4.x to ASP.NET Core while preserving the URL structure the app.
*   **The web.config file has also been replaced** in ASP.NET Core. Configuration itself can now be configured, as part of the application startup procedure described in Startup. Configuration can still utilize XML files, but typically ASP.NET Core projects will place configuration values in a JSON-formatted file, such as appsettings.json.
    *   ASP.NET Core offers a rich configuration sub-system that enables many different configuration options, including local user secrets, which are stored on a developer machine outside of the project structure (so that they are not checked into source control).
*   In ASP.NET Core MVC, **authentication and identity features are configured in Startup**. Unfortunately, there are two authentication types that we haven’t yet migrated from the ASP.NET MVC project: ApplicationDbContext and ApplicationUser. They must be manually added as class files.
*   In ASP.NET Core, the **ClaimsPrincipal.Current property is no longer set**. Code that was depending on it needs to be updated to get the current authenticated user’s identity through a different means.
*   It is necessary to **migrate the database schema for ASP.NET Membership-based apps to the database schema used for ASP.NET Core Identity**.
*   It is necessary to **migrate existing ASP.NET HTTP modules and handlers from system.webserver to ASP.NET Core middleware**. This is a major change so detailed review is necessary.
    *   Modules, handlers, Global.asax.cs, Web.config (except for IIS configuration) and the application life cycle are gone.
    *   The roles of both modules and handlers have been taken over by middleware.
    *   Middleware are configured using code rather than in Web.config.
    *   Pipeline branching lets you send requests to specific middleware, based on not only the URL but also on request headers, query strings, etc.

The process of migrating from ASP.NET to ASP.NET Core is doable but not without some heavy lifting and understanding the complexities of the differences in the new programming model. I do believe the change is worth the time if you are looking at moving to the cloud and want to use Azure WebApps, containers or LINUX OS as your host.

**More Information:**

[**Compare EF6 to EF Core**](https://docs.microsoft.com/en-us/ef/efcore-and-ef6/)

[**Overview of the porting process from .NET Framework to .NET Core**](https://docs.microsoft.com/en-us/dotnet/core/porting/)

[**Choosing between .NET Core and .NET Framework for server app**](https://docs.microsoft.com/en-us/dotnet/standard/choosing-core-framework-server)

[**Migrate from ASP.NET to ASP.NET Core**](https://docs.microsoft.com/en-us/aspnet/core/migration/proper-to-2x)

**Modern Applications – Premier Developer Support**

Let us help you get started with your Web Application Migration efforts.

## Author

![Developer Support](https://devblogs.microsoft.com/premier-developer/wp-content/uploads/sites/31/2021/08/devsupport-96x96.jpg)

Cloud Solution Architects

Microsoft Developer Support helps software developers rapidly build and deploy quality applications for Microsoft platforms.
