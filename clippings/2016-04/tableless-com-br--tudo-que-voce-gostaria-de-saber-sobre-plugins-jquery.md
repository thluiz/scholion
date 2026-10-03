---
url: "http://tableless.com.br/tudo-que-voce-gostaria-de-saber-sobre-plugins-jquery-e-ninguem-teve-paciencia-de-explicar/"
captured_at: "2016-04-11T10:58:02-03:00"
title: "Tudo que você gostaria de saber sobre plugins jQuery e ninguém teve paciência de explicar - Tableless"
domain: "tableless-com-br"
---

# Tudo que você gostaria de saber sobre plugins jQuery e ninguém teve paciência de explicar

[52 comentários](http://tableless.com.br/tudo-que-voce-gostaria-de-saber-sobre-plugins-jquery-e-ninguem-teve-paciencia-de-explicar/#disqus_thread)
![f159cc42cdb1ea7b0f757474cace8c15.jpg](tableless-com-br--tudo-que-voce-gostaria-de-saber-sobre-plugins-jquery/86f88fa6723a392a8ab04113c398ae82.jpg) por [Zeno Rocha](http://tableless.com.br/author/zeno/ "Posts de Zeno Rocha")

Então quer dizer que você anda brincando com jQuery. Volta e meia utiliza uns plugins que mais parecem mágica e se duvidar até se aventurou em criar o seu próprio, acertei?

Acontece que, caso você já saiba desenvolver os seus, talvez possam existir melhores formas de escrevê-lo. Será que você está seguindo as melhores práticas? Será que realmente entende o que está acontecendo por trás de cada linha?

Hoje vou tentar responder as dúvidas mais frequentes, explorando as melhores práticas para se construir um plugin. E no fim lhe mostrar um padrão interessante que você pode seguir agora que já entendeu os conceitos.

A ideia aqui não é simplesmente mostrar como criar um plugin, mas sim como criar direito, explorando tudo o que o jQuery tem de melhor para nos oferecer.

## Por que eu deveria construir um plugin?

Encapsulamento e reaproveitamento de código, essas são as palavras-chave. Se você está codificando algo que talvez sirva para futuros projetos, pode ser uma boa encapsular tudo isso em um plugin.

## Entendi, quero criar um! Como faz?

Existem diversas formas, mas vamos começar com essa:

```
1. meuPlugin function
2. // aqui vem a lógica
```

Esse é o mínimo que você precisa para iniciar o desenvolvimento de um plugin, basta adicionar uma propriedade ao **$.fn**.

Por mais trivial que isso possa parecer, muita gente não entende o que está acontecendo por trás disso exatamente. Portanto, antes de evoluirmos esse padrão, vamos recorrer ao [código fonte da biblioteca](http://code.jquery.com/jquery-1.7.1.js), na sua versão mais recente, para entender de verdade esse pequeno trecho de código.

## O que significa o cifrão ($) ?

O famoso **$** nada mais é do que um “apelido” para o objeto **jQuery**. Próximo ao fim do [código fonte da biblioteca](http://code.jquery.com/jquery-1.7.1.js) encontramos a seguinte definição:

```
1. windowjQuery  window jQuery
```

Isso significa que o mesmo objeto em memória pode ser referenciado de diversas formas: **window.jQuery**, **window.$**, **jQuery** ou simplesmente **$**.

## Qual a diferença entre $.meuPlugin e $.fn.meuPlugin?

Possivelmente você já se deparou com plugins que não utilizavam a propriedade **.fn**. Mas afinal, por que eu deveria utilizar o **.fn**? Por que não apenas **$.meuPlugin** ao invés de **$.fn.meuPlugin**?

Novamente, ao nos aventurarmos no [código fonte](http://code.jquery.com/jquery-1.7.1.js) percebemos, logo nas primeiras linhas, como o objeto **jQuery** é definido.

```
1. jQuery function selector context
2. return jQuery selector context rootjQuery
```

Note que **jQuery** é uma função e no Javascript uma função é também um objeto do tipo **Function**. Por isso **jQuery.meuPlugin** (ou **$.meuPlugin**) irá atribuir **meuPlugin** para o objeto jQuery do tipo **Function**.

Dito isso, voltamos ao [código fonte](http://code.jquery.com/jquery-latest.js) e veremos que **jQuery.fn** é a mesma coisa que dizer **jQuery.prototype**.

```
1. jQuery jQueryprototype
```

Portanto, a cada vez que você atribuir uma função (ou propriedade) para **jQuery.fn**, como em **$.fn.meuPlugin**, a função estará disponível para todas as instâncias desse objeto.

Isso é importante, pois quando você invoca a função **$()**, como em **$(“#algumID”)**, uma nova instância é criada nessa linha:

```
1. return jQuery selector context
```

E essa instância terá todos os métodos que atribuirmos ao **prototype**, mas não todos os métodos que foram atribuídos direto ao objeto **Function**.

Logo, vá de **.fn**.

## Evite conflitos

Sabia que existem outras bibliotecas Javascript que também utilizam o símbolo cifrão para referenciar seus objetos? Pois é, isso pode lhe causar uma baita dor de cabeça se utilizar apenas aquele primeiro padrão proposto.

Logo, uma boa prática seria encapsular a lógica do plugin em uma função anônima. Assim, garantimos que não irá haver conflito entre o **$** do jQuery com o **$** de outras bibliotecas.

```
1. function
2. meuPlugin function
3. // aqui vem a lógica
4. jQuery
```

Dessa forma mapeamos o **$** para que não seja afetado por nada fora desse escopo.

## Não quebre a corrente

Então, você já entendeu como funcionam algumas coisas, vamos criar nosso primeiro plugin! Começaremos com o clássico exemplo de um Tooltip (aquelas caixinhas que aparecem no mouseover).

Criamos então a chamada para o plugin a partir de determinado seletor:

```
1. function
2. ".BlaBlaBla"tooltip
```

E código do nosso plugin ficará definido assim:

```
1. function
2. tooltip function
3. background'yellow'
4. jQuery
```

Aparentemente tudo certo, já que o plugin funciona direitinho, certo?

Na verdade não, pois dessa forma estamos ferindo um dos princípios importantes que diferem os plugins bons dos ruins, e esse princípio se chama encadeamento.

No jQuery é muito comum vermos declarações do tipo:

```
1. 'div'addClass'BlaBlaBla'fadeIn
```

Isso, porque é possível encadear diversas chamadas, a um mesmo seletor. E uma excelente prática por sinal, já que não criamos diversas instâncias como em:

```
1. 'div'
2. 'div'addClass'BlaBlaBla'
3. 'div'fadeIn
```

Para permitirmos comportamento similar com nosso plugin basta retornar o **this**.

```
1. function
2. tooltip function
3. returnfunction
4. background'yellow'
5. jQuery
```

Assim, além de garantirmos o encadeamento, também manipulamos a coleção passada para o plugin através do método **each**, muito similar a um loop com **for** por exemplo.

## Como passar parâmetros e lidar com eles depois?

E que tal se evoluíssemos nosso plugin e resolvessemos passar como parâmetro a cor de fundo do nosso elemento.

```
1. function
2. ".BlaBlaBla"tooltip
3. 'corDeFundo''blue'
```

Agora preparamos nosso plugin para receber os parâmetros através da variável **options** e aplicamos a propriedade **corDeFundo** no **background**.

```
1. function
2. tooltip functionoptions
3. returnfunction
4. background optionscorDeFundo
5. jQuery
```

Maravilha, funcionou! Mas o que acontece se você resolve mais tarde não passar como parâmetro a cor de fundo? Nosso plugin quebra.

Portanto, não podemos nos esquecer de que precisamos nos preparar para receber esse conjunto de opções e assegurar que, caso não seja passado nenhum valor como parâmetro, nós possamos lidar com valores padrão.

```
1. function
2. tooltip functionoptions
3. defaults
4. 'corDeFundo''yellow'
5. settings extend defaults options
6. returnfunction
7. background settingscorDeFundo
8. jQuery
```

Para isso recorremos a função [$.extend](http://api.jquery.com/jQuery.extend/) que irá buscar os valores passados pela variável **options** e mesclar com os valores definidos na variável **defaults**, armazenando em outra variável chamada **settings**.

## A procura da batida perfeita

Esse é só o começo para você que deseja se aprofundar um pouquinho mais nessa arte de criar plugins, para entender mais visite o [guia oficial](http://docs.jquery.com/Plugins/Authoring).

Mesmo que a ideia de se formar um padrão único para criar plugins seja utópico, sugiro fortemente que dê uma olhadinha no [jQuery Boilerplate](http://jqueryboilerplate.com/), lá você vai encontrar um padrão bem sólido para iniciar seus projetos, sem contar que a versão traduzida para português foi lançada hoje!

Mas se o buraco for mais em baixo e você for lidar com plugins [stateful](http://en.wikipedia.org/wiki/State_(computer_science) que controlam o estado dos objetos, confira o [jQuery UI Widget Factory](http://wiki.jqueryui.com/w/page/12138135/Widget%20factory).

Lembre-se que o jQuery não é apenas uma caixa preta que faz mágicas pra você. Aventure-se no código fonte e verá que não é nada muito diferente do que você já faz com JavaScript puro.

E é isso, espero que depois desse artigo, você tenha evoluido de um simples “manipulador de plugins” para um criador de fato. Até a próxima!

Publicado no dia  2 de novembro de 2012
