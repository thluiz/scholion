---
url: "https://dev.to/jamesmh/essential-senior-dev-skill-solving-problems-with-patterns-1jp5"
captured_at: "2026-11-16T18:54:08+00:00"
title: "Essential Senior Dev Skill: Solving Problems With Patterns"
domain: "dev-to"
---

Let's continue with the "Stages Of Your Software Development Career" series!

I find the senior developer career stage one of the most interesting because there are so many different skill sets and targeted focuses that senior developers can have.

## [](#recap-of-the-last-article)Recap Of The Last Article

Last time, we looked at topics like:

*   Who's a senior developer?
*   What's an indicator of being a senior developer?
*   Some traits of senior developers
*   How experience plays a role
*   What scope of skills senior developers should focus on
*   Other various tips

## [](#intro)Intro

I want to dive into an important point I made last time (worded a bit differently):

_**An essential skill you must have is the ability to view potential problems as a series of patterns that have already been solved somewhere else.**_

This is essential if you want to become a senior developer.

Not a senior developer in title alone, but in skills and competence!

A big part of growing in your career is learning about more tools, techniques and patterns that enable you to solve more difficult problems and solve them more efficiently.

This will help you build trust, reputation, respect, etc. which will eventually lead to more career progress and options.

## [](#design-patterns-in-real-life)Design Patterns In Real Life?

Let's look at the classic [software design patterns](https://sourcemaking.com/design_patterns).

Design patterns are (usually) not meant to be something you use up-front when creating software. **They are designed specifically as solutions to specific problems you might face in your software's architecture/structure, behaviour, etc.**

## [](#adapter)Adapter

The adapter pattern, for example, is used _when you have two or more different interfaces which need to communicate or be integrated with each other._

In real life, this works much like an adapter for a socket wrench.

Well....it's actually the exact same thing!

This is actually a very important point: **the adapter pattern doesn't only apply to code/software!**

In fact, all these patterns aren't just for software design!

We see it being used in a physical sense with the socket wrench, with USB adapters that allow our mobile phones to communicate with our computers, etc.

_Note: It's also similar to the [Anti-Corruption layer](https://docs.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) concept found in [Domain Driven Design](https://amzn.to/2NoG2AW)._

## [](#facade)Facade

Let's take another.

The facade pattern is used _when you want to simplify a complex system/interface._

For example, the process for submitting an order in some web app might involve a complex series of steps to occur.

We can "wrap" the process into a one method call that will give the client a really simple way to execute that process.

Just like with Amazon or eBay, they might have a "one-click buy" feature which will automatically run you through the steps required to purchase.

_This is a facade._

This pattern can also be applied to more "real world" contexts like automobiles. Using a manual transmission involves knowing how to use the clutch, how to use one of your hands to shift the transmission stick at the same time, keeping your eyes on the road while doing it, etc.

