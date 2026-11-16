---
url: "https://fluentcpp.com/2020/03/10/3-types-of-toxic-software-projects"
captured_at: "2026-11-16T04:30:37+00:00"
title: "3 Types of Toxic Software Projects"
domain: "fluentcpp-com"
---

Published March 10, 2020

In software houses there are typically more projects opportunities to do than resources to realize them all. In my company at least, there are plenty of things we could do to make our software evolve, but only so many we have the time to invest in to and do properly.

This means that being able to choose what project to work on and what project _not_ to work on is crucial.

This is important for productivity for a team or for a company, but it also has an impact for the **quality of the code**. Indeed, some projects are detrimental for the quality of the code. In that sense, they’re toxic.

You may think: “if a project is toxic, then I just won’t do it!” Sure. But sometimes it’s not that simple. Some projects try to suck us in, blinding us from they toxicity, and entice us to carry them out.

Here are a few tips I have collected over time to identify those projects and interrupt them as soon as possible, in order to make code simpler in the end.

### Toxic project #1: The oops-that’s-not-what-we-need project

Picture this: to satisfy a requirement, you decide to start a new development project in your application. You perform a technical analysis to see how to implement it, you make your development plan, break down the features into stories, estimate them, plan them, and go off into coding.

Days and weeks go by, the project is moving on. One after the other, stories traverse the Agile dashboard, moving from the “Backlog” column all the way to the “Done” one.

Your team is writing code, reviewing code, implementing unit tests. The PO or whoever is requiring the feature is performing tests, giving feedback. You’re making progress.

But not far from the end of the project you realize, a chill running down your spine, that you shouldn’t have started the project in the first place.

There are various reasons this can happen. For example – it happened to me – the feature is not needed anymore (which itself has several reasons to happen: the client has found an acceptable work around or a simpler way to satisfy their business need, or they decide that they’d rather work with your competitor, or whatever).

Another reason – also happened to me – is that you haven’t understood enough how your development would satisfy the real business case. This can happen for example if you decide to implement a framework because you think that it will make your module compatible with the desired feature. And you realize at the end that you were wrong, the framework won’t help with the feature.

This is a hard one if you can make incremental tests that you’re implementing the framework correctly but can’t test the initial desired feature until you’ve fully implemented the framework.  All this came out of an approximate understanding at the beginning. This is why [you should refuse to develop what you don’t understand](https://www.fluentcpp.com/2019/07/09/you-should-refuse-to-develop-what-you-dont-understand/).

There are plenty of other reasons that happen and make you realize you shouldn’t have started a project in the first place (if you’ve been in that situation, please tell me your story in a comment!).

Those reasons may be out of your control. But what is in your control is what you decide to do, right now, with the project. And there is a little devil that wants you to make the wrong choice: the sunk cost fallacy.

#### The sunk cost fallacy

In economy, a sunk cost means a cost that you have spent and cannot recover. The sunk cost fallacy is a psychological bias that nudges you to invest more resources into a bad project that you’ve already invested sunk costs in, instead of stopping it, because stopping would admit the mistake.

In the above example of the software project your realize you shouldn’t have started in the first place, the right thing to do is to throw away everything you’ve done so far. But the sunk costs fallacy pushes you not to. Indeed, stopping the project would make the mistake concrete, and that you’ve worked for nothing. Who likes that?

The temptation is to think, “we’re far into the project, nearing the end, we might as well finish it off”. But by doing that, on top of having made a mistake and worked for nothing, the feature will sit in your codebase, adding its own complexity to the existing code. It will make all of your future developments more complex too, and for nothing.

When you realize your project is not needed and you’d like to carry on working on it, remember that you may be influenced by the sunk costs fallacy. Throw away the project. Every new dollar you invest in it is wasted, and will make you waste even more in the future by making your code more complex.

### Toxic project #2: The oops-that’s-harder-than-we-thought project

Let’s take the same story as above: requirement, dev plan, stories, estimates, and off we go in the implementation. But this time, the project doesn’t move on so smoothly. During the development phase, you are encountering difficulties you hadn’t anticipated.

There are various reasons this could happen (again, that all happened to me): you discover dependencies you didn’t suspect in that part of the code, or profiling tells you’ve impacted the application performance more than could be tolerated, or you hadn’t understood the requirement so well and it’s much more complicated than you thought, or you’ve impacted a lot of tests and you need to check them all, or whatever other reason.

There are plenty of other unanticipated difficulties that could rise in a development project. If you’ve faced some, please leave a comment too and tell us the story.

#### The value/cost ratio

At any given time, you should work on a project if the value (short or long term) it brings is higher than the cost it incurs. And if you have to choose between several projects, you should elect the one with the highest value/cost ratio. This is common sense.

It’s important to realize that value and costs ratio are **estimates**. We can’t know for sure how much a project will cost, or what it will bring in the end. We make estimates, and **those estimates change** when new information is available.

When we become aware of an unanticipated difficulties, this changes our estimate of the cost and, as a result, of the value/cost ratio of a development. Under the new conditions the project may no longer be worth it, if we now estimate that the costs of the remaining part outweighs the value the project would bring.

The sunk costs fallacy kicks in again, urging you to find a way to carry on. One way might be to be to ship the feature as it is. This can be detrimental to the code, if the feature is not really in a consistent state, because it will add this inconsistency to the codebase. Another way can be to find a couple of hacks to finish off the project in a quick and dirty way. This too is detrimental for the quality of the code, its expressiveness and your ability to work with it in the future.

All this adds up to the costs, and might make the best decision to throw away the work you’ve done so far. It it’s the case, have no mercy, and think that you’re making life easier for your future self as well as other developers.

### Toxic project #3: The maybe-we’ll-need-it-later project

One popular acronym to describe a best practice in software is YAGNI. It stands for You Ain’t Gonna Need It. This means that we shouldn’t develop features just in case we need them in the future, nor add unrequired capacities to an API, just because someone may need it at some point.

The rationale behind that guideline is that it is hard to anticipate what will be useful in the future, and that adding something now has a cost that is certain, by creating complexity. We therefore refrain from adding features that are not required now.

But some projects get delivered, sit in the codebase, and it’s only long after that we realize that they’re used by no one.

There is a temptation to think: we might just leave them here, they may well turn out to be useful one day.

The traditional application of YAGNI is during the development phase. But there is a form of YAGNI I feel we hear less about: **the YAGNI of projects that already sit in the codebase**.

If an existing piece of code is not used, just remove it. Don’t rely on the fact it could be useful in the future. It is detrimental in the present for sure: new developments in its vicinity have to take it into account thus making them harder to implement. Moreover, the new developments can break tests that cover the unused feature. But tests that cover a feature that is not used are a waste of time to analyse.

Those projects are just as toxic as the ones above, and you should root them out of the code with no regrets. The code that takes the less time to understand is the code that doesn’t exist. So if a project doesn’t have enough value, you should prevent it from entering or staying in your codebase.

Do you have other examples of toxic projects? How did you handle them?

### You will also like

*   [You Should Refuse to Develop What You Don’t Understand](https://www.fluentcpp.com/2019/07/09/you-should-refuse-to-develop-what-you-dont-understand/)

Don't want to miss out ? **Follow:**   [](https://twitter.com/joboccara "Follow me on twitter")[](https://www.linkedin.com/in/jonathan-boccara-23826921/ "Find us on Linkedin")[](https://www.fluentcpp.com/feed/ "Subscribe to our RSS Feed")  
Share this post!
