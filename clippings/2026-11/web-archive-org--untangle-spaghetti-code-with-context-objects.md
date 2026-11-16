---
url: "https://web.archive.org/web/20200923054153id_/https://killalldefects.com/2020/01/15/untangle-spaghetti-code-with-context-objects/"
captured_at: "2026-11-16T07:59:55+00:00"
title: "Untangle Spaghetti Code with Context Objects - Kill All Defects"
domain: "web-archive-org"
---

By the time I heard the term “spaghetti code” I was incredibly guilty of writing it.

Spaghetti code seems to mean something slightly different to everyone, but it’s key symptoms include:

*   Code you have to trace from file to file in order to follow a simple flow of logic
*   Methods that seem to take an increasing number of parameters as time goes on
*   Code that’s comprehensible only to its creator (and even that isn’t a guarantee)

In this article we’ll explore using context objects to address some of the worst symptoms of spaghetti code.

## Understanding Spaghetti Code

Let’s say you’re working on a food distribution algorithm for a high tech pasta-based dining establishment. You have code designed to take in details about the people dining at a table and dispense an appropriate amount of pasta for the guests.

Your existing method might look something like this:

Now, let’s say that your boss comes to you and tells you that she needs the system to dispense the _cheapest_ pasta currently in stock in order to cut costs and boost profits. Since the method doesn’t _have_ the current market rates on pasta, you will need to pass in that parameter upstream.

Your method will now look something like this:

Not only are we starting to have a larger method signature, but in order to support the new parameter you now need to pass in the parameter from other methods that call `BuildPastaMeal`, many of which may not have the parameter readily available.

As a result, the minor change you made in your logic necessitates changes in 8 or 9 methods.

On top of this, if loading pasta pricing information requires a database call or external API invocation, those 8 or 9 upstream places all need to manage that operation.

This is no way to grow software.

This is a good way to get merge conflicts or methods with an unhealthy number of parameters. Additionally, if database calls are needed, you will often see methods that load data just in case methods they call may need it.

Thankfully, there’s a better way to combat parameter explosion and spaghetti code.

## Context Objects to the Rescue

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/Pasta.png?resize=770%2C323&ssl=1)

Photo by [Olesya Yemets](https://unsplash.com/@ladymilkydeer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/spaghetti?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Instead of passing around individual parameters, you can create a _context object_ that wraps commonly used things together into a single object.

This way, if we need to add something, we simply add it to the context object and then either set the value when the context object is created (often at the beginning of a request or on authentication) or you have the property be lazy loaded.

Under lazy loading, expensive operations are performed the first time they’re needed. This means that if you turn out to not need a specific piece of information, you won’t have to pay for fetching it.

The primary benefits of context objects are:

*   Ease of adding new state to the context
*   Speed of new development without having to pass around additional parameters
*   Changes occur only in places where they’re actually relevant to the problem being solved (less connecting code)

However, there are some drawbacks.

## Hero or Villain?

Most good things, when taken to an extreme, turn out to be very bad things. Context objects are no different.

When taken to the extreme, you can start to see symptoms like:

*   Overly large “god objects”
*   Context objects performing application logic instead of just containing state
*   Too many small pieces of state stuck into the object that could have been wrapped into another object (for example, first name, last name, and age could and should be part of a `Person` object and not loose in the context)

A few healthy rules should discourage some of these behaviors:

*   Encourage context objects to have immutable state. That is, do not provide setters on properties. The exception to this is lazy-loaded state.
*   Strongly resist methods inside of your context objects, aside from private methods to lazy load values as needed.

## Closing Thoughts

Context objects are not a key to instant success, but in large web applications they can be helpful to keep applications focused on what really matters to the task at hand.

Properly used, context objects can drastically reduce the quantity of merge conflicts a team encounters, simplify code, and improve development speed by reducing unnecessary connecting code for parameter passthroughs.

By reducing the number of lines modified in each feature or fix, context objects help us [avoid quality issues](https://killalldefects.com/2019/11/22/avoiding-quality-minefields/) by reducing the amount of code churn. Put simply, if you don’t need to modify a line you’re not going to make a mistake modifying it that the compiler wouldn’t catch.

Similarly, if you don’t need to think about code gluing everything together, it reduces the noise during [code review](https://killalldefects.com/2019/08/27/code-review-and-your-team/), making it easier to spot the missed requirements or potential bugs that may be present.

Context objects aren’t always the solution, but they can be a maintainability lifesaver for larger applications – particularly those without formal [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) support.
