---
title: "What I Learned About C# From Job Interviews"
date: '2021-02-24T08:13:46-03:00'
category: webclip
summary: 'The post explains which C# features help in coding interviews, from multidimensional arrays and tuples to bitwise operators, string and array helpers, plus practical interview habits.'
tags: ["csharp", "coding-interviews", "algorithms", "job-interviews"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What I Learned About C# From Job Interviews - Michael's Coding Spot"
    url: "https://michaelscodingspot.com/what-i-learned-about-c-from-job-interviews/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/michaelscodingspot-com--what-i-learned-about-c-from-job-interviews.md"
    kind: repo
---

The post says coding interviews pushed the author to use C# features that are less common in day-to-day work but useful for algorithm problems. It focuses on multidimensional arrays, tuples, binary operators, and a few string and array methods, then adds interview habits that helped in practice.

## Reading notes

- Multidimensional arrays are useful in coding exercises, especially for 2D or 3D problems such as a maze or a cube, and they are different from jagged arrays.
- Tuples are presented as a compact alternative to classes when returning small groups of values in interview code.
- Bitwise operators such as `<<`, `>>`, `&`, and `|` can help with permutation-style problems, including generating all combinations of items.
- `string.Join`, `Array.Sort` with a `Comparison<T>`, and `Array.Copy` are highlighted as practical helpers for interview problems.
- Python solutions are described as shorter and often cleaner than C# solutions for algorithm questions.
- Preparation matters, and the author recommends practicing on LeetCode, starting with easy problems, spending more time on medium ones, and reviewing other submissions.
- Most interview questions, in the author’s experience, are medium-level and often involve DFS, BFS, binary trees, or heaps.
- Before writing code, it helps to think through the solution, explain it out loud, and check whether it can be simpler or more optimal.
- Short variable and method names are recommended for interview settings.
- The post closes by saying big-company interviews also include system design and behavioral questions, and the author says he is starting a new position at Microsoft.
