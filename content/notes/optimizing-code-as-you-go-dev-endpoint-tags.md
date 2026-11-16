---
title: "Optimizing Code as You Go"
date: '2026-11-16T20:10:32+00:00'
category: webclip
summary: 'Author shows how small, proactive optimizations on a heavily used endpoint, such as avoiding duplicate tag data and extra DB calls, can prevent future slowdowns and rework.'
tags: ["performance", "refactoring", "backend", "scalability"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Optimizing Code as You Go"
    url: "https://dev.to/molly_struve/optimizing-code-as-you-go-3b7e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--optimizing-code-as-you-go-dev-endpoint-tags.md"
    kind: repo
---

The author advocates always considering scale and optimization while writing code, even for small features. They use a DEV endpoint (`async_info/base_data`) that is called on every page load as an example, showing how duplicate tag data and extra database calls slipped into a critical path and later required a pull request to fix.

Examining the endpoint response hash, they highlight that two different fields (`followed_tag_names` and `followed_tags`) relied on the same tag data. They describe how a past developer might have added `followed_tags` to get richer tag information and then stopped there, unintentionally causing two calls for the same data on an endpoint hit millions of times a day. The author outlines two optimization approaches: memoizing the tag collection to reuse it in both fields, or removing the redundant field and deriving names from the richer JSON payload in the view, which is the solution implemented. They argue that a few extra minutes of thought during development can spare future work and help keep applications performant under growth.

## Reading notes

- The author supports thinking about scale and optimization for all code, regardless of product size.
- Some developers argue against optimizing early, saying it wastes time, but the author notes small extra effort now can prevent big headaches later.
- The focus is on small, in-place optimizations rather than rearchitecting entire features.
- DEV has an endpoint `async_info/base_data` that is called asynchronously on every page load to fetch user data for view variables.
- Because it is invoked on every page load, `async_info/base_data` is the most frequently hit endpoint in the system.
- The author decided to inspect this endpoint to ensure its response-building logic was as efficient as possible.
- The original response hash contained user fields and two tag-related fields: `followed_tag_names` and `followed_tags`.
- Both tag fields depended on the same underlying tags data, leading to redundant work.
- The narrative imagines a previous developer adding `followed_tags` to expose full tag information, on top of existing `followed_tag_names`.
- Many developers would stop after adding the new field, once their immediate data needs are met.
- The author urges developers to pause and check for duplication, noting that the change caused two calls to fetch equivalent tag information.
- While double-fetching tags might seem acceptable in rarely used code, it is problematic on a hot endpoint created millions of times daily.
- The extra call for tags can cumulatively waste resources and degrade performance as traffic grows.
- The first optimization option is to memoize the tag collection in a local `tags` variable and reuse it for both `followed_tag_names` and `followed_tags`.
- Memoizing tags in this way avoids multiple database hits for the same user tags within a single response build.
- The second option, and the one chosen, is to remove the `followed_tag_names` field entirely and rely on `followed_tags`.
- In the pull request, the view code was updated to parse the JSON from `followed_tags` and map it to tag names.
- This approach avoids the extra database call and also avoids sending duplicate tag information over the wire.
- The front-end snippet parses `currentUser.followed_tags` and extracts `name` values into `followedTagNames`.
- The derived `followedTagNames` are then passed as `availableTags` into the `ReadingList` component.
- The author concludes that spending a few extra minutes reviewing code with scale in mind can reduce future rework.
- They also note that such proactive checks can help prevent significant slowdowns if the app experiences large growth.
- The post ends with an encouragement to keep scaling concerns in mind while coding.
