---
title: "Faster web application deployments using Mina instead of Capistrano"
date: '2014-03-16T18:39:46-03:00'
category: webclip
summary: 'The page compares Capistrano and Mina for Rails deployments and argues that Mina is much faster because it runs the deployment as one Bash script over a single SSH session.'
tags: ["mina", "capistrano", "rails-deployment", "ssh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Faster web application deployments using Mina instead of Capistrano — Infinum"
    url: "https://www.infinum.co/the-capsized-eight/articles/faster-web-application-deployments-using-mina-instead-of-capistrano"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/infinum-co--faster-web-application-deployments-using-mina-instead-of-cap.md"
    kind: repo
---

The page compares Capistrano and Mina for deploying Ruby on Rails applications to VPS or dedicated servers. It says Capistrano works, but deployment can take several minutes, while Mina was faster in the author’s tests and replaced Capistrano in their toolset.

## Reading notes

- Capistrano is described as a common deployment tool, but slow enough to be a problem for teams that deploy every day.
- Mina drew attention after the authors saw that 13% of RailsRumble teams used it.
- For a new Rails project, Capistrano required adding gems, editing several files, and running `cap production deploy`.
- In the test, Capistrano took 180 seconds for the deployment.
- Mina required adding `gem 'mina'`, running `mina init`, editing `deploy.rb`, then running `mina setup` and `mina deploy`.
- Mina setup took 1 second to create the needed directories.
- The first Mina deploy took 85 seconds.
- On subsequent deploys, `assets:precompile` and `db:migrate` are skipped unless assets or database changes require them, and `bundle` only downloads new gems.
- On a small project, Mina is said to be 6.8 times faster than Capistrano.
- On the author’s larger web application, Mina was about 28 times faster than Capistrano on the second deploy.
- The speed difference is explained by Capistrano running each command in its own SSH session, while Mina generates one Bash script, uploads it, and runs it on the server.
- Mina is presented as easier to set up and clearer in console output, but it does not support rollback yet.
