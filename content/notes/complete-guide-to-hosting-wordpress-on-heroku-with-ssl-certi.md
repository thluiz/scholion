---
title: "Complete Guide To Hosting Wordpress On Heroku With SSL Certification"
date: '2020-07-05T14:10:41+00:00'
category: webclip
summary: 'The guide explains how to move a self-hosted WordPress site to Heroku, connect a custom domain through Cloudflare, handle HTTPS, manage updates and plugins, and avoid sleep on the free plan.'
tags: ["wordpress", "heroku", "cloudflare", "ssl"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Complete Guide To Hosting Wordpress On Heroku With SSL Certification"
    url: "https://dev.to/aryaziai/complete-guide-to-hosting-wordpress-on-heroku-with-ssl-certification-4f2l"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--complete-guide-to-hosting-wordpress-on-heroku-with-ssl-certi.md"
    kind: repo
---

The guide says a self-hosted WordPress site can run on Heroku at no monthly cost, aside from annual domain fees. It warns about a 5MB database limit, the need to update WordPress through Composer, and the need to add themes and plugins manually before pushing changes.

## Reading notes

- Create a Heroku account, choose PHP, and add a credit card so WordPress can be installed and the free dyno hours can increase.
- Use Philipp Heuer’s wordpress-heroku repository and the Deploy to Heroku button as the base setup.
- Clone the Heroku app repo locally, merge in wordpress-heroku, then commit and push.
- Set up Cloudflare, change nameservers at the registrar, and wait for propagation.
- Optionally add Cloudflare page rules for HTTPS, www redirection, and caching.
- Add the custom domain in Heroku without www or https, then copy the DNS target into Cloudflare.
- Update WordPress by changing the johnpbloch/wordpress version in composer.json and running composer update.
- Add or remove plugins and themes inside /web/app, then unzip them into the Theme and Plugin folders before pushing.
- Use Cloudflare Flexible SSL if login or HTTPS problems appear, and replace http with https in config/application.php when needed.
- Manage the database with MySQL Workbench or WP Optimize, especially to keep the database size under control.
- Use WP Offload Media Lite and AWS S3 for uploads, since pushing code overwrites the uploads folder.
- For debugging, use the Heroku app URL instead of the custom domain, and check config/application.php rather than wp-config.
- Disable redis-cache if it causes problems by removing its lines from composer.json and its mu-plugin file.
- Keep the app awake on the free plan by scheduling a Cron-job.org request every 30 minutes.
