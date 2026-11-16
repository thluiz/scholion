---
url: "https://gvaughn.github.io/2020/08/08/beam_spoiled_me.html"
captured_at: "2026-11-16T02:12:09+00:00"
title: "The BEAM has Spoiled Me"
domain: "gvaughn-github-io"
---

8 August 2020

by Greg Vaughn

I’ve noticed changes in how I prefer to develop software since I’ve been focusing my career on Elixir. It allows me to think bigger thoughts and to develop with lower friction and less fear. I don’t want to go back.

## It Began with Fault Tolerance

Many people are introduced to Elixir because of its focus on concurrency. Joe Armstrong even called Erlang a “concurrency oriented” language. (Note: most of my points are generic to any BEAM language, but my experience comes from an Elixir perspective, so please excuse bias in my terminology). I find it helpful to consider concurrency a logical consequence of a more primeval concern: fault tolerance. Achieving BEAM-style fault tolerance comes from isolated processes which do not affect any other if they crash, plus a supervisory process being informed when another process dies.

The core point of processes is to contain the “blast radius” of damage caused by an error. It just so happens that the isolation qualities that enable that also make them great candidates for concurrency.

## “Let It Crash”

When I first heard the “Let It Crash” mantra of the Erlang community, it sounded crazy based on my prior development exerience. It’s important to understand that it is not a license for irresponsibility, or that we should not care about the system crashing. What it is, at the core, is a recognition that our systems will have errors (even _if_ we write bug-free code, hardware will bug us eventually) and that with an architecture of managing the “blast radius” of damage, then little parts of the system crashing are no longer a scary thing.

Less fear – yes, please! I’ve learned to write my Elixir code with a focus on “blast radius” as a driver for when to reach for processes. Even in cases where I don’t need concurrency, I’ll use a process to enclose the damage an error might cause. I use supervision trees and durable work queues to recover from those minor crashes of processes. I’ve learned to prefer upserts over inserts to allow my logic to be retried safely for greater idempotency. These two ideas of processes to enclose possible errors plus idempotency have become second nature to me in any Elixir code I write.

## Freedom

This automatic ability to recover from errors changes the complexion of topics like test coverage enforcement, static types, extensive code reviews, etc. All those, at heart, are about preventing errors from being introduced in the first place (yes, I recognize their secondary benefits too). Those are still good things (I am not advocating irresponsibility), but with the solid safety net of fault tolerance from BEAM, we are able to look at them from a different perspective and see that they do add some friction and inertia to delivering software. Perhaps we can temper our reliance upon them in favor of greater delivery speed in some circumstances. Less fear means more freedom to choose.

## Bigger Thoughts

Elixir re-ignited my intellectual interest in software development. I found, via Erlang and BEAM history in general, a huge body of wisdom in distributed systems that I can learn from, and new tools in my toolbox of how to think about software. With processes so lightweight, pervasive, and offering freedom from fear of crashing, my perspective shifted in exciting ways. If I think I’m writing a “web application” then my thoughts are immediately limited. I now think of building systems. I can think bigger thoughts because I have better abstractions to build them upon.

Some teams are happy to use Elixir to write web applications, to fit it into their pre-existing microservice deployment model. I urge developers to reach for those bigger thoughts that fault tolerant lighweight processes enable. You can consider each process a logical microservice, but you don’t need the friction of deploying it separately, and serializing to/from json, and containers, and orchestration, and distributed logging, et.al. You can deploy an entire system of millions of interacting logical microservices in a single BEAM release.

## Game Changer

Elixir and BEAM certainly have been a game changer for me. I’m more fearless when I build systems, and I hope I can share that freedom with others. The BEAM has spoiled me, but in a good way.

tags: _beam_ - _elixir_ - _introspection_
