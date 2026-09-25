---
title: "Power Prompts in Claude Code"
date: '2026-02-02T14:28:42+00:00'
category: webclip
summary: 'The page shows how one prompt can make Claude Code capture screenshots, run parallel audits, compare visual regressions, update CLAUDE.md, and create a reusable skill.'
tags: ["claude-code", "prompt-design", "playwright-mcp", "workflow-automation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Power Prompts in Claude Code ・ Hardik Pandya"
    url: "https://hvpandya.com/power-prompts?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-02/hvpandya-com--power-prompts-in-claude-code-hardik-pandya.md"
    kind: repo
---

The page describes a single Claude Code prompt that asks for performance, accessibility, SEO, and code-quality improvements, while preserving the site’s look and features. It says the prompt can also trigger baseline screenshots, parallel agents, visual regression checks, documentation updates, and a reusable skill.

## Reading notes

- The author says Claude Code made frontend optimization easy to apply while redesigning the site.
- The prompt asks for performance, accessibility, SEO, and code-quality work in one run.
- Before changes, it captures baseline screenshots of key pages.
- It runs audits and fixes in parallel with separate agents for performance, accessibility, SEO, and code cleanup.
- After changes, it captures desktop, tablet, and mobile screenshots and compares them with the baseline.
- It updates CLAUDE.md with what changed.
- It creates a reusable skill so the same audit workflow can be run again later.
- The post says Playwright MCP is needed for the screenshot workflow.
- The reported results include unused font removal, accessibility fixes, JSON-LD schema changes, removal of test code, screenshot capture, zero visual regressions, and a new skill file.
