---
title: "Agent Jido: the Weather Agent example"
date: "2026-09-23T16:06:26+01:00"
category: webclip
summary: "A worked example shows how Jido, an Elixir agent framework, wires an LLM to a weather API tool through three layers: Actions, an AI Skill that renders prompts, and a signal-routed Agent process."
tags:
  - elixir
  - ai-agents
  - jido
  - tool-calling
has_commentary: false
sources:
  - title: "Agent Jido · Agent Jido"
    url: "https://agentjido.xyz/blog/weather-agent"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-04/agentjido-xyz--agent-jido-weather-agent-example.md"
    kind: repo
---

Jido is an agent framework built in [Elixir](/notes/elixir/), and this post walks through its first worked example: a weather agent that takes a natural language question, decides whether to call a weather tool, and answers in character as an "enthusiastic weather reporter."

Actions are typed, schema-validated units of functionality, such as `Jido.Tools.Weather`, which wraps the OpenWeatherMap API; an AI Skill routes incoming messages by signal type and renders them into a prompt template before an Action runs; the Agent process holds state and exposes the public API that ties both together.

## Reading notes

- `Jido.Action` validates parameters against a declared schema automatically, and its `to_tool/0` function converts the Action's definition into a JSON schema an LLM framework like Langchain can call as a tool.
- Every user message becomes a `Jido.Signal`, Jido's standard messaging format, wrapping the message with a type like `"jido.ai.tool.response"` before it reaches the agent process.
- The `Jido.AI.Skill`'s router maps signal types to specific Actions, and its `handle_signal/2` callback renders the user's message into an EEx prompt template before the LLM ever sees it.
- The actual LLM call happens through `Jido.AI.Actions.Langchain`, which converts Jido Actions into Langchain's tool-calling format and passes the model, rendered prompt, and available tools together.
- A full request traces through eleven steps: the agent module delegates to a signal, the skill's router picks the right Action, Langchain calls the LLM, the LLM decides to invoke the weather tool with parsed parameters (e.g. `location: "Tokyo"`), the tool runs and returns data, and the LLM formats a final response that bubbles back to the caller.
- The example ships with test data mode (`test: true`) built into the Weather Action's schema, so it runs end to end in a Livebook without an OpenWeatherMap API key.
