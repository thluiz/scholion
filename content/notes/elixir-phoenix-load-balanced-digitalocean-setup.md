---
title: "Elixir Phoenix App deployed into a Load Balanced DigitalOcean setup"
date: '2016-12-25T23:42:35-03:00'
category: webclip
summary: 'The post walks through deploying a Phoenix app on DigitalOcean with Postgres, HAProxy, and two Phoenix nodes, stressing Erlang clustering, release-based deployment, and the limits of PaaS for this setup.'
tags: ["deployment", "elixir", "phoenix", "digitalocean"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Phoenix App deployed into a Load Balanced DigitalOcean setup | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2016/12/23/elixir-phoenix-app-deployed-into-a-load-balanced-digitalocean-setup"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-12/akitaonrails-com--elixir-phoenix-load-balanced-digitalocean-setup.md"
    kind: repo
---

The post explains a load-balanced Phoenix deployment on DigitalOcean built around Erlang clustering, a separate PostgreSQL server, and HAProxy in front of two Phoenix nodes. It argues that Phoenix makes WebSocket broadcasts across nodes straightforward, but that this kind of setup needs more infrastructure control than Heroku-style PaaS offers.

## Reading notes

- Phoenix and Erlang make clustered WebSocket apps easier because nodes can broadcast across instances without special application code.
- The example uses four droplets: one PostgreSQL server, one HAProxy server, and two Phoenix servers in different regions.
- The Ubuntu setup includes locale configuration, a sudo user, SSH key setup, a swap file, unattended upgrades, Elixir, and Node.js.
- PostgreSQL is configured with a role matching the app user, a database with the same name, and access limited to the Phoenix server IPs, although the article notes this is still insecure.
- HAProxy is set to round-robin between the two Phoenix servers and needs `option http-server-close` for WebSockets.
- Phoenix production config must hardcode the public host, port 8080, and `:serve_endpoints, true`.
- The release workflow uses `distillery` and `edeliver`, with a `.deliver/config` file that defines build and production hosts and a custom hook for `prod.secret.exs`.
- The article says passphrase-protected SSH keys make deployment painful, especially on Mac, where it suggests an `ssh-askpass` helper.
- Each Phoenix server needs `vm.args`, a per-host Erlang config file, and `prod.secret.exs` in the home directory.
- First deployments are slow because edeliver fetches dependencies, compiles, runs npm, builds assets, creates a release, and copies it to the servers.
- Troubleshooting advice includes running Phoenix locally in prod mode with debug logging, checking controller code that behaves differently in production, and making sure Guardian and Ecto migrations are configured and run.
- The conclusion says the setup works, but deployment is slow and some login or redirect issues may still come from Coherence, ExAdmin, Phoenix, or HAProxy.
