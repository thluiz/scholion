---
title: "Restore NuGet Packages from a Private Feed when building Docker Containers"
date: '2022-04-05T18:36:34-03:00'
category: webclip
summary: 'The post explains how to create an access token for a private Azure DevOps NuGet feed and pass it into a Dockerfile so Docker image builds can restore packages from that feed.'
tags: ["nuget", "docker", "azure-devops"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Restore NuGet Packages from a Private Feed when building Docker Containers | Programming With Wolfgang"
    url: "https://www.programmingwithwolfgang.com/restore-nuget-inside-docker/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/programmingwithwolfgang-com--restore-nuget-packages-from-private-feed-docker.md"
    kind: repo
---

The post explains how to create an access token for a private Azure DevOps NuGet feed and pass it into a Dockerfile so Docker image builds can restore packages from that feed.

## Reading notes

- It focuses on creating an access token for a private Azure DevOps NuGet feed.
- It then shows how to pass that token to a Dockerfile during image builds.
- The goal is to make NuGet package restore work inside Docker containers.
