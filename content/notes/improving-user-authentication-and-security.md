---
title: "Improving User Authentication and Security"
date: '2020-02-22T12:11:59+00:00'
category: webclip
summary: 'The article argues that password-only authentication is obsolete and vulnerable to theft and hijacking, and that decentralized key pairs can let users sign requests and encrypt data more securely.'
tags: ["authentication", "security", "ethereum", "web3"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Improving User Authentication and Security | by Eric Elliott | JavaScript Scene | Medium"
    url: "https://medium.com/javascript-scene/improving-user-authentication-and-security-ddb60b1ef69b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--improving-user-authentication-and-security.md"
    kind: repo
---

The article says password-only security models are obsolete because stolen password databases, hashing attacks, and session hijacking can expose users to privacy loss, financial damage, and identity theft. It presents decentralized authentication as a safer model because each user gets a public and private key pair.

## Reading notes

- Password-based security is described as broken because stolen databases can be attacked at scale and sessions can be hijacked after login.
- With Ethereum-style key pairs, each request can be signed with the user’s private key and verified with the public key.
- Private keys can be kept off the internet and protected with hardware-level security.
- Key pairs can also encrypt user data so only the owner can read it.
- The article says users can authenticate with a crypto wallet, and tools like Fortmatic can bring that wallet experience into a mainstream browser without extensions.
- The `useFortmatic` hook example keeps track of wallet accounts, waits for `web3Ready`, and signs users in automatically when they are already authenticated.
- The article notes that API keys are not secrets, but domains must be authorized.
- It also says the app does not fall back to the browser’s built-in Web3 wallet by default for UX and privacy reasons.
