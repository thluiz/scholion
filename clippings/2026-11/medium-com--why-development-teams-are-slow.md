---
url: "https://medium.com/javascript-scene/why-development-teams-are-slow-89107985c75c"
captured_at: "2026-11-16T06:18:04+00:00"
title: "Why Development Teams are Slow. Common Software Jams and Solutions | by Eric Elliott | JavaScript Scene | Medium"
domain: "medium-com"
---

Why Development Teams are Slow
Common Software Jams and Solutions
Eric Elliott
18 min read
·
Mar 12, 2020

Image: Smoke Art Cubes to Smoke — MattysFlicks — (CC BY 2.0)

This post is part of the Managing Software series.
< Previous | Next >

Let’s take a look at what causes software assembly line jams, and what you can do about them as a manager. There are many causes, so we’re not going to try to create an exhaustive list. Instead, we’ll concentrate on a few of the most common issues:

Unrealistic Expectations
Too Many Open Issues
Unmanageable Task Size
Code Review Pile Up
Poor Training
Developer Burnout
Bugs
Poor Employee Retention

“Developers are too slow” is not a cause. It’s a symptom of these other causes. 100% of the time, if a development team is “too slow,” it’s the manager’s fault. The good news is that a manager has a lot of power to correct it. Let’s get a better understanding of these problems so that we can figure out what we can do about them.

Unrealistic Expectations

The most common problem with developer productivity is not a problem with development at all. Rather, it’s a problem with our perception of software development as managers and stakeholders.

The hardest part of being a software manager is understanding that software takes the time it takes, and rushing it will slow it down and make it buggy. Patience is everything.

The most common problem with software productivity by a landslide is not that the team is slow, but that the team is dealing with unrealistic expectations. That is entirely your responsibility. If the pressure is coming from above your head, you’re failing to manage expectations appropriately. If the pressure is coming from you, read on.

We often forget that we’ve never built this software before. If there is already software that does the job, buy it, use it, import the module, etc. Don’t build it from scratch. Newly developed software is generally unique. It’s doing something new or doing something differently. That’s why you have to build it in the first place. Since you’ve never built it before, you have no idea how long it will take. Unlike the construction industry who can predictably build prefabricated walls at a constant pace, and can use that data to inform their estimates, the software industry has no such source of reliable data. To further exacerbate the issue, there is an order of magnitude difference in performance between developers. To quote Steve McConnell (author, “Code Complete”):

The general finding that “There are order-of-magnitude differences among programmers” has been confirmed by many other studies of professional programmers (Curtis 1981, Mills 1983, DeMarco and Lister 1985, Curtis et al. 1986, Card 1987, Boehm and Papaccio 1988, Valett and McGarry 1989, Boehm et al. 2000).

We lack the data required to predict how long it will take to build our project. We’re going to discover scope and complexity along the way, as we’re building the software, and that’s a process that often comes with many surprises. Software is as much an exploration as it is a plan, regardless of how hard we try to plan.

“The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time.” ~ Tom Cargill, Bell Labs

There are some causes of unrealistic expectations that managers have some control over. One of the fundamental causes is measuring the wrong things.

You may be familiar with the famous quote by Peter Drucker:

“What gets measured gets managed.”

And of course, that’s excellent advice. We certainly should measure things! But that’s missing the point of the quote. More than that — it’s completely misinterpreting the meaning of the quote. The full quote is:

“What gets measured gets managed — even when it’s pointless to measure and manage it, and even if it harms the purpose of the organization to do so.”

In short, there are some things we definitely should not measure. Here are two examples:

Predictive burndown charts — A chart showing a line graph of the current number of open tickets, plotting a predicted completion date based on recent velocity measurements.
Closed Tickets by Developer — Metrics gathered for the number of jobs completed by an individual developer.

Measuring these two things has cost countless businesses countless billions of dollars in lost productivity, lost employees, and opportunity cost.

Predictive Burndown Charts

A lot of the software tools try to predict when you’ll finish a project based on the current scope and historical velocity. The problem is that predictive burndown charts can’t accurately account for undiscovered scope. It isn’t possible to account for undiscovered scope because the length of time it takes to complete a single work ticket can vary by orders of magnitude, which can severely skew and invalidate the application of historical averages to the current scope.

If you set a deadline or expectation based on a date you got from a burndown chart, you’ve already missed the date. The only thing that can save you is if you trim as much scope as you discover.

