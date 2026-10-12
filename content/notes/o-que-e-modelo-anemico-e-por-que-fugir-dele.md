---
title: "O que é Modelo Anêmico? E por que fugir dele?"
date: '2014-04-04T10:23:26-03:00'
category: webclip
summary: 'O texto critica a separação rígida entre dados e comportamento na arquitetura em camadas, porque ela costuma espalhar regras de negócio, repetir código e dificultar a manutenção.'
tags: ["modelo-anemico", "arquitetura-em-camadas", "orientacao-a-objetos"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "O que é Modelo Anêmico? E por que fugir dele? | blog.caelum.com.br"
    url: "http://blog.caelum.com.br/o-que-e-modelo-anemico-e-por-que-fugir-dele/?Win8App=ModernReader"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-04/blog-caelum-com-br--o-que-e-modelo-anemico-e-por-que-fugir-dele.md"
    kind: repo
---

O texto diz que a separação entre modelo, regras de negócio e acesso a dados pode levar a um modo de programar procedural dentro de uma arquitetura orientada a objetos. Isso gera classes grandes, regras repetidas e código difícil de manter e evoluir.

## Fichamento

- A interação pouco clara entre classes traz repetição de código, dificuldade de manutenção e propagação de bugs.
- A arquitetura em camadas separa regras de negócio, atributos da entidade e acesso a dados.
- O texto afirma que, na prática, essa separação costuma produzir programação procedural.
- Nesse cenário, as regras de negócio ficam espalhadas e repetidas em muitas classes.
- Esse arranjo é chamado de modelo anêmico.
- O autor cita críticas de Paulo Silveira, Martin Fowler e Philip Calçado ao mesmo problema.
- O texto diz que essa prática joga fora benefícios da orientação a objetos como reutilização de código, polimorfismo e herança.
- Entre os motivos apontados para isso estão a dificuldade de usar bem os recursos da OO, exemplos de “boas práticas” que sugeriam arquiteturas parecidas e a falsa sensação de facilidade de manutenção.
- A recomendação final é evitar modelos anêmicos e preferir objetos ricos, com atributos e métodos que manipulem esses atributos.
- O texto também recomenda usar abstrações, polimorfismo, herança e encapsulamento quando houver necessidade de flexibilidade.
