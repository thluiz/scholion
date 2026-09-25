---
url: "https://journal.optivem.com/p/manifesto-for-deadline-driven-development?isFreemail=true&post_id=178413172&publication_id=824051&r=s05z9&triedRedirect=true"
captured_at: "2025-11-11T12:42:13+00:00"
title: "Manifesto for Deadline Driven Development"
domain: "journal-optivem-com"
---

---
**Manifesto for Deadline Driven Development**

We are uncovering bitter ways of developing  
software by doing lots of overtime and helping others do it.  
Through this work we have come to value:

**Being on budget** over optimizing return on investment  
**Being on scope** over quality of code  
**Being on schedule** over delivering the right product  
**Being busy** over investing time for improvements

That is, while there is value in the items on  
the right, we value the items on the left more.

—Source: Unknown

Unfortunately, this is still too common in fake Agile development.

## You Can’t Be Agile Without Technical Practices

Agile isn’t just about daily stand-ups, story points, or hitting deadlines. Without strong technical practices, it becomes **fake Agile** — a sprint-to-sprint survival game.

Consider these realities:

-   **No TDD or automated tests** → every code change is a risk. Bugs slip into production, releases become slow and stressful, and the team spends more time firefighting than delivering value.
    
-   **Messy, unmaintainable code** → without clean code principles, adding new features takes exponentially longer. Refactoring becomes a nightmare, slowing down every iteration.
    
-   **Skipping continuous integration** → you can’t safely ship small, incremental changes. Releases are big, risky, and infrequent, which contradicts Agile’s goal of rapid feedback.
    

Agile promises fast feedback, adaptability, and incremental delivery.

But without tests, clean code, refactoring, and CI/CD, you lose the safety net that makes those promises possible.

In short: no tests, no quality, no real agility. You can run sprints, but you’re running blind.

[

![](https://substackcdn.com/image/fetch/$s_!zQKD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2efbd5c-f295-46cd-a8ab-9865dc1b1fe0_800x600.jpeg)

](https://substackcdn.com/image/fetch/$s_!zQKD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2efbd5c-f295-46cd-a8ab-9865dc1b1fe0_800x600.jpeg)

_Source: Unknown_

Well, you may “appear” to be agile without TDD or tests during the first 3-6 sprints. You’re hitting deadlines, stories are done, and the team feels productive.

But soon after, cracks start to show:

-   Adding new features takes longer because you’re afraid of breaking existing functionality.
    
-   Bugs creep into production, slowing down releases and users are getting frustrated.
    
-   Refactoring becomes risky, so code quality degrades over time.
    

**Without TDD** you don’t have the confidence to change code, refactor, and deliver continuously without fear. Quality degrades as regression bugs accumulate.

**Without** **ATDD** you risk building a system that fails to satisfy business requirements, whereby there's misalignment between developers and QA regarding requirements, causing expensive rework. Furthermore, without ATDD, your team is most likely having to resort to manual QA regression testing, leading to delivery delays and regression bugs escaping to production.

ATDD means that, given some requirements, we convert requirements (acceptance criteria) into executable requirements (acceptance tests), before we start coding. After coding is done, the acceptance tests help verify whether the system behaves as expected (whether acceptance criteria is satisfied).

ATDD enables the whole team to reach alignment regarding requirements, before development starts. Furthermore, acceptance tests simultaneously serve as regression tests. Developers then work under less stress and avoid overtime.

🚀 Join the **[ATDD Accelerator waitlist](https://atdd.optivem.com/)**

[Leave a comment](https://journal.optivem.com/p/manifesto-for-deadline-driven-development/comments)
