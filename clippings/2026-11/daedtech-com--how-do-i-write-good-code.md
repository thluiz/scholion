---
url: "https://daedtech.com/write-good-code"
captured_at: "2026-11-16T03:28:41+00:00"
title: "How Do I Write Good Code?"
domain: "daedtech-com"
---

My life has been undergoing some task thrash of late. That, combined with a decent amount of time doing car trips, has thrown me off of my recent reader question streak, in favor of cross posts.  But, today I remedy that.  A reader has a pretty straightforward question: “how do I write good code?”

Here is the question, verbatim.  It references [a post that I wrote a while back](https://daedtech.com/maintainable-code-vs-common-code/) that has definitely sparked some discussions and follow-up questions.

> You write about how to “de-brilliant” your code. I have worked with “brilliant” code in the past and can say that experience is anything but. I’m starting my career as a software dev now and one of the things I’ve been wondering about recently is how to write good code? I think generally that I can recognize well written code from poorly written code, but I want to get even better and I’m not sure how.

First of all, congratulations on the new career!  You’re off to a good start.  I’d say you’re beginning auspiciously by asking a question that is important, easy to understand, and really, really nuanced to answer.  But, let’s try.  Here is my general take on how to write good code, in order of priority.

[![DevSkills](https://daedtech.com/wp-content/uploads/2014/11/DevSkills.jpg)](https://daedtech.com/job-titles-be-like-the-wolf/devskills/)

### Make it Easy to Change

I make no secret of being a test driven development (TDD) proponent.  This development practice nets me many benefits, not the least of which is an excellent safety net for making changes.  Since I write the tests as I go, not a moment passes during which I lack this safety net.  The result?  I can fearlessly refactor my code any time I like.

And the safety net extends beyond just refactoring.  When the time comes to add the next bit of functionality or to adapt to a change in requirements, I know immediately if my changes break anything.  I thus consider my code to be easy to change.  Try whatever you want and see if anything goes red.  If not, you’re good.

I list this property first because of its foundational nature.  If you write code that is easy to change, then you will be setup for success in correcting anything else that may be wrong with it.  For making code easy to change, I certainly recommend automated tests and TDD, but I wouldn’t say these are the only possible ways to generate easily changed code.

### Make It Really Readable

Next up, I’d advise you to focus on making your code readable.  This theme certainly relates to making it easy to change, but with a subtle difference.  You can write code that readers have a difficult time comprehending but that is nonetheless easily changed (e.g. via extensive unit tests).  But, that said, readability tends to aid with ease of change.

Whether you can tease these concerns apart or not, I wouldn’t recommend trying.  Make your code as readable as possible.  Both you and others will read the code far more often than you will ever modify it, so optimize for fast, clear comprehension.

What do I mean?  Consider a few quick examples.

*   Spend a bit of time thinking through method and variable names to ensure they describe exactly their purpose.
*   Extract dense statements onto multiple lines that are each more readable.
*   Avoid large methods, complex methods, nested conditionals and other sources of dense complexity.  The human mind struggles to keep many variables, scopes, and parameters in context — make it simple by avoiding this burden.

“Uncle” Bob Martin, who is [an expert on Clean Code](http://amzn.to/2apSGHp), once said (or perhaps quoted someone who said) that clean code reads like prose.  Strive to write code that causes a reader to, with each line, say, “ok, ok, makes sense, yep, ok, gotcha.”  To force your own hand, try writing code without comments, relying only on the code itself to tell the story.

### Make It Work

It may sound strange, but I offer “it works” as the third priority in the world of writing good code.  I picked up this particular theme from a talk by the very same Bob Martin.

Think about it.  If you focus on writing easy to change, easy to understand code, then even if it does the wrong thing, you don’t have a significant problem.  You’ll find it easy to fix the problem.  If, on the other hand, you write code that does the right thing in terms of behavior, but is difficult to understand and change, you’re good for the moment.  But if requirements change (and they always do on a long enough timeline) your code is now both wrong _and_ hard to fix.

Make no mistake.  Writing code that does what you intend is certainly important and a prerequisite for professionalism.  But if you have discipline about ease of change and readability, getting things working becomes easier for you over the lifespan of the code you write.

### Make It Elegant

Design patterns, performance optimizations, space-preserving algorithms, architectural philosophies, major paradigms, aspect-oriented programming, security best practices… wow.  It can get pretty overwhelming.  But don’t let yourself be overwhelmed.

Writing elegant code is the last step I’ll cover here.  It also represents the step that you will never truly master.  Oh, make no mistake. You’ll write some elegant code in some spots.  You’ll do some things that make you proud to show them.  But there’s always a better algorithm, a more robust solution, or a new preferred architecture.

Making your code elegant demands that you spend time reasoning beyond the basics.  But it also demands that you never abandon the assumption that everything you do could always be just a little bit better.

### Learn from Accomplished Practitioners

I’ll close by advising that you help yourself to a large dose of wisdom from the field.  Practice is great.  Getting code reviews from or pairing with people more experienced than you is even better for guiding your practice.  Seek out advice and learn as much as you can, especially in the sorts of situations that you’ll encounter in your day to day (i.e. perhaps not textbooks).

Here are some books that I would recommend for further reading.  I found these to be quite formative in developing my own skills over the years.

*   [The Aforementioned Clean Code](http://amzn.to/2apVKDq)
*   [The Clean Coder](http://amzn.to/2aCaYsC)
*   [The Pragmatic Programmer](http://amzn.to/2ayiZuX)
*   [Working Effectively with Legacy Code](http://amzn.to/2az706k)
*   [Test-Driven Development by Example](http://amzn.to/2aCcwCC)
*   [Code Complete](http://amzn.to/2apVkgy)
