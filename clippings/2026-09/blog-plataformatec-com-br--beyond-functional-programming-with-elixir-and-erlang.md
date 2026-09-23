---
url: "http://blog.plataformatec.com.br/2016/05/beyond-functional-programming-with-elixir-and-erlang/"
captured_at: "2026-09-23T16:42:36+01:00"
title: "Beyond Functional Programming with Elixir and Erlang « Plataformatec Blog"
domain: "blog.plataformatec.com.br"
---

I would like to add a slightly different perspective to functional programming in the Erlang VM: functional programming is not a goal in the Erlang VM. It is a means to an end.

When designing the Erlang language and the Erlang VM, Joe, Mike and Robert did not aim to implement a functional programming language, they wanted a runtime where they could build distributed, fault-tolerant applications. It just happened that the foundation for writing such systems share many of the functional programming principles. And it reflects in both Erlang and Elixir.

Therefore, the discussion becomes much more interesting when you ask about their end-goals and how functional programming helped them achieve them. The further we explore those goals, we realize how they tie in with immutability and the control of shared state, for example:

Fault-tolerance: if you have two entities in your software that work on the same piece of data and one of them fails (i.e. it raises an exception), how do you guarantee that the failed entity did not leave a corrupt state? In Elixir, you would isolate those entities into light-weight threads of execution called processes and guarantee their state is not shared (coordination happens over communication);

Concurrency: many of the issues in writing concurrent software in OO and imperative languages comes from managing shared mutable state. Since both sharing (via a global namespace) and mutability are the default mode of operations in those languages, it is harder to pinpoint the pieces of data that can get you in trouble. With immutability as a default, the mutable parts that you effectively need to focus on when writing concurrent software will stand-out and give developers more precision when tackling race conditions;

Maintainability: the foundation for writing more maintainable code in both Erlang and Elixir come from functional programming. Immutable data ensures the data no longer changes under our feet! Pattern-matching brings terseness, protocols introduce dynamic polymorphism backed by explicit contracts, etc.

The examples above are why I prefer, most of the time, to introduce Elixir as a language for building maintainable and robust systems. And while some of the functional semantics may differ between Erlang and Elixir (rebinding, pipelines, etc), they are still means to an end. Past that, the foundation for building fault-tolerance and distribution applications in both languages is precisely the same since they are both built on top of the same VM and the OTP platform.

That's not to say the functional aspect is not important. It definitely is! I often summarize functional programming as a paradigm that forces us to make the complex parts of our system explicit and that's an important guideline when writing software. Fortunately, many of the functional programming lessons can be applied to other non-FP languages and platforms.

However, other features in the Erlang VM are less portable. Concurrency must come from the ground-up. All languages are constrained by Amdahl's law and it is important to maximize the parallel portion of our applications. Writing concurrent code is simpler when the runtime provides efficient abstractions and developers have good tooling to reason about concurrency.

Fault-tolerance is even trickier as it cannot be applied only to parts of your application. The whole ecosystem must be built on top of the same principles otherwise the "weakest link in the chain" will always break.

If you are building services that are meant to run 24/7 and serve multiple clients (and most network services and web applications must do precisely this), you must choose a platform that provides concurrency, robustness, and responsiveness from the ground-up. You want to give the best user experience to as many users as possible.

More importantly, those concerns go much beyond the infrastructure point of view. Developers often associate performance and concurrency with their application throughput (how many requests it can serve per second), however, such capabilities also directly affect the programmer productivity. If code compilation is slow or your application takes long to boot or your test suite spans over minutes, they become hurdles the programmer must overcome daily to write code. Hurdles that could be addressed by a more efficient and concurrent runtime. After all, in 2016, almost everything you do in your programming environment must be using all cores available.

Here is a quick exercise: imagine you have a CPU-intensive test suite that takes 2 minutes to run using a single-core. If your machine has 4 cores, its execution time could be reduced ideally to 30 seconds. However, given it is unlikely for the whole suite to be CPU intensive and to run fully in parallel, if we assume a parallelization of 80%, our suite will still take roughly only 48 seconds long, which is 2.5 times faster.

A strong foundation guarantees your users will enjoy a more fluid and robust experience and also gives developers a more productive and joyful working environment. That's why tools such as Elixir's Mix puts a lot of effort into, not only running your tests asynchronously but also in compiling all of your code in parallel and as fast as possible. The abstractions that provide fault-tolerance also give developers a great deal of introspection into both production and development environments. The fact Erlang and Elixir were built with such concerns in mind is what makes them one of the best options out there for writing such systems.

I would like to thank Robert Virding for reviewing the article. Still, all opinions and inaccuracies are my own. 🙂
