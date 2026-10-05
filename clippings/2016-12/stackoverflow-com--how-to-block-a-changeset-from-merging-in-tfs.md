---
url: "http://stackoverflow.com/questions/4024919/how-to-block-a-changeset-from-merging-in-tfs"
captured_at: "2016-12-14T17:54:31-03:00"
title: "How to block a changeset from merging in TFS?"
domain: "stackoverflow-com"
---

# How to block a changeset from merging in TFS?

In TFS 2010, how can one mark a changeset so that it cannot be merged from one branch to another? For example, so it doesn't show in the "merge wizard" in Visual Studio when using the "Selected changesets" option. Basically, I want it to look like the changeset in question has already been merged into another branch.

Our build process auto-increments the version numbers in all our AssemblyInfo.cs files. A changeset in a release branch that contains only version increments should not be merged into trunk (or another release branch, of course).

I believe this is analogous to the "Only record the merge (block revisions from getting merged)" checkbox in TortoiseSVN.
