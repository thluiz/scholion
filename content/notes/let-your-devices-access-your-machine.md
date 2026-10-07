---
title: "Let your devices access your machine"
date: '2012-06-08T11:48:56-03:00'
category: webclip
summary: 'The post explains how Xip.io maps domains to any IP address, then shows how Showoff.io lets a public IP route to your machine so you can share a URL that reaches localhost.'
tags: ["xip-io", "showoff-io", "dns", "localhost"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let your devices access your machine"
    url: "http://functionsource.com/post/let-your-devices-access-your-machine"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/functionsource-com--let-your-devices-access-your-machine.md"
    kind: repo
---

The post describes Xip.io as a magic domain name that gives wildcard DNS for any IP address, with an example that resolves a subdomain to 10.0.0.1. It also notes that *.localtest.me does something similar, but only for localhost.

It then says Showoff.io goes further by routing a public IP to your machine. The commands shown are gem install showoff-io and show 3000, after which you can share a URL that reaches localhost.

## Reading notes

- Xip.io provides wildcard DNS for any IP address.
- *.localtest.me works the same way, but only for localhost.
- A domain like foo.bar.10.0.0.1.xip.io resolves to 10.0.0.1.
- Showoff.io routes a public IP to your machine.
- The post gives gem install showoff-io and show 3000 as the setup.
- The result is a shareable URL that really gets through to localhost.
