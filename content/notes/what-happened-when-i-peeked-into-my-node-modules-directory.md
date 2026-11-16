---
title: "What Happened When I Peeked Into My Node_Modules Directory"
date: '2026-11-16T06:03:16+00:00'
category: webclip
summary: 'The piece jokes that popular JavaScript packages are bloated with hidden, unnecessary dependencies. It walks through Express, Ember, and Babel to argue for closer auditing of what gets installed.'
tags: ["javascript", "dependencies", "node-modules", "web-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What Happened When I Peeked Into My Node_Modules Directory | by Jordan Scales | Medium"
    url: "https://medium.com/friendship-dot-js/i-peeked-into-my-node-modules-directory-and-you-wont-believe-what-happened-next-b89f63d21558"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--what-happened-when-i-peeked-into-my-node-modules-directory.md"
    kind: repo
---

The article uses satire to criticize dependency bloat in JavaScript projects. It argues that popular packages pull in large chains of modules, waste space and bandwidth, and deserve closer scrutiny.

## Reading notes

- The author links dependency audits to the left-pad incident and says many developers are now checking what they install.
- A simple Express install is described as bringing in 291 modules.
- One Express dependency, “yummy,” contains a file called `like-tweet.js` that makes a POST request to the Twitter API.
- The route loaded by that request is a Hot Pockets tweet, which the author says is already favorited.
- Ember is presented as small at first glance, but most of its size is attributed to a library called Glimmer.
- Glimmer is said to depend on “brittanica,” which includes many alphabetized modules and large `terms.json` files.
- Those files are described as containing dictionary-like entries for words beginning with G.
- `glimmer/help.js` is shown printing the definition of “glimmer” from that data.
- Babel is introduced as a compiler with many dependencies, and `babel-preset-es2015` is said to install 90 dependencies and 17 MB of code.
- `babel-core` is described as especially large, and the referenced file is said to contain a picture of Guy Fieri.
- The conclusion says extra dependencies are not the end of the world, but maintenance and cleanup should matter more.
- The author ends by urging readers to inspect their own `node_modules` folders.
