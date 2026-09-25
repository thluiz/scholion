---
title: "How to Make Software Engineers Do the 'Right Thing'"
date: '2026-09-25T09:04:25+01:00'
category: webclip
summary: 'O texto propõe prioridades para criar cultura de responsabilidade em times de engenharia: registrar bugs, fazer RCA sem culpa, manter CI verde, acompanhar logs e reforçar melhoria contínua.'
tags: ["engenharia-de-software", "cultura-de-equipe", "qualidade-de-software", "ci"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Make Software Engineers Do the 'Right Thing'"
    url: "https://hackernoon.com/how-to-make-software-engineers-do-the-right-thing?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hackernoon-com--how-to-make-software-engineers-do-the-right-thing.md"
    kind: repo
---

The text argues that teams should build a culture of ownership and accountability so engineers treat quality and stability as priorities, not side work. It says this starts with recording and tracking production bugs, writing blameless RCAs, keeping CI green, and monitoring system health.

It also says these practices need repetition, clear ownership, public alerts, and team-wide responsibility. Over time, the goal is a culture where fixing alerts, broken builds, and bugs is treated as the team’s highest priority.

## Fichamento

- Defende que a base é criar uma cultura de ownership e accountability, e que isso precisa começar de imediato.
- Diz que equipes muitas vezes não registram nem priorizam bugs e defeitos em produção, o que dificulta discutir trocas entre qualidade, estabilidade e novas features.
- Propõe RCAs ou incident reports para issues importantes, com foco sem culpa, transparência, aprendizado e autonomia.
- Afirma que dívida técnica está na raiz de muitos problemas e que RCAs ajudam a priorizar correções e follow-ups frente a outros trabalhos.
- Sustenta que um build contínuo e verde no CI é essencial, e que testes flaky devem ser excluídos até serem corrigidos, com ownership claro sobre eles.
- Diz que saúde do sistema e logs exigem esforço de todo o time, com thresholds acordados, alertas em canal público e resposta ativa a problemas.
- Recomenda documentar os princípios, workshop com o time, alinhamento com produto e stakeholders, e cobrança contínua de melhoria.
- Lista como próximos passos melhorar testes, acelerar builds, reduzir handoffs, shift left da qualidade, colaborar melhor com produto e design e medir qualidade, uptime e cycle time.
