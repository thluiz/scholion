---
title: "Aventuras com armas em jogos com terceira pessoa"
date: '2012-05-07T11:29:53-03:00'
category: webclip
summary: 'O texto explica problemas de disparo em jogos de terceira pessoa e descreve a solução usada em Monday Night Combat: três rastreamentos separados para câmera, arma e mão, equilibrando mira, colisão e efeitos visuais.'
tags: ["third-person-shooters", "raycasting", "gameplay", "monday-night-combat"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Aventuras com armas em jogos com terceira pessoa"
    url: "https://imasters.com.br/desenvolvimento/aventuras-com-armas-em-jogos-com-terceira-pessoa"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/imasters-com-br--aventuras-com-armas-em-jogos-com-terceira-pessoa.md"
    kind: repo
---

O texto discute como jogos de tiro em terceira pessoa criam conflitos entre a câmera do jogador, a posição da arma e a geometria do cenário. Em Monday Night Combat, a solução combina rastreamentos da câmera, da arma e da mão para manter a mira coerente, evitar tiros abusivos através de coberturas e preservar o comportamento esperado de cada disparo.

## Fichamento

- Em jogos de terceira pessoa, a câmera fica atrás e acima do ombro, e a distância entre câmera, personagem e ponta do cano afeta o disparo.
- Um rastreamento que começa na câmera funciona melhor para a percepção do jogador, mas sozinho permite tiros através da geometria do mundo.
- Mover a origem do rastreamento para o cano da arma faria a mira deixar de corresponder ao ponto atingido.
- Em Monday Night Combat, a solução foi fazer um rastreamento inicial da câmera até o mundo e depois um rastreamento secundário da arma até o alvo encontrado.
- Se o rastreamento da arma falha por causa de uma parede perto do personagem, o novo ponto de alvo passa a ser usado.
- Quanto maior a distância entre a mira na tela e a ponta do cano, mais vezes o rastreamento da arma falha; armas no ombro sofrem menos com isso do que armas na altura do quadril.
- Há casos extremos em que o rastreamento da câmera acerta um inimigo, mas o rastreamento da arma bate na geometria e nenhum dano é causado.
- Para reduzir esse problema, o rastreamento da arma usa um limite máximo de distância, testado em cerca de sete metros.
- Efeitos visuais continuam partindo do cano, então o disparo pode parecer atravessar a geometria mesmo quando o dano é resolvido corretamente.
- Em armas penetrantes, como fuzil de precisão e railgun, o jogo usa um único rastreamento da arma até o alvo mais distante para decidir o dano de múltiplos acertos.
- Alguns problemas continuam quando a arma fica do outro lado da colisão do personagem ou do cenário, o que levou ao uso de um terceiro rastreamento da mão até a ponta do cano.
- O texto resume a solução de MNC como três rastreamentos: mão, câmera e arma.
- Outros jogos tratam o disparo de formas diferentes, como efeitos que nascem da testa, do cano ou do nariz, e cada um resolve cobertura e visual de modo próprio.
- O autor conclui que não existe uma fórmula única e que a solução de disparo depende do equilíbrio entre jogabilidade, colisão e efeitos visuais.
