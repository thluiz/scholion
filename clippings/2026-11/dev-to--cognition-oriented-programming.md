---
url: "https://dev.to/hugh_jeremy/cognition-oriented-programming-3359"
captured_at: "2026-11-16T00:52:43+00:00"
title: "Cognition-oriented Programming"
domain: "dev-to"
---

Programming is addictive. As programmers we have immense power. We can create machines of practically unlimited scale and scope. Our creations may yield immense joy and utility. In code anything seems possible.

We programmers are still human. We are delicate, non-deterministic machines with squishy bodies and even squishier minds. Our capacity to build software is a function of our capacity to direct the limited resources of our bodies and minds.

Programming paradigms provide loose rulesets to help us direct those resources. We adopt functional-oriented, object-oriented, data-oriented, or some other programming orientation. These paradigms are well established and serve wonderfully.

They are top-level distinctions that sit on top of a huge stack of programming techniques, patterns, fads, and principles. Much joy comes from exploring new ways to write code, and finding out what allows each of us to most effectively reach our goals.

## [](#science-gets-us-some-of-the-way)Science gets us some of the way

What should drive that exploration? How can we know whether we should adopt a data-oriented approach to our latest project? The decision is often made out to be one of computer science. What paradigm best fits the requirements of the system?

A game programmer might generally require their program to respond to user input in 16 milliseconds or less. They might be well served in trading some readability for intensely optimised hot-loops that keep as much data in L1 cache as possible. Perhaps data-oriented C++?

A web programmer might have bit more room to move, client-side progress animations and common acceptance of network latency yielding an acceptable response time of 20 - 150 milliseconds. They might be well served optimising for readability. Perhaps object-oriented Ruby?

Yet the choice is rarely so clear cut. The latest fads, frameworks, and celebrity-programmer proclamations might influence us in different directions.

## [](#think-first-paradigm-later)Think first, paradigm later

Our guide should be the disposition of our own cognition. Each of us has a different mind. Your brain has developed differently to mine. Different experiences, training, and genetic-predispositions conspire to influence the manner in which we reason about code.

This is quite abstract. Let us examine a practical example. Consider a single class definition. How long is too long? 200 lines? 1,000 lines? What if we mix multiple classes into a single file?

You might be comfortable working with files thousands of lines long. Having witnessed such capability, I initially worked in this manner as well. Over many years I realised that I was not capable of maintaining a mental map of so much data. Now, I aim for a maximum of 150 lines per file, with strictly one class definition per file.

If a definition becomes longer than 150 lines, I actively ponder breaking it into smaller composable parts. As I move through my programs, I operate on a maximum of two files at a time, working on the flow of data from to another. In this way, I am always operating on a maximum of approximately 300 lines of code.

To you, this might sound absurd. You might have huge files and be perfectly comfortable surfing through them. This is exactly the point: We are all different, and we must seek to write code in a manner that supports our own cognition. Call it “cognition-oriented programming”.

## [](#cognition-for-teams)Cognition for Teams

In a team, this might appear to present problems. What if your CTO likes massive files and you don’t? I suggest that in a well-gel’d team, leadership is setting objectives and standards, not methods.

That is, you are ideally told what you need to do and the bounds within which you need to do it, not how to do it. In such an environment, you might adopt a team-wide code-style guide. You might have rules such as “no global variables” and “no mutable state”.

Then, within these bounds, you might focus on providing maintainable, reasonable, and clear public interfaces for your code. Behind those interfaces, and while always maintaining compliance with the set bounds, you may lean towards optimising for your own cognition.

## [](#your-optimised-mental-model)Your Optimised Mental Model

The concept of being “in flow” is well studied. Cognition-oriented programming might be viewed as a subset of the requirements for being “in flow”. At the highest level, it may be viewed as the search for your own hyper-optimised mental model.

Your brain has some strict finite limits. Your short-term working memory is likely limited to storing around seven “objects” at once. Your long-term memory might store pointers to every corner of your 200,000 line program, but at any instant, you can only reason with reference to some small subset of that code.

How you structure that limited reference is crucial. Think of your working memory as your own L1 cache. In paradise, your program is crunching cache data at warp speed, never needing to reach out to comparatively glacial RAM. In maximum flow, your mind is crunching on concepts stored in your working memory set. You reason about them at immense speed and with great precision.

In reality, our real programs need to go to RAM. Worse, they might need to access persistent storage. Heaven-forbid they need to take the long voyage out through the network stack. This is true for our mental models as well. In our metaphor, RAM might be some other piece of our codebase. Storage might be referencing some documentation. Network I/O might be talking to another human being.

All of those operations are crucial and important. Optimising them will yield more time in nirvana, with your optimised mental model facilitating a flow of performant, reliable, and reasonable code. The feeling, in my experience, is close to that of playing a musical instrument. The dance of fingers across the keys is unending, rhythmic, and perhaps even spiritual.

## [](#seek-nirvana)Seek Nirvana

Finding your cognition-oriented model takes time. Try new patterns. Read widely. Observe what works for some very successful programmers. Not because you should imitate them, but because their models might provide inspiration for some part of your own.

Engage in trial and error. Construct, destruct, and modify systems. All the while, observe yourself. Do you feel transcendent? Or do you feel as though you are straining to keep a grip on the program? Do you instantly see the path to a new feature, fixed bug, or performance improvement? Or do you strain to comprehend how to proceed?

These questions will enable you to find the patterns that map to your own cognition. Do not force your patterns on others. Do not presume others’ patterns will work for you. Code is the tool that enables you, as a squishy mammal, to dent the universe. Seek to make it your own.
