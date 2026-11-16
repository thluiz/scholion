---
url: "https://dev.to/polypane/8-ways-to-increase-your-productivity-as-a-web-developer-3871"
captured_at: "2026-11-16T01:18:51+00:00"
title: "8 ways to increase your productivity as a web developer"
domain: "dev-to"
---

Making websites takes time. There are a lot of parts you have to think about if you want to create a good, solid website and sometimes it might feel like there just isn't a way to go through the work faster. Whether you work alone or with a team of designers and back-end developers, there are a lot of way to be more productive.

A mistake many people and many companies make is that they set out to standardize their product. They only build based on a single Wordpress theme, or all their sites have the same features. If you want to work with bigger clients they almost never want standard work though. They instead want something custom-fit to their needs and requirements. That's more interesting work, more challenging and pays more. But it also means you you can't standardize your product.

You can't (and don't want to) standardize your **product**, but what you can do is standardize your **process**. As a lead front-end developer with over 15 years of experience, I spent a lot of time thinking about how to optimally configure this process. If you're intentional about it you can get some impressive productivity gains in all areas of the process. Here's 8 ways to do that, from the beginning of the project through to the end:

1.  Start from a solid base
2.  Agree on design shortcuts
3.  Use handoff tools
4.  Use a CSS framework
5.  Re-use your components
6.  Use Emmet
7.  Use Polypane
8.  Set up automated quality checking

### [](#start-from-a-solid-base)Start from a solid base

If you start from scratch every single time, you can be sure you're never going to be faster than the last time. By creating or using a solid base for your website, you can save time on the things you're doing every time.

Backend developers already know this. Many will create their own starter project based on a language and framework of their choice, rather than a CMS. Where a CMS usually has a set number of functionality that you can only used in the way the CMS intended, a framework is more like a big box of building blocks that you can combine in ways that work best for your current project. This concept can be extended to your front-end too.

Take the last few projects and see which HTML is similar. Every website is going to have roughly the same elements: There's always a `<head>` with a title, favicon, opengraph info an links to your CSS and JS. 99% of the time a website will have a header with a logo and some form of navigation, and a footer with a copyright rule and some additional links, and most pages will have a content area for your CMS. Making that part of your "starter" or "base" HTML will save you a lot of time.

Additionally, though most of us love checking out new JavaScript frameworks, for your starter base you can probably get away with a few little JavaScript snippets. Cross-platform JavaScript is much easier than it was a few years ago, and most things can be solved with small "vanilla" scripts.

## [](#agree-on-design-shortcuts)Agree on design shortcuts

Design tools give designers access to all widths, all colors and all font sizes. But in reality your websites will only use a few of each. You can save time during design and during implementation not by cutting corners, but by laying down some ground rules.

