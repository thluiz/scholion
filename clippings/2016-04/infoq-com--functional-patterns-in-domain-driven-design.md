---
url: "http://www.infoq.com/news/2014/05/functional-patterns-ddd?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
captured_at: "2016-04-11T12:10:45-03:00"
title: "Functional Patterns in Domain-Driven Design"
domain: "infoq-com"
---

# Functional Patterns in Domain-Driven Design

[Domain-Driven Design](http://en.wikipedia.org/wiki/Domain-driven_design) (DDD) does a great job in encouraging developers to create a domain model and an [ubiquitous language](http://en.wikipedia.org/wiki/Domain-driven_design#Core_definitions), but trying to implement DDD concepts using object orientation principles with state and behaviour often gives you a muddled mutable model, [Debasish Ghosh](https://plus.google.com/106871002817915335660/posts) states in a blog post about [functional patterns in domain modelling](http://debasishg.blogspot.se/2014/05/functional-patterns-in-domain-modeling.html).

Debasish, a senior member of [ACM](http://www.acm.org/) and author of [DSLs in Action](http://www.manning.com/ghosh/), argues that a model may be rich in the sense that all concepts related to a particular domain abstraction are located in one class but that this also makes the class more fragile with a local instead of a global focus, thus when composing all abstractions in a domain it may become too polluted with code just needed to resolve the impedance mismatch between class boundaries.

In his arguing he refers to [Dean Wampler](http://www.deanwampler.com/) who recently [argued](http://www.slideshare.net/deanwampler/reactive-design-languages-and-paradigms) that functional programming principles can help improve in domain driven design. Dean claims that "Models should be anaemic", encouraging a practice with domain objects having only state and moving behaviours into standalone functions.

Another statement Debaish argues against is that bundling state and behaviour in a class increases encapsulation, instead he believes that building domain behaviours as standalone functions leads to a better modularization and realization of the domain model according to the principles of DDD. All domain behaviours are then modelled as functions in a module representing the aggregate.

As an example he continues from earlier blog posts where he implemented the Specification and Aggregate patterns in DDD using functional programming principles, now using functional patterns and functions as building blocks to build behaviours that model the ubiquitous language of the domain. Debaish claims that one principle in DDD is to lift the domain model vocabulary into your implementation so that the functionality becomes obvious during the whole system lifecycle.

Dean Wampler also did a presentation on a similar topic at the [React conference](http://reactconf.com/) in April talking about [reactive design and language paradigms](https://www.youtube.com/watch?v=4L3cYhfSUZs).

### Tell us what you think

Email me replies to any of my messages in this thread
