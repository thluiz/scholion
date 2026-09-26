---
title: "Deploying a asp.net core container with Zeit \"now\""
date: '2026-09-27T00:29:11+01:00'
category: webclip
summary: 'The post shows how to deploy a sample ASP.NET Core Web API with Zeit now by adding a Dockerfile, installing the CLI, and running `now`, while noting the free-plan file-size limit and its workarounds.'
tags: ["aspnet-core", "docker", "zeit-now", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Deploying a asp.net core container with Zeit \"now\""
    url: "https://dev.to/schwamster/deploying-a-aspnet-core-container-with-zeit-now"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--deploying-aspnet-core-container-with-zeit-now.md"
    kind: repo
---

The post walks through deploying a sample ASP.NET Core Web API with Zeit now. It starts from a fresh `dotnet new webapi` project, adds a Dockerfile and `.dockerignore`, installs the `now` CLI with npm, and deploys by running `now`.

It also describes a free-plan limitation in which files in the container build context cannot exceed 1 MB, which blocks a compiled-runtime approach. The author lists three workarounds: use the build image, remove the large files, or build and push an image to a registry before deploying. The post ends by recommending now for its simplicity while noting interest in how its web-app-focused constraints affect real projects.

## Reading notes

- Create a sample Web API with `dotnet new webapi`, confirm it runs locally, and expose the default `/api/values` endpoint.
- Use a Dockerfile based on `microsoft/aspnetcore-build`, expose port 80, copy the source into the container, restore dependencies, and run the app.
- Add `.dockerignore` so `bin` and `obj` stay out of the build context.
- The free plan has a 1 MB limit for individual files in the build context, which makes a compiled runtime-image approach fail for this project.
- The post lists three ways around that limit: use the build image, remove large runtime-irrelevant files, or build and push an image to a registry first.
- Install now with `npm install -g now` and deploy by running `now`, then follow the prompts and email registration if needed.
- Each deployment gets a new URL, and aliases or custom domains can point to chosen deployments.
- The author recommends now despite the file-size restriction and wants to test how its web-app-only model fits future projects.
