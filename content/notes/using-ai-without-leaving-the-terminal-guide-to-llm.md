---
title: "Using AI Without Leaving the Terminal: A Guide to llm"
date: '2025-07-17T13:19:42+01:00'
category: webclip
summary: 'The guide presents llm as a terminal-based interface to multiple language models, with logging, plugins, pipes, local models, embeddings, templates, and workflow automation.'
tags: ["llm", "command-line", "ai-tools", "developer-workflow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using AI Without Leaving the Terminal: A Guide to llm"
    url: "https://kashw1n.com/blog/llm-cli/?utm_source=weeklyfoo&utm_medium=web&utm_campaign=weeklyfoo-93&ref=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/kashw1n-com--using-ai-without-leaving-the-terminal-guide-to-llm.md"
    kind: repo
---

The page explains `llm` as a command-line tool that unifies access to language models from the terminal. It highlights installation options, provider setup, conversation logging, plugins, local models, fragments, templates, embeddings, and automation examples for everyday development work.

## Reading notes

- `llm` gives one command for different models instead of switching web interfaces.
- It saves every conversation to SQLite and can show logs, usage, and exports.
- Installation paths include `uv`, `uvx`, `pipx`, and Homebrew.
- You can set API keys for providers like OpenAI, Anthropic, and Gemini.
- Prompt flags go before the prompt, and files can be passed directly with `-f` or through pipes.
- Chat mode keeps context across exchanges.
- Plugins extend provider support and add tools, fragments, embeddings, and extras.
- On Apple Silicon Macs, `llm-mlx` allows local models, with model choices tied to RAM.
- Fragments can feed large inputs such as GitHub repos or code symbols.
- Functions and tools let models run code or use plugin tools.
- Aliases, templates, and default models reduce repeated setup.
- Embeddings and `similar` support semantic search over a SQLite database.
- `symbex`, `files-to-prompt`, and Git commands integrate `llm` into development tasks.
- Cost control includes choosing cheaper models, checking token usage, and reusing context.
- The page also shows batch summarization, documentation generation, structured JSON output, and image analysis.
- Best practices emphasize aliases, templates, fragments, low-cost models, Unix pipes, and disabling logs for sensitive data.
