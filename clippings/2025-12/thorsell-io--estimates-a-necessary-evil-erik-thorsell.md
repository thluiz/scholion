---
url: "https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter"
captured_at: "2025-12-08T18:43:49+00:00"
title: "Estimates – a necessary evil? - Erik Thorsell"
domain: "thorsell-io"
---

---
> **Product Owner:** Hey, how long do you believe `Feature F` will take?
> 
> **Developer:** Idk. We haven’t even started working on it and it’s bound to stir up some old issues.

Estimates come in various disguises, but when you peek under the trench coat there is always the question:

"How long -- and using what amount of resources -- will be required to do `X`?"

When I wear the _developer hat_, it can be infuriating to attempt to give an answer. It’s difficult to estimate (or the product owner could do it themselves) and a lot of the time it can be difficult to see why the estimate is even important.

When I wear the _product owner hat_, estimates are a crucial piece of the puzzle that must be laid in an attempt to plan the short _and_ long term life cycle of a product.

In this post I want to attempt to explore and elaborate on both sides, in an attempt to make developers understand _why estimates are important to product owners_ and in order to help product owners see _why developers so often despise having to estimate their work_.

## Why the PO wants you to estimate[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#why-the-po-wants-you-to-estimate "Permalink")

As a Product Owner (PO), I am responsible for _learning the market and customers’ needs_ and translating these into _feature requests which developers can turn into actual features in our products_. The means varies, but most organisations have some sort of backlog in which _things to be acted upon_ are placed while they await being _picked up_ by some developer or development team. We call these _things_ user stories, issues, tickets, tasks, _and probably many other things_… The important thing for this discussion is that the items in the backlog are candidates for being implemented in our product and it’s the PO’s job to prioritise the backlog.

Why does the backlog need to be prioritised?

Because the inflow of items to the backlog is (pretty much always) higher than the speed at which the developers can implement them. Ergo, if the PO does not constantly _learn the market and customers’ needs_ and prioritise the backlog accordingly, the developers might implement features that the users of the product are not interested in. Worst case? Existing users stop using the product and no new users buy it which will ultimately lead to bankruptcy.

### But what about the estimates?[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#but-what-about-the-estimates "Permalink")

The above makes sense – I hope – but it doesn’t really pinpoint the need for estimates. Unfortunately, the job of a PO is not as easy as always prioritising in accordance to whatever the market wants. More often than not, the PO must also consider pre-communicated release dates and manage expectations.

> I hate when release dates are communicated in advance. The only thing worse than release dates that are set in stone months ahead of time (I’m looking at you, Mr 12-week-increments-SAFe) are releases with pre-communicated content. Unfortunately, both are common. Often combined.

Imagine a backlog in which resides a really big feature. Something that is sought after, but will take a lot of time and resources to implement. The same backlog has a handful of smaller features which are not as requested as the big one. The PO would really like to include the big feature in the next release, but the next release date is not so far away. If the PO prioritises the big feature but it’s not done in time for _the already communicated release date_, the release will be severely lacking and considered a failure. In that case, the PO would rather include a couple of the smaller features. A safer bet, but the payoff is smaller.

**THIS** is why estimates matter so much to product owners. They must constantly run the above equation when they prioritise the teams’ backlogs. A constant risk/reward balancing act. They undoubtedly need help from the experts (the developers) to better understand the ramifications of the features they are proposing. If POs do not understand how big different _work packages_ are, they cannot do their jobs in an effective way.

### It gets worse[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#it-gets-worse "Permalink")

Instead of one PO there are now a couple of them. They are responsible for different _parts_ of a larger product which requires the POs to coordinate both the date _and_ the content of their releases. There is probably a _main backlog_ describing upcoming features in the final product, as well as _team backlogs_ where each team are assigned puzzle pieces which must be implemented and integrated in a coordinated fashion.

This is painful in multiple ways, but the most obvious issue is that – in order to have a functioning release – the POs must agree on the prioritisation of the _main backlog_ and this will in turn affect the prioritisation of the _team backlogs_. The POs must each acquire information about how long it will take (and how costly it will be) to implement and to integrate the puzzle piece(s) they are responsible for into a cohesive feature. The tool for acquiring this _idea_?

Estimates.

## Technical debt[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#technical-debt "Permalink")

