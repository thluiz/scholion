---
title: "Private Nuget feed in Docker .Net Core application"
date: '2022-04-05T18:36:54-03:00'
category: webclip
summary: 'The post explains why private NuGet feeds fail in Docker, how to pass a NuGet.config file, how to fix an SSL handshake issue, and how PAT-based authentication made the feed work.'
tags: ["docker", "nuget", "dotnet-core", "authentication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Private Nuget feed in Docker .Net Core application"
    url: "https://www.softwaredeveloper.blog/private-nuget-feed-in-docker"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/softwaredeveloper-blog--private-nuget-feed-in-docker-dotnet-core-application.md"
    kind: repo
---

The post describes the main obstacles to using a private NuGet feed inside Docker for a .NET Core app. It says Windows credentials are available on the host, but they are not accessible in Docker, so another authentication method is needed.

It then walks through the fixes the author used: passing a NuGet.config file to dotnet restore and publish, setting DOTNET_SYSTEM_NET_HTTP_USESOCKETSHTTPHANDLER=0 to solve an SSL connection error, and switching to a personal access token when basic credentials still returned 401 Unauthorized. As a temporary fallback, it mentions using a local NuGet feed.

## Reading notes

- Private NuGet feeds can fail in Docker because host credentials are not available inside the container.
- A NuGet.config file can be passed in the Dockerfile with --configfile.
- The config file should be stored at solution level and copied or referenced with the correct path.
- An SSL handshake error was fixed by setting DOTNET_SYSTEM_NET_HTTP_USESOCKETSHTTPHANDLER=0 before dotnet publish.
- A 401 Unauthorized error remained after that step.
- The feed started working after replacing the credentials with a personal access token.
- The token was placed in both Username and ClearTextPassword.
- The token may be valid for up to one year.
- A local NuGet feed is presented as a last resort, but it requires manual maintenance or automation.
