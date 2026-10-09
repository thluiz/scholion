---
title: "Entity Systems are the Future of MMOs Part 4"
date: '2014-05-05T08:42:19-03:00'
category: webclip
summary: 'The post argues that MMO development is dominated by content, post-launch work, rule changes, and persistent data handling, which makes database-friendly, changeable game architecture more valuable than prelaunch engine work.'
tags: ["massively-multiplayer", "entity-systems", "databases", "game-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Entity Systems are the Future of MMOs Part 4 | T-machine.org"
    url: "http://t-machine.org/index.php/2008/03/13/entity-systems-are-the-future-of-mmos-part-4/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-05/t-machine-org--entity-systems-are-the-future-of-mmos-part-4.md"
    kind: repo
---

The post says the connection between entity systems and MMOs is data. MMO development is driven by content production, post-launch updates, changing core rules over time, and the need to store and use large amounts of player data.

It argues that these pressures make long-term maintainability more important than initial engine work. Commercial MMOs therefore tend to favor databases, relational access, raw data for game logic, scripting where needed, and heavy testing, especially before live changes.

## Reading notes

- MMO development is mostly about data, not just the client or engine.
- Most of the cost of an MMO is content such as quests, areas, loot, and scripted events.
- Players consume content faster than developers can produce it, so content production must continue after launch.
- A large part of MMO development happens after launch through expansions and content updates.
- The core technology usually changes less than the content, though some MMOs later receive major visual or engine updates.
- MMO revenue depends on keeping players playing for longer periods.
- Game rules change over time through nerfs and expansions, so core logic must be easy to alter.
- MMO play generates large amounts of persistent data, including player progress and history.
- Any game data used in play must be programmatically accessible.
- MMO developers often prefer commercial databases, relational access, raw data for logic, and scripting languages.
- The post presents testing and post-launch change control as standard practical priorities in MMO development.
