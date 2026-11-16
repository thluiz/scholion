---
title: "Custom Site Generation with Azure Static Web Apps"
date: '2020-07-05T14:10:38+00:00'
category: webclip
summary: 'The post shows how Azure Static Web Apps can host a static site built by a custom generator, using GitHub Actions edits, Oryx behavior, and an F# script that turns CSV data into HTML.'
tags: ["azure-static-web-apps", "github-actions", "static-site-generator", "f-sharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Custom Site Generation with Azure Static Web Apps"
    url: "https://wizardsofsmart.wordpress.com/2020/06/04/custom-site-generation-with-azure-static-web-apps"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/wizardsofsmart-wordpress-com--custom-site-generation-with-azure-static-web-apps.md"
    kind: repo
---

The post explains that Azure Static Web Apps can work with more than the default npm build flow. Because the service commits a GitHub Actions workflow into the repository, the workflow can be edited safely to add a custom build step and change the app path used for deployment.

## Reading notes

- Azure Static Web Apps generates and commits the GitHub Actions workflow when the project is created.
- The committed workflow can be edited, so a custom build step can be added.
- Oryx tries to infer the app type and run the matching build commands.
- If Oryx cannot determine the app type, it treats the project as already built or as a plain static site.
- The example starts with a failed build because the application root was set to `/` while the static files were in `/src`.
- The workflow includes a section marked as safe to edit, with `######` comments showing the boundaries.
- Changing `app_location` from `/` to `src` makes the static deployment succeed.
- The site is a simple event registration form with an empty event drop-down.
- A `services.csv` file in the repository could be parsed with JavaScript libraries, but the post chooses a static generation approach instead.
- The added F# script reads the CSV, filters the services for the upcoming week, and writes modified HTML and other files to `/out`.
- The script uses AngleSharp, Deedle, and `dotnet fsi --langversion:preview`.
- After adding the generator, the workflow is updated again so `app_location` points to `out`.
- The workflow also adds a .NET Core setup step and a generate step before deployment.
- The result is a deployed form with event options generated from the CSV data.
- The post says Azure Static Web Apps may not support every static site generator directly, but it can still be used with custom tweaks to the workflow.
