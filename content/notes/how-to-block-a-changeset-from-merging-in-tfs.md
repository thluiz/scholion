---
title: "How to block a changeset from merging in TFS?"
date: '2016-12-14T17:54:31-03:00'
category: webclip
summary: 'The question asks whether TFS 2010 can mark a changeset so it will not appear in the Visual Studio merge wizard and will look already merged into another branch.'
tags: ["tfs", "merge", "changeset"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to block a changeset from merging in TFS?"
    url: "http://stackoverflow.com/questions/4024919/how-to-block-a-changeset-from-merging-in-tfs"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-12/stackoverflow-com--how-to-block-a-changeset-from-merging-in-tfs.md"
    kind: repo
---

The question asks whether TFS 2010 can mark a changeset so it cannot be merged from one branch to another, including in the Visual Studio merge wizard when using Selected changesets. The goal is to make the changeset appear as if it had already been merged into another branch.

It explains that the build process auto-increments version numbers in all AssemblyInfo.cs files, so a changeset in a release branch that contains only version increments should not be merged into trunk or another release branch. The post compares this need to TortoiseSVN’s "Only record the merge (block revisions from getting merged)" option.

## Reading notes

- In TFS 2010, the user wants a way to mark a changeset so it cannot be chosen for merge from one branch to another.
- The changeset should be hidden from the Visual Studio merge wizard when using the Selected changesets option.
- The desired effect is that the changeset looks as if it had already been merged into another branch.
- The motivation is that build automation increments version numbers in AssemblyInfo.cs files.
- Changesets in a release branch that contain only version increments should stay out of trunk and other release branches.
- The request is compared to TortoiseSVN’s option to record a merge and block revisions from being merged.
