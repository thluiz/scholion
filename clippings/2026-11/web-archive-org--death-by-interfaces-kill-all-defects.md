---
url: "https://web.archive.org/web/20200923061658id_/https://killalldefects.com/2020/01/19/death-by-interfaces/"
captured_at: "2026-11-16T07:57:20+00:00"
title: "Death by Interfaces? - Kill All Defects"
domain: "web-archive-org"
---

This might be an unpopular opinion, but we might be doing more harm than good with interfaces in object-oriented programming languages.

Let me explain.

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/01/Interface.png?resize=770%2C323&ssl=1)

Photo by [Clint Patterson](https://unsplash.com/@cbpsc1?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/plug?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

First, disambiguation time: when I’m talking about interfaces here, I’m referring to interface definitions in code, not user interfaces, user experience, or anything of a graphical nature.

Put flatly, an interface is a _contract_ that says a class will have certain characteristics – primarily public methods and properties – that other components can interact with.

The intent of an interface is to provide a programming language some degree of decoupling. For example, if you have a class that needs to read some external data, you might have it take in an `IDomainObjectDataProvider` instead of a `SqlServerDomainObjectDataProvider`.

That way your class wouldn’t need to care if it was talking to data in memory, in a database, or provided by some external API call.

This makes sense and its the classical reason for having interfaces.

Another reason might be a class in one layer not having references to a class defined in another layer. In that sense, interfaces can provide a certain degree of indirection. I like this reasoning less, but it can be valid in cases.

## So What’s Wrong With Interfaces?

Interfaces on their own are not _bad_, but they do have some significant tradeoffs and I’m not convinced that developers fully consider the tradeoffs of using them.

### Navigation Woes

First of all, using an interface makes it hard to navigate through code.

If I’m in my development environment of choice, most will support control clicking or some keyboard shortcut to navigate to the definition of a type.

With concrete types, navigation will take you directly to the implementation of the method you’re most interested in. With interfaces, you’ll navigate to the interface’s definition of that method.

This might not sound like much, but if you’re “in the flow” and thinking through a process, this is akin to coming around a corner and finding a solid wall where you expect a door. You have to make sense of what you’re seeing, then figure out which concrete type(s) you’re actually working with, find them, and find the relevant definition.

The penalty of this to our productivity is small, but significant, and this is a scenario that happens frequently in interface rich environments.

### Obfuscation via Interface

Let’s go back to the definition of an interface as a contract and the earlier example of an interface for a specific sort of data provider.

True, it’s very nice to have our code flexible and decoupled from specific implementations.

But if I’m looking at a class and seeing an interface, I can sometimes lose track of the runtime specifics.

Let’s say we only have one type of `IEmalSender` in an application, for example. If all I see when navigating code is an `IEmailSender` reference, I may lose track of what sender we’re actually working with in production and some of the specifics of its implementation.

Some may argue that this is a _good_ thing and that I shouldn’t have to care, and they’re right – to an extent – but the problem comes when we think so much in terms of abstraction that seeing the concrete deployment scenario becomes difficult.

### Architectural Cement

I like to think of interfaces as a sort of “architectural cement” in software development.

What I mean by this is that if I’m doing some refactoring (cleaning up the form of code without changing its behavior) and I find I no longer need to pass a certain parameter, or I want to make a method synchronous that was asynchronous (or vice versa), or any number of minor tweaks, interfaces make this harder.

Instead of changing something in one place, I have to navigate to the interface and change it there as well. If there were any other implementations of that interface, I need to seek them out and make sure they’re changed as well.

This means that an operation that might have been trivial to do in passing now takes me out of my natural flow and requires some additional degree of effort and thought to carry out. It might not be a lot, but it’s enough to make me think twice.

Additionally, if a member of an interface is never used, it’s much harder to detect that with code analysis tools than if a method that doesn’t adhere to an interface would be. This means that dead code that’s part of an interface definition stays around longer.

My point here is that _we pay for interfaces during the maintenance of our software in the form of little inconveniences._

It’s not a lot, but it’s more than you think, and the more interfaces you use, the more pronounced the problem becomes.

## Interface Segregation Principle

Another major issue I see with interfaces are violations of the Interface Segregation Principle (ISP). ISP is part of [SOLID programming principles](https://en.wikipedia.org/wiki/SOLID) which are 5 principles to produce maintainable software over time.

Specifically, ISP talks about preferring many smaller interfaces around specialized tasks to one larger interface designed for a class that does many general things.

This principle frequently gets violated when developers add interfaces to an existing system. Typically they’ll go into a class and extract an interface for all public members, then replace usages of the class with usages of the interface.

It’s somewhat straightforward and easy to do and so the path of least resistance leads to giant interfaces such as `IUserRepository` instead of smaller interfaces like `IUserValidator` and `IUserCreator`.

There are a number of problems with these larger interfaces including:

*   They frequently demonstrate the problems listed in earlier sections
*   They make it hard to make new implementations due to the number of members that are part of the interface
*   They tend to be the only concrete implementation of that interface
*   It tends to promote classes that don’t adhere to the Single Responsibility Principle (another tenant of [SOLID](https://en.wikipedia.org/wiki/SOLID))

All told, large interfaces are a bad idea and tend to lead to maintenance headaches in the long term.

## Inheritance vs Interfaces

So, if I’m cautioning on interfaces, what am I suggesting might be a better alternative?

Frequently when systems need a degree of flexibility in implementation, they don’t need _complete flexibility_ like an interface provides. Often they just need a base class that can serve as a bit of a mini-contract for purposes of dependency injection or testing.

Because of that, I advocate that any time you think about adding an interface, you consider instead if introducing or using an existing base class might be a better fit.

Some advantages that base classes can provide:

*   Navigation to a base class may actually navigate to a concrete or default implementation of a relevant method
*   Base classes provide a degree of code reuse / sharing that is not possible via interfaces
*   Base classes are slightly easier to refactor than interfaces

Of course, there are disadvantages and tradeoffs to consider:

*   Code in your base class will be present in any derived class unless overridden, which can constrain implementations too much
*   You don’t always control enough of the code to make base classes a viable option, or layer dependencies make this impossible
*   This can lead to too much “depth of inheritance” if there was already inheritance going on in your class hierarchy.

So, it’s a bit of a tradeoff as far as whether you use base classes or interfaces.

In general, I like to use interfaces for very small capabilities and tend to prefer base classes for things like configuring [inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control) containers.

## Closing Thoughts

Your preferences are going to match your needs. All I ask is that you don’t just automatically assume “This should be an interface” or “This should be a base class” or even “I shouldn’t pass a concrete class into this method”.

Whether you optimize for flexibility, maintenance, rapid development, or something else is entirely up to you.

Everything has advantages and tradeoffs, and software engineering is about finding the right mix for your codebase.
