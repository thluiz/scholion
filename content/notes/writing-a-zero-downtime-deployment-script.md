---
title: "Writing a Zero Downtime Deployment Script"
date: '2017-06-11T18:52:07-03:00'
category: webclip
summary: 'The post explains how to build a shell script that clones a repository into a timestamped deploy directory, flips a symbolic link to the new release, and can run the process over SSH.'
tags: ["shell-script", "zero-downtime", "deployment", "ssh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing a Zero Downtime Deployment Script"
    url: "https://dev.to/timacdonald/writing-a-zero-downtime-deployment-script"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/dev-to--writing-a-zero-downtime-deployment-script.md"
    kind: repo
---

The post describes building a shell script called FlipIt™ to deploy a site with zero downtime. It creates a timestamped deployment directory, clones the Git repository into it, and then switches the server’s public directory to the new release with a symbolic link.

It also shows how to turn those commands into a reusable script with arguments, run it locally, and have it execute on a remote server over SSH. The article notes that extra commands like composer install can run before the link switch, and it mentions possible future additions like rollback, init, and cleanup.

## Reading notes

- The author writes the deployment flow as a shell script after becoming more comfortable with terminal commands.
- Zero downtime comes from keeping the previous site active while the new version is prepared.
- The deployment directory uses Unix time so each release folder has a unique, ordered name.
- The repository is cloned into the new deployment directory instead of using git pull on the live copy.
- The public server directory is linked to the deployed release with ln -s -n -f.
- The script accepts arguments for the server public directory, repository URL, and repository public directory.
- A shebang line identifies the file as a shell script.
- The script can be wrapped in an SSH heredoc so it runs on a remote server.
- The post says this setup works for the author’s own environment but may differ on other servers.
- The notes mention that old deploys are not cleaned up automatically.
- The update recommends git clone --depth 1 to download only the latest version of the files.
