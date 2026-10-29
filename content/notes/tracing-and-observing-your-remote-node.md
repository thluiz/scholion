---
title: "Tracing and observing your remote node"
date: '2016-05-11T06:10:58-03:00'
category: webclip
summary: 'The post explains how to trace and observe a remote Elixir node through EPMD, SSH port forwarding, node naming, cookies, and tools like Erlyberly and Observer.'
tags: ["elixir", "erlang", "distributed-systems", "observer"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tracing and observing your remote node « Plataformatec Blog"
    url: "http://blog.plataformatec.com.br/2016/05/tracing-and-observing-your-remote-node/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/blog-plataformatec-com-br--tracing-and-observing-your-remote-node.md"
    kind: repo
---

The post shows how to reach a remote Erlang node from a local machine so you can trace it and inspect it with tools such as Erlyberly and Observer. It starts with EPMD as the name server, then uses SSH port forwarding so the local machine can register to the remote EPMD and discover remote nodes.

It then configures a Phoenix release by setting the node name, the distribution port, and the cookie in `vm.args`, and notes that the application must be restarted after the change. After that, a local shell or tracing tool can connect to the remote node through the shared cookie. If Observer fails with an `:observer_backend` error, the fix is to add `:runtime_tools` to `mix.exs`.

## Reading notes

- EPMD works as the name server for distributed Erlang on the hosts involved.
- `epmd -names` shows the port and the nodes registered on EPMD.
- SSH port forwarding can redirect local EPMD traffic to a remote EPMD.
- A Phoenix release can be configured in `vm.args` with a node name, a distribution port, and a cookie.
- After changing `vm.args`, the application must be restarted.
- With the right cookie and port forwarding, a local tracing tool can register through the remote EPMD and find the remote application.
- `iex --remsh` connects directly to the remote node.
- `:observer.start()` can be used from a local shell that shares the remote cookie.
- If Observer raises an `:observer_backend` error, adding `:runtime_tools` to `mix.exs` enables it.
