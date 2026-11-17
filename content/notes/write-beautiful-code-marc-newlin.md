---
title: "Write beautiful code"
date: '2015-06-02T14:17:11-03:00'
category: webclip
summary: 'Essay arguing that beautiful code is clear, simple, and readable: favor comments and whitespace, keep naming consistent, reuse good libraries, and write for beginners.'
tags: ["software-engineering", "code-style", "readability"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Making software is way fun.: Write beautiful code"
    url: "http://www.marcnewlin.me/2015/06/write-beautiful-code.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/marcnewlin-me--write-beautiful-code-marc-newlin.md"
    kind: repo
---

The text presents software development as an art form where each line of code shows both technical understanding and the ability to communicate with other engineers. It criticizes rigid style absolutes and stresses that context matters, contrasting quick hobby prototypes with foundational team code. Beyond functional and performance requirements, the author urges engineers to write code that can be easily understood later, including by their future selves.

The author challenges myths about code style. He argues that comments and whitespace are valuable because people process natural language more easily than dense code, and that consistent naming matters more than any specific convention. He also encourages using well‑licensed third‑party libraries instead of re‑implementing existing solutions. The core guidance is to write code simple enough for a freshman CS student to follow, keeping it minimal, well commented, and free of ego.

## Reading notes

- Writing code is framed as more than engineering, described as an art where each line reflects language mastery, communication skills, and experience from previous projects.
- There is said to be no single correct code style or engineering solution, and style guides written in absolutes are seen as context‑blind.
- The text contrasts a quick proof of concept for a hobby project with a base class used by an entire team to show how project context should influence style decisions.
- Meeting functional and performance requirements is labeled the first priority, but the author stresses that readability for other programmers, including one’s future self, is also crucial.
- The author evokes the common experience of revisiting six‑month‑old code and not understanding how it works, suggesting this is avoidable through better writing.
- Myth #1 claims verbose comments make you a bad programmer; the author disputes this and mocks the idea that code should be fully understandable without comments.
- The text asserts that humans process natural language better than code, so a few sentences in a native language are often easier to grasp than an unfamiliar function.
- Two versions of a function are presented, one dense and one with comments and line breaks, to illustrate how uncommented code takes much longer to understand.
- Comments are compared to cram notes before an exam, especially as projects grow in size and complexity.
- The profession is described as valuing efficiency, and from that perspective the advice is to comment early and frequently.
- Obfuscated or difficult code is acknowledged as looking cool in competitions, but the author argues production code must serve every future engineer who reads it.
- The phrase “Don’t be a dick. Comment your code.” is used to emphasize the social responsibility toward future maintainers.
- Myth #2 argues against the idea that whitespace is bad and that minimizing blank lines or shrinking code visually is inherently better.
- The article jokingly compares whitespace‑free code to classical Greek and Latin written in all caps without spaces to highlight how hard such text is to parse.
- Myth #3 addresses naming conventions, depicting the conflict between PascalCase, camelCase, underscore_case, and similar styles as a pointless war.
- The only thing the author treats as important in naming is consistency, not which particular style wins.
- When working on an existing project, the advice is to follow the conventions already in place rather than imposing a different style.
- For new projects, the recommendation is to choose naming conventions in advance and then stick to them.
- For languages with style guides, the article suggests following the defined naming rules, partly to accommodate future hires familiar with those conventions.
- A hypothetical scenario describes a future C# veteran using camelCase and disrupting underscore_case naming to show how ignoring common conventions can cause frustration.
- Myth #4 concerns the belief that using third‑party libraries is bad; the author notes that engineers enjoy building things and may resist external code.
- The author describes the personal satisfaction of implementing a complex algorithm from scratch and feeling accomplished after doing “hard things.”
- He then admits that in many cases a quick search would reveal an MIT or BSD licensed library that already solves the problem, often more completely.
- The guidance is to use existing code when licensing fits the project, rather than re‑implementing features purely for ownership or pride.
- Time spent re‑implementing a known solution is portrayed as time that could have been used to build something new or original.
- The author jokes about readers getting bored and returning to sites like Reddit, Hacker News, or Slashdot if the ranting continued.
- The main takeaway is to write code so that a freshman computer science student can read it, favoring simplicity and avoiding unnecessary complexity.
- The author advocates leaving ego aside, writing as little code as possible, ensuring it is well commented, and becoming more productive as a result.
- The closing message is an exhortation to write beautiful code understood as clear, simple, and considerate of future readers.
