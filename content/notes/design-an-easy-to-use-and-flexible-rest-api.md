---
title: "Design an easy to use and flexible REST API"
date: '2026-11-16T00:58:44+00:00'
category: webclip
summary: 'The article argues that a good REST API starts with an atomic database schema, then maps cleanly to URLs, while separate routes and history tables keep responses flexible and easier to maintain.'
tags: ["rest-api", "database-design", "odata", "graphql"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Design an easy to use and flexible REST API"
    url: "https://dev.to/khalyomede/design-an-easy-to-use-and-flexible-rest-endpoints-3fia"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--design-an-easy-to-use-and-flexible-rest-api.md"
    kind: repo
---

The article links REST API design to database design. It argues that tables should stay atomic, with columns that belong to the entity, so routes remain clear and easy to maintain. It uses a todo app to show CRUD endpoints, separate routes for related data, and history stored in a dedicated table.

## Reading notes

- A client that needs several dependent routes to get its data may signal a database design that should be reconsidered.
- A well-designed schema avoids repeated connections, keeps entity data in its own table, and allows new dependencies without heavy rework.
- Database normalization is presented as a tool for checking whether the schema is consistent.
- In the todo app example, users and tasks are mapped to CRUD-style REST endpoints.
- The article recommends treating table columns as attributes of the entity and avoiding columns that do not belong to it.
- Related data such as assigned tasks or assigned users should use separate routes instead of being folded into the main detail route.
- The author warns that returning 1-N relationships in an entity detail route can add unnecessary bandwidth and server work.
- Trashing a user is modeled as updating the `active` field to false rather than deleting the row.
- The trash action should be placed separately from the ordinary edit form.
- Created and modified timestamps are treated as a limited shortcut when the real need is to track who created, modified, or deleted an entity.
- History is better modeled as a separate table and exposed through a route such as `GET /api/task/{id}/history`.
- Keeping history types in a table avoids copying enum values into the client application.
- For flexible responses, the article points to GraphQL as a model and to OData as a REST-friendly way to select fields and filter server responses.
- OData-style query support is described as something that can be added with a logic layer before returning results.
