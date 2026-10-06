---
title: "Coding tricks of game developers"
date: '2012-03-17T03:36:50-03:00'
category: webclip
summary: 'A collection of game-dev anecdotes about deadline pressure, memory and performance hacks, and pragmatic workarounds that kept projects moving when shipping was close.'
tags: ["game-development", "optimization", "debugging", "workarounds"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dodgy Coder: Coding tricks of game developers"
    url: "http://www.dodgycoder.net/2012/02/coding-tricks-of-game-developers.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/dodgycoder-net--coding-tricks-of-game-developers.md"
    kind: repo
---

The page collects anecdotes and tips about coding under deadline pressure in game development. It shows how teams save memory, improve cache use, avoid costly branches, and sometimes ship with hacks that turn bugs into features or hide them just enough to meet release.

## Reading notes

- Game developers often work under crunch near release, so quick and dirty fixes become common when deadlines threaten the project.
- One team kept a two-megabyte memory buffer reserved early so it could be deleted later if the game went over budget.
- Tight loops should keep data small and contiguous so the CPU can load several iterations into cache at once.
- Some developers set specific times for email, Twitter, and breaks so the browser does not become a constant distraction.
- A camera bug was caused by inheritance from a damageable physical object, so air strikes were effectively killing the camera.
- A level bug where movement only worked along walls was turned into a story excuse by making the character blind.
- Performance problems were made visible to the whole team by linking an on-screen face icon to frame rate.
- An NPC dialog bug became a feature when characters were made to chat with each other.
- Explicit compiler hints and branch removal can improve low-level performance in some cases.
- One shipped game hid an object with a hardcoded level-and-object check in the engine code.
- Stack allocation is described as faster and shorter-lived, while heap allocation is more managed but more complex.
- Solo developers are advised to prototype with placeholder art first and add final art after the gameplay is locked down.
- A stack overflow in an interrupt handler was avoided by checking stack depth and returning early when needed.
- A port to the original PlayStation led to many geometry and collision patches, which eventually caused more problems than they solved.
- A resource conflict near gold master was fixed by adding a space to a text file so its CRC32 changed.
- One release used hex editing to replace an error message in a memory manager with a thank-you message.
- Another shipping fix restored a byte that firmware bugs kept overwriting in executable code space.
- One team kept spare servers in a rainy-day pool because infrastructure approval took too long.
- Branchless code is presented as a way to avoid pipeline stalls and mispredicted jumps.
