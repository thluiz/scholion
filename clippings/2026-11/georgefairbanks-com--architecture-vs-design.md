---
url: "https://georgefairbanks.com/blog/software-architecture-vs-design"
captured_at: "2026-11-16T03:40:46+00:00"
title: "George Fairbanks - Architecture vs. Design"
domain: "georgefairbanks-com"
---

In this video, I try to tease out the difference between architecture and design. It took a million takes to get the production right and dissuaded me from making more short videos :-)

## Transcript:

## Intro

I’m George Fairbanks from Rhino Research.  
Imagine that you have been asked to choose the architecture for a software project.  
It would be good to know what software architecture is, exactly.  
So let’s look at what it is and how it relates to software design.  
We can start with a definition.  
This definition from the Software Engineering Institute is great,  
But we will need some background info before it makes sense.  
Everyone agrees that software architecture is a kind of software design.  
Software design is all the details of the completed software  
… architecture details are a subset.  
But how can we tell if a details is architectural?

## The importance of models

When you are designing software, you’d ideally  
Understand everything  
Consider every possible failure  
And design a failure-proof system.  
If you’ve worked on smaller systems, this is probably what you’ve been trying to do, with varying success.  
So why don’t we always do that? Three reason:  
Because software is usually too complex to fully understand.  
You have limited time.  
And you simply cannot identify every way it could crash, produce bad output, run too slowly, etc.  
The alternative is to build a model that simplifies the problem.  
In our field, this is considered unusual,  
Yet it’s standard practice in every other engineering field.  
But a model of what, exactly?  
We can’t consider every possible failure just like we cannot understand everything.  
So we decide which failures are possible or likely (that is, the risks)  
And we build a model that lets us reason about those risks Let’s say that you’re building online software, like a website. You might worry about security and request spikes. And you’d build a model to help you reason about those risks.  
If you were building embedded software, like a thermostat  
You might instead be worried about memory leaks and portability to new hardware.  
And you’d build a model for those risks.  
It would be great to look at every risk, but you only have so much time.

## What’s in the Architecture Model (and Why)

Now we are ready to answer our question about architecture and design.  
So here is what differentiates them.  
As a software developer, you think about possible failures.  
You choose which kinds failures you will try to avoid.  
You think about lots of possible designs too …  
… and exclude the ones that are susceptible to the failures you are worried about.  
Since the system you will build is complex …  
… you do your reasoning with a model of the system.  
You include details in your model only if they help you reason about the failures you identified.  
And you omit other design details.  
This is the essence of what goes into architecture models,  
But on real projects, things are of course not so linear.  
So, as an architect you build models of the system you are designing.  
The model helps you reason about and avoid the failures you are worried about.  
The details you include in your model are architectural.  
The full design of the system contains other details,  
details needed to build the system but not needed to reason about failures.  
Those details are not architectural.  
Models may exist only in your head – what is essential is the rationale:  
A design detail is architectural if and only if it can be traced back to avoiding a failure risk.  
That is how we decide if design details are architectural.

## Architecture vs. Design

Now let’s return to the question:  
What is software architecture and how does it relate to design?  
Here’s the definition of software architecture again and this time it should make a lot more sense.  
“The software architecture of a system is  
the set of structures needed to reason about the system,  
which comprise software elements, relations among them, and properties of both.”  
“set of structures” just means models, models you use to reason about the system  
When you build models to reason through your risks,  
You are excluding design details,  
ones that are irrelevant to the risks you identified  
and including architectural details,  
ones that are essential to understanding your system’s success.

## Conclusion

We started out with a simple question – what is software architecture and how does it relate to design?  
To answer it, we have taken a tour through avoiding engineering failures, reasoning using models, and rationales.  
Still, there’s much more to learn about software architecture.  
We haven’t even yet discussed parts of the definition: software elements, relations, and properties.  
So check out our other videos to learn more.  
If you liked this video, you may be interested in my book.  
Several chapters are available for free download.
