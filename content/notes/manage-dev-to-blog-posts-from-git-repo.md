---
title: "Manage your dev.to blog posts from a GIT repo and use continuous deployment to auto publish/update them"
date: '2019-07-09T09:50:06+00:00'
category: webclip
summary: 'The post shows how to keep dev.to articles in a Git repo, track them in `dev-to-git.json`, and use CI to publish or update posts automatically from Markdown.'
tags: ["devto", "continuous-deployment", "github-actions", "travis"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Manage your dev.to blog posts from a GIT repo and use continuous deployment to auto publish/update them"
    url: "https://dev.to/maxime1992/manage-your-dev-to-blog-posts-from-a-git-repo-and-use-continuous-deployment-to-auto-publish-update-them-143j"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--manage-dev-to-blog-posts-from-git-repo.md"
    kind: repo
---

The post explains a workflow for storing dev.to articles in Git, so edits are versioned and updates can be deployed automatically. It says this makes it easier to edit safely, use formatting tools, keep a history, accept pull requests, and manage code examples alongside the article. An update at the top says Travis is no longer recommended and GitHub Actions is now the preferred CI runner.

## Reading notes

- The idea is to keep all dev.to posts in a Git repository and update them on dev.to when changes are merged.
- The author lists version control, safer editing, formatting with Prettier, pull requests from readers, and code examples managed with Embedme as reasons to do this.
- Setup is presented as a short process that can be done in a few minutes.
- The workflow can be added to an existing repository or started from a template repository.
- The main steps are to copy the template, create a dev.to token, pass the token to CI, and add the blog posts to the repository.
- The repository needs a `repository.url` in `package.json` so article images can be fetched from GitHub.
- A `dev-to-git.json` file at the project root maps each post `id` to a `relativePathToArticle`.
- To create the post ID, the author opens a draft on dev.to and reads the `data-article-id` from the browser console.
- The article files use front matter to store fields like `published`, `title`, `cover_image`, `tags`, `series`, and `canonical_url`.
- Local image links are rewritten so they point to remote files on GitHub.
- The top update says the template repo now uses GitHub Actions instead of Travis.
