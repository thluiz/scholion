---
title: "AI Needs Game Designers - David Kaye's Essays"
date: "2026-09-23T16:24:00+01:00"
category: webclip
summary: "David Kaye argues that running dozens of Claude Code agents in parallel is the same skill RTS players trained for years: attention allocation, not speed, and game designers already solved the interface for it."
tags:
  - ai-agents
  - claude-code
  - game-design
  - orchestration
has_commentary: false
sources:
  - title: "AI Needs Game Designers - David Kaye's Essays"
    url: "https://blog.davidkaye.co/p/ai-needs-game-designers"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-01/blog-davidkaye-co--ai-needs-game-designers.md"
    kind: repo
---

Steve Yegge's Gas Town runs 20-30 Claude Code instances in parallel under a human "Overseer." RTS players have spent decades managing exactly that kind of parallel, semi-autonomous system, and Kaye treats the two as the same problem. Gas Town assigns agents roles like The Mayor, Polecats and Refinery, and routes work through "convoys" that start, execute and land without the human present. The transferable skill is attention allocation across many running processes, not speed on any one of them. Competitive StarCraft and Factorio players already trained for years in what we now call agent orchestration.

For Kaye, the gap is the interface. There's no way to monitor and intervene across many agents without reading everything each one produces. Gas Town currently runs on tmux, and Yegge tells users they'll have to learn it or wait for someone to build a better UI. Kaye points to StarCraft 2's control groups, minimaps and alert systems as thirty years of R&D on that same problem, letting one person direct many autonomous agents without reading every line each one produces. His conclusion is that game designers are best positioned to design that interface.

## Reading notes

- Gas Town runs 20-30 Claude Code instances at once, assigning them roles (Mayor, Polecats, Refinery, Witness) and routing work through "convoys" that start, execute and land without a human present.
- Kaye maps RTS skills directly onto agent orchestration: parallel attention management (watching everything, intervening selectively), and systems that run without the operator, the way Factorio factories and StarCraft economies keep producing unattended.
- Pro RTS players sustain 300+ actions per minute; Kaye frames the transferable skill as attention allocation, knowing when to check an expansion versus when to trust units to handle themselves.
- Gas Town's current interface is tmux; Yegge himself frames this as a stopgap, waiting for "someone to write a better UI."
- Shopify CEO Tobi Lütke lets employees expense Factorio and calls StarCraft "a good teaching tool for tech workers," which Kaye cites as evidence the game-to-work pipeline already has executive buy-in.
- Kaye reverses the usual framing. AI orchestration is the one that needs what game designers already know about making multi-agent systems legible.
