---
title: "Dados distribuídos — Particionamento/Sharding"
date: '2020-08-26T19:31:16+00:00'
category: webclip
summary: 'A página explica como particionamento e sharding ajudam a escalar bancos de dados, mostra por que estratégias ingênuas geram hot spots e resume os custos de joins e índices secundários distribuídos.'
tags: ["particionamento", "sharding", "hot-spots", "indices-secundarios"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dados distribuídos — Particionamento/Sharding"
    url: "https://dev.to/brenoferreira/dados-distribuidos-particionamento-sharding-pip"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--dados-distribuidos-particionamento-sharding.md"
    kind: repo
---

O texto apresenta o particionamento, ou sharding, como uma técnica para aumentar a escalabilidade de bancos de dados com conjuntos de dados muito grandes e alto volume de queries. Também mostra que a escolha da chave de particionamento é decisiva, porque uma divisão ingênua pode concentrar acesso em uma única partição.

## Fichamento

- Particionamento, também chamado de sharding, é usado para escalar bancos de dados com muitos dados e muitas consultas.
- Estratégias simples de particionamento podem criar hot spots, com uma partição recebendo a maior parte dos acessos enquanto as outras ficam quase paradas.
- Particionar por username em uma rede social pode concentrar usuários muito acessados na mesma partição quando as iniciais mais comuns se acumulam.
- Particionar por data também pode criar hot spots quando quase toda a escrita cai em uma partição específica em cada dia.
- Particionar por hash ajuda a distribuir melhor os dados entre as partições e reduz, mas não elimina, hot spots.
- Em bancos relacionais, joins distribuídos entre vários nós tendem a ficar menos eficientes.
- Índices secundários ficam mais difíceis de usar com partições, porque os dados relevantes podem estar espalhados.
- Com índices secundários locais, a consulta precisa consultar cada partição em uma operação de scatter/gather, que costuma ser lenta.
- Com um índice global particionado, a busca melhora porque o índice aponta para as partições corretas, mas a escrita piora porque o índice precisa ser atualizado a cada escrita.
- A atualização assíncrona de um índice distribuído sofre com replication lag, e mantê-lo fortemente consistente exige uma transação distribuída cara.
