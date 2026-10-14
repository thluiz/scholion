---
title: "Dica Git da semana: Merging"
date: '2012-04-25T16:57:47-03:00'
category: webclip
summary: 'O texto explica como o Git torna branches e merging práticos, como um merge traz vários commits para o branch atual e como resolver conflitos antes de confirmar o resultado.'
tags: ["git", "branches", "merging", "merge-conflicts"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dica Git da semana: Merging"
    url: "http://imasters.com.br/artigo/24228/desenvolvimento/dica-git-da-semana-merging"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/imasters-com-br--dica-git-da-semana-merging.md"
    kind: repo
---

A página diz que o Git torna branching e merging baratos o bastante para entrarem no fluxo de trabalho diário. Também descreve o padrão de criar um branch de recurso, fazer commits durante a implementação e depois voltar ao master para fazer o merge.

## Fichamento

- O Git permite usar branches como parte normal do desenvolvimento porque branching e merging são baratos.
- Um merge traz mais de um commit para o branch atual, e os commits envolvidos podem ser nomes de branches ou qualquer hash no repositório.
- Um fluxo comum é criar um branch de recurso, fazer commits enquanto a funcionalidade é implementada e depois voltar ao master para fazer o merge do branch.
- Se não houver problemas, o git merge cria um commit automaticamente.
- Se o mesmo arquivo mudar em commits divergentes, pode surgir um conflito de merge.
- Conflitos são resolvidos editando o arquivo, removendo os marcadores, tratando um conflito de cada vez e executando git add.
- git status mostra os arquivos com conflitos de merge separadamente.
- Ao final, git commit registra as alterações, e o commit resultante tem dois pais nos metadados.
