---
title: "Optimizing for Free Hosting — Elixir Deployments"
date: '2021-02-08T07:59:44-03:00'
category: webclip
summary: 'The article lays out a single-server Phoenix deployment on free Google Cloud hardware, using raw Linux tools, Nginx, systemd, releases, and a bash script to achieve simple, low-cost, zero-downtime deploys.'
tags: ["elixir", "phoenix", "deployment", "google-cloud"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Optimizing for Free Hosting — Elixir Deployments | by Damon Janis | Medium"
    url: "https://damonvjanis.medium.com/optimizing-for-free-hosting-elixir-deployments-6bfc119a1f44"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/damonvjanis-medium-com--optimizing-for-free-hosting-elixir-deployments.md"
    kind: repo
---

The article proposes a free-to-start deployment path for a Phoenix app on a single Google Cloud Compute Engine instance. It emphasizes low cost, full control, simple infrastructure, and zero-downtime releases without hot code upgrading, using built-in Linux tools instead of heavier deployment stacks.

## Reading notes

- The setup targets a free Google Cloud VM, with a static IP, DNS records, SSH access, swap space, Erlang, Elixir, Node, and Postgres installed manually.
- The author argues that simple server and deployment processes reduce downtime more than rare hardware failure does, as long as the database is backed up.
- Postgres is opened for remote access, with firewall and configuration changes so the database can be reached from a development machine.
- The app code is cloned from a Git repository, and secrets are copied to the server with `scp`.
- Nginx and Certbot are installed to provide SSL and reverse proxying to Phoenix.
- Zero-downtime deployment is achieved by starting a new release on the unused port while the old one still serves traffic, then reloading Nginx to switch over.
- A bash deploy script runs updates, tests, asset compilation, release creation, migrations, and port switching.
- `systemd` services keep the app running after crashes or reboots and route logs to `journald`.
- `journalctl` is used to follow logs, and `journald` is configured to limit log disk usage.
- The bonuses cover automated backups to another free instance and a rollback script for previous releases.