This can be super expansive, by creating a full design system, for example in the soon-to-be-released [Modulz](https://modulz.app/), where all the available design elements and variants are pre-designed and generated from actual code. You spend more time up front, but the result is something that can be quickly designed and build, often in tandem.

But design shortcuts can also be super simple: get your team to agree on set of design shortcuts that you apply to every part of the design.

For example, agree on a set of margins you re-use for every design element (like 8px/16px/32px/64px) and a designer will never have to worry about making sure all the margins are perfectly 64px instead of 63px (or worse, 63.47845px. Thanks Sketch!). On the flip side, you as a web developer will never have to waste time asking designers if they actually meant to use 60px this one time, or if it should just be 64 like all the rest. You can do the same for font-sizes and even colors.

This simple, low-tech piece of _communication_ can save you hours of (re)development time. If you already agreed on potential margins everywhere, and any design element that uses a slightly different one you can just use the nearest matching one, then you also don't have to do any pixel-bleep-ing sessions with your designer. Or at least a lot less.

Of course it doesn't mean a design can _never_ use a different margin, but the designer would clearly indicate any exceptions in your design file.

## [](#use-handoff-tools)Use handoff tools

Working from a design file directly is a recipe for problems. Not only can you accidentally move parts of the UI without realizing, but the interface is geared towards creating a design, not dissecting it to re-implement elsewhere. For that, there are handoff tools.

They take a design and bring a unique interface that is focused on what front-end developers do. Favorites of ours include [Avocode](https://avocode.com/), [Zeplin](https://zeplin.io/) and [Marvel](https://marvelapp.com/), but design tools like XD, Figma and Sketch now all include their own handoff modes too.

Get familiar with these tools together with your designer so they can learn the best way to prepare design files for these tools and you as a developer learn how to most efficiently use the tools.

## [](#use-a-css-framework)Use a CSS framework

First let me say that I'm not much of a fan of CSS frameworks. Most are big, slow, carry a lot of legacy and overly limiting while providing no good defaults, or if they have good defaults, they're _usually someone else's defaults_ that probably won't work for you and your situation (Oh hi, Material design).

But.

There are interesting new frameworks that could work for you:

[Bulma](https://bulma.io/) is a "next generation" CSS framework built for modern browsers, so it has a simpler and smaller codebase, is easy to customize and has some good looking defaults. I've seen this work in production really well.

[Tailwind](https://tailwindcss.com/) - Be warned, you might hate it when you first see it (I know I did). The trick here is that it moves your styling from writing CSS to writing class names. Each style (color, margin etc) gets their own classes so even though you're limited to a few fixed classes, your site will always be consistent. You get to either use the defaults, or customize them.

If you get over the fact you have to style using just classes, developing in it becomes really, _really_ fast. The Polypane management console is written with it, for example. If you want to see how varied your designs can be and what the implementations might look like, I recommend [Tailwind Toolbox](https://www.tailwindtoolbox.com/)

## [](#reuse-your-components)Re-use your components

While there are good, fast, accessible and responsive components out there, it's difficult to find ones that perfectly fit your and your teams way of working so often you'll end up creating your own. Yet, between projects there's usually UI elements and patterns that you re-use.

Maybe you have [the perfect responsive menu](https://polypane.app/blog/the-perfect-responsive-menu/), or the perfect contact form with accessible error handling and fancy animation.

Document those in such a way that you can easily implement them in each new project. Over time, they will evolve and you will add new features to them. If you do, don't forget to also update your reference component. Otherwise you'll still be digging around in old project to find that specific version of a component.

## [](#use-emmet)Use Emmet

While any text editor or IDE that you use will have support for snippets (use those for the reusable components we just mentioned), using [Emmet](https://emmet.io/) can save you so much time. It's available for basically all text editors and IDE's.

The concept for Emmet is simple: What if you create HTML by writing CSS selectors? From the Emmet documentation:

This abbreviation:  

```
#page>div.logo+ul#navigation>li*5>a{Item $}
```

...can be transformed into  

```
<div id="page">
  <div class="logo"></div>
  <ul id="navigation">
    <li><a href="">Item 1</a></li>
    <li><a href="">Item 2</a></li>
    <li><a href="">Item 3</a></li>
    <li><a href="">Item 4</a></li>
    <li><a href="">Item 5</a></li>
  </ul>
</div>
```

...with a single "expand" shortcut. You can clearly see which of these two is faster to write, and as a front-end developer you already know CSS so there is very little to learn for such a massive increase in speed.

Just like how Polypane saves you time by all the resizing and reloading you don't have to do, So does Emmet save you time by all the typing you don't have to do.

## [](#use-polypane)Use Polypane

Didn't think I was gonna leave this out, right? On average, [Polypane](https://polypane.app/) saves teams about 60% of their implementation time. That sounds insane, I know, but they're observed numbers. Very simply, if you count up all the time you spend resizing your browser during development, it's a lot. And it's just not something you do only once per page. In Polypane, that resizing doesn't have to happen because you already see all your breakpoints side by side. If you use it for QA, you can decimate the time it takes because you'll have far less devices to manage. More on that in a later article.

Polypane doesn't just save time because you don't have to resize. It has many other tools that will make you as a developer faster, like [built-in live reloading](https://polypane.app/docs/live-auto-reloading/) that will make refreshing the page obsolete too, or [overlays](https://polypane.app/docs/overlays/) that do everything from highlighting contrast issues to running visual impairment simulators live.

If you don't use Polypane yet, I challenge you to keep a tally of how much your resize your browser during a single day. [Then go use Polypane](https://polypane.app/product-tour/).

But more importantly, when you build a site and you see all screen sizes at once, issues are caught faster (often before they happen) so your time spent per page will go down. You simply have less fixes to make after your initial implementation. With time you will automatically take those fixes into account with your first pass saving even more time.

That benefit carries pretty far: it also means far less issues come up after a project has been released. Having to do bug fixes on projects that were finished months ago is the most costly waste of time a web development team can have. Imagine not having to download a database and static files, and set up an old project on your machine just to fix a single issue.

## [](#set-up-automated-quality-checking)Set up automated quality checking

You could manually check your in-progress site every now and then, but quality testers like Lighthouse and Webhint usually take a while to run. Ideally you do not want to wait for them to finish. So rather than running them manually, make them part of your progress. Automate checking every PR, for example, using [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) and [webhint's CI integration](https://webhint.io/docs/user-guide/development-flow-integration/summary/). That way you keep a good overview of how your project is doing quality-wise, without having to waste time waiting for the tests to finish.

## [](#suggestions)Suggestions?

Those are my suggestions for improving the productivity of a web developer. If you have other suggestions, I'd love to hear them!

Reach out on twitter ([@polypane](https://twitter.com/polypane) or [@kilianvalkhof](https://twitter.com/kilianvalkhof)) or email me: [kilian@polypane.app](mailto:kilian@polypane.app) and I'll add them to this article.
