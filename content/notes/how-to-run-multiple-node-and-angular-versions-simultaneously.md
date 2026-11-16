---
title: "How to run multiple Node and Angular versions simultaneously"
date: '2020-04-20T21:22:36+00:00'
category: webclip
summary: 'The article shows how to keep separate Node versions with nvm and use the local Angular CLI from each project, so each app runs with its matching toolchain.'
tags: ["node", "angular-cli", "nvm", "version-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to run multiple Node and Angular versions simultaneously"
    url: "https://dev.to/patricepeartree/how-to-run-multiple-node-and-angular-versions-simultaneously-3lfj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-run-multiple-node-and-angular-versions-simultaneously.md"
    kind: repo
---

The article argues that switching between projects with different Node and Angular requirements is easier if each project keeps its own Node version and uses its local Angular CLI. It points out that Angular CLI is recorded in package.json, while Node version needs to be documented, and suggests nvm plus local CLI binaries as the practical setup.

## Reading notes

- nvm can install multiple Node versions and use different versions in separate shells.
- A normal workflow is to install each project's Node version and run it in an independent shell for that project.
- Example projects XPTO and EPIC use Node 8.17.0 and 12.16.1.
- The command `nvm use` sets the Node version for the current shell session, not only for one directory.
- A new shell starts with the default nvm Node version unless something else is configured.
- The `.nvmrc` file lets a directory specify the Node version nvm should use there and in subdirectories.
- The article says to use nvm commands such as `nvm run` and `nvm exec` so the `.nvmrc` file is applied.
- For Angular projects, the correct CLI version should come from the project's local `node_modules` folder.
- Angular CLI is added as a development dependency in `package.json`.
- One option is to use `package.json` scripts, since `npm run-script` adds `node_modules/.bin` to PATH for the script.
- Adding `"ng": "ng"` as a script allows direct `npm run ng` use of the local Angular CLI.
- Another option is to run `./node_modules/.bin/ng` directly.
- The article concludes that using nvm together with local Angular CLI binaries makes it possible to manage multiple versioned projects in a straightforward way.
