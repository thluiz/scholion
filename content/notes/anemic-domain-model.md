---
title: "Anemic Domain Model"
date: '2015-05-14T21:02:35-03:00'
category: webclip
summary: 'An anemic domain model has domain objects with little behavior and pushes logic into services. Fowler argues this recreates procedural design, keeps the costs of a domain model, and loses its main benefits.'
tags: ["domain-model", "service-layer", "object-oriented-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "AnemicDomainModel"
    url: "http://martinfowler.com/bliki/AnemicDomainModel.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/martinfowler-com--anemic-domain-model.md"
    kind: repo
---

Fowler describes an anemic domain model as a design that looks like a domain model at first, because it has objects named after domain nouns and rich relationships. The problem appears when those objects have little behavior and act mostly as bags of getters and setters, while services hold the domain logic.

He argues that this goes against object-oriented design, which combines data and process in the same place. In his view, an anemic domain model keeps the costs of a domain model, especially O/R mapping, but gives up the benefits by sliding into transaction scripts and procedural programming. He also says a service layer can exist, but it should stay thin and delegate to a behaviorally rich domain layer. Eric Evans’s description of application and domain layers is used to support that separation.

## Reading notes

- The anti-pattern looks like a domain model at first because the objects match domain nouns and have rich structure.
- The weakness is that the objects have almost no behavior and are reduced to getters and setters.
- Domain logic is pushed into service objects that sit on top of the model and use it for data.
- Fowler says this conflicts with object-oriented design because it separates data from process.
- The pattern keeps the cost of mapping a domain model to a database, including O/R mapping.
- By moving behavior into services, the design loses the benefits of a domain model and becomes closer to transaction scripts.
- Domain objects should hold domain logic such as validations, calculations, and business rules.
- A service layer is acceptable when it stays thin and coordinates work instead of holding business rules.
- Evans’s application layer directs domain objects and does not contain business rules.
- The domain layer is described as the heart of business software, with state and business rules controlled there.
- Fowler sees the problem as common among people who have not worked with a proper domain model, especially from a data background.
- He also points to technologies like J2EE Entity Beans as encouraging the pattern.
- If most behavior ends up in services, the design is likely losing the advantages of a domain model.
