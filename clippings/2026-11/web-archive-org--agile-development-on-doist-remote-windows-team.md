---
url: "https://web.archive.org/web/20200610040258id_/https://doist.com/blog/agile-development-remote-team/"
captured_at: "2026-11-18T11:41:32+00:00"
title: "What Agile Development Looks Like on a Remote Team"
domain: "web-archive-org"
---

There’s no one way that [Doist](https://doist.com/?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team) “does development”. Our fully remote engineering teams have always had independent workflows.

At the company level, we define work and set high-level priorities through monthly [Doist Objectives](https://doist.com/blog/how-we-manage-projects-on-a-fully-remote-team/?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team) (DOs for short). However, each development team (e.g. Frontend, Backend, Android, Apple, Windows, Integrations) can execute using whichever process they’d like. This independence allows us to experiment with new ways of working without excessive red tape. Using agile development on a remote team is one of those experiments.

The Windows team at Doist started as just one person when I was hired in 2015. As is the case with most one-person teams, there was no process. But after adding a few folks, we started experiencing growing pains:

*   Requests of our team came from many sources. Prioritizing these requests and setting expected delivery dates was pure guesswork.
*   We worked in isolation for long periods, becoming lone wolves more than a pack, which prevented us from understanding where we could unblock our teammates when needed. Oftentimes, people got stuck on a task for multiple days before reaching out, because team members lacked the visibility.

It was clear we needed a more organized way to collaborate and manage all of the demands on our small but growing team.

Most of us had experience with agile development from previous jobs, so our first instinct was scrum. But replicating the scrum methodology in a fully remote setting isn’t easy. The Doist culture of mindful, [async communication](https://doist.com/blog/asynchronous-communication/?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team) – paired with the ever-present scheduling and connectivity challenges with teammates spread across time zones – made techniques like daily check-ins, fast feedback loops, and pair programming non-starters.

We wanted to leverage the fact that we’re [entirely remote](https://doist.com/blog/how-doist-works-remote/?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team) to its fullest, allowing people to freely organize their days to maximize their most productive hours. For our team, that meant blocking off several days of [deep work](https://doist.com/blog/deep-work/?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team) without distractions. Engineering work requires a great deal of focus. The ability to disconnect and concentrate was an advantage we didn’t want to give up.

At the same time, we were still looking for a process to incentivize team collaboration, enable fact-based time estimates, and deliver high-quality results on time.

These requirements meant that we had to find the right balance between the fast pace of agile and long stretches of heads down, focused work. That balance is always a moving target – we continuously iterate on our process, and it’s never perfect. Processes should evolve with the reality of the team. Over time, we add to the process when we discover new needs and remove parts when we outgrow them.

This article goes over the essential elements we’ve now practiced successfully for several years, which have worked well for us. It represents our collective experiences, as well as learnings from some great books, in particular:

*   [Agile Kaizen: Managing Continuous Improvement Far Beyond Retrospectives](https://www.goodreads.com/book/show/21516615-agile-kaizen) by Ángel Medinilla
*   [Agile Project Management with Kanban](https://www.microsoftpressstore.com/store/agile-project-management-with-kanban-9780735698956) by Eric Brechner
*   [Scrum: The Art of Doing Twice the Work in Half the Time](https://www.goodreads.com/book/show/19288230-scrum) by Jeff Sutherland

The main elements of our process are:

1.  The Backlog
2.  The Meeting
3.  The Sprint

## (1) The Backlog

At Doist, we have a lot of sources of work that engineering teams need to keep an eye on.

*   **Support** tells us about issues our users are experiencing, as well as their ideas for improvements.
*   **Design** asks us to add polish to various places in the app.
*   **DO Squads** (temporary, cross-disciplinary, project-based teams) set the high-priority projects and drive the bulk of our work.
*   **Internally**, our team always watches telemetry data for bugs and has a lot of ideas for refactoring, as well as for new features.

![The Backlog](https://i0.wp.com/doist.com/blog/wp-content/uploads/sites/3/2020/05/2_Backlog.png?resize=616%2C290&quality=85&strip=all&ssl=1)

Aggregating these needs led us to create an internal team backlog within [Azure Boards](https://azure.microsoft.com/en-us/services/devops/boards/), which stores _all_ of our work. Aside from small exceptions, if it’s not in the backlog, we don’t work on it. This requirement helps us build the discipline to use it consistently and creates confidence that it represents reality.

![scrum development backlog](https://i0.wp.com/doist.com/blog/wp-content/uploads/sites/3/2020/05/2_Backlog_Desktop-wide.png?resize=1472%2C693&quality=85&strip=all&ssl=1)

The backlog represents all of the potential tasks the Windows team could work on in any given sprint. With few exceptions, if it’s not in the backlog, we don’t work on it.

While the whole team contributes to the backlog, two roles interact with it the most:

1.  The team lead (me) owns the backlog. The team leader curates the backlog, works with team members to ensure that it reflects all future work, and uses it to propose sprint workloads.
2.  The monthly [hero](https://doist.com/blog/heroes-housekeeping-days/?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team) in our team focuses on _communicating_ with other teams, chiefly Support, [in Twist threads](https://get.twist.help/hc/en-us/articles/115003629449-What-are-threads-?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team), to clarify users’ bug reports and improvement ideas. The hero then turns those threads into _actionable_ work items in the backlog. This role rotates monthly so everyone has the opportunity to work closely with user feedback and do more heads-down, project work.

![backlog item description](https://i2.wp.com/doist.com/blog/wp-content/uploads/sites/3/2020/05/1_Backlog_Item_Desktop-wide.png?resize=1472%2C658&quality=85&strip=all&ssl=1)

Each item in the backlog is briefly described with a link back to the original thread about the bug or feature in [Twist](https://twist.com/?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team).

Building and maintaining a backlog is a lot of work. But as the pressure on the team grows, it’s essential to understand what the team should prioritize, unearth hidden dependencies between work items, and plan sprints.

With a well-defined workload, the team is ready to plan our sprint.

## (2) The Meeting

On our team, one sprint runs for two weeks. We’ve experimented with weekly sprints as well, but they didn’t fit into our remote setting. Asynchronous communication allows us to do more deep work, but it also slows down communication. It can be unrealistic to execute certain tasks within a span of a single week if there’s a significant amount of communication involved.

At the beginning of each sprint, we have a meeting. It’s long and exhausting, at around two hours, but it’s also the only meeting we have as a team in the two weeks. The primary goals of the meeting are to assess incoming work, identify uncertainty and risks, and lock in the scope for the upcoming sprint.

The meeting has a fixed format:

1.  **Scoring**. Go through new items in the backlog since the last meeting one by one, understand their complexity, and assign them a numerical score.
2.  **Scope Lock-In**. Agree on a team commitment for the upcoming sprint, and move the work that won’t make it into scope into future sprints.
3.  **Kaizens**. Discuss ideas for process improvements based on our recent experiences.

Let’s look at each one in detail:

### Scoring

The most time-consuming activity of the meeting is going through new work items we’ve accrued in the past two weeks. For each one, we discuss the implementation path and effort required. This discussion can help catch poorly defined work items or items that have too much uncertainty attached. We reject scoring these, putting a hold on their execution until they’re better defined.

We formalize the agreement on the effort required by assigning story points using the planning poker technique. The resulting score allows us to see the cost of the work item relative to other items in the backlog.

_Whoa whoa whoa. Hold up. What are “story points” and what’s the planning “poker technique”?_

**Story points**

Story points measure the expected difficulty of implementing a piece of work relative to other pieces of work. Unlike an hour-based forecast, it does not express the amount of time execution will take. Instead, it tries to answer the question: What will be more challenging to do, A or B, and how much more challenging will it be?

Story points are frequently limited to numbers out of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) (e.g. 0,1,1,2,3,5,8,13,21,34,55, 89, 144…). By using the Fibonacci sequence, a team acknowledges that, as a task grows more complex, the team’s ability to estimate it becomes worse, which in turn increases the risk of failing to meet commitments agreed upon beforehand. It also acts as an incentive for the team to break down their tasks into smaller chunks as the team will deem tasks with a lot of story points too uncertain to execute in their current form.

![Story points scale](https://i1.wp.com/doist.com/blog/wp-content/uploads/sites/3/2020/05/1_Story-points-scale.png?resize=669%2C304&quality=85&strip=all&ssl=1)

Story points are also team-specific. When the Windows team adopted story points, we went through old tasks we had already executed and agreed on which pieces of work represented 1 story point (for us, a clear-cut bug that looks easy to fix) or 13 story points (for us, some unknowns and dependencies on other teams, which usually takes a week or more to implement).

The next concept related to story points is _team velocity_. Team velocity tells us how many story points, on average, we’ve been able to execute over the past few sprints as a team. With this knowledge, we can understand what’s doable per single sprint and plan accordingly.

If you’re still not convinced about the utility of story points, give [this blog post from scrum.org](https://www.scrum.org/resources/blog/why-do-we-use-story-points-estimating) a try.

Finally, we need a way to assign story points to tasks. We do this with planning poker…

**Planning poker**

![What planning poker looks like](https://i1.wp.com/doist.com/blog/wp-content/uploads/sites/3/2020/05/3_Poker-Planning.png?resize=1452%2C984&quality=85&strip=all&ssl=1)

We play “planning poker” to individually score a piece of work, then reveal the scores and discuss any discrepancies before agreeing on a number.

Planning poker gamifies the process of assigning story points to tasks, while minimizing [groupthink](https://www.psychologytoday.com/us/basics/groupthink) and incentivizing discussion.

There are many variants on planning poker, but ours goes like this:

1.  The creator of an upcoming task briefly presents it, giving context about what we’re trying to achieve and what obstacles we might face.
2.  The team asks clarifying questions about the task.
3.  Based on that information, everyone individually picks a number from the Fibonacci sequence that they believe represents the task difficulty well, without revealing it to others.
4.  Everybody shows their number at the same time.
5.  If the highest and lowest revealed number differ by no more than one step in the Fibonacci sequence, we average them out, and that becomes the assigned story points number for the task.
6.  If the highest and lower numbers revealed differ by more than one step in the Fibonacci sequence, people with the highest and lowest number outline their reasoning, followed by a short discussion.
7.  Based on the new information, everybody picks a fresh number, and we again reveal them at the same time.
8.  We average our numbers, and that becomes the story point count for the task.

Poker planning can be time-consuming, but becomes faster with practice. Through this process, we learn how different people think about problems and assess uncertainty, bringing us closer together as a team.

### Scope lock-in

When scoring is done, we move on to discuss which tasks will be included in the next sprint. We know roughly how much we can execute by looking at the number of story points we delivered in previous sprints.

![Scrum story points](https://i2.wp.com/doist.com/blog/wp-content/uploads/sites/3/2020/05/4_Story-Points-Sprints.png?resize=1452%2C748&quality=85&strip=all&ssl=1)

We estimate our team capacity for each sprint based on the average number of story points we’ve completed in past sprints.

Agreeing on the work is a joint exercise that’s data-informed but comes down on an agreement between people based on their intuition – we don’t use any formal prioritization method. At the same time, we need to always take into account our commitments to cross-company initiatives (our DOs) and ensure that they are prioritized.

### Kaizens

In the last part, we briefly discuss the previous 2-week cycle and identify steps we can take to become better as a team.

The idea of Kaizen ([改善](https://jisho.org/word/%E6%94%B9%E5%96%84), translates to “betterment”) was first implemented at the Toyota Motor Corporation in 1950. The term refers to continuously finding small, incremental improvements and applying them immediately. This idea contrasts with concepts like [10x thinking](http://theviewinside.me/10x-thinking/), which focus on revolutionary but infrequent innovations. These two mindsets always need to coexist within any team or organization. While kaizen is a reliable tool to get to the local maximum, a more radical change is needed to break onto another level.

![Kaizen vs 10x Thinking](https://i2.wp.com/doist.com/blog/wp-content/uploads/sites/3/2020/05/3_Kaizen-vs-10x-thinking-1.png?resize=709%2C361&quality=85&strip=all&ssl=1)

## (3) The Sprint

After the meeting, we have two weeks to execute. During the sprint, we aim for an individual mix of work that plays to the developer’s strengths and includes some easier tasks to recover from bigger, more involved ones.

While scrum advises daily stand-ups, they’re impractical on a remote team. Agreeing on a consistent time slot is difficult and undermines one of the greatest advantages of remote work – flexibility.

Instead, we watch the flow of work items on our task board and make sure that we resolve the most critical tasks first. A shared understanding of relative priority comes from the order of items on the board, plus context shared during [The Meeting](#the-meeting).

Throughout the sprint, we communicate asynchronously in [Twist threads](https://get.twist.help/hc/en-us/articles/115003629449-What-are-threads-?utm_source=doist_blog&utm_medium=referral&utm_campaign=agile_development_remote_team) and messages as needed. If an item’s progress stalls on the board, we discuss who needs help and who has the time to provide it.

The team leader is responsible for making sure that people aren’t stuck and tries to help out by communicating with other teams, as well as doing some [rubber-ducking](https://en.wikipedia.org/wiki/Rubber_duck_debugging), and providing historical context about the codebase where needed.

* * *

On its face, agile seems at odds with a remote environment. The approach was first conceived of as a way for co-located development teams to iterate and react quickly to change. As stated in [The Twelve Principles of Agile Software](http://agilemanifesto.org/principles.html): “The most efficient and effective method of conveying information to and within a development team is face-to-face conversation.”

But one of the four agile pillars is “Responding to change over following a plan”. One of the most exciting things about working for a fully remote company is the opportunity to experiment with new ways of collaborating – sometimes we adapt what’s worked for co-located teams, sometimes we reject it, and sometimes we develop new approaches entirely. Any agile workflow needs to serve the team’s needs, not the other way around. Nothing should be held sacred or static.

As mentioned at the beginning of this article, our process is a snapshot in time that worked for us in a specific context. We’ll continue to iterate as our team’s and users’ needs change. Agile provides an extensive toolbox that we can pick and choose from in order to continue delivering amazing experiences to our customers — regardless of where we’re working from.
