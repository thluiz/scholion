---
title: "Bring your own machine to Visual Studio Online"
date: '2026-11-16T19:42:18+00:00'
category: webclip
summary: 'Visual Studio Online now lets you register your own machines and access them remotely from VS Code or the web editor, with CLI support for headless scenarios and a simpler one-click registration flow.'
tags: ["visual-studio-online", "visual-studio-code", "cli", "self-hosted-environment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bring your own machine to Visual Studio Online"
    url: "https://msft.it/6018T5nW0"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/msft-it--bring-your-own-machine-to-visual-studio-online.md"
    kind: repo
---

Visual Studio Online can use self-hosted machines as remote development environments, not only fully managed cloud environments. The post says this helps developers connect an already configured work or home machine, or use specialized hardware that is not currently supported in the cloud.

The update adds a CLI preview for registering machines in server and headless OS scenarios on macOS, Linux, and Windows, with installation paths through Homebrew, APT, and a Windows script. It also updates the Visual Studio Code extension so users can register a self-hosted environment from the Visual Studio Online viewlet or the command palette with one click.

## Reading notes

- Visual Studio Online now supports registering your own machine and accessing it remotely from Visual Studio Code or the web editor.
- This is presented as useful for developers who want to connect an existing work or home machine for anywhere access.
- It also supports cases where specialized hardware is needed and not currently supported.
- The CLI preview expands registration to server and headless OS scenarios across macOS, Linux, and Windows.
- The CLI is published to Homebrew and APT, and a Windows installation script is provided.
- After installing the CLI, `vso start` registers the machine and lets the user select a plan in the current region.
- Visual Studio Code now includes a one-click command, “Register self-hosted environment…”, in the Visual Studio Online viewlet.
- The same registration command is still available from the command palette.
- The post points readers to the docs and to the GitHub page for feedback or issues.
