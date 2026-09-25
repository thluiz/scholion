---
url: "https://kashw1n.com/blog/llm-cli/?utm_source=weeklyfoo&utm_medium=web&utm_campaign=weeklyfoo-93&ref=weeklyfoo"
captured_at: "2025-07-17T13:19:42+01:00"
title: "Using AI Without Leaving the Terminal: A Guide to llm"
domain: "kashw1n-com"
---

---
![using llm(cli-tool) to use AI](https://kashw1n.com/static/llm-cli.png)

I first discovered the `llm` tool watching Simon Willison’s talk “Catching up on the weird world of LLMs” at North Bay Python 2023. Since then, it’s become an essential part of my development workflow. This guide covers everything you need to know to get started and use it effectively.

## What is llm?

`llm` is a command-line tool that provides a unified interface to various language models. Instead of switching between different web interfaces, you can chat with GPT-4, Claude, Gemini, or local models directly from your terminal.

Key features:

-   **Universal interface**: One command for all models
-   **Automatic logging**: Every conversation saved to SQLite
-   **Plugin ecosystem**: Extend functionality with 70+ plugins
-   **Pipe friendly**: Works naturally with Unix pipes and command chains

## Installation and Setup

There are several ways to install `llm`. Choose the method that works best for your setup:

```
<span><span># Recommended: isolated environment with uv</span></span>
<span><span>uv</span><span> tool</span><span> install</span><span> llm</span><span>               # Python ≥ 3.9 (creates a venv under ~/.uv)</span></span>
<span></span>
<span><span># Quick one‑off try‑out (temporary env)</span></span>
<span><span>OPENAI_API_KEY</span><span>=</span><span>sk‑...</span><span> uvx</span><span> llm</span><span> "fun facts about skunks"</span></span>
<span></span>
<span><span># Traditional options</span></span>
<span><span>pipx</span><span> install</span><span> llm</span><span>   # or</span></span>
<span><span>brew</span><span> install</span><span> llm</span></span>
<span></span>
```

> **Tip:** `uvx` spins up a throw‑away virtualenv each run; switch to `uv tool install` when you’re ready for a permanent install.

Once installed, you’ll need to configure at least one AI provider. OpenAI is the most straightforward to start with:

```
<span><span>llm</span><span> keys</span><span> set</span><span> openai</span><span>      # paste your key</span></span>
<span><span>llm</span><span> "Ten names for a pet pelican"</span></span>
<span></span>
```

Add more providers at any time:

```
<span><span>llm</span><span> install</span><span> llm-anthropic</span></span>
<span><span>llm</span><span> keys</span><span> set</span><span> anthropic</span></span>
<span></span>
```

## Basic Usage Patterns

Here are the fundamental ways to interact with `llm`:

**Prompting & system messages:**

```
<span><span>llm</span><span> -m</span><span> gpt-4o</span><span> "Explain quantum computing in one tweet"</span></span>
<span><span>llm</span><span> -s</span><span> "You are an SRE"</span><span> -f</span><span> server.log</span><span> "Find errors in this log"</span></span>
<span></span>
```

Place flags **before** the prompt so shell tab completion stays happy.

**Working with files:** Instead of copy-pasting content, you can directly reference files or pipe content:

```
<span><span>llm</span><span> -f</span><span> myscript.py</span><span> "Summarise this code"</span></span>
<span><span>cat</span><span> diff.patch</span><span> | </span><span>llm</span><span> -s</span><span> "Generate a conventional commit message"</span></span>
<span></span>
```

**Interactive chat:** For longer conversations, use chat mode to maintain context across multiple exchanges:

```
<span><span>llm</span><span> chat</span><span>               # new conversation</span></span>
<span><span>llm</span><span> chat</span><span> -c</span><span>            # continue last one</span></span>
<span><span>llm</span><span> chat</span><span> -m</span><span> claude-4-opus</span></span>
<span></span>
```

## Managing Conversations

All conversations are automatically saved to SQLite. Here’s how to search and manage your conversation history:

```
<span><span>llm</span><span> logs</span><span> -n</span><span> 10</span><span>                 # tail</span></span>
<span><span>llm</span><span> logs</span><span> -q</span><span> "vector search"</span><span>    # search strings</span></span>
<span><span>llm</span><span> -c</span><span> "follow up question"</span><span>    # continue context</span></span>
<span><span>llm</span><span> logs</span><span> -u</span><span>                    # include token &amp; cost usage</span></span>
<span><span>llm</span><span> logs</span><span> --json</span><span> &gt; </span><span>backup.json</span><span>  # export</span></span>
<span></span>
```

## Essential Plugins

The plugin ecosystem extends `llm` to work with different AI providers and add specialized functionality:

| Category | Examples |
| --- | --- |
| Local models | `llm-mlx`, `llm-gguf`, `llm-ollama` |
| Remote APIs | `llm-anthropic`, `llm-gemini`, `llm-mistral`, `llm-openrouter` |
| Tools | `llm-tools-quickjs`, `llm-tools-sqlite` |
| Fragments | `llm-fragments-github`, `llm-fragments-pdf` |
| Embeddings | `llm-sentence-transformers`, `llm-clip` |
| Extras | `llm-cmd`, `llm-jq`, `llm-markov` |

Install with `llm install <plugin>` with no restart needed.

```
<span><span># Major AI providers</span></span>
<span><span>llm</span><span> install</span><span> llm-anthropic</span><span>    # Claude models</span></span>
<span><span>llm</span><span> install</span><span> llm-gemini</span><span>       # Google Gemini</span></span>
<span><span>llm</span><span> install</span><span> llm-ollama</span><span>       # Local models via Ollama</span></span>
<span></span>
<span><span># Add API keys</span></span>
<span><span>llm</span><span> keys</span><span> set</span><span> anthropic</span></span>
<span><span>llm</span><span> keys</span><span> set</span><span> gemini</span></span>
<span></span>
<span><span># Now use different models</span></span>
<span><span>llm</span><span> -m</span><span> claude-4-opus</span><span> "Write a technical explanation"</span></span>
<span><span>llm</span><span> -m</span><span> gemini-2.0-flash</span><span> "Quick calculation"</span></span>
<span></span>
```

## Running Local Models on Apple Silicon

For privacy or offline work, you can run models locally on Apple Silicon Macs using the `llm-mlx` plugin:

```
<span><span>uv</span><span> tool</span><span> install</span><span> llm</span><span> --python</span><span> 3.12</span><span>   </span></span>
<span><span>llm</span><span> install</span><span> llm-mlx</span><span>                # macOS 14.4+ only</span></span>
<span></span>
<span><span># Download a 3 B model (≈1.8 GB)</span></span>
<span><span>llm</span><span> mlx</span><span> download-model</span><span> mlx-community/Llama-3.2-3B-Instruct-4bit</span></span>
<span></span>
```

**Model recommendations by RAM:**

| RAM | Model (4 bit) |
| --- | --- |
| 8 GB | Llama 3.2 3B |
| 16 GB | Mistral 7B |
| 32 GB | Mistral Small 24B |

Assign an alias for convenience:

```
<span><span>llm</span><span> aliases</span><span> set</span><span> local3b</span><span> mlx-community/Llama-3.2-3B-Instruct-4bit</span></span>
<span></span>
```

## Fragments for Long Context

Fragments let you feed **huge** inputs without copy paste:

```
<span><span># Install the GitHub fragments plugin first</span></span>
<span><span>llm</span><span> install</span><span> llm-fragments-github</span></span>
<span></span>
<span><span># Summarise an entire GitHub repo</span></span>
<span><span>llm</span><span> -f</span><span> github:simonw/files-to-prompt</span><span> "Key design decisions?"</span></span>
<span></span>
<span><span># Use the symbex loader to extract a single Python symbol</span></span>
<span><span>llm</span><span> install</span><span> llm-fragments-symbex</span></span>
<span><span>symbex</span><span> my_module:some_func</span><span> | </span><span>llm</span><span> -c</span><span> "Write pytest tests"</span></span>
<span></span>
```

Let models run code imperatively:

```
<span><span>llm</span><span> --functions</span><span> 'def sq(x:int)-&gt;int: return x*x'</span><span> \</span></span>
<span><span>    "What is 431²?"</span><span> --td</span><span>     # shows the tool call</span></span>
<span></span>
<span><span># Use a plugin tool</span></span>
<span><span>llm</span><span> install</span><span> llm-tools-quickjs</span></span>
<span><span>llm</span><span> --tool</span><span> quickjs</span><span> "JSON.parse('[1,2,3]').reduce((a,b)=&gt;a+b,0)"</span></span>
<span></span>
```

## Templates and Aliases

Create shortcuts and reusable prompts to speed up common tasks:

```
<span><span>llm</span><span> aliases</span><span> set</span><span> fast</span><span> gpt-4o-mini</span></span>
<span><span>llm</span><span> aliases</span><span> set</span><span> smart</span><span> gpt-4o</span></span>
<span></span>
<span><span>llm</span><span> -s</span><span> "Explain like I'm five"</span><span> --save</span><span> eLI5</span><span>   # save as template</span></span>
<span><span>llm</span><span> -t</span><span> eLI5</span><span> "Why is the sky blue?"</span></span>
<span></span>
```

Set a default model for the session:

```
<span><span>llm</span><span> models</span><span> default</span><span> gpt-4o-mini</span></span>
<span></span>
```

## Embeddings & Semantic Search

Build searchable knowledge bases with embeddings:

```
<span><span># Embed text into a SQLite DB</span></span>
<span><span>llm</span><span> embed</span><span> -m</span><span> clip</span><span> "hello world"</span><span> -d</span><span> embeds.db</span></span>
<span></span>
<span><span># Find similar rows</span></span>
<span><span>llm</span><span> similar</span><span> "vector databases"</span><span> -d</span><span> embeds.db</span><span> -n</span><span> 5</span></span>
<span></span>
```

## Development Workflow Integration

**Code analysis with symbex:** The `symbex` tool pairs perfectly with `llm` for code analysis and documentation:

```
<span><span># Install companion tools</span></span>
<span><span>pip</span><span> install</span><span> symbex</span><span> files-to-prompt</span></span>
<span></span>
<span><span># Analyze specific functions</span></span>
<span><span>symbex</span><span> my_function</span><span> | </span><span>llm</span><span> -s</span><span> "Explain this code"</span></span>
<span></span>
<span><span># Generate tests</span></span>
<span><span>symbex</span><span> my_function</span><span> | </span><span>llm</span><span> -s</span><span> "Write pytest tests"</span></span>
<span></span>
<span><span># Document entire codebase</span></span>
<span><span>files-to-prompt</span><span> .</span><span> -e</span><span> py</span><span> | </span><span>llm</span><span> -s</span><span> "Generate API documentation"</span></span>
<span></span>
```

**Git integration:** Integrate AI into your Git workflow for better commit messages and code reviews:

```
<span><span># Generate commit messages</span></span>
<span><span>git</span><span> diff</span><span> --cached</span><span> | </span><span>llm</span><span> -s</span><span> "Generate a conventional commit message"</span></span>
<span></span>
<span><span># Code reviews</span></span>
<span><span>git</span><span> diff</span><span> HEAD~1</span><span> | </span><span>llm</span><span> -s</span><span> "Review these changes for potential issues"</span></span>
<span></span>
```

## Cost Optimization

Monitor and control costs by using the right models for different tasks:

```
<span><span>llm</span><span> -u</span><span> "Analyse this file"</span><span> -f</span><span> big.txt</span><span>   # prints tokens &amp; cost</span></span>
<span><span>llm</span><span> logs</span><span> -u</span><span> | </span><span>ttok</span><span> -s</span><span>                   # summary of past usage</span></span>
<span></span>
<span><span># Cheap model for simple tasks</span></span>
<span><span>llm</span><span> -m</span><span> gpt-4o-mini</span><span> "Quick draft tweet"</span></span>
<span></span>
<span><span># Continue conversations to reuse context</span></span>
<span><span>llm</span><span> "Analyze this architecture"</span><span> -f</span><span> project/</span></span>
<span><span>llm</span><span> -c</span><span> "Now focus on security"</span><span>  # Reuses previous context</span></span>
<span></span>
```

## Automation Examples

Create scripts to automate repetitive AI tasks:

**Batch summariser:**

```
<span><span>#!/usr/bin/env bash</span></span>
<span><span>for</span><span> url</span><span> in</span><span> "</span><span>$@</span><span>"</span><span>; </span><span>do</span></span>
<span><span>  curl</span><span> -s</span><span> "</span><span>$url</span><span>"</span><span> | </span><span>strip-tags</span><span> article</span><span> | </span><span>\</span></span>
<span><span>  llm</span><span> -s</span><span> "3 bullet summary"</span><span> &gt; </span><span>"summary_$(</span><span>basename</span><span> $url</span><span>).md"</span></span>
<span><span> done</span></span>
<span></span>
```

**Documentation generator:**

```
<span><span>files-to-prompt</span><span> src/</span><span> -e</span><span> py</span><span> | </span><span>\</span></span>
<span><span>llm</span><span> -s</span><span> "Generate API docs"</span><span> &gt; </span><span>docs/api.md</span></span>
<span></span>
```

## Advanced Features

**Structured output:** Get responses in specific JSON formats for easier programmatic processing:

```
<span><span># Get JSON with specific schema</span></span>
<span><span>llm</span><span> "Analyze sentiment"</span><span> --schema</span><span> '{</span></span>
<span><span>  "type": "object",</span></span>
<span><span>  "properties": {</span></span>
<span><span>    "sentiment": {"type": "string"},</span></span>
<span><span>    "confidence": {"type": "number"}</span></span>
<span><span>  }</span></span>
<span><span>}'</span></span>
<span></span>
```

**Multi-modal capabilities:** Work with images and other media types using compatible models:

```
<span><span># Image analysis</span></span>
<span><span>llm</span><span> "Describe this image"</span><span> -a</span><span> screenshot.png</span><span> -m</span><span> gpt-4o</span></span>
<span></span>
<span><span># Extract text from images</span></span>
<span><span>llm</span><span> "Extract all text"</span><span> -a</span><span> document.jpg</span><span> -m</span><span> gpt-4o</span></span>
<span></span>
```

## Best Practices

1.  Create **aliases** for favourite models
2.  Save reusable **templates** and **system prompts**
3.  Use **fragments** to feed large context instead of copy paste
4.  Pick the **cheapest model** that solves the task
5.  Combine with **Unix pipes** for powerful automation
6.  Turn logging off with `llm logs off` if working with sensitive data

## Conclusion

It’s been transformative integrating AI directly into my command-line workflow. Instead of context-switching between web interfaces, I can analyze code, generate documentation, or ask quick questions without leaving the terminal. The combination of universal model access, automatic conversation logging, and pipe-friendly design makes it an essential tool for any developer working with AI.

For more detailed information and advanced features, check out the official documentation at [https://llm.datasette.io/](https://llm.datasette.io/)
