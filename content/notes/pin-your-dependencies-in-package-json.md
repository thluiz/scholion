---
title: "Pin your dependencies in package.json"
date: '2026-09-25T21:34:14+01:00'
category: webclip
summary: 'The page explains how dependency version ranges work in package.json and argues for exact versions to keep JavaScript projects consistent, reliable, and safer across environments.'
tags: ["package-json", "dependencies", "version-pinning", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pin your dependencies in package.json"
    url: "https://thetshaped.dev/p/pin-your-dependencies-in-packagejson"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/thetshaped-dev--pin-your-dependencies-in-package-json.md"
    kind: repo
---

The page says package.json is central in JavaScript projects because it defines the external packages the project relies on. It explains four dependency versioning styles and shows that exact versions avoid ambiguity across installs and environments.

It argues that pinning dependencies improves consistency, reliability, and security, while reducing surprises from automatic updates. It also recommends using Renovate, Dependabot, npm audit, Snyk, and lockfiles like package-lock.json or yarn.lock to keep dependencies controlled.

## Reading notes

- package.json defines the project’s dependencies in Node.js, npm, and yarn projects.
- Version ranges can allow minor, patch, or major updates automatically, depending on the syntax used.
- Pinning dependencies means specifying exact versions instead of ranges such as `^`, `~`, or `>=`.
- Exact versions help every environment install the same modules.
- Pinning is presented as a way to reduce “it works on my machine” issues.
- Exact versions are linked to fewer surprises from updates that introduce bugs or break functionality.
- Pinning is also presented as a security measure against automatic updates to vulnerable or compromised code.
- The page notes that pinning creates maintenance overhead because dependencies still need regular review and updates.
- It recommends automation tools like Renovate and Dependabot to open pull requests for updates.
- It recommends tests because automatic update PRs can be merged when checks pass.
- It mentions npm audit and Snyk for detecting vulnerabilities and suggesting or applying patches.
- It says package-lock.json and yarn.lock enforce the exact versions recorded in the last successful installation.
