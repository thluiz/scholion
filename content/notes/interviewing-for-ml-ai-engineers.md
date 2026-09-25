---
title: "Interviewing for ML/AI Engineers"
date: '2025-12-25T19:15:04-03:00'
category: webclip
summary: 'The essay argues that ML engineer interviews should mix coding, data modeling, system design, project deep dives, and career chats, while limiting ML system design interviews because they often produce low signal.'
tags: ["machine-learning", "software-engineering", "interviews", "strategy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Interviewing for ML/AI Engineers"
    url: "https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-12/moderndescartes-com--interviewing-for-ml-ai-engineers.md"
    kind: repo
---

The essay rethinks the ML engineer interview loop after the author’s recent ML/AI job search. It defines ML engineering as software engineering plus the ability to reason about statistical and distributional properties of data, then separates the role into concrete SWE and ML skillsets.

It compares interview formats and argues that coding, data modeling, project deep dives, and standard system design usually give more signal than ML system design. The preferred loop varies by level, with ML system design reserved for Staff+ candidates and only when the interviewer can ask pointed, scenario-specific questions.

## Reading notes

- An ML engineer needs both software engineering ability and the ability to reason about data distribution and statistics.
- The author says some companies label regular software engineering roles as ML engineering.
- Relevant SWE skills include maintainable code, algorithms and data structures, distributed systems, and production debugging.
- Relevant ML skills include ML code, ML methods, exploratory data analysis, and monitoring for schema drift and data drift.
- Coding interviews should focus on problems that resemble real work, especially indexing, search, graph, tree, and heap problems.
- Data modeling interviews should use a live dataset or task, with bugs, class imbalance, architecture changes, or training changes to debug and improve performance.
- Math quizzes can help, but they should not dominate an interview because they have high false negative rates.
- System design interviews work better when they include concrete numbers and equations.
- ML system design should test product context, user experience, dataset availability, modeling likelihood, metrics, and production monitoring.
- Project deep dives can reveal seniority, communication skills, and motivation, and should be collaborative rather than skeptical.
- Career chats can show ambition, growth potential, and fit with the company’s work style.
- The author recommends different interview loops for junior, senior, and Staff+ candidates.
- Many ML system design interviews fail because they are really vanilla system design with ML words added.
- Other failure modes include vague prompts, outdated problems, and questions that require rederiving known algorithms from scratch.
- The author argues that many ML system design interviews would be better replaced by data modeling, system design, or project deep dive interviews.
