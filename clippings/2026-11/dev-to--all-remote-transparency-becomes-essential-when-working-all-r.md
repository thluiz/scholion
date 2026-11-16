---
url: "https://dev.to/codestream/all-remote-transparency-becomes-essential-when-working-all-remote-part-3-1khf"
captured_at: "2026-11-16T01:37:45+00:00"
title: "All Remote: Transparency becomes essential when working all-remote (Part 3)"
domain: "dev-to"
---

## [](#introduction)Introduction

[In Part 1](https://dev.to/codestream/we-are-all-remote-developers-working-from-home-part-1-2od1), we discussed the personal and human factors affecting all of us during the COVID-19 pandemic. In [Part 2 of this series](https://dev.to/codestream/developers-must-choose-collaboration-in-an-all-remote-world-part-2-2oh5) we talked about how a combination of cultural and technology factors has traditionally led to insufficient collaboration among developers.

From a technology perspective, until recently it’s been surprisingly difficult to carry out simple tasks like asking a question about code you are viewing in your editor, but don’t understand. If you are among the developers who use tools like Slack or GitHub to discuss code, there are some significant limitations in both, but for different reasons. Developers often turn to Slack to ask ephemeral questions about code that’s unclear, but this involves copying and pasting from your IDE into a channel, and having to then recreate the whole context you just lost in order to explain to the recipient what they are actually looking at. Code reviews are often conducted In GitHub, where the context is more clear, however, you are limited to discussing only the changes that are part of that PR. What if you have questions or a suggestion about another part of the code that is not changing?

Here we will focus on another aspect of remote work. Before your team went all-remote, it was relatively easy to keep informal tabs on what everyone was working on. Just looking around you, could see who is at their desk or in a meeting, or who moved a task on a board. Gone is the physical tap on the shoulder to ask a question or bounce off an idea. In an all-remote world, there is a need to become more transparent in order to improve collaboration, perhaps to demonstrate to your boss that you are actually working while at home, and most importantly, to improve performance and code quality for your team and your company.

## [](#what-is-transparency-in-software-development)What is transparency in software development?

One way to think of transparency is to consider it a philosophy, or a point of view. It implies openness, communication, and accountability. Transparency is operating in such a way that it is easy for others to see what actions are performed, and how they are performed. The benefits of transparency were well understood long ago. As explained by [Nathan Donaldson](https://www.boost.co.nz/blog/2018/11/agile-transparency-reduces-project-risk) of Boost, there are many different dimensions to transparency. For a manager, it might mean knowing the status of a project. For a developer it might be seeing work in progress on a board. In both cases, it’s about producing the best product with the lowest risk. This chart from Boost, who specialize in Agile risk management, illustrates its benefits:

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--HzFucw1p--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh5.googleusercontent.com/Eh9dT-IcR2k9SBZJdOJ8jy0jPIyMH1crBFlyVRa3WxCBUDfbTZH9bPaHxkeDji7mggdAyRlNXHLUU_i1X56SYY5TDGU1zSXlrACakQSJYN_S1YRCEyIFElit-lSI0JCrLSRfPCip)](https://res.cloudinary.com/practicaldev/image/fetch/s--HzFucw1p--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh5.googleusercontent.com/Eh9dT-IcR2k9SBZJdOJ8jy0jPIyMH1crBFlyVRa3WxCBUDfbTZH9bPaHxkeDji7mggdAyRlNXHLUU_i1X56SYY5TDGU1zSXlrACakQSJYN_S1YRCEyIFElit-lSI0JCrLSRfPCip)

## [](#from-transparency-to-visibility)From Transparency to Visibility

[Kanban-style boards](https://www.atlassian.com/agile/kanban/boards) have been popular in software development for a long time. If you used to rely on a physical board to have visibility of the state of a project, in a remote team that becomes impractical. Some software tools, like [Trello](http://trello.com/), implement the methodology of a kanban board and give you task level visibility of what your teammates are working on. That is very useful and quite adequate for improving visibility in a remote team. However, the value of radical transparency becomes more evident in a remote environment. As communication is a bit harder, it’s easier to make mistakes or incorrect assumptions.

As described by Matthew Bellows in [this post by First Round Review](https://firstround.com/review/the-case-for-startups-to-make-radical-transparency-the-top-priority/), there is a strong case to be made for Radical Transparency among startups, which is likely to apply to companies of all sizes. Matthew says: “Whether you’re starting from scratch or looking to make your existing culture more transparent, start by building it into the tools you use every day. Make the executive team’s calendars visible internally, for example, so everyone can see who’s in a given meeting or when colleagues are available.”

That is why at [CodeStream](http://codestream.com/) we have been working on giving development teams the tools they need to increase visibility at a granular level.

## [](#the-networked-ide-comes-of-age-in-a-remote-era)The networked IDE comes of age in a remote era

Developers tend to choose their IDEs individually in a BYOD world. In any given team you might find some using VS Code, others IntelliJ, a third group Atom or pycharm. One of the best ways to increase granular visibility is to connect your teammates’ IDEs to each other. That is exactly [what we have done](https://www.codestream.com/blog/codestream-7-0-code-reviews-in-your-ide-and-live-view) at CodeStream. We just introduced Live View, a new feature in our collaboration platform that allows admins or any developer to see a live snapshot of what everyone is working on. Specifically we show each user’s name with a list of the repositories in which they have made local changes (i.e., edits that haven’t been pushed). When you hover over a repo entry, you can see the actual files that have changed, as well as the number of additions and deletions, like this:

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--H7fDopXo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh5.googleusercontent.com/xs0Zb4DIOA2xDBNMDcAazfltnQD_Fd2uCiQ9P7bl9mCZo_Tr8dM7IK4XMHlxvc8EQzJswT91P5Myu6fV8T8wXD1ohW-jXPRj7BIKdbOQgS_PpRr9fwJE7Iw681JcQLb-lFrwH655)](https://res.cloudinary.com/practicaldev/image/fetch/s--H7fDopXo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh5.googleusercontent.com/xs0Zb4DIOA2xDBNMDcAazfltnQD_Fd2uCiQ9P7bl9mCZo_Tr8dM7IK4XMHlxvc8EQzJswT91P5Myu6fV8T8wXD1ohW-jXPRj7BIKdbOQgS_PpRr9fwJE7Iw681JcQLb-lFrwH655)

Note also the warning sign indicating that Peter may have a potential merge conflict in the “gore” repo. He can then contact whoever is also working on that file in “gore” and resolve the issue before it becomes a painful process to unwind, or to ensure that they aren’t duplicating work.

## [](#documenting-code-is-a-great-way-to-increase-transparency)Documenting code is a great way to increase transparency

Software development projects are notorious for [their lack of useful documentation](https://softwareengineering.stackexchange.com/questions/101388/why-do-so-many-libraries-have-no-poor-documentation). When working remotely, documenting software becomes increasingly important as informal communication decreases while the increased friction can slow things down. Yet, asking developers to document their code may not be the best answer.

In Part 4 we will describe how we have tackled the documentation issue at CodeStream with a radical idea. We capture the interactions that take place every day among developers in tools like Slack, Jira, and GitHub and turn them into nuggets of wisdom that explain how the code works.
