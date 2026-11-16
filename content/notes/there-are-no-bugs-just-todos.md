---
title: "There Are No Bugs, Just TODOs"
date: '2026-11-16T03:49:06+00:00'
category: webclip
summary: 'The essay argues that issue trackers should stay minimal, with single ownership, one ordered queue, simple states, and aggressive closing. It rejects absolute priority, ticket type, version, and severity fields as sources of confusion.'
tags: ["issue-tracking", "kanban", "project-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "There Are No Bugs, Just TODOs"
    url: "https://almad.blog/essays/no-bugs-just-todos"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/almad-blog--there-are-no-bugs-just-todos.md"
    kind: repo
---

The essay argues that issue trackers work best when they stay small and operational. A ticket should have a clear owner, belong to one ordered queue, move through a simple state flow, and be broken down when it spans more than one deployment. It also calls for a separate channel for internal support requests so the main tracker does not turn into a swamp.

## Reading notes

- Issue trackers are useful, but they should not replace understanding the underlying software delivery.
- A ticket needs to reach someone who can do the work, with triage handled reliably when ownership is unclear.
- Every team should have one ordered queue, and all incoming work should be prioritized against each other in one place.
- The simplest useful ticket states are Todo, Doing, and Done, with extra states added only when needed.
- A ticket should map to a single deployment, and larger work should be split into sub-tickets with the relationship recorded.
- Absolute priority fields create abuse; priority should be relative to other issues.
- Ticket type often creates unproductive debate, because the team should focus on resolving the expectation mismatch.
- Software version tracking makes sense for shipped libraries and on-premise packages, but not for continuously delivered SaaS.
- Severity often duplicates priority and depends on role and effort.
- The system should make it easy to close issues aggressively, or it will turn into an unmanageable ticket swamp.
- Questions for the development team need a separate system, because random messages and badly specified tickets overload the queue.
