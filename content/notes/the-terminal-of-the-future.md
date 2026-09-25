---
title: "the terminal of the future"
date: '2026-09-25T17:11:13+01:00'
category: webclip
summary: 'The post argues that a better terminal should combine shell integration, persistent sessions, structured I/O, undoable transactions, and a Jupyter-like frontend, then adopt those pieces step by step.'
tags: ["terminal", "shell-integration", "persistent-sessions", "jupyter"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "the terminal of the future"
    url: "https://jyn.dev/the-terminal-of-the-future?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/jyn-dev--the-terminal-of-the-future.md"
    kind: repo
---

The post describes a terminal as four parts: the emulator, the PTY, the shell, and the programs it spawns. It argues that current terminals are limited because input, output, and session state are handled too rigidly.

## Reading notes

- Jupyter is presented as a useful model because it supports rich rendering, rerun controls, editable views of source and output, and a built-in editor.
- A shell-based Jupyter model runs into problems with character-by-character input, long-lived processes, rerun side effects, and undo/redo.
- Warp and iTerm2 show that shell integration can expose command boundaries, output, navigation, notifications, and overlays.
- Long-lived processes are split into interaction, suspension, and disconnection.
- tmux, Zellij, Screen, Mosh, alden, shpool, dtach, abduco, and diss are placed in different parts of the detach and resume design space.
- The post treats rerun and undo/redo as a dataflow problem and points to Pluto.jl and orthogonal persistence.
- Once IO is tracked and processes are sandboxed, the terminal session can be treated as a pure function of inputs, file system state, environment variables, and process attributes.
- The proposed derived features include runbooks, CSS-based customization, command search by output or timestamp, timestamps and durations, local line editing over networks, IntelliSense, collaborative terminals, editable recordings, build tracing, branching undo trees, and LLM workflows inside sandboxes.
- The build plan is incremental: first transactional CLI semantics, then persistent sessions, then structured RPC with metadata, and only at the end a Jupyter-like frontend.
- The author says the full project would take about a decade and invites readers to spread the word.
