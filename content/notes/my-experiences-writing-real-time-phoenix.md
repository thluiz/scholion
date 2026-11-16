---
title: "My Experiences Writing Real-Time Phoenix"
date: '2020-07-05T14:11:16+00:00'
category: webclip
summary: 'The author recounts why he wrote Real-Time Phoenix, how the proposal and publishing process worked, the chapter structure he used, and the burnout, refactoring, and release stages of writing the book.'
tags: ["writing", "elixir", "phoenix", "technical-books"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My Experiences Writing Real-Time Phoenix"
    url: "https://stephenbussey.com/2020/05/06/my-experiences-writing-real-time-phoenix.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/stephenbussey-com--my-experiences-writing-real-time-phoenix.md"
    kind: repo
---

The author says the book grew out of real-time app work at SalesLoft, where he learned hard lessons about rollout, scalability, and Elixir. He then describes pitching publishers, revising the proposal with Bruce Tate’s advice, and writing the chapters with Pragmatic’s editorial process.

He also explains the book’s chapter formula, the difficulty of sustaining momentum across a long project, the pressure of always feeling he should be writing, and the value of refactoring chapters and removing content. The post closes with the book’s beta and final release, acknowledgments, and a short update on what he plans to do next.

## Reading notes

- The book began after work on extracting a live feed feature from the SalesLoft Rails monolith exposed gaps in his understanding of real-time app development.
- He thought the book could be finished in three weeks, but the actual process was much longer and more demanding.
- He first tried Pragmatic Bookshelf and then Manning Publications, and Manning asked for a formal proposal.
- Bruce Tate advised him to focus on what the technology enables rather than on WebSocket technology itself.
- The formal proposal for Pragmatic included a substantial sample chapter and was accepted.
- The first weeks involved Pragmatic’s build system, style guide, editor introduction, and early chapter outlines.
- Each chapter started from a two-level outline, then followed a repeated structure of introduction, several substantive sections, and a closing section that prepared the reader for the next chapter.
- Editorial review produced many comments at first, and the number of comments and review rounds later decreased as the writing improved.
- Part 2 became harder because the example project continued across the rest of the book, making continuity difficult and slowing his pace.
- ElixirConf 2019 gave him a deadline and helped him reach the beta release.
- He describes a persistent feeling that he should be writing whenever he was not, which he presents as the hardest part of the process.
- Chapter 3, 4, and 5 were originally one large chapter and had to be split apart through refactoring and transition rewriting.
- He values removing content when it makes the material simpler and more direct.
- The book had a beta release in August 2019 and a final release in April.
- He thanks technical reviewers, the Phoenix community, and Chris McCord and other maintainers.
- He says he does not plan to write another book soon and wants to return to greenfield software and future talks.
