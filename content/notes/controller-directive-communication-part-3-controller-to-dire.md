---
title: "Controller-Directive Communication Part 3: Controller to Directive"
date: '2015-09-04T10:09:49-03:00'
category: webclip
summary: 'The post argues for letting a controller notify a directive through an explicit observer pattern, instead of events, services, or scope hacking, to keep the flow clear and robust.'
tags: ["angular", "observer-pattern", "controller-directive"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Controller-Directive Communication Part 3: Controller to Directive - The Code Dump"
    url: "http://www.codelord.net/2015/09/02/controller-directive-communication-part-3-controller-to-directive"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-09/codelord-net--controller-directive-communication-part-3-controller-to-dire.md"
    kind: repo
---

The post closes a three-part Angular series by focusing on the case where a controller needs to tell a directive to act, such as scrolling a chat list to the bottom. It rejects events, services, and scope mangling as less clear or less appropriate for this kind of local communication.

## Reading notes

- The controller sometimes needs to tell the chat list directive to scroll to the bottom, for example when the user marked the chat as read from another device.
- Events work, but the post says they make component dependencies harder to find and worsen code quality.
- Services are described as better for global app-wide concerns, not for communication between two instances on screen.
- Scope mangling is presented as an abuse of bindings, because the directive adds functions onto an object passed from the controller.
- The preferred approach is an observer pattern with some boilerplate, so the controller manages handlers and notifies them when needed.
- In the example, the controller stores directive handlers and calls them when it needs to notify the directive.
- The directive receives a bound function used as a registration hook for change notifications.
- This approach is described as clearer and more robust, because the flow is explicit and failures happen at useful points.
- The note at the end warns that functions passed this way should be cleared when the bound scope is destroyed to avoid memory leaks and undefined behavior.
