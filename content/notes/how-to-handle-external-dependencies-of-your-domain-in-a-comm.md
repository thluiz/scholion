---
title: "How to handle external dependencies of your domain in a command-event architecture"
date: '2026-09-25T09:07:11+01:00'
category: webclip
summary: 'The article compares five ways to handle external dependencies in a command-event architecture domain, from classic injection to the reader monad, and concludes in favor of internal commands with explicit dependencies.'
tags: ["command-event-architecture","dependency-injection","fsharp","reader-monad"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to handle external dependencies of your domain in a command-event architecture"
    url: "https://hardt.software/how-to-handle-external-dependencies-of-your-domain-in-a-command-event-architecture/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hardt-software--how-to-handle-external-dependencies-of-your-domain-in-a-comm.md"
    kind: repo
---

The article walks through several ways to handle external data needed by a domain in a command-event architecture. It compares classic OOP dependency injection, a more idiomatic F# function-based approach, dependency records, a pure execute function fed by the service layer, internal and external commands, and a reader monad on the service level.

Its main point is that the best fit, for the author, is to keep the domain execute function pure and move the needed data into internal commands instead of one growing dependency record. The reader monad is presented as interesting, but not clearly better for this example.

## Reading notes

- The article is about how to manage external dependencies and additional data in a command-event architecture domain.
- The author warns that the focus is not on modeling the domain better, but on handling dependency management.
- In the example, an invoice needs customer and product data to be created and enriched with lines.
- The model stores name, address, price, and quantity inside the events and the invoice state.
- In the classic OOP approach, the aggregate root receives repositories in the constructor and calls those repositories in the command methods.
- This approach is straightforward, but it requires more boilerplate and heavier tests with mocks.
- In the more idiomatic F# approach, the logic becomes execute, apply, and applyEvents functions.
- In this version, the data access functions come in as parameters and are then partially applied in the service.
- The author says that this still spreads dependencies across parameters and does not improve tests much.
- In an attempt to hide dependencies, he groups access functions into a Dependencies record.
- This version reduces the parameter list, but shifts the problem to the growth of the record itself.
- Then, the article makes execute pure by moving external calls into the service and leaving only already loaded data there.
- In this scenario, the service builds a dependencies record with customer or product and calls the pure execute.
- The author notes that this improves testability, but still centralizes too many dependencies in a single record.
- In the last approach before the reader monad, he separates ExternalCommand and internal Command.
- The internal commands carry optional customer or product in the payload, and each command starts carrying its own dependencies.
- The author prefers this solution because it gives more clarity and better separates responsibilities.
- In the version with the reader monad, he creates a single IDependencies interface and encapsulates injection in the dependency computation expression.
- Even so, for this example, he does not see a clear advantage over passing the interface directly to executeCommand.
- He concludes that the reader monad may make more sense when the application grows and there are more dependencies to hide.
