---
url: "http://tableless.com.br/parallax-scrolling/"
captured_at: "2012-12-03T13:11:36-03:00"
title: "Parallax Scrolling"
domain: "tableless-com-br"
---

Parallax Scrolling foi uma das grandes tendências do webdesign em 2012. Mesmo que você não conheça o termo é capaz de já ter visto o efeito por aí… Ele serve para dar a ilusão de profundidade de campo e pode ser utilizado para criar uma experiência de navegação bem diferentes do convencional. Neste artigo vamos entender da onde surgiu este termo, quais cuidados devemos tomar e é claro, como implementar o efeito de parallax scrolling através de javascript.

  

## O que afinal é parallax?

  

Segundo  a Wikipedia:

  
> Parallax é uma entidade cósmica que nutre e se alimenta do próprio medo que espalha nos seres vivos dos planetas que são tocados por sua energia amarela.

  

Opa, Parallax errado! Esta é o vilão da marvel. O termo certo em português é “paralaxe”. Vamos a definição correta da nossa grande amiga [Wikipedia](http://pt.wikipedia.org/wiki/Paralaxe):

  
> Paralaxe é a alteração aparente de um objeto contra um fundo devido ao movimento do observador.

  

Parece confuso? Existe uma experiência simples para ver este efeito no “mundo real”. Você pode testar agora mesmo. Levante seu dedo indicador e estique o braço. Agora feche um olho e preste atenção no fundo atrás do seu dedo. Depois, ainda com o braço parado, feche o olho que estava aberto e abra o outro. A impressão é que dá é que seu dedo “andou” em relação ao fundo, certo?

  

## O que isto tem a ver com desenvolvimento web?

  

Na verdade esta não é uma idéia muito nova. Utilizar camadas de imagens que se movem em velocidades diferentes é uma técnica que já foi muito utilizada no cinema e até em video games. Quem é um pouco mais velho certamente se lembra dos jogos 2D. As camadas de cenário em jogos como Super Mario, por exemplo, criavam a ilusão de profundidade de campo quando o personagem se movia pela tela. A idéia aqui é a mesma. Utilizar elementos gráficos como texto, imagens, background etc sobrepostos em camadas que se movem em diferentes velocidades de acordo com a rolagem do mouse na tela.

  

A febre se espalhou mesmo na internet com o site Nike Better World (A Smashing Magazine inclusive tem um [case](http://coding.smashingmagazine.com/2011/07/12/behind-the-scenes-of-nike-better-world/) bem interessante sobre o projeto). Desde então o parallax foi utilizado em inúmeras situações e se tornou uma ótima ferramenta de storytelling, já que o efeito é ótimo para criar uma continuidade visual como no site [Ben, the bodyguard](http://benthebodyguard.com). Ou até mesmo uma história em quadrinhos interativa de como a [Soul Reaper](http://www.soul-reaper.com).

  

## Alguns cuidados necessários

  

OK. Uma vez tomada a decisão de utilizar o efeito, para aplica-lo na prática é necessário bastante planejamento e uma boa integração entre o designer e o desenvolvedor. É importante sentar junto para pensar quais elementos do layout devem se sobrepor, a qual velocidade, em que momento deverão “aparecer” e “sumir” da tela… Esta etapa é fundamental e se pulada pode levar a uma grande confusão visual digna dos idos tempos do Flash. E o que tinha a intenção de melhorar a experiência acaba atrapalhando… Por isto capriche no wireframe. Pode ser um documento detalhado ou um rabisco no verso de uma folha que só a sua equipe compreende, o importante é ter as informações do projeto pensadas antes de iniciar o desenvolvimento em si ao invés de ficar na tentativa e erro.

  

## Stellar

  

Existem diversos métodos de implementar o efeito parallax, a maior parte se baseia em jQuery. Neste artigo vou me focar no plugin [stellar.js](http://markdalgleish.com/projects/stellar.js/) por sua fácil implementação, flexibilidade de uso  e compatibilidade com dispositivos móveis.

  

A primeira decisão a ser tomada é se a rolagem do site será horizontal ou vertical, já que ambas são permitidas pelo plugin. Para este artigo vamos exemplificar com elementos verticais.

  

#### Os Elementos Parallax

  

A velocidade natural de scroll dos elementos é 1. O que este plugin faz é altera-la através do parâmetro data-stellar-ratio.  Uma observação importante é que a posição dos elementos deve ser declarada no CSS como absolute, relative ou fixed.

  

Este exemplo duplica a velocidade de scroll da div.

  

```
 <div data-stellar-ratio="2">
```

  

Lembre-se de trocar o número “2″ pela velocidade desejada. Você pode até utilizar números negativos para inverter a direção dos elementos.

  

#### Parallax Backgrounds

  

Este parâmetro altera a rolagem do fundo de acordo com a rolagem do mouse.

  

```
 <div></div>
```

  

#### Offsets

  

Determina em qual posição o elemento vai voltar para a sua posição original. Isto pode ser aplicado de duas maneiras:

  

**Configura o Offset de todos os elementos:**

  

```
 $.stellar({  
   horizontalOffset: 40,  
   verticalOffset: 150  
 });
```

  

**Apenas de um elemento:**

  

```
 <div data-stellar-ratio="2"  
      data-stellar-horizontal-offset="40"  
      data-stellar-vertical-offset="150">
```

  

**Offset Parents**

  

Por padrão o offset (momento em que o objeto “some” da tela) é sempre relativo ao elemento container. O elemento pai é sempre o item mais próximo com uma posição fixed ou absolute (como no CSS). Mas é possível “forçar” outro elemento a ser o parent

  

```
 <div></div>
```

  

O parent também pode ter seus próprios Offset

  

```
 <div data-stellar-offset-parent="true"  
      data-stellar-horizontal-offset="40"  
      data-stellar-vertical-offset="150">
```

  

#### Scroll Positioning

  

Você consegue determinar o que exatamente significa “scroll”. Se é mudar de posição, CSS transform, etc É isto que permite o stellar funcionar no iOS. Exemplo utilizando CSS transforms:

  

```
 $('#gallery').stellar({  
   positionProperty: 'transform'  
 });
```

  

Para mais informações, não se esqueça de conferir a [documentação](http://markdalgleish.com/projects/stellar.js/docs/) do plugin e/ou o repositório no [Github](https://github.com/markdalgleish/stellar.js).

  

## Uma dica importante

  

Aqui cabe um alerta. O paralax scrolling é mesmo um efeito bacana e é legal conhecer a técnica, mas é importante saber **quando** é o melhor momento para se utilizar. Antes de adicionar, não apenas este efeito especificamente como qualquer outro elemento visual, não se esqueça da pergunta “Por que eu quero fazer isto?”…. Principalmente no caso de efeitos e animações que podem influir negativamente na experiência do usuário trazendo poluição visual, aumento no tempo de carregamento de uma pagina, etc. E se a resposta for apenas “porque é bonitinho” é melhor pensar duas vezes antes de utilizar parallax scrolling. Como qualquer aspecto do design, é importante que o parallax seja utilizado não apenas como um efeito visual, mas como parte integrante do storytelling.

  

### Posts Relacionados

  

[Criando um plugin JavaScript (sem jQuery!)](http://tableless.com.br/criando-um-plugin-javascript-sem-jquery/)

  

[Adobe Edge](http://tableless.com.br/adobe-edge/)

  

[Underscore.js: cinto de utilidades JavaScript](http://tableless.com.br/underscore-js-cinto-de-utilidades-javascript/)

  

[Criando uma aplicação simples com AngularJS](http://tableless.com.br/criando-uma-aplicacao-simples-com-angularjs/)

  

[Retina.js – Imagens para telas retina](http://tableless.com.br/retina-js-imagens-para-telas-retina/)

  
   
 from Tableless <http://tableless.com.br/parallax-scrolling/>
