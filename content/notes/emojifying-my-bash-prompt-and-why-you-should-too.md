---
title: "Emojifying my Bash Prompt (and why you should too)"
date: '2017-08-01T07:49:31-03:00'
category: webclip
summary: 'The post shows how the author replaces parts of a Bash prompt with emoji, then extends the prompt to surface outdated packages from brew, npm, pip2, and pip3 using files updated by cron jobs.'
tags: ["bash", "terminal-prompt", "emoji", "package-updates"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Emojifying my Bash Prompt (and why you should too)"
    url: "https://dev.to/thatjoemoore/emojifying-my-bash-prompt"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-08/dev-to--emojifying-my-bash-prompt-and-why-you-should-too.md"
    kind: repo
---

The author customizes a Bash prompt with emoji to make routine command-line work feel more pleasant. He replaces `~` with a house, the prompt arrow with `⏩`, and later adds a building icon for `~/work`, keeping the setup simple and intentionally playful.

He then moves package-update checks out of the prompt and into cron jobs so the prompt stays fast. The cron jobs write counts for brew, npm, pip2, and pip3 updates into files under `/tmp`, and the Bash profile reads those counts to display update messages and provide an `update_all` helper.

## Reading notes

- The prompt starts with emoji replacements for the home directory, the prompt arrow, and the work directory.
- `brew update` and `brew outdated` are moved out of the prompt and into scheduled jobs because they are too slow to run on each prompt.
- The same file-based approach is extended to npm, pip2, and pip3 update counts.
- A Bash helper named `update_all` runs the relevant upgrade commands for each package manager.
- The post presents the setup as a small source of daily joy and a way to handle developer stress.
