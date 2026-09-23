---
url: "https://dev.to/leading-edje/coding-agents-are-here-is-your-team-ready-for-ai-devs-3dk2?context=digest"
captured_at: "2025-08-11T15:26:43+01:00"
title: "Coding Agents are here: Is your team ready for AI devs? - DEV Community"
domain: "dev.to"
---
In this post we'll explore the concept of AI agents as software engineers on your development team. The idea that you could write up an enhancement or bug fix and assign it to an AI team member and see what they came up with a short while later would have sounded fantastical only a few years ago, and yet, with the announcement and preview of GitHub Copilot Agents, this is a real technology that exists and you can make use of today.

## Introducing GitHub Copilot Coding Agents

GitHub Copilot Coding Agent is a new technology, currently in preview, associated with GitHub pro and enterprise accounts. With Coding Agents you can assign individual issues in a GitHub repository to GitHub Copilot, just like you were assigning it to a team member.

Copilot will then create a branch for your issue, just like a developer would, and begin to plan its approach to carrying out the work item.

> Quota Usage Note: GitHub Copilot Coding Agent uses part of your account's allocated monthly premium requests.

### Coding agents at work

After analyzing the issue and your repository, it forms a plan of action to accomplish the work you've assigned to it. As it works, the branch's comment updates to reflect Copilot's progress, accomplished tasks, and remaining work. This helps you monitor its progress and acts as a reference to help ground the AI agent as it works.

Copilot will analyze your code as it works and can also make use of additional resources such as Model Context Protocol (MCP) servers you have configured on GitHub and optional additional documentation you provide for Copilot on the structure of your repository.

I've also noticed Copilot making use of command line tools to find relevant strings in files in your repository, which can help it orient itself. Copilot is also capable of executing commands to build and test applications, and can even resolve build issues with missing dependencies it finds on its end.

### Security and GitHub Copilot

While all of these capabilities are interesting, they also raise important security questions. By default, Copilot has firewall rules in place that prevent it from working outside of GitHub's sandboxed ecosystem. Additionally, any violations of these policies will be logged for your review later on.

It's worth noting that these features are currently only available if your code is on GitHub and you have a paid plan that supports it, so you're also going to benefit from all of GitHub's standard and enterprise security features.

### Completing a pull request

When Copilot believes it is complete, it will notify the person who assigned it the task who can then review the pull request for changes. The developer can either approve the pull request or request changes. If changes are requested, Copilot will respond to any comments and notify you when the work item is ready for review again.

Once you're satisfied with Copilot's work, you can mark the pull request as ready for review. This will trigger more parts of your workflow, such as additional tests or having the standard GitHub Copilot system review the pull request, summarize it, and make suggestions. Once you're satisfied, you can approve the pull request, merge it, and it becomes part of your codebase as GitHub closes the issue.

### Can AI agents really serve as team members?

So, how good is Copilot? Is this going to replace members of your team?

Well, probably not, but it might change how you work or how you hire.

### How coding agents change how I write code

I'm early on in my journey working with copilot, but I'm already impressed. As an experienced developer I can write out what I'm trying to accomplish in technical terms, assign it to Copilot, and see it have a result that's close to what I envisioned. This does require me to think about how I would try to solve a problem and the type of solution I'd like to see, and highlight any areas of concern I have with potential implementations. Interestingly, this is the type of thing I'd probably normally communicate to a technical team member through a direct message or a comment on a work item already.

Because AI agents are capable of working quickly, I've found myself able to quickly gather some thoughts on relatively simple changes, send them over to Copilot, and then come back to that topic later on when I have more focus. I can easily see senior engineers writing up a request, sending it to Copilot, attending a meeting, then reviewing and improving Copilot's result after they're free.

I've found myself also starting development sessions by reviewing what Copilot sent me on something between work sessions, which can be a great way of getting into the flow of something - or take care of the more tedious aspects of software engineering while letting me focus on the strategic direction or specific concerns I care about.

### How coding agents might impact hiring

If you look at the prior section, you'll see that a lot of what I'm doing is more senior or supervisory in nature versus directly authoring code. While I'm still writing code and enjoying it, I'm finding that the code I'm writing is less boilerplate or trivial in nature and more specialized and strategic.

This is good, but not all developers can do this. You need a certain level of experience to be able to guide other developers and evaluate their code effectively, and this holds up well for AI.

Because of this, I view AI as filling similar roles to more junior team members: executing on well-defined and standardized tasks that can be easily communicated.

While AI doesn't replace the more junior team members in your organization, it does rival them in some ways:

