---
url: "https://medium.com/@qertoip/elixir-obsoletes-ruby-erlang-and-clojure-in-one-go-605329b7b9b4"
captured_at: "2016-04-11T13:59:47-03:00"
title: "Elixir obsoletes Ruby, Erlang and Clojure in one go — Medium"
domain: "medium-com"
---

# Elixir obsoletes Ruby, Erlang and Clojure in one go

I’ve been a happy Ruby programmer and evangelist since 2005. Also, a Clojure fan and minor project donor around 2008–2010. I have also shortly flirted with Erlang in 2007 to learn about its unmatched concurrency model and neanderthal syntax.

Recently I’ve come to conclusion all these languages are now obsolete.

In a surprising twist [Elixir](http://elixir-lang.org/) supersedes all of them by delivering extremely well thought out mix of characteristics and features.

#### Programmer Happiness and Productivity

Most importantly, Elixir is designed for programmer happiness, stealing Ruby’s main selling point.

Forget Erlang VM for a while: Elixir is simply **the first language since Ruby** to really care about code beauty and UX of the language, libraries and ecosystem. Whether Elixir’s UX is slightly better or still slightly worse than Ruby’s is a matter of a debate. The thing is, it is definitely in the same league and should be (at least!) acceptable for a demanding Ruby programmer.

In fact, Elixir was invented by a well recognized Ruby programmer José Valim.

#### Ultimate Concurrency Story for Real-Time Web and Internet of Things

Why care about massive concurrency in the first place? Rails apps we’ve been writing for the last ten years work just fine… Except they don’t once we enter the real-time web era.

RT and IoT bring entirely new requirements for server infrastructure. We are now expected to keep multiple permanently open connections **for each and every client** (like a browser tab or a mobile app). Even for the relatively small apps we can be very quickly out of OS threads.

Until recently Node.js was realistically the only tech used to achieve over 10K connections on a commodity hardware. Elixir changes the scene dramatically. Not only Elixir scales better than Node.js — it also doesn’t suck.

Elixir is built on BEAM, the famous Erlang VM. Elixir apps natively employ multiple servers, processors, cores and threads. Servers-to-threads, programmer is offered the same, consistent, clean and non-leaking concurrency abstraction — the Actor Model.

Erlang VM allows you to enjoy full concurrency without unwieldy async IO. In Elixir you **can do synchronous IO** if you want. You can fearlessly commit a VM process to it without penalty. Erlang VM will free the underlying OS thread to serve other VM processes.

#### Functional yet practical

Elixir is among the most practical functional languages to date. It cherry-picked some of the best Clojure features — efficient, immutable data structures, optional lazy evaluation, protocols and records/structs. Contrary to Clojure it also enjoys true tail call optimization and the pipeline operator. Finally, it has a pleasant, modern, Ruby-like syntax, a rare gem among functional languages.

#### Full macro system

Elixir is close to being homoiconic. Everyday syntax is a just bit of sugar on top of Elixir data structures. The way from code to its representation is direct and clear. Elixir supports full macros known from Lisp and Clojure without the torture of parentheses-driven syntax.

#### Summary

Why would you choose Ruby over Elixir? Certainly mature libraries give Ruby huge productivity boost and are the only possible reason to still consider Ruby over Elixir. But it gets less relevant every day as Elixir packages pop-up like gems in Ruby’s golden era. What about Rails? Well, there is an excellent [Phoenix](http://www.phoenixframework.org/) contender.

Why would you choose Clojure over Elixir? It’s really hard to justify except when you need to run on JVM for other reasons.

Why would you choose Erlang over Elixir? You wouldn’t. Elixir is an almost-strict superset of Erlang’s offering.

This is why I firmly believe Elixir obsoletes Ruby, Clojure and Erlang in one go.
