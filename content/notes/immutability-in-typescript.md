---
title: "Immutability in TypeScript"
date: '2026-11-16T05:50:14+00:00'
category: webclip
summary: 'The post argues that readonly properties and private constructors help enforce immutability in TypeScript, and that builders plus immutable data structures solve copying and mutation issues.'
tags: ["typescript", "immutability", "builders", "immutable-data-structures"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Immutability in TypeScript. Since I learnt Scala, immutability has… | by Ezequiel Foncubierta | Medium"
    url: "https://medium.com/@ezequiel/immutability-and-builders-with-typescript-b69a51c94e8c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--immutability-in-typescript.md"
    kind: repo
---

The post says immutability makes code simpler and less error prone, and that TypeScript can enforce it at compile time. It first shows a Person class with readonly fields, then shows that changing a property or adding new ones is blocked.

## Reading notes

- Immutability is presented as a top priority because it leads to simpler and less error prone code.
- JavaScript allows adding attributes to objects even when they were not declared.
- TypeScript can enforce immutable code at compile time.
- A Person class with readonly name, surname, and city only allows those values to be assigned in the constructor.
- If a field must change, the object has to be copied and rebuilt with the new value.
- Copying becomes painful when an object has many properties, and adding a new attribute breaks the copy code.
- The builder pattern is introduced as a way to build and copy Person objects more conveniently.
- The Person constructor is made private so the object can only be created through Person.builder().
- PersonBuilder can take an existing Person, change selected fields, and build a new Person.
- A readonly array property is still mutable, so push and pop can still change its contents.
- To handle that case, the post switches to Immutable.js and uses Set<string> for the cities field.
- Immutable.js is described as providing data structures such as List, Stack, Map, OrderedMap, Set, OrderedSet, and Record.
- With an immutable set, add returns a new set instead of changing the original one.
- The author says this approach is used at Hyperdoc to build immutable objects.
