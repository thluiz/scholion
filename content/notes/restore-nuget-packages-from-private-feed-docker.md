---
title: "Restore NuGet Packages from a Private Feed when building Docker Containers"
date: '2022-04-05T18:36:34-03:00'
category: webclip
summary: 'The post explains why restoring a private Azure DevOps NuGet feed works in Visual Studio but fails inside Docker, and shows how to use a PAT in nuget.config and Docker build arguments to restore packages locally and in the pipeline.'
tags: ["nuget", "docker", "azure-devops", "personal-access-token"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Restore NuGet Packages from a Private Feed when building Docker Containers"
    url: "https://www.programmingwithwolfgang.com/restore-nuget-inside-docker/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/programmingwithwolfgang-com--restore-nuget-packages-from-private-feed-docker.md"
    kind: repo
---

The post explains that a private NuGet feed can be restored in Visual Studio but fails during a Docker image build with a 401 Unauthorized error because the build does not have access to the feed. It then shows how to create a personal access token in Azure DevOps, keep it out of source control, and pass it into the Docker build so the image can restore private packages.

## Reading notes

- A private NuGet feed restored in Visual Studio can fail in Docker with a 401 Unauthorized error.
- The article uses a Personal Access Token in Azure DevOps with Packaging read scope.
- The PAT is copied once and cannot be viewed again after the token window is closed.
- A nuget.config file is added to the project root with nuget.org and the private feed URLs.
- The PAT is not committed in nuget.config because the file goes to source control.
- Docker build arguments are used to pass the PAT into the Dockerfile.
- The Dockerfile inserts the PAT and a username into nuget.config.
- The Dockerfile copies nuget.config into the image and uses --configfile during dotnet restore.
- The pipeline stores the PAT in a secret variable.
- The Docker build task passes the secret variable as a build argument.
- With the PAT passed this way, the pipeline can restore private NuGet packages successfully.
