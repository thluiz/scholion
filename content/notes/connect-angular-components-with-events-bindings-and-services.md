---
title: "Connect Angular Components with Events, Bindings, and Services"
date: '2026-11-16T07:55:16+00:00'
category: webclip
summary: 'The article shows how Angular components can share user input through two-way binding, a service, and an EventEmitter, so a command entry updates the story view without tight coupling.'
tags: ["angular", "eventemitter", "two-way-binding", "services"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Connect Angular Components with Events, Bindings, and Services - Kill All Defects"
    url: "https://web.archive.org/web/20200810163737id_/https://killalldefects.com/2020/02/08/connect-angular-components-with-events-services-and-binding/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--connect-angular-components-with-events-bindings-and-services.md"
    kind: repo
---

The article explains how to wire an Angular interface so a command entry component and a story view component can interact without being tightly coupled. It uses `ngModel` for two-way binding, a service to receive commands, and an `EventEmitter` so another component can subscribe to new entries and update the story view.

## Reading notes

- The project starts with a text-based game UI called Doggo Quest that already has a story view and a player input area, but the two parts do not communicate yet.
- The article uses Angular two-way binding, events, event emitters, services, and subscriptions to connect the interface.
- A service is added to link the command entry component to the main story display.
- Services are described as classes that provide functionality to other parts of the application and can be injected automatically into component constructors.
- The service is generated with Angular CLI using `ng g s <name-of-service>`.
- The service is expanded with an `EventEmitter` and a `handlePlayerInput` method.
- An `EventEmitter` can emit events that other code subscribes to, and it can have no subscribers or many subscribers.
- The command entry component receives the story service through dependency injection.
- The component’s `submitCommand` method reads the command field and passes the value to the service.
- After sending the command, the component clears the `Command` field.
- The template uses `(click)` to call `submitCommand` when the button is clicked.
- The template also uses `keyup.enter` so pressing Enter triggers the same method.
- In Angular templates, parentheses indicate events and brackets indicate binding.
- `[(ngModel)]="Command"` is presented as a combination of property binding and event binding for two-way binding.
- With two-way binding, user input updates the component field, and clearing the field in code updates the input box through change detection.
- The story view component also receives the story service through dependency injection.
- Instead of calling methods on the service, it subscribes to the `EntryAdded` `EventEmitter`.
- The story view component implements `OnInit` and `OnDestroy` so it can subscribe and unsubscribe in `ngOnInit` and `ngOnDestroy`.
- The subscription is stored so it can be released later.
- Unsubscribing is important to avoid errors and poor performance from dead components.
- When the `EntryAdded` event fires, the new entry is added to the story array and appears in the user interface through Angular binding and change detection.
- The result is a flexible connection between components, with the user’s text appearing in the story view along with a default response.
