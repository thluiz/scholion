---
title: "Using Bootstrap Native with Phoenix LiveView"
date: '2026-11-16T03:32:16+00:00'
category: webclip
summary: 'The article shows how to combine Bootstrap Native with LiveView by configuring Webpack, loading Bootstrap CSS and JavaScript, reinitializing Bootstrap hooks after page updates, and handling dropdowns, forms, and modals.'
tags: ["bootstrap", "forms", "phoenix", "liveview"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using Bootstrap Native with Phoenix LiveView"
    url: "https://dashbit.co/blog/using-bootstrap-native-with-live-view"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dashbit-co--using-bootstrap-native-with-phoenix-liveview.md"
    kind: repo
---

The article explains how to make Bootstrap and LiveView work together without bringing in jQuery. It uses Bootstrap Native for client-side components, then shows how to configure Webpack, load Bootstrap’s CSS and JavaScript, and reapply Bootstrap hooks after LiveView updates the page.

## Reading notes

- Use Bootstrap Native instead of Bootstrap’s jQuery-based JavaScript because most of the app is already powered by LiveView.
- Install bootstrap, bootstrap.native, and bootstrap.native-loader, then add a Webpack rule to load Bootstrap Native components, with an `only` option if you want to limit what gets loaded.
- Import Bootstrap’s SCSS in `app.scss` and `bootstrap.native` in `app.js`.
- After LiveView finishes page loading, call `BSN.initCallback(document.body)` so newly inserted content gets Bootstrap Native’s JavaScript behavior.
- Add `phx-update="ignore"` to elements that open and close on the client, such as dropdown roots, so LiveView does not interfere with them during updates.
- Use `phx-feedback-for` on the wrapper around an input to control when validation feedback appears, and pair it with `phx-no-feedback` styles that hide invalid and valid messages until the field has been used.
- The article’s form example relies on a single `input` function to generate fields, and points to a previous post about dynamic forms in Phoenix.
- For LiveView modals, the article uses a `live-modal` class at the top of the modal, keeps Bootstrap modal classes inside it, and adds CSS based on Phoenix’s modal styling.
