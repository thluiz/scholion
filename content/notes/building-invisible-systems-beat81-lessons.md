---
title: "Building invisible systems"
date: '2026-11-17T14:58:53+00:00'
category: webclip
summary: 'Author reflects on leading a team whose software underpins, but is not the focus of, Beat81 workouts, exploring invisible success, tight recovery windows, broad stakeholders, and leadership shifts.'
tags: ["product-engineering", "infrastructure", "leadership", "user-experience"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Building invisible systems"
    url: "https://devonestes.com/software-thats-supposed-to-disappear"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--building-invisible-systems-beat81-lessons.md"
    kind: repo
---

The author describes moving from building software that is the entire product to leading the team behind Beat81’s workout tech, where the workout and community are the real product and the software is only an enabler. Success for this team means participants get what they need without thinking about the tech, so impact is hard to see, failures are very public, recovery windows are dictated by class schedules, and “stakeholders” include coaches, front-of-house staff, and real estate. This demands careful design of degraded modes, earlier investment in safety, long-range coordination, and a leadership mindset that treats invisibility as a design constraint and a source of pride.

## Reading notes

- At earlier jobs, shipped software largely was the product, so value and impact were easy to show through releases.
- At Beat81, the team builds software and hardware that power in-studio workout experiences, but customers come for exercise and community, not the tech.
- Beat81 workouts existed before the current tech stack, with just a coach, equipment, and a group, while the software is useless without the workout, making the dependency one-directional.
- The author emphasizes that “you’re not the product” does not mean the work is unimportant; the tech differentiates Beat81 and retains users who value technology-enhanced workouts and real-time feedback.
- The role of software differs from typical SaaS: in SaaS, the software is the experience, but in workouts, time spent on screens or tablets detracts from the physical session and flow state.
- The ideal outcome is that participants receive the benefits of the system without consciously noticing the technology at all.
- This goal of “getting out of the way” disrupts standard engineering feedback loops, since visible interaction is not the measure of success.
- When the system works, there is usually no explicit positive feedback, no clear NPS bump, and no public praise tied to a release.
- The author compares this invisibility of success to the asymmetry often experienced in security work, now seeing it also applies to product engineering in this setting.
- Failures are immediately visible in the studio: broken screens, silence when music stops, and discomfort in front of full classes.
- These failures are felt by participants on-site, without needing tickets or logs to surface the problem, making the impact highly tangible.
- The asymmetry between invisible success and visible failure can erode morale, especially for engineers who want work that clearly matters.
- Proximity to some studios lets the team experience new features themselves and see firsthand how they influence workouts and participant motivation.
- New capabilities that help participants reach fitness goals, enable more personalized coaching, or free staff to offer better hospitality provide clear, felt impact even though the workout remains the central experience.
- The author’s earlier thinking on failure focused on quickly detecting and undoing problems, where “quickly” was negotiable in web apps.
- In the studio context, workouts are fixed time blocks; if something breaks, the team only has that class duration before participants leave.
- Elixir’s runtime introspection and on-the-fly issue resolution help avoid stopping workouts, but visible bugs still diminish people’s enjoyment.
- The recovery window is controlled by the class schedule rather than the deployment pipeline, prompting a shift in planning.
- Degraded operation must be intentionally designed: the team asks whether a failure still allows the workout to proceed, treating that as a key severity distinction.
- They devote substantial planning to degraded experiences and failure handling so that issues do not cancel or ruin classes.
- Rollback, while necessary, is insufficient because a reverted deploy cannot restore a just-started class that was already impacted.
- Safety work is moved earlier through detailed test plans, progressive rollouts, avoiding peak windows for risky changes, and gating sensitive features behind flags.
- Incident risk is concentrated in morning and evening peak class times, with lower-risk opportunities for testing during quieter periods or empty studios.
- This time-based pattern lets the team choose safer moments for “production tests” and isolated environment checks.
- Stakeholders extend far beyond product and sales; frontline staff, coaches, and real estate all depend on engineering decisions.
- Features that change studio behavior cannot be deployed without preparing Front of House staff and coaches, who run the room and answer participant questions.
- Quietly shipping studio-facing changes without training effectively ambushes colleagues in front of customers, so deployment does not mark completion.
- Communication plans become core project elements, and release dates are shared decisions made with teams having separate constraints.
- Opening new studios requires real estate teams to know hardware needs and room layout months ahead, tying physical design to engineering choices.
- Decisions about screen placement, sightlines, and room capabilities can become permanent because walls cannot be refactored like code.
- Some dependencies and lead times span months and involve teams that will not reorder their quarter around engineering, so planning must respect their timelines.
- A large portion of the author’s role occurs outside engineering, focusing on which decisions are fixed versus adaptable and ensuring shared visibility of permanent choices.
- Collaborating directly with people who run workouts forces realistic discussions about failure modes and who will be present when issues occur.
- This collaboration helps avoid designing idealized experiences detached from what actually happens in classes, since operators provide grounded feedback early.
- The core leadership question is identifying what users truly came for, which in this case is the workout, not the interface.
- When the software is not the destination, common product instincts need adjustment: maximizing engagement or interaction can conflict with the real goal.
- Additional surface area or usage does not automatically represent improvement, because attention spent on the tech subtracts from the workout itself.
- The team cannot lean on conventional usage metrics for impact, since a better outcome may mean participants almost never notice the system.
- In building Power Zones RIDE cycling workouts, the team added a personalized metrics screen and repeatedly revisited how prominent and information-dense it should be.
- They balanced the importance of data against preserving other core elements: coach motivation, music-driven atmosphere, and social connection.
- Excessive focus on individual screens would undermine those elements, so the team iterated extensively to find an appropriate balance.
- Early feedback suggests they achieved a satisfying mix, and the author expresses strong pride in contributing to that experience.
- The author notes that many teams build supporting systems—platforms, checkout, payments, or flows that users pass through on the way to their real goal.
- Treating these supporting systems as destinations can distort metrics and potentially degrade the actual user destination.
- Being explicit with the team that their work is not the main attraction helps, framed as a design constraint and as something to be proud of.
- The team’s challenge is to produce work that is both excellent and invisible, which the author views as a harder and more interesting problem than excellence that demands attention.
