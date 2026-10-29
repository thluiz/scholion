---
title: "Test Driven Development With Node, Postgres, and Knex (Red/Green/Refactor)"
date: '2016-05-09T13:53:08-03:00'
category: webclip
summary: 'The post walks through building a REST API with Node, Express, Knex, and PostgreSQL using TDD, from setup and migrations to tests and routes for CRUD operations.'
tags: ["test-driven-development", "node", "postgresql", "knex"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Test Driven Development With Node, Postgres, and Knex (Red/Green/Refactor) - Michael Herman"
    url: "http://mherman.org/blog/2016/04/28/test-driven-development-with-node"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/mherman-org--test-driven-development-with-node-postgres-and-knex.md"
    kind: repo
---

The post outlines a test-first workflow for building a RESTful API with Node, Express, Knex, and PostgreSQL. It covers project setup, database configuration, migrations, seed files, and Mocha/Chai test setup before moving into route implementation.

## Reading notes

- Sets up separate development and test databases with Knex configuration for different environments.
- Uses migrations to create a `shows` table with fields for name, channel, genre, rating, and explicit content.
- Uses seed files to populate development and test databases with the same initial rows.
- Configures Mocha, Chai, and Chai HTTP for route testing, and prefixes routes with `/api/v1`.
- Shows the red/green/refactor cycle by writing a failing test, then adding a query and route until it passes.
- Builds GET all shows, GET one show, POST, PUT, and DELETE routes for the `shows` resource.
- Uses `beforeEach` and `afterEach` to roll back migrations and reseed the database so tests stay isolated.
- Prevents updating the `id` field and adds a test for that case.
- Notes that error handling is still incomplete for missing fields and deleting absent rows.
