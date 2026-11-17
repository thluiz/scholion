---
title: "A Proposal for Some New Rules for Phoenix Contexts"
date: '2026-11-17T15:06:10+00:00'
category: webclip
summary: 'Proposes a layered Phoenix/Ecto structure: schemas limited to data and changesets; per-schema Secondary Contexts for CRUD and Repo access; Primary Contexts for higher-level composition.'
tags: ["phoenix", "elixir", "contexts", "architecture"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "A Proposal for Some New Rules for Phoenix Contexts"
    url: "https://devonestes.com/a-proposal-for-context-rules"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--new-rules-for-phoenix-context-structure.md"
    kind: repo
---

The author proposes explicit rules for structuring Phoenix apps (v1.3+) that use Ecto. The goal is to avoid analysis paralysis and duplication by enforcing clear layers: Schema modules limited to data and changesets, per-schema Secondary Contexts handling all Repo-based CRUD, and Primary Contexts expressing higher-level domain ideas by composing Secondary Context functions. This structure is presented as theoretical and experimental, intended to spark discussion rather than as proven best practice.

## Reading notes

- Rules are presented as a way to reduce decision fatigue when programming, even if they are somewhat arbitrary or later revised.
- The proposal targets Phoenix applications using contexts (1.3+) and Ecto, aiming to refine the loosely defined guidance from Phoenix about where functions should live.
- The author emphasizes they have not used these rules in a large production system and sees the post as a proposal to encourage community debate rather than as empirically validated advice.

- Rule 1: every Ecto-backed resource gets a Schema file containing only schema definitions, type specs, validations, and changeset functions.
- All public functions in a Schema module should return an `Ecto.Changeset` struct, and no validations or changeset generation should live in controllers or other layers.
- In real applications, schema and changeset logic can grow to hundreds of lines, so restricting this behavior to a dedicated file keeps it focused.
- The Schema module is considered private in practice: tests should target behavior through the corresponding Secondary Context instead of testing the schema module directly.

- Rule 2: every Schema has a dedicated Secondary Context module responsible for CRUD operations for that resource.
- Each function in a Secondary Context returns either a single resource, a list of resources, a changeset, or a list of changesets in error cases.
- Secondary Contexts are named as the namespace containing the Schema (e.g. `MyApp.SocialMedia.Users` for `MyApp.SocialMedia.Users.User`).
- The example Secondary Context shows functions such as `find/1`, `find_and_load_associations/1`, `create/1`, and specific preload helpers.
- The author expects these modules to grow with many small functions, which they view as useful building blocks for composition.

- Rule 3: the only place `Repo` is used is inside a Secondary Context, and only for that context’s associated resource.
- The author forbids Repo calls from controllers, views, or other modules; any needed Repo access should be added as a function in the appropriate Secondary Context.
- Within a Secondary Context, it is considered wrong to pass a different resource type to the Repo (e.g. using `Repo.preload/2` on `FacebookPost` inside `Users`), even if the returned type is allowed.
- In that case, the operation should be delegated to the other resource’s Secondary Context (e.g. `FacebookPosts.with_user/1`) and then used from there.
- Calling functions across Secondary Contexts is allowed, but the example where a function deals with relationships between two resources is identified as something that belongs in a Primary Context instead.

- Rule 4: Primary Contexts define higher-level concepts and orchestrate interactions between multiple resources.
- The author separates basic CRUD (Secondary Contexts) from broader domain operations (Primary Contexts) to keep modules maintainable over time.
- A Primary Context may call many Secondary Context functions and combine them into operations like resolving the author of a post, loading all posts for a user, or downloading and persisting posts from external APIs.
- The Primary Context is described as the true context boundary: code outside it should not directly call Secondary Contexts in that domain.
- To the rest of the application, Secondary Contexts and their Schemas are treated as hidden behind the Primary Context interface.

- The author conceptualizes Schema, Secondary Context, and Primary Context as three privacy layers, each with specific allowed dependencies.
- Primary Contexts may call any Secondary Context in their domain but not Schemas directly; Secondary Contexts may call their own Schema but not sibling Schemas.
- This layering is intended to provide clean abstractions and make placement of new functions easier to reason about.
- The author finds that having a separation between Primary and Secondary Contexts makes it easier to move resources between contexts during refactoring.
- They note that applications evolve with new understanding, and this structure is meant to support that evolution by easing later changes.

- The proposed layout forms a tree-like directory and dependency structure, shown with `social_media.ex` at the top and per-resource context and schema files under it.
- The author highlights that trees are recursive, suggesting the possibility of composing Primary Contexts into even higher-level "Super Contexts" in the future.
- They describe how the approach emerged from starting with only Secondary Contexts while boundaries were unclear, then later introducing Primary Contexts as abstractions once clearer domain boundaries appeared.
- The author is unsure how far composition into larger units should go but expresses interest in exploring deeper levels of abstraction over time.
