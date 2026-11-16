---
title: "Setup email for a website, and perform send/receive thru your main Gmail."
date: '2026-11-16T01:10:42+00:00'
category: webclip
summary: 'The post explains how to forward mail from a custom domain to Gmail with Namecheap, then add the custom address in Gmail so you can send and reply from that domain too.'
tags: ["gmail", "namecheap", "email-forwarding"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Setup email for a website, and perform send/receive thru your main Gmail."
    url: "https://dev.to/ogrotten/setup-email-for-a-website-and-perform-send-receive-thru-your-main-gmail-3dme"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--setup-email-for-a-website-and-use-gmail.md"
    kind: repo
---

The post describes a setup where mail for a custom domain is forwarded to a Gmail inbox, and Gmail is configured to send mail using that custom domain as the From address. It says this can be done without extra cost, using Namecheap for forwarding and Gmail for sending and receiving.

## Reading notes

- Namecheap is configured to forward a specific custom-domain address to a Gmail account.
- The author also notes that a catch-all forwarder is possible, but the example uses a single alias.
- In Namecheap Advanced DNS, Mail Settings should be set to Email Forwarding.
- Gmail is then set up using Google’s documentation for sending mail from an alias.
- After setup, Gmail should show the custom domain address in the From dropdown.
- A test message from regular Gmail to the custom domain should arrive in the inbox quickly.
- A reply from the custom domain From address should also arrive in Gmail quickly.
- Gmail preferences can be adjusted in Accounts and Import under Send mail as for reply behavior.
