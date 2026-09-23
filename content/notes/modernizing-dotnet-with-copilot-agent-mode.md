---
title: "A step-by-step guide to modernizing .NET applications with GitHub Copilot agent mode"
date: "2026-09-23T15:49:37+01:00"
category: webclip
summary: "Microsoft's guide walks through GitHub Copilot app modernization in Visual Studio 2026: an agent that assesses a .NET codebase, drafts an editable upgrade plan, and applies changes in a fix-and-test loop."
tags:
  - dotnet
  - github-copilot
  - legacy-modernization
  - azure
has_commentary: false
sources:
  - title: "A step-by-step guide to modernizing .NET applications with GitHub Copilot agent mode - .NET Blog"
    url: "https://devblogs.microsoft.com/dotnet/modernizing-dotnet-with-github-copilot-agent-mode/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-08/devblogs-microsoft-com--modernizing-dotnet-with-github-copilot-agent-mode.md"
    kind: repo
---

In Visual Studio 2026, GitHub Copilot app modernization runs an upgrade or Azure migration as an agent session instead of a manual version bump. The agent produces three files as it works: an assessment.md report of outdated packages and breaking changes, an editable plan.md with the proposed upgrade steps, and a tasks.md log that tracks each step as it executes.

Human approval happens at plan.md: only after that file is reviewed does the agent apply any change. If it hits an error it can't resolve, it stops and asks for input instead of guessing.

## Fichamento

- Two entry points start a session: right-click the project in Solution Explorer and choose Modernize, or type `@modernize` in Copilot Chat.
- The assessment stage lists outdated NuGet packages with recommended target versions, project count and upgrade complexity, and an API analysis of potential breaking changes, before anything is touched.
- The plan.md file is fully editable: you can add context, reorder steps, or exclude specific projects before approving the upgrade.
- During execution, Copilot runs a fix-and-test loop on build errors and commits major changes to Git as it goes, so each step is a separate, revertible commit.
- The Azure migration path runs the same assess-plan-execute structure: a cloud readiness scan for framework compatibility and identity gaps, an editable migration plan, then automated CVE scans and safe version replacements before deployment.
- The final deployment step provisions resources, configures monitoring and logging, and secures identities without hand-written infrastructure scripts.