When you base your estimate on incomplete information, that estimate is going to come back to bite you and your team. The unrealistic estimate creates unrealistic expectations. Things get even worse if you make the mistake of sharing those false predictions with the marketing team and then set unrealistic expectations with customers and the press.

But not all burndown charts are evil. Non-predictive burndown charts give us useful insights. They can give us early warnings of scope creep and complexity explosions when you see the number of open tickets in scope continually growing rather than shrinking or moving sideways. A useful burndown chart tracks actual closed numbers rather than predicting future numbers. For example, this chart tracks a project from inception to completion. For the bulk of the project, the movement has ups and downs but moves mostly sideways until we reach the final stages of the project, and we can finally gain on the newly discovered scope.

A burndown chart illustrating a downward curve.

A project suffering from scope creep would curve upwards instead of downward, or fail to curve downward in the final weeks of the project.

A burndown chart illustrating a scope explosion.

Keep in mind, the purpose of watching that chart shape is not to manipulate the chart shape, but to identify and fix the underlying issues. You don’t want your developers to try to manipulate the chart shape by failing to open work tickets to document discovered scope. The goal is process visibility, not flat or descending lines on a chart.

Beware of Goodhart’s law:

“When a measure becomes a target, it ceases to be a good measure.”

Not all projections are evil. When you have a drop-dead deadline (e.g., trying to ship your new game before Black Friday), you can judiciously project into the future based on average ticket velocity to get an early warning when you need to cut scope. If the historical velocity projection tells you it won’t be done until December, believe it. It’s time to prioritize and cut.

Rule of thumb for software production predictions:

If a prediction tells you you can do something by some date, don’t believe it. If a prediction tells you that you can’t do something by some date, believe it.

Closed Tickets by Developer

It’s very tempting as a manager to count the number of work tickets each developer is closing, and then compare that to the team average. I urge you to resist the temptation. There are many better ways we can gain insights on developer productivity.

There are two fundamental flaws with closed ticket counting. First, not all tickets represent equal work or equal value, and in fact, the value of work completed falls on a power law curve. A small handful of tickets account for many orders of magnitude more value than “average”: The difference between a skyscraper’s foundation and a finishing nail. So a simple count of closed tickets can’t accurately tell the value delivery story.

Task Value Power Law

Years ago, I was working for a world-leading retailer on a shopping cart. One day I stopped writing code and closing tickets in Jira (the ticket tracker of choice in its day). I added one ticket: “Usability study.”

We’d been working on a redesign of our shopping cart for more than a year, and the time for the new release was quickly approaching. Up until this point, we had not conducted any end-user usability testing of the new checkout experience: so I took a week. We gave early access to 1,000 of our most loyal supporters and surveyed them to collect feedback. I analyzed the results and noticed a disturbing pattern in the comments and the log files:

The cart abandonment rate was in the double-digits too high. A pending disaster! So I set to work planning video-recordings for in-person usability tests. I put newbies in front of the new shopping cart, gave them some tasks to accomplish, and set them to work. I didn’t say anything. Just watched them use the cart.

I noticed that during the checkout, people were having a hard time with error feedback in the checkout form. With that data in hand, I made some tiny changes to an open-source project on GitHub (note: recorded on GitHub, not in our issue tracker). After a while, I ran the same analysis I did before. The shopping cart abandonment rate was reduced by double digits: A difference worth more than $1 million per month.

Meanwhile, my teammates had each closed 10–15 tickets. You could argue that I could have opened more tickets about the usability study, but to make it reflect the value more accurately, I would have needed to open a thousand or more tickets, and that would have only served to create noise and waste a lot of time.

The other reason closed ticket counts are misleading is that your most productive developers are also the ones everybody else on the team turns to for help. They know the most about the code base, or they’re just excellent developers, collaborators, or communicators. They’re helping you slog through the pull request backlog, reviewing the code of other developers, and they’re teaching and mentoring the other developers on your team. They are the most productive developers on the team because they’re helping every other member of the team be twice as productive. Perhaps the tickets they do close are libraries or frameworks that make the entire team more productive. They are landing all the assists while other developers get credit for the dunks.

If you’re not careful, it can be easy to overlook the contributions of your most productive developers. The best way to understand how your developers are contributing to the project is to ask them. Then ask other developers to provide feedback about who the most helpful members of the team are.

