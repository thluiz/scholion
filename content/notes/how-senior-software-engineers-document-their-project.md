---
title: "How Senior Software Engineers Document Their Project"
date: '2026-09-25T00:25:18+01:00'
category: webclip
summary: 'The article argues that ADRs help teams record architectural changes, their impact, and what was learned, so future developers can understand decisions and avoid relying on memory.'
tags: ["software-documentation", "adr", "architecture", "team-process"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Senior Software Engineers Document Their Project"
    url: "https://dev.to/koladev/how-senior-software-engineers-document-their-project-1nf4?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-senior-software-engineers-document-their-project.md"
    kind: repo
---

The article says software engineers often dislike documentation, but documenting project decisions is what helps teams remember why an architecture was chosen. It presents ADRs, or Architectural Decision Records, as a way to track changes, impacts, and lessons learned.

It also says ADRs can live in a repository, Notion, or JIRA, and that linking changes to issues can help teams remember technical decisions months or years later.

## Fichamento

- O texto defende que documentar decisões de arquitetura ajuda porque a memória falha com o tempo.
- ADR significa Architectural Decision Record e serve para registrar a mudança feita, o impacto dela e o que foi aprendido.
- O autor compara o ADR a um diário pessoal, mas usado pela equipe.
- O texto diz que documentar mudanças ajuda outros desenvolvedores a entender por que uma escolha foi feita, inclusive quem entra depois no projeto.
- O autor descreve um projeto fintech em que a equipe avançou rápido e não priorizou planejamento de escalabilidade.
- Ele diz que, ao pesquisar, encontrou o ADR como uma convenção de documentação que lhe agradou.
- O texto mostra um modelo de ADR com contexto, problema, fatores de decisão, opções consideradas, resultado da decisão, consequências, confirmação, prós e contras e mais informações.
- Também afirma que esse tipo de documento pode ficar no repositório do projeto, no Notion ou no JIRA.
- O autor relata que, na empresa anterior, usavam issues do GitLab e ligavam cada mudança a uma branch para acompanhar os motivos das alterações.
- A conclusão do texto reforça que ADRs ajudam líderes de time, colegas e pessoas que chegam depois a entender decisões técnicas passadas.
