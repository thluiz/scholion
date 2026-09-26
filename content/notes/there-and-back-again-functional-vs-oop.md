---
title: "There and Back Again"
date: '2026-09-27T00:41:02+01:00'
category: webclip
summary: 'The author compares C# and F# through a bank-account withdrawal app, showing how immutability in F# keeps data changes separate from persistence, while C# needs extra care with Entity Framework tracking.'
tags: ["functional-programming", "c-sharp", "f-sharp", "immutability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "There and Back Again"
    url: "http://www.andreavallotti.tech/en/2017/09/there-and-back-again/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/andreavallotti-tech--there-and-back-again-functional-vs-oop.md"
    kind: repo
---

The post compares the same bank-account withdrawal app in C# and F#. In the C# version, Entity Framework tracking keeps the modified object alive in the context, so the displayed balance changes even when the user does not confirm saving. The fix is to detach the object with `AsNoTracking()` and attach it again only when the update is confirmed.

In the F# version, the domain model is an immutable record and `withdraw` returns a copy with the new balance. Data access is kept separate from the domain logic, and the console app confirms the withdrawal before persisting the updated record. The conclusion is that immutability makes the separation between reading, changing, and saving data clearer, while good OOP code requires more discipline.

## Reading notes

- The author spent six months in Indianapolis and took part in conferences and meetups there.
- Functional programming drew attention for three reasons: unfamiliarity, its potential, and Dave Fancher’s enthusiasm.
- The example application reads a bank account, withdraws an amount, asks for confirmation, saves the balance only if approved, and repeats.
- In the first C# version, `BankAccount` is a mutable entity with a `Withdraw` method that changes `Balance`.
- The first C# implementation uses Entity Framework context tracking, so the in-memory object changes even before the save.
- If the user refuses to confirm, asking for the same account again can still show the modified balance.
- The revised C# version loads the account with `AsNoTracking()` and marks it modified only after confirmation.
- In F#, `BankAccount` is a record and `withdraw` creates a new record with the updated balance.
- The F# data access layer maps the record to SQL Server and keeps the application code detached from the database.
- The F# console app mirrors the C# workflow, but the author says it was harder only because they are more used to OOP.
- The conclusion says immutability helps define the boundary between data access and data processing.
- The author says good OOP code needs discipline, while the functional style is more formal and more intuitive only to a point.
