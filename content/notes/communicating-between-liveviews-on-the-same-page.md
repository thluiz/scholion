---
title: "Communicating between LiveViews on the same page"
date: '2020-09-07T15:29:19-03:00'
category: webclip
summary: 'The post compares ways for multiple LiveViews on one page to communicate: via parent and child PIDs, sibling routing through a shared ancestor, or PubSub scoped by root PID or page ID.'
tags: ["elixir", "phoenix-liveview", "pubsub"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Communicating between LiveViews on the same page – The Pug Automatic"
    url: "https://thepugautomatic.com/2020/08/communicating-between-liveviews-on-the-same-page/?utm_source=elixir-radar&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/thepugautomatic-com--communicating-between-liveviews-on-the-same-page.md"
    kind: repo
---

The post lays out several ways to make LiveViews on the same page communicate. It first suggests checking whether multiple LiveViews are needed at all, since a single LiveView with components may fit better. When multiple LiveViews are used, the examples show message passing between parent and child, between siblings through a shared ancestor, and through PubSub when the LiveViews share a root or a page identifier.

## Reading notes

- A parent LiveView can pass session data to a child LiveView with `live_render`, but the data is only sent when the child mounts.
- Including an assign in the child ID makes the child remount when that value changes, but remounting resets the child’s state.
- A child LiveView can send a message to its parent because the socket exposes `parent_pid`; `root_pid` is also available for deeper nesting.
- To let a parent send to a child, the child can send its own PID to the parent during connected mount, and the parent can store it in assigns.
- If two sibling LiveViews share an ancestor, one child can send a payload to the ancestor, and the ancestor can forward it to the other child.
- PubSub can be used for communication across LiveViews on the same page when they share a root LiveView.
- The post uses `root_pid` in the PubSub topic so subscriptions are scoped to the current page.
- The sender can use `broadcast_from!/5` so it does not receive its own broadcast.
- A process registry is mentioned as an alternative, but the post warns against it because atom names are not garbage collected and it only works on the local node.
- If a user ID or session ID is used with PubSub, all tabs or windows for that user would be affected, not only one page.
- A unique page ID can be generated in the controller and passed into both LiveViews so PubSub targets only the current page.
