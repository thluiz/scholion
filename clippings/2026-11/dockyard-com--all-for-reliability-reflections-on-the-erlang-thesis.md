---
url: "https://dockyard.com/blog/2018/07/18/all-for-reliability-reflections-on-the-erlang-thesis"
captured_at: "2026-11-16T03:51:37+00:00"
title: "All For Reliability: Reflections on the Erlang Thesis - DockYard"
domain: "dockyard-com"
---

![The Mehmed Paša Sokolović Bridge is a stone bridge in Višegrad, Bosnia and Herzegovina, and was completed in 1577. Photo by Torsten Muller, found at https://unsplash.com/photos/tfoqHmi-MOg](https://assets.dockyard.com/images/b9409088-b7e6-4530-b9df-472e894e2316-large.webp)

![Nathan Long](https://s3.amazonaws.com/dockyard-com-production/images/team-monster-08.png)

If you ask Elixir developers what got us interested in the language, many will say "concurrency." We wanted to make our programs faster by making them use more cores.

That desire is a big part of why Elixir exists. Before creating Elixir, José Valim was trying to make Rails thread-safe, and found it frustrating. He remembered thinking:

> "If the future is going to have \[many\] cores, we needed to have better abstractions, because the ones I had working with Ruby and Rails were not going to cut it. So I decided to study other languages and see what they were doing."

That study led him to Erlang, and he built Elixir to run on the Erlang virtual machine.

Similarly, [Chris McCord](https://dockyard.com/blog/authors/chris-mccord) wanted to use WebSockets in his Rails apps, but struggled to create a scalable solution in Ruby. Then he heard about WhatsApp using Erlang to get 1 million connections on a single machine.

> "That kind of blew my mind, because I was looking at getting maybe a hundred connections on my Rails app."

That got McCord interested in Erlang, then Elixir. He went on to create Elixir's main web framework, [Phoenix](https://phoenixframework.org/), known for sub-millisecond response times and massively scalable WebSocket support.

Personally, I worked on a travel search engine that needed to do a lot of on-demand concurrent work, but was written in a language that made that difficult. I learned about Elixir while at that job, and though we couldn't adopt it there, I knew it was a tool I'd want to use in the future.

But although he calls it a "concurrency-oriented programming language", Erlang co-creator Joe Armstrong does not cite speed as the main reason for its creation in his 2003 PhD dissertation, ["Making reliable distributed systems in the presence of software errors"](http://erlang.org/download/armstrong_thesis_2003.pdf). Its purpose is there in the title: reliability.

What's fascinating is how many of Erlang's (and therefore Elixir's) attributes are direct consequences of designing it to be reliable.

## Mistakes Are Inevitable

In the paper, Armstrong talks about the challenges his team faced in writing telephone switching systems in the 80s.

First, they needed to write complex systems, with "several millions of lines of program code", and might have teams with "many hundreds of programmers" of varying experience levels.

The requirements were demanding:

> Market pressure encourages the development and deployment of systems with large numbers of complex features. Often systems are deployed before the interaction between such features is well understood. During the lifetime of a system, the feature set will probably be changed and extended in many ways.

Under such constraints, there was no way they could produce perfect software.

Yet something approaching perfection was required. Telephone calls are important; some of them are emergencies. You can't turn off the phone system each night for maintenance. A telephone system needs "to be in continuous operation for many years", "typically having less than two hours of down-time in 40 years."

It's quite a problem! How can an imperfectly-written system get near-perfect results? Or as Armstrong puts it:

> The central problem addressed by this thesis is the problem of constructing reliable systems from programs which themselves may contain errors.

## Handling the Worst Case

Before solving the problem, Armstrong makes it harder by considering the worst case: hardware failure. Imagine a perfectly-written program running on a computer that bursts into flames.

There are a lot of failures from which a process can recover, but ceasing to exist is not one of them.

Armstrong addresses this situation simply.

> To guard against the failure of an entire computer, we need two computers.

Specifically:

> If the first computer crashes, the failure is noticed by the second computer, which will try to correct the error.

This might mean, for example, creating a new process elsewhere to replace the one that died.

Here we see the first interesting property of Erlang: it's made to run systems that span multiple machines, because that's what's needed for reliability.

Even better: **since the failure of one process must be corrected by another process when they're on separate machines, Erlang uses that mechanism for _all_ failures**. All failures are handled via "monitors" and "links", which are ways for one process to react to the failure of another, supported directly by the VM. (These mechanisms are the foundation for the supervision tools and patterns of OTP.)

In fact, the Erlang VM goes so far as to make hardware failures _look like_ software failures. If Process A is monitoring Process B and Process B dies, Process A is notified. This happens whether Process B divides by zero, loses connectivity, or dies in a fire; in the last two cases, the "distress call" is faked by the VM when it loses contact with Process B.

As Armstrong says:

> The reason for coercing the hardware error to make it look like a software error is that we don't want to have two different methods for dealing with errors... we want one uniform mechanism. This, combined with the extreme case of hardware error, and the failure of entire processors, leads to the idea of handling errors, not where they occurred, but at some other place in the system.

## Process Properties

Now consider the two processes mentioned above, running on separate machines. There are certain things we can be sure of.

*   They can't share memory because they're physically separated. This is nice, because a failing process can't corrupt the memory of the process that's watching it.
*   They can communicate only by passing messages.
*   They will succeed or fail independently.

This separation is analogous to a firewall. In construction, a "firewall" is a wall between two parts of a building that keeps fire from spreading. A maximally-safe house would have firewalls around every room, chair, and bed. In a house, this is impractical. But in an Erlang system, process boundaries are like firewalls for failures, and they cost almost nothing.

And again, for uniformity, these same "firewall-like" characteristics are true whether two processes run on separate machines or not. Processes on the same machine share no memory and communicate only by passing messages, just as if they were on separate machines.

( As Armstrong noted, Erlang's process isolation isn't perfect; if one process allocates an inordinate amount of memory or atoms, for example, it could crash the Erlang VM on that machine, including all its processes. )

To further improve reliability, several more properties are needed.

First, messages must be asynchronous. As Armstrong says:

> Isolation implies that message passing is asynchronous. If process communication is synchronous then a software error in the receiver of a message could indefinitely block the sender of the message, destroying the property of isolation.

Second, processes must be lightweight. If safety is increased by dividing a system into more processes, we'll want to run a lot of them, creating them quickly and on-demand.

And third, processes must take turns. As Armstrong says:

> Concurrent processes must also time-share the CPU in some reasonable manner, so that CPU-bound processes do not monopolise the CPU, and prevent progress of other processes which are "ready to run."

Like most operating systems, the Erlang VM uses "preemptive multitasking" ([more](https://happi.github.io/theBeamBook/#_scheduling_non_preemptive_reduction_counting) or [less](https://happi.github.io/theBeamBook/#_reductions)). This means that each process gets a fixed amount of time to use the CPU. If a process isn't finished when its turn is up, it is paused and sent to the back of the line, then another process gets a turn. It's also paused if it's waiting to read a file or get a network response.

In this way, the Erlang VM supports "non-blocking IO" as well as "non-blocking computation", both of which get applied automatically to sequential-looking code.

## Where Reliability and Performance Meet

You might have noticed that those last two points of reliability are also performance concerns. That's because the two are related.

Imagine a system that's handling a large number of small tasks - calls, web requests, or whatever. In comes a large task. What happens?

If the system's overall performance takes a dive, it's not reliable. Calls get dropped, web requests time out, and so on. A reliable system must perform consistently.

This is the logic behind the Erlang VM's multitasking. In absolute terms, frequent task-switching wastes a little time, making performance sub-optimal. But the benefit is that performance is consistent: small tasks continue completing quickly, while large tasks get processed a little at a time.

Garbage collection works this way, too. Although Erlang's immutable data means that a lot of garbage is created, it's divided into tiny heaps across many processes. When a process dies, its memory is freed, and GC isn't needed. For long-running processes, GC is performed concurrently. There are no "stop the world" pauses to collect garbage from the entire system, so GC is no barrier to consistent performance.

## Evidence for Reliability

After all this effort toward building reliable systems, Armstrong tried to find out how well several Erlang-based systems had worked; he interviewed the maintainers, analyzed the source code, and examined bug reports.

Armstrong has [elsewhere cited](https://pragprog.com/articles/erlang) Ericsson's ADX301 switch as an example of "nine nines" reliability - an uptime of 99.9999999%.

Here's how he describes the switch:

> The ADX301 is designed for "carrier-class" non-stop operation. The system has duplicated hardware which provides hardware redundancy and hardware can be added or removed from the system without interrupting services. The software has to be able to cope with hardware and software failures. Since the system is designed for non-stop operation, it must be possible to change the software without disturbing traffic in the system.

In his thesis, he treats the "nine nines" figure as uncertain:

> Evidence for the long-term operational stability of the system had also not been collected in any systematic way. For the Ericsson AXD301 the only information on the long-term stability of the system came from a PowerPoint presentation showing some figures claiming that a major customer had run an 11 node system with a 99.9999999% reliability, though how these figure had been obtained was not documented.

And that particular figure has been [the subject of some debate](https://stackoverflow.com/questions/8426897/erlangs-99-9999999-nine-nines-reliability).

However, Armstrong's investigations seemed to indicate that the Erlang systems he examined were indeed extremely reliable:

> The software systems in the case study are so reliable that the people operating these systems are inclined to think that they are error-free. This is not the case, indeed software errors did occur at run-time but these errors were quickly corrected so that nobody ever noticed that the errors had occurred.

## Performance After All

So here's a recap of what the Erlang VM gives us in pursuit of reliability:

*   Lightweight, shared-nothing processes that communicate via asynchronous messages
*   A built-in mechanism for processes to react to failures in other processes
*   The ability to quickly spawn a large number of processes and run them on multiple machines
*   Efficient context-switching and concurrent garbage collection

No wonder Armstrong calls Erlang a "concurrency-oriented programming language". These features, created mainly for reliability, make it easy to write concurrent programs that scale horizontally across cores and computers. You write your program using processes and messages, and the VM takes care of all the tricky parts - running a scheduler per core, giving each process its turn, moving processes between schedulers to balance throughput and power consumption, and so on.

Having tiny processes makes this easier. Armstrong once [described the ease of scheduling small Erlang processes vs larger operating system processes](https://youtu.be/bo5WL5IQAd0?t=16m5s):

> Packing huge big rocks into containers is very very difficult, but pouring sand into containers is really easy. If you think of processes like little grains of sand and you think of schedulers like big barrels that you have to fill up, filling your barrels up with sand, you can pack them very nicely, you just pour them in and it will work.

And of course, the Erlang VM _is_ pretty fast. As Armstrong [once joked in a conference talk](https://www.youtube.com/watch?v=ed7A7r6DBsM&t=33s):

> You take a program and you want it to go a thousand times faster, just wait ten years, and it goes a thousand times faster. So that's solved. If you want it a million times faster, you wait twenty years. So that problem's solved. And that's why Erlang's really fast today, because we waited a long time.

Erlang was created in the 1980s for telephones switches that handled "many tens of thousands of people" interacting simultaneously. As Armstrong implied, it rode the wave of ever-increasing chip speeds even as it [continued to be optimized](http://blog.erlang.org/beam-compiler-history/), so that its once-acceptable speed became truly formidable.

That wave has passed, and the future of performance is concurrency. To take advantage of it, we have to write concurrent programs. If Armstrong's thesis is correct, "concurrency-oriented programming" is also the key to reliability.

And it's awfully nice to get both at the same time.

### Stay in the Know

Get the latest news and insights on Elixir, Phoenix, machine learning, product strategy, and more—delivered straight to your inbox.

![Narwin holding a press release sheet while opening the DockYard brand kit box](https://assets.dockyard.com/images/narwin-press-release-og-v2.svg)