Usually, the value reflected in those discussions is quite different from the value reflected in the ticket counts.

Do monitor value delivery in aggregate, but don’t try to judge the contribution of every developer with the same simple metric. Software is a team sport, and each member of the team plays a different role. There is no single magic metric to tell you about developer productivity.

Too Many Open Issues

It’s easy to get an idea, open up an issue in your issue tracker, and then move on with your day, but every issue in your issue tracker represents a cycle of rework. Each issue needs to be triaged, prioritized, and assigned before a developer can even begin to work on it. That work gets repeated nearly every time developers finish tasks and go to select another task to begin. If you have a project manager or scrum master who assigns work for developers, they repeat that work every time they reprioritize the queue (which typically happens at least once per sprint or every couple of weeks).

Then the developer needs to absorb the context of the issue, develop an understanding of the problem, decompose complex problems into simpler problems, and all that before they can begin to develop a solution.

Tickets are a lot of work, but not only that, they’re not real work. They’re meta-work — work about work. Tickets themselves have zero intrinsic customer value. And they get worked on repeatedly every time the developers need to figure out what to work on next. The fewer tickets you have to sort through to figure that out, the better. The fewer low-priority issues in the backlog, the better the chances that a developer will select a high-priority, high value ticket.

If there’s a bug in the software that only one customer has ever mentioned, does that bug matter? Sure, it bothered one person, but are other bugs in the queue impacting more users? Are there new features that will unlock more value than fixing that bug?

Probably. Reduce the noise in your issue backlog. Delete stuff that you don’t plan to start soon. If it’s really important, you’ll add it again at a more appropriate time.

Unmanageable Task Size

In general, I like to ask developers on my team to break their work down into tickets they can complete in one day. This is harder than it sounds because it means learning how to break complex problems down into simpler, easier-to-solve problems which can be independently tested, separate from the rest of the application. For example, if you’re building a new purchase flow, you don’t have to mix the UI components, state process, and server communications together into one giant commit touching 13 different files, all tightly coupled to the existing codebase. This is problematic because it causes very large Pull Requests (PRs) that are difficult to review and merge.

Instead, start with an independently testable shopping cart state module for the client side code and make a pull request for that. Then build the server side checkout API and make a separate PR for that. Then build a UI component that imports the client side state module and connects to the server side API. Each of these can be broken up into their own work tickets and their own commits, even though the assignment was really one big feature. Bonus: You may be able to assign multiple developers and get to feature completion faster by making better use of your developer headcount.

A feature toggle system makes this process safer and easier by allowing you to toggle features off until they’re complete and ready to enable in production.

Warning: Don’t try to do this without good smoke test coverage to ensure that you haven’t broken any critical workflows in the app by shipping half-finished features to production. Be sure to test both states of the feature toggle.

Code Review Pile Up

When developers do bite off more than they can chew in a day, the result is often a huge pull request for code review. This is the “integration” phase of “Continuous Integration” (CI). The problem is that the longer a PR stays open, the more hours you burn on it because curious developers pop it open to see if they can help get it merged. Then they offer some feedback, request some changes, and it’s back to the author to respond to the change request and hopefully address all the concerns so it will get approved.

When several developers make a habit of creating very large commits, you can develop a backlog of commits, and integration begins to drift. Bob makes a change to a file that JSC already edited but hasn’t yet merged. Bob’s PR gets approved and merged first, allowing JSC’s still open PR to drift from master. She can’t merge her branch until she fixes any merge conflicts caused by Bob’s code changes. Multiply this PR traffic jam by n developers, where n is the number of developers with overlapping work in your project. These traffic jams lead to more commit churn. Let's keep track of the total number of churns in a common scenario:

Bob and JSC check out the same master branch. Churn: 0
Bob makes his change from the master branch and commits to his branch. JSC makes her change from the master branch and commits to her branch. Churn: 2
Bob’s change merges first. JSC then merges Bob’s changes with hers and finds a conflict. She fixes the conflict and commits the change to her branch. Churn: 3
JSC opens a pull request. Bob mentions to JSC that her change to his code will break something that she didn’t account for. JSC incorporates Bob’s suggestion and commits the code again. Churn: 4
JSC’s PR is approved and merged. Total churn: 4

Alternatively, if the commits were smaller and PRs were merged quickly, this same flow could look like:

