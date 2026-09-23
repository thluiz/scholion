---
title: "3 Essential Techniques for Managing Transactions in EF Core"
date: "2026-09-23T18:58:18+01:00"
category: webclip
has_commentary: false
summary: "Compares three ways to wrap EF Core writes in a transaction: automatic per-call, manual begin/commit/rollback, and execution-strategy transactions that retry on transient failure."
tags:
  - entity-framework
  - dotnet
  - database-transactions
  - csharp
sources:
  - title: "3 Essential Techniques for Managing Transactions in EF Core"
    url: "https://blog.elmah.io/3-essential-techniques-for-managing-transactions-in-ef-core/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-elmah-io--3-essential-techniques-for-managing-transactions-in-ef-core.md"
    kind: repo
---

Ali Hamza Ansari walks through three ways EF Core wraps database writes in a transaction, moving from the automatic default to a manually controlled version to one built to survive transient failures.

Automatic transactions come free: each call to SaveChangesAsync wraps its own changes as a transaction and rolls them back on failure, with no extra code required. That scope is also the limit, since each call is its own transaction and the technique can't tie together operations that depend on each other across multiple calls. Manual transactions fix that by wrapping several SaveChangesAsync calls between Database.BeginTransaction and an explicit Commit or Rollback, trading simplicity for full control over multi-insert scenarios. The strategy-based technique goes further: CreateExecutionStrategy wraps a transaction so that a transient failure retries the entire block from the start, suited to writes across dependent entities, such as a Building row and the BuildingUnit rows that reference it.

## Fichamento

- Automatic transactions: each SaveChangesAsync call auto-wraps its own changes and rolls back on failure. Simplest option, runs asynchronously by default, but scopes to a single call and can't cover operations that depend on each other across multiple calls.
- Manual transactions: Database.BeginTransaction opens a transaction that spans several SaveChangesAsync calls, closed by an explicit transaction.Commit() or transaction.Rollback() inside a try/catch. Full control and per-exception handling, at the cost of more code and manual bookkeeping.
- Strategy-based transactions: _context.Database.CreateExecutionStrategy() wraps a transaction (BeginTransactionAsync, CommitAsync, RollbackAsync) inside strategy.ExecuteAsync, so a transient failure retries the whole block from the start instead of failing outright.
- The strategy technique fits writes across dependent entities in one request, such as saving a Building row and the BuildingUnit rows that reference its generated id, where a partial write would leave orphaned foreign keys.
- Tradeoff named for the strategy technique: resilience against transient failures and support for interdependent writes come with code that's harder to write, read, and tune than the other two.
