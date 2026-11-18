---
title: "Building invisible systems"
date: '2026-11-18T13:52:51+00:00'
category: webclip
summary: 'Essay on leading engineering for tech that supports, but is not, the core experience, where success is invisible, failure public, and leadership centers on enabling workouts, people, and spaces.'
tags: ["engineering-leadership", "product-strategy", "developer-experience", "systems-thinking"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Building invisible systems"
    url: "https://devonestes.com/software-thats-supposed-to-disappear"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--building-invisible-systems-excellent-and-invisible.md"
    kind: repo
---

The author describes moving from building software that **is** the product to leading a team whose systems support Beat81’s workout experiences without being the main attraction. Participants come for exercise and community, not screens, so the ideal outcome is that they get what they need from the tech without thinking about it. This shift makes success largely invisible, while failures are public and disruptive in physical spaces, and it changes how feedback, reliability, recovery, and stakeholder collaboration must be handled.

The text details how fixed workout schedules define recovery windows, why degraded modes and pre‑emptive safety measures matter more than fast rollbacks, and how many more stakeholders beyond product and engineering shape what can be built and when. Leadership becomes an exercise in aligning on what users truly came for, resisting the instinct to chase engagement or surface area, and taking pride in work that must be both excellent and unobtrusive.

## Reading notes

- At earlier companies, impact was easy to see because the shipped software was essentially the entire product, directly tied to customer value.
- At Beat81, the software and hardware power workout experiences, but the workouts and community remain the real product that customers seek.
- Beat81 workouts originally ran without any of the current team’s technology, while the software is useless without the workout, creating a one‑way dependency.
- The software’s role differs from typical SaaS, where the software is the whole experience; in workouts, attention should stay on exercising, not on screens or tablets.
- Every moment a participant spends thinking about the tech instead of the next exercise undermines immersion and the flow state group classes can provide.
- The team’s goal is for participants to receive exactly what they need from the systems while never needing to think about the underlying technology.
- Because success means being unnoticed, usual engineering feedback loops break down: working systems rarely generate thanks, measurable bumps, or public praise.
- Failure is highly visible, occurring in a room full of people who immediately feel the impact of a broken screen or stopped music without filing tickets.
- This asymmetry between silent success and loud failure can wear on engineers who want their work to feel meaningful, so leaders must watch for that effect.
- Proximity to some studios lets the team experience new features themselves, seeing firsthand how they can make workouts more fun and effective.
- New capabilities can help participants reach fitness goals, enable coaches to give more tailored feedback, and give front-of-house staff more time for hospitality and community building.
- Even when the workout stays central, the team can clearly see how their systems make certain experiences and improvements possible.
- In previous writing, the author emphasized detecting production issues quickly and undoing them fast, which works differently for web apps than for workouts.
- In many web contexts, acceptable recovery times are negotiable, and minor bugs can wait for the next deployment without many users noticing.
- For in‑person classes, the workout time, room, and group are fixed; if something fails at the start, the only window to fix it is the duration of that class.
- Elixir’s runtime introspection and live issue resolution help avoid interrupting ongoing workouts, but visible bugs still diminish participants’ enjoyment.
- The effective recovery window is dictated by the class schedule rather than by the team’s development and deployment process.
- The team treats degraded operation as an explicitly designed state, asking whether workouts can still run when something fails and adjusting priorities accordingly.
- They invest heavily in planning for degraded experiences and failure handling, recognizing that canceled or broken classes have different severity than internal issues.
- Rollback alone is insufficient because reverting a deploy in minutes does not undo disruption for a class that has already started.
- To compensate, much of the safety budget goes into earlier stages: detailed testing, progressive rollouts, avoiding peak times for releases, and using feature flags for fast toggling.
- Incidents follow the timetable of class schedules, with load and risk concentrated in morning and evening peaks rather than spread evenly.
- This pattern lets the team choose safer times for experiments or test workouts with fewer participants, and use empty studio windows for more isolated testing.
- Stakeholders extend well beyond product, sales, and nearby functions; dependencies reach to front-of-house staff, coaches, and real estate teams.
- Features that change in‑studio behavior cannot be shipped until staff and coaches know how to use them, because they run the room and face participant questions.
- Quietly deploying changes that alter staff interfaces or participant expectations effectively ambushes colleagues in front of customers.
- A feature release completes only when it is successfully used in production, so communication and training plans are part of the project, not afterthoughts.
- Release timing becomes a shared decision with teams outside engineering who have their own constraints and are not organized around software delivery cadence.
- For new studios, the real estate team needs hardware specs and room layout guidance months in advance, tying physical space design closely to technical choices.
- Placement of screens, sight lines, and physical room capabilities involve decisions that become fixed long before all desired information is available.
- Software can be refactored, but walls and physical layouts cannot, so casual planning choices can become years‑long constraints.
- These are not problems solved by more Slack messages; they are real, time‑sensitive dependencies with months‑long lead times on teams outside software.
- A sizeable part of the author’s role now happens outside engineering, focusing on which decisions can change and which are permanent, and making permanent ones widely visible.
- This broader alignment forces realistic conversations about failure modes and who will be physically present when something goes wrong.
- Involving the people who actually run workouts in design discussions prevents shipping idealized experiences detached from real‑world constraints.
- Coaches and staff bring grounded knowledge about what really happens in classes and can provide strong feedback before ideas reach customers.
- All these considerations trace back to a central question: what did users actually come for in the first place?
- When the team is not the destination, common product instincts need adjustment: user engagement with the system stops being a clear goal.
- Attention directed to the tech is attention pulled from the core experience, so more visible product surface is not automatically beneficial.
- The team cannot rely on usage metrics alone to feel impactful, because the desired outcome is closer to users never having to think about the system.
- Building the Power Zones RIDE workouts illustrates this: the team added a metrics screen for cycling classes and constantly debated how prominent and information‑dense it should be.
- They aimed to make the data screen helpful while preserving vital elements like the coach’s motivation, music-driven atmosphere, and community connections.
- Excessive focus on individual screens would undermine those aspects, so reaching the right balance required substantial time and multiple iterations.
- Early feedback suggests they achieved this balance, and the author feels proud of contributing to that workout experience.
- Many teams work on supporting systems rather than the main thing users seek, such as internal platforms, payment flows, or other transitional product areas.
- The risk for such teams lies in measuring themselves as if they were the destination, potentially damaging the true destination in pursuit of their own metrics.
- The author finds that explicitly acknowledging their supporting role with the team, as a hard design constraint and source of pride, is highly helpful.
- The work must be both excellent and invisible, which is described as a more difficult engineering and product challenge than excellence that demands user attention.
- The author enjoys tackling this harder problem of building high‑quality systems that deliberately get out of the way of the primary experience.
