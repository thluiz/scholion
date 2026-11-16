---
url: "https://sachinrekhi.com/basecamp-shape-up"
captured_at: "2026-11-16T04:17:07+00:00"
title: "3 Compelling Concepts from Basecamp's Shape Up"
domain: "sachinrekhi-com"
---

![](https://substackcdn.com/image/fetch/$s_!qs1G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75a25597-071a-4bde-a03f-488fc859ff1f_358x505.png)

I always love reading each new book the [Basecamp](https://basecamp.com/) team publishes as they are inevitably chock-full of unique perspectives that preach an approach to working better that goes against conventional wisdom and established best practices. I don't always agree with every practice they preach, but I absolutely love reflecting upon diverging opinions that challenge my own assumptions. The Basecamp team does a fantastic job of thinking from first principles, questioning the status quo, and coming up with novel practices that they've carefully battle-tested on their own team over the last 15 years of developing Basecamp.

Their latest book, [Shape Up](https://basecamp.com/shapeup) by Ryan Singer, delivered another compelling read on effectively managing software projects. The book shares the full software development process that the Basecamp team currently uses across it's 50-person team to build and enhance Basecamp itself. As always, it preaches a uniquely Basecamp way of doing things. Jason Fried says so himself in the foreward:

> For one, we’re not into waterfall or agile or scrum. For two, we don’t line walls with Post-it notes. For three, we don’t do daily stand ups, design sprints, development sprints, or anything remotely tied to a metaphor that includes being tired and worn out at the end. No backlogs, no Kanban, no velocity tracking, none of that. We have an entirely different approach. One developed in isolation over nearly 15 years of constant trial and error, taking note, iterating, honing in, and polishing up. We’ve shaped our own way.

While the book covers many aspects of the software development cycle, I wanted to share the three concepts I found most compelling.

Before even considering a project for building in an upcoming cycle, the Basecamp team always shapes the work. The idea is to make an abstract project idea more concrete by defining key elements of the solution before betting on it. A small group of senior members work on shaping projects in parallel to all the execution teams that are focused on delivering projects that have already been shaped and approved.

The key with shaping projects is it isn't equivalent to putting together a product spec for the project. It's instead at a higher level of abstraction: concrete enough that the teams know what to do, yet abstract enough that they have room to work out the interesting details themselves. As part of shaping a project, you might put together a fat marker sketch, which is a low-fidelity UI sketch of the solution that conveys a high-level design without actually defining the details. You also define an appetite, which is how much time you want to spend on this project based on how much you believe this project is worth in terms of customer and business impact. This is opposed to simply coming up with an estimate of how long the project will take. Each of these elements ultimately gets put together in a short pitch, a document that presents the problem, the appetite, and the solution of the now-shaped project idea for consideration in the roadmap.

[

![](https://substackcdn.com/image/fetch/$s_!aS-Q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefa52ffc-3ee2-4045-8550-ab908ab94460_972x1010.png)

](https://substackcdn.com/image/fetch/$s_!aS-Q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefa52ffc-3ee2-4045-8550-ab908ab94460_972x1010.png)

The reason this approach is compelling is it allows you to better understand the consequences of taking on a potential project during roadmap planning. Too often in roadmap planning we approve high-level projects like "Redesign the homepage", "Add a calendar view", etc without fully understanding them. We leave it to the teams to figure out the details and deliver a solution. The challenge is after approving the project, we might not like the ultimate outcomes. The finalized design might do far more damage to the overall product experience than good. Or the project might overrun it's initial estimate, derailing all our other plans. By shaping the work upfront and understanding what the potential solution might be before deciding to take on the project, we significantly reduce the uncertainties associated with accepting the project.

While we've never used the term shaping a project, we actually do this regularly at [Notejoy](https://notejoy.com/). We take on investigation tasks that are all about coming up with a high-level approach to a problem to help us decide whether it's worth taking on the project in an upcoming cycle. Sometimes these investigations end with unsatisfactory solutions so we punt on the project. Other times we come up with elegant solutions that get immediately prioritized. We've found the approach to be far better than just taking on the project when we have limited information about it upfront.

Another critical concept the Basecamp team talks about is the betting table, which is their take on a roadmap planning meeting. In this meeting they bring together a few senior leaders at the company (CEO, CTO, head of strategy, and senior eng leader) to decide the projects for the upcoming 6-week cycle based on the pitches that were prepared to be reviewed. Everyone has already had a chance to deep-dive into each shaped project by pre-reading the pitches. This allows the discussion to be very focused on debating each pitch and deciding on it's inclusion relative to the priority of the other pitches. During a betting table meeting, they may debate for each pitch how important the problem is worth solving, debate whether the appetite is the right one for this problem, and even debate whether the proposed high-level design is an attractive solution.

This process ends up allowing the senior team to be far more involved in ensuring the right projects are green-lit based on a holistic view of the problem being solved, the resources required to solve it, and the elegance of the solution as opposed to taking a far riskier bet on a raw idea and simply hoping the team comes back with a properly scoped great solution. It's also far more cost effective than making these calls in late-stage product reviews where it's so expensive to make any meaningful changes to the product when it's already begun implementation.

The process also ends up being far lighter-weight than a traditional spec review process that often precedes implementation of a project. While this traditional process does allow the senior team to review critical elements of a proposed solution before implementation, the fact that it's heavier-weight means that it's traditionally only used for large endeavors and usually skipped for small feature implementations, which usually don't enjoy senior oversight and consideration, which can result in feature implementations that aren't cohesive across the entire experience nor appropriately scoped relative to the level of impact.

![](https://substackcdn.com/image/fetch/$s_!DStt!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f919828-c522-4f0c-a5e5-a2789046c8b4_2560x1000.gif)

The Basecamp team has also reinvented ongoing project status by creating an alternative mechanism for sharing how far along each project is. Traditional project management status struggles with a few issues. Some teams simply look at the number of tickets for a given project and chart the completion of those tickets to provide status. Of course not every ticket is created equal so this gives you a poor sense of project progress. Even if you added estimates to each ticket, as projects progress, more tickets are created as new implementation details are discovered or new bottlenecks are understood. This results in an increase in the number of tickets, which means any initial estimate you were making based on the tickets is still wrong. While you can spend significant time upfront coming up with all implementation tasks and scoping a project, this is often wasted effort when its more realistic to discover detailed tasks as the project progresses.

Basecamp throws out these traditional approaches to ticket-based project estimation and status and replaces it with a hill chart, which is a diagram showing the status of work on a spectrum from unknown to known to done. Early in a project, when you are going uphill, you are still discovering all the edges of the work, creating lots of new tasks as you progress. Once you've understood the full solution, you move from the unknown part of the project to the known part of the project where you're simply executing against the tasks that are well-defined and understood. What Basecamp does it create a hill chart for each project and plot each project scope, or component, along the hill chart, giving you a high-level view on where the team believes it is on each of the project components. Leaders can see the current status, but more importantly, track movement across the hill charts. Project scopes that remain stuck are areas for leaders to drill in to see if they can help resolve the bottleneck.

This far simpler project status approach requires far less effort to keep up-to-date but still provides leaders with the transparency they need in order to understand where projects stand and be able to offer to help when needed.

If you've found any of these concepts interesting, I would encourage you to check out [Shape Up](https://basecamp.com/shapeup), which the Basecamp team has made available for free as a web book.

**Whenever you’re ready, here are 3 ways I can help:**

1.  **[AI Productivity](https://www.reforge.com/courses/ai-productivity)**: Learn how leading product managers use AI to become faster, smarter, and gain super powers beyond their traditional role.
    
2.  **[Mastering Product Management](https://www.reforge.com/courses/mastering-product-management)**: Accelerate your product career by learning rigorous frameworks for each PM deliverable, from crafting a strategy to prioritizing a roadmap.
    
3.  **[Product Innovation Strategy](https://www.reforge.com/courses/product-innovation-strategy)**: Building a new product? Learn how to leverage the Deliberate Startup methodology, a modern approach to finding product/market fit.
