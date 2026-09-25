---
title: "Migrating from Hugo to Astro"
date: '2025-10-22T11:20:47+01:00'
category: webclip
summary: 'The author migrates a long-running blog from Hugo to Astro, porting templates, pages, feeds, metadata, and posts while noting that most complexity comes from accumulated site-specific logic.'
tags: ["astro", "hugo", "site-migration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Migrating from Hugo to Astro - DEV Community"
    url: "https://dev.to/huijing/migrating-from-hugo-to-astro-3j95?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/dev-to--migrating-from-hugo-to-astro.md"
    kind: repo
---

The author is moving an 11-year-old blog from Hugo to Astro after finding Hugo’s revamped template system hard to manage. The migration keeps the same design, but rewrites generated components, page logic, the RSS feed, head metadata, and blog post handling.

## Reading notes

- The blog has already moved from Jekyll to Hugo, and this migration to Astro is the third platform change.
- The design has never changed, and the author treats that as part of the site’s identity.
- The author chooses to port everything, including many pages beyond the blog posts.
- Hugo’s updated template system broke local listing pages, and the author describes the problem as personal inability rather than a fault in Hugo.
- Astro and Bun are used for the new setup, starting from the blog template.
- Template components, styles, and frontmatter-related logic are moved first, but the migration quickly turns into page work as well.
- The RSS feed needs custom logic so external publication posts point to their canonical external URLs.
- The head element contains most of the site-specific complexity, including canonical URLs, robots metadata, social metadata, favicons, and stylesheet selection.
- Blog posts stay in markdown, but the author adds Astro content collection schemas to type the frontmatter fields.
- Some earlier shortcode-based choices now feel like tech debt, and the author plans to replace temporary components later.
- The full migration takes about three days, similar to the previous migration.