Bob makes a small change, and it gets merged to master quickly. Churn: 1
JSC checks out master with Bob’s change already incorporated and makes her change with Bob’s change already integrated: Churn: 2
Since JSC’s change was also small, it gets merged to master quickly. Total churn: 2

By keeping PRs small and staying on top of them, we can significantly reduce rework caused by code churn and integration conflicts.

Poor Training

The software industry is terrible at training and supporting developers. Universities drill algorithms that are already built-in to the standard libraries we use and few developers should implement from scratch, while neglecting software development foundations such as principles of abstraction, causes of coupling, modularity vs. monolithic design, working with modules, function composition, object composition, framework design, API design, and application architecture. Due to the explosive growth of the relatively young software industry, nearly half of all software developers have fewer than five year’s experience, and 88% of employees feel like they could use more training.

Teams are slow because they don’t know what they’re doing, and nobody has bothered to teach them. As managers, it’s our job to hire senior mentors to guide our teams, and then give them dedicated time to do that. Here are some tactics:

Code review — Developers learn a great deal from looking at each other’s code.
Pair senior engineers with junior developers — These pairings don’t need to be full-time. I find that ad-hoc pairing works fine.
Dedicated time to mentorship sessions — Hire senior engineers who love to teach and are great at communicating, and then give them time to connect 1:1 with junior developers to help juniors figure out what they need to learn next to develop their skills.
Developer Burnout

Far worse than missing a deadline, the ultimate shame a manager can reap is burning out the team.

Developer burnout is a serious issue that can lead to the loss of developers on your team, causing employee churn, bus factor risk, and tremendous business expense, but far more importantly, developer burnout can cause serious health issues for the developers you’re burning out. Those issues can cause long-term disabilities or even death by heart attack or stroke. In Japan, this phenomenon is common enough that they have a word for it: Karoshi.

A manager can burn out an entire team at once, bringing team productivity to a grinding halt. The problem of whole teams burning out is particularly prevalent in the video game industry, where Black Friday is almost always a drop-dead deadline. Unfortunately, “drop-dead” is too often literal in practice, but rarely understood as literal or taken literally.

Instead of working developers harder, managers need to recognize that 100% of the responsibility of hitting a deadline falls on management, not developers. We can hit deadlines better using alternative tactics:

Prioritize better and cut scope
Use a more productive process (e.g., implement better bug control measures)
Identify and refactor sources of churn in the code
Poor Employee Retention

LinkedIn’s 2018 data showed that the software industry had the highest talent turnover rate of any industry. This is bad because it leads to unusually high bus factor risk — the risk that you’ll lose your team’s key technical experts.

Many companies in the industry don’t place enough value or emphasis on retention. Let’s take a closer look at the cost of developer churn. Recruiters typically charge $15k — $30k for placement fees. In the US, an engineer’s time costs an average of $90/hour. Multiply that by about 50 to interview prospective developers, and then add many more hours to answer questions and onboard the new recruit. We’re already comfortably in the $50k territory, but there’s more. The new developer could take a year or more of salary ramping up to the level of productivity of the employee they replaced, and will likely make a lot of mistakes and cause a lot of rework in the early days.

All told, recruiting, interviewing, onboarding, training, and opportunity costs associated with the lost employee and the lost productivity of developers who need to fill the void can add up to more than 90% of the lost employee’s salary. Replacement can take many months, and developers typically spend several months ramping up.

All of this is very time consuming, and large teams generally suffer a continuous drag because, as a 2019 Stack Overflow survey noted, 60% of developers surveyed changed jobs less than 2 years ago.

By the time a developer truly ramps up, you’ve lost them.

How can you avoid that? Synthesizing data from a variety of sources:

Pay fairly
Offer regular salary raises
Offer generous vacation time
Offer remote work
Keep your expectations realistic
Provide work that aligns well with the engineer’s interests
Don’t let your tech stack fall too far behind
Provide excellent training and professional development opportunities
Provide excellent health benefits
Don’t ask developers to work more than 40 hours/week
Provide current equipment
Bugs

If you think you don’t have time to implement a high-quality software development process, you really don’t have time to skip it.

According to “Evaluating Software Engineering Technologies” (David N. Card, Frank E. Mc Garry, Gerald T. Page, 1978), quality processes reduce errors without increasing costs. One reason for that is that software defect removal is the most expensive and time-consuming form of work for software, according to “Software Assessments, Benchmarks, and Best Practices” (Caspers Jones, 2000).

