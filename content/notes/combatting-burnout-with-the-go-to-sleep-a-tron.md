---
title: "Combatting Burnout with the \"Go to Sleep-a-tron\""
date: '2026-11-16T01:59:02+00:00'
category: webclip
summary: 'The post presents a playful GitHub Action that checks commit timestamps against a timezone and comments when work happens before 9am or after 7pm, with notes on implementation limits and future extensions.'
tags: ["github-actions", "burnout", "timezones", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Combatting Burnout with the \"Go to Sleep-a-tron\""
    url: "https://dev.to/frasertooth/combatting-burnout-with-the-go-to-sleep-a-tron-25f9"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--combatting-burnout-with-the-go-to-sleep-a-tron.md"
    kind: repo
---

The post introduces a playful GitHub Action called the Go-To-Sleep-a-Tron. It was inspired by Charlie Gerard’s work and the GitHub Actions Hackathon, and it comments on commits that happen outside a chosen sleep-friendly window.

## Reading notes

- The action checks commit timestamps and posts a comment if the commit was made before 9am or after 7pm in the committer’s timezone.
- `GITHUB_TOKEN` is required, `custom_message` is optional, and `timezone` is required for events other than pushes.
- The author says the intended users are companies that want to discourage overworking.
- The implementation follows GitHub’s official guides and Charlie Gerard’s code.
- For push events, the action checks each commit for a `timestamp` field that includes the time and timezone.
- The author wanted the action to work on more GitHub event types, but the available data only exposed the committer’s timezone in commit data.
- Timezone libraries were hard to use here because the author already had the timezone and wanted to keep it from being converted to UTC.
- The final approach was to extract the timezone from the string with regex and do the timing check manually.
- Developing the action locally was awkward, so the author kept pushing changes to GitHub to test it.
- The post ends by suggesting possible extensions such as more action types, per-contributor timezones, and notifications through Slack or email.
