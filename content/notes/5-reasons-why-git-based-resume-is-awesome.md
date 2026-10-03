---
title: "5 reasons why Git based resume is awesome"
date: '2018-05-01T16:00:53-03:00'
category: webclip
summary: 'The author argues that keeping a resume in GitHub makes it portable, easier to review through pull requests, simpler to customize, cheaper to manage, and free from dependence on a fixed document stack.'
tags: ["git", "resume", "github", "version-control"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "5 reasons why Git based resume is awesome"
    url: "https://dev.to/acro5piano/5-reasons-why-git-based-resume-is-awesome-127"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2018-05/dev-to--5-reasons-why-git-based-resume-is-awesome.md"
    kind: repo
---

The author keeps a resume on GitHub instead of using a normal document workflow. He says this fits how he already works with Git, helps with backup, and makes the resume easy to edit, share, and maintain across devices.

## Reading notes

- The resume is stored on GitHub and updated there, with Git used for version control and backup.
- Portability lets the author show and edit the resume from different computers, including someone else’s PC.
- A friend can review the repository, correct mistakes, and send a pull request, which the author merges after checking the diff.
- CSS knowledge makes layout changes easier, while tools like Sketch are mentioned as less suitable for writing the resume itself.
- Git reduces confusion about which file is the latest version, since Word-style filenames can multiply and become hard to trust.
- The author prefers any text editor and avoids MS Word’s interface and multi-click export flow.
- HTML, webpack, Chromium headless, or wkhtmltopdf can be used to build a PDF, and the build command can be added to an NPM script.
- The author wants to add CI, I18n for English and Japanese, and eventually a web page for the resume.
