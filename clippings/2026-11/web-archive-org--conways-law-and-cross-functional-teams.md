---
url: "https://web.archive.org/web/20200808054233id_/https://killalldefects.com/2020/01/30/conways-law-and-cross-functional-teams/"
captured_at: "2026-11-16T08:01:24+00:00"
title: "Conway's Law and Cross-Functional Teams - Kill All Defects"
domain: "web-archive-org"
---

In this article, I’ll explore and explain Conway’s Law and the effects it has on software engineering departments and the systems they manage.

## Conway’s Law Explained

Conway’s Law, states:

> Organizations … are constrained to produce designs which are copies of the communication structures of these organizations.
> 
> [Melvin Conway](https://en.wikipedia.org/wiki/Conway%27s_law)

Put another way, if I have a development department with 3 teams, I’m going to wind up with 3 separate systems or large modules that talk to each other sparingly.

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/image-33.png?w=770&ssl=1)

Additionally, at the team level, when people work on things in parallel they tend to introduce artificial boundaries that might not otherwise have been present. This can be in the form of new methods, classes, or even projects in the same overall solutions.

Essentially, Conway’s Law says that the structure of organizations and even individual teams matters more than we think it might, because these organizational structures lead us to divide our code.

![](https://i2.wp.com/killalldefects.com/wp-content/uploads/2020/01/image-34.png?w=770&ssl=1)

## So Is Conway’s Law Bad?

I would not categorically call Conway’s law good or bad, much like I wouldn’t call the laws of physics good or bad. **Conway’s Law simply describes the natural gravity of software development teams and their systems.**

Diving labor between teams by creating separate systems or modules isn’t necessarily bad. These things allow us to work on things in separation, distribute and divide work, and wrap our heads around complex systems as enterprises become larger and more complex over time.

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/01/image-35.png?fit=770%2C363&ssl=1)

Certainly, this division of work into separate systems can lead to bad behavior such as:

*   Slower performance from systems talking to each other in sequence
*   Increased complexity
*   Misunderstandings between teams
*   Lack of knowledge sharing between people in different teams
*   New classes of bugs arising from system interactions
*   Code duplication
*   Increased number of things that can fail

Note that a lot of what I’ve described here has some overlaps with downsides in microservice systems – particularly those who do not rely on a message queue or a request / acknowledge architecture.

* * *

However, Conway’s Law has some upsides:

*   Organizations can effectively scale up to larger sizes as they grow
*   It allows multiple developers to work in parallel
*   It creates spaces where skilled specialists can work on specific areas
*   Teams can adjust their services as needed to solve the problems they’re focused on, as long as they keep the same external interface

Whether the good outweighs the bad is another question entirely, but largely irrelevant since we can’t easily escape Conway’s Law’s effects. Instead, we should be focusing on what we can do with the knowledge that it _does_ exist.

## Manipulating Conway’s Law

So, knowing that systems eventually take on the shape of their organization, you can use this to your advantage to encourage certain behaviors.

If your organization is struggling from communication issues between systems, one thing you _may_ want to consider is shifting personnel and some projects around between teams.

For example, if Priya and Ahmed are both responsible for MyWebService and that systems has a large number of communication issues with OtherTeamBigService, it _may_ make sense to move the two of them into the other team, potentially moving others out of that team to make room.

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/image-37.png?w=770&ssl=1)

Before Reorganization

![](https://i2.wp.com/killalldefects.com/wp-content/uploads/2020/01/image-36.png?w=770&ssl=1)

After Reorganization

By putting people close together, you increase their communication and understanding of each other’s systems, domain logic, and technologies. This makes things more efficient over time between those systems and can lead to services merging together or making more efficient use of shared logic.

This brings us to an interesting point. What if your teams are composed of different technologies? For example, if I had a JavaScript team, I couldn’t necessarily move them into a Java team without some form of learning curve, despite what some recruiters might think!

If you organize your teams by product instead of by technology, you can identify areas of shared domain experience and systems that will naturally need to talk to each other in order to work properly and effectively. Even if you have only a technologist or two or two of the same discipline (C# dev vs Go, for example) on the team, they’ll be in a spot where they can efficiently share knowledge and troubleshoot problems as a team.

![](https://i2.wp.com/killalldefects.com/wp-content/uploads/2020/01/image-38.png?w=770&ssl=1)

If you _don’t_ do this, you can have cases where it’s much easier to hand a problem off to another team to troubleshoot who then hands it off to another, and nobody gets together to talk through the actual problem and assumptions going on in system communications.

This may sound trivial, but this problem can become severe, and cross functional teams can make a radical difference.

The downsides are that it becomes harder to share knowledge among people in the same technology group and you’re less likely to have managers directly involved in things their direct reports are working on, making it harder to accurately assess people who are excelling or under achieving.

Overall, though, shifting to smaller functional groups can make a lot of sense for organizations with wide varieties in engineering technologies.

## Closing Thoughts

Whether you decide to change organizational structures or not, understand Conway’s Law and the effect it has over time, because it will inevitably assert itself.

Like anything else in technology, there are tradeoffs with every decision. Every decision will solve some problems while making other things harder. Don’t restructure your organization just because it looks good on paper or you read a random article on the internet.

That said, if you are experiencing significant problems with knowledge sharing and system communication between teams and can’t seem to find a solution to these issues, I think there’s clear evidence to suggest that Conway’s Law offers some solutions.