Programming is a craft. An art. My art, to some extent. I’m in my happy place when I get to succumb to a tricky task and surface a couple of days later with a solution to a problem that initially seemed impossible. As a developer, I want to build the best possible product. I dislike shortcuts. Half-arsed solutions. _Fixes._ Not because a single shortcut or fix will destroy a product, but because the [_technical debt_](https://en.wikipedia.org/wiki/Technical_debt) they incur will accumulate over time and eventually erode the product from the inside out; making it ever more difficult to work with it and ultimately cause it to break.

Technical debt is – I believe – the main reason for conflict between a PO and a development team. A not so technically inclined PO will fail to see how detrimental technical debt is to the product and how painful it is for the developers to work in a code base with a high amount of debt.

Put in other words: If I’m tasked with implementing a new feature and I come across something in the code that is obviously smelly, error prone, or just not very good, I want to leave the code in better shape than I found it. Not taking time to “payoff” such debt _once_ might not be the end of the world, but the hard coded quick-fix that you know ought to be generalised will likely bite you down the road. And if you have ignored updating dependencies for a couple of months and find yourself in a situation where you _need_ to upgrade `Package 1`, but it depends on a newer version of `Packages 2 & 3`, which in turn requires a framework upgrade… Let’s just say the feature you’re working on will take a while longer.

## Why developers HATE estimates[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#why-developers-hate-estimates "Permalink")

When a PO asks: “How long will it take to implement `Feature F`?”, they aren’t just asking the developers to estimate the amount of time they think it will take to write the code for the feature. A good PO understands that implementing a new feature is an iterative process and that _integration hell_ is a thing. An even better PO understands that they are also asking the team to estimate how many unforeseen issues they will encounter while implementing the feature.

This detail: _The unforeseen issues_, which the PO asks the developers to foresee, is key. It is – per definition – not possible to foresee something unforeseeable.

Many developers I’ve met dislike uncertainty. One of the things they appreciate most about coding is the deterministic aspect of it. You run the same program again and again and it returns the same results.<sup id="fnref:determinism" role="doc-noteref"><a href="https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#fn:determinism" rel="footnote">1</a></sup> The journey on which we travel while writing the code is, however, not particularly deterministic.

It is true, that the more you code and the more familiar you get with a codebase, the more accurate your estimates will be. However, just the other day I was working on an issue which I had estimated would take _approximately two days_. All of a sudden, I realised that the simple change required updating a shared component that had been tightly coupled years ago. When I touched that code, dozens of failing tests appeared, each revealing another hidden dependency. Fixing those uncovered yet another module depending on outdated patterns. Halfway through, we decided we had to refactor the entire flow just to make the original change safe. My “two-day task” turned into two weeks of archaeological software excavation.

Could we have solved this quicker by not caring so much about the amount of technical debt we left in our wake? Probably.

Would we have encountered a two _month_ excavation in the future? Probably.

### It gets worse[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#it-gets-worse-1 "Permalink")

[According to Merriam-Webster](https://www.merriam-webster.com/dictionary/estimate): _estimate_ is defined as:

> To judge tentatively or approximately the value, worth, or significance of.

The very definition of _estimates_ tells us that they are either _tentative_ or _approximate_. As a developer, I choose to interpret the _or_ as meaning that it could even be both.

When I started my career as a software developer, I really did not have an issue with estimates. We would refine our backlog and I would gladly give an estimate on various items. (1) Because I was fresh out of university and wanted to prove myself by doing a good job and not being too difficult, but more importantly: (2) because I had not understood that my estimates would soon be used against me.

I soon learned that my team’s estimates were not interpreted and used as _estimates_. They were used as _deadlines_. If we broke down a feature into its reasonable components (an error prone science, which introduces uncertainties, on its own) and estimated the parts accordingly, the PO would often take the sum of the parts and communicate it to their colleagues as: “This is the time we will be done.”

Two things came out of this:

1.  My team (consisting mostly of newly graduated developers) became much more reluctant to estimate.
2.  When we estimated we always padded our _actual beliefs_, significantly, to give ourselves a buffer.

The estimates stopped being estimates. They became safety railings against being held accountable for unreasonable expectations.

## The clash[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#the-clash "Permalink")

Do you see the problem?

Do you see a solution?

I believe the overarching problem with estimates stems from expectations. Somewhere, someone, communicates _something_ to the users/customers of the product, which sets expectations the rest of the organisation are then forced to live up to. In a small company, it might very well be the PO who does that communication but in a larger organisation the PO is likely as helpless as the developers w.r.t. having a say about the product’s roadmap.

The “solution” is simple: Stop communicating new features in advance. Stop setting more or less arbitrary deadlines<sup id="fnref:deadlines" role="doc-noteref"><a href="https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#fn:deadlines" rel="footnote">2</a></sup>. Let the PO tell the developers what features they want, in what order, and let the developers do what they do best: Code!

But these deadlines are there for a reason. If your company builds a product which assists people doing their yearly tax returns, a missed delivery window will result in the entire revenue opportunity for that year being missed. Resources (most often in terms of salaries to employees) will have been poured into a project and if there’s no payoff in terms of additional sales, it could lead to a need for finding other ways to reclaim those resources; often in terms of reduced costs, which universally means: lay-offs.

Therefore, it’s in everyone’s best interest to play along. We play the estimates game even though it’s a bad way (but also the best we know of) to help each other do our respective jobs.

## What about DevOps?[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#what-about-devops "Permalink")

_You didn’t think I’d miss an opportunity to talk about DevOps, did you?_

_Flow_ is a key concept within DevOps which describes an organisation’s ability to reduce bottlenecks and increase the pace at which they are able to deliver new versions of their product(s). High flow is synonymous with frequent deliveries and updates of our product(s).

The concepts from DevOps do not directly address the issue with estimates, but there are tools which can be used to reduce the risk associated with delivering software. Flow can inform how we tackle technical debt and how we make sure we don’t fall behind on our dependencies. Flow can also help us identify issues in our product’s life cycle as well as help us understand how to get rid of the issues.

Flow is one of [_The Three Ways_](https://itrevolution.com/articles/the-three-ways-principles-underpinning-devops/) in DevOps and if you want to learn more, feel free to reach out. I give presentations on various topics related to DevOps and I can come to your company and give a course about DevOps tailored to your company’s needs.

## Conclusion[Permalink](https://thorsell.io/2025/12/07/estimates.html?utm_source=tldrnewsletter#conclusion "Permalink")

Estimates – as defined in the English language – isn’t really the problem here. The problem is when _estimates_ are treated as predictions, deadlines, and used to put pressure on developers who are just trying to do their jobs. Estimates – the way they are used in our industry today – hurts people and reduces the psychological safety in our organisations. I believe we would be better off if we could work in a way that allows developers to be transparent and continuously communicate updated estimates as development progresses.

Then again, product owners are people too! As developers we must understand that POs are under pressure too. We must help them and the best way to help them is to continuously provide them with updates about how development is progressing and whether we have encountered anything that we believe will significantly alter the original estimate we gave.
