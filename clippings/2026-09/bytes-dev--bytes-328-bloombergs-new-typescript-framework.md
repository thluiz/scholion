---
url: "https://bytes.dev/archives/328?ref=dailydev"
captured_at: "2026-09-24T23:08:02+01:00"
title: "Bytes #328 - Bloomberg's new TypeScript framework"
domain: "bytes-dev"
---

![Bytes](https://bytes.dev/images/bytes-banner-rounded.png)

**Today’s issue:** Evan You gets some bread, visualizing your (Zod) issues, and live betting on ViteConf.

Welcome to [#328](https://bytes.dev/archives/328).

* * *

![Eyeballs logo](https://bytes.dev/images/content/eyes.png)

## The Main Thing

![Goku smoking a cigar looking at a pile of money](https://bytes.dev/images/content/goku-money.jpg)

Me after investing my life savings into an obscure TypeScript library

### Bloomberg’s new TypeScript framework

If you offered me 10 million dollars, I couldn’t tell you what Bloomberg does. But whatever it is, I’m guessing that static typing is _very_ important because their developers have been launching some really cool TypeScript-flavored OSS lately.

We highlighted [ts-blank-space](https://bloomberg.github.io/ts-blank-space) last month, a fast type-stripping compiler that converts TS to JS. And they just launched [Stricli](https://github.com/bloomberg/stricli/) earlier this week, a framework for building complex CLIs with type safety and zero dependencies.

**Why do we need another CLI framework?** Michael Molisani (the project’s maintainer) [wrote](https://bloomberg.github.io/stricli/blog/intro/) about how existing frameworks like oclif and clipanion do offer full type safety, but they can also introduce additional dependencies and complexity that aren’t necessary for many use cases.

So he and his team built Stricli to give them all the features they wanted, without any extra overhead:

*   **Full TypeScript support** – including types for named flags and positional arguments that are defined once and flow through the entire app.
    
*   **Dual support for ESM and CommonJS** – plus easy code splitting with ESM build tools and dynamic autocomplete.
    
*   **Zero runtime dependencies** – plus support for optional dependency injection, because all system access is encapsulated in a single context object.
    

The tradeoff here is that Stricli was purposefully designed with a more limited scope, so you’ll need to add other packages if you want interactive user prompts, terminal output styling, and other features.

**Bottom Line:** If I had known that open-source TypeScript projects were the secret behind Michael Bloomberg’s $100 billion fortune, I would’ve pledged my allegiance to the Type Nerd Mafia way sooner.

* * *

![Arcjet logo](https://bytes.dev/images/content/arcjet-logo.png)

## Our Friends  
(With Benefits)

![A dog's head on a human's body looking worried](https://bytes.dev/images/content/dog-head.jpg)

Me watching bots flood my email form with infinite variations of bigbuttz99@hotmail.com

### [Protect your app in just a few lines of code with Arcject](https://arcjet.com/?ref=ui.dev)

It gives you _native_ security for Bun, Next.js, Deno, Node.js and every other modern platform – so you can easily implement rate limiting, bot protection, email validation, and protection from common attacks.

**“bUt hOw iS tHIs diFFeReNt fRoM oTheR sEcURitY tOOLs?”** Arcjet is _\*actually\*_ unique because of 3 core principles:

1.  **Proper security needs the _full context_ of the application** – so your security rules are located alongside the code they’re protecting ([see live example](https://example.arcjet.com/?ref=ui.dev)).
    
2.  **Security rules should be easy to test in dev and prod** – so you can [run Arcjet locally](https://docs.arcjet.com/testing/?ref=ui.dev), in staging, and in production.
    
3.  **Security shouldn’t interfere with the rest of your app** – so Arcjet is easy to install, doesn’t add latency, and doesn’t require any re-architecting.
    

[Use it for free on your personal projects](https://arcjet.com/pricing/?ref=ui.dev) – and see how easy it is to get enterprise-quality security.

* * *

![Spot the Bug logo](https://bytes.dev/images/content/spot-the-bug.png)

## Spot the Bug

```
const products = [
  { name: 'Grapes', price: 2 },
  { name: 'Banana', price: 1 },
  { name: 'Apple', price: 3 },
  { name: 'Cherry', price: 2 },
  { name: 'Date', price: 1 }
];

products.sort((a, b) => a.price > b.price);
```

* * *

![Cool Bits logo](https://bytes.dev/images/content/cool-bits.png)

## Cool Bits

1.  [ViteConf is live](https://viteconf.org/live) and happening right now if you want to tune in. I tried using FanDuel to live-bet on how many times the speakers would say “blazing”, but I think that integration is broken.
    
2.  Amelia Wattenberger wrote a beautifully visual article on [bridging the gap between the hard logic of machines and the soft logic of humans](https://wattenberger.com/thoughts/hard-and-soft) with your UI.
    
3.  [Zod.fyi](https://zod.fyi/) lets you visualize the issues in a `ZodError`. The last time my therapist told me to “visualize my issues,” I didn’t go outside for three days, so hopefully this experience will be more helpful.
    
4.  Here’s an early New Year’s resolution – stop wasting your time on manual tests and [get QA Wolf to give you a personalized demo](https://www.qawolf.com/?utm_campaign=CutYourQACycles10032024&utm_source=bytes&utm_medium=newsletter) of how they can help your team achieve 80% automated test coverage and ship 5x faster. They’ve done that for hundreds of companies like Salesloft, Drata, and Autotrader, so you’ll definitely be in good hands. \[sponsored\]
    
5.  ESLint now officially supports [linting JSON and Markdown](https://eslint.org/blog/2024/10/eslint-json-markdown-support/).
    
6.  Devon Govett gave a great talk on [the past, present, and future of JavaScript bundlers](https://www.youtube.com/watch?v=JUS6EPMbk0U).
    
7.  [Eleventy v3.0](https://github.com/11ty/eleventy/releases/tag/v3.0.0) was released full ESM support, async configuration, new Deno support, and more.
    
8.  Datadog’s team created this [Front-end Developer Kit](https://datadoghq.com/bytes) with a bunch of free resources to help you better understand user activity and troubleshoot front-end issues _before_ you crash prod, ideally. \[sponsored\]
    
9.  [Tauri 2.0](https://v2.tauri.app/blog/tauri-20/) comes with hot module replacement, a more advanced plugin system, and some noticeable DX improvements.
    
10.  Vite just [launched a company called VoidZero](https://voidzero.dev/posts/announcing-voidzero-inc) and raised $4.6m from investors. You might not _love_ the idea of VC-funded open source, but it’s probably more sustainable than Evan You releasing a wallpaper app with a bunch of high-res photos of the Vite maintainers that costs $13.99/month.
     

* * *

![Spot the Bug logo](https://bytes.dev/images/content/spot-the-bug.png)

## Spot the Bug: Solution

#### Presented by [Raygun](https://raygun.com/blog/js-toolbox-part-1/?utm_medium=sponsorship&utm_source=bytes&utm_campaign=brand&utm_content=blog)

When using the `Array.sort` method, the compare function should return a number, not a boolean. Returning a negative number will sort the first item before the second, a positive number will sort the second item before the first, and returning 0 will leave the items in the same order.

```
const products = [
  { name: 'Grapes', price: 2 },
  { name: 'Banana', price: 1 },
  { name: 'Apple', price: 3 },
  { name: 'Cherry', price: 2 },
  { name: 'Date', price: 1 }
];

products.sort((a, b) => a.price - b.price);
```
