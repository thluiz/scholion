---
url: "https://elixirforum.com/t/the-sam-state-action-model-pattern/703"
captured_at: "2026-11-16T03:23:15+00:00"
title: "The SAM (State - Action - Model) pattern - General Discussion, Blog Posts, Wiki | Elixir Forum"
domain: "elixirforum-com"
---

> SAM is a new reactive/functional pattern that simplifies Front-End architectures by clearly separating the business logic from the view and, in particular, strictly decoupling back-end APIs from the Front-End. SAM is technology independent and as such can be used to build Web Apps or Native Apps. It is also protocol independent and can be implemented over HTTP, WebSockets…

Creator: [@jdubray](https://elixirforum.com/u/jdubray)  
Gitter chat: [https://gitter.im/jdubray/sam](https://gitter.im/jdubray/sam)

> SAM is a pattern that aims at replacing the MVC pattern. If you are already familiar with MVC, you should be able to make an easy transition to SAM.

There are two main differences between MVC and SAM. First, SAM is reactive, while MVC is generally implemented in an interactive way. Some attempts have been made at implementing it in a reactive way, however, SAM is not just a reactive implementation of MVC. Second, SAM introduces the concept of State as a mechanism to further decouple the View from the Model and treats the view merely as a “State Representation”.

[![](https://forum.elixirforum.com/uploads/default/original/2X/c/c0590f87262f4824fde432d63c2b6b61c6b464e6.jpg)](https://forum.elixirforum.com/uploads/default/original/2X/c/c0590f87262f4824fde432d63c2b6b61c6b464e6.jpg "fig6.jpg")

## [](#p-4492-articles-1)Articles

*   [Why I No Longer Use MVC Frameworks](https://www.infoq.com/articles/no-more-mvc-frameworks) — [@jdubray](https://elixirforum.com/u/jdubray)

## [](#p-4492-examples-2)Examples

*   [sam-tic-tac-toe](https://github.com/509dave16/sam-tic-tac-toe)
*   [SAM Lambda](https://github.com/jdubray/sam-samples/tree/master/crud-blog-lambda) — SAM Lambda is a boiler plate project that implements the SAM pattern in AWS Lambda using DynamoDB to manage application/session state

## [](#p-4492-temporal-logic-of-actions-tla-3)Temporal logic of actions (TLA)

*   [TLA homepage @ Microsoft Research](http://research.microsoft.com/en-us/um/people/lamport/tla/tla.html)

### [](#p-4492-articles-4)Articles

*   [Temporal logic of actions (TLA)](https://en.wikipedia.org/wiki/Temporal_logic_of_actions) is a logic developed by Leslie Lamport, which combines temporal logic with a logic of actions. It is used to describe behaviours of concurrent systems.
    
*   [TLA+](https://en.wikipedia.org/wiki/TLA%2B)
    
    > … is a formal specification language developed by Leslie Lamport. It is used to design, model, document, and verify concurrent systems. TLA+ has been described as exhaustively-testable pseudocode and blueprints for software systems.
    > 
    > TLA+ is based on the idea that the best way to describe things formally is with simple mathematics, and that a specification language should contain as little as possible beyond what is needed to write simple mathematics precisely. TLA+ is especially well suited for writing high-level specifications of concurrent and distributed systems.
    
*   [Use of Formal Methods at Amazon Web Services](http://research.microsoft.com/en-us/um/people/lamport/tla/formal-methods-amazon.pdf)
    
*   [Why We Should Build Software Like We Build Houses](http://www.wired.com/2013/01/code-bugs-programming-why-we-need-specs/)
    

##### [](#p-4492-indirect-5)INDIRECT

*   [Boiling React Down to a Few Lines in jQuery](http://hackflow.com/blog/2015/03/08/boiling-react-down-to-few-lines-in-jquery/)
*   [Why We Ditched Angular.js and Wrote Our Own UI Library](https://blog.smartdraw.com/why-we-ditched-angular-js/)

### [](#p-4492-presentations-6)Presentations

*   [Modeling and Developing Systems Using TLA+](http://www.loria.fr/~merz/talks/argentina2005/slides.pdf)

### [](#p-4492-academic-papers-7)Academic Papers

_See [The Writings of Leslie Lamport](http://research.microsoft.com/en-us/um/people/lamport/pubs/pubs.html) for a full list of publications from this researcher._

*   [The PlusCal Algorithm Language](http://research.microsoft.com/en-US/um/people/Lamport/pubs/pluscal.pdf)

> “Programming languages provide no well-defined notion of a program step”

*   [Computation and State Machines](http://research.microsoft.com/en-us/um/people/lamport/pubs/state-machine.pdf) (2008)

> “State machines provide a framework for much of computer science. They  
> can be described and manipulated with ordinary, everyday mathematics”

*   [Model Checking TLA+ Specifications](http://research.microsoft.com/en-us/um/people/lamport/pubs/yuanyu-model-checking.pdf) (1999)
*   [Temporal logic of actions](http://research.microsoft.com/en-us/um/people/lamport/pubs/lamport-actions.pdf) (1994)
*   [Specifying Concurrent Program Modules](http://research.microsoft.com/en-us/um/people/lamport/pubs/spec.pdf) (1983)
*   [‘Sometime’ is Sometimes ‘Not Never’](http://research.microsoft.com/en-us/um/people/lamport/pubs/sometime.pdf) (1980)
*   [A New Approach to Proving the Correctness of Multiprocess Programs](http://research.microsoft.com/en-us/um/people/lamport/pubs/new-approach.pdf) (1979)
*   [The Implementation of Reliable Distributed Multiprocess Systems](http://research.microsoft.com/en-us/um/people/lamport/pubs/implementation.pdf) (1978)
*   [Proving the Correctness of Multiprocess Programs](http://research.microsoft.com/en-us/um/people/lamport/pubs/proving.pdf) (1977)

### [](#p-4492-books-8)Books

*   _[Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers](http://research.microsoft.com/en-us/um/people/lamport/tla/book.html)_
*   _[TLA+2: A Preliminary Guide](http://research.microsoft.com/en-us/um/people/lamport/tla/tla2-guide.pdf)_
*   _[Specifying Concurrent Systems with TLA+](http://research.microsoft.com/en-us/um/people/lamport/pubs/lamport-spec-tla-plus.pdf)_

## [](#p-4492-related-architectures-9)Related architectures

*   [Backends for Frontends (BFF)](https://www.thoughtworks.com/insights/blog/bff-soundcloud) at Soundcloud
*   [Elm architecture (functional frontend)](https://github.com/paldepind/functional-frontend-architecture)
