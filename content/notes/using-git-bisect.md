---
title: "Using git bisect"
date: '2017-04-24T09:47:55-03:00'
category: webclip
summary: 'The article explains how git bisect narrows a commit range to find the first bad commit, using a checkout bug as a real-world example of marking commits good and bad.'
tags: ["git", "git-bisect", "debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using git bisect"
    url: "https://dev.to/gonedark/using-git-bisect"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-04/dev-to--using-git-bisect.md"
    kind: repo
---

The article uses a checkout bug as the example for git bisect. The bug appeared in a live page while the same Stripe Checkout code worked on a fresh page, so the problem was in the author's code rather than in Stripe.

It explains the basic workflow: start the bisect, mark a known bad commit, mark a known good commit, then test each commit that git bisect selects until it identifies the first bad one. In the example, that commit contained JavaScript that listened for click events and prevented the default behavior, which blocked the checkout form from opening.

## Reading notes

- git bisect is used when you know one commit where a bug exists and another where it does not.
- The command moves through the commit range and asks you to classify each tested commit as good or bad.
- The author found a bug in checkout behavior by using a known working commit from earlier history.
- In the case described, the introduced change was JavaScript that prevented the checkout form from launching.
- The article presents git bisect as a practical way to locate regressions in commit history.
