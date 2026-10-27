---
title: "HowTo: Easily integrate a (SSH secured) GIT repository into Redmine"
date: '2014-01-06T08:05:27-03:00'
category: webclip
summary: 'This how-to explains how to clone a Git repository as a mirror, register it in Redmine, and keep it updated with a cron job so Redmine can show commits and repository trees.'
tags: ["redmine", "git", "ssh", "cron"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "HowTo Easily integrate a (SSH secured) GIT repository into redmine - Redmine"
    url: "http://www.redmine.org/projects/redmine/wiki/HowTo_Easily_integrate_a_%28SSH_secured%29_GIT_repository_into_redmine"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-01/redmine-org--howto-easily-integrate-ssh-secured-git-repository-into-redmi.md"
    kind: repo
---

This how-to shows how to connect a Git repository to a Redmine project and keep it up to date. It assumes SSH access to the repository, a local directory for the clone, and a Redmine installation that can find the Git binaries.

## Reading notes

- The repository should be cloned as a mirror, not as a bare repository, because Redmine only needs the commit information.
- The example uses the Redmine owner user `redmine`, a local path under `/var/lib/redmine/repos/`, and a remote repository at `git@...:my_repo`.
- After cloning, the repository must be added in Redmine under administration or project settings, with type set to GIT and the absolute local path filled in.
- Opening the repository dialog makes Redmine fetch changesets between the local repository and the Redmine database, which can take a long time for large repositories.
- Opening that dialog does not fetch new commits from Git itself, so Redmine will not show fresh commits unless the local repository is updated separately.
- To keep the repository current, the text recommends a cron job for the Redmine user that runs `git fetch --all` every five minutes.
- If several repositories are cloned, each one needs its own crontab entry.
