---
title: "How I Stopped Worrying and Started Loving the Umbrella – TAGBASE"
date: '2025-07-17T13:36:19+01:00'
category: webclip
summary: 'The author explains why Tagbase moved from separate Node.js and Elixir apps to an Elixir umbrella app, focusing on shared code, clearer boundaries, faster local development, and safer separation between portal and back office.'
tags: ["elixir", "phoenix", "umbrella-apps", "monorepo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I Stopped Worrying and Started Loving the Umbrella – TAGBASE"
    url: "https://www.tagbase.io/how-i-stopped-worrying-and-started-loving-the-umbrella/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/tagbase-io--how-i-stopped-worrying-and-started-loving-the-umbrella-tagba.md"
    kind: repo
---

The author says Tagbase began with a Node.js verification prototype, then added an Elixir portal and later an Elixir back office. Once the product split into three Phoenix apps that needed shared code, the setup became hard to maintain, especially during local development.

## Reading notes

- Tagbase started with a Node.js prototype that could verify NFC tags, then moved into Elixir with Phoenix for the portal and the back office.
- The portal needed a globally distributed verification flow, while customers needed a centralized place to configure tags, so the two concerns could not stay in one app.
- Sharing code across standalone Elixir apps was awkward, and the author tried to manage the apps with a shared folder structure and different build targets.
- That arrangement worked with Docker and Fly.io, but local development became confusing because changes landed in the wrong folder and Tailwind components did not update across apps.
- The author decided to switch to an umbrella app after the setup cost, weak documentation, and unclear handling of shared assets kept causing friction.
- Security also mattered, because the back office contained risky functionality that the author did not want close to the portal codebase.
- After the move, the apps could run with one command, shared files compiled once, code changes appeared across all apps, and each app kept its own dependency tree.
