---
title: "The two patterns by which agents connect sandboxes"
date: '2026-02-10T16:34:41+00:00'
category: webclip
summary: 'The post describes two ways to connect agents to sandboxes: run the agent inside the sandbox for tighter coupling, or keep the agent outside and use the sandbox as a tool for easier updates and cleaner separation.'
tags: ["agents", "sandboxes", "architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The two patterns by which agents connect sandboxes"
    url: "https://x.com/hwchase17/status/2021261552222158955?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-02/x-com--the-two-patterns-by-which-agents-connect-sandboxes.md"
    kind: repo
---

The post says agents increasingly need isolated workspaces where they can run code, install packages, and access files. It frames sandboxes as the boundary that keeps agent execution separate from the host system, and then compares two architecture patterns for using them.

## Reading notes

- More agents need a workspace that can run code, install packages, and access files.
- Sandboxes provide isolation between the agent environment and the host system.
- Pattern 1 runs the agent inside the sandbox and communicates with it over the network.
- This pattern mirrors local development and gives the agent direct filesystem access.
- Its trade-offs include extra infrastructure for HTTP or WebSocket communication, API keys living inside the sandbox, slower updates, and the need to resume the sandbox before the agent becomes active.
- Pattern 2 runs the agent locally or on a server and uses the sandbox as a remote execution tool.
- This pattern makes it easier to update agent logic, keeps API keys outside the sandbox, and separates agent state from execution state.
- Its main trade-off is network latency, especially for workloads with many small executions.
- The post says deepagents supports both patterns with simple configuration.
