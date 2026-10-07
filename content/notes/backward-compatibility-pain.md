---
title: "Backward compatibility pain"
date: '2015-03-04T11:41:45-03:00'
category: webclip
summary: 'The post compares three .NET 4.6 compatibility changes: a broken OrderByDescending case, a TimeZoneInfo model change, and a PersianCalendar leap-year change, to show the tradeoffs between correctness and compatibility.'
tags: ["backward-compatibility", "dotnet", "timezoneinfo", "persiancalendar"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Backward compatibility pain"
    url: "http://codeblog.jonskeet.uk/2015/03/02/backward-compatibility-pain/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/codeblog-jonskeet-uk--backward-compatibility-pain.md"
    kind: repo
---

The post argues that backward compatibility creates hard tradeoffs in APIs. It uses three .NET 4.6 examples to show how a fix or improvement can leave existing code broken, even when the change makes the system more correct or more flexible.

## Reading notes

- `OrderByDescending` fails with valid comparers when `IComparer.Compare` returns `int.MinValue`, because the implementation reverses order with unary negation.
- A safer fix would be to use `Math.Sign` or reverse the comparer arguments, but the post criticizes keeping the bug to avoid breaking incorrect comparer implementations.
- `TimeZoneInfo` in .NET 4.6 can now represent changing standard offsets over history, which improves the model.
- That same change makes it harder to predict `GetUtcOffset` from `AdjustmentRule` alone, because the rule does not expose the new offset information directly.
- `PersianCalendar` changes in .NET 4.6 to use a more complex leap-year formula aligned with Windows 10.
- The documented simple leap-year rule still matches the new one for a long range around the modern era, so the visible impact is mainly on older dates.
- The author says Noda Time 2.0 will support simple, astronomical, and arithmetic Persian calendars.
- The conclusion says backward compatibility is hard, and the best choice depends on whether the cost of preserving old behavior is worse than the disruption of change.
