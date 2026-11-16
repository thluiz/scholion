---
title: "Why you should never ignore the alt attribute"
date: '2026-11-16T19:49:02+00:00'
category: webclip
summary: 'Explains that the alt attribute improves accessibility and SEO by giving images readable text for screen readers and crawlers, and shows how to keep alt text relevant, concise, and context-aware.'
tags: ["alt-attribute", "accessibility", "seo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why you should never ignore the alt attribute"
    url: "https://dev.to/nataliedeweerd/why-you-should-never-ignore-the-alt-attribute-2gh0"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--why-you-should-never-ignore-the-alt-attribute.md"
    kind: repo
---

The page argues that the alt attribute has long been part of HTML and matters for both accessibility and search visibility. It should describe the image in a way that fits the page context, and decorative images can use an empty alt attribute instead of leaving it out.

It also warns against alt text that is too vague, too generic, copied from nearby page text, or unnecessarily long. The examples show that good alt text is concise and specific, while poor alt text misses important context or repeats too much detail.

## Reading notes

- The alt attribute was introduced in HTML 2 in 1995 and has been used for a long time.
- It helps search engine crawlers and screen readers understand what an image is.
- Alt text should reflect the nature of the image, not give a literal description when a more useful description fits the context.
- The detail in alt text should match the content of the rest of the page.
- If an image is decorative, an empty alt attribute is better than omitting it.
- Screen readers may read out the image URL if no alt attribute is included.
- Alt text supports accessibility by giving a readable text version of an image.
- Alt text can help SEO because bots can read it while they cannot read the image itself.
- Copying page text into alt text may look like spam to crawlers and can harm SEO.
- Good alt text is clear, concise, and specific.
- Subjective adjectives should only be used when they make sense in the site’s context.
- Weak alt text can be too vague, such as just naming an object.
- Alt text can become too long and should stay succinct and descriptive.
