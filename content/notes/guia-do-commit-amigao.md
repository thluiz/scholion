---
title: "Guia do Commit Amigão"
date: '2017-10-11T11:33:15-03:00'
category: webclip
summary: 'A página defende uma convenção para mensagens de commit para facilitar a leitura do histórico, manter o time alinhado, preservar contexto e ajudar na manutenção e no changelog.'
tags: ["mensagens-de-commit", "git-log", "convencao-de-codigo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "BeeTech-global/bee-stylish"
    url: "https://github.com/BeeTech-global/bee-stylish/blob/master/commits/README.md"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-10/github-com--guia-do-commit-amigao.md"
    kind: repo
---

A página defende que uma convenção compartilhada para mensagens de commit torna o histórico mais fácil de navegar, ajuda a manter um padrão entre desenvolvedores, preserva o contexto da mudança, melhora a manutenção do projeto no longo prazo e facilita a geração de changelog. Também apresenta uma estrutura de commit com tipo, escopo, assunto, corpo e rodapé.

## Fichamento

- Sem padrão, o `git log` fica difícil de ler e de explorar.
- O time deve combinar uma convenção para estilo, conteúdo e metadados.
- O estilo deve tratar de sintaxe, gramática, capitalização e pontuação.
- O conteúdo deve informar o que e por que mudou, e não como foi feito.
- Os metadados devem registrar referências de issues, IDs ou pull requests.
- O formato proposto é `<tipo>(escopo): assunto`, seguido de corpo e rodapé.
- O assunto deve ter no máximo 50 caracteres, ficar em minúsculas e usar imperativo.
- Os tipos permitidos são feat, style, refactor, test, fix, docs e chore.
- O corpo deve ter no máximo 80 caracteres e contextualizar a mudança.
- O rodapé serve para indicar metadados, como issues encerradas pelo commit.
