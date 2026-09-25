---
url: "https://dev.jimgrey.net/2025/07/21/unlocking-high-software-engineering-pace-build-less-ship-frequently-learn-faster/?utm_source=bonobopress&utm_medium=newsletter&utm_campaign=2098"
captured_at: "2025-07-28T08:29:11+01:00"
title: "Unlocking high software engineering pace: Build less, ship frequently, learn faster – Jim Grey on software management"
domain: "dev-jimgrey-net"
---

---
_This is Part 3 of a series. See the introduction and full list of articles in this series [here](https://dev.jimgrey.net/2025/05/05/unlocking-high-software-engineering-pace/)._

When I work with software engineering teams, I see the same pattern over and over. They plan two-week sprints, fill them with tickets until they hit their velocity target, and then work hard until the sprint ends. They’ve made progress on whatever feature they’re building. But they haven’t delivered anything a user could actually touch.

This is what I call “waterfall in two-week sprints.” The team burns through work on a larger project until it’s eventually done. That might take five sprints, or 12, or 20. Everyone’s working hard, but the only evidence of progress is a burndown chart. There’s no working software and no user feedback — and thus no validation that you’re building the right thing.

![](https://dev.jimgrey.net/wp-content/uploads/2025/07/ship-at-killybegs.jpg?w=1024)

Ship at dock, Killybegs, County Donegal, Ireland

Meanwhile, your competitors are shipping. Your customers are waiting. Your engineers are frustrated (or, worse, disengaged) because they can’t see the impact of their work.

There’s a better way.

## What if you shipped something this sprint?

Instead of building the full feature, what if your team:

-   Modeled the core data and put it in whatever store makes sense
-   Built basic services to interact with that data
-   Created a simple UX that lets users do the most essential things
-   And then put it in front of real users — customers, prospects, your CS team — and got feedback?

You’d learn fast whether you’re on the right track. You’d validate assumptions early, when pivoting is cheap instead of expensive. And you’d start generating business value immediately instead of months down the road.

## How one of my clients turned years of requests into three sprints

Let me tell you about a client who built [ERP](https://en.wikipedia.org/wiki/Enterprise_resource_planning)/[PDM](https://en.wikipedia.org/wiki/Product_data_management) software for manufacturers in a particular niche. For years, customers had been asking for “Supplier Management” — functionality to track and manage relationships with the outside manufacturers who made parts for them.

In the PDM world, [Supplier Management is well understood](https://www.ibm.com/think/topics/supplier-management). It’s also massive. The full feature would take more than a year, to build, and the ROI wasn’t strong enough for it to make the roadmap.

Then a clever Product Manager asked a different question: what’s the smallest version of Supplier Management that could provide real value?

The answer: let customers add, edit, and inactivate suppliers. That’s it.

Two sprints later, they had it working. The Product Manager didn’t just demo it, she had it deployed live to Production. Customers could start using it immediately.

Within a month, customers had created hundreds of supplier records. More importantly, they started asking for one specific enhancement: when a quality problem occurred with a supplier’s component, they wanted to link that quality problem to the supplier.

One more sprint and that was done. And then something interesting happened: customers stopped asking for enhancements. They’d gotten what they actually needed.

## The business case for starting small

Think about what happened from a business perspective:

**Speed to value:** Instead of a months-long project with uncertain ROI, they delivered customer value in two sprints and validated demand immediately. Being first with “good enough” often beats being second with “perfect.”

**Risk mitigation:** They avoided the classic trap of building something comprehensive that customers didn’t actually want. They learned what mattered while the cost of changing course was still low.

**Resource and cost efficiency:** Three sprints instead of potentially dozens. That’s engineering capacity they could redirect to other priorities. Building smaller, shipping faster, and learning early means less wasted engineering time and budget.

**Competitive advantage:** While competitors were still planning their comprehensive supplier management systems, this client was already serving customers and gathering real usage data.

**Team morale:** Engineers got to see their work being used immediately instead of wondering if months of effort would pay off.

**Reduced opportunity cost:** By building exactly what customers needed rather than the comprehensive feature, the team freed up engineering capacity much sooner. Instead of spending months building features nobody would use, they could redirect that effort to the next high-value opportunity.

## Why this is hard (and how to make it easier)

The biggest challenge isn’t technical — it’s cultural. Engineers want to build things “the right way” from the start. Product Managers want to launch something they can be proud of. Stakeholders worry about looking unsophisticated.

But here’s what I’ve learned: the “right way” is the way that delivers value to real users as quickly as possible. You can always enhance, refactor, and polish later. You can’t get back months spent building something nobody wanted.

The key is being ruthless about what “smallest version” actually means. Not what would look impressive in a demo. Not what covers every edge case you can imagine. What would let a real user solve a real problem today.

That requires discipline. It requires saying no to good ideas so you can say yes to the essential ones. It requires leaders who can manage stakeholder expectations and teams who can resist the urge to over-engineer.

You have to coach your teams through this, and stay on top of it while they build. But my experience is that after the very first time they see customers happily using the small thing they’ve built, they never want to go back to the old way. Shortly you find you have a culture of shipping and learning.

Because in today’s market, the team that learns fastest wins. And you can’t learn until you ship.
