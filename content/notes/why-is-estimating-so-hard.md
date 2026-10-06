---
title: "Why is Estimating so Hard?"
date: '2012-05-02T11:57:33-03:00'
category: webclip
summary: 'The post argues that estimates fail when people confuse how easy a task feels to do by hand with how hard it is to write the procedure. Human judgment hides procedural complexity.'
tags: ["estimation", "procedures", "software-craftsmanship", "professionalism"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why is Estimating so Hard? | 8th Light"
    url: "http://blog.8thlight.com/uncle-bob/2012/04/20/Why-Is-Estimating-So-Hard.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/blog-8thlight-com--why-is-estimating-so-hard.md"
    kind: repo
---

The post says estimating goes wrong when people judge a job by how easy it seems to do manually. In the example of breaking text into 13-character lines, a person can do the task in minutes, but turning that ability into a program requires writing a procedure, and that is much harder.

It argues that manual work and procedural work are different. Humans keep checking the output and adjusting until it looks right, while a procedure must already contain the rules that make the output correct. The post recommends estimating by identifying the procedural elements in the task, since even simple-looking work can hide several cases and decisions.

## Reading notes

- Estimating text wrapping by hand is easy because a person can keep adjusting the result while working.
- Writing the program is harder because the procedure must be explicit and cannot rely on intuition.
- The post says many estimates are wrong because they measure the wrong thing.
- It suggests breaking a task into procedural cases before estimating it.
- It uses tying shoes as an example of a simple task with hidden procedure.
