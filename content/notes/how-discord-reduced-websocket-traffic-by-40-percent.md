---
title: "How Discord Reduced Websocket Traffic by 40%"
date: '2026-09-25T08:01:36+01:00'
category: webclip
summary: 'Discord reduced gateway bandwidth by replacing zlib with tuned zstandard, then cutting passive session snapshots with PASSIVE_UPDATE_V2, reaching almost 40% less traffic overall.'
tags: ["discord", "websocket", "compression", "bandwidth"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Discord Reduced Websocket Traffic by 40%"
    url: "https://discord.com/blog/how-discord-reduced-websocket-traffic-by-40-percent?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/discord-com--how-discord-reduced-websocket-traffic-by-40-percent.md"
    kind: repo
---

Discord first tested plain zstandard against zlib and found it worse, because zlib was using streaming compression while zstandard was not. After adding streaming support, tuning compression settings, and rolling it out across clients, zstandard outperformed zlib on ratio and compression time.

The team also tried zstandard dictionaries, but the gains were small or mixed and not worth the added complexity. A separate optimization, PASSIVE_UPDATE_V2, replaced full snapshots in passive sessions with deltas and cut that traffic from 35% to 5%, bringing the combined bandwidth reduction to almost 40%.

## Fichamento

- O texto descreve a tentativa de reduzir a largura de banda usada pelos clientes, sobretudo em iOS e Android, para tornar a experiência mais responsiva.
- O gateway já usava zlib com compressão desde o fim de 2017.
- A equipe avaliou zstandard como substituto, porque ele oferece melhores taxas de compressão, menor tempo de compressão e suporte a dicionários.
- O teste inicial usou um dark launch de zstandard sem streaming e o resultado ficou pior que o zlib.
- A diferença principal era que o zlib usava compressão em streaming e o zstandard não.
- Como as cargas eram pequenas, a ausência de histórico prejudicava o zstandard.
- A equipe escolheu ezstd, adicionou suporte a streaming por fork e depois contribuiu a mudança de volta ao projeto original.
- Com zstandard em streaming, a taxa de compressão e o tamanho dos payloads melhoraram, e o tempo de compressão caiu.
- A equipe então ajustou chainlog, hashlog e windowlog, escolhendo nível 6, chainlog 16, hashlog 16 e windowlog 18.
- O grupo também testou dicionários de zstandard com dados anonimizados de 120 mil mensagens, separados entre JSON e ETF.
- Os dicionários trouxeram ganhos pequenos no READY e resultados mistos em outros payloads.
- Por causa da complexidade extra, a equipe desistiu dos dicionários.
- Também houve um teste de aumentar buffers em horários de menor uso, mas a estratégia foi revertida por causa de fragmentação de memória e custo de ajuste.
- O rollout final levou zstandard para usuários desktop, iOS e Android, com bindings por plataforma e experimento para permitir rollback rápido.
- Em outra frente, o texto explica que PASSIVE_UPDATE_V1 enviava snapshots grandes para sessões passivas, mesmo quando pouca coisa mudava.
- A nova PASSIVE_UPDATE_V2 passou a enviar apenas o delta e reduziu esse tráfego de 35% para 5%.
- Somando zstandard e PASSIVE_UPDATE_V2, o texto diz que o uso de banda caiu quase 40%.
