---
url: "https://swizec.com/blog/smart-core-thin-interfaces/?ref=dailydev"
captured_at: "2026-09-25T21:16:15+01:00"
title: "Smart core, thin interfaces"
domain: "swizec-com"
---

![Swizec Teller](https://swizec.com/assets/swizec-byline-CCFrcNvL.jpg)

Here's an approach to writing code that I've been using for years across multiple stacks and couldn't quite put into words until now. One of those _"This code feels wrong but I can't explain why"_. Now I can!

## [Smart core, thin interfaces](#smart-core-thin-interfaces)

The best way to avoid a [big ball of mud](https://swizec.com/blog/big-ball-of-mud-the-worlds-most-popular-software-architecture/) is to use _small_ balls of mud called modules.

But how do you structure those?

The approach I've seen work time and again and that keeps coming up across literature, is to build core business logic modules surrounded by interfaces for different actors. Based on the [actor-command-event](https://swizec.com/blog/finding-modules-in-a-big-ball-of-mud/#how-to-detangle-the-domain) approach to domain modeling.

[![Smart core, thin interfaces](https://swizec.com/_vercel/image?url=%2Fassets%2FSmart-core-thin-interfaces-90di76-BbFvESxp.png&w=960&q=75)](https://swizec.com/assets/Smart-core-thin-interfaces-90di76-BbFvESxp.png)

Empirically we know that [modularization leads to maintainable adaptable software](https://swizec.com/blog/empirical-evidence-for-code-modularity/). Tightly coupled components are hard to kill and experience constant churn. Loosely coupled components tend to stabilize and are easy to replace when you need to.

The smart core understands a business domain, its events and commands, and encapsulates the logic required to make it work. Like a billing module that understands the intricacies of your payment plans, discounts, subscriptions, and so on.

The light-weight interfaces understand how different actors want to interact with this logic. Admins need to make exceptions, consumers want clear information, the integrations API cares about fault tolerance, and your backend systems need to be notified when something happens.

Each actor has different needs, but they must all agree on the current state of the system and follow the same set of rules for what's possible when. Push that logic to the edges and mistakes are all but guaranteed. Keep it tightly packed and you stand a chance.

That is to say: **Repeat code with abandon. Avoid repeating semantics**.

If this sounds familiar, the philosophy flies under many names:

*   [hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/) is a way to achieve this in monolithic applications
*   [service oriented architecture](https://www.atlassian.com/microservices/microservices-architecture/soa-vs-microservices) is for when your modules are coupled but talk through an events bus
*   [microservices architecture](https://www.atlassian.com/microservices/microservices-architecture/soa-vs-microservices) happens when your modules are independently deployable and talk through RPCish or RESTful APIs
*   [fat models, skinny controllers](http://weblog.jamisbuck.org/2006/10/18/skinny-controller-fat-model) are popular in the world of fullstack web frameworks
*   [state machines](https://www.smashingmagazine.com/2018/01/rise-state-machines/), [custom hooks](https://react.dev/learn/reusing-logic-with-custom-hooks), and [global state managers](https://blog.isquaredsoftware.com/2017/05/idiomatic-redux-tao-of-redux-part-1/) are popular in the world of modern UI frameworks
*   [functional core, imperative shell](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell) is popular in some functional programming circles

They're all implementation details of the same idea:

## [Sanitize at the edges](#sanitize-at-the-edges)

Keep your business logic contained and hide the messy details behind a pretty interface. Avoid smearing that logic into other parts of the system and validate/sanitize inputs at the edges so your deep logic has fewer exceptions to deal with.

Like this:

```
function prettyInterface(input = null) {
  if (input) {
    doTheThingWithInput(input);
  } else {
    doTheThingWithoutInput();
  }
}
```

Instead of:

```
function doTheThing(input = undefined) {
	const data = db.query(sql`select * from blah where ${input ? 'col = '+input : 'col is null'})

	if (data && input) {
		return `Search ${input} found ${data}`
	} else if (data && !input) {
		return `Found ${data} with null values`
	} else if (!data && input) {
		return `Search ${input} found nothing`
	} else if (!data && !input) {
		return `No empty values found`
	}
}
```

Without the interface, your deep method has to handle all possible branches in functionality. This makes it brittle. If it doesn't handle those exceptions, then everywhere you use that method has to deal with the exceptions. This makes every change impact a large part of your codebase.

In practice you'd make the `prettyInterface` function public and the rest private. This helps you fight [Hyrum's law](https://www.hyrumslaw.com/) by preventing unintended use. How you do that depends on your language and team conventions.

## [What's an interface?](#whats-an-interface)

An interface is any pile of code that translates public commands into internal function calls. How that looks depends on your context.

For an API it might be a short controller function that takes an API request, cleans up the inputs, and calls an internal module.

For a consumer UI, it can be a whole backend-for-frontend with server-side rendering and oodles of client code creating the app experience.

Cheers,  
~Swizec

Filed under: [Software Engineering](https://swizec.com/categories/software-engineering)[Architectural Complexity](https://swizec.com/categories/architectural-complexity)[Scaling Fast Book](https://swizec.com/categories/scaling-fast-book)

## Dive deeper with my books

### Related Articles

*   [Finding modules in a big ball of mud](https://swizec.com/blog/finding-modules-in-a-big-ball-of-mud/)
*   [Common abstraction traps](https://swizec.com/blog/common-abstraction-traps/)
*   [Why even care about code structure](https://swizec.com/blog/why-even-care-about-code-structure/)
*   [Say no to abstract code](https://swizec.com/blog/say-no-to-abstract-code/)
*   [Better tooling won't fix your API](https://swizec.com/blog/better-tooling-wont-fix-your-api/)
