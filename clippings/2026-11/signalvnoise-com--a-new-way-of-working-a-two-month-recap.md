---
url: "https://signalvnoise.com/posts/2185-a-new-way-of-working-a-two-month-recap"
captured_at: "2026-11-16T04:16:36+00:00"
title: "A New Way of Working: A Two-Month Recap"
domain: "signalvnoise-com"
---

Back in early January [I posted about our new way of working in 2010](http://37signals.com/svn/posts/2099-2010-the-year-of-the-products-a-new-way-of-working). Instead of working individually in isolation as we had in the past, we’re breaking into small teams of three (two programmers, one designer). We’re keeping the teams intact for two months at a time. During those two months, the teams will work on four separate iterations, two weeks each. The goal is to drastically cut down scope, set short fixed deadlines, and focus on improving our products.

Now that January and February are behind us, and March is upon us, we can reflect on the first two month term. So how’d it go?

It went incredibly well. It was the most productive two month period we’ve had in a long time. It wasn’t all perfect, and some adjustments were required, but all in all we definitely feel like we made the right call switching to this new way of working.

Plus a variety of bug fixes, minor updates, infrastructure improvements, and design and language tweaks.

A lot. Here are some of the lessons we learned along with some of the adjustments we made along the way. We have a lot more to learn, but we think these early discoveries are going to make the next two-month term even better than the first.

## Lesson: Design needs a head start

Since we believe in [designing the interface first](http://gettingreal.37signals.com/ch09_Interface_First), we ultimately found it made sense for the programmers to take on a few small tasks or bug fixes on the first Monday, Tuesday, and Wednesday of an iteration while the designer was working on the UI for the first big feature of the iteration. This way no one was sitting around waiting for design to be ready before they could begin. With short two-week iterations there’s no time for anyone to sit around waiting for step one before they can start on step two.

## Lesson: Deploy along the way

If something’s done, get it out now. For the first iteration we waited to launch everything together on the last Friday of the iteration. That causes unnecessary stress and problems. So instead we started deploying every time a new feature was ready, whenever that was.

## Lesson: Friday deploys suck

Friday deploys suck. We wanted to maximize work time over two weeks so we typically worked on a project from the first Monday to the last Friday, and then deployed that Friday night. The problem was that any problems we missed had to be dealt with over the weekend. And that’s no good. We don’t want people working on the weekends. So we decided that final deploys should happen on the last Thursday of an iteration. This way we had a full Friday to deal with any lingering issues we missed or problems that popped up.

## Lesson: Get out the scope hammer early and often

For two week iterations, true scope should be nailed down no later than half-way through. We found ourselves up against the wall a few times because we didn’t cut scope early enough. So we decided that on Monday of the second week we’ll review the work done during the previous week and the work remaining to complete the iteration. Since humans are notoriously bad estimators, we’ll be extra conservative with scope. We’ll bring out the hammer and beat down the scope. And then we’ll do it again on Wednesday, two days before the end of the iteration. We want to throw work overboard, not our sanity or our sleep. Late nights are a sign of scope failure. Hero mode is a sign of scope failure. You can’t compartmentalize burnout. Yes, we start new iterations every two weeks, but burnout carries over. The scope hammer helps eliminate burnout.

## Lesson: Pick one, two, or three up front

We also discovered that sometimes one week or three week iterations are better than two week iterations. We experimented with a three week iteration for the last iteration of the two month term. It made sense for one of the projects (to be released soon), but it definitely contributed to sloppiness and missing the deadline on another project. With more time it was easy to say “We’ll deal with that tomorrow” or “We can worry about that next week.” Turns out when you start saying that you’re often already in trouble. Without a looming deadline you can feel (you can feel the pressure two weeks a lot more than three weeks), scope creeps and things get pushed off. So we decided that next time around we’ll experiment with one week, two week, and three week iterations — but that call needs to be made up front. You can’t start with one week and turn it into two or three. A team will say “This is a one weeker” or “This is a two weeker” etc.

## Here we go

The next two-month term started yesterday, March 1. We’re excited to take what we learned in the first two-month term and apply it to this next term. We’ll report back in early May.
