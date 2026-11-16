---
url: "https://dev.to/iamdoomling/five-things-that-are-killing-my-productivity-as-a-developer-and-how-to-potentially-fix-them-1db"
captured_at: "2026-11-16T19:47:08+00:00"
title: "Five things that are killing my productivity as a developer (and how to potentially fix them)"
domain: "dev-to"
---

Lately I've had the rare opportunity to sit at home contemplating my daily routine and analyzing it to a fault (_thanks COVID-19_).

In doing so I've noticed that some days are _incredibly_ productive and others resemble something very similar to **what you get if you steam a bunch of pears for too long.**

I know productivity fluctuates like mood does -- and I always assumed it was which side of the bed I woke up that morning, but on a closer look I started noticing a **pattern that seemed to be linked to the team I was working with.**

As a frontend developer I’m usually assigned to multiple projects at the same time, but even if they have differences like which framework is used, the tasks end up being pretty much the same. I integrate API calls, use a lot of filter() and reduce() and fix the occasional padding. And I like all those tasks pretty much the same **so motivation wasn’t really related to complexity or fun in this case**.

But I found **some variables that do change between projects** and teams, and realized most of my productivity issues were related to those. So let me share my findings as they may shine a light on what's affecting you.

## [](#well-meant-but-illtimed-reviews)Well meant (but ill-timed) reviews

Reviews are a great place to suggest improvements or alternative, more performant resolutions to a problem. But what happens when that well-meant suggestion comes in the wake of a code freeze? It’s important to measure the **impact of the change versus implementation time**.

So before suggesting, ask yourself: _\- Will that particular dev be able to finish the rework before the deadline? Are you adding another task on top of a pile of unfinished work? \* \*\*Is it worth it?_\*

If it means refactoring most of the feature and the benefit won’t have too much of an impact then maybe **it’s better to open a backlog ticket to improve later**. Of course this only applies to code that **was already** **solving the issue in an acceptable manner**. Sometimes good enough is…**good enough**.

## [](#poorly-planned-meetings)(Poorly planned) Meetings

Yes, I was tempted to remove _poorly planned_ from the title, but let’s face it: **meetings are important for teams to get organized**. The problem arises when meetings don’t have a clear agenda or end up being a 1-1 conversation with all other members as spectators.

People start to lose interest and become drained, **and drained teams need to recover before being productive again**. So, to reduce the burnout risk make an active effort to keep meetings _short and sweet_, anything over the one hour mark should be a big no-no. Stick to a previously planned bullet-list **and learn to identify which conversations should be taken offline or rescheduled to 1-1 meetings.**

And remember, some meetings can actually be emails.

## [](#broken-things)Broken things

There’s an Allie Brosh blog entry called ‘_Sneaky hate spiral’_ which sums up pretty perfectly what I’m about to describe (_If you don’t know Allie Brosh, I’ll link to her blog at the end of this entry — she is no longer active but her writing should be considered an internet treasure_)

Picture this: you are about to start working on a new task, you try to build the project and something fails, you get an error, trace it back, try reinstalling, find out your database is too old, refresh, reinstall, get some weird error and at some point after a coffee and two hours scrolling stack overflow the project finally builds, **you have no idea which of the 200 thing you did worked** and you don’t remember what you were actually trying to accomplish in the first place.

So, you go back to the specs, check them out, try to start working and **BOOM: 500 from and endpoint, congratulations! you have been trapped in the sneaky debug spiral**, look a the clock, it’s 5pm, _goodnight_.

If you can’t relate to this scenario then I gotta say LUCKY YOU! (And is your company hiring? Just asking for a _"friend"_) but for many of us this is a very normal situation which can **rob us of a whole day of work**.

The key fix here is **communication**, let the team know if a core feature has new dependencies or needs any particular data setup to work and generate a safe work environment where people don’t fear asking questions. **Sometimes the solution is one slack away and you can save a team member from some nasty troubleshooting.**

## [](#constant-priority-switch)Constant priority switch

We usually work in projects that required a certain amount of flexibility, but when a team constantly needs to switch priorities around **it’s usually a symptom of bad planning.**

Switching tasks puts an extra weight on our brains, makes us lose focus and we take longer solving issues. **From a productivity point of view it’s a very costly decision, and it should be reserved exclusively to emergencies or top priority issues.**

Having a general roadmap that’s detailed enough to provide good guidance but leaving some extra room for the unexpected **is a great investment in any team’s productivity and mental health.**  
It can take longer to generate (and will probably require some meetings) but in the end the return will be worth it.

**And remember, if everything is top priority then nothing is.**

## [](#micromanagement)Micromanagement

Ah, _micromanagement_. So much has been said about this topic that I feel like the lady with the 'I can't believe we are still protesting this sh\*t'.

**For managers wanting to know status is healthy, and absolutely necessary part of their job descriptions.** One needs to know what’s going on, what’s done, what’s blocked and **why** in order **to make efficient decisions**.

**But micromanagement is not about knowing, micromanagment is about control and mistrust**. And trust goes both ways, so when an employee doesn’t feel trusted, it immediately impacts in their ability to trust the company and the team which ends up impacting productivity output. **Plus micromanagement is really costly in terms of time**. Instead of using that precious slot to push someone for results, use it to work on the general roadmap I mentioned earlier providing worth for the whole team.

Try communicating effectively and honestly. If you feel someone’s job is subpar or that they priorities are mixed then **ASK what’s going on**, and try to understand what they are saying.

Sometimes is not that employees are keeping things from you. Maybe they are not aware that something is affecting their output. **Keep an open door for constant feedback, and do keep it open both ways**. You _may_ find a rotten fruit in the basket but most people will react positively to this approach.

So that concludes my observations so far. I've tried changing some of this variables by bringing them up with my teams and so far, so good. Old habits are hard to break, but with good communication and attitude it can be done.

P.S: Now go have some fun: [Allie Brosh - Hyperbole and a Half | Sneaky hate spiral](http://hyperboleandahalf.blogspot.com/2010/05/sneaky-hate-spiral.html)
