---
title: "Proxy Design Pattern in C# - Code Maze"
date: '2026-09-24T23:18:02+01:00'
category: webclip
summary: 'The Proxy pattern adds a wrapper around a real object to control access and add logic without changing the original service. The article shows a caching proxy in C# and mentions logging, protection, remote, virtual and selection proxies.'
tags: ["proxy-pattern","csharp","caching","design-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Proxy Design Pattern in C# - Code Maze"
    url: "https://code-maze.com/csharp-proxy-design-pattern/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/code-maze-com--proxy-design-pattern-in-c-sharp-code-maze.md"
    kind: repo
---

The article explains the Proxy design pattern as an extra layer of control over access to an object. The proxy implements the same contract as the real subject, holds a reference to it, and can run its own actions before or after delegating a call.

It uses an exchange-rate service to show why a proxy is useful when repeated remote calls hurt performance. A caching proxy keeps the client and the original service unchanged, stores the first result, and serves later requests from cache. The text also mentions logging, protection, remote, virtual, and selection proxies, and notes that proxies can add complexity, maintenance overhead, performance cost, cache invalidation issues, leaky abstraction, and security risks when used alone.

## Reading notes

- The proxy is a structural pattern that places an extra layer of control over access to an object, using a wrapper that acts on behalf of the real object.
- The proxy implements the same contracts as the real subject and keeps a reference to it to delegate the operation before or after executing other actions.
- The pattern solves cases where you want to add logic without changing the functionality or intent of the original object.
- In the exchange rates example, repeated calls to a remote service generate unnecessary requests and worsen performance.
- The proposed solution is to load the data once, store it in cache for a time, and reuse it in subsequent calls.
- The caching proxy code implements `IExchangeRateService`, creates an internal `ExchangeRateService`, and stores the return value in `_exchangeRates`.
- If `_exchangeRates` already has data, the proxy returns the cache; if it does not, it calls the real service, stores the result, and then returns the data.
- The client only needs to start using `CachedExchangeRateService`, without changing the consumption logic.
- The article also mentions logging proxy, protection proxy, remote proxy, virtual proxy, and selection proxy as other uses.
- Among the cautions noted are extra complexity, maintenance cost, possible performance impact, difficulty synchronizing state, leaked abstraction, and risks of relying only on the proxy for security.
