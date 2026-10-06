---
title: "How to backup your Linode or Digital Ocean VPS to Amazon S3"
date: '2015-05-01T21:14:20-03:00'
category: webclip
summary: 'Explains how to set up an offsite backup for a VPS using Amazon S3, s3cmd, and a weekly cron job, so server files and package lists are copied outside the hosting provider.'
tags: ["amazon-s3", "vps-backup", "s3cmd", "cron"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to backup your Linode or Digital Ocean VPS to Amazon S3"
    url: "https://levels.io/backup-linode-digital-ocean-vps-amazon-s3/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/levels-io--how-to-backup-linode-digital-ocean-vps-to-amazon-s3.md"
    kind: repo
---

The post describes a simple offsite backup setup for a Linode or Digital Ocean VPS. It uses Amazon S3 as the storage target, argues for keeping backups outside the hosting company, and points out that s3cmd can upload selected server directories and package lists on a schedule.

## Reading notes

- It recommends creating an S3 bucket in a chosen region and saving the access key and secret key needed by the VPS.
- It suggests giving the server access to the whole AWS account if the account only contains that bucket, while warning that this is unsafe for accounts with other resources.
- It uses s3cmd on the VPS to connect to S3 and set an encryption password during configuration.
- It shows syncing important directories such as /srv, /etc, /home, and /var instead of copying the entire Linux installation.
- It also backs up the installed package list with dpkg --get-selections.
- It wraps the upload commands in a shell script and schedules that script with cron to run weekly.
- It notes that s3cmd also runs on OSX, so the same approach can be used to back up a Mac to S3.
