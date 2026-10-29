---
title: "Replacing Pingdom with Ruby and Heroku"
date: '2016-02-07T22:27:37-03:00'
category: webclip
summary: 'The post explains how to replace Pingdom with a self-hosted uptime checker built with Ruby, run it on Heroku for $7/month, and configure notifications and checks through a YAML file.'
tags: ["ruby", "heroku", "uptime-monitoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Replacing Pingdom with Ruby and Heroku"
    url: "http://nandovieira.com/replacing-pingdom-with-ruby-and-heroku"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/nandovieira-com--replacing-pingdom-with-ruby-and-heroku.md"
    kind: repo
---

The post describes how to replace Pingdom after its starting plan rose from $10 to $14. The suggested setup uses `uptime_checker`, a Ruby project with fewer than 500 lines, deployed on Heroku for $7 per month.

## Reading notes

- The tool checks defined URLs every 30 seconds by default and can verify both the expected status code and whether the response body contains a string.
- It supports multiple notification channels, including Telegram, Twitter direct message, e-mail, Slack, and Hipchat.
- Setup starts by forking the repository, cloning it, creating a branch, and copying `checkers.yml.sample` to `checkers.yml`.
- The `checkers.yml` file defines monitored sites and supports ERB for dynamic values.
- A shared block can be used to avoid repeating notifier settings across multiple sites.
- The checks can expect a 200 status code or a specific string in the response.
- Deployment on Heroku requires creating an app, adding Redis, and adding Sendgrid for e-mail notifications.
- The example uses a `NOTI_FNANDO` environment variable for Noti notifications.
- The app is deployed by pushing the `personal` branch to Heroku’s `master` branch.
- To run it continuously on Heroku, the worker is scaled up and set to hobby dyno type.
- Logs can be viewed with `heroku logs --tail`.
- The post also describes a workflow for keeping the Heroku deployment aligned with `master` by rebasing `personal` onto `master` and force-pushing again.
- If Heroku is not used, the author says the app can also be deployed to a VPS, but does not detail that setup.
