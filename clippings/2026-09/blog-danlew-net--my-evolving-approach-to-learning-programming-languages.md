---
url: "https://blog.danlew.net/2024/09/24/my-evolving-approach-to-learning-programming-languages/"
captured_at: "2026-09-23T18:52:34+01:00"
title: "My Evolving Approach to Learning Programming Languages"
domain: "blog.danlew.net"
---

python
My Evolving Approach to Learning Programming Languages
Dan Lew
24 Sep 2024 • 3 min read

I've recently started a new job that uses Python.

The last time I professionally Python'd was 15 years ago, writing backends for mobile apps I worked on. At the time, I was still a novice developer, only a couple years out of college. While I've returned to Python from time to time for tiny throwaway scripts, I've not seriously examined the language or its ecosystem since.

Now I'm back in the thick of it with Python. And it's been a fascinating journey diving into a language again as a far more experienced developer.

For example, when I last used Python, I found list comprehensions totally incomprehensible. These strange constructs scared me; any code snippets I found online using them felt like arcana. Why would anyone use these over simple `for` loops?

Now, having become experienced in the ways of map/filter, list comprehensions make so much sense. What before seemed like magic now seems like table stakes - of course your language should have some way to do a map/filter quickly!

While brushing up on Python, I found myself paying attention to different aspects of the language than I did as a novice developer. I think those differences are telling - the sorts of things one worries about as a more experienced developer.

Here's (some) of the questions I ask nowadays… (I've opted not to actually answer any of the questions I've raised because I am sure those answers would be horribly outdated within a year.)

Reproducible Environment

Question: If I were to check out my source code on another computer, how many steps would I have to take before I could run it?

Me, 15 Years Ago: All I need is for this code to work on my computer and the server. Therefore, I use Python 2.whatever; it's installed by default on both machines! I try to avoid libraries because it is scary to depend on strangers' code. If I do use one, I never update - not because I fear breaking anything, but because I literally don't know libraries are regularly updated!

Why I Care Now: The more deterministic your software is, the easier it is to develop. That starts with your environment; "works on my machine" doesn't cut it when working with other people (and deploying software to the cloud). Plus, the tools that allow reproducible environments tend to also make it easier to install dependencies.

Unit Testing

Question: How do I run unit tests?

Me, 15 Years Ago: I had a derisive attitude towards automated testing. It's a waste of time, tests always break, and it's easier to just run the code myself.

Why I Care Now: I'm big into test-driven development now, primarily because it is a much faster way to test the code myself. Sure, writing the test takes time, but then I can repeatedly verify my solution as I develop it. Also, whenever I want to refactor the code in the future, the tests keep me from shooting myself in the foot. As a cherry on top, writing testable code often results in better code design.

Typing

Question: How do I get type checking?

Me, 15 Years Ago: Who cares about types? It's a small server, I know all the inputs and outputs. If something goes wrong, I can always fix it quickly; I know the codebase top to bottom.

Why I Care Now: The codebases I work with now are too large to know it all. I want to know what the inputs/outputs of a function are without having to read the implementation! Also, people make mistakes all the time - letting the type checker figure out those mistakes quickly now is better than finding out later, in production.

Privacy

Question: How do I hide the private implementation details of my public APIs?

Me, 15 Years Ago: I had no concept whatsoever of what an "implementation detail" is.

Why I Care Now: I work hard to reduce accidental complexity in a codebase (so that it remains maintainable). Tightly defining your API is a great way to do that, which means hiding all the implementation details that consumers shouldn't need to know about or use directly.

Data Classes

Question: How do I make a structured collection of data that's immutable?

Me, 15 Years Ago: How could you ever write a program with immutable data? Isn't data all about mutation? Mutable dicts for everyone!

Why I Care Now: Nowadays I'm a fan of functional programming (as a way of keeping side effects to a minimum, which in turn reduces code complexity). Part of what makes it work is immutable data, which prevents subroutines from changing your inputs unexpectedly.

Conclusion

These concerns are not exclusive to Python - they're the sort of questions I'd ask of any language when getting started these days.

What's fascinating to me is that there was nothing stopping me from asking these questions last time I used Python! Though, some of the answers would've been more frustrating - there were no type hints, no dataclasses, etc. In some ways, the concerns I have now are modern concerns that people (in general) weren't thinking about as much 15 years ago.

Think about how differently we'll view software development in 15 years! I'm sure there are patterns we'll develop in the next decade that become standard - truly unthinkable that you wouldn't use them - that no one has thought up yet today. We'll see!
