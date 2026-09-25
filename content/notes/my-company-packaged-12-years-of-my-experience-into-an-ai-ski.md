---
title: "My company packaged 12 years of my experience into an AI Skill, then laid me off. When it crashed, the CTO called at 5x my salary."
date: '2026-06-11T19:19:19+01:00'
category: webclip
summary: 'A first-person story about turning years of operational knowledge into an AI Skill, getting laid off, and being called back when the system failed on a newer Kafka setup the skill could not handle.'
tags: ["ai-skill", "knowledge-transfer", "kafka", "layoff"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My company packaged 12 years of my experience into an AI Skill, then laid me off. When it crashed, the CTO called at 5x my salary. - DEV Community"
    url: "https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-06/dev-to--my-company-packaged-12-years-of-my-experience-into-an-ai-ski.md"
    kind: repo
---

The story follows an engineer whose company spends three months extracting his operational knowledge into an AI Skill. The system performs well on historical incidents, the company treats that as enough, and he is laid off with severance.

When the AI Skill later fails on a Kafka-based incident, it applies an old RabbitMQ-era retry strategy and makes the outage worse. The former CTO calls him back, offers five times his old salary, and asks him to return on his terms.

## Reading notes

- The company frames the project as a knowledge transfer initiative, but the narrator reads it as turning his experience into a replacement.
- The AI Skill reproduces his reasoning on past incidents and is reported at 96.8% accuracy across 312 historical failure scenarios.
- After the validation meeting, his position is eliminated in a restructuring.
- He registers a consulting LLC and decides not to use AI in his delivery chain.
- The skill is deployed after his departure and takes over much of tier-2 operations work.
- A later migration to Kafka changes the infrastructure, but the Skill is not revalidated after the change.
- During the crash, it recommends the same 450 ms retry backoff that had been correct for an older RabbitMQ setup.
- The old timing creates poll delays, triggers a consumer-group rebalance, and worsens the outage.
- The CTO later calls him, references a note about the 450 ms RabbitMQ GC window, and asks him to come back.
- He asks for five times his old salary and sets the terms of the contract himself.
