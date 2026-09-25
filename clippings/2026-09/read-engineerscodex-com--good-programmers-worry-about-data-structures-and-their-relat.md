---
url: "https://read.engineerscodex.com/p/good-programmers-worry-about-data?ref=dailydev"
captured_at: "2026-09-25T20:23:20+01:00"
title: "Good programmers worry about data structures and their relationships"
domain: "read-engineerscodex-com"
---

_Engineer’s Codex is a publication about real-world software engineering._

I recently came across a quote by Linus Torvalds (creator of Linux and Git) in this [great Stack Overflow post](https://softwareengineering.stackexchange.com/questions/163185/torvalds-quote-about-good-programmer). (This post reviews many quotes from that post.)

It succinctly described a problem I’ve been working on recently:

> _"Bad programmers worry about the code. Good programmers worry about data structures and their relationships."_

Right before the above quote, Linus said:

> _git actually has a simple design, with stable and reasonably well-documented data structures. In fact, I'm a huge proponent of designing your code around the data, rather than the other way around, and I think it's one of the reasons git has been fairly successful \[…\] I will, in fact, claim that the difference between a bad programmer and a good one is whether he considers his code or his data structures more important._

Good data structures make code easier to design and maintain. It makes software more reliable, systems more understandable, and code more readable. When designing any software, application logic often follows the data model. Treating the data model as an afterthought results in more work down the line. The inverse is true also - having a well-thought out data model makes migrations and building on top of complex systems easier down the line.

When I read this quote, I actually was able to recognize countless examples in the past of this. I once worked on a project where we spent quite a while optimizing complex algorithms, only to realize that by restructuring our data, we could eliminate entire classes of problems. We replaced a 500-line function with a 50-line function and a well-designed data structure. Not only was the new code faster, but it was also much easier to understand and maintain. (Of course, then the problem also shifted “down the stack” to where the majority of toil was in restructuring existing data.)

Another relevant quote here is in _The Art of Unix Programming_: 

> Rule of Representation: Fold knowledge into data so program logic can be stupid and robust.
> 
> Even the simplest procedural logic is hard for humans to verify, but quite complex data structures are fairly easy to model and reason about. To see this, compare the expressiveness and explanatory power of a diagram of (say) a fifty-node pointer tree with a flowchart of a fifty-line program. Or, compare an array initializer expressing a conversion table with an equivalent switch statement. The difference in transparency and clarity is dramatic. See Rob Pike's Rule 5.
> 
> **Data is more tractable than program logic. It follows that where you see a choice between complexity in data structures and complexity in code, choose the former. More: in evolving a design, you should actively seek ways to shift complexity from code to data.**
> 
> The Unix community did not originate this insight, but a lot of Unix code displays its influence. The C language's facility at manipulating pointers, in particular, has encouraged the use of dynamically-modified reference structures at all levels of coding from the kernel upward. Simple pointer chases in such structures frequently do duties that implementations in other languages would instead have to embody in more elaborate procedures.

The **actionable tip here is to start with the data.** Try to reduce code complexity through stricter types on your interfaces or databases. Spend extra time thinking through the data structures ahead of time.

That’s not to say the _code isn’t important_. Obviously, everything is important - but it’s useful to have a strong high-level approach of how data will flow and how different components interact before going deeper into code-related details. 

It’s why one of the _Senior Engineer (L5)_ requirements (at least for FAANG) generally involves writing higher-level design docs for more complex systems (which includes driving team planning and building good roadmaps for medium-to-large features).

[Ryan Peterman](https://open.substack.com/users/38830210-ryan-peterman?utm_source=mentions) from [The Developing Dev](https://open.substack.com/pub/ryanlpeterman) wrote a great piece on the higher level of influence L5s generally have here:

[Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions) from [High Growth Engineer](https://open.substack.com/pub/highgrowthengineer) also wrote a great piece about getting to Senior Engineer:
