---
title: "I built a VSCode extension: ngrok for VSCode"
date: '2020-04-15T10:59:07+00:00'
category: webclip
summary: 'The author describes a first VSCode extension that starts ngrok tunnels from the command palette, using either a port number or a named tunnel from the ngrok config file.'
tags: ["vscode", "ngrok", "extension"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "I built a VSCode extension: ngrok for VSCode"
    url: "https://dev.to/philnash/i-built-a-vscode-extension-ngrok-for-vscode-29f7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--i-built-a-vscode-extension-ngrok-for-vscode.md"
    kind: repo
---

The post introduces a first VSCode extension built to make ngrok easier to use inside the editor. It lets users start a tunnel from a port number or a named tunnel in the ngrok config file, then open the ngrok dashboard or close the tunnel from the command palette.

The author says the extension is open source, asks for feedback from ngrok users, and mentions possible future additions such as a Status Bar Item or Tree View for more control over running tunnels.

## Reading notes

- Built over the Easter weekend as a first VSCode extension
- Aims to make ngrok easier to use in VSCode
- ngrok exposes a localhost server through a public URL
- Version 1 can start a tunnel from a port number or a named tunnel from the ngrok config file
- One setting allows a custom path to the config file
- Users can open the ngrok dashboard or close the tunnel after it starts
- All commands are available from the VSCode command palette
- The code is open source on GitHub
- Future ideas include a Status Bar Item or Tree View for running tunnels
- The author asks for feedback, bug reports, feature requests, and reviews
