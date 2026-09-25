---
title: "Architecture Is a Game of Constraint Satisfaction"
date: "2026-09-23T17:58:16+01:00"
category: webclip
has_commentary: false
summary: "Gregor Hohpe argues architects keep designing around constraints (procurement lead times, hardware size, coupling costs) long after the constraint that justified them has quietly disappeared."
tags:
  - software-architecture
  - cloud-computing
  - technical-debt
sources:
  - title: "Architecture is a game of constraint satisfaction."
    url: "https://architectelevator.com/architecture/architecture-constraints/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/architectelevator-com--architecture-is-a-game-of-constraint-satisfaction.md"
    kind: repo
---

Gregor Hohpe builds the essay around a line from Eli Goldratt: technology only brings benefit when it removes a limitation. His extension of that idea is the harder part: once a constraint is gone, the behavior it shaped doesn't automatically change with it, because nobody explicitly remembers which constraint produced which habit. His example: business units write bloated requirement lists because they learned, under an old constraint, that adding requirements later was slow or impossible. Removing that constraint through agile ways of working doesn't erase the habit of asking for everything upfront.

He runs that lens over several constraints he says have quietly weakened in enterprise IT without the corresponding behavior catching up. Cloud computing removed the constraint on provisioning lead time, but IT managers still price cloud servers by multiplying hourly cost by 720 hours, the same math they used to compare against owned hardware, ignoring that instant provisioning changes the calculation entirely. Server size is the constraint he spends the most space on: most enterprise architectures assume a single machine can't handle the workload, an assumption he says a modern high-end server (240+ cores, 16TB RAM) makes false for the overwhelming majority of real business workloads, not just hypothetically. He extends the same logic to "loose coupling," arguing the constraint that justified it (change being hard to locate and hard to make) has been substantially reduced by better tooling, so the old default toward looser coupling may no longer be worth its cost everywhere.

## Reading notes

- Central mechanism, from Goldratt: technology helps only by removing a limitation, but removing the limitation doesn't automatically change behavior shaped by it, since the constraint is usually baked into practice without being explicitly named.
- Requirements-list example: business users learned that adding requirements later was expensive or impossible, so they front-load every possible requirement; removing that constraint through agile practices doesn't automatically unwind the habit.
- Solar power example (from his own rural setup in Southeast Asia): centralized power generation doesn't scale down economically, but componentization (interchangeable panels, controllers, batteries) and commoditization (cheap, reliable individual parts) let small-scale local generation bypass that constraint entirely, something a purely economies-of-scale argument for centralization misses.
- Cloud provisioning: IT managers still compare cloud server hourly cost x 720 hours against owned hardware monthly cost, a comparison that assumes the old constraint (long procurement lead times, sunk hardware cost) still applies, when cloud's actual benefit is the removed constraint itself, not just a different price point.
- Server size, his most concrete data point: a Dell PowerEdge R960 offers 240 cores and 16TB RAM; he estimates most enterprise workloads (his example: a 100,000-account insurance system) fit comfortably on a single modern server, undercutting the standard assumption that scale requires distribution.
- On distributed/serverless architecture specifically: cloud providers (his examples: SQS processing billions of messages daily, S3 handling 100 million requests per second) must architect for a scale most companies don't have, but adopting their services means inheriting their distributed, asynchronous programming model regardless of whether you need it at your actual scale.
- Coupling: the traditional case for loose coupling rests on change being hard to locate and hard to make; he argues tooling (source search, CI/CD, automated tests) has reduced both costs substantially, meaning tighter coupling is affordable in more cases than architectural convention assumes.
- His closing metaphor for organizational constraints: once a limitation is designed out of a system (his image: sweetener removing the sugar-calories link), you can't retroactively remove it from existing processes, you have to build the next version differently from scratch.
