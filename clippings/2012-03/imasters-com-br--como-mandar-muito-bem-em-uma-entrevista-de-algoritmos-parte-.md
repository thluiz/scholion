---
url: "https://imasters.com.br/desenvolvimento/como-mandar-muito-bem-em-uma-entrevista-de-algoritmos-parte-01"
captured_at: "2012-03-08T23:28:15-03:00"
title: "Como mandar muito bem em uma entrevista de algoritmos - Parte 01"
domain: "imasters-com-br"
---

### Sent to you by Thiago Silva via Google Reader:

## 

[Como mandar muito bem em uma entrevista de algoritmos - Parte 01](http://feedproxy.google.com/~r/imasters/~3/Up2i_xTlzjw/story01.htm)

via [iMasters -](http://imasters.com.br/) by Redação iMasters (redacao@imasters.com.br) on 3/6/12

  

Fazemos muitas entrevistas na Palantir, e vou te dizer: é difícil. Não quero dizer que fazemos perguntas difíceis (apesar de fazermos). Quero dizer a tarefa de avaliar o candidato é que é difícil.

O problema? Dado um quadro branco e uma hora, determinar se uma pessoa de frente para você é alguém com quem você gostaria de trabalhar, pelos próximos n anos. O desempenho de um candidato durante uma entrevista é fracamente relacionado ao seu verdadeiro potencial, mas estamos presos ao problema de tornar um rabisco no quadro em um ‘sim ou um ‘melhor’.

Às vezes, parece um jogo de alto risco de leitura de folhas de chá. Acredite em mim, estamos fazendo o melhor, mas muitas vezes ficamos com a sensação de que estamos deixando passar pessoas brilhantes que simplesmente tiveram um dia ruim ou que não tiveram um  'click' com um problema em particular.

Em um esforço para melhorar essa situação, quisemos escrever um guia para ajudar os candidatos a compreender esse processo, ou pelo menos a parte conhecida como Entrevista de Algoritmos. Na Palantir, perguntamos sobre coisas que testam diferentes habilidades - codificação, design, conhecimento de sistemas etc. - mas uma das nossas entrevistas mais importantes é pedir para o candidato criar um algoritmo para resolver um determinado problema.

Geralmente começa assim:

Dado X, encontre uma maneira eficiente de fazer Y.

Primeiro: certifique-se de que tenha entendido o problema. Você não vai perder pontos por pedir  esclarecimentos ou falar sobre o óbvio. Isso também te dará tempo se o seu cérebro não estiver pegando no tranco imediatamente. Ninguém espera que você resolva o problema em 30 segundos ou até nos primeiros minutos.

Uma vez que você tenha entendido o problema, tente bolar uma solução - qualquer solução. Desde que seja válida, não importa se sua solução é trivial, feia ou extremamente ineficiente. O que importa é que você fez algum progresso. Isso faz duas coisas: (1) força você a se engajar com a estrutura do projeto, e (2) dá a você algo do banco, que em retorno te dará confiança. Se você puder encontrar uma solução de força bruta para o problema, você terá superado um importante obstáculo para conseguir resolvê-lo de uma maneira mais eficiente.

Agora vem a parte mais difícil. Foi dada a você uma solução O(n^3) e seu entrevistados pede para você fazer mais rápido. Você olha para o problema, mas nada chega à sua mente. Nesse ponto, existem alguns caminhos que você pode seguir, dependendo do problema em questão e da sua personalidade. Quase todos estes podem te ajudar em qualquer problema:

**1.** **Comece escrevendo no quadro.** Isso pode parecer óbvio, mas eu tive dezenas de candidatos que travaram olhando para uma parede branca. Talvez eles não sejam pessoas visuais, mas eu ainda acho que é mais produtivo olhar para alguns exemplos do problema do que olhar para nada. Se você pode pensar em uma imagem que possa ser relevante, desenhe. Se existe um exemplo de tamanho médio que pode ser relevante, vá em frente (tamanho médio é melhor que pequeno, porque às vezes a solução para um exemplo pequeno não será generalizada). Ou apenas escreva algumas proposições que você acredita serem verdadeiras. Qualquer coisa é melhor que nada.

**2. Converse sobre ele.** E não se preocupe se algo soar estúpido. Se falar em voz alta faz você se sentir melhor, diga ao seu entrevistador: "eu irei apenas falar comigo mesmo, não leve isso em consideração". Sei que muitas pessoas preferem contemplar um problema em silêncio, mas, se você estiver travado, falar é uma maneira de sair dele. Às vezes, você irá dizer algo que claramente se comunica com o seu entrevistador, que você entende o que está acontecendo. Apesar de você não dar muita ênfase naquilo, seu entrevistador pode te interromper e dizer para que você siga naquela linha de raciocínio. Você pode decidir fazer o que quiser, mas, por favor, não vá atrás de dicas. Se você precisa delas, seja honesto e peça por uma.

**3. Pense em algoritmos.** Às vezes, é útil ponderar sobre as particularidades do problema em questão e esperar que uma solução surja do nada para você (esta seria uma abordagem ascendente). Mas você também pode pensar em algoritmos diferentes e perguntar se cada um deles se aplica ao problema diante de você (abordagem descendente). Mudar seu quadro de referência dessa maneira muitas vezes pode levar a um insight imediato. Aqui estão algumas técnicas algoritmicas que podem ajudá-lo a resolver mais da metade dos problemas que pedimos na Palantir:

- Classificação (mais pesquisa/busca binária)
- Divida e conquiste
- Programação dinâmica/memoization
- Greediness
- Recursão
- Algoritmos associados a uma estrutura específica de dados (o que nos leva para nossa quarta sugestão...)

**4. Pense em estruturas de dados.** Você sabia que as 10 principais estruturas de dados valem por 99% de toda a estrutura de dados usada em todo o mundo real? Provavelmente não, porque eu acabei de inventar esses números - mas eles estão na estimativa correta. Sim, ocasionalmente perguntamos sobre um problema cuja solução otimizada requer um Bloom filter ou suffix tree, mas mesmo esses problemas tendem a ter uma solução quase-otimizada que usa uma estrutura de dados muito mais mundana. As estruturas de dados que aparecem mais frequentemente são:

- Array
- Stack/Queue
- Hashset/Hashmap/Hashtable/Dictionary
- Tree/binary tree
- Heap
- Graph

Você deve saber essas estruturas de dados de trás pra frente. Quais são as características de inserção/exclusão/pesquisa? (O(log n) para uma árvore binária equilibrada, por exemplo). Quais são as ressalvas comuns? (Hashing é complicado, e geralmente leva O(k) tempo, quando k é o tamanho do objeto sofrendo o hash). Quais algoritmos tendem a acompanhar cada estrutura de dados? ([Dijkstra](https://secure.wikimedia.org/wikipedia/en/wiki/Dijkstra%27s_algorithm) para um gráfico). Mas quando você compreende essas estruturas de dados, às vezes a solução para um problema irá surgir na sua cabeça assim que você pensar em usar a correta.

**5. Pense em problemas relacionados que você viu antes e como eles foram resolvidos.** As chances são grandes de o problema a que você foi apresentado seja um problema que você já viu antes. Pense sobre essas soluções e como elas podem ser adaptadas para o problema em questão. Não fique preso na forma como o problema está sendo apresentado - destile-o até o fim e veja se corresponde a algo que você já viu no passado.

**6. Modifique o problema ao quebrá-lo em problemas menores.** Tente resolver um caso especial ou uma versão simplificada do problema. Olhar para outros cases é uma boa maneira de driblar a complexidade e o escopo do problema. Uma redução do problema em um subconjunto do problema maior pode te dar uma base para saber de onde começar e então permitir que você trabalhe seu caminho para o escopo completo em questão. Olhando para o problema como uma composição de problemas menores também pode ser útil. Por exemplo, "encontre um número em um array classificado que foi ciclicamente modificado por uma constante k desconhecida" pode ser resolvido por (1) encontrar "k" e então (2) descobrir como executar uma busca binária em um array modificado).

**7. Não tenha medo de voltar atrás.** Se você acha que uma abordagem em particular não está funcionando, pode ser o momento de tentar uma abordagem diferente. Claro que você não deve desistir tão facilmente. Mas se você gastou alguns minutos em uma abordagem que não está gerando nenhum fruto e não parece promissora, volte e tente outra coisa. Eu vi muitos candidatos que comitaram e depois descomitaram, o que significa que você deveria (todo o resto igual) estar mais disposto a abandonar uma abordagem não promissora.

Tentar algumas abordagens diferentes (em vez de ficar preso com uma única abordagem) tende a funcionar bem em entrevistas, porque os problemas que escolhemos para entrevistas geralmente têm muitas soluções diferentes. Felizmente, o mesmo é verdadeiro para problemas que solucionamos no trabalho. =)

*⁂*

*Texto original disponível em <http://blog.palantirtech.com/2011/09/26/how-to-rock-an-algorithms-interview/>*

[anexo ausente]

|  |  |
| --- | --- |
| [9bcafcd24ef5e7a319a7e300c0d5b221.gif](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Como+mandar+muito+bem+em+uma+entrevista+de+algoritmos+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F23715%2Fdesenvolvimento%2Fcomo-mandar-muito-bem-em-uma-entrevista-de-algoritmos-parte-01) | [75b9131ce15803402621ad7d693d4dd1.gif](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Como+mandar+muito+bem+em+uma+entrevista+de+algoritmos+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F23715%2Fdesenvolvimento%2Fcomo-mandar-muito-bem-em-uma-entrevista-de-algoritmos-parte-01) |

  
  
[[anexo ausente]](http://da.feedsportal.com/r/127698505585/u/49/f/546640/c/33212/s/1d30b8f8/kg/312/a2.htm)[anexo ausente][anexo ausente]

  

### Things you can do from here:

- [Subscribe to iMasters -](http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fimasters.uol.com.br%2Ffeed%2F?source=email) using **Google Reader**
- [Get started using Google Reader](http://www.google.com/reader/?source=email) to easily keep up with **all your favorite sites**
