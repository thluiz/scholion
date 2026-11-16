---
title: "takeWhile, takeUntil, takeWhat?"
date: '2026-11-16T19:37:30+00:00'
category: webclip
summary: 'The post contrasts takeWhile and takeUntil in RxJS, showing that takeWhile depends on incoming values while takeUntil is driven by an external Observable, and that both should usually be last in the pipeline.'
tags: ["rxjs", "takewhile", "takeuntil", "observables"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "takeWhile, takeUntil, takeWhat?"
    url: "https://dev.to/rxjs/takewhile-takeuntil-takewhat-5006"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--takewhile-takeuntil-takewhat.md"
    kind: repo
---

The post compares two RxJS ways to unsubscribe from Observables. It shows that `takeWhile` checks each incoming value against a condition, while `takeUntil` unsubscribes when another Observable emits. The difference matters because `takeWhile` needs one more emission to stop and can still trigger extra work before unsubscribing.

## Reading notes

- `takeWhile` is used when the incoming value itself decides whether to stay subscribed.
- `takeUntil` is used when an outer Observable or event should end the subscription.
- With `takeWhile`, a long-lived Observable may need one extra notification before unsubscribing.
- That extra notification can start side effects such as animation or an HTTP call before the unsubscribe happens.
- If the source never emits again, `takeWhile` may never run and the subscription can stay active.
- Moving `takeWhile` earlier in the pipe avoids some extra work, but it does not unsubscribe inner Observables returned by operators such as `switchMap`.
- The same placement issue applies to `takeUntil`, so the unsubscribe operator should be last in the pipe.
- The post presents long polling as a case where `takeWhile` fits, because the current value can tell whether the process is completed.
- For external triggers, the post recommends `takeUntil` with a `Subject`.
