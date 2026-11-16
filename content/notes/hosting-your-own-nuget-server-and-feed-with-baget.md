---
title: "Hosting your own NuGet Server and Feed for build artifacts with BaGet"
date: '2020-02-22T12:11:42+00:00'
category: webclip
summary: 'The page surveys NuGet server options and argues that BaGet is a strong cross-platform choice, especially for private feeds, read-through caching, and simple self-hosted artifact storage.'
tags: ["nuget", "baget", "build-artifacts", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hosting your own NuGet Server and Feed for build artifacts with BaGet"
    url: "https://hanselman.com/blog/HostingYourOwnNuGetServerAndFeedForBuildArtifactsWithBaGet.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hanselman-com--hosting-your-own-nuget-server-and-feed-with-baget.md"
    kind: repo
---

The page reviews the NuGet ecosystem and lists several ways to host or browse feeds, from Artifactory, GitHub Packages, Azure Artifacts, and MyGet to static feeds like Sleet. It presents BaGet as a favorite option because it is open source, cross-platform, written in ASP.NET Core 3.1, and can run in cloud, Docker, or behind IIS.

## Reading notes

- NuGet is the package management system for .NET, and there are alternatives to nuget.org, including other servers and clients.
- Team setups can use private NuGet feeds so one team publishes packages for others to consume.
- FuGet offers a different way to browse NuGet packages.
- Artifactory can store many artifact types and can act as an internal cache for nuget.org.
- NuGet Gallery is open source, so you can run your own copy of the nuget.org website.
- NuGet.Server is lightweight but limited, and the page suggests BaGet instead.
- GitHub Packages and Azure Artifacts are SaaS options for NuGet packages.
- MyGet can host many package types and is known for license compliance features.
- Sleet generates static NuGet v3 feeds that can be hosted on Azure Storage or Amazon S3.
- LiGet is described as a NuGet server with a Linux-first approach.
- BaGet is highlighted as cross-platform, open source, and suitable for Azure, AWS, Google Cloud, IIS, or Docker.
- BaGet supports read-through caching, which can speed up restores from nuget.org and help with offline restores.
- The page describes BaGet as a way to place a private caching layer in front of developers.
- BaGet can be started quickly with Docker or without Docker by installing the .NET Core SDK, downloading a release, running dotnet BaGet.dll, and opening localhost:5000.
- The page notes that some BaGet documentation is incomplete and points to open issues labeled as good first issue.
