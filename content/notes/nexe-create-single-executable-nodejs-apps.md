---
title: "nexe"
date: '2026-09-25T08:53:44+01:00'
category: webclip
summary: 'Nexe compila aplicações Node.js em um único executável. A página destaca binários autocontidos, builds idempotentes, recursos adicionados ao bundle e opções de compilação e API.'
tags: ["nodejs", "cli", "executavel", "build"]
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

## Fichamento

- Compila aplicações Node.js em um único executável.
- Permite distribuir binários sem precisar de Node ou npm.
- Aceita aplicações autocontidas e várias aplicações com runtimes diferentes.
- Menciona builds idempotentes, deploy mais rápido, rollback de versões e pipeline de build flexível.
- Suporta builds cross-platform.
- Permite adicionar recursos ao binário com `-r` e lê-los com `fs.readFile` ou `fs.readFileSync`.
- Por padrão tenta baixar um executável pré-compilado; se necessário, usa `--build` para compilar a partir do código-fonte.
- Documenta opções como `input`, `output`, `target`, `bundle`, `name`, `cwd`, `build`, `resources`, `patches` e `plugins`.
- A API Node.js mostra `compile({ input, build: true, patches: [...] })` e o uso de `setFileContentsAsync` para modificar arquivos da source.
- Para módulos nativos, os binários nativos precisam ser enviados junto com o executável gerado.