However, most cars today do all of this automatically for you (I suppose that's why they are called _automatic transmissions?_ 😜).

This is the same kind of pattern but applied in a non-software oriented context.

The underlying pattern is about simplifying how a client interacts with your product - regardless of what domain it's applied to (software, automobiles, etc.)

## [](#systems-thinking)Systems Thinking

This idea of using common patterns to solve problems in different domains and contexts is sometimes called "systems thinking".

[Scott Hanselman has also recently blogged a bit about this idea](https://www.hanselman.com/blog/SystemsThinkingAsImportantAsEverForNewCoders.aspx).

By understanding the fundamentals around building systems and the patterns that can be used to solve problems, **you can become someone who can bring value to businesses no matter where you are placed!**

* * *

P.S. This article is originally from [YourDevCareer.com](https://yourdevcareer.com/) where you can check out more articles and resources to help accelerate your career growth!

* * *

## [](#a-real-example)A Real Example

A conversation I was in recently involved some performance issues with a legacy application running in .NET.

One of the issues we discussed was around degraded system performance under a high load.

The overall problem is that the system doesn't have enough "workers" to handle many HTTP requests all-at-once.

The immediate solution offered by a co-worker was "we need another server so we can use load balancing."

_This solution adds a new node/server and places a middleman between them and the client. Kinda like [the mediator pattern](https://sourcemaking.com/design_patterns/mediator)?_

However, my response was that the best (and cheapest) fix is to address the fact that all database I/O in that system is synchronous.

If we make all those I/O operations asynchronous, then those threads will become available to handle any new HTTP requests while the database is working in the background.

_This solution, at a low-level, uses [the futures/promises pattern](https://en.wikipedia.org/wiki/Futures_and_promises)._

**But at a higher level, it's the same solution that you use when baking in a recipe!**

## [](#efficient-cooks-dont-need-a-master-chef)Efficient Cooks Don't Need A Master Chef 🤔

The solution of adding a middleman and more nodes, instead of making the workers you have more efficient, would be like adding a master chef to your kitchen and also hiring another person who you can delegate tasks to.

While one worker is staring at the oven while it bakes, the chef will order the other worker to make the frosting.

_Sound like some companies you've been in?_ 😂

However, if the one cook you have is already working at a high-efficiency then you might actually need to introduce another worker and possibly a master chef to delegate tasks.

But, if that one worker isn't working efficiently, then you probably want to make him/her as efficient as possible first, before hiring more employees (just like making your threads more efficient using async I/O).

Hopefully, this example and the kitchen type of analogy can help you see how there are these overarching patterns and techniques that can be applied in technical and non-technical contexts.

## [](#with-knowledge-comes-great-power)With Knowledge Comes Great Power

Part of the issue though, in this case, is understanding the root problem.

Sometimes, even when we know the real problem we may not be aware of the fact that there exists a specific pattern to solve it.

My co-worker, for example, is aware that the database I/O is synchronous. But perhaps was unaware of the fact that there is a more efficient method.

In the absence of a solution, the thought process has to move up to a higher level and apply a less-efficient solution.

**It's essential to learn about design and system patterns at least to the point where you know what problems have solutions!**

You don't need to know how to implement design patterns, **but you better know what problems they solve.**

Once you come across that problem, you'll remember, _"Oh ya, there's a pattern for that I remember reading about..."_ 👌

## [](#some-more-deep-dives)Some More Deep Dives

Let's take a look at a couple more examples and see what familiar patterns apply.

## [](#example-requesting-a-restaurant-meal)_Example: Requesting A Restaurant Meal_

_[Queues](https://docs.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling)_:  
When taking your order, the waiter might place your order into a queue since the cooks are busy with other orders right now.

_[Chain of responsibility](https://sourcemaking.com/design_patterns/chain_of_responsibility) / [Pipes](https://docs.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters)_:  
There may be a series of cooks who need to look at the order, complete their part, and then pass it on to the next cook who can spice it up, garnish it, etc.

_Master-slave_:  
The chef might assemble a complete meal from the individual dishes the lower-cooks made.

## [](#example-banking-transactions)_Example: Banking Transactions_

_Ledger / Append-only / [Event Sourcing](https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)_:  
When banks deal with account transactions they never erase a previous event or transaction.

For example, if PayPal mistakenly pays you $100, they won't "erase" that transaction. They will issue a corresponding counter-transaction (e.g. take $100 back from you). Even though both parties have the same amount of money they started with, the transactions themselves remain.

This is quite different than the typical CRUD type applications most companies build. These usually just store the current state of the system.

But this type of append-only pattern addresses problems in a system that needs:

*   Ability to audit all actions performed on the system
*   Ability to responsibly manage shared resources (like money) between multiple external parties
*   Ability to perform analytics across trends in the system (since you have recorded every event in the system)
*   Ability to query the system at specific instances of time

_[Sagas](https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part/) / [Distributed Transactions](https://docs.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction#example)_:  
When you do something like an interact e-transfer (e.g. I want to send money to my mother who is with a different bank altogether), there involves an inherent overall "transaction" (like a database transaction).

Except, this spans multiple systems (your bank, another external person's bank, other third-parties, etc.)

If you send $100 to your mother, then:

1.  It is "taken out" of your account (at least, you don't see it).
2.  Your mother has 30 days (or whatever) to accept the money.
3.  If she does, great!
4.  If not, then your bank has to perform some kind of [compensating action](https://docs.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction#example) (e.g. Put the money back into your account.)

If any step fails, you want to make sure the money is put back to the correct place. You don't want to lose data! That would mean lost money 😯.

There is a complex series of steps involved that aren't tied to a specific database or even a specific system, yet needs to be part of a consistent database-like transaction to ensure your money either gets to your mother or eventually comes back to your account.

Known as distributed transactions (i.e. transactions that span multiple systems), there are specific patterns that help deal with these kinds of scenarios - like [the saga pattern](https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part/).

That's quite a bit advanced but worth looking into if you're interested.

## [](#more-resources)More Resources

I hope you've learned something new that will help you think about solving business and technical problems in new ways!

The main point to remember is that **you don't need to know how to implement these patterns, but simply know that they exist and what kinds of problems they solve.** You can become a superhero if you can intervene when, for example, designing a system and saying, _"Hey, I remember there was a pattern that solves this already! Let me find it..."_

If you want to dig into some of these more "senior" level topics and areas around systems patterns, here are some resources I've found the most helpful in my own career.

**Free**:

*   [An awesome free collection of system patterns that are written for architecting Azure applications](https://docs.microsoft.com/en-us/azure/architecture/guide/) - These are general enough to be _very_ helpful.
*   Jimmy Bogard ([blog](https://jimmybogard.com/) and [YouTube](https://www.youtube.com/results?search_query=jimmy+bogard))
*   Udi Dahan ([blog](http://udidahan.com/articles/) and [YouTube](https://www.youtube.com/results?search_query=udi+dahan))
*   [Martin Fowler](https://martinfowler.com/tags/)

**Books**:

*   [Patterns of Enterprise Application Architecture](https://amzn.to/2XksZFf) - Full of small practical techniques and patterns that can help when dealing with large or complex codebases and systems.
*   [Building Microservices: Designing Fine-Grained Systems](https://amzn.to/2Xi76Sj) - Probably the best primer on distributed systems I've read. It's not super in-depth into any particular area, but deep enough that you'll learn tons about how to design and think about more complex systems and problems.
*   [Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions](https://amzn.to/2xrv6HW) - More of an advanced look at specific patterns around distributed systems. Focuses on patterns you can use to reliably build complex business processes and integrate separate systems together with more advanced messaging techniques.

## [](#was-this-helpful)Was This Helpful?

If you enjoyed this, please share on Twitter, Reddit, etc. so more devs can benefit from the content 👍.

## [](#keep-in-touch)Keep In Touch

Don't forget to connect with me on:

*   [Twitter](https://twitter.com/jamesmh_dev)
*   [LinkedIn](https://www.linkedin.com/in/jamesmhickey/)

You can also find me at my web site [www.jamesmichaelhickey.com](https://www.jamesmichaelhickey.com/).

## [](#navigating-your-software-development-career-newsletter)Navigating Your Software Development Career Newsletter

An e-mail newsletter that will help you level-up in your career as a software developer! Ever wonder:

✔ What are the general stages of a software developer?  
✔ How do I know which stage I'm at? How do I get to the next stage?  
✔ What is a tech leader and how do I become one?  
✔ Is there someone willing to walk with me and answer my questions?

Sound interesting? [Join the community!](https://eepurl.com/gdIV5X)
