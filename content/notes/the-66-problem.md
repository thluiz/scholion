---
title: "The 66% Problem"
date: '2026-09-25T00:01:40+01:00'
category: webclip
summary: 'O texto argumenta que assistentes de IA escrevem código “quase certo”, mas difícil de depurar, criando bugs novos e uma sensação enganosa de produtividade.'
tags: ["ai-coding", "debugging", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The 66% Problem"
    url: "https://dev.to/evanlausier/the-66-problem-1c3m?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--the-66-problem.md"
    kind: repo
---

O texto diz que assistentes de IA geram um tipo novo de problema: código que parece correto, passa testes e ainda assim introduz erros sutis. O autor trata isso como um risco maior do que falhas óbvias, porque o custo aparece depois, quando é preciso depurar o que a IA assumiu sem pedir confirmação.

## Fichamento

- O autor conta que perdeu três horas atrás de um bug que, no fim, nem existia; o problema real era uma função adicionada pela Claude para paginação, embora isso não tivesse sido pedido.
- Ele usa isso para definir o “66% problem”, ligado à frustração de código “quase certo” e ao trabalho extra de depurar código gerado por IA.
- Código totalmente errado falha de forma clara, enquanto código quase certo pode passar testes, ir para staging e causar falhas sutis depois.
- Para o autor, os bugs gerados por IA são mais difíceis porque, ao encontrar um problema, ele precisa descobrir o que a IA fez sem perceber.
- O texto cita um estudo da Microsoft Research com nove modelos e a banca SWE-bench Lite; o melhor modelo resolveu 48,4% das tarefas, menos da metade.
- O autor distingue gerar código de depurar código: gerar é completar padrões, mas depurar exige hipótese, entendimento do que o sistema deveria fazer e do motivo da diferença.
- A IA não conhece regras de negócio antigas nem particularidades de arquitetura que moldam o sistema, então tende a apenas reconhecer padrões.
- O texto cita um ensaio aleatorizado da METR, de julho de 2025, em que desenvolvedores experientes ficaram 19% mais lentos com IA, embora achassem que estavam 24% mais rápidos.
- O autor diz que o ganho percebido de produtividade pode esconder dívida de depuração acumulada.
- Ele não defende abandonar essas ferramentas, mas passar a ler cada sugestão com mais cautela, como se viesse de um júnior confiante.
- A conclusão é que as ferramentas são boas o bastante para serem perigosas, e que seguir usando IA exige manter testes e hábitos de depuração fortes.
