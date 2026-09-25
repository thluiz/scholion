---
title: "Building Your First Use Case With Clean Architecture"
date: '2026-09-25T22:32:55+01:00'
category: webclip
summary: 'The article explains how a user-registration use case fits in the Application layer, depends on interfaces for external systems, and follows the dependency rule while remaining testable.'
tags: ["clean-architecture", "use-case", "application-layer", "dependency-rule"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Your First Use Case With Clean Architecture"
    url: "https://www.milanjovanovic.tech/blog/building-your-first-use-case-with-clean-architecture?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/milanjovanovic-tech--building-your-first-use-case-with-clean-architecture.md"
    kind: repo
---

The article shows how to design a user-registration use case with Clean Architecture by keeping the core logic in the Application layer. The use case coordinates domain entities, takes a registration request, returns a result, and hides external systems like the database and password hasher behind interfaces.

It also points out two practical issues. Email uniqueness checks can fail under concurrent requests, so a unique database index is the safer place to enforce that rule. Changing the password hash function can break existing logins, so the system should keep track of which algorithm produced each stored hash and migrate users gradually.

## Reading notes

- A use case belongs in the Application layer and orchestrates data flow to and from domain entities.
- External systems such as a user repository and password hasher are abstracted behind interfaces and injected as dependencies.
- The dependency rule says source code dependencies can only point inward.
- For user registration, the use case validates input, checks whether the email already exists, hashes the password, creates a User, saves it, and returns the result.
- The example use case is named `RegisterUser` and uses `RegistrationRequest` and `RegistrationResult`.
- This structure makes it possible to test the use case with mocks without needing real implementations first.
- A race condition can happen when two requests pass the email uniqueness check before either saves the user.
- A unique index on the Email column pushes uniqueness enforcement into the database and lets the application handle the resulting error.
- Replacing a password hashing implementation can break logins for existing users because stored hashes no longer match.
- The suggested fix is to store which hash function produced each password hash and rehash users gradually during login.
