---
title: "Um pouco sobre DDD - Domain Events"
date: '2015-08-31T09:59:24-03:00'
category: webclip
summary: 'O texto define Domain Events como mensagens sobre algo relevante para o domínio e mostra um exemplo em que uma encomenda gera ações como salvar no banco e enviar emails.'
tags: ["domain-events", "ddd", "csharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Um pouco sobre DDD - Domain Events"
    url: "http://viniciusmussak.net/2015/08/30/domain-events/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/viniciusmussak-net--um-pouco-sobre-ddd-domain-events.md"
    kind: repo
---

Domain Events são apresentados como parte do DDD e como eventos que fazem sentido para o domínio. O texto os descreve como mensagens sobre algo que aconteceu no passado e que interessa ao negócio, usadas para separar preocupações técnicas do domínio.

## Fichamento

- Domain Events fazem parte do DDD e servem para ocasiões em que aconteceu algo que especialistas do domínio se preocupam.
- Eles são eventos que fazem sentido para o domínio, ligados a situações que precisam acontecer quando uma ação ocorre.
- O texto os define como mensagens que descrevem algo ocorrido no passado e de interesse do negócio.
- A ideia é separar as preocupações técnicas do domínio.
- O exemplo usa um sistema de encomendas e cria a classe EncomendaRealizada para representar uma nova encomenda.
- O autor diz que uma interface vazia como IDomainEvent ainda faz sentido no DDD porque o evento tem um papel explícito na aplicação.
- Os eventos são disparados por meio de uma classe estática comum, com auxílio de um container de injeção de dependência.
- A interface IHandle é usada para tratar o evento, e o método Handle executa o que deve acontecer quando ele é disparado.
- No exemplo, o evento EncomendaRealizada precisa salvar no banco e enviar emails para a transportadora e para o cliente.
- O código de exemplo está disponível no GitHub.
