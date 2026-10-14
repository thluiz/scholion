---
title: "Algoritmos genéticos: resolvendo a equação quadrática"
date: '2013-02-26T09:57:58-03:00'
category: webclip
summary: 'O artigo mostra um exemplo de algoritmo genético que usa números reais para aproximar as raízes de y = 13x^2 - 5x - 12 e descreve codificação, fitness, crossover, parada e teste da implementação.'
tags: ["algoritmos-geneticos", "equacao-quadratica", "funcao-fitness", "crossover"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Algoritmos genéticos: resolvendo a equação quadrática"
    url: "http://imasters.com.br/desenvolvimento/algoritmos-geneticos-resolvendo-a-equacao-quadratica/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/imasters-com-br--algoritmos-geneticos-resolvendo-a-equacao-quadratica.md"
    kind: repo
---

O artigo apresenta uma implementação simples de algoritmo genético aplicada à equação quadrática y = 13x^2 - 5x - 12. Em vez de cadeias de bits, usa números reais, calcula o fitness pela proximidade das soluções e diz que a aproximação das raízes ocorre em pouco menos de 23 segundos.

## Fichamento

- O autor diz que encontrou muita explicação teórica sobre algoritmos genéticos, mas poucos exemplos reais, e por isso resolveu implementar um caso vivo.
- O exemplo escolhido foi a solução de uma equação quadrática, por ser simples de implementar, embora sem aplicação prática neste caso.
- O cromossomo guarda dois genes e um valor de aptidão.
- A população inicial é criada com valores aleatórios para os genes.
- O fitness soma os valores absolutos gerados pela equação para os valores do cromossomo; quanto menor o resultado, mais perto da solução.
- Durante as iterações, o algoritmo guarda os índices das melhores soluções para produzir a próxima geração.
- O crossover combina os melhores fenótipos para gerar descendentes e pode substituir a geração antiga pela nova.
- O código apresentado junta crossover e mutação na mesma função, embora o autor diga que normalmente eles podem ser separados.
- A taxa de mutação define a velocidade de evolução das soluções, com troca entre rapidez e exatidão.
- A execução deve parar quando a precisão desejada for alcançada ou quando ficar claro que a equação não tem raízes.
- O texto diz que precisão e velocidade dependem da taxa de mutação e do tamanho da população.
- A implementação aproxima as raízes em pouco menos de 23 segundos e gera soluções precisas para a maioria das necessidades.
- O autor conclui que algoritmos genéticos podem ser usados em seleção de topologia de rede neural e em outras otimizações.
