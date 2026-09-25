---
title: "Goodhart's Law in Software Engineering"
date: '2026-09-24T23:07:08+01:00'
category: webclip
summary: 'The text defends the strong version of Goodhart''s law: when a metric becomes a target, it starts to drift away from the value it was meant to represent. In engineering, this appears in test coverage, complexity, benchmarks, and productivity metrics.'
tags: ["goodhart","software-engineering","metrics"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Goodhart's Law in Software Engineering"
    url: "https://buttondown.com/hillelwayne/archive/goodharts-law-in-software-engineering/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/buttondown-com--goodharts-law-in-software-engineering.md"
    kind: repo
---

The text argues that metrics are approximations of values that cannot be measured directly. When the metric starts to guide action, the focus shifts from the goal to the indicator, and this can worsen the result one wanted to achieve. The author treats this dynamic as a central part of Goodhart's law.

He applies this idea to software engineering examples, such as test coverage, cyclomatic complexity, function size, benchmarks, and time spent in pair programming, review, and debugging. He also mentions the DORA report as a case of metrics used as proxies for more diffuse goals, and concludes that the practical way out is to use engineering judgment, even if that is not a scalable guideline.

## Reading notes

- The weak version of the law talks about incentives to manipulate metrics; the strong version says that pursuing a metric honestly can also move you away from the real objective.
- Metrics exist because what really matters is often non-quantifiable, so they function as imperfect approximations of the desired value.
- In the example of software reliability, the number of bugs in the tracker only approximately measures reliability, and fixing bugs can even reduce reliability without changing the bug record.
- Sexual selection is presented as an example of Goodhart in action: more conspicuous plumage starts as a proxy for fitness and becomes the target itself over generations.
- In engineering, test coverage, cyclomatic complexity, function size, and benchmarks are useful proxies, but they can diverge from the objective when other aspects of the system start to matter more.
- The time spent in pairing, code review, and debugging also appears as a proxy for productivity.
- The DORA report is described as a case where metrics function as proxies for goals such as elite performance and employee satisfaction, while also encouraging smaller commit sizes to improve proxy metrics.
- Combining metrics can help reveal tensions between objectives, but it can also become another target subject to the same distortion.
- The practical solution proposed is to use the best engineering judgment, because Goodhart's law can affect any metric used as a target.