Bugs are notorious for causing rework and code churn, and and the later you catch them, the more expensive they are to fix. When a developer is assigned a high-priority fix for a bug that’s already in production, it often interrupts whatever that developer was doing to fix the issue quickly for customers. According to “A Diary Study of Task Switching and Interruptions” (Mary Czerwinski, Eric J. Horvitz, Susan Wilhite), an interrupted task can take twice as long and contain twice as many errors, which means that high-priority bugs are contagious. In the process of fixing one, you’re likely to cause another.

Bugs in production also lead to an increased demand for customer support as well as customer attrition, both of which will likely cost you money. Then you have to factor in the opportunity cost of fixing bugs instead of building new value for customers. A bug found at implementation time can typically be fixed in a few minutes, but if the bug is found in production, it will go through additional development phases, including bug reporting, triage, prioritization, assignment, and finally, development. But we’re not done with the slow-down, yet. A bug fix typically gets its own commit, its own code review, its own integration, and in some cases, its own deployment, and at any stage in that process, a test could fail, triggering another restart of the development-CI/CD cycle.

All told, a bug found in production can cost orders of magnitude more to fix than a bug caught during development, even before you count customer service and user attrition costs.

Here are some things you can do to increase your quality process.

Slow down to speed up. Slow is smooth and smooth is fast.
Practice design review. The combination of design and code inspection can catch 70% of software defects. “Measuring Defect Potentials and Defect Removal Efficiency”, (Caspers Jones, 2008)
Practice code review. Inspected software costs 90% less to maintain. An hour of inspection saves 33 hours of maintenance. Developers who inspect code are at least 20% more productive.
Use TDD. TDD can reduce bugs 40% — 80%
Use Continuous Integration/Continuous Deployment (CI/CD). CI/CD, referred to collectively as continuous delivery, is an automated process that combines code review, automated tests (unit and functional tests), automated test deployment, and finally, automated production deployment. Because the whole pipeline is automated, there’s no opportunity for errors in any step of this highly error-prone process, and the automation can save dozens or even hundreds of hours of manual work per developer per delivery. If you’re not using CI/CD, start today.
Improve test coverage. Your Continuous Integration/Continuous Deployment (CI/CD) process should run a suite of automated tests and halt if any of those tests fail. This can prevent bugs from being released into production and save a whole lot of time and money in the process. Continuous delivery is a bad idea if you don’t start with good enough test coverage. Aim for a minimum of 70% code coverage before automating delivery, and try to keep that number above 80%. After that, you’ll see diminishing returns as you get closer to 100%. At that phase, functional test case coverage of your most important user workflows will deliver more value than increasing unit test coverage.
Conclusion

There are many ways managers can impact the performance of their teams. Among them:

Set realistic expectations (both up and down the reporting chain)
Monitor and control the number of currently open issues
Manage task size
Don’t let code reviews pile up
Train developers
Provide good work/life balance for developers
Implement an effective software quality process
Pay attention to employee retention
Next Steps

DevAnywhere offers mentorship for leaders of software development teams. You can get 1:1 personalized advice for your team on topics such as building a great quality process, nurturing a culture of learning and mentorship, collaborating with product teams, and building an efficient CI/CD process. To learn how we can help your team ship high quality software faster, tell us about your team and your needs.

Want to get your team up to speed with TDD and reduce production bugs by 40% — 80%? EricElliottJS.com includes the TDD Day 5-hour training used by employees of Disney Interactive, Spotify, Netflix, PayPal, and Amazon to improve their quality practice. It’s also packed with lessons on JavaScript, TDD, functional programming, React, Redux, and more. Want to buy passes for your whole team? Let us know how many you want to buy, and we’ll send you an invoice you can pay all at once. Once you’ve paid, we’ll send you a magic link your employees can use to set up their accounts.

Eric Elliott is a tech product and platform advisor, author of “Composing Software”, cofounder of EricElliottJS.com and DevAnywhere.io, and dev team mentor. He has contributed to software experiences for Adobe Systems, Zumba Fitness, The Wall Street Journal, ESPN, BBC, and top recording artists including Usher, Frank Ocean, Metallica, and many more.

He enjoys a remote lifestyle with the most beautiful woman in the world.
