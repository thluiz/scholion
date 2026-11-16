---
title: "Event Versioning Guidelines"
date: '2020-02-22T12:11:48+00:00'
category: webclip
summary: 'The post says event versioning should preserve backward compatibility when possible, use version numbers when needed, and treat non-compatible changes as new events. It also describes double publishing v1 and v2 in some cases.'
tags: ["event-versioning", "backward-compatibility", "semantic-versioning", "messaging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Event Versioning Guidelines"
    url: "https://codeopinion.com/event-versioning-guidelines"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/codeopinion-com--event-versioning-guidelines.md"
    kind: repo
---

The post outlines practical guidelines for versioning events in messaging systems. It says adding properties usually does not break consumers, but changing the contract requires a new event version and a breaking change.

## Reading notes

- Adding properties to an event usually does not create a versioning conflict for consumers.
- If events are stored, old events must be upcast to the new version.
- When the contract changes, a new version of the event is needed.
- A version number can be included in the event so consumers know how to handle it.
- Non-backward-compatible changes often mean a completely new event with a different name.
- It can be hard to tell whether the new event replaces the old business event or reflects a new understanding of the concept.
- One approach is to publish both v1 and v2 to the queue or event stream.
- With double publishing, consumers must process only one version and ignore the other.
- Double publishing is less suitable when replaying events from an event store, because processing both versions can have negative effects.
- When consumers are not replaying events, they can adopt the new version and later remove the old handler.
