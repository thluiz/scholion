---
url: "https://startbigthinksmall.wordpress.com/2009/01/20/utf8encodingdefault-encodingutf8-net-c/"
captured_at: "2015-06-12T15:39:53-03:00"
title: "UTF8Encoding.Default != Encoding.UTF8 (.NET C#)"
domain: "startbigthinksmall-wordpress-com"
---

# UTF8Encoding.Default != Encoding.UTF8 (.NET C#)

January 20, 2009 by [Lars Corneliussen](https://startbigthinksmall.wordpress.com/author/larscorneliussen/ "Posts by Lars Corneliussen")

Looks like *UTF8Encoding.Default* would return a default instance of the UTF8Encoding, right?

Well, it doesn’t – it returns the operating system’s default ANSI encoding.

The same with *ASCIIEncoding.Default*, *UnicodeEncoding.Default*, *UTF32Encoding.Default* and *UTF7Encoding.Default*!

Why? Because they all derive from ***System.Text.Encoding*** **where *Default* is definded:**

```
|  |  |
| --- | --- |
|  | /// <summary>  /// Gets an encoding for the operating  /// system's current ANSI code page.  /// </summary>  public static System.Text.Encoding Default { get; } |
```

[![tmp1f4-thumb.png](startbigthinksmall-wordpress-com--utf8encoding-default-vs-encoding-utf8-dotnet-csharp/5b6f1bb5f5df1780808a678c0206642d.png)](https://startbigthinksmall.files.wordpress.com/2009/01/tmp1f4.png)

So instead use *Encoding.ASCII*, *Encoding.UTF8*, *Encoding.UTF7*, *Encoding.UTF32* and *Encoding.Unicode* to refer explicitly to an encoding.

[About these ads](http://wordpress.com/about-these-ads/)
