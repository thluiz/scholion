---
url: "https://planetgeek.ch/2020/07/17/our-journey-to-f-relearning-using-the-ide"
captured_at: "2026-11-16T04:38:56+00:00"
title: "Our journey to F#: Relearning using the IDE"
domain: "planetgeek-ch"
---

After a month of programming F#, I realized that I changed my usage of my IDE (JetBrains Rider). Here is how and why:

## Where are the important parts?

I was used to put the most important code in C# at the top of each file – typically the public members of the class, followed by the code invoked by them – the private methods. So I was used to locate the file I’m looking for in the Solution Explorer and start reading at the top. Or when navigating with `Ctrl+T`, I could directly jump to a type or file and start reading – at the top again.

With F# the direction is reversed. The (typically) important code is at the end of the file and invokes functions and uses types that are defined earlier in the file.

As simple as it is, it took me a while to get used to this. One tool that helped me a lot is the Structure tool window (Rider or ReShaper). It shows the contents of a file, its types and functions. After getting used to the Structure tool window, my navigation skills got a lot better.

## Modules and classes are very different

After starting to write code in F#, I quickly realized that I arrange my code quite differently. In C#, I put every single class in its own file. In F#, I put the things belonging closely together into the same module – the same file. Because F# code is typically so much shorter than the equivalent C# code and the Structure tool window provides me with a good overview of a file this feels very good. I don’t have to switch files as often as in C#, which makes coding a bit faster.

## Explorability – aka how much can IntelliSense help me

At first, I struggled with calling functions because Rider did not help me much with IntelliSense. When I wanted to call a function from another module, I opened the module at the top of the file and tried to write the function name correctly – of course, I failed to guess the right name often. So I jumped over to the other module and looked up the name. I felt like being back in the early 2000s when programming C++ in Sniff.

Until I realized that there is a much better way. Instead of opening the module at the top of the file (by hand by the way) and guessing the function names, I first wrote the name of the module followed by a dot. Et voilà, IntelliSense is back. Rider could automatically add the module to the list of opened modules and show me all the contained functions. For many of you, that may be obvious. It wasn’t for me in the first couple of weeks of F#.

Since writing the blog post about Shortcuts, I also realized that in using `Ctrl+Space` works better than `Alt+Enter` to include modules – even when the name of the module is written correctly.

## Solution-wide analysis

I’m a really really really big fan of solution-wide analysis in Rider/ReSharper with C#. Not so much anymore with F#. I still haven’t figured out when it is capable of showing me errors introduced by making a change in code, and when not. I just find myself building the code much more often than when writing C#. That’s sad, but not too big a problem.

Maybe it has something to do that my F# code was using inter-op with C# a lot. Remember that I ported only a very small slice of our existing C# code to F#, so the F# code made a lot of calls to C#.

What’s for sure, Rider cannot show changes in F# that result from changes in C# code without a build. When switching rapidly between C# and F# that sometimes caught me on the wrong foot. I don’t think that will be a problem when we write complete features in F# and have much less inter-op.

Find the next post in this series [here](https://www.planetgeek.ch/2020/08/11/our-journey-to-f-happy-path-coding/).

Find all blog posts about our journey to F# [here](https://www.planetgeek.ch/tag/f-journey/).

[![](https://www.planetgeek.ch/wp-content/uploads/2020/05/timerocket-rocket-1024x992.png)](http://timerocket.ch/)

This blog post is made possible with the support of [Time Rocket](http://timerocket.ch/), the product this journey is all about. Take a look (German only).
