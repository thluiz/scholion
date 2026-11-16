---
title: "Phoenix LiveView: Multi-step forms"
date: '2020-07-05T14:10:40+00:00'
category: webclip
summary: 'The post argues that multi-step forms are easier to reason about when each step lives in its own LiveComponent, with computed fields, progress managed by the parent LiveView, and browser timezone input pushed in via a hook.'
tags: ["phoenix-liveview", "livecomponents", "multi-step-forms", "ecto-changeset"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Phoenix LiveView: Multi-step forms"
    url: "https://bernheisel.com/blog/liveview-multi-step-form"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/bernheisel-com--phoenix-liveview-multi-step-forms.md"
    kind: repo
---

The post says Phoenix LiveView makes it practical to move common front-end logic into the backend, especially for long or multi-step forms. The author contrasts a single large LiveView form with a component-based approach, where each step owns its own state and computed fields.

## Reading notes

- LiveView is presented as a good fit for consolidating front-end logic in the backend, especially for long-running or multi-step forms.
- The first attempt used one large LiveView and one `<form>` for every step, with hidden sections shown one at a time.
- That approach caused problems with Enter submitting too early, state from other steps still needing management, validations affecting hidden inputs, and difficult testing.
- The author also needed computed fields such as dates, times, time zones, and duration, which made the single-form approach harder to reason about.
- The recommended structure is to split the form into LiveComponents, with embedded schemas as form objects for each step.
- The parent LiveView keeps a `%Step{}` structure and a step order list, and switches the visible step when components send messages back.
- Each component initializes its changeset from the record, validates user input locally, computes derived values, and sends the finished struct upward when valid.
- The `WhenComponent` example stores timezone, date, time, and computed fields such as `start_at`, `end_at`, and `duration`.
- The component updates computed values after validation and on load, so the parent can combine step params into the final record later.
- Browser timezone is detected with `Intl.DateTimeFormat().resolvedOptions().timeZone` and passed into the component through a `phx-hook`.
- The hook updates a hidden input and immediately pushes a `timezone` event to the LiveComponent so the changeset can be updated before user interaction.
- Validation events are targeted at the LiveComponent with `phx-target`, and the component adjusts time params when `start_at_time` or `end_at_time` changes.
- On submit, the component uses `Ecto.Changeset.apply_action/2` to confirm validity and then sends the completed struct to the parent LiveView.
- The parent LiveView merges the step data into accumulated params, advances to the next step, and saves once there is no next step.
- The conclusion notes that drafts between steps could be persisted with `handle_params`, and that the code is written for creating a new event rather than editing one.
