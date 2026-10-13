---
title: "Part 8 - Sharing Code Options | xamarin"
date: '2013-08-05T13:53:05-03:00'
category: webclip
summary: 'The page compares four ways to share C# code across iOS, Android, and Windows Phone projects, listing how each one works and the tradeoffs in setup, syncing, and tooling.'
tags: ["file-linking", "shared-code", "xamarin", "project-linker"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 8 - Sharing Code Options | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/sharing_code_options"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-8-sharing-code-options-xamarin.md"
    kind: repo
---

The page compares four ways to share C# source files across iOS, Android, and Windows Phone projects. It says file linking, linked library projects, cloned project files, and Microsoft’s Project Linker all support shared code, but each method differs in setup, directory layout, and how much manual synchronization is needed.

## Reading notes

- File linking lets each app project point to the same source files in a separate directory.
- Shared files can be edited once and used by all linked projects, but added, moved, or deleted files must be updated by hand everywhere.
- Visual Studio requires choosing Add As Link; otherwise it copies the file into the target project.
- Xamarin Studio can detect files outside the project directory and offer to add them as links.
- File linking works for all platforms and can be split into separate library projects for larger apps.
- Linked projects need empty folder structures on disk so the linked paths exist.
- Cloned project files keep the shared files in the same directory as the project files and use direct file references instead of links.
- Cloned projects also require manual updates when files change, but Xamarin Studio can re-add a folder tree more easily.
- Microsoft’s Project Linker can synchronize multiple project files automatically, but Xamarin does not officially support it.
- The summary says Portable Class Libraries are the simplest option, while file linking and cloned project files are simpler to create but need constant manual intervention.
