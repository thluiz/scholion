---
url: "https://ocelot.readthedocs.io/en/latest/introduction/gotchas.html"
captured_at: "2026-09-25T18:31:49+01:00"
title: "Hosting Gotchas — Ocelot API Gateway v25.0 \".NET 10\" documentation"
domain: "ocelot-readthedocs-io"
---

Table of Contents

*   [IIS](#iis)
    
*   [Kestrel](#kestrel)
    

Many errors and incidents (gotchas) are related to web server hosting scenarios. Please review deployment and web hosting common user scenarios below depending on your web server.

## [IIS](#id11)[¶](#iis "Link to this heading")

> Repository Label: [![label IIS](https://ocelot.readthedocs.io/en/latest/_images/label-IIS-c5def5.svg)](https://github.com/ThreeMammals/Ocelot/labels/IIS)

We **do not** recommend to deploy Ocelot app to IIS environments, but if you do, keep in mind the gotchas below.

*   When using ASP.NET Core 2.2+ and you want to use In-Process hosting, replace `UseIISIntegration()` with `UseIIS()`, otherwise you will get startup errors.
    
*   Make sure you use Out-of-process hosting model instead of In-process one (see [Out-of-process hosting with IIS and ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/out-of-process-hosting)), otherwise you will get very slow responses (see [1657](https://github.com/ThreeMammals/Ocelot/issues/1657)).
    
*   Ensure all DNS servers of all downstream hosts are online and they function perfectly, otherwise you will get slow responses (see [1630](https://github.com/ThreeMammals/Ocelot/issues/1630)).
    

The community constanly reports [issues related to IIS](https://github.com/ThreeMammals/Ocelot/issues?q=is%3Aissue+IIS). If you have some troubles in IIS environment to host Ocelot app, first of all, read open/closed issues, and after that, search for [IIS-related objects](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20IIS&type=code) in the repository. Probably you will find a ready solution by Ocelot community members.

## [Kestrel](#id12)[¶](#kestrel "Link to this heading")

> Repository Label: [![label Kestrel](https://ocelot.readthedocs.io/en/latest/_images/label-Kestrel-c5def5.svg)](https://github.com/ThreeMammals/Ocelot/labels/Kestrel)

We **do** recommend to deploy Ocelot app to self-hosting environments, aka Kestrel vs Docker. We try to optimize Ocelot web app for Kestrel & Docker hosting scenarios, but keep in mind the following gotchas.

**1\. Upload and download large files** [\[1\]](#f1)

This is proxying the large content through the gateway: when you pump large (static) files using the gateway. We believe that your client apps should have direct integration to (static) files persistent storages and services: remote & destributed file systems, CDNs, static files & blob storages, etc. We **do not** recommend to pump large files (100Mb+ or even larger 1GB+) using gateway because of performance reasons: consuming memory and CPU, long delay times, producing network errors for downstream streaming, impact on other routes.

> The community constanly reports issues related to [large files](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22large+file%22&type=issues), `application/octet-stream` content type, [Chunked Encoding](https://ocelot.readthedocs.io/en/latest/introduction/notsupported.html#chunked-encoding), etc., see issues [749](https://github.com/ThreeMammals/Ocelot/issues/749), [1472](https://github.com/ThreeMammals/Ocelot/issues/1472).
> 
> If you still want to pump large files through an Ocelot gateway instance, use [23.0](https://github.com/ThreeMammals/Ocelot/releases/tag/23.0.0) version and higher.
> 
> In case of some errors, see the next point.

**2\. Maximum request body size**

ASP.NET `HttpRequest` behaves erroneously for application instances that do not have their Kestrel [MaxRequestBodySize](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.kestrel.core.kestrelserverlimits.maxrequestbodysize) option configured correctly and having pumped large files of unpredictable size which exceeds the limit.

As a quick fix, use this configuration recipe:

var builder \= WebApplication.CreateBuilder(args);
builder.WebHost.ConfigureKestrel((context, serverOptions) \=>
{
    int myVideoFileMaxSize \= 1\_073\_741\_824; // assume your file storage has max file size as 1 GB (1\_073\_741\_824)
    int totalSize \= myVideoFileMaxSize + 26\_258\_176; // and add some extra size
    serverOptions.Limits.MaxRequestBodySize \= totalSize; // 1\_100\_000\_000 thus 1 GB file should not exceed the limit
});

* * *
