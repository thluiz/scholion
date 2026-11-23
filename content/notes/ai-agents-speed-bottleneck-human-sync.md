---
title: "Agents are here to stay, how can companies really go faster ?"
date: '2026-11-23T18:51:54+00:00'
category: webclip
summary: 'AI agents greatly accelerate execution, but team speed is capped by human sync costs, which grow with company size, making small autonomous teams and product engineers more effective.'
tags: ["ai-agents", "team-productivity", "human-sync", "product-engineering"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Agents are here to stay, how can companies really go faster ?"
    url: "https://www.clemsau.com/posts/agents-are-here-to-stay-what-does-that-means-for-tech-companies/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/clemsau-com--ai-agents-speed-bottleneck-human-sync.md"
    kind: repo
---

The text argues that AI agents already provide a large speedup across many tasks, from coding to planning and debugging. Despite this, the main speed bottleneck in companies remains human synchronization. As organizations grow, the time spent on alignment, meetings, and reviews dominates, so accelerating execution with agents only shifts the proportion further toward sync work. The author uses Amdahl’s law and Brooks’s law to show how communication overhead and quadratic growth of communication channels limit overall speedups, especially in larger teams. The conclusion is that smaller, more autonomous teams and product engineers who own the full product cycle are better positioned to capture the benefits of agentic workflows without sacrificing quality.

## Reading notes

- The author observes recurring skepticism online about AI agents’ ability to handle coding, planning, debugging, and presenting.
- In contrast to naysayers, the author states that AI delivers a dramatic speed increase for almost all kinds of work.
- This acceleration exposes human synchronization as the primary speed bottleneck, particularly in larger companies.
- As company size grows, the network of people needing alignment expands, increasing overhead for communication and coordination.
- Agentic coding and workflows speed up many tasks, but the dominant bottleneck of sync remains and can become more severe.
- The author notes that if sync previously consumed half of the time, it could rise to around 90% once execution is heavily accelerated by agents.
- The cost that grows in this context is communication, not raw execution capacity.
- Amdahl’s law is cited to frame how overall speed is capped by the proportion of time spent in the bottlenecked part of the process.
- In typical teams, meetings, reviews, and alignment likely make up the non-accelerated portion that constrains total velocity.
- Example: if execution takes 80% of a sprint and sync 20%, then reducing execution time nearly to zero still limits total speedup to around 5x, since 20% remains.
- Another example: when sync is already 50% of time, making execution 10x faster only reduces total time from 1.0 to 0.55, which is about a 1.8x speedup.
- In that second scenario, sync grows to roughly 91% of the remaining work after execution is sped up.
- Under these conditions, the theoretical maximum speedup is only about 2x, regardless of how fast agents become.
- Brooks’s law is introduced to explain why the problem worsens with company growth.
- Communication channels increase with team size according to n(n-1)/2, creating many more paths as people are added.
- The author illustrates this with numbers: 5 people correspond to 10 channels, 10 people to 45, and 50 people to 1,225 channels.
- Agents raise the amount of output each person can produce but do not directly improve people’s ability to align with others.
- More output per person implies more artifacts and decisions that require synchronization, intensifying the burden from the quadratic growth of communication channels.
- After using these laws as illustrations, the author emphasizes that smaller companies or small teams retain an advantage in speed.
- Environments where individuals work more autonomously and let agents iterate independently reduce the cap imposed by sync overhead.
- In such settings, the full benefits of agentic workflows are easier to realize because less time is trapped in coordination.
- The author argues that adopting this model does not necessarily degrade product quality, code quality, architecture, or security.
- The text highlights the rise of the Product Engineer role, a software engineer responsible for the entire product cycle.
- Responsibilities for this role include deciding what to build, designing the user experience, writing the code, and measuring user impact.
- Product Engineers may also take part in defining the broader direction of the product.
- The author suggests that this type of end-to-end ownership role is likely to become common as agentic workflows spread.
