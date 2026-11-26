---
title: "Why I'm Bullish on MCP for 2027"
date: '2026-11-26T16:28:44+00:00'
category: webclip
summary: 'The article argues MCP has matured beyond its hype cycle through Code Mode, Skills, Events, and Apps, making it central to scalable, multimodal and always-on agent workflows by 2027.'
tags: ["mcp", "ai-agents", "developer-tools", "protocols"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Why I'm Bullish on MCP for 2027"
    url: "https://www.philschmid.de/mcp-2027"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/philschmid-de--why-im-bullish-on-mcp-for-2027.md"
    kind: repo
---

MCP went through hype, backlash, and confusion around context bloat, but recent usage data from companies like Linear, Notion, Atlassian, Neon, and Apple shows strong growth and adoption. The protocol itself is evolving with specs that simplify sessions, add extensions, and enable smarter clients. New capabilities like Code Mode, typed outputs, embedded Skills, Events, and MCP Apps turn MCP into a foundation for multimodal, always-on, and collaborative agent workflows, with the author expecting the best 2027 agent harnesses to win on their MCP integration.

## Reading notes

- MCP initially suffered from context bloat complaints, leading many teams to favor CLIs and progressive disclosure with Skills.
- The author disagreed with the shift away from MCP and notes that sentiment is changing as adoption grows.
- At Linear and Notion, agents now create roughly half of all issues and pages, with Notion seeing a 60x increase in MCP traffic.
- Atlassian reports over 5M tool calls per workday over MCP, with 44% of users outside software teams where CLIs were never practical.
- Neon reports MCP-based agent usage growing 14% week over week, and Apple ships local MCP servers for Pages, Numbers, and Keynote.
- The 2026-07-28 MCP spec removed stateful sessions and added official extensions, indicating an actively improving protocol.
- Code Mode changes tool usage by giving models a sandbox and exposing MCP tools as callable functions instead of listing many tool schemas in prompts.
- With Code Mode, clients can auto-generate typed stubs using `inputSchema` and `outputSchema`, letting models chain multiple MCP calls in a single script.
- The example TypeScript snippet shows joining Linear issues with Sentry stats inside one script, returning only a compact summary to model context.
- MCP servers are natively multimodal, allowing `structuredContent` for code plus separate image, audio, or embedded resource blocks in a single tool call.
- MCP-based auth avoids storing broad-scope API keys in environment variables by delegating OAuth 2.1 flows and scoped permissions to the client outside the sandbox.
- The Skills vs MCP split is narrowing as Agent Skills move into MCP via the `io.modelcontextprotocol/skills` extension.
- Each skill is exposed via a `skill://` URI with YAML frontmatter and a file manifest that includes SHA-256 digests for versioning.
- SHA-256 digests help keep skills in sync across teams because clients pull updated versions automatically when the digest changes.
- Anthropic launched Skills over MCP in public beta for Claude and Claude Code, with vendors like Shopify, HubSpot, and Atlassian serving account-specific playbooks.
- The Skills lifecycle minimizes context by only injecting short names and descriptions initially and loading full `SKILL.md` content on demand via `resources/read` or `skills/get`.
- Clients can cache skill files locally keyed by digest so agents can read them from disk instead of reloading them into context repeatedly.
- MCP integrations were originally pull-based, unable to receive external notifications or wake agents when events occurred.
- The MCP Events extension (`io.modelcontextprotocol/events`) introduces server-advertised events, discoverable via `server/discover` and `events/list`.
- Harnesses or clients can expose subscription tools so users or agents subscribe to events across MCP servers.
- MCP Events supports three delivery modes: webhook (`events/subscribe`), push streaming (`events/stream`), and polling (`events/poll`).
- Webhook delivery sends signed HTTP POST requests to a callback URL so events can reach a harness while the user is offline.
- Push streaming keeps an open connection for live updates such as build logs or deployment progress.
- Polling lets clients without public URLs or with local CLIs check for events on a timer.
- The text uses a P0 security alert or urgent customer email as examples where events can wake an agent for triage.
- When an event fires, the MCP client tracks a cursor and deduplicates by `eventId` before passing the payload to the harness.
- The harness can resume the same chat trajectory or start a new one per alert when handling an incoming webhook event.
- Early implementations like Shop MCP (for order updates) and Vercel (for `deployment.succeeded`) already support MCP Events.
- Paired with MCP Tasks (`io.modelcontextprotocol/tasks`), agents can handle async workflows over MCP without custom webhook glue.
- Remote or durable harnesses such as ChatGPT expose callback endpoints for MCP Events so agents can wake up while users are offline.
- In these setups, the model or user defines filters and standing instructions once, and the MCP client manages subscription callbacks with renewable TTLs.
- MCP Apps (`io.modelcontextprotocol/ui`) allow servers to return sandboxed interactive HTML views (`text/html;profile=mcp-app`) inside compatible clients.
- MCP Apps address use cases like inspecting latency charts, filtering dashboards, or reviewing design decks without switching between multiple browser tabs.
- Slack's MCP client, Claude's interactive connectors, and Google Antigravity already render MCP Apps inline in chat, side panels, and as custom viewers.
- The author lists observability and intent as open problems because MCP servers typically only see tool calls, not the full user conversation.
- Adding `telemetry.intent` metadata or feedback tools such as Cloudflare's `submit_feedback` can improve server understanding of why tools are invoked.
- Discovery is another gap, since registering an MCP server in multiple registries does not scale.
- The text suggests approaches like `/.well-known`-based discovery with automated security scanning to streamline finding MCP servers.
- Security remains a concern, with untrusted webhook payloads, Code Mode sandboxes, and embedded UI iframes increasing prompt-injection risk.
- The author argues MCP is evolving beyond simple remote tool calls into a full runtime that unifies Code Mode, typed outputs, Skills, Tasks, Events, and UI.
- They expect the strongest agent harnesses in 2027 to differentiate themselves through their quality of MCP integration.
- The harness itself can act as an MCP server so agents coordinate using the same protocol primitives they already use for tools.
- In this model, subagents run as MCP Tasks and a shared "swarm board" exposes tools for posting findings and claiming work.
- MCP Events can notify coordinators or peer agents when tasks finish or when new updates appear, enabling multi-agent coordination.
- The author recommends MCP servers expose fine-grained tools for agents instead of wrapping entire SaaS products behind a single `ask_agent` endpoint.
- A monolithic `ask_agent` tool hides state and context that a higher-level agent already holds, limiting composition.
- The suggested pattern is to keep regular MCP servers focused on typed tools and structured data and use agent-as-MCP-server only for longer-running coordination across subagents, teams, or organizations.
