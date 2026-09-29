---
title: "Um exemplo prático da importância da lei de Conway"
date: '2020-07-06T21:22:22-03:00'
category: webclip
summary: 'A lei de Conway mostra que a arquitetura de software tende a refletir a estrutura de comunicação da empresa. O texto liga organização de times, base de dados, deploy e acoplamento entre componentes.'
tags: ["lei-de-conway", "arquitetura-de-software", "times", "estrutura-organizacional"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Um exemplo prático da importância da lei de Conway - EximiaCo"
    url: "https://www.eximia.co/pt/2020/07/06/um-exemplo-pratico-da-importancia-da-lei-de-conway/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-07/eximia-co--um-exemplo-pratico-da-importancia-da-lei-de-conway.md"
    kind: repo
---

A lei de Conway é apresentada como uma regra prática para pensar arquitetura de software e organização de times. O texto afirma que, com o tempo, a estrutura do software tende a repetir a estrutura de comunicação da empresa que o desenvolve.

Em um cenário com três squads por área de negócio, um núcleo corporativo para bancos de dados e um time para operação, a página prevê três contextos bem delimitados no backend, uma base única e monolítica para o conjunto do software e deploy combinado entre todos os times. Também aponta que conversas incentivadas em ferramentas e ritos da organização aumentam a chance de acoplamento entre componentes. A conclusão é que o design da estrutura organizacional precisa ser compatível com o tipo de arquitetura desejada, incluindo a diluição de núcleos centrais quando se quer reduzir monólito e permitir deploy independente.

## Fichamento

- A lei de Conway é usada para mostrar que a arquitetura do software tende a reproduzir a comunicação da empresa.
- Com três squads por área de negócio, um núcleo corporativo de bancos de dados e um time de operação, a solução tende a refletir essa divisão.
- O texto prevê três contextos fortes no backend, com código próprio para cada frontend, mas sem fácil acesso externo.
- A base de dados tende a virar uma estrutura única, compartilhada, acoplada e monolítica, servindo como gargalo de evolução.
- O deploy tende a ser combinado, em formato tudo ou nada, envolvendo as entregas de todos os times.
- Pela teoria das restrições, o ritmo das entregas tende a ser definido pelo time menos eficiente.
- Conversas incentivadas em ferramentas de comunicação ou ritos da organização aumentam a chance de acoplamento entre componentes.
- Se a intenção for evitar base monolítica e permitir deploy independente, o núcleo de DBA e o núcleo de operações precisam ser diluídos nas squads.
- Se a organização quiser oferecer uma experiência externa consistente e consolidada, o texto indica a necessidade de uma equipe responsável por isso.
- O CTO precisa garantir que a estrutura dos times seja compatível com a arquitetura pretendida.
