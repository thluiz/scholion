---
title: "How to isolate complex queries in an object oriented fashion – Alfredo Motta"
date: '2016-02-07T22:42:34-03:00'
category: webclip
summary: 'The article shows how a talent-hunting app can move player search logic out of the active record model and into an `InterestingPlayer` query object, so domain-specific queries stay reusable and `TalentHunter` stays easier to read.'
tags: ["query-object", "decorator-pattern", "active-record", "ruby-on-rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to isolate complex queries in an object oriented fashion – Alfredo Motta"
    url: "http://www.alfredo.motta.name/how-to-isolate-complex-queries-in-an-object-oriented-fashion/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/alfredo-motta-name--how-to-isolate-complex-queries-in-an-object-oriented-fashion.md"
    kind: repo
---

The article starts from a talent-hunting system that searches football players by team, shooting accuracy, and age. Instead of keeping these conditions inside `TalentHunter` as a chain of conditional query clauses, it proposes moving them into a separate object tied to the talent-hunting use case.

## Reading notes

- The example system searches players using three criteria: big team membership, good shooting accuracy, and young age.
- The first implementation builds the query in `TalentHunter` with conditional statements.
- The text suggests refactoring with Extract Method or with scopes in the `Player` model.
- The proposed alternative uses a Query Object-style approach.
- The goal is to isolate queries in a separate object without adding scopes to the active record model.
- The text says queries like young, good shooting accuracy, and playing for a top team make sense in the talent-hunting task.
- `InterestingPlayer` is presented as a decorator-like object that behaves like `Player` and adds query methods.
- Some methods on `InterestingPlayer` return a new wrapped object so queries can keep composing.
- Other delegated methods return the final result when the underlying relation no longer matches a relation type.
- `TalentHunter` then uses domain terms such as `right_foot`, `playing_for_big_team`, `with_great_shoot_accuracy`, and `young`.
- The article says this makes `find_good_forward` easier to read and keeps the general model less polluted.
- It concludes that the approach simplifies both the query builder and the `TalentHunter` object.
