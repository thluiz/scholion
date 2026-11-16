---
title: "Introducing Code Notes"
date: '2026-11-16T03:41:27+00:00'
category: webclip
summary: 'The author explains why he built Code Notes, a Gatsby theme for searchable, shareable code notes with MDX support, Git versioning, and a simple responsive design.'
tags: ["gatsby", "code-notes", "markdown", "flexsearch"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introducing Code Notes"
    url: "https://zander.wtf/blog/code-notes-release"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/zander-wtf--introducing-code-notes.md"
    kind: repo
---

The post says the author started making code notes because he kept searching for answers to problems he had already solved. He wanted notes with snippets, examples, explanations, and copied documentation, but none of the apps he tried had all the features he wanted.

## Reading notes

- Code Notes is a Gatsby theme that gives full control over how notes are written, published, and stored.
- The notes are searchable and shareable by default, so the author could send links to colleagues.
- GitHub hosts the notes, so they are versioned with Git and can be forked or reverted.
- Notes are written in MDX or markdown, and MDX lets JSX or HTML render inside the note.
- Notes can include interactive code and previews side by side.
- Iframes can also be added, including gists, Codepens, and Figma designs.
- Search includes all code snippets, using Flexsearch with optimizations for speed.
- The design is intentionally simple so notes stay legible, and there are light and dark themes.
- The notes also work well on mobile.
- A Gatsby starter is available for setting up a notes site.
- A first note can be created by adding an `.mdx` file in the `notes` directory with frontmatter and content.
- The project is open source, and the author invites feedback, contributions, and bug reports.
- The author says Notion worked well for about a year, but it was slow.
- SnippetsLab, Quiver, and Boostnote were fast and useful for code snippets, but notes were less accessible and had no preview.
