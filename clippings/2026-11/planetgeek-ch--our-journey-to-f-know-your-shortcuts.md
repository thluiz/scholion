---
url: "https://planetgeek.ch/2020/07/15/our-journey-to-f-know-your-shortcuts"
captured_at: "2026-11-16T04:38:30+00:00"
title: "Our journey to F#: Know your shortcuts"
domain: "planetgeek-ch"
---

I develop code with C# for 18 years and I’m a heavy ReSharper/Rider user. So I know a lot of shortcuts. Really a lot.  
_Actually, my fingers know them. Whenever I get asked during pair programming how I did this, I almost certainly reply with: “ask my fingers, I don’t know.”_

Programming in F#, I had to retrain my fingers to use some new shortcuts that I was not used to. And that’s why I share them here with you:

## Error Description (Ctrl+F1 / Alt+T)

I use the error description to show me the function signature when calling a function. This is quicker than hovering over the function with the mouse to show the tooltip.

![](https://www.planetgeek.ch/wp-content/uploads/2020/06/Error-Description.png)

Error description shows the function signature

Unfortunately, the visualisation is rather weak and larger signatures are hard to read. But there is hope that the tooltips in Rider get some love in an upcoming version ([https://blog.jetbrains.com/dotnet/2020/05/29/rider-2020-2-roadmap/](https://blog.jetbrains.com/dotnet/2020/05/29/rider-2020-2-roadmap/)).

## Go to type definition

In C#, I’m used to navigate a lot with `F12` (Go to declaration): go to declaration of a variable, then jump to the declaration of its type.

However, that doesn’t get me far in F# when types are inferred. So I switched to **Go to definition** (Ctrl+Shift+F11) that takes me directly from a value to its declaring type.

Of course, this works exactly the same in C#, but I asked around, and my peers know about `F12` but not about `Ctrl+Shift+F11`.

_But as [Patrick](https://twitter.com/constlyConfused) told me: “once a user has found a way to get the task done, she or he won’t look for another.”_ True, true, true.

Find the next post in this series [here](https://www.planetgeek.ch/2020/07/16/our-journey-to-f-bye-bye-fluent-syntax/).

Find all blog posts about our journey to F# [here](https://www.planetgeek.ch/tag/f-journey/).

[![](https://www.planetgeek.ch/wp-content/uploads/2020/05/timerocket-rocket-1024x992.png)](http://timerocket.ch/)

This blog post is made possible with the support of [Time Rocket](http://timerocket.ch/), the product this journey is all about. Take a look (German only).
