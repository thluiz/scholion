---
title: "Remote IEx access via :ssh"
date: '2016-02-07T23:10:47-03:00'
category: webclip
summary: 'The post shows how to start the SSH application first, then launch the daemon with IEx as the shell so a remote Elixir node opens an interactive IEx prompt over SSH.'
tags: ["elixir", "ssh", "iex"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Remote IEx access via :ssh"
    url: "http://bbhoss.io/remote-iex-access-via-ssh/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/bbhoss-io--remote-iex-access-via-ssh.md"
    kind: repo
---

The post explains that remote IEx access over SSH is possible in Elixir by adapting the approach used for Erlang nodes. The key change is to start the SSH application first and then configure the SSH daemon to use `IEx.start/0` as the shell.

## Reading notes

- Start `:ssh` before starting the daemon.
- Use `shell: {IEx, :start, []}` when calling `:ssh.daemon/2`.
- Connecting to the SSH port opens an interactive Elixir prompt.
- Typing `h()` disconnects the shell because of a Unicode issue.
- `:observer.start` appears to run on the local machine without X11 forwarding.
- The author presents this as a quick way to debug an application over SSH.
