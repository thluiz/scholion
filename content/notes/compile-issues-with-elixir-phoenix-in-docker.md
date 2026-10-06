---
title: "Compile issues with Elixir/Phoenix in a Docker container"
date: '2015-05-25T08:53:56-03:00'
category: webclip
summary: 'A Phoenix project compiled in Docker breaks after container restarts because Hex registry data in ~/.hex is not preserved, causing deps like plug to disappear from _build/dev/lib until deps are fetched again.'
tags: ["elixir", "phoenix", "docker", "hex"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[elixir-talk:8586] Compile issues with Elixir/Phoenix in a Docker container - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d87057983dd727"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/mail-google-com--compile-issues-with-elixir-phoenix-in-docker.md"
    kind: repo
---

The thread describes a Phoenix app that compiles inside a Docker container at first, but fails after the container is restarted. The build folder loses compiled dependencies such as plug because Mix no longer sees them as dependencies.

José Valim points to Hex registry problems, and the original poster confirms that the missing piece was the ~/.hex directory. Mounting that folder as a volume makes compilation work again after restarts.

## Reading notes

- The project folder is mounted as a volume, so source files survive container restarts.
- After restarting the container, running mix compile removes some compiled dependencies under _build/dev/lib.
- The error shown is a MatchError tied to plug.app not being found.
- Running mix deps.get does not download anything new, but it makes compilation work again.
- José Valim says this happens when plug is no longer seen as a dependency.
- He suggests checking behavior with --no-compile or --no-deps-check.
- The reported cause is a missing ~/.hex registry after container restarts.
- Mounting $(pwd)/.hex to /root/.hex fixes the issue.
