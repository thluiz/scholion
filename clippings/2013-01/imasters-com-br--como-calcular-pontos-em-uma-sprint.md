---
url: "http://imasters.com.br/desenvolvimento/gerencia-de-projetos/como-calcular-pontos-em-uma-sprint/"
captured_at: "2013-01-25T12:15:14-03:00"
title: "Como calcular pontos em uma Sprint?"
domain: "imasters-com-br"
---

Olá, pessoal! O artigo de hoje, da série Agile, trata de um assunto que não é fácil para o scrum master, para a equipe e o product owner: definir a quantidade máxima de um ponto que um Sprint pode suportar, ou seja, quantas estórias do backlog podem fazer parte do sprint backlog? É isso que veremos neste artigo.

  

Claro que o que abordaremos aqui não é a única forma, ou a mais adequada para ser implementada em qualquer projeto, porém é bem utilizada por scrum master mais experientes, como o Crisp.  Eu particularmente gosto de ter os cases do Crisp como referência.

  

Definir prazo, de acordo com a quantidade de trabalho dentro de um número X de dias, não é uma tarefa fácil. Claro que quanto mais experiência vamos adquirindo, as chances de erros tendem a diminuir. Mas não quer dizer que não podemos errar em estimativas e sabemos que esse tipo de erro gera grandes impactos, até porque o cliente está diretamente envolvido – já que prometemos entregar em uma Sprint cinco novas features, mas conseguimos apenas concluir três. Então, como podemos evitar isso? Vamos ver como Kniberg nos ajuda a entregar tudo aquilo que prometemos e manter uma boa saúde da equipe.

  

Lá vem a pergunta: como uma equipe define as estórias que vão para um Sprint?

  

1. Pode ser por sentimento ou instinto: essa aqui é bem comum e pode ser a primeira opção a ser adotada. É errado? Não. Tudo depende da equipe e da auto-confiança da mesma nas estórias definidas no backlog do product owner.

     

   Estimativas de cálculo de velocidade: essa aqui é um pouco mais matemática e não envolve sentimento ou instinto. E o objetivo final da “velocidade” ajuda a saber a quantidade de trabalho que pode ser adicionado ao sprint.  Porém temos duas formas de  fazer o cálculo:

Forma 1 – Tempo de Ontem: é assim que é chamada, onde olhamos para o Sprint anterior e somamos os pontos do que foi entregue e podemos ter uma margem para próxima Spring.

  

Forma 2 – Fator foco: é onde uma estimativa de como a equipe é focada para achar o fator foco, então o calculo para encontrar esse “fator foco” seria:

```
 fator foco(%) = soma das estimativas homem-dia
```

  

Agora, calculando os pontos por estória para o Sprint, é só pegar o percentual do fator foco anterior e multiplicar pela quantidade homem-dia do Sprint seguinte, assim chegamos ao total de pontos que o Sprint a seguir deve atingir para garantir a entrega. Se o resultado for 20 pontos por exemplo, então esse será o valor máximo que o Sprint backlog pode ter. Cálculo:

  

```
 Pontos = fator foco(%) * homem-dia
```

  

## O que é homem-dia?

  

Se nunca viu este termo, homem-dia é quantas pessoas teremos disponíveis para aquela Sprint e o cálculo não é por “cabeça” e sim por disponibilidade. O fato de ter três pessoas não quer dizer que temos elas 100%. Podemos ter o seguinte cenário:

  

Camilo: 20 dias

  

João: 20 dias

  

Maria: 10 dias

Logo, temos 50 homens-dia disponíveis.

  

Vamos considerar que seja um Sprint de vinte dias, então, no cenário acima, apenas dois dos três tem disponibilidade 100% para toda a Sprint, e isso tem um grande impacto na quantidade de estórias para o backlog.

  

## Simulação

  

Supondo que tivemos 40% de fator foco no Sprint anterior, quantos pontos máximos devemos ter na próxima Sprint, com base no homem-dia anterior?

  

Pontos = 40 %\* 50 = 20

  

Então sabemos que  não podemos ultrapassar o valor de vinte, do contrário já estaremos comprometendo a entrega de estórias do Sprint.  Vamos supor as seguintes estórias  no backlog:

  

fazer página login (7)

  

autenticação DB (6)

  

Test de Perfomance (5)

  

Popular DB (3)

As estórias acima atingem 21 pontos. O que fazer? Colocar apenas por causa de 1 ponto? É possível pensar assim, mas a melhor escolha poderia ser escolher o menor número, ou seja, até 18 pontos  (no caso acima) e evitar ultrapassar  o limite de pontos para o Sprint. Em alguns casos, pode-se colocar o item que sobrou, como se tivesse um tempo de folga e for possível ser implementado, mas o product owner não pode contar com aquela estória ao final da Sprint.

  

## E quando não temos nenhuma Sprint para fazer os cálculos?

  

Isso acontece quando vamos para primeira Sprint. Então, que fator foco adotar? Aí é questão de análise do scrum master conhecer sua equipe e ter uma ideia do escopo. Você vai encontrar livros Scrum que falam 70%, 50%, 80%, enfim, fica a seu critério. Eu adotaria 70%, por não ser algo muito alto, nem tão baixo.

  

Vou ficando por aqui com mais um artigo Agile e espero que tenham gostado. Não deixe de compartilhar sua experiência.

  
![](http://imasters.com.br.feedsportal.com/c/33212/f/546640/s/27e4fcce/mf.gif)  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--como-calcular-pontos-em-uma-sprint/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Como+calcular+pontos+em+uma+Sprint%3F&amp;link=http%3A%2F%2Fimasters.com.br%2Fdesenvolvimento%2Fgerencia-de-projetos%2Fcomo-calcular-pontos-em-uma-sprint%2F)

  

[![](http://rss.feedsportal.com/images/bookmark.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Como+calcular+pontos+em+uma+Sprint%3F&amp;link=http%3A%2F%2Fimasters.com.br%2Fdesenvolvimento%2Fgerencia-de-projetos%2Fcomo-calcular-pontos-em-uma-sprint%2F)

  
  
  
[![](http://da.feedsportal.com/r/151885078879/u/49/f/546640/c/33212/s/27e4fcce/a2.img)](http://da.feedsportal.com/r/151885078879/u/49/f/546640/c/33212/s/27e4fcce/a2.htm) ![](http://pi.feedsportal.com/r/151885078879/u/49/f/546640/c/33212/s/27e4fcce/a2t.img)  
  
![](http://feeds.feedburner.com/~r/imasters/~4/3w4KCLTV48Y)  
  
  
  
from iMasters <http://imasters.com.br/desenvolvimento/gerencia-de-projetos/como-calcular-pontos-em-uma-sprint/>
