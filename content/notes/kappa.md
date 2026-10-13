---
title: "Kappa"
date: '2013-11-11T09:58:32-03:00'
category: webclip
summary: 'Kappa is a smart npm proxy for enterprises that need private modules without mirroring the full public registry. It fetches public and private packages from the right place and serves them transparently.'
tags: ["npm-proxy", "private-modules", "enterprise"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "nearForm NodeCrunch"
    url: "http://www.nearform.com/nodecrunch/?p=109"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/nearform-com--kappa.md"
    kind: repo
---

Kappa is presented as a smart npm proxy for enterprises that need to deploy private modules efficiently. The page says existing solutions often require replicating the entire public npm registry just to deploy a few private packages.

It says Kappa fetches public and private npm packages from the right place, so a company can keep a private npm server that only stores its own modules. It also says future support will include licensing checks, blacklisting, statistics, and more.

## Reading notes

- Solves the problem of deploying private modules without copying the whole public npm registry.
- Routes public and private npm packages from the correct source.
- Lets companies keep a private npm server limited to their own modules.
- Plans to add licensing checks, blacklisting, and statistics.
