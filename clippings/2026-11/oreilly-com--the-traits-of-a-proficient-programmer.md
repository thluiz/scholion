---
url: "https://oreilly.com/ideas/the-traits-of-a-proficient-programmer"
captured_at: "2026-11-16T03:27:24+00:00"
title: "The traits of a proficient programmer"
domain: "oreilly-com"
---

![Abstract](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2019/06/abstract-2881_1400-fce6753350faa34408f3a5ec7247d5f5-1.jpg) Abstract (source: [Pixabay](https://pixabay.com/en/abstract-architecture-background-2881/))

Do you know what the difference between competence and proficiency is?

That sounds like a trick question, because the words seem to mean the same thing. But the subtle distinction between them is critically important.

Competence means having enough experience and knowledge to get stuff done; proficiency involves knowing why you are doing something in a certain way, and how it fits into the big picture. In other words, a proficient practitioner is always a competent practitioner, but the opposite may not be true.

The [Dreyfus Model of Skill Acquisition](http://www.dtic.mil/cgi-bin/GetTRDoc?AD=ADA084551&Location=U2&doc=GetTRDoc.pdf) covers this topic in great detail. Although its title sounds a bit academic, the paper is very approachable—and it has an amazing cover page that will make you feel like you’re reading a secret Illuminati cable that you found in some hidden library in a haunted house:

![](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2019/06/dreyfus_model-11bfed397e59e6da9ed6fd8276dafd33.png)

Figure 1. Cover page from “A Five-Stage Model of the Mental Activities Involved in Directed Skill Acquisition” by Dreyfus, Stuart E.; Dreyfus, Hubert L. (February 1980). Washington, DC: Storming Media.

I recommend reading the original source material for a great overview of the path from beginner to expert. But in this article, I will focus on the bottleneck for most software developers I’ve known: crossing the divide from competence to proficiency.

So first, let’s establish a working definition of competence as just meaning “I know how to do stuff”—it’s an oversimplification, but it’s close enough for our needs. It’s fair to say that no matter what kind of occupation you work in, knowing how to do stuff is pretty important. If you are a programmer, learning how to do stuff is a huge part of your work:

*   I need to know how to use revision control
*   I need to know how to use a consistent coding style
*   I need to know how to set up a continuous integration server
*   I need to know how to query a database
*   I need to know how to implement a responsive layout
*   I need to know how to work with a service API

And don’t get me wrong: Knowing how to do stuff, and a lot of it, is critically important. Don’t stop working on that, or you’ll soon find yourself out a job.

But the place where the intermediate programmer tends to get stuck (and many end up stuck there for life) is thinking that the difference between a beginner and an expert can be measured in how much stuff you know. That’s only half correct, and it emphasizes the less important half.

This is where proficiency comes in. And at its essence, proficiency is about “why you do things a certain way”—It’s the difference between understanding each of the parts of a problem individually, and understanding how the parts fit into the whole.

The gap between competence and proficiency may explain why so many people struggle with high level programming ideas, like design patterns.

A competent programmer can surely read up on the [Memento Pattern](https://en.wikipedia.org/wiki/Memento_pattern) and understand how to implement it. They would likely even be able identify scenarios where the pattern can be applied (perhaps to implement an undo operation within a GUI). But without knowing more about the big picture, they may still end up applying the pattern inappropriately.

By contrast, a proficient programmer is able to identify when the Memento Pattern breaks down (for example, if you are copying large amounts of data, or making a large number of copies). They might know of some alternative options to consider if the pattern wasn’t a perfect fit. They would also have some ideas on how to take the basic concepts behind Memento, and then adapt them to create a custom solution that is a better fit for their particular use case.

Far more importantly, a proficient programmer is capable of identifying the right and wrong times to talk about design patterns at all—if building a proof-of-concept feature, the question of proper code design is potentially irrelevant. If explaining a codebase to a beginner, a proficient developer may decide to stick to the basics of what the code is actually doing rather than throwing out named patterns and telling a novice “Go read the Gang of Four before asking me any questions.”

**And so with proficiency, comes the flexibility of a holistic mindset**.

Patterns, principles, idioms, libraries, language features—these are all tools. But a truly proficient programmer fits the tool to the job, not the other way around.

Many never specifically focus on developing proficiency, because frankly, it is more straightforward to develop competence. But should you want to shift your focus and need some help getting started, here are a few ideas to try out:

*   Explain the reasoning for why you want to do something a certain way, but don’t rely on generic “best practices” or community guidelines. Discuss pros and cons solely in the context of the current problem you are solving.
    
*   Learn fewer things, better. Then try to apply them in many different contexts, and see where they work well, and where they don’t. Use failures to identify opportunities to seek new tools that might help broaden your skill set, but only once you’ve established a clear need.
    
*   Look for examples of when others “break the rules” and are met with success. Occasionally break some of your own rules and see whether it hurts you, helps you, or leads to no change.
    
*   Dig into primary sources rather than just reading summaries. It takes more work, but helps you figure out both the basis and the boundaries of a technique, and also gives you an opportunity to generate new ideas of your own that are inspired by core principles.
    
*   Drop yourself into the deep end in a project that you are mostly unfamiliar with, and then try to find your way around without relying on your memorized routines, habits, and rules.
    
*   Ask others to explain why they do things, but don’t just accept dogmatic reasoning. Demand examples and inquire about context, so that you can try to imagine what it is like to be in their shoes. Doing this is tremendously valuable because it allows you to see the strengths and weaknesses of ideas in their natural habitats.
    
*   Pick a small number of specific skills you’re simply good but not great at, and then develop competence to an extreme, almost obsessive degree. Get to the point that you’re better at that particular tiny corner of the world than nearly anyone else you know. Once you get there, examine the pros and cons of deep but highly specific knowledge.
    

The thing about proficiency is that a little goes a long way. You need an extraordinary level of competence to be able to stand out on “knowing stuff”—but even a loose grasp on “knowing how to use the right stuff, at the right time” will take you far.

And here is the best part: **once you start focusing on proficiency, there’s a good chance that you will end up finding the true path to mastery**.

* * *

_Editor’s note: Gregory Brown is working on a book about the non-code aspects of software development, called [Programming Beyond Practices](https://www.safaribooksonline.com/library/view/programming-beyond-practices/9781491943816/?utm_source=oreilly&utm_medium=newsite&utm_campaign=the-traits-of-a-proficient-programmer-body-text-cta). Follow its progress [here](http://programmingbeyondpractices.com/)._
