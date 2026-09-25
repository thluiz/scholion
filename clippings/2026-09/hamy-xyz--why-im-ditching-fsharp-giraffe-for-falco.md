---
url: "https://hamy.xyz/blog/2025-01_ditching-giraffe-for-falco"
captured_at: "2026-09-25T19:18:25+01:00"
title: "Why I'm Ditching F# + Giraffe For Falco For Building WebApps"
domain: "hamy-xyz"
---

I recently released version 3 of [CloudSeed - my F# webapp project boilerplate](https://cloudseed.xyz/). The release contains various changes but the biggest is migrating webframeworks from Giraffe to Falco.

In this post I wanted to share a little background on why I'm making the change.

## F# + Giraffe

I want to start off by saying that [Giraffe](https://github.com/giraffe-fsharp/Giraffe) remains a solid webframework. It's fast, it's straightforward, it's battle-tested, and it still gets regular updates.

There is nothing wrong with using Giraffe to build webapps with F#. I've been happily [building webapps with F# + Giraffe](https://hamy.xyz/blog/tags/giraffe) for the past few years and there's not much reason to migrate my existing projects off it (in fact this blog runs on F# + Giraffe currently).

_More on how I built this blog: [Build a Simple Markdown Blog with F# / Giraffe](https://hamy.xyz/blog/2023-12-fsharp-giraffe-markdown-blog)_

But the library isn't without its downsides. I find some of the APIs a bit cumbersome, there's sharding in the community ab best practices around things like endpoints, and while it gets small updates it rarely gets big ones. These aren't big issues really - the framework is battle-tested, production-ready, and is feature complete. But it is to say it's not perfect.

## F# + Falco

I've had my eye on the [Falco web framework](https://github.com/pimbrouwers/Falco) for awhile (here's my [2023 F# web framework roundup](https://hamy.xyz/blog/2023-01-top-fsharp-backend-frameworks) that highlights Falco). It's a web framework that focuses clear and straightforward APIs.

I've followed [the creator](https://github.com/pimbrouwers)'s journey and was intrigued with the updates in v5 so gave it a try.

Overall I liked the ergonomics of the APIs, was happy to see it similarly performant, and wanted to support its ongoing development so decided to take the plunge.

I've since built [several side projects with Falco](https://hamy.xyz/blog/tags/falco) and liked it enough to make it the default for my projects going forward. So that's what I did.

![CloudSeed with Falco](https://cdn.hamy.xyz/labs/posts/2025/2025-01_ditching-giraffe-for-falco/20250116_cloudseed-falco_0.png)

## CloudSeed Going Forward

CloudSeed aims to be a [Simple Scalable System](https://hamy.xyz/blog/2024-03_simple-scalable-systems) for starting, running, and scaling webapps.

Largely this means it provides what I currently believe is the best foundation for most webapps - an 80/20 approach including core features, tech stack, and patterns.

So I've updated CloudSeed to reflect my current philosophy for building webapps - and that includes using Falco as the core web framework.

## Next

Before I wrap up I want to call out that there are several other production-ready F# web frameworks including Saturn, WebSharper, and Oxpecker (see [official F# docs](https://fsharp.org/guides/web/)). I've decided Falco is right for me but it's possible another one will work better for you so worth giving them a look.

_Get up and running with a fullstack F# webapp in minutes with [CloudSeed](https://cloudseed.xyz/)._

If you liked this post you might also like:

*   [Build a Single-File Web API with F# + Falco](https://hamy.xyz/blog/2024-10_fsharp-falco-webapi)
*   [Build a Simple Single-File Web API with F# / Giraffe](https://hamy.xyz/blog/2024-09_single-file-webapi-fsharp-giraffe)
*   [Why F# is a fun programming language](https://hamy.xyz/blog/2024-02_fsharp-is-fun)
