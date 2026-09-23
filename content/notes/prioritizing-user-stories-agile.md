---
title: "Prioritizing user stories in agile product management"
date: "2026-09-23T19:15:20+01:00"
category: webclip
has_commentary: false
summary: "Walks through MoSCoW and RICE as the two dominant methods for prioritizing a product backlog, and argues each fits a different stage of a product's life."
tags:
  - product-management
  - agile
  - prioritization
sources:
  - title: "Prioritizing user stories in agile product management - LogRocket Blog"
    url: "https://blog.logrocket.com/product-management/prioritize-user-stories-agile/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-logrocket-com--prioritizing-user-stories-agile.md"
    kind: repo
---

MoSCoW, created by Dai Clegg at Oracle in the early 2000s, sorts stories into must have, should have, could have, and won't have. RICE, built by Intercom for its own roadmap, scores each story numerically on reach, impact, confidence, and effort, then multiplies the first three and divides by the fourth. The piece treats these as answers to different problems rather than competing solutions to the same one: MoSCoW needs no user data and suits a product that doesn't have any yet, RICE needs real usage numbers and suits a product that's already live.

Each method carries its own failure mode. MoSCoW breaks when too many stories get labeled must have, since a backlog that's all top priority makes deadlines impossible; the piece recommends aiming for an even split across the four categories instead. RICE breaks on bad inputs, particularly the impact score, since it forces a number onto something that's closer to a gut feeling, and Intercom's own confidence variable exists specifically to flag when that number shouldn't be trusted.

## Fichamento

- MoSCoW's must-have test is a checklist, not a gut call: is the story replaceable, is there a workaround, is the product meaningful or safe without it, does it solve the customer's problem without it.
- The "won't have" category in MoSCoW isn't a rejection. It just means the team lacks time or resources right now, and a story there can move up if its importance later increases.
- RICE's reach score requires picking a fixed time window (monthly, quarterly, yearly) before comparing stories, since raw user counts across different intervals aren't comparable.
- For a pre-launch product with no usage data, the piece suggests substituting customer surveys, existing market or competitor analysis, and prior research for the real numbers RICE normally needs.
- RICE's impact and confidence scores are both deliberately bucketed into a small set of fixed values (impact 1-5, confidence at 100/80/50 percent) rather than left as free numbers, specifically to keep teams from over-precision on numbers they can't actually justify.
