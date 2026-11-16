---
title: "Revolutionary Evolution"
date: '2020-08-26T19:31:19+00:00'
category: webclip
summary: 'The article argues that changing a team’s coding habits requires building a coalition, not acting alone. The author describes mentoring junior engineers, running weekly lectures, and using code reviews to shift a 30-person Java team.'
tags: ["software-architecture", "team-dynamics", "mentoring", "oop"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Revolutionary Evolution"
    url: "https://yegor256.com/2019/11/05/revolutionary-evolution.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--revolutionary-evolution.md"
    kind: repo
---

The article says that a lone developer cannot change a team’s habits by force. A better path is to gather support, mentor the people most open to learning, and create a sub-team that starts moving the codebase and the discussion in a different direction.

## Reading notes

- A radical rewrite or direct attack on the team’s preferred stack would likely be rejected and could risk the developer’s job.
- Most people follow the community around them, so changing practice requires social support, not just technical arguments.
- The author chose the youngest and most receptive engineers, not the most senior ones.
- He became an unofficial mentor and used code reviews, blog posts, and books to explain design ideas.
- He organized weekly lectures for the whole team about topics like NULL and unit tests.
- He refactored critical parts of the codebase and asked the group to review the pull requests.
- The goal was to build a coalition of supporters, not to fix the architecture immediately.
- A small gang of seven was enough to shift the direction of a team of thirty.
- When he left the project, the codebase was moving toward more immutable objects, more test coverage, and fewer new DTOs.