- AI agents are becoming increasingly able to get unstuck on their own
- Copilot has the breadth of its training data available to it, so it likely knows libraries junior devs don't yet
- Copilot works quickly, and can produce a lot of code very quickly, outpacing even senior developers

Of course, junior team members have a lot of value as well, and can do things that AI can't:

- A greater degree of domain knowledge in your organization, its products, its data, and its business context
- Effectively consider the end user and the context in which code operates
- Human level problem-solving, common sense, and decision-making
- The ability to debug problems or scenarios related to specific data situations
- The tendency to grow and become senior engineers

A good junior developer is going to provide far more value to an organization than a solid AI agent is able to, but I can see the temptation for organizations to rely on AI agents instead of junior developers, and this scares me for our industry and the many talented people already struggling to get a foot in the door.

Ultimately, if you're an organization that has busy senior engineers and code already present on GitHub, Coding Agents are something that you should try out and see how it impacts your workflow and productivity. Just be cautious because although Coding Agent is usually cheaper than a junior engineer's salary, it's not a replacement for talented, growing, flexible, and human engineers on your team.

### Where AI agents fall short

In conversations about AI and particularly about AI productivity there's a central truth that is often overlooked: Most of software engineering isn't about writing code.

I've been writing code for the vast majority of my life, and over two decades professionally. While a lot of my job is around writing code, that code only comes after:

1. Understanding the business need or current inadequate behavior
2. Determining what an ideal solution should do
3. Identifying several different ways of achieving this goal
4. Selecting a leading candidate for implementation - often with collaboration from others who understand other areas and other needs
5. Identifying places in code that will need to be adjusted to support the change
6. Making code changes to support the new behavior
7. Ensuring the code works
8. Thinking of ways the code might break, edge cases that we might not have considered, etc. then making sure the code works for those ways as well.
9. Ensuring the code is as secure, testable, and performant as we expected it to be when we selected our candidate solution
10. Communicating the change in documentation and to others.
11. Ensure the change flows through the processes for feedback, testing, and deployment to various environments

As you can see, code changes are only a small portion of software engineering, yet we pay an inordinate amount of attention to them when we think about AI productivity solutions and even when we consider using offshore development resources.

While I believe AI systems can already perform some of these steps to some degree or another, we tend to evaluate their effectiveness mostly on authoring new content, which is a strength area for AI systems. However, humans have strong skills across all of these areas and knowing what to change and the implications of different approaches along with how this fits into the existing data and application architecture are critically important pieces of software engineering.

Also keep in mind that in modern software engineering a change is often needed across multiple different services and databases. While an AI agent might be able to handle changes in one place, they might find themselves less equipped to know all the services that need to change and make the requisite changes for those areas.

### AI and Human Partnership

Because of the complexity of software engineering and the relative strengths and weaknesses of AI and humans, I think that AI agents and AI tooling are best deployed for targeted tasks that have been thought through by an experienced engineer.

An ideal flow might be:

1. Engineers vet an organization's needs and determine a series of technical changes needed to support the new goals
2. These individual changes are written up as work items and either assigned to other engineers or assigned to AI agents
3. AI agents or engineers work on the change and send a draft pull request on for review
4. The change is manually tested and verified by another engineer who uses it as a starting point for the final pull request
5. The developer makes additional improvements, changes, and tests to support the pull request and ensure it fully meets the organization's needs
6. The PR is marked ready for review
7. Other developers review the PR, familiarize themselves with the changes, and leave comments
8. The change eventually merges into the main branch and reaches production, where it will be supported by a team that understands the changes and designed the approach.

### Where software engineering may be headed with AI Copilots

AI agents like GitHub Copilot are powerful and destined to change how organizations and engineers hire and work.

I believe that software engineers can focus on the big picture, stay oriented around technical changes going on in their systems, but use AI to do the majority of the work on well-defined tasks the engineers define, then customize the final behavior of those changes.

Not every change will benefit from AI, and some more sensitive pieces of work reveal new things to think about with each line of code that needs to be modified or added, but a strategic deployment of AI can help busy engineers remain productive between meetings and optimize their time on a busy schedule.

I also hope that the emergence of AI as skilled solutions implementers will help focus experienced and new software engineers on other core competencies that are uniquely theirs: domain knowledge, communications skills, past experiences, empathy for users and business stakeholders, and the ability to evaluate a number of different plans and possible implementations and select the one that is right for the business today and where they're going tomorrow.

AI is advancing at a tremendous rate and being an efficient, experienced, well-rounded, and adaptable engineer is more important than ever, but I'm glad to have copilots along for the ride as we build new things together.
