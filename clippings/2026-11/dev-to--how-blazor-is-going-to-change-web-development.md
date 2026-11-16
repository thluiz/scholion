---
url: "https://dev.to/pluralsight/how-blazor-is-going-to-change-web-development-14n4"
captured_at: "2026-11-16T19:20:45+00:00"
title: "How Blazor Is Going to Change Web Development"
domain: "dev-to"
---

A couple of weeks ago I wrote an article about [building and deploying a Blazor app without touching a Windows machine](https://www.jeremymorgan.com/blog/linux/blazor-in-linux/) and realized maybe I should take a step back and explain what Blazor is and why anyone would use it. It's still fairly new to most in the front end development world, but it's awesome and you should check it out.

### [](#so-what-is-it-exactly)So what is it, exactly?

Blazor is a framework from Microsoft that you can use to develop interactive client-side Web UIs with C#.

In their own words:

> Blazor lets you build interactive web UIs using C# instead of JavaScript. Blazor apps are composed of reusable web UI components implemented using C#, HTML, and CSS. Both client and server code is written in C#, allowing you to share code and libraries.

Pretty cool right? You can **[download it here](http://bit.ly/GetBlazor)** and get started. 

### [](#the-old-way)The old way

Remember the old way of developing web applications? 

[![What is Blazor](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F9j97zjox5oszmvf7mul5.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F9j97zjox5oszmvf7mul5.jpg)

For the longest time, we built applications that ran solely on the server, using things like ASP.NET, PHP, etc and they generated an HTML file to be pushed to the browser.   

We've always had some bit of interactivity with JavaScript and AJAX but for many years most of the business logic is handled on the server itself, spitting out HTML pages to interact. The browser for many years was just a glorified document viewer. It worked, but we knew we could do better.

There are some downsides to this pattern that we're all aware of:

*   The server needs to be configured with software to run the web app. ASP.NET, PHP, etc. Backend processors or runtimes have to exist on the server. 
*   Most of the processing power is on the server. 
*   Page loads are annoying and slow. 

So we found a new answer to it. 

### [](#how-we-do-it-now)How we do it now

With the rise of the Single Page Applications we have a new pattern, with frameworks like Angular, React and Vue:

[![What is Blazor](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fmkaavsy552vmytimuf2f.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fmkaavsy552vmytimuf2f.jpg)

Now we're building full applications in JavaScript that run on the browser. This splits the business logic, so that some runs on the browser, and some runs on the server. JavaScript applications run client-side and use messaging to communicate with the "server". You can easily replace "server" with a service or application in the cloud, but the model is still the same.

This is an excellent improvement on what we had before, which essentially manipulating HTML and tossing it back and forth. Now we have real applications running in the browser, and page loads are mostly a thing of the past.

But Blazor improves on that pattern further. There are two main ways to develop with it.

### [](#option-1-web-assembly-method)Option 1: Web Assembly Method

When you choose to build a Blazor Web Assembly application it looks like this:

[![What is Blazor](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Forwm8f5xzwvw2lf1v03k.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Forwm8f5xzwvw2lf1v03k.jpg)

Blazor uses [Web Assembly](https://webassembly.org/) which ships in all major browsers now. Web assembly is a binary instruction format that runs a virtual environment in the browser.

So what does that really mean?

Now the browser acts as a host for your application. Files built in a Blazor Web Assembly application are compiled and sent to the browser. The browser then runs your JavaScript, HTML and C# in an execution sandbox on the browser. It even runs a version of the .NET Runtime. This means you can execute calls to .NET from within the browser, and it's a fully-fledged application in the browser. It can even be run offline.

#### [](#why-this-is-cool)Why this is cool:

*   You can run it on any static file server (Nginx, ISS, Apache, S3, Heroku, etc)
*   It runs JS as bytecode, and runs C# at near-native speeds.
*   You can use C# to develop rich front-end applications.
*   Web Assembly ships with all major browsers
*   Reuse .NET components
*   Use Microsoft tooling and debugging

This is great for low latency applications such as games. There's no need for communicating with a server if you don't need to. You can download the application and run it offline in a browser. This is great for games and other things you need to run lightning fast in a browser.

#### [](#some-downsides)Some downsides:

*   The .NET Framework and other runtime files need to be downloaded (one time)
*   You're restricted to the capabilities of the browser
*   All secrets (credentials, API keys, etc) downloaded locally
*   Not all .NET Framework components are compatible

So this may not be ideal for all applications. The good news is, there's another Blazor pattern we can use.

### [](#option-2-blazor-server)Option 2: Blazor Server

If you decide to build a Blazor Server application, it looks like this:

[![What is Blazor](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhw15g7u34lu0j4xyljk8.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhw15g7u34lu0j4xyljk8.jpg)

This is closer to the model we're using today. You build an application and have a server that's powered by .NET Core, and you send HTML and JavaScript to the browser to act as a client. This is a great way to make screaming fast thin clients. 

#### [](#why-this-is-cool)Why this is cool:

*   You get the full power of the .NET Framework
*   Everything rests on the server, small downloads
*   Web Assembly is not required
*   Your secrets are safe

#### [](#some-downsidesnbspnbsp)Some downsides:  

*   No offline applications
*   Requires a server running .NET Core or a service
*   Can be high latency with lots of network traffic

### [](#so-how-do-i-choose-which-one-to-usenbsp)So how do I choose which one to use? 

If you want powerful client-side applications that can run offline and served from a static server, choose **Blazor Web Assembly**. If you want the full power of .NET and want to run a model with thin clients, choose **Blazor Server**.

### [](#why-is-this-such-a-big-deal)Why is this such a big deal?

Blazor patterns open up big opportunities for development. Whether you want to build a powerful service with several thin clients, or some cool interactive game that runs in a browser, Blazor enables rich, interactive application potential.

Web Assembly is the way of the future. It enables near-native speeds in a browser, and uses a common interface. You will find Web Assembly on PCs, Phones, and tablets. If you have a bunch of C# developers on your team who don't do front end programming, they are now empowered to do it in the language they love.

It's pretty awesome, and I'm excited to see how Blazor progresses.

### [](#where-can-i-learn-it)Where can I learn it?

You can learn more about it from [Microsoft's Blazor Site](http://bit.ly/BlazorDotNet).

I recently wrote a tutorial about setting up and deploying Blazor apps without touching a Windows Machine

If you want to dig deep and learn Blazor, Pluralsight has some modern courses that will get you running quickly:

*   **[Blazor - The Big Picture](http://bit.ly/BlazorBigPicture)**
*   **[Blazor - Getting Started](http://bit.ly/BlazorGettingStarted)**
*   **[Blazor - Authentication and Authorization](http://bit.ly/BlazorAuth)**
*   **[Creating Blazor Components](http://bit.ly/BlazorComponents)**

So try it out! [Let me know](http://bit.ly/JeremyCMorgan) what you think of Blazor and share your experiences in the comments!
