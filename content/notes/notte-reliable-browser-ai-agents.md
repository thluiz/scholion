---
title: "Notte: Reliable Browser AI agents"
date: '2025-08-11T15:14:20+01:00'
category: webclip
summary: 'Notte is a full-stack framework for building and deploying web automation agents, combining deterministic scripting with AI to reduce costs, improve reliability, and support structured output, sessions, vaults, personas, and scraping.'
tags: ["browser-automation", "ai-agents", "playwright", "structured-output"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "nottelabs/notte: 🔥 Reliable Browser AI agents (YC S25)"
    url: "https://github.com/nottelabs/notte?utm_source=tldrai"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/github-com--notte-reliable-browser-ai-agents.md"
    kind: repo
---

Notte presents itself as a full-stack framework for web automation agents. It combines scripting for deterministic steps with AI only where needed, and says this can cut costs by more than 50% while improving reliability. The project also offers a single API to develop, deploy, and scale agents and automations.

## Reading notes

- The opensource core includes running web agents from natural language tasks, structured output with Pydantic models, and site interactions using Playwright-compatible primitives and natural language commands.
- The API service adds stealth browser sessions with CAPTCHA solving, proxies, and anti-detection.
- It also includes hybrid workflows, secrets vaults for credentials, and digital personas with unique emails, phones, and automated 2FA for account creation flows.
- The quickstart shows installation with `pip install notte` and `patchright install --with-deps chromium`.
- The local mode example uses `notte.Session` and `notte.Agent` with a reasoning model and a task prompt.
- The Python SDK example uses `NotteClient`, hosted browser sessions, and a drop-in change from `notte` objects to `cli` objects.
- The benchmarks table reports Notte as ranking first, with 96.6% task reliability, 47 seconds per task, and higher reported scores than Browser-Use and Convergence.
- Structured output lets the agent return data in a specified Pydantic model.
- Vaults store credentials and are used automatically when needed.
- Personas provide digital identities with unique email addresses, phone numbers, and automated 2FA handling.
- Session features include stealth options, built-in CAPTCHA solving, proxy configuration, file upload and download support, and cookie-based authentication.
- The project supports external CDP-compatible browser sessions.
- Workflows combine scripted navigation and agent reasoning in the same session.
- The scraping endpoint can extract data with structured outputs and custom instructions.
- The license is SSPL-1.0.
