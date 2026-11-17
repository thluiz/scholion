---
title: "Accepting incorrectness"
date: '2026-11-17T13:43:42+00:00'
category: webclip
summary: 'Argues that bugs in production are inevitable and less harmful than a culture that tolerates noisy, unfixed issues, and proposes treating noise itself as the real quality bug.'
tags: ["software-quality", "production-operations", "engineering-culture", "observability"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Accepting incorrectness"
    url: "https://devonestes.com/accepting-incorrectness"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--accepting-incorrectness-software-quality-noise.md"
    kind: repo
---

The text challenges the idea of a strict tradeoff between speed and correctness in software delivery, arguing that all non‑trivial systems are already incorrect and will always ship with unknown bugs. The core question shifts from preventing every production fault to how quickly a team can see and reverse mistakes, with strong observability and fast rollbacks enabling safe, rapid iteration.

It then distinguishes unavoidable production bugs from the deeper cultural problem of tolerating noisy, low‑impact defects that linger. Accumulated ignored alerts, misleading UIs, and dead code erode signal, normalize broken systems, and teach newcomers that keeping things running well is not valued. The proposed rule is that "noise is the real bug": alerts must be fixed or conclusively silenced, misleading UI and data should be corrected or removed, and teams should resist relying on inaccurate metrics. A culture that rejects noise and embraces ownership of operational health is presented as a prerequisite for effective product work.

## Reading notes

- The common framing of software quality as a spectrum between speed and correctness is questioned, especially as AI accelerates development.
- The author claims production systems are always already incorrect and contain long‑lived, undiscovered bugs.
- Shipping something with defects is described as a normal consequence of building sizable software, not automatic evidence of a low quality bar.
- Since some faults inevitably reach production without extreme measures like formal verification, the key issue becomes how teams respond when failure occurs.
- Two priorities are highlighted: the ability to quickly detect problems in production and the ability to quickly fix or roll them back.
- Effective detection involves actionable error tracking, meaningful alerts that reach humans for important failures, and observability sufficient to answer when an issue started without resorting to git bisect.
- Fast recovery relies on small deploys, rapid rollbacks, and feature flags for risky changes so reversing mistakes is quick and minimally disruptive.
- With strong detection and rollback, moving fast and being occasionally wrong is framed as a good, often optimal, strategy to validate whether work is correct by exposing it to users.
- The author argues the true quality problem is not individual bugs reaching production but persistent, noisy issues that everyone learns to ignore.
- Examples of this noise include high‑volume errors left unresolved, log lines the team habitually disregards, nonfunctional admin UI controls, stale displayed values, and mysterious modules nobody dares delete.
- These issues are distinguished from classic bugs because they linger without being addressed, reflecting a cultural tolerance rather than a one‑off failure.
- The text states that tolerating ongoing defects in production signals that the team has stopped caring, and that this quiet shift is the real quality failure.
- Low‑impact but constant defects consume attention and time, drawing focus away from more meaningful work.
- Accumulated noise undermines signal: an error tracker full of open issues cannot easily highlight genuinely new problems.
- Alerts that trigger daily train people to dismiss them, turning broken dashboards into the perceived normal state.
- When brokenness feels normal, teams lose the safety net that had justified moving quickly in the first place.
- The operational state of tools like Sentry during onboarding influences cultural expectations, showing newcomers whether running systems well truly matters.
- A backlog of ignored issues communicates a low bar for operational care, which new engineers are likely to adopt.
- The article warns that aiming for zero production faults in most domains is unrealistic and leads to wasting time chasing diminishing returns.
- The proposed guiding rule is that noise should be treated as the real bug in a system.
- For alerts, the team should either fix the underlying issue or silence the alert permanently, and only silence it when confident it cannot indicate a real production problem.
- If a UI presents incorrect information, the options are to correct the behavior or remove the misleading element entirely.
- Wrong data is described as worse than no data, since ongoing support overhead for known, unfixed issues accumulates unhelpfully.
- Skepticism is expressed toward “data‑driven management” when the underlying data is often inaccurate.
- The author prefers acknowledging a lack of correct data over justifying decisions with flawed metrics.
- Counting production faults is criticized as a poor primary metric for software quality, alongside concerns about other hard‑to‑measure qualities such as readability or scalability.
- The text concludes that a cultural stance against operational noise, combined with ownership and accountability for system health, significantly improves team outcomes.
- This cultural foundation is described as almost a prerequisite for teams to tackle real product work effectively.
