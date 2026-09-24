---
title: "What I learned while implementing a colorblind mode for my Belgian Wage Calculator site"
date: '2026-09-25T00:09:49+01:00'
category: webclip
summary: 'O autor relata o que aprendeu ao criar um modo para daltonismo no Belgian Wage Calculator, incluindo como as cores mudam com diferentes deficiências e por que duas versões funcionam melhor que uma só.'
tags: ["colorblindness", "web-accessibility", "css"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What I learned while implementing a colorblind mode for my Belgian Wage Calculator site"
    url: "https://dev.to/illarious/what-i-learned-while-implementing-a-colorblind-mode-for-my-belgian-wage-calculator-site-51f0?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--what-i-learned-while-implementing-a-colorblind-mode.md"
    kind: repo
---

The article is a retrospective on building a colorblind mode for the Belgian Wage Calculator. It explains the differences between red, green, and blue colorblindness, describes what the author learned from simulation tools and feedback, and shows why separate modes for red and green deficiencies worked better than a single combined palette.

## Fichamento

- O autor apresenta o trabalho como um retrospecto sobre a criação de um modo para daltonismo no Belgian Wage Calculator.
- Ele descreve a colorblindness como um espectro e distingue formas completas e parciais para vermelho, verde e azul.
- A expectativa inicial era escolher cores opostas para um receptor e confiar que elas fossem distinguíveis mesmo em deficiência total.
- Ao simular essas condições no Firefox, ele percebeu que a perda total de vermelho ou verde reduz bastante a paleta disponível.
- O autor concluiu que o efeito para vermelho e verde fica mais parecido do que ele imaginava, com diferenças menores do que no caso do azul.
- Ele também observou que a extensão usada para simulação parecia menos fiel no caso da deficiência azul em partes mais escuras do espectro.
- Outra lição foi que as cores mudam conforme a severidade da deficiência, então a escolha intuitiva de tons vizinhos pode falhar.
- Para obter um azul claro equivalente em caso de daltonismo verde, o caminho que ele considerou intuitivo para o ciano se mostrou errado; a solução passou pela faixa de roxo e rosa.
- Ele recebeu a sugestão de dar mais peso a gradações de claro e escuro nos fundos em vez de depender só de cor.
- Depois disso, o autor considerou mais manejável encontrar uma paleta melhor para o site.
- No estado original, o site usava vermelho para valores negativos e verde para positivos, com contraste que parecia claro para quem enxerga normalmente.
- Na simulação de daltonismo verde severo, negativo e positivo ficaram difíceis de distinguir, sobretudo em combinação com certos fundos.
- O autor passou a testar versões específicas para daltonismo verde e para daltonismo vermelho.
- Ele notou que, em sua simulação de daltonismo verde, o resultado ficava bastante roxo e que isso parecia estranho à primeira vista.
- Com 100% de daltonismo verde, porém, essa versão passa a fazer sentido dentro do deslocamento da faixa de cores.
- Na simulação de 50% de daltonismo verde, a versão ainda era legível e mais próxima de tons rosa e roxo.
- Depois de testar uma versão única para verde e vermelho, ele decidiu separar o modo em duas opções que o usuário pode alternar.
- Ele não criou um modo específico para daltonismo azul, porque o layout normal ainda parecia distinguível.
- O autor comenta que o modo vermelho também é útil para algumas pessoas com certos graus de daltonismo verde.
- A esperança dele é que pelo menos um dos modos funcione bem para cada pessoa, inclusive para quem tem deficiência total de cor.
- Para esses casos, ele diz ter usado princípios básicos de design, como sinais claros de mais e menos para valores positivos e negativos.
- O texto termina com um agradecimento ao subreddit r/Colorblind pelo retorno dado e com a indicação de que a página ainda está em ajuste, principalmente nos fundos e no contraste.
