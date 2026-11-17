---
title: "7 steps to ace your system design interview"
date: '2021-07-29T13:43:43+00:00'
category: webclip
summary: 'Oliver Jumpertz outlines an incremental 7‑step workflow for system design interviews, from clarifying requirements and defining APIs and data models to detailing components and explicitly discussing bottlenecks.'
tags: ["system-design", "software-architecture", "interviews"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread de @oliverjumpertz: I've been a software architect for most of my professional life, and system design has alw…"
    url: "https://x.com/oliverjumpertz/status/1420729273518903300"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-07/x-com--7-steps-system-design-interviews-jumpertz.md"
    kind: repo
---

Oliver Jumpertz, a software architect and tech lead, shares a structured, incremental workflow he personally uses for designing systems and recommends for system design interviews. He breaks the process into seven steps: clarifying requirements, defining system interfaces, estimating scale, defining the data model and data flow, drawing a high‑level design, detailing core components, and explicitly calling out bottlenecks and their trade‑offs.

He emphasizes asking many questions to pin down scope, making assumptions visible, and letting interviewers correct course. Throughout, he encourages visual diagrams (use case, class, component, and simple box‑and‑arrow sketches) and grounded estimates of scale to justify design choices. He also notes that system design knowledge is mandatory for senior roles and becomes more relevant as company size and architectural complexity grow.

## Reading notes

- Jumpertz presents a 7‑step approach he uses to design systems and recommends using the same process in system design interviews.
- He stresses that interviews are about helping interviewers understand the design through an incremental and organized workflow they can follow.
- **Step 1 – Clarify requirements:** ask many questions to discover what the interviewer expects and to narrow the exact scope, even when redesigning an existing system.
- Suggests example questions: presence of multiple frontends, regulatory requirements, whether to use own auth or third‑party, other API consumers, third‑party integrations, need for a data lake, and data consistency requirements.
- **Step 2 – Define system interfaces:** enumerate the APIs the system needs and explain the purpose of each so the interviewer can correct misunderstandings early.
- Uses Instagram as an example, listing APIs for uploading/viewing images, retrieving the feed, handling comments and likes, managing profiles and followers, and working with stories and reactions.
- Notes that existing systems are large, so it is reasonable to ask whether to cover everything or focus on a specific part of the system.
- Recommends a use case diagram as a way to identify and illustrate potentially needed APIs.
- **Step 3 – Estimate the scale of the system:** provide rough scale estimates and state them clearly so the interviewer can adjust them and better understand design decisions.
- Advises not to chase exact numbers but to propose reasonable ones, especially for well‑known platforms whose usage data can be researched before the interview.
- Mentions typical metrics: daily/monthly active users translated into expected API requests per second.
- Suggests that having approximate usage numbers for the company’s own products can impress interviewers and demonstrate preparation.
- Warns against being off by hundreds of millions of users, since that can push a design toward very different architectural choices.
- **Step 4 – Define the data model:** describe the entities and how data flows through the system, and check how much detail the interviewer wants.
- Recommends using relational data models where appropriate but also considering other models such as document and graph stores depending on the entity.
- Notes that graph models may fit friendship or follower relationships and should be modeled that way when suitable.
- Encourages explicitly describing how entities move between services, such as a feed service fetching user data from a user service.
- Points out that you do not need to reproduce the exact real‑world solution; instead, define just enough properties to satisfy the requirements.
- Provides an example of user properties that are typically needed: forename, name, ID, email address, and similar basic fields.
- Encourages asking the interviewer for hints if unsure about necessary properties, since guiding the candidate is part of their role.
- For visualizing entities, suggests UML class diagrams, simple property boxes, or property lists, and mentions simple diagrams to depict data flow for certain operations.
- **Step 5 – Draw a high‑level design:** identify a few crucial components that form the core of the system and draw about five key boxes showing how they interact.
- Notes that in microservice architectures services often communicate frequently, which can be shown with arrows between service boxes when one uses data managed by another.
- Suggests reusing previously modeled data flows to inform the high‑level architecture diagram.
- States that simple box‑and‑arrow diagrams with descriptions are sufficient to communicate the high‑level design.
- **Step 6 – Design components in detail:** ask whether to focus on specific components and, if not guided, pick the three most important to describe and visualize in depth.
- Uses an image service in an Instagram‑like system as an example, with an API to retrieve images implemented internally.
- Explains that the image service also needs a separate internal implementation for accessing storage to persist images.
- Advises laying out these internals with diagrams to help the interviewer understand component responsibilities and behavior.
- Mentions that a UML component diagram‑like representation can work well for detailed service views.
- **Step 7 – Explicitly state bottlenecks:** assert that every design has limits and candidates should clearly identify and explain them.
- Recommends explaining what factors stress each bottleneck and how one might mitigate or alleviate those constraints.
- Notes this step requires strong knowledge of the chosen components and the design principles applied in the system.
- Gives examples of needed knowledge: when relational databases underperform compared to NoSQL stores, and in which situations certain message brokers cease to be good choices.
- Raises the scenario where a relational model works at first but migration becomes painful at higher scale.
- Encourages creativity in discussing bottlenecks, while still grounding the discussion in known trade‑offs and component characteristics.
- Points out that interviewers may highlight bottlenecks they see, giving a chance to discuss and collaboratively find improvements.
- States that candidates do not need to list every downside of each component but should know and mention the most important drawbacks.
- Concludes the thread by inviting readers to like, retweet, and follow for more content if they found the advice useful.
- In replies, he states that system design is mandatory knowledge for any senior role.
- Adds that the larger the company, the more likely candidates will face system design topics, sometimes focused on app architecture and interfacing systems instead of whole‑system designs.
- Shares links to resources such as an O’Reilly software architecture patterns book and recorded interviews and videos as further learning materials.
- Emphasizes that learning system design takes more than one book and involves trying things out, seeing what works, and recognizing that there usually is no single correct approach for every system.
