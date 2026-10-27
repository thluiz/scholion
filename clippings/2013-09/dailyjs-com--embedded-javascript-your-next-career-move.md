---
url: "http://dailyjs.com/2013/08/26/embeddedjs/"
captured_at: "2013-09-05T13:54:41-03:00"
title: "DailyJS: Embedded JavaScript: Your Next Career Move"
domain: "dailyjs-com"
---

# [Embedded JavaScript: Your Next Career Move](http://dailyjs.com/2013/08/26/embeddedjs)

26 Aug 2013 |
By Alex Young |
[v8](http://dailyjs.com/tags.html#v8)
[microsoft](http://dailyjs.com/tags.html#microsoft)
[google](http://dailyjs.com/tags.html#google)

Most of us started out writing JavaScript for web pages**.** Even if you’re a server-side developer focused on Node, you probably wrote client-side JavaScript first**.** We see JavaScript as a language closely integrated with the DOM, and as a relatively lightweight server-side language, but you can flip this around and think of it as en entirely embedded language: after all, it’s embedded within web pages – it’s bridged to native data structures and functionalities that are required by the runtime**.**

### Why Embed?

Why are scripting languages embedded in other software at all**?** If you think about a large C++, C#, or Objective-C project, then build time and deployment are major issues**.** Certain programming chores lend themselves well to scripting languages, so rather than rebuilding a huge project every time a small tweak is required, changing a script might be more productive**.**

In game development Python and Lua are typical choices for scripting**.** They’re used for game interfaces, logic, asset loading, AI, and more**.** Part of the success of the modding community based around Unreal engine games came from the use of [UnrealScript](http://en.wikipedia.org/wiki/UnrealScript) **.**

### Binding

You’re probably wondering: why Python and Lua**?** It’s mainly because these languages are widely adopted and suitable for embedding**.** [Boost.Python](http://www.boost.org/doc/libs/1_54_0/libs/python/doc/index.html)  and [Luabind](http://www.rasterbar.com/products/luabind.html)  are examples of libraries that help with binding**.** Without bindings to the underlying native code it’s impossible for the scripting language to communicate, so this has to be fast and easy**.**

### Web UI

An alternative to low-level binding is to use a web view that hosts JavaScript code, with some event-based bindings to the underlying application**.** Many mobile and desktop applications use web views for chunks of UI that are easier to implement with HTML, so this is happening more often than you might realise**.**

Once you’ve got large amounts of UI written with HTML, the required JavaScript starts to become messy**.** That’s where modern MVC frameworks like Backbone and AngularJS come in: but writing this code properly is a whole skill in itself, so that’s when the C++/Objective-C developers call us for help**!**

Unfortunately, embedding JavaScript as a runtime isn’t simple as it should be**.** There are many different ways to do it for each language**.**

In the .NET world there are lots of projects for running JavaScript inside your applications**.** [IronJS](https://github.com/fholm/IronJS)  is an ECMAScript 3.0 implementation built on Microsoft’s [Dynamic Language Runtime](http://dlr.codeplex.com/) **.** [ClearScript](http://clearscript.codeplex.com/)  allows multiple scripting languages to be added to .NET applications: it supports JavaScript through V8 – imagine being able to add `using Microsoft.ClearScript.V8` to a C# program and then do `engine.Execute("Console.WriteLine(lib.System.DateTime.Now)")`**.** There’s also [Jurassic](http://jurassic.codeplex.com/)  – another ECMAScript runtime**.**

The general wisdom seems to be that [embedding V8 is the way to go](https://developers.google.com/v8/embed) **.** There are also SpiderMonkey-based projects like [libjspp](https://code.google.com/p/libjspp/) **.**

### Objective-C

Apple’s [Introduction to WebKit Objective-C Programming Guide](https://developer.apple.com/library/mac/documentation/cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html)  explains how to access JavaScript from Objective-C**.**

Another approach is to embed [JavaScriptCore](http://trac.webkit.org/wiki/JavaScriptCore) **.** Apparently, [Appcelerator Titanium](http://en.wikipedia.org/wiki/Appcelerator_Titanium)  uses JavaScriptCore for iOS projects – you should be able to figure this out by looking at [Appcelerator’s GitHub projects](https://github.com/appcelerator/) **.**

### Job Opportunities

I’m currently contracting at a particularly eclectic office: my team has Objective-C, C++, C#, and JavaScript developers**.** The shared wisdom amongst the non-JavaScript developers is they want to embed JavaScript in their projects: whether they’re games, desktop software, or mobile applications**.**

That’s great for us, but it’s worth remembering that JavaScript isn’t good at *everything* – the type system might not suit certain projects, its scope and coercion rules can be a source of frustration for people from other backgrounds**.** It looks C-like, but that doesn’t mean it’s C: and that’s the problem when you’re working with people who are more fluent in C than JavaScript**.**

If you’re wondering how people see JavaScript from the other side, then I found [Choosing a scripting language](http://blog.wolfire.com/2010/01/Choosing-a-scripting-language)  by David Rosen interesting: he struggled with JavaScript’s readability because he couldn’t overload operators, and wanted to write maintainable linear algebra code**.**

However, it seems like there’s a huge amount of momentum behind JavaScript in a growing number of platforms, so it’s an area you should take seriously**.** Don’t be surprised to find yourself writing scripts for games or apps in the near future**.**
