---
url: "https://dev.to/areknawo/why-you-should-have-ditched-ie-support-long-ago-1jj9"
captured_at: "2020-09-07T20:03:12-03:00"
title: "Why you should have ditched IE support long ago... - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

# Why you should have ditched IE support long ago...

7 de jan.
*Originally published at
[areknawo.com](https://areknawo.com/why-you-should-have-ditched-ie-support-long-ago/)*
・9 min read

**This post was taken from [my blog](https://areknawo.com/), so be sure to check it out for more up-to-date content.**

[October 14, 2025](https://death-to-ie11.netlify.com/) - remember this date, as this will supposedly (still not official) be the last day of *IE 11* support. Why I'm telling you this? Well, because, as you might know, IE is one of these web browsers that cause headaches for many web developers. But is this really that bad, and should you even care about IE support in 2020?

# A bit of history

*Internet Explorer* (IE) is a web browser, originally released by Microsoft in *1995*. These were times when web browsers were at their infancy, and standards weren't widely-respected. JavaScript wasn't even a thing (created December 1995) and browsers often contained custom unstandardized features, addons, and plugins.

So, when Microsoft entered the market with IE in 1995, it didn't have much competition (other than [Netscape Navigator](https://en.wikipedia.org/wiki/Netscape_Navigator)). Not long after the original release MS started including IE for free in every new version of its highly-popular OS - *Windows*. This resulted in a drastic increase in IE usage, topping off at more than *90% market share* in the early 2000s. Of course, it wasn't all without anti-trust and power-abuse controversies, but that's not important right now.

Dialogs and pop-ups like "Sorry, but this website only works on IE" went pretty wild. But, it all soon ended as Microsoft failed to improve its web browser and started introducing quirks and obstacles instead. The Web also became more accessible, and other web browsers entered the market (like *Google Chrome* in 2008). All of this, together with the rise of *mobile* ([IE Mobile](https://en.wikipedia.org/wiki/Internet_Explorer_Mobile) - there was such a thing), resulted in IE usage coming crashing-down to what now is [~1.5%](https://gs.statcounter.com/).

Apparently, even Microsoft [came to a conclusion](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/the-perils-of-using-internet-explorer-as-your-default-browser/ba-p/331732) that its web browser was failing. So, in 2015, together with Windows 10, it released the all-new *Edge* browser, with rewritten internals. However, low market share and "just install Chrome" mindset, proved too much for the new browser to handle. Microsoft had to act yet again.

Just in a few days, on January 15, 2020, a [new version of Edge](https://www.theverge.com/2019/11/4/20942038/microsoft-edge-chromium-release-date-new-logo-features), with fresh *new icon* and [Chromium](https://www.chromium.org/Home) at its core (the same one that powers *Chrome*, *Opera* and many other browsers), will try to once again to take back its userbase. The browser is available to download in beta [right now](https://www.microsoftedgeinsider.com/en-us/), and I must admit - it feels OK. Kind of like Edge and Chrome combined!

# Missing features

But let's get back to the main topic. Recently, when working on a redesign of this very website, I was considering what it would take to support IE. As it turns out - quite a lot! So, I'm sorry to all the *<0.4%* of my readers who use it as their main browser, but I'll stop supporting it in the near future. To justify my choice, let's go over a few features which a potential website that wants to support IE 11 (not even mentioning its older versions) would have to give up.

## JavaScript

JS really exploded in popularity with the introduction of *ES6* in 2015. Given that IE 11 was originally introduced in *2013* and replaced by Edge shortly after, in 2015, it's expected that it won't provide modern ES6 features. You might not even consider it an problem, as tools like [Babel](https://babeljs.io/) can handle the compatibility issues pretty fine. However, certain features cannot be *polyfilled* (replaced with "older" code). Also, as a lot of browsers [support ES6](https://areknawo.com/ecmascript-6-and-up-in-2019/), polyfilling it can only result in unnecessarily bloated code or complicated production pipeline.

### EcmaScript 6

Based on the data from [Can I Use](https://caniuse.com/), IE 11 doesn't support most of the EcmaScript 6 (ES6) features. This means no syntactical sugar like *arrow functions* or *classes*, but also more implementation-bound features, like *Promises* or *WeakSets*. Others, like (*Weak*)*Maps*, *Sets* and `let`/`const` variable declarations are only partially-supported. Naturally, features newer than ES6 are even less common (if they even exist).

There are a lot more of such examples, but I don't want to be nitpicky. Old versions of other browsers also don't provide certain features, but they're either frequently (and seamlessly) *updated* or not too popular.

### Web APIs

While not part of the JavaScript itself, *Web APIs* allow for some really unique functionalities to be used on the Web. However, unlike syntax-related features, these, in most cases, are impossible to polyfill.

From the more relevant Web APIs, IE lacks support for [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), [Web Notifications](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API) and [WebRTC](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API). And while the Fetch API can be polyfilled with the use of [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), the other two cannot. Thankfully, both Notification API and WebRTC are meant for modern, feature-rich web apps, that aren't even targeting IE in the first place.

There are also examples of Web APIs having only partial support. The most notable one is probably [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API). WebGL 2 support is obviously not present, but that's expected. What's more important is the fact that IE 11 still requires `"experimental-webgl"` identifier to access WebGL context, rather than the standard `"webgl"`.

## HTML/CSS

If you want it hard enough, you can make a website without JavaScript. When considering Server-Side Rendering (SSR) or [JAMStack](https://jamstack.org/) (static websites) - it's not actually that hard. But there's no way of avoiding CSS, let alone HTML! And sadly enough, features-related issues got even here! Let's name a few of them.

### HTML

From the HTML side, things look pretty good - if you consider partial *HTML5* support "good". There aren't many features lacking - just those that were introduced a bit later than the standard itself, so it's fine.

### CSS

CSS, however, is a whole another story. Mostly it's full of partially-supported, but really important features like *Flexbox*, *Grid*, *CSS variables* and *viewport units* (e.g. `vmax`). Some only require a prefix but others either lack certain functionalities or support older, incompatible versions of the specs. CSS can still be processed with tools like [PostCSS](https://postcss.org/), but it's still bad, considering that most web browsers fully support the listed features.

# Case-study

For the purpose of this post, I left my *Linux comfort zone* and went on a journey to Windows 10's darkest corners - the IE 11. I must admit - the experience and performance of the browser itself leave a lot to be desired. I also couldn't help but reflect on all the memories and jokes that came to my mind. ;) Anyway, as we now have some knowledge about IE 11 limited feature set, let's browse a few websites and see how they work!

## [Areknawo](https://areknawo.com/)

I'll start with *my blog*. In its current version, it works pretty well. Only the JavaScript part of it doesn't work. The ad at the top doesn't show up, the newsletter subscription box and the [Disqus](http://disqus.com/) comments under each blog post disappeared and the AJAX page transitions don't work. All of this thanks to... unsupported *ES6 template literals* being used in my code!

Honestly, I don't think I'm going to fix this little issue - especially when working on IE-incompatible redesign. It just doesn't make much sense. This blog is directed towards web developers and "techy" people that usually use all the latest and greatest tools. Most of the targeted demographic simply doesn't use IE and even if... maybe only for testing. ;)

## [YouTube](https://www.youtube.com/)

Opening *YouTube* on IE feels like going *back in time*. Everything works, but the UI is simply outdated. Seems like Google left the browser with the last redesign that it's compatible with. Smart move. But for smaller organizations and companies, maintaining old versions of the same website might be somewhat inefficient.

## [GitHub](https://github.com/)

*GitHub* simply tells you that you're using an unsupported browser. Funny is the fact that it's now [owned by Microsoft](https://news.microsoft.com/announcement/microsoft-acquires-github/) itself. But I don't blame them - they did the right thing. Anyway, you can dismiss the *little dialog*, but right off the bat, you'll be greeted with a broken toolbar. The login page also seems to be broken and shows a loader all the time. I didn't try to log in, as I'm a bit afraid about the *security* of that thing - there have been multiple security issues with IE in the past.

## [CodePen](http://codepen.io/)

*CodePen* also shows a dialog, but much bigger and "undismissable". It says that PRO members can use it with so-called *Debug View*, but as I haven't tested it, I've got nothing more to say.

## [CSS-Tricks](https://css-tricks.com/)

*CSS-Tricks* is an example of [a simple website](https://css-tricks.com/simple-boring/) - it doesn't use much JS and features mostly *text-heavy content*. There's no dialog or info - just a *somewhat broken* page. Styles are off and things disappear, but at least the content and posts are readable.

## Others

There's not enough space for this post to contain all the "anti-IE" websites. I still have some honorable mentions, though! [Slack](https://slack.com/) and [Trello](https://trello.com/) - very popular productivity tools simply don't allow you to log in. And even [Apple's homepage](https://www.apple.com/) layout is broken! Other pages look fine, although without fancy scrolling effects and you cannot buy anything unless you "upgrade your browser".

If you still want more examples than that, feel free to open IE 11 (if you're using Windows 10 - it's probably still there) and check out some of the websites you're usually visiting. Along the way, you'll feel the pain that I've gone through! ;)

# Final words

The main goal of this post is to tell you that supporting IE is not that important anymore. You should feel a bit more *freedom* when it comes to using modern features. Especially when considering new projects.

I've heard of enterprises that rely upon IE-only code and cannot afford to upgrade. In my humble opinion, this is just *bad design* - no offense. The Web was and is a very dynamic place where you have to adapt and change in order to persist. If the design of your app doesn't let you do that, then it's not good. That's just my opinion. As a matter of fact, I even experienced such a website, which, funnily enough, didn't even work on IE 11! It required the previous version of the browser to properly work - even though none of them are supported anymore!

So, unless you're targeting a very broad or specific demographic, I'd say that you shouldn't care that much about IE. If supporting it doesn't cost you anything or doesn't limit your product's functionalities, then go for it! But, based on the features we've discussed, it seems the reality is often different...

Anyway, that's it! Let me know down in the comments what do you think about the whole *IE support* thing and if your website supports it. Also, if you like this post consider *sharing it* and *following me* on [Twitter](https://twitter.com/areknawo), [Facebook](http://facebook.com/areknawoblog) or simply checking out [my personal blog](https://areknawo.com/) to keep up-to-date with all of the latest content. If you're interested, I also got a [YouTube channel](https://www.youtube.com/channel/UCUw6bg379ONlG1E_oxhwi-A/), which you can check out and drop a like or a sub there! As always, thank you very much for reading this piece, and have a nice day!
