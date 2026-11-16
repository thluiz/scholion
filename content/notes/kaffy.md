---
title: "Kaffy"
date: '2020-07-05T14:10:39+00:00'
category: webclip
summary: 'Kaffy is a flexible admin interface for Phoenix apps, with support for contexts, custom dashboards, pages, queries, search, authorization, actions, callbacks, and scheduled tasks.'
tags: ["phoenix", "admin-interface", "ecto", "customization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Kaffy"
    url: "https://aesmail.github.io/kaffy"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/aesmail-github-io--kaffy.md"
    kind: repo
---

Kaffy is presented as a simple, flexible, customizable admin interface for Phoenix applications, inspired by Django’s admin and Rails’ ActiveAdmin. The page explains setup requirements, configuration, and the main extension points for adapting the admin UI without changing the existing codebase.

## Reading notes

- It supports the latest two Phoenix versions starting with v0.10.0.
- Installation requires adding Kaffy as a dependency and configuring router, endpoint static assets, otp_app, ecto_repo, and router settings.
- The default browser pipeline is `:kaffy_browser`, and custom pipelines are appended after it.
- Version 0.9 replaces `:schemas` with `:resources`.
- Resources can be auto-detected or explicitly defined, including contexts and admin modules.
- The home page can be the dashboard, a schema index page, or a custom page.
- Dashboard widgets can be text, tidbit, progress, or chart widgets.
- Admin modules can define custom side menu links with top, sub, or bottom placement.
- Custom pages are defined with a slug, name, view, template, assigns, and order.
- Index pages can customize displayed fields, labels, values, filters, ordering, and default actions.
- Form pages can customize field types, choices, labels, help text, create and update visibility, and array values.
- `belongs_to` associations are referenced by the foreign key field name, and `many_to_many` is not supported.
- Custom field types can define form and index rendering.
- Queries can be customized for index and show pages, including preloading associations.
- Extensions can inject CSS and JavaScript into Kaffy’s layout.
- Embedded schemas and JSON fields are supported.
- Search supports several field types and can traverse associations.
- Authorization is handled per schema with `authorized?/2`.
- Separate create and update changesets can be defined.
- Singular and plural resource names can be overridden.
- Single-resource actions, list actions, callbacks, overwritten CRUD actions, and scheduled tasks are supported.
- Scheduled tasks run in memory under GenServers and are meant for simple, non-critical operations.
