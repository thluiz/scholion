---
url: "https://web.archive.org/web/20200305134438id_/https://gunnarpeipman.com/blazor-hybrid-application-experimental/"
captured_at: "2026-11-16T15:49:49+00:00"
title: "Building experimental hybrid Blazor WebAssembly application"
domain: "web-archive-org"
---

After getting done with [Blazor desktop applications](https://gunnarpeipman.com/blazor-on-desktop-webwindow-experiment/ "Exploring WebWindow examples for Blazor on desktop") I tried to build kind of hybrid Blazor WebAssembly application that can run on desktop and in web equally. Although I failed to make it as one single application, I still got it work with a little different architecture. And what’s best – Blazor desktop applications run already now as self-contained executables. Here’s my experiment.

> **Warning!** [WebWindow](https://github.com/SteveSandersonMS/WebWindow "WebWindow project @ GitHub") is experimental technology by [Steve Sanderson](https://blog.stevensanderson.com/ "Steve Sanderon's blog") to host Blazor WebAssembly applications in desktop windows using local browser’s web view. Right now it’s not even sure if WebWindow makes its way to official codebase of Blazor. Play with it, but don’t go live with it yet.

### Architecture of shared Blazor WebAssembly application

What I tried to do was architecture like shown on the following screenshot.

![Diagram: Blazor WebAssembly project shared between desktop and web application](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/blazor-webassembly-app-as-shared-component.png "Diagram: Blazor WebAssembly project shared between desktop and web application")

Blazor WebAssembly application is implemented as a shared library that contains user interface artifacts like pages, layouts and code-behind files. Also it is possible to host shared interfaces in this project.

WebWindow and ASP.NET Core based web server projects are just for building application for target environment and configuring dependency injection to use implementations for given environment.

### Shared application solution

[![Blazor WebAssembly app as shared component library](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/blazor-webassembly-app-shared-visualstudio_thumb.png "Blazor WebAssembly app as shared component library")](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/blazor-webassembly-app-shared-visualstudio.png)After moving all user interface files to shared project and deleting these files from applications projects I finished up with projects like shown on screenshot. wwwroot folder is necessary as there are static files needed by application. Most important one is index.html as it is different for both applications.

Screenshot clearly shows how applications projects have only wwwroot folder (later more about it), Program and Startup classes and implementation of weather data service. Notice that I managed to move also App.razor to shared project. As application projects doesn’t have any user interface components then I got rid of \_Imports.razor files too.

**NB!** There’s one issue – static assets in shared library are not supported by Blazor on desktop. When publishing these applications we can copy static assets from wwwroot of shared project to desktop application publishing folder. It’s hack, yes, but don’t forget we are messing with pre-alpha and beta level tooling.

### Differences in applications

It’s important to see what’s the difference between desktop and web application. I tried first to make total hybrid application – one application running wherever you want, but it turned out to be task over my skills.

First and most important difference is in project file definition – applications use different project SDK.

<!-- Desktop application \-->  
<Project Sdk\="Microsoft.NET.Sdk.Razor"\>  
    
<!-- Web application \-->  
<Project Sdk\="Microsoft.NET.Sdk.Web"\>

Here are Program and Startup class of desktop application.

public class Program  
{  
    public static void Main(string\[\] args)  
    {  
        ComponentsDesktop.Run<Startup\>("My Blazor App", "wwwroot/index.html");  
    }  
}

 public class Startup  
{  
    public void ConfigureServices(IServiceCollection services)  
    {  
        services.AddSingleton<IWeatherService, LocalDiskWeatherService\>();  
    }

     public void Configure(IComponentsApplicationBuilder app)  
    {  
        app.AddComponent<App\>("app");  
    }  
}

Let’s compare these two with ones from web application project.

public class Program  
{  
    public static void Main(string\[\] args)  
    {  
        CreateHostBuilder(args).Build().Run();  
    }

     public static IWebAssemblyHostBuilder CreateHostBuilder(string\[\] args) =>  
        BlazorWebAssemblyHost.CreateDefaultBuilder()  
            .UseBlazorStartup<Startup\>();

     public class Startup  
    {  
        public void ConfigureServices(IServiceCollection services)  
        {  
            services.AddSingleton<IWeatherService, WebWeatherService\>();  
        }

         public void Configure(IComponentsApplicationBuilder app)  
        {  
            app.AddComponent<App\>("app");  
        }  
    }  
}

Desktop application uses ComponentDesktop class to initialize program while web application uses Blazor WebAssembly host builder. Startup classes are similar in big part, but ConfigureServices method is different – this is where dependency injection happens.

There are also small differences in index.html files. Let’s start with desktop application.

<!DOCTYPE html\>  
<html\>  
<head\>  
    <meta charset\="utf-8" />  
    <meta name\="viewport" content\="width=device-width" />  
    <title\>MyDesktopApp</title\>  
    <base href\="/" />  
    <link href\="css/bootstrap/bootstrap.min.css" rel\="stylesheet" />  
    <link href\="css/site.css" rel\="stylesheet" />  
</head\>  
<body\>  
    <app\>Loading...</app\>

     <script src\="framework://blazor.desktop.js"\></script\>  
</body\>  
</html\>

Here is index.html for Blazor web application. Notice how stylesheets are linked from \_content folder as Blazor web application supports static assets hosted in component projects. Also compare how Blazor application script is included. Blazor desktop application uses URL starting with framework:// while Blazor web application uses regular web server location.

<!DOCTYPE html\>  
<html\>

 <head\>  
    <meta charset\="utf-8" />  
    <meta name\="viewport" content\="width=device-width" />  
    <title\>BlazorDemoWeb</title\>  
    <base href\="/" />  
    <link href\="\_content/BlazorDemoShared/css/bootstrap/bootstrap.min.css" rel\="stylesheet" />  
    <link href\="\_content/BlazorDemoShared/css/site.css" rel\="stylesheet" />  
</head\>

 <body\>  
    <app\>Loading...</app\>

     <div id\="blazor-error-ui"\>  
        An unhandled error has occurred.  
        <a href\="" class\="reload"\>Reload</a\>  
        <a class\="dismiss"\></a\>  
    </div\>  
    <script src\="\_framework/blazor.webassembly.js"\></script\>  
</body\>

 </html\>

With these minor things differences end. Application and its user interface is living in shared project. In both cases application looks the same.

![Blazor desktop application showing weather data](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/blazor-desktop-application.png "Blazor desktop application showing weather data")

There’s one minor difference – desktop application runs inside operating system window and web application runs in browser.

### Blazor desktop application as self-contained executable

After getting things work I wanted to try out one final thing – what happens if I publish desktop application as [self-contained executable with assembly trimming](https://gunnarpeipman.com/dotnet-core-self-contained-executable/ "Self-contained executable with .NET Core 3.0 on Windows, Linux and Raspberry") enabled. Assembly trimming removed all code from resulting assembly that is not executed by application.

I opened Blazor desktop application folder in command prompt and executed the following command:

dotnet publish -c Release -r win10-x64 /p:PublishSingleFile=true /p:PublishTrimmed=true  

Instead of publish folder with many files I got something really small.

![Blazor desktop application as self-contained trimmed executable](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/blazor-desktop-self-contained.png "Blazor desktop application as self-contained trimmed executable")

Without assembly trimming executable will take ~70MB. Assembly trimming saved us roughly 50% in resulting assembly size.

> **No WebAssembly JavaScript files for desktop!** After publishing and running Blazor desktop application I had one question: where are those JavaScript files that make Blazor possible? I couldn’t find these from publish folder. Well, it seems like Blazor desktop apps are able to load WebAssembly application without need for separate JavaScript files. And framework:// protocol we saw before seems to make the trick. Cool!

### Wrapping up

Although not all things work like they should, I was still able to build kind of hybrid Blazor WebAssembly application. User interface is in shared component library and application projects are there to build and publish application for target environment or platform. Suprising moment was that assembly trimming works like charm with Blazor desktop applications and all I have to try out now is to buid a simple installer. Blazor WebWindow is in pre-alpha but already damn powerful toy to play with.

[![Serverless360 Logo](https://www.serverless360.com/wp-content/uploads/2020/02/sl360-logo-guest-blog.png)](https://www.serverless360.com/?utm_source=gunnar-peipman-blog&utm_medium=blog-bottom-cta)

## A portal focused on Operations and Support for Microsoft Azure Serverless services

[FREE TRIAL](https://portal.serverless360.com/OnBoarding/Register/?utm_source=gunnar-peipman-blog&utm_medium=blog-bottom-cta)
