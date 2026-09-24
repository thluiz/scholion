---
title: "Bytes #328 - Bloomberg's new TypeScript framework"
date: '2026-09-24T23:08:02+01:00'
category: webclip
summary: 'Issue da Bytes destaca o Stricli, novo framework TypeScript da Bloomberg para CLIs com tipagem completa, zero dependências e suporte a ESM e CommonJS, além de vários links curtos de ferramentas e notícias.'
tags: ["typescript", "cli", "bloomberg", "viteconf"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bytes #328 - Bloomberg's new TypeScript framework"
    url: "https://bytes.dev/archives/328?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/bytes-dev--bytes-328-bloombergs-new-typescript-framework.md"
    kind: repo
---

The issue highlights Stricli, a new Bloomberg framework for building complex CLIs with TypeScript. It is presented as a way to keep type safety while avoiding extra dependencies and unnecessary complexity. The issue also notes that Stricli supports ESM and CommonJS, and that its scope is intentionally limited, so other packages are needed for prompts, terminal styling, and similar features.

## Fichamento

- A Bloomberg lançou o Stricli, um framework para construir CLIs complexas com TypeScript, segurança de tipos e zero dependências.
- O texto contrasta o Stricli com ferramentas como oclif e clipanion, dizendo que elas podem trazer dependências e complexidade a mais para alguns usos.
- O framework oferece suporte completo a TypeScript, com tipos definidos uma vez para flags nomeadas e argumentos posicionais que atravessam a aplicação.
- Ele também suporta ESM e CommonJS, além de facilitar code splitting com ferramentas de build ESM e autocomplete dinâmico.
- O projeto evita dependências em tempo de execução e centraliza o acesso ao sistema em um objeto de contexto, com injeção de dependência opcional.
- A limitação assumida é que o escopo do Stricli é mais restrito, então prompts interativos, estilo no terminal e recursos parecidos ficam por conta de outros pacotes.
- O restante da edição menciona ViteConf ao vivo, Zod.fyi para visualizar issues em `ZodError`, ESLint com suporte oficial a JSON e Markdown, Eleventy v3.0 com ESM e Deno, Tauri 2.0 e VoidZero.
