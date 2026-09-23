---
url: "https://martinfowler.com/fragments/2026-02-13.html"
captured_at: "2026-09-23T16:05:41+01:00"
title: "Fragments: February 13"
domain: "martinfowler.com"
---

Fragments: February 13
Martin Fowler

13 February 2026

I've been busy traveling this week, visiting some clients in the Bay Area and attending The Pragmatic Summit. So I've not had as much time as I'd hoped to share more thoughts from the Thoughtworks Future of Software Development Retreat. I'm still working through my notes and posting fragments - here are some more:

 ❄                ❄

What role do senior developers play as LLMs become established? As befits a gathering of many senior developers, we felt we still have a bright future, focusing more on architectural issues than the messy details of syntax and coding. In some cases, folks who haven't done much programming in the last decade have found LLMs allow them to get back to that, and managing LLM agents has a lot of similarities to managing junior developers.

One attendee reported that although their senior developers were very resistant to using LLMs, when those senior developers were involved in an exercise that forced them to do some hands-on work with LLMs, a third of them were instantly converted to being very pro-LLM. That suggests that practical experience is important to give senior folks credible information to judge the value, particularly since there's been striking improvements to models in just the last couple of months. As was quipped, some negative opinions of LLM capabilities "are so January".

 ❄                ❄

There's been much angst posted in recent months about the fate for junior developers, as people are worried that they will be replaced by untiring agents. This group was more sanguine about this, feeling that junior developers will still be needed, if nothing else because they are open-minded about LLMs and familiar with using them. It's the mid-level developers who face the greatest challenges. They formed their career without LLMs, but haven't gained the level of experience yet to fully drive them effectively in the way that senior developers do.

LLMs could be helpful to junior developers by providing a always-available mentor, capable of teaching them better programming. Juniors should, of course, have a certain skepticism of their AI mentors, but they should be skeptical of fleshy mentors too. Not all of us are as brilliant as I like to think that I am.

 ❄                ❄

Attendee Margaret-Anne Storey has published a longer post on the problem of cognitive debt.

I saw this dynamic play out vividly in an entrepreneurship course I taught recently. Student teams were building software products over the semester, moving quickly to ship features and meet milestones. But by weeks 7 or 8, one team hit a wall. They could no longer make even simple changes without breaking something unexpected. When I met with them, the team initially blamed technical debt: messy code, poor architecture, hurried implementations. But as we dug deeper, the real problem emerged: no one on the team could explain why certain design decisions had been made or how different parts of the system were supposed to work together. The code might have been messy, but the bigger issue was that the theory of the system, their shared understanding, had fragmented or disappeared entirely. They had accumulated cognitive debt faster than technical debt, and it paralyzed them.

I think this is a worthwhile topic to think about, but as I ponder it, I look at it in a similar way to how I look at Technical Debt. Many people focus on technical debt as the bad stuff that accumulates in a sloppy code base - poor module boundaries, bad naming etc. The term I use for bad stuff like that is cruft, I use the technical debt metaphor as a way to think about how to deal with the costs that the cruft imposes. Either we pay the interest - making each further change to the code base a bit harder, or we pay down the principal - doing explicit restructuring and refactoring to make the code easier to change.

What is this separation of the cruft and the debt metaphor in the cognitive realm? I think the equivalent of cruft is ignorance - both of the code and the domain the code is supporting. The debt metaphor then still applies, either it costs more to add new capabilities, or we have to make an explicit investment to gain knowledge. The debt metaphor reminds us that which we do depends on the relative costs between them. With cognitive issues, those costs apply on both the humans and The Genie.

 ❄                ❄

Many of us have long been advocating for initiatives to improve Developer Experience (DevEx) to improve the effectiveness of software development teams. Laura Tacho commented:

The Venn Diagram of Developer Experience and Agent Experience is a circle

Many of the things we advocate for developers also enable LLMs to work more effectively too. Smooth tooling, clear information about the development environment, helps LLMs figure out how create code quickly and correctly. While there is a possibility that The Genie's Galaxy Brain can comprehend a confusing code base, there's growing evidence that good modularity and descriptive naming is as good for the transformer as it is for more squishy neural networks. This is getting recognized by software development management, leading to efforts to smooth the path for the LLM. But as Laura observed, it's sad the this implies that the execs won't make the effort for humans that they are making for the robots.

 ❄                ❄

IDEs still have a future, but need to incorporate LLMs into their working. One way is to use LLMs to support things that cannot be done with deterministic methods, such as generating code from natural language documents. But there's plenty of tasks where you don't want to use an LLM - they are a horribly inefficient way to rename a function, for example. Another role for LLMs is to help users use them effectively - after all modern IDEs are complex tools, and few users know how to get the most out of them. (As a long-time Emacs user, I sympathize.) An IDE can help the user select when to use an LLM for a task, when to use the deterministic IDE features, and when to choreograph a mix of the two.

Say I have "person" in my domain and I want to change it to "contact". It appears in function names, field names, documentation, test cases. A simple search-replace isn't enough. But rather than have the LLM operate on the entire code base, maybe the LLM chooses to use the IDE's refactoring capabilities on all the places it sees - essentially orchestrating the IDE's features. An attendee noted that analysis of renames in an IDE indicated that they occur in clusters like this, so it would be a useful capability.

 ❄                ❄

Will two-pizza teams shrink to one-pizza teams because LLMs don't eat pizza - or will we have the same size teams that do much more? I'm inclined to the latter, there's something about the two-pizza team size that effectively balances the benefits of human collaboration with the costs of coordination.

That also raises a question about the shape of pair programming, a question that came up during the panel I had with Gergely Orosz and Kent Beck at The Pragmatic Summit. There seems to be a common notion that the best way to work is to have one programmer driving a few (or many) LLM agents. But I wonder if two humans driving a bunch of agents would be better, combining the benefits of pairing with the greater code-generative ability of The Genies.

 ❄                ❄                ❄                ❄                ❄

Aruna Ranganathan and Xingqi Maggie Ye write in the Harvard Business Review

In an eight-month study of how generative AI changed work habits at a U.S.-based technology company with about 200 employees, we found that employees worked at a faster pace, took on a broader scope of tasks, and extended work into more hours of the day, often without being asked to do so.

…

While this may sound like a dream come true for leaders, the changes brought about by enthusiastic AI adoption can be unsustainable, causing problems down the line. Once the excitement of experimenting fades, workers can find that their workload has quietly grown and feel stretched from juggling everything that's suddenly on their plate. That workload creep can in turn lead to cognitive fatigue, burnout, and weakened decision-making. The productivity surge enjoyed at the beginning can give way to lower quality work, turnover, and other problems.

 ❄                ❄                ❄                ❄                ❄

Camille Fournier:

The part of "everyone becomes a manager" in AI that I didn't really think about until now was the mental fatigue of context switching and keeping many tasks going at once, which of course is one of the hardest parts of being a manager and now you all get to enjoy it too

There's an increasing feeling that there's a shift coming our profession where folks will turn from programmers engaged with the code to supervisory programmers herding a bunch of agents. I do think that supervisory or not, programmers will still be accountable for the code generated under their watch, and it's an open question whether increasing context-switching will undermine the effectiveness of driving many agents. This would lead to practices that seek to harvest the parallelism of agents while minimizing the context-switching.

Whatever route we go down, I expect a lot of activity in exploring what makes an effective workflow for supervisory programming in the coming months.

latest fragments:

September 16

previous post:

February 9

next post:

February 18

All Fragments
