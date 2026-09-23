---
url: "https://bartwullems.blogspot.com/2024/07/understanding-pure-domain-modelling.html?ref=dailydev"
captured_at: "2026-09-23T18:19:19+01:00"
title: "Understanding Pure Domain Modelling: Bridging the Gap Between Existing Systems and the Real Domain"
domain: "bartwullems.blogspot.com"
---
Understanding Pure Domain Modelling: Bridging the Gap Between Existing Systems and the Real Domain
July 01, 2024

Domain modelling plays a crucial role in the way that I design systems to reflect the business's needs and processes. However, I experienced there is often a disconnect between the idealistic view of domain modelling and the practical reality faced by domain experts. One key issue is that domain experts tend to start from their existing systems rather than describing the 'real' domain.




In this post I want to talk about pure domain modelling as a way to overcome the bias that domain experts have when explaining their needs.

The domain expert bias

When domain experts contribute to domain modelling, they frequently start from the perspective of the existing systems they are familiar with. These systems, whether they are legacy products, databases, or other technological solutions, shape their understanding and descriptions of the domain. While this approach has its advantages, it also introduces several challenges:

Bias Towards Existing Systems: Domain experts may describe the domain in terms of how it is implemented in the current system rather than how it truly operates. This can lead to models that are overly constrained by the limitations and design choices of existing systems.
Overlooked Business Rules: Important business rules and processes that are not well-represented in existing systems may be overlooked. Domain experts might inadvertently omit details that are crucial for a comprehensive domain model.
Resistance to Change: There can be resistance to adopting new models that deviate significantly from existing systems. Domain experts may be more comfortable with familiar structures and processes, even if they are suboptimal.

Remark: It is important to understand that these challenges exist when talking to domain experts. I've spend a full workshop with business creating a domain modelling where at the end I discovered we just had modelled the existing system and didn't capture the real business needs.

Users don't describe requirements, they describe workarounds. – Udi Dahan

What is Pure Domain Modelling?

Pure domain modelling refers to the process of creating a conceptual model of the domain that is as close to reality as possible. It involves understanding the core business processes, rules, and entities without being influenced by existing systems or technologies. The goal is to capture the essence of the domain in a way that is both accurate and understandable.

To create effective domain models, it is essential to bridge the gap between the practical reality of existing systems and the ideal of pure domain modelling. Here are some strategies to achieve this:

Educate and Collaborate: Educate domain experts about the principles of pure domain modelling and the importance of capturing the true essence of the domain. Encourage collaboration between domain experts and developers to ensure a shared understanding of the domain's core aspects.
Use Interviews and Workshops: Conduct interviews and workshops that focus on understanding the business processes and rules independently of existing systems. Ask domain experts to describe the domain as if no systems were in place, highlighting the 'why' behind each process and rule.
Identify and Document Assumptions: Identify and document assumptions made based on existing systems. Challenge these assumptions and explore alternative ways to represent the domain. This can help uncover hidden aspects of the domain that are not well-represented in current systems.
Incremental Modelling: Adopt an incremental approach to domain modelling. Start with high-level concepts and progressively refine the model by incorporating more details. This allows domain experts to gradually transition from system-based thinking to a more domain-centric perspective.
Leverage Domain-Driven Design (DDD) Practices: Utilize Domain-Driven Design (DDD) practices to facilitate the creation of pure domain models. Techniques such as Event Storming and the use of ubiquitous language can help align the model with the true nature of the domain.
Take away

The tendency of domain experts to start from existing systems rather than the 'real' domain can pose significant challenges. By recognizing this tendency and employing strategies to bridge the gap, it is possible to create domain models that are both realistic and beneficial. A key question I always ask during domain modelling workshops is:

What would you do if there was no system available?

SHARE
Labels
Architecture
Domain Driven Design
Software Development
LABELS: ARCHITECTURE  DOMAIN DRIVEN DESIGN  SOFTWARE DEVELOPMENT
SHARE
