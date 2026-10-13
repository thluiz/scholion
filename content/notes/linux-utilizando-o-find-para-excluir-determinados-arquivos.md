---
title: "Linux: Utilizando o find para excluir determinados arquivos [Dica]"
date: '2012-06-28T11:10:29-03:00'
category: webclip
summary: 'Mostra um comando find para localizar arquivos .log dentro de /teste e excluí-los diretamente com -delete.'
tags: ["linux", "find", "arquivos-log"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Linux: Utilizando o find para excluir determinados arquivos [Dica]"
    url: "http://www.vivaolinux.com.br/dica/Utilizando-o-find-para-excluir-determinados-arquivos/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/vivaolinux-com-br--linux-utilizando-o-find-para-excluir-determinados-arquivos.md"
    kind: repo
---

Mostra um comando find para localizar arquivos .log dentro de /teste e apagá-los com -delete.

## Fichamento

- Usa `find /teste -name '*.log' -delete` para procurar arquivos `.log` na árvore de `/teste` e removê-los.
