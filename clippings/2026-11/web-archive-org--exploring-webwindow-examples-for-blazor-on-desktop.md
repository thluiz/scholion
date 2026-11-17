---
url: "https://web.archive.org/web/20200316004858id_/https://gunnarpeipman.com/blazor-on-desktop-webwindow-experiment/"
captured_at: "2026-11-16T15:49:13+00:00"
title: "Exploring WebWindow examples for Blazor on desktop"
domain: "web-archive-org"
---

Blazor on desktop is one of latest hot topics and [.NET Conf: Focus on Blazor](https://gunnarpeipman.com/focus-on-blazor-announcements/ "Announcements from .NET Conf: Focus on Blazor") only added more fuel to fire. Blazor seems to come everywhere and it’s unstoppable. One of interesting desktop experiments is WebWindow by Steve Sanderson. It’s cross-platform component to make Blazor WebAssembly applications run on desktop. Let’s take a closer look at WebWindow and Blazor on desktop.

> **Warning!** [WebWindow](https://github.com/SteveSandersonMS/WebWindow "WebWindow @ GitHub") is experimental project by [Steve Sanderson](https://blog.stevensanderson.com/ "Steve Sanderson's Blog") – one of masterminds behind Blazor. There are no ready-made stable packages or components, no beautiful templates and other luxury like this. Get ready to make hands really dirty with raw bits and bytes!

### Why Blazor on desktop?

Blazor WebAssembly needs only rendering engine with WebAssembly support to run and most of modern browsers support WebAssembly. There Blazor applications doesn’t necessarily need web server to run. Web server is just one option to deliver Blazor application so browser can download and run it.

If web server is not necessary then there’s question to ask: can we somehow remove web server from equation and make those Blazor WebAssembly apps look and feel more like desktop application? Blazor on desktop is here to address this question with high chances to answer “yes”.

### What is WebWindow?

WebWindow is .NET Core library that makes it possible to run HTML, JavaScript and WebAssembly applications in local browser window. It uses some existing browser or web renderer library to create a window where web application is loaded and run.

WebWindow is cross-platfrom library. Current experimental implementation of WebWindow works on following platforms:

*   **Windows** – needs Chromium-based Edge
*   **Linux** – uses WebKit
*   **Mac** – needs Safari

Here’s how we start Blazor on desktop on all three platforms.

using WebWindows.Blazor;

namespace BlazorDesktopApp  
{
    public class Program
    {
        static void Main(string\[\] args)
        {
            ComponentsDesktop.Run<Startup\>("My Blazor App", "wwwroot/index.html");
        }
    }
}  

WebWindow is made available on same desktop platforms where .NET Core runs.

### Downloading and running WebWindow examples

Experimental WebWindow code lives in GitHub repository [SteveSandersonMS/WebWindow](https://github.com/SteveSandersonMS/WebWindow "SteveSandersonMS/WebWindow").

*   Clone or download [latest WebWindows version](https://github.com/SteveSandersonMS/WebWindow "Download latest WebWindow version") from master branch
*   Run Visual Studio 2019 and update it to latest version
*   Open WebWindow.Samples.sln file in Visual Studio

There are three projects in samples solution:

*   **HelloWorldApp** – simple Hello, World! demonstrating basics of WebWindow
*   **VuewFileExplorer** – sample of JavaScript based local file browser
*   **BlazorDesktopApp** – running Blazor WebAssembly app on desktop

Let’s see what’s inside those sample applications.

### Hello WebView

First project to explore is Hello, world! It is not about Blazor but WebWindow component that hosts HTML and Blazor applications. This is console application that creates new WebWindow and shows local index.html file.

using WebWindows;

namespace HelloWorldApp
{
     class Program
     {
         static void Main(string\[\] args)
         {
             var window = new WebWindow("My first WebWindow app");
             window.NavigateToLocalFile("wwwroot/index.html");
             window.WaitForExit();
         }
     }
}  

WaitForExit() method of WebWindow stops execution of Main() method until windows is closed.

When we run application then it opens in local web view window. The following screenshot shows Hello, World application running on Windows 10.

![Hello, World WebWindow application](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/blazor-webwindow-hello-world.png "Hello, World WebWindow application")

With this example our first step is made.

### Browsing file system of host machine

Next WebWindow example is in project called VueFileExplorer. It makes step further with WebWindow and introduces communication between user interface shown in web view and .NET Core process hosting it. WebWindow defines OnWebMessageReceived event handler and SendMessage command. These two members of WebWindow class enable two-way communication between web view and hosting process.

VueFileExplorer uses Vue.js to build two-pane window to explore file system. Left pane is for files and folders, right pane is for file content like shown on the following screenshot.

![Vue file explorer](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/webwindow-vue-file-explorer.png "Vue file explorer")

When file or folder is clicked then JavaScript sends message to window. This is the Vue app serving user interface and communicating with host application.

var app = new Vue({
     el: '#app',
     data: {
         directoryInfo: null,
         fileInfo: null
     },
     methods: {
         navigateTo: function (relativePath, event) {
             event.preventDefault();
             window.external.sendMessage(JSON.stringify({
                 command: 'navigateTo',
                 basePath: app.directoryInfo.name,
                 relativePath: relativePath
             }));
         },
         showFile: function (fullName, event) {
             event.preventDefault();
             window.external.sendMessage(JSON.stringify({
                 command: 'showFile',
                 fullName: fullName
             }))
;         }
     }
});

window.external.receiveMessage(function (messageJson) {
     var message = JSON.parse(messageJson);
     switch (message.command) {
         case 'showDirectory':
             app.directoryInfo = message.arg;
             break;
         case 'showFile':
             app.fileInfo = message.arg;
             break;
     }
});

window.external.sendMessage(JSON.stringify({ command: 'ready' }));
  

Here’s the fragment of code from Program class demonstrating how WebWindow messages are listened and processed.

static void Main(string\[\] args)
{
     var window = new WebWindow(".NET Core + Vue.js file explorer");
     window.OnWebMessageReceived += HandleWebMessageReceived;
     window.NavigateToLocalFile("wwwroot/index.html");
     window.WaitForExit();
}

static void HandleWebMessageReceived(object sender, string message)
{
     var window = (WebWindow)sender;
     var parsedMessage = JsonDocument.Parse(message).RootElement;
     switch (parsedMessage.GetProperty("command").GetString())
     {
         case "ready":
             ShowDirectoryInfo(window, Directory.GetCurrentDirectory());
             break;
         case "navigateTo":
             var basePath = parsedMessage.GetProperty("basePath").GetString();
             var relativePath = parsedMessage.GetProperty("relativePath").GetString();
             var destinationPath = Path.GetFullPath(Path.Combine(basePath, relativePath))
                                         .TrimEnd(Path.DirectorySeparatorChar);
             ShowDirectoryInfo(window, destinationPath);
             break;
         case "showFile":
             var fullName = parsedMessage.GetProperty("fullName").GetString();
             ShowFileContents(window, fullName);
             break;
     }
}  

Based on message sent from web view the response is built and sent to web view as message. Here’s how showing of file contents is implemented.

private static void ShowFileContents(WebWindow window, string fullName)
{
     var fileInfo = new FileInfo(fullName);
     SendCommand(window, "showFile", null); // Clear the old display first
     SendCommand(window, "showFile", new
     {
         name = fileInfo.Name,
         size = fileInfo.Length,
         fullName = fileInfo.FullName,
         text = ReadTextFile(fullName, maxChars: 100000),
     });
}  

SendCommand is simple static method that sends prepared command to web view.

static void SendCommand(WebWindow window, string commandName, object arg)
{
     window.SendMessage(JsonSerializer.Serialize(new { command = commandName, arg = arg }));
}  

As we can see then we can use WebWindow to host JavaScript application and make it use host system through messaging.

### Blazor desktop application

The pearl of WebWindow example applications is the one that hosts Blazor WebAssembly. The example uses default Blazor WebAssembly application with famous Counter and Fetch data views. Here is the example of weather forecasts we have seen in numerous Blazor demos. Now it is running on your desktop instead of web server.

![blazor-desktop-application](https://static.gunnarpeipman.com/wp-content/uploads/2020/01/blazor-desktop-application.png "blazor-desktop-application")

Where comes the data to weather forecast view if Blazor application is hosted in web window and there’s no web server running? It’s coming straight from disk. Here’s the FetchData page from Blazor desktop application project.

@page "/fetchdata"
@using System.IO
@using System.Text.Json

<h1\>Weather forecast</h1\>

<p\>This component demonstrates fetching data from the server.</p\>

@if (forecasts == null)
{
     <p\><em\>Loading...</em\></p\>
}
else
{
     <table class\="table"\>
         <thead\>
             <tr\>
                 <th\>Date</th\>
                 <th\>Temp. (C)</th\>
                 <th\>Temp. (F)</th\>
                 <th\>Summary</th\>
             </tr\>
         </thead\>
         <tbody\>
             @foreach (var forecast in forecasts)
             {
                 <tr\>
                     <td\>@forecast.Date.ToShortDateString()</td\>
                     <td\>@forecast.TemperatureC</td\>
                     <td\>@forecast.TemperatureF</td\>
                     <td\>@forecast.Summary</td\>
                 </tr\>
             }
         </tbody\>
     </table\>
}

@code {
     WeatherForecast\[\] forecasts;
     protected override async Task OnInitializedAsync()
     {
         var forecastsJson = await File.ReadAllTextAsync("wwwroot/sample-data/weather.json");
         forecasts = JsonSerializer.Deserialize<WeatherForecast\[\]>(forecastsJson, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
     }
     public class WeatherForecast
     {
         public DateTime Date { get; set; }
         public int TemperatureC { get; set; }
         public string Summary { get; set; }
         public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);     }
}  

Instead of using HttpClient like examples of server hosted Blazor do, here they are accessing file system to load and deserialize weather forecast data.

In all other means it is the same Blazor application we get when we create new Blazor application. But this time it runs on desktop.

### Wrapping up

Blazor WebApplication (formerly known as [client-side Blazor](https://gunnarpeipman.com/blazor-preview/ "WebAssembly apps with Blazor")) is going through revolutionary times. There are many things happening around it and making Blazor run on desktop is perhaps the most interesting part. Although WebWindow is in early experimental stages and it’s not even clear if this approach will stay here long enough to get to stable version, it is still very promising. WebWindow and desktop support are in my opinion important part of Blazor-everywhere vision.

[![Serverless360 Logo](https://www.serverless360.com/wp-content/uploads/2020/02/sl360-logo-guest-blog.png)](https://www.serverless360.com/?utm_source=gunnar-peipman-blog&utm_medium=blog-bottom-cta)

## A portal focused on Operations and Support for Microsoft Azure Serverless services

[FREE TRIAL](https://portal.serverless360.com/OnBoarding/Register/?utm_source=gunnar-peipman-blog&utm_medium=blog-bottom-cta)
