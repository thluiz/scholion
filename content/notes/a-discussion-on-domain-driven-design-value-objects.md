---
title: "A Discussion on Domain Driven Design: Value Objects"
date: '2013-12-18T09:00:37-03:00'
category: webclip
summary: 'The post explains Value Objects as domain concepts without identity, contrasted with Entities. It uses everyday examples and a family model to show how Attire belongs to Kid and must be changed through the owner.'
tags: ["domain-driven-design", "value-objects", "entities", "aggregate"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Discussion on Domain Driven Design: Value Objects | Joe Ocampo's Blog"
    url: "http://lostechies.com/joeocampo/2007/04/23/a-discussion-on-domain-driven-design-value-objects/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/lostechies-com--a-discussion-on-domain-driven-design-value-objects.md"
    kind: repo
---

The post defines Value Objects as descriptive parts of a domain model that have no conceptual identity of their own. It contrasts them with Entities, which carry identity and lifecycle, and argues that a model becomes clearer when smaller descriptive parts are pulled out into Value Objects.

## Reading notes

- Value Objects are modeling concepts, not CLR value types, and they are not tied to a programming language.
- They describe aspects of the domain that matter for what they are, not for which instance they are.
- Everyday examples like pens, gum, paper clips, shoelaces, and currency are used to show cases where identity is irrelevant.
- A Value Object cannot live on its own without an Entity.
- Jay’s clothes are modeled as an Attire type so the Entity stays expressive while the model becomes simpler.
- Jay’s identity in the family context is his name, not an SSN.
- In the family context, Attire cannot exist on its own and is a Value Object of the Kid Entity.
- Access to or changes in Attire should go through Kid, which is presented as an Aggregate.
- The author suggests evaluating the model by asking whether an object needs identity outside its context and whether it can be simplified as a Value Object.
- The model should be validated with the product owner so the code and the model grow together.
