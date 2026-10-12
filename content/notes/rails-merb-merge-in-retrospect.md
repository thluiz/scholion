---
title: "The Rails/Merb Merge In Retrospect"
date: '2014-07-07T14:31:20-03:00'
category: webclip
summary: 'The post argues that the Rails/Merb merge delivered limited practical modularity, took too long, and left Rails behind newer web development needs while community pressure and design choices pulled in different directions.'
tags: ["rails", "merb", "open-source", "modularity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Giles Bowkett: The Rails/Merb Merge In Retrospect"
    url: "http://gilesbowkett.blogspot.fr/2014/06/the-railsmerb-merge-in-retrospect.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/gilesbowkett-blogspot-fr--rails-merb-merge-in-retrospect.md"
    kind: repo
---

The post argues that the Rails/Merb merge did not deliver much useful modularity to most Rails developers. Although Rails became somewhat more modular and some tasks got easier, the change was slow, hard to use, and largely unused by the wider community.

It also says Rails kept a strong original design focus on business logic and page flow, but that focus fit web development less well as APIs, client-side logic, and new frameworks became more important. The post treats this as a tradeoff between preserving a clear vision and responding to changing community needs.

## Reading notes

- The post frames the Rails/Merb merge as a historical and technical failure to give most developers modularity they could actually use.
- It says the merge improved some things, like the site generator and swapping out ActiveRecord, but did not change daily Rails practice much.
- It argues that exploiting Rails modularity well requires deep knowledge of Rails internals, which most developers do not have.
- It contrasts official Rails modularity with the more common habit of splitting apps into services and smaller files.
- It says Rails originally narrowed the programmer’s concerns to business logic and page flow, which helped productivity.
- It argues that newer web development added client-side logic, mobile concerns, and JavaScript integration, making that original model less complete.
- It presents the Rails/Merb merge as a choice that favored a more arcane form of modularity over the kinds of modularity developers were already trying to use.
- It says Rails developers often built unofficial modular practices despite opposition from Rails leadership.
- It connects the issue to a broader tension in open source between a strong guiding vision and listening to the community.
- It suggests that Rails may have said no too often, but also that many people tried to use Rails for unsuitable purposes.
