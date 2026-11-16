---
url: "https://blog.plataformatec.com.br/2016/07/key-points-to-consider-when-doing-a-big-software-refactoring"
captured_at: "2026-11-16T03:24:46+00:00"
title: "Key points to consider when doing a big software refactoring « Plataformatec Blog"
domain: "blog-plataformatec-com-br"
---

The second post of Low Internal Software Quality series.

Doing a big software refactor[1](#fn-refactor) is not a simple thing. There are lots of points that you should think about, from planning and prioritizing to team motivation and execution. Understanding these points in a structured and clear way is part of the job. The good news is that we’ve been in that situation before and have learned the key points you should worry about.

Here are the main points you should consider when planning and executing a big refactoring process.

### Define your business goals

A big software refactoring process should not be started without clear business goals, otherwise it can suffer from a lack of commitment by your stakeholders. Here are some examples of goals:

*   We’re doing a refactor so that we can plug in multiple payment gateways.
*   We’re doing a refactor so that we can improve velocity.
*   We’re doing a refactor so that we can have a multi-tenant architecture in order to simplify our infrastructure operations.

### Measure progress

By its very nature, a software refactoring process is a technical effort, which is why it’s common for people not to measure its progress in the same structured way that they measure progress on development of new features. Don’t fall into that trap.

As with every task in a project, a refactor should always be planned and [measured](https://blog.plataformatec.com.br/2016/02/why-we-love-metrics-learning-with-lead-time/).

### Pay attention to your team’s motivation

Working on a legacy codebase can be demotivating for developers, especially if they don’t have a feeling of progress, or if they don’t know when it’s going to end. When going with a refactoring process, you should keep this in mind.

Show your team they’re moving forward. Plan for small deliverables, so that you can continually ship stuff and celebrate the good work done. Also, think about developer rotation, which can help by maintaining motivation and keeping fresh eyes on the task.

### Define your approach: pull or push?

Are you going to improve your codebase only when touching some bad part of it, or are you going to proactively choose which parts you’re going to improve?

### Prioritizing

If you have a clear business goal, it’s easier to proactively choose which parts need to be improved to make that goal a reality. With the parts listed, you can apply your usual prioritization techniques.

But if you’re going to do a constant and big software refactor because you know the whole codebase needs to be improved, it’s more difficult to prioritize. This is because there are not just one or two main parts that need improvement, but lots of them. It’s difficult to know where to start.

One way to prioritize in that situation is to instruct your team to evaluate which parts need to be refactored based on their complexity and churn. By that we mean, whenever they are evaluating if some part of the code should or should not be refactored, they should ask themselves:

*   “Is the complexity of that class too high compared to the others?”
*   “Do we constantly need to make changes on that file?”

If the answers are both yes, that part is a good candidate for refactoring. Plot a chart of “class complexity X churn” and prioritize the parts that are too complex and that you’re changing every time.

The parts that have big complexity but don’t need to change constantly are not good candidates to be refactored because they’re parts that are ugly but usually work, and nobody needs to change them to do their everyday job.

### Know when you’re done

A software refactoring process can turn into an endless endeavor if you don’t plan, prioritize and measure progress. You should treat it as a project. It should have a beginning, a middle and an end.

### Test suite coverage

Your refactoring process should improve stuff that is already working without breaking anything. Make sure you have good test coverage, otherwise the process can generate more bugs than quality improvements.

### Test suite performance

If your test suite is too slow, it will slow down the refactoring process since a software refactor is greatly based on continuously running the tests. Make sure the test suite performance is not a bottleneck.

### Sponsors commitment

A refactoring process can take a long time: weeks, months. During that time the velocity in which new features are delivered will be compromised. Make sure that every business stakeholder understands the goals and the nature of that kind of work, so that they don’t give up in the middle of it.

What about you? Do you have any more tips on what to worry about when doing a big software refactor? Share with us!

* * *

1.  _I prefer the term “code refurbishment,” but people aren’t generally used to it. So I’m using “refactor” in this blog post for the sake of clarity. [↩](#fnref-refactor)_

* * *

Tags: [CTO](https://blog.plataformatec.com.br/tag/cto/), [refactoring](https://blog.plataformatec.com.br/tag/refactoring/), [software](https://blog.plataformatec.com.br/tag/software/), Posted in [English](https://blog.plataformatec.com.br/category/english/), Comments Off on Key points to consider when doing a big software refactoring
