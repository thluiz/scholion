---
title: "What Agile Development Looks Like on a Remote Team"
date: '2020-07-05T14:11:17+00:00'
category: webclip
summary: 'Article describes how Doist’s remote Windows team adapted agile practices with a shared backlog, bi‑weekly planning meeting, story points, kaizen, and flexible sprints suited to async work.'
tags: ["agile-development", "remote-work", "software-teams"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "What Agile Development Looks Like on a Remote Team"
    url: "https://web.archive.org/web/20200610040258id_/https://doist.com/blog/agile-development-remote-team/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--agile-development-on-doist-remote-windows-team.md"
    kind: repo
---

Doist’s fully remote engineering teams choose their own workflows under company‑level monthly Objectives. The Windows team grew from a one‑person setup with no process into a small group facing scattered requests, unclear priorities, and limited visibility into each other’s work. Borrowing from agile but constrained by asynchronous, time‑zone‑spanning collaboration, they avoided traditional scrum rituals like daily stand‑ups and pair programming, aiming instead to protect long stretches of deep work while still improving collaboration, estimates, and delivery.

They evolved a process centered on three elements: a single backlog, a bi‑weekly planning meeting, and a two‑week sprint. All incoming work from Support, Design, DO Squads, telemetry, and internal ideas feeds into an Azure Boards team backlog, which is expected to capture nearly everything the team will work on. The team lead curates this backlog and uses it to propose sprint scopes, while a rotating monthly “hero” surfaces and refines user‑driven issues and ideas from Twist threads into actionable items. Each backlog item includes a short description and a link to its originating discussion, making the backlog a comprehensive, up‑to‑date picture of potential work.

## Reading notes

- Company‑wide work is guided by monthly Doist Objectives, but each development team chooses its own execution process, enabling experimentation with approaches like agile in a remote context.
- The Windows team started as a single developer with no defined process, which became problematic as more people joined and coordination needs increased.
- As the team grew, they struggled with requests arriving from many directions, making prioritization and delivery timelines largely guesswork.
- Long periods of isolated work turned developers into “lone wolves”, limiting awareness of where teammates were blocked and delaying help when people got stuck.
- Fully reproducing scrum in a remote, async‑first culture proved difficult because practices like daily check‑ins, rapid feedback loops, and pair programming clashed with time‑zone differences and scheduling friction.
- The team wanted to preserve the remote advantage of flexible scheduling and multiple days of uninterrupted deep work, which they saw as critical for engineering focus.
- They looked for a process that would encourage collaboration, support evidence‑based time estimation, and help them ship high‑quality work reliably.
- Their workflow is treated as a moving target: they keep iterating, adding steps when new needs appear and removing ones that no longer fit the team’s reality.
- The described process builds on the team’s experience plus ideas from books on agile, kanban, and scrum by Ángel Medinilla, Eric Brechner, and Jeff Sutherland.
- All work sources funnel into a single internal backlog: user issues and ideas from Support, polishing tasks from Design, high‑priority projects from DO Squads, and bugs, refactors, and new features from internal telemetry and brainstorming.
- They maintain a strict expectation that almost nothing gets done outside the backlog, which reinforces consistent use and confidence that it mirrors real work.
- The team lead owns and curates the backlog, coordinating with teammates to ensure future work is represented and using that view to shape proposed sprint scopes.
- A rotating “hero” role focuses on communication with other teams, especially Support, turning user reports and suggestions from Twist threads into detailed backlog items.
- Each backlog entry contains a brief explanation plus a link back to its original Twist discussion, tying implementation work to its source context.
- They acknowledge that backlog maintenance is demanding, but see it as necessary for prioritization, uncovering dependencies, and planning sprints under growing pressure.
- Their sprints last two weeks; trials with one‑week sprints failed because asynchronous communication can slow decisions and make some tasks unrealistic in a shorter window.
- The sole team meeting every two weeks, around two hours long, aims to review new work, surface risk and uncertainty, and agree on the upcoming sprint scope.
- The meeting follows a fixed structure: scoring new backlog items, deciding sprint scope, and then discussing kaizen improvements.
- In scoring, they walk through new items, talk about implementation and effort, and defer work that is still too vague or uncertain to estimate.
- They use story points to express relative difficulty rather than duration, focusing on which tasks are more challenging compared to others.
- Story points are taken from the Fibonacci sequence to reflect increasing uncertainty on larger tasks and to encourage breaking down oversized items.
- The team calibrated story points by reviewing past tasks and agreeing which represented low and higher values, such as a simple bug for 1 point and a multi‑dependency task for 13 points.
- Team velocity, defined as the average story points completed over recent sprints, informs how much work they can realistically include in a new sprint.
- They suggest further reading on the value of story points from an external scrum.org blog post.
- Planning poker is used to assign story points, with each teammate privately choosing a Fibonacci value, then revealing and reconciling differences together.
- The task creator gives context and likely hurdles, the team asks clarifying questions, and only then does everyone independently pick a difficulty score.
- If estimates are close, they simply average them; if the spread is wide, those with extreme values share their reasoning and the group discusses before re‑estimating.
- Through repeated planning poker sessions, the team learns how colleagues think about complexity and uncertainty, and the estimation step becomes faster.
- Once scoring is complete, they choose which items to include in the next sprint by looking at past velocity and discussing what feels achievable.
- Sprint composition is decided collaboratively, without a formal prioritization framework, blending data from story points with individual and team judgment.
- They always factor in commitments to broader company initiatives (DOs) and ensure those projects receive the needed attention in scope decisions.
- In the kaizen segment of the meeting, they review the last two weeks and identify small, concrete tweaks to improve how they work together.
- Kaizen is described as an approach focused on ongoing, incremental improvements, originally popularized in the 1950s at Toyota.
- They contrast kaizen with “10x thinking”, which pursues large, infrequent leaps in innovation, and argue both approaches need to coexist within teams.
- After planning, the team has two weeks to execute, with each developer balancing demanding work with some simpler tasks to recover between tougher efforts.
- Daily stand‑ups are seen as a poor fit for their remote setup because coordinating a fixed time harms flexibility, a key benefit of working remotely.
- Instead of stand‑ups, they monitor the movement of work items on a shared board and prioritize according to the board’s ordering and the meeting’s context.
- As work progresses, they rely on asynchronous Twist threads and messages to coordinate, especially when progress on a task slows or stalls.
- The team leader watches for stuck items, helps by liaising with other teams, offers rubber‑duck debugging conversations, and supplies historical background on the codebase.
- The article notes that agile was originally articulated for co‑located teams and even emphasizes face‑to‑face communication as highly effective.
- They highlight that one of agile’s core values is responding to change, and use this to justify adapting or discarding practices that don’t serve a remote team’s needs.
- Working in a fully remote company is framed as a chance to try new collaboration models, sometimes borrowing from co‑located practices and sometimes inventing new ones.
- The authors treat their current process as a snapshot tailored to their specific moment and context, expecting it to keep evolving with team and user needs.
- Agile is presented as a flexible toolkit from which teams can select techniques that support delivering strong customer experiences from any location.
