---
title: "UTF8Encoding.Default != Encoding.UTF8 (.NET C#)"
date: '2015-06-12T15:39:53-03:00'
category: webclip
summary: 'The post explains that UTF8Encoding.Default does not return UTF-8. It returns the operating system’s default ANSI encoding, so explicit Encoding.UTF8 and similar properties should be used instead.'
tags: ["dotnet", "csharp", "encoding", "utf-8"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "UTF8Encoding.Default != Encoding.UTF8 (.NET C#)"
    url: "https://startbigthinksmall.wordpress.com/2009/01/20/utf8encodingdefault-encodingutf8-net-c/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/startbigthinksmall-wordpress-com--utf8encoding-default-vs-encoding-utf8-dotnet-csharp.md"
    kind: repo
---

The post says that `UTF8Encoding.Default` does not create a UTF-8 encoder. It returns the operating system’s default ANSI encoding, and the same applies to `ASCIIEncoding.Default`, `UnicodeEncoding.Default`, `UTF32Encoding.Default`, and `UTF7Encoding.Default` because they all derive from `System.Text.Encoding`.

It points to `System.Text.Encoding.Default` as the place where this behavior is defined, and recommends using `Encoding.ASCII`, `Encoding.UTF8`, `Encoding.UTF7`, `Encoding.UTF32`, and `Encoding.Unicode` when an encoding needs to be named explicitly.

## Reading notes

- `UTF8Encoding.Default` returns the OS default ANSI encoding, not UTF-8.
- The same pattern applies to `ASCIIEncoding.Default`, `UnicodeEncoding.Default`, `UTF32Encoding.Default`, and `UTF7Encoding.Default`.
- `System.Text.Encoding.Default` is defined as the operating system’s current ANSI code page.
- Use `Encoding.ASCII`, `Encoding.UTF8`, `Encoding.UTF7`, `Encoding.UTF32`, and `Encoding.Unicode` to refer to encodings explicitly.
