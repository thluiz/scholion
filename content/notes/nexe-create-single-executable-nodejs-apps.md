---
title: "nexe"
date: '2026-09-25T08:53:44+01:00'
category: webclip
summary: 'Nexe compiles Node.js applications into a single executable. The page highlights self-contained binaries, idempotent builds, resources added to the bundle, and compilation options and API.'
tags: ["nodejs", "cli", "executable", "build"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - nexe/nexe: 🎉 create a single executable out of your node.js apps"
    url: "https://github.com/crcn/nexe?utm_source=nodeweekly&utm_medium=email"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/github-com--nexe-create-single-executable-nodejs-apps.md"
    kind: repo
---

Nexe is a command-line utility that compiles a Node.js application into a single executable file. The page presents it as a way to distribute binaries without Node or npm, run apps with different runtimes, and control builds across platforms.

## Reading notes

- Compiles Node.js applications into a single executable.
- Allows distributing binaries without needing Node or npm.
- Supports self-contained applications and multiple applications with different runtimes.
- Mentions idempotent builds, faster deploys, version rollback, and a flexible build pipeline.
- Supports cross-platform builds.
- Allows adding resources to the binary with `-r` and reading them with `fs.readFile` or `fs.readFileSync`.
- By default it tries to download a precompiled executable; if necessary, it uses `--build` to compile from source code.
- Documents options such as `input`, `output`, `target`, `bundle`, `name`, `cwd`, `build`, `resources`, `patches` and `plugins`.
- The Node.js API shows `compile({ input, build: true, patches: [...] })` and the use of `setFileContentsAsync` to modify source files.
- For native modules, the native binaries need to be sent together with the generated executable.
