---
url: "http://imasters.com.br/linguagens/javascript/preparando-se-para-o-desenvolvimento-javascript-moderno/"
captured_at: "2013-01-29T08:53:52-03:00"
title: "Preparando-se para o desenvolvimento JavaScript moderno | iMasters"
domain: "imasters-com-br"
---

# **P**reparando-se para o desenvolvimento JavaScript moderno

sexta-feira, 25/01/2013 às 03h01, por [Redação iMasters](http://imasters.com.br/perfil/redacao_imasters/)

Há muita coisa acontecendo no mundo do JavaScript hoje em dia, dentro e fora do navegador**.** Falar sobre carregadores de script, frameworks MVC do lado do cliente, minifiers, AMD, Common**.**js, CoffeeScript, pode fazer a sua cabeça girar. E, para aquelas pessoas que estão completamente imersas nesse mundo, pode ser fácil esquecer que a grande maioria dos desenvolvedores JavaScript de hoje não ouviu falar de nenhuma dessas ferramentas e, na verdade, provavelmente ainda nem está equipados para testá-las**.**

Este artigo será apenas uma tentativa de resolver algumas das metas mais básicas, e tenta reunir alguns conceitos diferentes que um desenvolvedor deve entender antes de sair por aí e tentar cuidar de algo como Backbone**.**js ou Ember.js. Depois de entender a maioria dos conceitos deste artigo, então você vai poder abordar os tópicos mais avançados do JavaScript com um pouco de confiança**.** Este artigo pressupõe que você já tenha desenvolvido com JavaScript antes, por isso, se você não tiver, é melhor você começar com algo um pouco mais básico**.** Com isso fora do caminho, aqui vamos nós**!**

## Módulos

Como muitos de vocês estão trabalhando com um aplicativo que tem JavaScript semelhante a esse apenas junto de um arquivo (repare que eu não disse embutido em seus arquivos html, não existe nenhuma boa desculpa para isso):

`var` `someSharedValue = 10;`

`var` `myFunction =` `function``(){` `//do something }`

`var` `anotherImportantFunction =` `function``() {` `//do more stuff }`

Se você chegou a este ponto do artigo, então provavelmente está lidando com (ou criando) um código que tem essa aparência**.** Não estou te julgando, eu escrevi códigos iguais a esse por muito tempo**.** Os problemas aqui são muitos, mas vamos focar na poluição do namespace global**.** Ao escrever um código como esse você está apenas enfiando todos esses métodos e variáveis ​​no namespace global**.** Precisamos de uma maneira de manter esse tipo de dado fora do espaço global e a técnica que vamos usar aqui é o módulo padrão**.** Existem formas diferentes que os módulos podem assumir, mas vou começar com o método mais fácil, que você já pode começar a usar hoje, um IIFE (Immediately Invoked Function Expression)**.**

É um grande nome, mas a implementação é muito simples:

`(``function``(){`

`//do some work`

`})();`

Isso pode parecer pouco estranho no início, caso você não tenha usado um IIFE antes**.** Tem um monte de parênteses por aqui**!** Basicamente, temos uma função anônima com um conjunto de parênteses depois dela, que fazem com que a função seja imediatamente invocada**.** Por isso, estamos criando a função e imediatamente chamando-a**.** Daí a parte do nome “função invocada imediatamente”**.** A parte da “expressão” do IIFE  vem do fato de que nós precisamos transformar isso em uma expressão e não em uma afirmação, já que uma afirmação de função deve ter um nome**.** Fazemos isso adicionando o conjunto extra de parênteses ao redor do exterior**.** Isso também nos fornece uma maneira fácil de detectar IIFE quando olhamos através do nosso código**.**

Agora que já sabemos como implementá-lo, vamos falar sobre o motivo de fazermos isso**.** Em JavaScript, tudo o que temos para trabalhar com scoping são funções e, por isso, se quisermos criar scope, utilizamos uma função**.** Ao executar o código dentro do IIFE, estamos fazendo um scope em todas as variáveis ​​e funções dentro do IIFE e por isso não estamos poluindo o namespace global**.** O único problema é que todas as variáveis ​​que criamos agora estão dentro do scope da função, portanto, se quisermos acessá-las de fora do scope global, é preciso levá-las para o namespace global, ou pelo menos em algo que está no namespace global**.**

Uma coisa que podemos fazer é usar o objeto window e atribuir a ele quaisquer funções ou valores, o que nos permite chamar esses métodos externamente**.** Para garantir que nada bagunce a variável window, podemos passar o objeto window como um parâmetro para IIFE**.** Podemos fazer a mesma coisa com referências a bibliotecas ou mesmo com o valor ‘undefined’**.** Nosso IIFE acaba por ficar parecido com isto:

`(``function``(window, $, undefined){`

`//do some work`

`})(window, jQuery);`

Como você pode notar, estamos passando nas variáveis window e ​​jQuery (a variável jQuery $ é apenas um alias para a variável ‘jQuery’, e a utilizamos aqui no caso de outra biblioteca ter redefinido a variável $), mas então temos três parâmetros indo para o método**.** A ideia é que, uma vez que não estamos passando um terceiro parâmetro, ele acaba sendo indefinido, então temos uma variável chamada ‘undefined’ local ao método que está garantida para realmente ter  o valor ‘undefined’, no caso de outra parte do JavaScript a ter modificado**.** Observe que poderíamos chamar qualquer um desses valores dentro da função, sem passá-los; isso funciona porque as funções em JavaScript closures formam closures nas quais eles fecham o scope externo onde eles residem**.** Este tópico dá um artigo inteiro e [escrevi um que explica closures em termos de C#](http://www.codethinked.com/c-closures-explained) , mas os conceitos são muito semelhantes**.**

Agora temos um método que é executado imediatamente, possui um contexto de execução muito mais seguro contendo um window válido, $, e variáveis ​​indefinidas (ainda é possível que algo possa ter transferido uma dessas variáveis antes de chegarmos ao script, porém é muito menos provável)**.** Estamos em um ótimo lugar, depois de ter evitado que nosso código se tornasse um monte de lixo nos namespaces globais e ter reduzido o potencial de colisões com outro JavaScript executando nosso aplicativo**.**

Neste ponto, qualquer coisa que quisermos exportar a partir do módulo, estaremos apenas atribuindo direção ao objeto window**.** Mas muitas vezes não quero apenas atribuir tudo ao meu módulo diretamente para o objeto window, quero ter alguma forma de funcionalidade de agrupamento**.** Na maioria das linguagens, nós chamamos isso de namespaces containers, e podemos emulá-los em JavaScript usando objetos**.**

## Namespaces

Se quisermos declarar um namespace e atribuir uma função a ele, poderíamos fazer assim:

`window.myApp = window.myApp || {};`

`window.myApp.someFunction =` `function``(){`

`//so some work`

`};`

Estamos apenas criando um objeto no namespace global, verificando se ele já existe, e se podemos usá-lo; caso contrário, criamos um novo objeto usando object literal notation: {}**.** Nesse ponto, nós só poderíamos começar a construir o namespace atribuindo funções como estamos fazendo acima, mas não queremos que o nosso código apenas pendurado por aí, queremos combinar nossos namespaces com os nossos módulos assim:

`(``function``(myApp, $, undefined){`

`//do some work`

`}(window.myApp = window.myApp || {}, jQuery));`

Isso também poderia ser escrito desta maneira:

`window.myApp = (``function``(myApp, $, undefined){`

`//do some work`

`return` `myApp;`

`})(window.myApp || {}, jQuery);`

Agora, em vez de passar window para nosso módulo, estamos passando um objeto namespace que está pendurado fora do objeto window**.** A razão pela qual o atribuímos ele usando || é que, se utilizarmos esse namespace em vários lugares, acabamos usando o mesmo objeto uma vez atrás da outra, ao invés de criarmos um novo de cada vez, o que limparia o nosso namespace**.** Muitas bibliotecas incluem funções namespace que criarão namespaces para você, ou você pode usar algo como [namespace**.**js](https://github.com/maximebf/Namespace.js) , que permite que você crie facilmente namespaces aninhados**.** Geralmente, tento não criar namespaces profundamente aninhados, já que em JavaScript você precisa especificar o namespace em cada item que está nele**.** Então, se você criou um método “doSomething” no namespace MyApp.MyModule.MySubModule, você teria que fazer referência a ele assim:

`MyApp.MyModule.MySubModule.doSomething();`

toda vez que você o chamasse, ou você teria que criar um alias para o namespace dentro de seu módulo fazendo:

`var` `MySubModule = MyApp.MyModule.MySubModule;`

Dessa forma, você só precisa dizer “MySubModule.doSomething()”**.** Ele só torna as coisas mais complicadas e, a não ser que você tenha uma tonelada de código, isso pode ser desnecessário**.**

## R**evealing module pattern**

Há um outro padrão que você verá ser usado com frequência para criar módulos, e ele é chamado de revealing module pattern**.** Ele é apenas uma abordagem diferente para a criação de um módulo, permitindo que você defina tudo privativamente dentro do módulo; em seguida, ele expõe o que você deseja expor, retornando um objeto que tem referências a tudo o que você deseja expor publicamente**.** Vamos dar uma olhada em como você definiria isso:

`var` `myModule = (``function``($, undefined){`

`var` `myVar1 =` `''``,`

`myVar2 =` `''``;`

`var` `someFunction =` `function``(){`

`return` `myVar1 +` `" "` `+ myVar2;`

`};`

`return` `{`

`getMyVar1:` `function``() {` `return` `myVar1; },` `//myVar1 public getter`

`setMyVar1:` `function``(val) { myVar1 = val; },` `//myVar1 public setter`

`someFunction: someFunction` `//some function made public`

`}`

`})(jQuery);`

Como você pode ver, estamos criando um módulo em um passo, o que torna tudo mais simples, e estamos retornando um objeto que expõe os pedaços do nosso módulo que queremos tornar público, enquanto nos permite manter nossas variáveis ​​privadas escondidas**.** A variável “MyModule” conterá os dois itens expostos publicamente, mas, como você pode ver, “someFunction” usa “MyVar2″, mas ele não está acessível externamente**.**

## Criando construtores (classes)

Não possuímos classes em JavaScript, mas podemos criar objetos, e fazemos isso por meio da criação de uma função construtor**.** Vamos dizer que queríamos criar um monte de objetos Person, e queríamos passar um nome, um sobrenome e a idade**.** Podemos definir nosso construtor assim (nós provavelmente colocaríamos isso dentro de um módulo):

`var` `Person =` `function``(firstName, lastName, age){`

`this``.firstName = firstName;`

`this``.lastName = lastName;`

`this``.age = age;`

`}`

`Person.prototype.fullName =` `function``(){`

`return` `this``.firstName +` `" "` `+` `this``.lastName;`

`};`

Olhando apenas a primeira função, você verá que estamos criando um construtor Person**.** Ele é o que usaremos para construir novos objetos Person**.** Ele usa três parâmetros e atribui todos eles ao contexto de execução da chamada atual do construtor**.** É dessa forma que obtemos variáveis ​​de instância pública**.** Podemos criar variáveis privadas aqui também, atribuindo os parâmetros do construtor para variáveis ​​locais dentro do construtor, mas o problema passa a ser o fato de os métodos públicos não poderem acessar essas variáveis, e então provavelmente será melhor tornar todas públicas**.** Você pode criar métodos dentro do construtor que são acessíveis publicamente e pode acessar as variáveis privadas, mas eles criam todo um conjunto diferente de problemas**.**

Em seguida, você verá que estamos acessando o “protótipo” do construtor Person**.** O protótipo de uma função é um objeto para onde todas as instâncias dela vão ao tentar resolver campos ou funções chamadas na instância**.** Então, o que estamos fazendo aqui é criar uma única instância de um método “fullName” que todas as instâncias de “Person” podem acessar sem ter uma tonelada de ocorrências de “fullName” por aí**.** Poderíamos ter definido “fullName” dentro do construtor como “this.fullName = function() { …”, mas depois cada person teria uma outra cópia do método fullName, é não é o que queremos**.**

Se quisermos começar a criar people, poderíamos fazer assim:

`var` `person =` `new` `Person(``"Justin"``,` `"Etheredge"``);`

`alert(person.fullName());`

Se quiséssemos, poderíamos também criar outro construtor que é herdado do construtor Person**.** Vamos dizer que queríamos criar um construtor Spy, que iria construir uma instância de Spy, mas só iria declarar um único método:

`var` `Spy =` `function``(firstName, lastName, age){`

`this``.firstName = firstName;`

`this``.lastName = lastName;`

`this``.age = age;`

`};`

`Spy.prototype =` `new` `Person();`

`Spy.prototype.spy =` `function``(){`

`alert(``this``.fullName() +` `" is spying."``);`

`}`

`var` `mySpy =` `new` `Spy(``"Mr."``,` `"Spy"``, 50);`

`mySpy.spy();`

Como você pode ver, estamos criando um construtor que se parece com Person, mas depois estamos configurando seu protótipo a uma instância do construtor Person**.** Agora podemos adicionar métodos, e quando criarmos uma instância do Spy, ela pode acessar métodos no construtor Person, e os métodos, por fim, podem acessar variáveis ​​que foram atribuídas na instância Spy**!** É um pouco complicado, mas, uma vez que você sobreviver aos detalhes, é bem elegante**.**

## Resumindo

Neste ponto, se você aprendeu algo, então ótimo**!** Mas, infelizmente, nós realmente não tocamos em qualquer desenvolvimento JavaScript “moderno”**.** Todos os tópicos que percorremos neste artigo são relativamente antigos, e têm sido usados de maneira bastante ampla, pelo menos nos últimos anos**.** Mas espero que você esteja no caminho certo. Agora que você está dividindo o seu código em módulos e usando vários arquivos diferentes (você deveria**!**), o próximo passo para você deve ser começar a pesquisar combinação e minimização de JavaScript**.** Se você for um desenvolvedor Rails, e estiver usando o Rails 3, então pode ter tudo isso de graça no pipeline ativo**.** Se estiver usando. NET, então pode dar uma olhada no framework que comecei, [SquishIt](https://github.com/jetheredge/SquishIt) **.** Caso esteja usando ASP.NET MVC 4, ele também tem algumas combinações built in e suporte para minimização**.**

Espero que isso tenha ajudado**!**

*Texto original disponível em <http://www.codethinked.com/preparing-yourself-for-modern-javascript-development>*
