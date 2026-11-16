---
url: "https://gvaughn.github.io/2020/05/17/why_hot_deploys_are_cool.html"
captured_at: "2026-11-16T03:52:20+00:00"
title: "Why Hot Deploys are Cool"
domain: "gvaughn-github-io"
---

17 May 2020

by Greg Vaughn

I’ve become an unintentional nonconformist in the Elixir community because I LOVE hot deploys. I try to keep newcomers’ minds open to the possibility in light of all the others telling them hot deploys are worthless, but it’s tiring and I’m outnumbered, so I wrote a blog.

## A Brief History

I got involved in Elixir in 2013. I came via Java and C# and Ruby and Clojure, et. al., without any deep history with BEAM, but I found a depth of experience and wisdom in distributed systems that reinvigorated my interest in programming and has made me want to dig into Erlang history. I’ve read the writings and watched the videos from Joe Armstrong and Robert Virding about the history of the platform. This is a distilled version through my lens and any inaccuracies are my fault.

The government was going to charge Ericsson huge penalties for any downtime for phone switches, therefore the original Erlang team had a primary requirement of zero downtime. The core features enabling that are hot code loading (to upgrade software) and supervision across physical machines (in case of hardware failure). All other features (and limitations) can probably be traced to one of those two core features. The links and monitors that enable supervision are things we all use even within a single VM. Just as supervision is useful even without physical redundancy, perhaps there’s value in hot code loading even when we don’t require zero downtime.

## The Middle Ground

Let’s make a distinction between _relying_ on hot deploys and simply enjoying them. To rely upon them means to architect your system where it must remain running constantly. You pay for that up-time with more complex deploys. You’ll have to write and test custom appup/relup files and code\_changed callbacks for situations when you need to change your supervision tree and/or modify things stored in some long-running GenServer state. This is a daunting notion to get consistently correct and most people stop learning about hot deploys at this point, however, I find that 90% (or more) of my deploys do not require these sorts of changes. Most of my changes are to the logic in the plain modules called via the existing process supervision tree. Changing the structure of the tree itself is much less frequent.

Distillery automatically generates relup files that allows me to hot deploy plain modules “for free” over 90% of the time. As long as I ensure my system durably stores important data, refreshes caches properly at startup, etc. for the other 10% of cases, then I can use a full restart release. I’ve never written appup/relup files or code\_changed callbacks, yet I’ve been enjoying hot deploys for 3 years. I gain a lot of value for very little effort. Hot deploys are cool! They allow all the thousands of background tasks that are always running in my system to keep running without interruption. That’s quite convenient.

## Context Matters

There’s some of you who have been saying “but Docker …” to yourselves since reading the title of this blog. Docker (which I’ll use loosely as a proxy for containerization/orchestration in general) is the right organizational decision in certain contexts. Like all decisions, it has tradeoffs and one of the tradeoffs is to treat your various microservices in various languages at a common denominator level in order to streamline operational concerns. To someone working in the context of a company that has invested in that style of architecture, yeah, I can see the logic of deciding not to support hot deploys, even at the “middle ground” level. But there are other contexts and newcomers to Elixir shouldn’t immediately be assumed to be under those tradeoffs/constraints.

My current context is at a small startup that built upon Elixir from day one (though I have prior experience at larger, more perscriptive (micro)service oriented organizations too). Our system consists mostly of periodic background tasks we do on behalf of our customers. Our Phoenix component primarily displays status and allows for the occasional manual step. The UI is a small portion of our overall traffic. The problem domain matches the concurrency benefits Elixir and BEAM offer quite nicely. It’s not a conventional CRUD webapp, yet it is somewhat architecturally adjacent, and we do enjoy our 90% hot deploys.

## Newbie Advice

To those new to the Elixir (and BEAM) community, welcome! There’s going to be different ways of doing things here, and that can be frustrating, but try to remember there is a reason for the differences, even if you don’t immediately see them. Hot deploys probably shouldn’t be at the top of your list of things to delve into, but I encourage you to keep the idea in the back of your mind instead of completely writing it off. I suggest, when you’re ready, that you explore it on some side project, where you have few constraints. It will help you gain intuition of which contexts it is a good or bad fit for. At risk of getting too philosophical, that intuition of technology/technique to context is core to leveling up as a software developer.

tags: _elixir_ - _deployment_
