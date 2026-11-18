---
title: "How to waste half a million dollars"
date: '2020-06-17T11:51:02+00:00'
category: webclip
summary: 'Article argues that startups often "save" on PaaS by running their own servers, but hidden engineering and ops costs can reach hundreds of thousands and distract from the core product mission.'
tags: ["startups", "cloud-infrastructure", "heroku", "engineering-management"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "How to waste half a million dollars"
    url: "https://web.archive.org/web/20200617050314id_/https://dev.to/heroku/how-to-waste-half-a-million-dollars-474e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--how-to-waste-half-a-million-dollars-servers.md"
    kind: repo
---

The article describes how startups drift from their true mission of building and selling a great product into running infrastructure. Using a fictional company, GoCo, it shows how moving from a platform like Heroku to self-managed servers appears to cut the hosting bill but actually consumes valuable engineering time, leads to new operational headcount, and can add up to roughly half a million dollars per year. The author argues that teams rarely account for these hidden costs or question whether operating servers aligns with the company’s mission.

## Reading notes

- The author says every startup they worked for effectively had the same mission: build a product customers love enough to recommend, charge for it, and make money.
- The piece focuses on how teams get distracted from this mission and end up working on activities that do not help it.
- The fictional startup GoCo starts by hosting its product on Heroku, which handles updates, patching, and general server concerns.
- Early on, GoCo uses the platform to build a product, deliver demos, gain first users, and generate interest at meetups and conferences.
- As costs grow, GoCo’s CFO reacts to spending "hundreds of dollars" on Heroku and pushes for running their own servers to lower the bill.
- A top engineer, Grace, spends several weeks migrating the application to low-cost virtual machines, and the visible hosting bill goes down.
- The author points out that this is a mistake because the company paid Grace for weeks of work, and those labor costs are usually ignored when celebrating a lower service bill.
- During the migration, Grace could have been building new product features or optimizations that support the company’s mission.
- The article emphasizes that missing features do not show up on a balance sheet, but without compelling features and a better product the startup cannot make money.
- The author uses a stark example: the most effective way to cut costs is to fire everyone and shut down, which no mission statement endorses.
- Over time, GoCo’s bargain servers experience downtime, especially during a critical conference, because patching and configuring is now the company’s responsibility.
- Grace is not a full-time operations engineer and is likely evaluated on feature delivery, making server management a misalignment with her role.
- After an outage, executives hold a post-mortem and decide they need an operations specialist or team to handle servers.
- The discussion may cover the new ops salary but usually ignores the estimated $50,000 in engineer time, bonuses, and ramp-up costs involved in hiring.
- The author notes that no one talks about how a highly paid employee is now focused entirely on infrastructure work that does not directly advance the original mission.
- They have seen leaders complain about the cost of support, team events, and software services, but not about engineers shifting from feature delivery to infrastructure maintenance.
- A year later, GoCo is thriving and plans a GoCoCon, while the new operations team is praised for metrics like 99.999% uptime.
- Despite these successes, leadership still does not ask what a platform like Heroku would cost compared with the full expense of running an internal operations team.
- The author estimates that a team of three to four operations engineers can cost about half a million dollars per year when including salary, benefits, stock, hiring and bonuses, communication overhead, and office costs.
- They call this $500,000 figure a conservative guess and argue managers should reevaluate Platform-as-a-Service options.
- The comparison between PaaS and low-cost virtual machines should include the cost of the engineers required and the impact on the team when attention drifts away from the mission.
