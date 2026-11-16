---
title: "Domain-Driven Refactoring: Defactoring and Pushing Behavior Down"
date: '2026-11-16T04:44:43+00:00'
category: webclip
summary: 'The post shows how to reverse earlier extractions, inline the helper methods, and then move the assignment logic onto Member. The goal is to keep behavior in the domain model and make it easier to test.'
tags: ["refactoring", "domain-driven-design", "feature-envy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Domain-Driven Refactoring: Defactoring and Pushing Behavior Down"
    url: "https://jimmybogard.com/domain-driven-refactoring-defactoring-and-pushing-behavior-down"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/jimmybogard-com--domain-driven-refactoring-defactoring-and-pushing-behavior-d.md"
    kind: repo
---

The post continues the refactoring of a procedural handler by undoing earlier extractions, then regrouping the assignment logic so it can be moved into the domain model. The author uses defactoring to inline methods, then extracts the whole block again to identify direct inputs and outputs before moving the method to Member.

The main cue for where the behavior should live is feature envy. Member is the object receiving the action, so the assignment logic fits there better than in Offer or in the handler. After moving the method, the handler becomes smaller and the member object owns the work of creating the offer and updating its own state.

## Reading notes

- Earlier extractions made the handler more testable, but the remaining code was still procedural.
- Defactoring is described as a logical undo of refactoring, such as inlining methods that were previously extracted.
- The author lists reversible pairs like Extract Method and Inline Method, Extract Variable and Inline Variable, and Extract Class and Inline Class.
- After inlining, the code calculates the expiration date and constructs the offer in place.
- Extracting that block again helps isolate its direct inputs and outputs.
- The method is static at first, so it has no indirect inputs or outputs.
- The main code smell identified is feature envy.
- Member is the primary actor because the method sets its state and adds the new offer to its collection.
- OfferType is only used to calculate the final value.
- Offer is treated as the return value, not as the best place for the behavior.
- The author uses the grammar idea of the object receiving the action as a guide for where the method should live.
- The method is moved with a Move Method-style refactoring using ReSharper's Make Method Non-Static.
- After the move, the handler calls member.AssignOffer(offerType, value).
- The moved method now uses Member instance members such as AssignedOffers and NumberOfActiveOffers.
- The result is a domain method that can be unit tested without mocks or stubs.
