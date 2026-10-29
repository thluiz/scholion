---
title: "Why ActiveRecord Sucks - Very Good Indicators"
date: '2015-07-26T11:01:31-03:00'
category: webclip
summary: 'The post says ActiveRecord is useful, but its convenience comes with memory overhead, tighter coupling, weaker SQL for complex queries, and less readable code when queries get intricate.'
tags: ["activerecord", "orm", "rails", "sql"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why ActiveRecord Sucks - Very Good Indicators"
    url: "http://www.verygoodindicators.com/blog/2015/04/20/why-activerecord-sucks/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/verygoodindicators-com--why-activerecord-sucks-very-good-indicators.md"
    kind: repo
---

The post argues that ActiveRecord makes common tasks easy, but that ease hides costs in memory use, coupling, SQL quality, and readability. It also connects this preference for ease with a broader habit of chasing convenience without considering the tradeoffs.

## Reading notes

- ActiveRecord does a lot of work behind the scenes, which can increase memory use when many instances are created.
- It can make classes depend on Rails and on specific object APIs, which increases coupling and makes tests rely on loading Rails.
- For simple queries it works fine, but complex queries can become worse SQL than an experienced engineer would write directly.
- When queries become intricate, ActiveRecord code can turn into many method calls and SQL fragments that are harder to read than plain SQL.
- The author likes ActiveRecord, but says its convenience should be weighed against performance and complexity costs.
