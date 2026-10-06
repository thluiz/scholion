---
title: "DigitalOcean Backups and Snapshots Explained"
date: '2015-05-01T13:29:41-03:00'
category: webclip
summary: 'DigitalOcean distinguishes manual snapshots from weekly automated backups, notes that snapshots shut down the server while backups run in the background, and explains pricing, storage, and common uses.'
tags: ["digitalocean", "backups", "snapshots"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DigitalOcean Backups and Snapshots Explained | DigitalOcean"
    url: "https://www.digitalocean.com/community/tutorials/digitalocean-backups-and-snapshots-explained"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/digitalocean-com--digitalocean-backups-and-snapshots-explained.md"
    kind: repo
---

DigitalOcean offers snapshots and backups as two ways to save and restore data, duplicate configurations, and scale servers. The page also warns that automated backups on a server with an active database can be incomplete, so database exports such as mysqldump or pg_dump are suggested.

## Reading notes

- Snapshots can be generated manually and enabled at any time, while backups run automatically weekly and must be enabled during droplet creation.
- The server shuts down during snapshots, but stays powered on during backups, which run in the background.
- Both snapshots and backups are stored on hardware separate from the droplet resources.
- Backups cost 20% of the virtual server price, with the charge based on at least four successful backups per month.
- Snapshots cost $0.02 per GB of snapshot storage per month.
- Snapshots can be used to scale out a system by spinning up a new droplet from a current server image.
- Snapshots can also support occasional usage by letting you delete a droplet and restore it later from the saved image.
- A snapshot can be taken before drastic configuration changes so there is a version to revert to if the changes fail.
