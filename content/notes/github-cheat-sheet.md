---
title: "GitHub Cheat Sheet"
date: '2015-02-10T12:28:34-03:00'
category: webclip
summary: 'A collection of Git and GitHub features and shortcuts, showing URL tweaks, branch comparison, gists, markdown rendering, issue handling, and local git commands.'
tags: ["github", "git", "cheat-sheet", "workflow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "tiimgreen/github-cheat-sheet"
    url: "https://github.com/tiimgreen/github-cheat-sheet"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/github-com--github-cheat-sheet.md"
    kind: repo
---

A collection of hidden and visible Git and GitHub features, organized as a cheat sheet. It covers URL parameters, branch and commit views, gists, GitHub writing features, issue workflows, and local Git commands.

## Reading notes

- Adding `?w=1` to a diff URL removes whitespace-only changes.
- Adding `?ts=4` to a diff or file URL changes tab width, though not on Gists or raw file views.
- Adding `?author={user}` to a commits URL filters commits by author.
- A repository URL can omit the `.git` suffix when cloning.
- The repository's Branches page lists branches not merged into the main branch and lets you compare or delete them.
- GitHub compares branches with `/compare/{range}`, including date-based ranges and `.diff` or `.patch` views.
- Forked repositories can be compared with `/compare/{foreign-user}:{branch}...{own-branch}`.
- Gists can be cloned, pushed to, and opened as HTML-only pages with `.pibb`.
- `git.io` shortens GitHub URLs and can be used with `curl`.
- Keyboard shortcuts on repository pages include `t`, `w`, `s`, `l`, `y`, and `?`.
- Line numbers or `#L52` style fragments highlight lines and ranges in code files.
- Commit messages with `fix`, `close`, or `resolve` keywords can close issues.
- Issues can auto-link with `#` or `user/repo#ISSUE_NUMBER`.
- Owners and collaborators can lock conversations in pull requests and issues.
- Travis CI can build pull requests, and the page points to the commit status API.
- Markdown code fences support syntax highlighting through GitHub's Linguist.
- Emojis can be used in issues, pull requests, and commit messages with `:name_of_emoji:`.
- Images and GIFs can be embedded in comments and READMEs, and GitHub caches them.
- Wiki pages can embed images with height or width settings.
- Pressing `r` in a comment thread quotes selected text into a block quote.
- Chrome users can paste clipboard images into comments for auto-upload.
- GitHub offers quick license templates for new repositories and existing ones, including `.gitignore`.
- Task lists work in issues and pull requests, and read-only task lists also work in full Markdown documents.
- Relative links are recommended in Markdown because they survive URL changes.
- GitHub Pages can expose repository metadata through `site.github`, and Jemoji plus jekyll-mentions work in posts and pages.
- GitHub renders YAML metadata at the top of documents as a horizontal table.
- GitHub supports tabular data in `.csv` and `.tsv` files.
- A merged pull request can be reverted from the Revert button.
- Rendered prose diffs, diffable maps, and expanding context are available in diffs.
- Pull requests can be viewed as `.diff` or `.patch`.
- GitHub renders common image formats and compares image versions.
- Hub adds command-line helpers for GitHub workflows.
- Adding a `CONTRIBUTING` file links it for issue and pull request authors.
- Octicons are open sourced.
- `git checkout -` switches to the previous branch.
- `git stripspace` strips trailing whitespace, collapses newlines, and adds a final newline.
- Pull requests can be fetched locally through `refs/pull/[PR-Number]/head` or a broader refspec.
- Empty commits can be created with `--allow-empty` for annotation and communication.
- `git status -sb` shows a shorter status view.
- A styled `git log` command is shown, along with a `git show :/query` search for recent commit messages.
- `git branch --merged` and `git branch --no-merged` list merged and unmerged branches.
- `--fixup` and `--autosquash` help correct earlier commits.
- `git instaweb` starts a web view of the local repository.
- `.gitconfig` aliases, auto-correct, and color settings are presented as configuration examples.
