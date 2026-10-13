---
title: "SOLID: Part 1 – The Single Responsibility Principle"
date: '2013-12-17T14:57:05-03:00'
category: webclip
summary: 'Explains SRP as the rule that a class should have one reason to change, tied to one actor. It shows how separating presentation, persistence, and business logic reduces coupling and change impact.'
tags: ["solid", "single-responsibility-principle", "software-design", "refactoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SOLID: Part 1 – The Single Responsibility Principle | Nettuts+"
    url: "http://net.tutsplus.com/tutorials/php/solid-part-1-the-single-responsibility-principle/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/net-tutsplus-com--solid-part-1-single-responsibility-principle.md"
    kind: repo
---

The page defines the Single Responsibility Principle as the idea that a class should have only one reason to change. It links that reason to an actor, meaning the part of the business that uses the code and can request change.

It uses books, printing, saving, and library lookup to show when responsibilities are mixed and when they are separated. The text also warns that SRP should be applied with care, because trying to split everything too early can make the design scattered.

## Reading notes

- SRP says a class should have only one reason to change.
- Multiple reasons to change can mean multiple teams, redeployments, and retesting work.
- The audience of a module helps identify its reason for change.
- Roles are easier to reason about through actors than through concrete people.
- A responsibility is a family of functions that serves one particular actor.
- An actor is the single source of change for that responsibility.
- Printing belongs outside the Book class when presentation is a separate actor.
- Saving belongs outside the Book class when persistence is a separate actor.
- Moving persistence into another class keeps the Book class free to change for business reasons only.
- Factories, persistence, and presentation can each sit in separate parts of the architecture.
- Requirements that affect the same group of functions may indicate one responsibility.
- The primary value of software is ease of change.
- User needs lead to actor needs, and actor needs define responsibilities.
- Design should find actors, identify the responsibilities that serve them, and group functions accordingly.
- A Book class that includes location can still violate SRP if librarians and readers are different actors.
- Introducing BookLocator separates the librarian’s concern from the reader’s concern.
- Whether SRP is respected depends on the actual business, including self-service library models.
- SRP reduces coupling, but overapplying it too early can create a scattered design.
