---
title: "You blog? then better ask your boss"
date: '2026-09-24T20:23:16+01:00'
category: webclip
summary: 'The post warns employed bloggers to be careful about what they publish, since a boss or web host may object. It also describes a Movable Type change that adds a direct delete link to comment-spam warning emails.'
tags: ["blogging","comment-spam","movable-type"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You blog? then better ask your boss"
    url: "https://brajeshwar.com/2003/you-blog-then-better-ask-your-boss/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/brajeshwar-com--you-blog-then-better-ask-your-boss.md"
    kind: repo
---

The post says employed bloggers should be careful about blog content, because a boss may not like what is published. It also mentions a warning about “Abuse-Copyright Infringement” tied to comments on the blog and says the author spent half a day reading and deleting many comments. After that, it explains a Movable Type change for handling comment spam more easily by adding a delete link directly into the email notification.

## Reading notes

- The author warns that people who have jobs need to be careful about what they publish on their blog, because the boss may not like the content.
- He reports having received a “Abuse-Copyright Infringement” notice because of comments on the blog and says he had to spend half a day reading and deleting several of them.
- The text says he follows Tip No. 6 of the “seven quick steps to spam-free blog”.
- The technical section presents a Perl change in the file `lib/MT/App/Comments.pm` to handle comment spam.
- The change puts in the email a link that goes directly to the “Delete comment? [Yes/No]” page in Movable Type.
- The text notes that this page closes the browser window after the click, so the link should be opened in a separate or empty window.
