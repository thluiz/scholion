---
url: "https://dev.to/coss-media/lessons-in-managing-a-distributed-team-46i3"
captured_at: "2026-11-16T19:10:47+00:00"
title: "Lessons in Managing a Distributed Team"
domain: "dev-to"
---

Building a 100% distributed, or remote first, workforce is becoming more popular for tech companies. Some notable ones are: GitLab, Basecamp, Hashicorp, Automattic, and of course our beloved DEV. _(If I missed any, please leave a comment, and I’ll keep updating this list.)_

Having recently just built and managed a globally distributed team at [PingCAP](https://pingcap.com/en/), a classic commercial open source software (COSS) company built on an open source distributed database [TiDB](https://github.com/pingcap/tidb), both the joys and complications of working in a fully distributed fashion are still fresh in my head. For context, our global team had employees, both technical and non-technical, that spanned three countries (the U.S., Canada, New Zealand). Not only did we work amongst ourselves, we also collaborated and coordinated with a much larger team in China, which was also distributed across six cities. “Global” in my case simply meant anywhere but China.

Since the virtues of a fully distributed team have been articulated in many other places, I want to instead share some lessons I learned from operating one, so you can build your own with a clear-eyed approach. A fully distributed team is totally the way to go, especially if you are building a COSS company, because remote collaboration is ingrained in the open source DNA. But nothing is all sunshine and rainbows, tradeoffs exist in every situation, and the more aware you are of what they are, the more sunshine you will get to feel.

## [](#focus-on-back-office-details)Focus On Back Office Details

By “back office” I mean to describe the operational processes and details that are necessary to support a fully distributed team: how do you pay employees living in different parts of the country or world, business and income tax implications for both the employee and company, benefits and rights afforded to the employee given her location or jurisdiction. The list gets long.

The term has a negative connotation (and I’m open to alternatives). It’s usually perceived as either “boring” or “unimportant”, both of which could not be further from the truth.

Our first “global” employee besides myself was based in Canada. I was based in the U.S., and we only had a U.S. entity. I worked with her to figure out the kind of entity we needed to register in Canada, so the proper taxes could be remitted. We used bank wiring to pay her initially, which was a pain in the ass, costly, and led to awkward emails where she sometimes had to remind management to pay her because you can’t automate it. We put in more time to research better options, and eventually used a different service that could make payments somewhat easier from a U.S. account to non-U.S. accounts. It was by no means perfect, just improved. And I’m grateful to this day that she put up with it all.

It took a lot of energy out of us. She was an engineer, who had a background in distributed systems. I had multiple responsibilities -- building our open source community, setting our go-to-market strategy, recruiting more people, writing blog posts and case studies, etc. Neither of us was well-suited to deal with “back office” work. It was painful, and at times felt like distractions, but ultimately very necessary.

Our team grew and things got better over time, partly because we found better tools, but mostly because I had to learn to communicate upfront the difficulties and rough edges in working with us in a distributed setting. A lot of the operational complexities were out of my control, but the least (or most) I could do was be open upfront about it all.

Ultimately, solid talent continued to apply to our openings because we had a strong open source brand, interesting technical challenges to solve, a bright business prospect, along with a distributed work setting. Hopefully that’s why people are applying to your company too, and not _just_ because they want to live and work from wherever they are.

Getting these operational details right, hopefully from the start, and if not, over time and be transparent about it, will yield big cultural dividends in the long term. Lean on your lawyers for help -- one of the few instances where I would advocate for lawyer use in the early days of a company. Otherwise, even the smallest mistakes will leave a bad taste and erode trust over time in other areas of work, no matter how “world-changing” your mission is.

_(One other noteworthy issue of a distributed team where engineers span different countries is IP ownership. It’s a whole ‘nother can of worms that we will cover in more detail in future posts.)_

## [](#flatten-decision-making)Flatten Decision Making

The naysayers of fully distributed work often to point to the lack of face-to-face contact, spontaneous interactions, and time overlap due to distance and time zones differences as downsides.

These are not wrong, but they are mere symptoms. The core problem is siloed decision-making, which isn’t a distributed workforce problem per se. It is a general workforce coordination problem. However, physical distance and remoteness _could_ make a fully distributed team more vulnerable to this problem.

People become disengaged and disenchanted when decisions are made without their involvement or knowledge, regardless of whether it affects their day-to-day work or not. Good employees don’t want to be mere “satellites” just taking orders. (Employees who want that probably aren’t good employees.) When the _process_ of decision-making is not clear and transparent, doubt and distrust start to form. This problem repeats often in both small startups and larger startups who still think like a small startup.

A fully distributed team, by default, removes a lot of the physical silos (conference rooms and corner offices are notorious devices for making secret decisions). But it doesn’t remove the temptation or ability to make snap decisions, often for the sake of “moving fast” or “efficiency”; phone calls and Slack DMs still exist.

The cure for siloing is **transparent process-driven decision-making**. Lay out how each type of decisions are made, who decides and who’s accountable (should be the same person), and iterate on the process over time. Most crucially, founders and executives have to be disciplined about sticking to the process and resist the temptation to just “hash it out”, simply because they have the authority to do so. It may feel inefficient at first, but the cost of employee disengagement and distrust is much greater.

Open source best practices -- public documentation, Request for Comment (RFC) templates, open code review -- are good rubrics to adapt from when building decision-making processes for your distributed team.

By effectively “flattening” decision-making into one layer, a fully distributed team can minimize the potential distrust that may come with “remoteness”.

## [](#strategically-use-conferences-and-airbnb)Strategically Use Conferences and Airbnb

As a database company, we go to quite a few industry conferences. Every company probably has some set of conferences or summits to attend to drive awareness for its product.

Our playbook for these business trips is: everyone is invited regardless of your function, and we all live under a single roof, eschewing hotel rooms.

This setup builds more cross-functional empathy (booth duty is hard work!), more familiarity with how the company’s product or service is positioned publicly (don’t assume everyone knows), and a shared work experience that tends to produce higher quality bonding than the traditional offsite model, where you are bonding for the sake of bonding.

For the first conference we went to as a team, there were four of us in an Airbnb house. After the conference, we all went tent camping, which turned out amazingly well (but in hindsight was an aggressive choice for a first offsite). For the last trip I organized as the general manager, there were 16 of us! We obviously had to find a much bigger house. We shared rooms, bunk beds, and worked and lived under one roof for a solid four days. It was basically an adult band camp (or database camp).

Whether it was four or 16 people, these conferences-turned-band-camps were always chaotic, fun, productive (somewhat), and revealing of everyone in ways you would never see.

Here’s a video montage of that last trip with 16 people:

Thinking back, observing our team in this light was hugely beneficial to me as a manager. Who chips in to help? Who takes the trash out? Who proactively buys groceries? Who leaves their stuff lying around? Seeing these situations and gathering these behavioral data points helped me better coordinate, manage, and streamline different people’s personalities, after we all disperse and return to our distributed way.

## [](#distributed-future)Distributed Future

For technology and knowledge workers, a fully distributed setting will become more mainstream. As more and more companies adopt this approach, I hope these personal experiences could help you think through now to minimize the cons and maximize the pros of distributed work.

I’d love to hear your stories, experiences, and lessons from managing or working in a distributed team. Please comment and share your thoughts!
