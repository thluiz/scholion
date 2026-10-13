---
title: "Métricas para Projetos Agile #6"
date: '2017-04-17T15:54:40-03:00'
category: webclip
summary: 'O e-mail apresenta o lead time breakdown como forma de detalhar cada etapa do desenvolvimento, identificar filas e gargalos, e apoiar melhorias no fluxo com dados.'
tags: ["lead-time-breakdown", "metricas-ageis", "kanban", "eficiencia-de-processo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Métricas para Projetos Agile #6"
    url: "https://mail.google.com/mail/u/0/#inbox/15b773d1df3c22fd"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-04/mail-google-com--metricas-para-projetos-agile-6.md"
    kind: repo
---

O e-mail apresenta o lead time breakdown como uma forma de segmentar o lead time e observar a latência entre o início e o fim de cada etapa do desenvolvimento em cada item de trabalho. A proposta é dar ao time uma visão mais detalhada que o CFD para evidenciar problemas do processo mais cedo.

## Fichamento

- A métrica serve para responder o que está acontecendo com os itens em progresso, se existe impedimento e se há gargalo no fluxo, como sobrecarga na etapa de testes.
- A visualização usa dias de trabalho no eixo vertical, itens de trabalho no eixo horizontal e barras acumuladas para representar cada etapa do processo.
- No exemplo, o tempo alto de revisão, a variação na etapa de desenvolvimento e as barras de espera por testes mostram atraso na revisão, pouca padronização nas histórias e baixa disponibilidade de teste.
- A eficiência do fluxo é definida como o somatório das etapas em que houve trabalho dividido pelo lead time total.
- A etapa de espera, como “Aguardando Teste”, não entra no cálculo de eficiência.
- O uso do gráfico em daily ou em eventos frequentes ajuda a discutir desperdícios, propor melhorias com base em dados, deixar o tempo de espera visível e apoiar retrospectivas sobre o processo.
