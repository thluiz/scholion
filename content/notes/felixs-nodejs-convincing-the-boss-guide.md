---
title: "Felix's Node.js Convincing the boss guide"
date: '2014-06-19T09:40:21-03:00'
category: webclip
summary: 'The guide says node.js fits JSON APIs, single-page apps, streaming, soft real-time systems and Unix tool integration, but it is a poor choice for CPU-heavy apps, simple CRUD sites and risky stacks built around buzzword-driven NoSQL.'
tags: ["nodejs", "web-apps", "json-apis", "soft-realtime"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Felix's Node.js Convincing the boss guide"
    url: "http://nodeguide.com/convincing_the_boss.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/nodeguide-com--felixs-nodejs-convincing-the-boss-guide.md"
    kind: repo
---

The guide argues that node.js should be used selectively. It fits lightweight REST and JSON APIs, AJAX-heavy single-page apps, streaming data, shelling out to Unix tools, and soft real-time applications. It is a poor fit for CPU-heavy software, simple CRUD or HTML sites, and architectures that add NoSQL complexity without a clear reason.

## Reading notes

- CPU-heavy workloads such as video encoding or AI are better served by C or C++, although node.js can still sit on top as a scripting layer with C++ addons.
- For simple CRUD or HTML apps, node.js does not yet offer clear business advantages over PHP, Ruby, or Python, and its frameworks are not yet as mature as Rails, CakePHP, or Django.
- The text warns against stacking node.js with NoSQL choices just for novelty, and suggests conservative databases like postgres or mysql when business risk matters.
- Node.js is presented as a strong fit for JSON APIs because its non-blocking I/O and JavaScript make it useful for exposing databases and web services through a JSON interface.
- Single-page apps, especially AJAX-heavy ones like Gmail, benefit from low response times and shared validation code between client and server.
- Node.js is also suited to reusing existing command-line tools, since it can spawn many child processes and treat their output as streams.
- Streaming use cases include real-time file upload processing and proxies between data layers.
- Soft real-time systems such as Twitter-like apps, chat software, sports betting, and instant messaging interfaces fit better than hard real-time systems, where Erlang is suggested instead.
- To convince management, the guide recommends building a one-week prototype to gather evidence before asking for a larger commitment.
- It argues that JavaScript talent is widely available, that the node.js community is growing quickly, and that corporate backing from Joyent reduces long-term project risk.
- Performance is framed as a persuasive argument when it matters, because V8 and non-blocking I/O can support thousands of concurrent connections.
- For clients, the advice is more cautious: confirm fit, ensure future support, and expect version update work every 3 to 6 months.
