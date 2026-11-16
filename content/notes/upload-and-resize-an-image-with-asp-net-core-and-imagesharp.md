---
title: "Upload and resize an image with ASP.NET Core and ImageSharp"
date: '2020-04-20T21:22:38+00:00'
category: webclip
summary: 'Explains how to replace ASP.NET MVC''s WebImage in ASP.NET Core by accepting an uploaded file with IFormFile, loading it with ImageSharp, resizing it, and saving the result.'
tags: ["asp-net-core", "imagesharp", "file-upload", "image-resizing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Upload and resize an image with ASP.NET Core and ImageSharp"
    url: "https://blog.elmah.io/upload-and-resize-an-image-with-asp-net-core-and-imagesharp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-elmah-io--upload-and-resize-an-image-with-asp-net-core-and-imagesharp.md"
    kind: repo
---

The post shows a simple way to handle user photo uploads in ASP.NET Core after moving away from ASP.NET MVC. Since `WebImage` is not available in Core, it uses `IFormFile` for uploads and ImageSharp for loading, resizing, and saving the image.

## Reading notes

- The author needed a new way to let users upload and resize a profile photo during a migration to ASP.NET Core.
- The old `WebImage` helper from ASP.NET MVC is not available in ASP.NET Core.
- A basic upload form can post a file with `multipart/form-data` to `/home/upload`.
- The upload action can accept the file through the `IFormFile` interface from `Microsoft.AspNetCore.Http`.
- ImageSharp is presented as the replacement for `WebImage`.
- The image can be loaded from `file.OpenReadStream()` with `Image.Load(...)`.
- The `Mutate` method can resize the image to a fixed size, such as `256 x 256`.
- The resized image can then be saved to a stream or to a file.
- The full `Upload` method combines file upload, image loading, resizing, and saving in a short action method.
