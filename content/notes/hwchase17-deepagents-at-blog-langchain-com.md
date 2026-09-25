---
title: "Deep Agents"
date: '2025-08-04T17:06:45+01:00'
category: webclip
summary: 'The package wraps planning, subagents, a mocked file system, and a detailed prompt into a general-purpose deep agent. It shows how to create and customize one with tools, instructions, subagents, and a model.'
tags: ["deep-agents", "langgraph", "subagents", "planning-tool"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "hwchase17/deepagents at blog.langchain.com"
    url: "https://github.com/hwchase17/deepagents?ref=blog.langchain.com&utm_source=tldrnewsletter"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/github-com--hwchase17-deepagents-at-blog-langchain-com.md"
    kind: repo
---

The page presents `deepagents` as a Python package for building agents that can handle longer, more complex tasks. It says the package combines a planning tool, subagents, access to a file system, and a detailed prompt to move beyond shallow tool-calling loops.

## Reading notes

- `deepagents` is described as a general-purpose way to create a Deep Agent for an application.
- The project says it was primarily inspired by Claude Code.
- The example shows `create_deep_agent` being used with a search tool and research instructions.
- A deep agent created with `create_deep_agent` is said to be a LangGraph graph, so it can use streaming, human-in-the-loop, memory, and studio.
- `create_deep_agent` takes `tools` and `instructions` as required parameters.
- It also accepts optional `subagents`, each defined with a name, description, prompt, and optional tools.
- By default, `deepagents` uses the model `claude-sonnet-4-20250514`.
- The built-in system prompt is described as detailed and as necessary for the agent to work well on deep tasks.
- The built-in planning tool is compared to Claude Code's TodoWrite tool and is used to keep a plan in context.
- The file system tools are `ls`, `edit_file`, `read_file`, and `write_file`, and they are mocked through LangGraph state rather than a real file system.
- The file system is currently one level deep and uses the `files` key in the LangGraph State object.
- The package includes a built-in `general-purpose` subagent and allows custom subagents for context quarantine and custom instructions.
- The roadmap includes custom system prompts, cleaner code, a more robust virtual filesystem, a deep coding agent example, benchmarking the deep research agent, and human-in-the-loop tool support.
