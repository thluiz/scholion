---
title: "The toxic side of free. Or: how I lost the love for my side project (part 3)"
date: '2026-09-25T20:32:35+01:00'
category: webclip
summary: 'Remy Sharp describes how open registration on JS Bin attracted abusive users, filled the database with junk, and eventually exhausted disk space, forcing a move to GitHub-only sign-in.'
tags: ["js-bin", "abuse", "registration", "database"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The toxic side of free. Or: how I lost the love for my side project (part 3)"
    url: "https://remysharp.com/2015/09/16/jsbin-toxic-part-3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/remysharp-com--the-toxic-side-of-free-part-3.md"
    kind: repo
---

JS Bin began as a fully anonymous tool, but that design made it impossible for users to recover old bins. Remy first added a crude name-and-key registration system, then later rebuilt sign-in properly with registration and password reminders, but without email checks, captchas, or limits on public output.

That openness increased registrations and let abusive users create multiple accounts and bins. On March 26, 2015, the database ran out of disk space, which stopped saving and even made deletions fail because MySQL could not create a temporary file. After a temporary disk upgrade, the longer-term response was to allow registration only through GitHub, which reduced the abuse but did not remove it entirely.

## Reading notes

- JS Bin started as anonymous, but that made old bins hard to recover.
- The first registration system used a name and key as a token before the full version 3 rewrite.
- Version 3 added proper sign-in, registration, and password reminders.
- There were no account checks, no email authentication, no captcha, and no limits on public output for registered users.
- Abusive users created multiple accounts and multiple bins.
- Blacklisting existed, but it only caught a small part of the junk.
- On March 26, 2015, the database ran out of disk space.
- JS Bin could still recall bins and be used, but saving failed.
- Deleting data also failed because MySQL could not create a tmp file.
- A 400GB disk replaced the 100GB disk and fixed the immediate outage.
- Registration was later restricted to GitHub, which lowered the signup rate and made abuse rarer.
