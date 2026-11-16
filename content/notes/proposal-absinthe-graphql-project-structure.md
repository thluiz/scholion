---
title: "A proposal for an Absinthe application structure"
date: '2026-11-16T20:08:49+00:00'
category: webclip
summary: 'Proposes a consistent Absinthe/GraphQL project structure in Elixir, separating types, schema fragments and resolvers, with matching tests and clear naming and input patterns.'
tags: ["elixir", "graphql", "absinthe", "project-structure"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "A proposal for an Absinthe application structure"
    url: "https://devonestes.com/a-proposal-for-absinthe-project-structure"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--proposal-absinthe-graphql-project-structure.md"
    kind: repo
---

The text proposes a clear structure and vocabulary for organizing Absinthe-based GraphQL applications in Elixir. It distinguishes between types, input objects, schemas (as decomposed schema fragments), and resolvers, and shows how to arrange them in separate directories under a Phoenix-style `blog_web` umbrella. The author emphasizes consistency in where definitions live, how arguments are modeled with input objects, and how schema fragments are imported into a single root schema. Testing mirrors the source layout, with resolver tests treating resolvers like normal functions and schema tests exercising both GraphQL responses and side effects. The tradeoff is a larger number of files in exchange for consistent organization and manageable test sizes.

## Reading notes

- GraphQL's broad abstractions (everything as objects with fields) improve composability but make project organization and shared terminology difficult.
- The author defines terms: a "type" is an Absinthe `object` definition; an "input object" is a type used specifically for operation arguments; a "schema" here is the Absinthe API interface composed of queries, mutations and subscriptions.
- To avoid confusion with other schemas (like Ecto or database schemas), the author suggests explicitly saying "Ecto schema" or "Absinthe schema" when talking with the team.
- The example domain uses the canonical blog model with users, posts and comments.
- The proposed directory layout separates `types`, `schemas` and `resolvers` under `blog_web`, with subdirectories for schemas by operation kind (queries, mutations, subscriptions).
- Each domain concept (user, post, comment) has its own type file, resolver module, and per-operation schema files where applicable.
- The `types` directory contains one file per domain concept, and each file can define multiple related `object` and `input_object` definitions.
- Input objects are stored alongside types in the same module because they are closely related to the same domain area.
- In the `BlogWeb.Types.User` example, user-related objects and input objects (`:user`, `:user_input`, `:admin`, `:admin_input`) are kept together in a single module.
- Type modules should not contain resolver functions, and anonymous resolver functions are discouraged even if short; all resolver logic should live in resolver modules.
- Resolver modules such as `UserResolver` or `PostResolver` are the only place for resolver definitions, referenced from types and schema fragments.
- The `schemas` directory holds decomposed pieces of a single large Absinthe schema, split by domain and by operation type (queries, mutations, subscriptions).
- A queries module like `BlogWeb.Schemas.Queries.User` defines a `:user_queries` object that groups user-related query fields and wires them to resolver functions.
- These schema fragments are responsible for setting up arguments, using previously defined input objects (e.g., `:user_input`) for arguments where possible.
- The text advises designing queries, mutations and subscriptions to take a single argument that is an `input_object` when arguments are needed.
- The root `BlogWeb.Schema` module imports all type modules and schema fragments with `import_types`, grouping imports by domain and operation type.
- The `query`, `mutation` and `subscription` blocks in `BlogWeb.Schema` use `import_fields` to pull in field groups like `:user_queries` or `:post_subscriptions`.
- The author notes that consistent naming might allow a macro to automate schema imports, but cautions against reaching for macros too quickly due to long-term maintenance costs.
- Resolver tests live under `test/blog_web/resolvers`, mirroring the resolver modules, and treat resolvers as ordinary functions to be unit-tested.
- A resolver test example for `UserResolver.list/3` inserts test data with a factory and asserts that the returned list matches the inserted users.
- Schema tests mirror the schema fragment files under `test/blog_web/schemas/queries`, `mutations` and `subscriptions`, matching the source hierarchy.
- In schema tests, each `describe` block corresponds to a specific GraphQL query, mutation or subscription under test.
- The example mutation test for `createComment` builds a GraphQL mutation string, passes variables to `Absinthe.run/3`, and asserts on both the returned data and database state.
- The `createComment` test checks that the response contains an integer `id`, that the nested post `id` matches the request, and that the persisted comment in the database matches the expected values.
- The author emphasizes testing both the client-visible response and the side effects (often database writes), warning that testing only responses is dangerous.
- Typically, schema-level tests cover the happy path and one expected failure case (such as missing data or authorization), with more detailed scenarios tested at lower layers.
- A tradeoff of the proposed structure is the increased number of files, which some developers might find excessive compared to consolidating schemas per domain.
- An alternative structure would place all of a domain's queries and mutations in a single file like `blog_web/schemas/user.ex`, but the author argues this leads to very large test files.
- The author prefers file-level consistency between source and tests, so each smaller schema file has a corresponding smaller, focused test file.
- They argue that when a domain (often `user`) grows to many mutations, large monolithic files become unwieldy, and splitting them later harms consistency.
- The chosen design favors consistent structure across the project over convenience in the majority of simple cases that do not include heavily loaded domains.
