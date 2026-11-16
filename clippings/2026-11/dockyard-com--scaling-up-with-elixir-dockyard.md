---
url: "https://dockyard.com/blog/2020/05/28/scaling-up-with-elixir"
captured_at: "2026-11-16T03:51:24+00:00"
title: "Scaling Up With Elixir  - DockYard"
domain: "dockyard-com"
---

![White arrow pointed up painted on blue concrete](https://assets.dockyard.com/images/White%20arrow%20pointed%20up%20painted%20on%20blue%20concrete-large.webp)

![Nathan Long](https://s3.amazonaws.com/dockyard-com-production/images/team-monster-08.png)

It's exciting when your website or platform gets a spike in traffic -- that is, unless it fails. A disappointing web experience can quickly encourage new users to look elsewhere for an alternative that is faster and more responsive to their needs.

There are many facets to making web experiences scalable and reliable, including infrastructure, database design, and code optimization. One important factor is how your code handles concurrency -- that is, its ability to juggle multiple tasks at once (read more about concurrency [here](http://nathanmlong.com/2017/06/concurrency-vs-paralellism/)). And as many companies have shown, for concurrent programming, you can't beat the Erlang virtual machine.

The Erlang VM was originally built to power ultra-reliable devices like telephone switches, a job it's been doing admirably for decades. As internet services experienced higher traffic and became more critical, developers began to realize that the problems they were having had already been solved in Erlang and they began adopting it.

For example, you may have heard that [90% of all internet traffic goes through Erlang-controlled nodes](https://www.youtube.com/watch?v=077-XJv6PLQ), with Cisco alone shipping 2 million devices a year that use Erlang. Or that [WhatsApp scaled to serve 900 million users with an Erlang service written by just 50 engineers](https://www.wired.com/2015/09/whatsapp-serves-900-million-users-50-engineers/).

In recent years, the Elixir language has provided an extremely productive way to write code for the Erlang VM. Success stories include Discord, which [scaled its Elixir-based video and chat platform to 5 million concurrent users with Elixir alone](https://blog.discord.com/scaling-elixir-f9b8e1e7c29b), and later to [11 million concurrent users by pairing Elixir and Rust](https://blog.discord.com/using-rust-to-scale-elixir-for-11-million-concurrent-users-c6f19fc029d3). They also include Bleacher Report, which [handled 1.5 billion page views per month and sent out more than 3 billion push notifications per month using just five servers](https://www.techworld.com/apps-wearables/how-elixir-helped-bleacher-report-handle-8x-more-traffic-3653957/).

Elixir is at the heart of DockYard's approach to writing scalable web services, too. For example, DockYard helped [POA network](https://www.poa.network/) index millions of Ethereum blockchain transactions at faster-than-realtime rates, with smart usage of concurrency, batching, and upserts into a well-tuned PostgreSQL database.

So, how do Elixir and the Erlang VM help us build scalable systems?

## Concurrency-Oriented Programming

A scalable system is one that can cope with a growing workload. For a web service, that means handling many requests at once. Picture a busy call center. To handle more calls, you need more agents.

In computing, those agents are known as processes and threads. Most programming languages rely on the operating system to create processes and threads and to ensure that each gets its fair share of CPU time.

OS processes are robust but expensive, so you have to carefully budget how many you create. OS processes can create threads, which are cheaper but more error-prone due to the need to coordinate their access to the memory they share. Multithreaded programming is a notorious source of tricky bugs.

By contrast, Erlang was built as a "concurrency-oriented programming language." The Erlang VM can create and manage its own lightweight, internal processes, and was designed to run millions of them. Erlang processes are lighter weight than threads, but independent like OS processes, so they can't corrupt one another's data. Instead of sharing memory, they use message passing to coordinate their work.

The Erlang VM runs multiple schedulers -- one per CPU core -- and ensures that its processes are efficiently spread across them. This means you get the full benefit of that multi-core server. Also, if a process runs long enough to need garbage collection (and many do not), other processes do not have to pause while that happens.

Due to their isolated nature and the way they're scheduled, Erlang processes have some powerful features:

*   **Non-blocking IO**: when a process needs to do input or output -- like reading from or writing to a file or database or making a network request -- that process can go to sleep while it waits for a reply, letting other processes get work done in the meantime.
*   **Non-blocking computation**: when one process gets stuck with a heavy workload, the Erlang scheduler ensures that it performs that work in bursts; between them, other processes get a chance to run. So a small number of expensive requests can't bog down the whole system.
*   **Error isolation**: if an error occurs in one process, it can fail or be restarted without other processes being affected at all. If need be, other processes can be notified and react accordingly.

**Erlang processes are a game-changer**. Picture a call center where every time a phone rings, a new agent appears to answer it. Incoming web request? Spawn a process. Have an email to send? Spawn a process. Need to make an API call, query a database, or perform a calculation? Spawn a process.

Erlang processes can even be spread over multiple nodes, cooperating and coordinating as if they were all on the same machine.

## Superpowers Applied

Besides being directly useful, Erlang processes are the foundation of some of Erlang and Elixir's most exciting tools. For example:

*   The [Cowboy web server](https://github.com/ninenines/cowboy) spawns a process for every incoming web request, which keeps errors or heavy work in one request from affecting others.
*   The [Phoenix web framework](https://www.phoenixframework.org/), created by DockYard's [Chris McCord](https://dockyard.com/blog/authors/chris-mccord), uses Cowboy and gets this behavior for free.
*   [Phoenix Channels](https://hexdocs.pm/phoenix/channels.html) use an Erlang process per websocket connection, enabling soft real-time communication with [millions of connected clients from a single server](https://www.phoenixframework.org/blog/the-road-to-2-million-websocket-connections). Scalable push notifications are a necessary part of chat applications, multiplayer games and IoT services, but are also important for any site with real-time notifications, like booking and auction sites which tell you how many other users are viewing an item right now. Channels can communicate with in-browser JavaScript, native phone apps, or custom hardware.
*   [Phoenix LiveView](https://github.com/phoenixframework/phoenix_live_view) lets us build rich, interactive browser applications without any custom JavaScript and using a fraction of the development time you'd typically need when pairing an API and front-end framework. It uses Phoenix Channels to track application state and handle events server-side, pushing fast, tiny updates to the client. See [this short, exciting demo](https://www.phoenixframework.org/blog/build-a-real-time-twitter-clone-in-15-minutes-with-live-view-and-phoenix-1-5) and [these Phoenix Phrenzy contest entries](https://phoenixphrenzy.com/results) for a taste of what it can do.

When you build with LiveView, you can be confident that it's scalable because of the foundation it builds on. LiveView scales well because [Phoenix Channels scale well](https://dockyard.com/blog/2016/08/09/phoenix-channels-vs-rails-action-cable), and channels scale well because they're built on Erlang processes.

As Saša Jurić has explained, building a system on Erlang processes is like building [on solid ground](https://www.youtube.com/watch?v=pO4_Wlq8JeI).

## Simpler Stacks

When your core technology can do so much, you need fewer pieces to build a system.

You can use a library to manage background jobs. Or you can spawn Task processes in Elixir.

You can use Redis for short-term state. Or you can use an Agent or GenServer.

You can use a third-party service for push notifications. Or you can use Phoenix Channels.

You can write an API that goes hand-in-hand with your custom React front end. Or you can write an interactive site with LiveView.

What you use depends on your requirements and experience, but there's a lot of potential to simplify your tech stack. And fewer pieces means less complexity to manage -- something that any team can appreciate.

## Icing on the Cake

Besides the inherent advantages that come with Erlang processes, the Elixir ecosystem has some great performance and scalability features built in to common tools.

*   Phoenix has a tiny memory footprint and can happily run on a Raspberry Pi Zero as the interface of a [Nerves](https://www.nerves-project.org/) project.
*   Phoenix template rendering is blazing fast, [based on its usage of nested "io lists."](http://nathanmlong.com/2016/11/elixir-and-io-lists-part-2-io-lists-in-phoenix/) Where other frameworks need complex template caching to ensure snappy rendering, "Phoenix automatically and universally applies this simple view caching strategy: the static parts of our template are always cached. The dynamic parts are never cached. The cache is invalidated if the template file changes. The end." This strategy especially shines when you want to personalize content for every user.
*   [Ecto](https://github.com/elixir-ecto/ecto) makes it nearly impossible to write N+1 queries, and leans on database constraints to ensure consistent data under high load.
*   Tools like Erlang's Observer and [Phoenix Live Dashboard](https://github.com/phoenixframework/phoenix_live_dashboard) (built with many contributions from DockYard's [Michael Crumm](https://dockyard.com/blog/authors/michael-crumm)) give us built-in observability to diagnose bottlenecks and slowdowns in production.
*   When raw computation speed is paramount, [Rustler](https://github.com/rusterlium/rustler) (created by DockYard's Hans Elias Josephsen) lets us safely delegate to Rust code.

To be clear, Elixir is no silver bullet. Writing scalable software always requires thought and care.

But with Erlang processes as a solid foundation and so many important pieces in place, the Elixir ecosystem is a wonderful place to build scalable, reliable software.

And here at DockYard, we'd love to show you how.

## Learn More

_[DockYard](https://dockyard.com/) is a digital product agency offering custom software, mobile, and web application development consulting. We provide exceptional professional services in strategy, user experience, design, and full stack engineering using Ember.js, React.js, Ruby, and Elixir. With a nationwide staff, we've got consultants in key markets across the United States, including San Francisco, Los Angeles, Denver, Chicago, Austin, New York, and Boston._

### Stay in the Know

Get the latest news and insights on Elixir, Phoenix, machine learning, product strategy, and more—delivered straight to your inbox.

![Narwin holding a press release sheet while opening the DockYard brand kit box](https://assets.dockyard.com/images/narwin-press-release-og-v2.svg)
