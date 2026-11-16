---
url: "https://blog.elmah.io/upload-and-resize-an-image-with-asp-net-core-and-imagesharp"
captured_at: "2026-11-16T04:28:20+00:00"
title: "Upload and resize an image with ASP.NET Core and ImageSharp"
domain: "blog-elmah-io"
---

Written by [Thomas Ardal](https://blog.elmah.io/author/thomas/), March 17, 2020

While migrating our web app to ASP.NET Core, I had to find a new way for the user to upload and resize a profile photo. We used the `WebImage` class in ASP.NET MVC, which unfortunately isn't available in Core. In this post, I will show you how I solved it using file support in ASP.NET Core and the ImageSharp library.

[![Upload and resize an image with ASP.NET Core and ImageSharp](https://storage.ghost.io/c/a8/df/a8df410f-f385-46fe-9464-e894f7952067/content/images/2020/12/upload-and-resize-an-image-with-asp.net-core-and-imagesharp.png)](https://storage.ghost.io/c/a8/df/a8df410f-f385-46fe-9464-e894f7952067/content/images/2020/12/upload-and-resize-an-image-with-asp.net-core-and-imagesharp.png)

Upload and resize an image with ASP.NET Core and ImageSharp

Let's face it. While ASP.NET Core is a great web framework already, some things are still missing (or intentionally left out to make room for alternatives). Resizing images is such a feature. The `WebImage` class in ASP.NET, was a pretty impressive little helper, covering most needs when needing to allow for user uploads, image manipulation and more. Like already mentioned, `WebImage` hasn't been ported to ASP.NET Core, why something else is needed.

Let's start by looking at file uploads in ASP.NET Core. To implement some backend, I'll start by creating a simple client:

```
<form enctype="multipart/form-data" method="post" action="/home/upload">
    <input type="file" name="file" />
    <input type="submit" />
</form>
```

No magic there. Just an (ugly) HTML form with a file picker:

[![Upload file form](https://storage.ghost.io/c/a8/df/a8df410f-f385-46fe-9464-e894f7952067/content/images/2020/03/file-form.png)](https://storage.ghost.io/c/a8/df/a8df410f-f385-46fe-9464-e894f7952067/content/images/2020/03/file-form.png)

There are multiple ways of creating the form and you could even upload the file through AJAX. The official documentation from Microsoft has some good samples, why I don't want to repeat them here.

To implement the `/home/upload` as an action accepting a file, you can use the `IFormFile` interface available in the `Microsoft.AspNetCore.Http` namespace:

```
[HttpPost]
public IActionResult Upload(IFormFile file)
{
    // ...
    return Ok();
}
```

If you put a breakpoint inside the `Upload` method, you will see metadata about the chosen file:

[![File metadata](https://storage.ghost.io/c/a8/df/a8df410f-f385-46fe-9464-e894f7952067/content/images/2020/03/file-info.png)](https://storage.ghost.io/c/a8/df/a8df410f-f385-46fe-9464-e894f7952067/content/images/2020/03/file-info.png)

Now for the resizing part. Since we no longer have access to the `WebImage` class, I'll install an excellent replacement named `ImageSharp`:

```
Install-Package SixLabors.ImageSharp -IncludePrerelease
```

`ImageSharp` is currently in beta but already working out great. `ImageSharp` has an `Image` class that works like `WebImage` in a lot of ways. It accepts the posted file as a stream:

```
using var image = Image.Load(file.OpenReadStream());
```

Once you get an instance of the image, you can start manipulating it using the `Mutate` method. For this post I want to resize the image to a fixed size:

```
image.Mutate(x => x.Resize(256, 256));
```

Finally, we can save the image to a stream or as a file:

```
image.Save("filename");
```

Again, lots of possibilities using the `Image` class, so check out the documentation.

Here's the entire `Upload` method:

```
[HttpPost]
public IActionResult Upload(IFormFile file)
{
    using var image = Image.Load(file.OpenReadStream());
    image.Mutate(x => x.Resize(256, 256));
    image.Save("...");
    return Ok();
}
```

That's pretty compact IMO.

### [elmah.io](https://elmah.io/): Error logging and Uptime Monitoring for your web apps

This blog post is brought to you by elmah.io. elmah.io is error logging, uptime monitoring, deployment tracking, and service heartbeats for your .NET and JavaScript applications. Stop relying on your users to notify you when something is wrong or dig through hundreds of megabytes of log files spread across servers. With elmah.io, we store all of your log messages, notify you through popular channels like email, Slack, and Microsoft Teams, and help you fix errors fast.

[![elmah.io app banner](https://blog.elmah.io/assets/img/elmahio-app-banner.webp?v=ynVeGari0x9GA-uD)](https://elmah.io/)

[See how we can help you monitor your website for crashes Monitor your website](https://app.elmah.io/signup/)
