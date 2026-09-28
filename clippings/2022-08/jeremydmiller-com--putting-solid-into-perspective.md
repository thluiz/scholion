---
url: "https://jeremydmiller.com/2022/08/10/putting-solid-into-perspective/"
captured_at: "2022-08-16T11:31:23-03:00"
title: "Putting SOLID into Perspective – The Shade Tree Developer"
domain: "jeremydmiller-com"
---

# Putting SOLID into Perspective

[jeremydmiller](https://jeremydmiller.com/author/jeremydmiller/ "Posts by jeremydmiller") 

[Software Design](https://jeremydmiller.com/category/software-design/) 

August 10, 2022August 10, 2022 
11 Minutes

*This is the 3rd part of multi-part series where I’m formulating my thoughts about an ongoing initiative at [MedeAnalytics](https://medeanalytics.com/). I started with a related post called [On Giving Technical Guidance to Others](https://jeremydmiller.com/2022/08/08/on-giving-technical-guidance-to-others/) that’s a synopsis of an impromptu lecture I gave our architecture team about all the things I wish I’d known before becoming any kind of technical leader.* *The first post was [What Is Good Code?](https://jeremydmiller.com/2022/08/09/what-is-good-code/) where I attempted to put a marker down on the inherent qualities we want in code before bothering to talk about ways to arrive at “good code.” As time permits, I’m training a rhetorical double barreled shotgun at the Onion or Clean architectures next in an attempt to see those completely banned in my shop, followed by some ranting about database abstractions.*

I think many people have put the old [SOLID Principles](https://en.wikipedia.org/wiki/SOLID) on a pedestal where the principles are actually rules. “SOLID as rules” has maybe become the goto standard for understanding or defining what is good code or architecture for a sizable segment of the software development community. I’ve frequently heard folks say that they “write SOLID code,” but even after having been exposed to these principles for almost 20 years I have no earthly idea what that really means. I even had a functional programming advocate tell me that I could use SOLID with functional programming, and I have even less of an idea about how 30 year old rules specific to class oriented programming have any relevance for FP other than maybe as a vague notion toward writing cohesive code.

Dan North recently made a [tongue in cheek presentation saying that each SOLID principle was wrong](https://dannorth.net/2021/03/16/cupid-the-back-story/) and that you should just write simple code — whatever the hell that means.

As the section title says, I think we need to put the SOLID principles into a bit of perspective as neither a set of authoritative rules that can be used in isolation to judge the worthiness of your code nor something that is completely useless or wrong. Rather than [throw the baby out with the bathwater](https://en.wikipedia.org/wiki/Don%27t_throw_the_baby_out_with_the_bathwater), I would describe the SOLID principles as a sometimes helpful *heuristic*.

> *Heuristics are methods or strategies which often lead to a problem solution but are not guaranteed to succeed*.
>
> <https://www.simplypsychology.org/what-is-a-heuristic.html>

Rather than a hard and fast rule, the SOLID principles can be used as a mental tool to think through the consequences of a coding design or to detect potential problems seeping into your code. One of the realizations I’ve made over the years is that there’s a wide variance in how developers think about coding problems and the types of techniques that fit these different mental models. I find SOLID to be somewhat useful, while others find it to be a stuffy set of rules that bear no resemblance to anything they themselves think about in terms of quality code.

Let’s run through the principles and I’ll do my best to tell you what I think they mean and how applicable or useful they are:

**Single Responsibility Principle** (SRP) — “There should never be more than one reason for a [class](https://en.wikipedia.org/wiki/Class_(computer_programming)) to change.”

It’s really a restatement of the quality of cohesion, which I certainly think is important. As many others have pointed out over the years though, this is vaguely worded, prone to a wide range of interpretation, and frequently leads to idiotic, masturbatory “how many Angels can dance on the head of a pin” arguments about how finely sliced the code should be and what a “responsibility” actually is. I think this is really a “by feel” kind of test and very highly subjective.

Another old rule of thumb is to just ask yourself if every responsibility of a piece of code directly relates to its name. Except that also starts another argument about what exactly is a responsibility. Sigh, let’s move on for now, but in a later section I will talk about Responsibility Driven Design as an actually effective way to decide on what a responsibility actually is.

**Open Closed Principle** (OCP) — “Software entities … should be open for extension, but closed for modification.”

I wrote [an article about this way, way back in 2008 for MSDN](https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/june/patterns-in-practice-the-open-closed-principle) that I think is still relevant. Just think on this for a bit, is it easier to go in to make modifications to some existing code to add new behavior or change the way it works today, or to write all new code that’s relatively decoupled from existing code and hence your new code will have fewer potential unintended side effects? I think this comes up much more in designing software frameworks than day to day feature code, but it’s still something I use as a consideration putting together code. In usage it’s just looking for ways to structure your code in order to make the addition of new features be mostly done by adding all new code files.

Consider building a web API of some sort. If you use an MVC framework like ASP.NET Core MVC that can auto-discover new `Controller` methods at startup time, you’re able to add new APIs without changing the code in other controller files. However, if you’re naively using a Sinatra-flavored approach, you may have to continuously break into the same routing definition file to make changes for every single new API route. The first approach is “OCP-compliant”, but the second approach could easily be considered to be simpler, and hence better in many cases.

Once again, OCP is a useful tool to think through possible designs in code, but not really any kind of inviolable rule. Moreover, I’d say that OCP more or less comes out a lot of time as “pluggability,” which is a double-edged sword that’s both helped and hindered anyone who’s been a developer for any length of time.

**Liskov Substitution Principle** (LSP) — “Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it.”

A casual reading of that will just lead you to a restatement of [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)), which is fine I guess, but doesn’t really help us necessarily write better code. Going a little deeper I’d say that what is important is that the client code for any interface or published API should not be making any assumptions about the underlying implementation and therefore less likely to break if using a new implementation of the same interface. If you want another way to think about this, maybe the [leaky abstraction anti-pattern](https://en.wikipedia.org/wiki/Leaky_abstraction) is an easier heuristic.

**Interface Segregation Principle** (ISP) — “Clients should not be forced to depend upon interfaces that they do not use.”

I mostly interpret this as another way to say [Role Interface](https://www.martinfowler.com/bliki/RoleInterface.html), which is an exhortation to make interfaces be focused to just the needs of a client and only expose a single role to that client. I do pay attention to this in the course of my work on OSS projects that are meant to be used by other developers.

You could make the case that ISP is somewhat a way to optimize the usage of [Intellisense](https://code.visualstudio.com/docs/editor/intellisense) or code completion features for folks consuming your API in an IDE, and I think that’s a perfectly valid goal that improves usability.

As an example from my own work, the [Jasper project](https://jasperfx.github.io/) has an important interface called [IExecutionContext](https://github.com/JasperFx/jasper/blob/master/src/Jasper/IExecutionContext.cs) that currently contains some members meant to be exposed to Jasper message handler code. And it also currently contains some members that are strictly for the usage of Jasper internals and could cause harm or unintended consequences if used inappropriately by developers using Jasper in their own code. ISP suggests that that interface should be changed or split up based on intended roles, and in this particular case, I would independently agree with ISP and I definitely intend to address that at some point soon.

I see ISP coming up far more often when building infrastructure code, but occasionally in other code just where it’s valuable to separate the interface for mutating an object and a separate interface for consumers of data. I’ve never understood why this principle made the SOLID canon when more important heuristics did not — other than the authors really needed to say “[Pat, I’d like to buy a vowel](https://simplify101.com/organizing-blog/pat-id-like-to-buy-a-vowel/)” to make the acronym work.

**Dependency Inversion Principle** — “Depend upon abstractions, [not] concretions.”

For some background for those of you who stumble into this and have no idea who I am, I’m the author of [StructureMap](https://structuremap.github.io/), the original, production capable IoC tool in the .NET ecosystem (and its modern successor [Lamar](https://jasperfx.github.io/lamar)) — the one single development environment that most embraced IoC tools in all their glory and folly. By saying all of this, you would expect me to be the one person in the entire world who would [go to bat](https://www.dictionary.com/browse/go--to--bat--for#:~:text=Take%20the%20side%20of%2C%20support,Slang%3B%20early%201900s%5D) for this principle.

But nope, I’m mostly indifferent to this other than I probably follow it mostly out of inertia. Sometimes it’s absolutely advantageous to build up an interface by developing the client first, then happily generate the concrete stubs for the interface with the IDE of your choice. It’s of course valuable to allow for swapping out implementations when you really do have multiple implementations of a single interface. I’d really urge folks though to avoid building unnecessary abstractions for things like domain model types or message bodies.

To sum up the principles and their usefulness:

- **S**RP — Separation of concerns is important in code, but the SRP is too vaguely worded by itself to be hugely helpful
- **O**CP — It’s occasionally helpful for thinking through an intended architecture or adjusting an architecture that’s proving hard to change. I don’t think it really comes up too often
- **L**SP — Leaky abstractions can be harmful, so no argument from me here, but like all things, the impact is pretty variable and I wouldn’t necessarily make this a hard rule
- **I**SP — Important here and there if you’re building APIs for other developers, but probably not applicable on a daily basis
- **D**IP — Overblown, and probably causes a little more harm than good to folks that over apply this

All told, I think SOLID is still somewhat useful as a set of sometimes applicable heuristic, but very lacking as an all encompassing strategy for writing good code all by itself and absurd to use as a set of inviolate rules. So let’s move on to some other heuristic tools that I actually use more often myself.

## But what about CUPID?!?

Since it’s the new shiny object, and admittedly one of the reasons I finally got around to writing my own post, let’s talk about [Dan North’s new CUPID properties](https://dannorth.net/2022/02/10/cupid-for-joyful-coding/) he proposed as a “joyful” replacement or successor to SOLID. To be honest, I at first blew off CUPID as yet another example of celebrity programmers who are highly entertaining, engaging, and personable but don’t really bring a lot of actual intellectual content to the discussion. That’s most likely unfair, so I made myself take CUPID a little more seriously while writing this post and read it much more carefully the second time around.

I will happily recommend reading the CUPID paper. I don’t find it to be specific enough to be actionable, but as a philosophical starting point it’s pretty solid (no pun intended). As an over worked supporter of a heavily used OSS library, I very much appreciate his emphasis on writing code within the idioms of the language, toolset, and codebase you’re in rather than trying to force code to fit your preconceived notions of how it should be. A very large proportion of the nastier problems I help OSS users with is due to stepping outside of the intended idiomatic usage of libraries, the programming language, or the application frameworks they’re using.

## Other Heuristics I Personally Like

When I first joined my current company, my boss asked me to do an internal presentation about the SOLID Principles as a way to improve our internal development. I did indeed do that, but only as a larger presentation on different software design heuristics to include other models that I personally find frankly more useful than SOLID. I’d simply recommend that you give mental tools like this a try to see if it fits with the way you work, but certainly don’t restrict yourself to my arbitrary list or force yourself to try to use a mental tool that doesn’t work for you.

**Responsibility Driven Design**

To over simplify software design, it’s the act of taking a big, amorphous set of intended functionality and dividing that into achievable chunks of code that somehow makes sense when it’s all put together. To that end, the single most useful mental tool in my career has been [Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design) (RDD).

I highly recommend [Rebecca Wirfs-Brock’s A Brief Tour of Responsibility-Driven Design](https://www.wirfs-brock.com/PDFs/A_Brief-Tour-of-RDD.pdf) slide deck. In particular, I find her description of [Object Role Stereotypes](https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/august/patterns-in-practice-object-role-stereotypes) a very useful way of discovering and assigning responsibilities to code artifacts within a system.

**GRASP Patterns**

Similar to RDD is the [GRASP patterns from Craig Larman](https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)) that again can be used to help you decide how to split and distribute responsibilities within your code. At least in OOP, I especially use the [Information Expert pattern](https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)#Information_expert) as a guide to assign responsibilities in code.

**Command Query Separation**

I’m referring to the older coding concept rather than the later, much larger CQRS style of architecture. I’m going to be lazy again and just refer to [Fowler’s explanation](https://martinfowler.com/bliki/CommandQuerySeparation.html). I would say that I’d pay attention to this as a way of making sure your code is more predictable and falls inline with my concern about being careful about when and where you mutate state within your codebase.

**Don’t Repeat Yourself (DRY) or Once and Only Once**

From the Pragmatic Programmer (still on my bookshelf after 20 years of moves):

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system
>
> <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>

It’s an imperfect world folks. Duplication in code can easily be problematic when business rules or technologies need to change. Or when you’ve copy/pasted or implemented the same bug all over the code.

Unfortunately, people have used DRY as the motivation behind doing horrendously harmful things with abstractions, frameworks, and generics (and frequently come to discussion boards wanting my help making their custom framework work with my OSS tools). Somewhat because of that, there’s a nasty backlash against DRY. I’d again urge folks to not throw the DRY baby out with the bathwater. I would urge you to try to be mindful about duplication from your code, but back off of that if the effort to remove duplication when that adds complexity that feels like it’s more harmful than helpful.

**“A-Frame Architecture”**

I’ll happily recommend Jim Shore’s [Testing Without Mocks: A Pattern Language](https://www.jamesshore.com/v2/blog/2018/testing-without-mocks) paper, but I’d like to specifically draw your attention to what he terms the “A-Frame Architecture” as a way to decouple business logic from infrastructure, maximize testability, but also avoid going into unnecessarily complex abstractions.

**Code Smells**

Take the time to read through the chapter on [Code Smells](https://martinfowler.com/bliki/CodeSmell.html) in the [Refactoring book](https://martinfowler.com/books/refactoring.html) some time. Code smells are an easy mental tool to notice possible problems in your code. It doesn’t necessarily mean that your code is bad, but rather just something that might require more of your attention.

[More content on Wikipedia](https://en.wikipedia.org/wiki/Code_smell).

**Anti-Patterns**

Similar to code smells, anti-patterns are previously identified ideas, habits, or practices that are known to lead to bad outcomes. I’d spend more time on this, but it’s showing my age because the [AntiPatterns website](http://antipatterns.com/) was very clearly written with FrontPage ’97/’98!

**Tell, Don’t Ask**

I’m running out of steam, so I’m going to refer you to [Martin Fowler’s TellDontAsk](https://martinfowler.com/bliki/TellDontAsk.html). This is a shorthand test that will help you improve encapsulation and coupling between elements of code. It’s a complement to “Information Expert” from the GRASP patterns or “feature envy” from code smells. As usual, there’s a lot of ways to try to express the same idea in coding, and just use whatever metaphor or heuristic works best for you.

## Next time on “Jeremy expands on his Twitter rants…”

It’s finally time to explain why I think prescriptive architectural styles like Clean or Onion are problematic and why I’m trying to pull rank at work to ban these styles in new development.

Loading...
