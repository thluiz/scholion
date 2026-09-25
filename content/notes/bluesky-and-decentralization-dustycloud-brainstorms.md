---
title: "Bluesky and Decentralization -- Dustycloud Brainstorms"
date: '2026-09-25T08:28:25+01:00'
category: webclip
summary: 'The post argues that Bluesky uses useful decentralization techniques and credible exit, but is not decentralized or federated under the author’s definitions, and that full self-hosting would create quadratic scaling costs.'
tags: ["bluesky", "decentralization", "activitypub", "atproto"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bluesky and Decentralization -- Dustycloud Brainstorms"
    url: "https://dustycloud.org/blog/re-re-bluesky-decentralization/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dustycloud-org--bluesky-and-decentralization-dustycloud-brainstorms.md"
    kind: repo
---

The post responds to Bryan Newbold’s reply and says the exchange was generally polite and worthwhile. It also frames the larger disagreement as one of terminology, because the author thinks Bluesky’s use of decentralization language moves the goalposts and hides the role of power distribution in the network.

A central claim is that ATProto’s public shared-heap model does not scale well toward meaningful self-hosting. The author argues that message-passing systems can keep per-node costs flat while a fully decentralized shared-heap system makes each node receive all messages, producing quadratic whole-network costs. The post also contrasts Bluesky’s goals with ActivityPub and Spritely, and says credible exit is valuable but not enough to make the system decentralized.

## Fichamento

- O texto responde à réplica de Bryan Newbold e diz que a troca foi respeitosa, mas mantém as críticas técnicas e conceituais ao Bluesky.
- O autor sustenta que as definições usadas por Bryan e por Mark Nottingham enfraquecem demais “decentralization” e “federation” porque deixam de lado a distribuição de poder.
- A discussão sobre Paul Baran aparece para mostrar que a definição citada por Bryan vinha de um contexto em que “decentralized” ainda era um tipo de centralização hierárquica.
- O post afirma que “credible exit” é útil, mas não basta para chamar o sistema de descentralizado.
- O autor defende que ActivityPub e sistemas de message passing escalam melhor quando a rede cresce e quando mais nós entram no sistema.
- Para ATProto, ele argumenta que a arquitetura de shared heap com firehose público impõe custos quadráticos quando se tenta levar a descentralização até a participação plena dos usuários.
- O texto diz que self-hosting real exigiria mudanças fundamentais na arquitetura, aproximando o sistema de algo mais parecido com ActivityPub.
- Há uma distinção entre os valores e objetivos declarados por Bluesky, ActivityPub e Spritely, com ênfase em controle de dados, agência, colaboração e comunidades saudáveis.
- O fechamento afirma que o autor não quer seguir em um vai-e-vem infinito e prefere colaborar em soluções que construam o futuro.
