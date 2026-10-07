---
title: "5 Useful Tips For A Better Commit Message"
date: '2015-02-05T21:06:41-03:00'
category: webclip
summary: 'The page recommends keeping the first line under 50 characters, using spell check and 72-column wrapping, avoiding git commit -m, and writing commit messages that explain why, how, side effects, and the related issue or story.'
tags: ["git", "commit-messages", "code-review", "vim"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "5 Useful Tips For A Better Commit Message"
    url: "http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/robots-thoughtbot-com--5-useful-tips-for-a-better-commit-message.md"
    kind: repo
---

The page argues that commit messages should be written for future readers, especially reviewers and the same developer weeks or years later. It recommends a short summary line, a blank line after it, spell checking and 72-column wrapping in Vim, and a fuller message that explains the reason for the change, the approach taken, and the side effects.

It also advises against using git commit -m, since that encourages overly compressed messages. Instead, it suggests including a link to the issue, story, or card, and treating the commit message as part of the project history.

## Reading notes

- Keep the first line to 50 characters or less, then leave a blank line.
- Use Vim commit plugins, plus spell checking and 72-column wrapping for git commit messages.
- Avoid git commit -m / --message=<msg> because it encourages poor commit messages.
- Explain why the change is necessary, how it addresses the issue, and what side effects it has.
- Include a full URL to the related issue, story, or card as a standard part of the message.
- Treat commit messages as part of the project history that helps others understand the change later.
