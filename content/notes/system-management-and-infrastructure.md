---
title: "System Management and Infrastructure"
date: '2019-05-16T22:53:08+00:00'
category: webclip
summary: 'This section groups patterns for administering actors and messages, rerouting or inspecting messages, attaching metadata, tracking request-reply flows, testing messages, and purging channels.'
tags: ["actor-model", "message-patterns", "system-management", "infrastructure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "System Management and Infrastructure"
    url: "https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/system-management-and-infrastructure.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--system-management-and-infrastructure.md"
    kind: repo
---

This section groups patterns for system-level handling of actors and messages. It covers administration, rerouting, inspection without changing delivery, metadata and history, request tracking, message testing, and channel purging.

## Reading notes

- Control Bus allows you to administer and control actors and messages.
- Detour reroutes messages so extra steps can run before delivery to the target actor.
- Wire Tap inspects messages without changing their content or destination.
- Message Metadata/History adds metadata and history to messages for tracking.
- Message Journal/Store records delivered messages in a permanent location.
- Smart Proxy tracks messages that use the Return Address pattern by keeping requesters and relaying replies.
- Test Message checks the health of an actor by distinguishing test messages from production messages.
- Channel Purger removes messages from an actor or Message Store.
