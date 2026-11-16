---
url: "https://web.archive.org/web/20200314110847id_/https://killalldefects.com/2019/12/31/top-five-takeaways-for-improving-software-quality/"
captured_at: "2026-11-16T08:00:30+00:00"
title: "My Top 5 Ways to Improve Software Quality from 2019 - Kill All Defects"
domain: "web-archive-org"
---

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2019/12/Quality.png?w=770&ssl=1)

_Photo by [Kira auf der Heide](https://unsplash.com/@kadh?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/gem?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_

In early 2019, the development team I manage was given an extremely aggressive goal of achieving an unprecedented degree of software quality. Because of the quantity of legacy code and technical debt I manage, I knew we would have our work cut out for us.

What followed was an obsessive search for any and every way of improving software quality and doing _whatever it takes_ to prevent bugs from reaching the end user.

I started my website [Kill All Defects](http://https;//www.KillAllDefects.com) to host a collection of thoughts on software quality, but even so, some practices and technologies stood out as ones I should share with the community at large.

And so here we are: a .NET and TypeScript development manager’s top 5 quality practices from 2019, in no particular order.

## Celebrating Quality Practices

Too often we celebrate late night heroism and doing what it takes to get things done for a critical deadline or to patch a debilitating bug. These things _are_ praiseworthy and _should_ still be praised, but they shouldn’t be the main thing being praised.

The problem is that we tend to celebrate the fire fighters kicking down doors to solve problems instead of the fire marshals who quietly do their job to prevent the fires from breaking out in the first place.

The only way the fire marshal gets praised is if you explicitly look for activities of heroism to ensure quality before things go out the door and so, as managers and team members, we need to do this.

When you see a colleague or employee taking active steps to guarantee software quality, get early warnings of defects, or make entire classes of defects impossible to begin with, this needs decisive and formal praise both in private and in public.

This should be a big deal. Bigger than completing a critical feature on time or fixing an urgent issue.

Why?

Because as much as we say quality is important, people recognize what an organization rewards and talks about. Because of this, we need to make sure that achieving stellar quality while paying down technical debt is something that is baked into our teams and organization or the quest for quality will never be truly real.

## Code Review has a HUGE Return On Investment

At the beginning of 2019, I was reviewing all code for my team. There were other reviews sometimes in addition to me, but I looked through code at a high level to see what types of changes we were making, if tests were present, if the right code patterns were being followed, and if technical debt was being paid down with every commit.

It wasn’t enough.

It wasn’t until I looked at the aggregated data for the first half of the year that I began to notice trends in the types of bugs we were encountering and the mistakes we were making that got past code review.

And what I found told me that the quick skim I was doing as part of code review wasn’t enough.

By doubling or tripling the amount of time I spent per merge request coming my way, I was able to:

*   Give my team more of a shield from potential defects by catching more issues
*   Understand each change more fully
*   Spot more teaching moments to communicate best practices

Of these three benefits listed above, you’d think the first would be most important, but it turned out that we got the most benefit by focusing on code review as an opportunity for individuals to learn more about the software, programming in general, and software quality.

On top of that, we instituted a 2 reviewer policy where each merge request should have at least two reviews – preferably someone more senior and someone more junior. This helps others learn more from how others are programming and how others are reviewing software.

I also made it a standard practice to challenge people by asking them how they know the commit works and does not cause other issues. It’s a silly little thing, but it turns out that by knowing that they _will_ be asked on test plans prior to things going to quality assurance, engineers are more diligent about testing their code and documenting the work they’ve done on that front (which helps me recognize and reward that effort).

Overall, by decreasing my own capacity each sprint slightly to make room for more dedicated time in code review, we drastically improved our overall quality and skill level of the team.

## Pinning Tests Are Invaluable

The best book I read in 2018 was [Working Effectively with Legacy Code, by Michael C Feathers](https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052). It wasn’t until 2019 that I fully put some of its practices in place, however.

Specifically, Michael discusses the concept of a “Pinning Test” – that is, a test designed to pin the current application behavior in place. Right or wrong, if any future change causes the system to act differently, a pinning test should fail.

These are most effective at calculation or transformation-based algorithms and things like [reducers](https://killalldefects.com/2019/12/28/rise-of-the-reducer-pattern/) and I work with plenty of those.

My earliest pinning tests were manual tests where I compared objects by checking properties against expected results, but these were extremely tedious.

And then I met [Jest](https://jestjs.io/). Jest is a JavaScript unit testing framework that has, among other things, something called snapshot tests. Snapshot tests serialize an object to JSON and compares that JSON against the stored JSON snapshot of the original object’s state from when the test was first run.

This effectively lets you write a pinning test in a single `ShouldMatchSnapshot` assertion, which is both incredibly powerful and potentially very easy to abuse. Not every test should be a pinning test – most shouldn’t, but you need a few broad tests to provide a safety net while you get he more specific behavioral tests in place.

For more information on snapshot based tests in JavaScript or .NET, [see my article on the subject](https://killalldefects.com/2019/08/30/snapshot-testing-in-javascript-net/).

The critical thing to stress about these tests, however, is that without the broad coverage of pinning tests, I would not have had the courage to pay down technical debt to the degree that I did this year, or with the same level of courage.

## Pay Down Technical Debt Scientifically

Between late August and the end of 2019, I wrote around 80 articles. But if I had just one library I was able to share, it be the Scientist series of libraries.

Scientist allows you to compare a legacy implementation of something with a new implementation of that same thing and compare the results and performance of both algorithms.

You might be wondering how this is different than snapshot testing as I mentioned in the last section.

The main difference here is that Scientist is designed to run _in production_ on data from actual end-users and not the various pieces of test data you throw at it during development and testing.

This is where Scientist’s key strength comes in: If I write a new version of something that is faster, more efficient, more maintainable, but errors for 5% of users, I might never see those problems until the code goes to production. With Scientist, the errors in the new routine will still be present, but the user will get the results of the legacy version of the algorithm.

![In cases where the new routine errors or doesn’t match the old, the results can be recorded and fixed later and the customer is ignorant that an issue even occurred.](https://i0.wp.com/res.cloudinary.com/practicaldev/image/fetch/s--K_ZTM6A2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://imgur.com/FDAgrQO.png?zoom=1.25&w=770&ssl=1)

This means that we can effectively canary test our new code in production without introducing any defects or adverse behavior to any end user. If an error _does_ occur, we can log it to some form of [exception monitoring service](https://killalldefects.com/2019/11/23/monitoring-quality-with-error-tracking/), log file, or database. We can then ship a new version with that fixed implementation at our leisure and confirm that no further errors occur.

Only once we’re fully satisfied with the quality of the new code do we remove Scientist from the mix and have the new version of our code take over.

For a detailed look into this, check out [my article on Scientist .NET](https://killalldefects.com/2019/12/08/experimental-csharp-with-scientist-dotnet/).

## Code Quality Needs to be Something you Can Communicate

Every one of us deals with technical debt to some extent or another.

Technical debt is a natural byproduct of changing priorities, scope changes, technological innovations, and us growing in skills and talent over time.

But technical debt is something that only matters to developers unless you can communicate it in a way that product management and business management can understand.

Think about it this way: If I come up to you and ask you about your technical debt, what would you tell me?

If I asked if it was getting better or worse, what would you say? Could you prove it?

If I asked where technical debt is causing the most issues in terms of productivity losses and bugs emerging, could you answer that accurately?

If I gave you a day to spend on technical debt, where would you spend it? What about a week? Why would you spend it in that area? Would you be ready to go without planning around the effort?

All of these are perfectly reasonable questions. In fact, these are _softball questions_ where I’m not explicitly trying to challenge you by saying your technical debt isn’t important.

So here’s my point: technical debt amounts to a nebulous specter to the business unless you can illustrate it to them.

This is a complex and nuanced topic, and one I’ve written a lot about.

A good place to start might be my article on [communicating technical debt](https://killalldefects.com/2019/10/01/communicating-technical-debt/).

If you’re working with people without much understanding of tech debt, you might appreciate [Defining Technical Debt](https://killalldefects.com/2019/12/23/defining-technical-debt/).

If your organization believes technical debt isn’t truly something that impacts the business, you may want to read [The True Cost of Technical Debt](https://killalldefects.com/2019/11/09/the-true-cost-of-technical-debt/).

If others are aware of technical debt but hesitant to prioritize paying it down, I recommend working with them to [treat technical debt as risk](https://killalldefects.com/2019/12/24/technical-debt-as-risks/).

And finally, if you want to always have empirical data around trends in code smells, you can look at automated code analysis tools such as [NDepend for .NET](https://killalldefects.com/2019/11/02/tracking-dotnet-code-quality-with-ndepend/).

Yes, I know, that’s a lot of links, but tech debt is an incredibly nuanced topic and it’s very difficult to condense many broad articles into a single section of a year in review article.

## Closing Thoughts

I’ve thrown a lot of things your way. I often do this. I like to introduce others to many tools and practices they may not have considered so that they can investigate them more when and if they make sense.

If there’s anything in this collection of topics that you’d like me to drill into more, I’m happy to do so as I charge ahead into 2020.

As for my team: while we still let a handful of bugs get into the wild, these were generally very benign and quickly remedied. These tips and techniques I’ve outlined here have had a pronounced impact on how we develop software and develop teams with a true culture of emphasizing software quality.

Best of luck to you in your future and may 2020 be one with defects few and far between.
