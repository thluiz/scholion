---
title: "Understanding how to port your ASP.NET web apps to ASP.NET Core"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'The post explains when moving to ASP.NET Core makes sense and reviews three migration areas: EF6 to EF Core, .NET to .NET Core, and ASP.NET to ASP.NET Core, with several compatibility changes to check first.'
tags: ["asp-net-core", "migration", "entity-framework", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Understanding how to port your ASP.NET web apps to ASP.NET Core"
    url: "https://devblogs.microsoft.com/premier-developer/understanding-how-to-port-your-asp-net-web-apps-to-asp-net-core"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--understanding-how-to-port-asp-net-web-apps-to-asp-net-core.md"
    kind: repo
---

The post says the move to ASP.NET Core is driven by needs like cross-platform support, microservices, Docker, performance, scalability, and side-by-side .NET versions. It treats the change as a porting effort that requires reviewing the data layer, the controller or business layer, and the view or UI layer.

## Reading notes

- For new apps, EF Core is recommended when the app needs .NET Core capabilities and EF Core supports the required features.
- EF6 is the better fit when the app runs on Windows and .NET Framework 4.0 or later and EF6 covers the needed features.
- Existing EF6 apps can move to EF Core, and the post says the main reason is that EF Core is significantly more performant than EF6.
- EF Core can run with legacy .NET Framework apps, so the app itself does not need to be Core to use EF Core.
- EF Core and EF6 can be used in the same application or library if both NuGet packages are installed, though matching type names can create ambiguity.
- For server apps, .NET Core is preferred for cross-platform needs, microservices, Docker containers, high performance, scalability, and side-by-side versions.
- .NET Framework is recommended when the app already uses it, depends on third-party libraries or NuGet packages not available for .NET Core, or relies on technologies or platforms not supported by .NET Core.
- ASP.NET Core projects can target .NET Core, .NET Framework, or both, and the .csproj format is simplified.
- Global.asax is no longer used; Program.cs Main and Startup handle application and MVC setup.
- Configuration is loaded from files such as appsettings.json during startup, and ASP.NET Core has native dependency injection.
- Static files live under wwwroot unless configured otherwise, and they are added to the request pipeline with UseStaticFiles.
- Multi-value cookies are not supported, so one cookie per value is required.
- Partial app migration is supported through an IIS sub-application that moves selected routes while keeping the URL structure.
- web.config is replaced in ASP.NET Core, although XML can still be used for configuration and appsettings.json is common.
- Authentication and identity are configured in Startup, and ApplicationDbContext and ApplicationUser must be added manually as class files.
- ClaimsPrincipal.Current is no longer set, so code using it must be updated.
- ASP.NET Membership databases must be migrated to the ASP.NET Core Identity schema.
- HTTP modules and handlers from system.webserver must be moved to middleware, and middleware is configured in code rather than Web.config.
- Pipeline branching can route requests based on URL, headers, and query strings.
- The post closes by saying the migration is doable but requires heavy lifting, and it is worth it for cloud hosting, Azure WebApps, containers, or Linux hosts.
