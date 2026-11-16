---
url: "https://freecodecamp.org/news/software-design"
captured_at: "2026-11-16T02:43:42+00:00"
title: "How to Learn Software Design and Architecture - a Roadmap"
domain: "freecodecamp-org"
---

![How to Learn Software Design and Architecture - a Roadmap](https://www.freecodecamp.org/news/content/images/size/w2000/2019/09/banner-1.png)

By Khalil Stemmler

> This article is a summary of what I'm writing about in my newest project, [solidbook.io - The Handbook to Software Design and Architecture with TypeScript](https://solidbook.io/). Check it out it you like this post.

It's crazy to me to consider the fact that Facebook was once an empty text file on someone's computer.

Lol.

This past year, I've been going hard in software design and architecture, [Domain-Driven Design](https://khalilstemmler.com/articles/domain-driven-design-intro/), and [writing a book](https://solidbook.io/) on it, and I wanted to take a moment to try to piece it together into something useful I could share with the community.

Here's my roadmap for how to learn software design and architecture.

I've broken it down into two artifacts: the **stack** and the **map**.

## The Stack

Similar to the [OSI Model](https://en.wikipedia.org/wiki/OSI_model) in networking, each layer builds on top of the foundation of the previous one.

![The stack](https://thepracticaldev.s3.amazonaws.com/i/e727h5b9nozcuo4za2yw.png)

## The Map

While I think the stack is good to see the bigger picture of how everything works together, the map is a little bit more detailed (and inspired by the [web developer roadmap](https://github.com/kamranahmedse/developer-roadmap)) and as a result, I think it's more useful.

Here it is below! To [fork the repo, read my detailed write-up and download it in high-res, click here](https://khalilstemmler.com/articles/software-design-architecture/full-stack-software-design/).

![Software Design and Architecture Roadmap](https://user-images.githubusercontent.com/6892666/65834517-bb39f980-e2a9-11e9-8a75-0e1559c5ed56.png)

## Stage 1: Clean code

The very first step towards creating long-lasting software is figuring out how to write **clean code**.

Clean code is code that is easy to understand and change. At the low-level, this manifests in a few design choices like:

*   being consistent
*   preferring meaningful variable, method and class names over writing comments
*   ensuring code is indented and spaced properly
*   ensuring all of the tests can run
*   writing pure functions with no side effects
*   not passing null

Writing clean code is incredibly important.

Think of it like a game of jenga.

In order to keep the structure of our project stable over time, things like indentation, small classes and methods, and meaningful names, pay off a lot in the long run.

The best resource to learn how to write clean code is Uncle Bob's book, "[Clean Code](https://www.amazon.ca/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)".

## Stage 2: Programming Paradigms

Now that we're writing readable code that's easy to maintain, it would be a good idea to really understand the 3 major programming paradigms and the way they influence how we write code.

In Uncle Bob's book, "[Clean Architecture](https://www.amazon.ca/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=asc_df_0132350882/?tag=googleshopc0c-20&linkCode=df0&hvadid=292982483438&hvpos=1o2&hvnetw=g&hvrand=13521899336201370454&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9000834&hvtargid=pla-435472505264&psc=1)", he brings attention to the fact that:

*   Object-Oriented Programming is the tool best suited for defining how we cross architectural boundaries with polymorhpism and plugins
*   Functional programming is the tool we use to push data to the boundaries of our applications
*   and Structured programming is the tool we use to write algorithms

This implies that effective software uses a hybrid all 3 programming paradigms styles at different times.

While you _could_ take a strictly functional or strictly object-oriented approach to writing code, understanding where each excels will improve the quality of your designs.

> If all you have is a hammer, everything seems like a nail.

### Resources

For **functional programming**, check out:

*   [Professor Frisby's Mostly Adequate Guide to Functional Programming](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/)
*   [Domain Modeling Made Functional](https://pragprog.com/book/swdddf/domain-modeling-made-functional?fbclid=IwAR0NHoyVrMoSRIE-EJMUOdsb3bhivow6JXKyUeg4FPHE8QmeOQG4L77HzMo)

## Stage 3: Object-Oriented Programming

It's important to know how each of the paradigms work and how they urge you to structure the code within them, but with respect to architecture, Object-Oriented Programming is the clear _tool for the job_.

Not only does Object-Oriented programming enable us to create a **plugin architecture** and build flexibility into our projects; OOP comes with the 4 principles of OOP (encapsulation, inheritance, polymorhism, and abstraction) that help us create **rich domain models**.

Most developers learning Object-Oriented Programming never get to this part: learning how to create a software implementation of the problem domain, and locating it in the center of a **layered** web app.

Functional programming can seem like the means to all ends in this scenario, but I'd recommend getting acquainted with model-driven design and [Domain-Driven Design](https://khalilstemmler.com/articles/domain-driven-design-intro/) to understand the bigger picture on how object-modelers are able to encapsulate an entire business in a zero-dependency domain model.

> Why is that a huge deal?

It's huge because if you can create a mental-model of a business, you can create a software implementation of that business.

## Stage 4: Design Principles

At this point, you're understanding that Object-Oriented Programming is very useful for encapsulating rich domain models and solving the [3rd type of "Hard Software Problems"- Complex Domains](https://khalilstemmler.com/wiki/3-categories-of-hard-software-problems/).

But OOP can introduce some design challenges.

When should I use composition?

When should I use inheritance?

When should I use an abstract class?

Design principles are really well-established and battle-tested object-oriented best practices that you use as railguards.

Some examples of common design principles you should familiarize yourself with are:

*   Composition over inheritance
*   Encapsulate what varies
*   Program against abstractions, not concretions
*   The hollywood principle: "Don't call us, we'll call you"
*   The [SOLID principles](https://khalilstemmler.com/articles/solid-principles/solid-typescript/), especially the [Single responsibility principle](https://khalilstemmler.com/articles/solid-principles/single-responsibility/)
*   DRY (Do Not Repeat Yourself)
*   [YAGNI (You Aren't Gonna Need It)](https://khalilstemmler.com/wiki/yagni/)

Make sure to come to your _own_ conclusions, though. Don't just follow what someone else says you should do. Make sure that it makes sense to you.

## Stage 5: Design Patterns

Just about every problem in software has been categorized and solved already. We call these patterns: design patterns, actually.

There are 3 categories of design patterns: **creational**, **structural**, and **behaviour**.

### Creational

Creational patterns are patterns that control how objects are created.

Examples of creational patterns include:

*   The **Singleton pattern**, for ensuring only a single instance of a class can exist
*   The **Abstract Factory pattern**, for creating an instance of several families of classes
*   The **Prototype pattern**, for starting out with an instance that is cloned from an existing one

### Structural

Structural patterns are patterns that simplify how we define relationships between components.

Examples of structural design patterns include:

*   The **Adapter pattern**, for creating an interface to enable classes that normally can't work together, to work together.
*   The **Bridge pattern**, for splitting a class that should actually be one or more, into a set of classes that belong to a hierarchy, enabling the implementations to be developed independently of each other.
*   The **Decorator pattern**, for adding responsibilities to objects dynamically.

### Behavioural

Behavioural patterns are common patterns for facilitating elegant communication between objects.

Examples of behavioural patterns are:

*   The **Template pattern**, for deferring the exact steps of an algorithm to a subclass.
*   The **Mediator pattern**, for defining the exact communication channels allowed between classes.
*   The **Observer pattern**, for enabling classes to subscribe to something of interest, and to be notified when a change occurred.

### Design pattern criticisms

Design patterns are great and all, but sometimes they can an additional complexity to our designs. It's important to remember YAGNI and attempt to keep our designs as simple as possible. Only use design patterns when you're really sure you need them. You'll know when you will.

If we know what each of these patterns are, when to use them, and when to _not even bother_ using them, we're in good shape to begin to understand how to architect larger systems.

The reason behind that is because **architectural patterns are just design patterns blown-up in scale to the high-level**, where design patterns are low-level implementations (closer to classes and functions).

### Resources

[Refactoring Guru - Design Patterns](https://refactoring.guru/design-patterns)

## Stage 6: Architectural Principles

Now we're at a higher level of thinking beyond the class level.

We now understand that the decisions we make towards organzing and building relationships between components at the high-level and the low-level, will have a significant impact on the maintainability, flexibility, and testability of our project.

Learn the guiding principles that helps you build in the flexibility that your codebase needs in order to be able to react to new features and requirements, with as little effort as possible.

Here's what I'd recommend learning right off the bat:

*   Component design principles: [The Stable Abstraction Principle](https://khalilstemmler.com/wiki/stable-abstraction-principle/), [The Stable Dependency Principle](https://khalilstemmler.com/wiki/stable-dependency-principle/), and The Acyclic Dependency Principle, for how to organize components, their dependencies, when to couple them, and the implications of accidentally creating dependency cycles and relying on unstable components.
*   [Policy vs. Detail](https://khalilstemmler.com/articles/enterprise-typescript-nodejs/clean-nodejs-architecture/), for understanding how to separate the rules of your application from the implementation details.
*   Boundaries, and how to identify the [subdomains](https://khalilstemmler.com/articles/enterprise-typescript-nodejs/application-layer-use-cases/) that the features of your application belongs within.

Uncle Bob discovered and originally documented many of these principles, so the best resource to learn about this is again, "[Clean Architecture](https://www.amazon.ca/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=asc_df_0132350882/?tag=googleshopc0c-20&linkCode=df0&hvadid=292982483438&hvpos=1o2&hvnetw=g&hvrand=13521899336201370454&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9000834&hvtargid=pla-435472505264&psc=1)".

## Stage 7: Architectural Styles

Architecture is about the stuff that matters.

It's about identifying what a system needs in order for it to be successful, and then stacking the odds of success by choosing the architecture that best fits the requirements.

For example, a system that has a lot of **business logic complexity** would benefit from using a **layered architecture** to encapsulate that complexity.

A system like Uber needs to be able to handle a lot of **real time-events** at once and update drivers' locations, so **publish-subscribe** style architecture might be most effective.

I'll repeat myself here because it's important to note that the 3 categories of architectural styles are similar to the 3 categories of design patterns, because **architectural styles are design patterns at the high-level**.

### Structrual

Projects with _varying levels_ of components and wide-ranging functionality will either benefit or suffer from adopting a structural architecture.

Here are a few examples:

*   **Component-based** architectures emphasize separation of concerns between the _individual components_ within a system. Think **Google** for a sec. Consider how many applications they have within their enterprise (Google Docs, Google Drive, Google Maps, etc). For platforms with lots of functionality, component-based architectures divide the concerns into loosely coupled independent components. This is a _horizontal_ separation.
*   **Monolithic** means that the application is combined into a single platform or program, deployed altogether. _Note: You can have a component-based AND monolithic architecture if you separate your applications properly, yet deploy it all as one piece_.
*   **Layered** architectures separate the concerns _vertically_ by cutting software into infrastructure, application, and domain layers.

![Clean Architecture](https://khalilstemmler.com/img/blog/software-architecture-design/app-logic-layers.svg)

> An example of cutting the concerns of an application _vertically_ by using a layered architecture. Read [here](https://khalilstemmler.com/articles/software-design-architecture/organizing-app-logic/) for more information on how to do this.

### Messaging

Depending on your project, messaging might be a really important component to the success of the system. For projects like this, message-based architectures build on top of functional programming principles and behavioural design patterns like the observer pattern.

Here are a few examples of message-based architectural styles:

*   **Event-Driven** architectures view all signficant changes to state as events. For example, within a [vinyl-trading app](https://github.com/stemmlerjs/white-label), a offer's state might change from "pending" to "accepted" when both parties agreee on the trade.
*   **Publish-subscribe** architectures build on top of the Observer design pattern by making it the primary communication method between the system itself, end-users / clients, and others systems and components.

### Distributed

A distributed architecture simply means that the components of the system are deployed separately and operate by communicating over a network protocol. Distributed systems can be very effective for scaling throughput, scaling teams, and delegating (potentially expensive tasks or) responsibility to other components.

A few examples of distributed architectural styles are:

*   **Client-server** architecture. One of the most common architectures, where we divide the work to be done between the client (presentation) and the server (business logic).
*   **Peer-to-peer** architectures distribute application-layer tasks between equally-privileged participants, forming a peer-to-peer network.

## Stage 8: Architectural Patterns

Architectural _patterns_ explain in greater tactical detail how to actually implement one of those architectural _styles_.

Here are a couple of examples of architectural patterns and the styles that they inherit from:

*   **[Domain-Driven Design](https://khalilstemmler.com/articles/domain-driven-design-intro/)** is an approach to software development against really complex problem domains. For DDD to be most successful, we need to implement a **layered architecture** in order to separate the concerns of a domain model from the infrastrural details that makes the application actually run, like databases, webservers, caches, etc.
*   **Model-View Controller** is probably the most well-known architectural pattern for developing user interface-based applications. It works by dividing the app into 3 components: model, view, and controller. MVC is incredibly useful when you're first starting out, and it helps you piggyback towards other architectures, but there hit's a point when we realize [MVC isn't enough](https://khalilstemmler.com/articles/enterprise-typescript-nodejs/when-crud-mvc-isnt-enough/) for problems with lots of business logic.
*   **Event sourcing** is a functional approach where we store only the transactions, and never the state. If we ever need the state, we can apply all the transactions from the beginning of time.

## Stage 9: Enterprise patterns

Any architectural pattern you choose will introduce a number of constructs and technical jargon to familiarize yourself with and decide on whether it's worth the effort to use or not.

Taking an example that many of us know, in **MVC**, the _view_ holds all the presentation layer code, the _controller_ is translates commands and queries from the _view_ into requests that are handled by the _model_ and returned by the _controller_.

Where in the Model (M) do we handle these things?:

*   validation logic
*   invariant rules
*   domain events
*   use cases
*   complex queries
*   and business logic

If we simply use an ORM (object-relational mapper) like [Sequelize](https://freecodecamp.org/news/) or [TypeORM](https://freecodecamp.org/news/) as the _model_, all that important stuff to gets left to interpretation on where it should go, and it finds itself in some unspecified layer between (what should be a rich) _model_ and the _controller_.

![mvc-2](https://www.freecodecamp.org/news/content/images/2019/10/mvc-2.svg)

> Taken from "3.1 - Slim (Logic-less) models" in [solidbook.io](https://solidbook.io/).

If there's something I've learned so far in my journey going beyond MVC, it's that **there is a construct for everything**.

For each of those things that MVC fails to address, there exist other **enterprise patterns** to solve them. For example:

*   **[Entities](https://khalilstemmler.com/articles/typescript-domain-driven-design/entities/)** describe models that have an identity.
*   **[Value Objects](https://khalilstemmler.com/articles/typescript-value-object/)** are models that have no identity, and can be used in order to encapsulate validation logic.
*   **[Domain Events](https://khalilstemmler.com/articles/typescript-domain-driven-design/chain-business-logic-domain-events/)** are events that signify some relevant business event occurring, and can be subscribed to from other components.

Depending on the architectural style you've chosen, there are going to be a ton of other enterprise patterns for you to learn in order to implement that pattern to it's fullest potential.

### Integration patterns

Once your application is up and running, as you get more and more users, you might run into performance issues. API calls might take a long time, servers might crash from being overloaded with requests, etc. In order to solve these problems, you might read about integrating things like **message queues** or **caches** in order to improve performance.

This is probably the most challenging stuff: _scaling, audits, and performance_.

Designing a system for _scale_ can be incredibly challenging. It requires a deep understanding of the limitations of each component within the architecture, and a plan of action for how to mitigate stress on your architecture and continue to serve requests in high-traffic situations.

The need also the need to _audit_ what's going on in your application. Large enterprise companies need to be able to perform audits in order to identify potential security issues, understand how users are using their applications, and have a log of everything that's ever happened.

This can be challenging to implement, but common architectures end up looking **event-based** and build upon a wide range of software and system design concepts, principles, and practices like Event Storming, DDD, CQRS (command query response segregation), and Event Sourcing.

* * *

I hope that was useful to you!

Let me know if you have any suggestions or questions.

Cheers!

[Fork it on GitHub](https://github.com/stemmlerjs/software-design-and-architecture-roadmap)

[Read the book on software design & architecture](https://solidbook.io/)

[Read the write-up](https://khalilstemmler.com/articles/software-design-architecture/full-stack-software-design/)

* * *

> [khalilstemmler.com](https://khalilstemmler.com/) - I teach Advanced TypeScript & Node.js best practices for large-scale applications and how to write flexible, maintainable software.

* * *

Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. [Get started](https://www.freecodecamp.org/learn)
