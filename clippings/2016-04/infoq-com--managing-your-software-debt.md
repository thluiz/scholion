---
url: "http://www.infoq.com/news/2014/03/managing-software-debt?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
captured_at: "2016-04-11T10:57:21-03:00"
title: "Managing your Software Debt"
domain: "infoq-com"
---

# Managing your Software Debt

Software debt exists in different ways. [Technical debt](http://www.infoq.com/technicaldebt/) is widely known, some other forms are competence debt and quality debt. Software debt can cause product maintenance costs to increase and can depress developers. Several solutions exist to manage software debt.

In the blog post [the other kind of software debt](http://www.leanway.no/competence-debt/) Niklas Björnerstedt talks about “competence debt”. He defines it as:

> The gap between what is in your codebase and how much of it you understand.

To keep software maintenance low you should pay attention to both technical debt and competence debt, as Niklas explains:

> Just as technical debt inexorably grows with time unless you fight it, competence debt also grows with time. The biggest difference between the two types of debt is that while technical debt grows faster the more you change a codebase, competence debt grows faster if you stop changing it! Competence debt is therefore a problem that is most acute in mature systems where active development has ended.

Niklas proposes two techniques that can be used to reduce your debt: programming in pairs and code refactoring:

> For me, the real value of pair programming is in reducing both technical debt and competence debt. By pairing, team members broaden the areas of the codebase they are familiar with and increase overlap. In a similar manner, the value of refactoring is not just the reduction of technical debt. Refactoring is a great way of reducing competence debt too. It is only when you can change a system that you truly understand it.

When competence debt is accrued the effort needed to maintain systems increases, up to a point where organizations start to consider replacing the system:

> People would claim that the old system was impossible to maintain when the real problem was that they did not understand how it worked. Yes, technical debt made things worse since the confusing code and lack of automated tests made it frustrating to understand the system. The impulse to rewrite typically comes when too few of the original developers are left and the business is unable to find new developers that are able or willing to learn.

Mike Hustler wrote a blog post about [the most agile way to manage technical debt](http://www.appneta.com/blog/agile-technical-debt/) where he discusses how to balance between developing product capabilities and managing technical debt. He explains how handing products over to a maintenance team can lead to increasing technical and competence debt:

> I have seen organizations build a separate maintenance team that is, for example, half the size of the new-feature team. In my opinion, this is the wrong approach (at least for the size of teams we work with). (…) The follow through which comes from the pride of ownership is lost because someone else is dealing with the bugs created by a different person, in fact a different team. Without solid communication, the backstory of why a certain initial approach was taken is lost. The domain knowledge is not present and thus the efficiency in fixing the issue is reduced. Even worse, I’ve seen maintenance teams of less experienced developers have trouble identifying the root cause of issues, resulting in band-aid fixes where rework would be preferred.

Technical debt depresses developers and can make them decide to leave which increase competence debt as Cory House described in his blog post [7 reasons clean code matters](http://blog.pluralsight.com/7-reasons-clean-code-matters):

> Writing sloppy or confusing code injects technical debt into our projects. And while technical debt can be useful when carefully considered in context, excessive technical debt is depressing and drives talent away from the organization. When the easy things become hard, developers start voting with their feet and go elsewhere. Developers derive more job satisfaction out of the quality of their work than the quantity. Technical debt decreases the chance of reuse and sets a low bar for quality throughout the rest of the code base.

David Hammerslag wrote the blog post [want predictability? Avoid quality debt](http://www.bigvisible.com/2013/10/want-predictability-avoid-quality-debt/) where he discusses the effects of leaving defects that have been found in the code unsolved. His definition of quality debt is:

> Quality Debt is a measure of the effort needed to fix the defects existent in a software product at any given point in time.

He compares quality debt with technical debt:

> Technical debt is a measure of the quality of the design and the code, which is the internal quality of the software. Quality debt is a measure of the external quality of the code, the things that the user sees and experiences. A user never (directly) sees technical debt.
>
> A program could be completely quality debt free and have a huge technical debt. It could correctly implement all the required and expected functionality and run flawlessly. Yet its technical debt could be enormous, exhibiting every poor software design and implementation you can imagine. On the other hand, the best designed, most sublimely elegant code could still produce wrong results or be missing functionality.

 Quality debt shouldn’t be ignored as David explains:

> Quality Debt is much like a financial debt: the older it gets the harder it is pay down. In the worst case a project puts off testing until the development is done. It is well established that the longer a defect ages the harder it is to fix. If many defects persist (either known or unknown) the effect is exacerbated as the defects mask each other, and fixes involve the same code.

 David suggests several agile practices that can be used to manage defects and keep your quality debt low:

> - Definition of Done.
> - BDD / Automated Acceptance Testing.
> - Continuous Integration.
> - Automated Testing.
> - Don’t tolerate “broken windows”.

### Tell us what you think

Email me replies to any of my messages in this thread
