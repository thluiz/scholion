---
url: "http://blog.caelum.com.br/boas-praticas-com-javascript-e-jquery-codigo-nao-obstrusivo/"
captured_at: "2012-06-04T15:34:22-03:00"
title: "Boas práticas com JavaScript e jQuery: código não-obstrusivo"
domain: "blog-caelum-com-br"
---

![8aab83bad293f8801da06f15a0415115.jpg](blog-caelum-com-br--boas-praticas-com-javascript-e-jquery-codigo-nao-obstrusivo/8aab83bad293f8801da06f15a0415115.jpg)

  

Já há bastante tempo, por conta do amadurecimento da Web como plataforma de aplicações, a programação front-end de aplicações para Web vem adotando alguns [padrões e boas práticas](http://coding.smashingmagazine.com/2008/09/16/jquery-examples-and-best-practices/). Os benefícios disso são claros, principalmente quando consideramos o fato de que até as mais simples páginas Web não são tão triviais: são compostas de camadas distintas de marcação, apresentação e interatividade, normalmente tendo HTML, CSS e JavaScript como responsáveis.

  

Uma das práticas mais importantes quando pensamos na tríade do front-end é o desacoplamento dessas camadas, ou seja, **não devemos adicionar informações visuais, nem sobre interatividade com o usuário, na camada de marcação**. Dessa maneira a manutenção de cada componente é muito mais fácil pois cada um tem seu lugar distinto. Infelizmente a mistura ainda ocorre, como este frequente código:

  

```
 <a style="font-size:16px" href="#" onclick="adicionaItem()">Adicionar item</a>
```

  

No exemplo acima posso distinguir claramente quem não pertence ao HTML, se levarmos em consideração as camadas visuais (`style`) e de interatividade (`onclick`). Elas não deveriam estar ali. Para mantermos nossa marcação limpa podemos utlizar um seletor do CSS para externalizar as informações visuais, para deixar o exemplo simples vamos trocar os atributos alienígenas (pertencentes a outras camadas) por um atributo `id`:

  

```
 <a id="additem" href="#">Adicionar item</a>
```

  

Agora podemos criar o seguinte seletor no CSS e adicioná-lo ao HTML de maneira adequada (tag `<style>` ou `<link>` para arquivo CSS externo):

  

```
 #additem {  
   font-size: 16px;  
 }
```

  

De acordo com o demonstrado no primeiro exemplo, o navegador deve disparar a execução da função JavaScript `adicionaItem()`, quando o usuário clicar na área da página ocupada pelo elemento `<a>`. A implementação dessa função não é de nosso interesse no exemplo, só precisamos executá-la. Como fazer isso sem adicionar essa função diretamente na marcação HTML?

  

Uma das características mais importantes da execução de JavaScript em uma página Web é que o navegador disponibiliza acesso a todo e qualquer elemento declarado no HTML através da DOM API (Document Object Model API). Isso significa que podemos, em nosso código JavaScript, criar objetos que fazem referência direta a tags do HTML.

  

Alguns desses objetos refletem a alteração de seus atributos imediatamente no navegador. Para implementar o comportamento necessário devemos informar ao navegador que em determinado elemento há uma função a ser executada caso ele seja o *taget* de um evento. Para obtermos esse resutado precisamos interagir com o *EventListener* desse elemento. Em JavaScript puro teríamos a seguinte abordagem:

  

```
 // Primeiro é necessário criar um objeto que faz  
 // referência ao elemento no HTML:  
 var linkAddItem = document.getElementById('additem');  
   
 // Depois adicionamos a função "adicionaItem" à lista de  
 // funções que devem ser executadas quando o usuário clica  
 // na área do elemento no navegador:  
 linkAddItem.addEventListener('click', adicionaItem);
```

  

Esse padrão é o que chamamos de **JavaScript não-obstrusivo**. Estamos adicionando interatividade à página através do JavaScript, sem a adição de atributos e informações desnecessárias na marcação. Note que passamos como segundo argumento o nome da função somente, sem os parênteses, necessários para executá-la. Isso porque não queremos executá-la de fato, apenas delegar sua execução à ocorrência do evento.

  

Fato é que os navegadores (principalmente o IE) não são exatamente consistentes na implementação desses objetos em suas APIs. A própria função `addEventListener` não existe no IE, devemos chamar a função `attachEvent`, que implementa o mesmo comportamento.

  

Para termos um código compatível entre navegadores, seria necessário realizar uma série de verificações para identificar qual abordagem tomar em cada caso. A boa notícia é que algumas bibliotecas de JavaScript fazem isso para nós, elas abstraem essas diferenças em funções relativamente mais simples e compatíveis com os principais navegadores, versões e plataformas, se não todas.

  

[![8aab83bad293f8801da06f15a0415115.jpg](blog-caelum-com-br--boas-praticas-com-javascript-e-jquery-codigo-nao-obstrusivo/8aab83bad293f8801da06f15a0415115.jpg)](http://caelum.wpengine.netdna-cdn.com/wp-content/uploads/2012/05/jq.jpg)

  

O [jQuery](http://jquery.com/), hoje a biblioteca JavaScript que é quase onipresente, interage com os `EventListeners` de maneira bem direta:

  

```
 $('#additem').on('click', adicionaItem);
```

  

Caso você precise usar uma versão anterior a 1.7 do jQuery, substitua a função “on()” pela “bind()”.

  

No código acima, a função `$('#additem')` nos retorna um objeto que representa o elemento com id `additem` em nossa marcação. Esse é um objeto do jQuery e podemos chamar sua função `on()` que precisa de dois argumentos: o nome do evento a ser observado e o nome da função que deve ser executada ao ocorrer esse evento na área que o elemento ocupa na página. Essa abordagem nos permite descartar o atributo alienígena `onclick` no HTML, sendo que o próprio JavaScript identifica qual função deve ser executada quando ocorre um evento em determinado elemento da página.

  

Nos casos em que a função a ser executada precise de argumentos, não podemos passar os argumentos com esse padrão, é necessário passar como argumento para a função `on()` uma função anônima e, dentro dessa, chamar a função `adicionaItem()` com argumentos.

  

Essa função anônima (bem como a função `adicionaItem` nos exemplos anteriores) recebe, por padrão, um objeto que representa o evento ocorrido no caso de sua execução. Esse objeto contém diversas informações interessantes como um timestamp de quando ocorreu o evento, no caso do evento `click`, quais eram as coordenadas do mouse na janela do navegador no momento do clique entre outras.

  

Vamos supor um número como argumento por exemplo:

  

```
 $('#additem').on('click', function(event) {  
     // Essa função anônima pode conter uma lógica mais complexa.  
     adicionaItem(1);  
 });
```

  

Por estarmos adicionando um evento a um link nesse exemplo, o comportamento padrão do navegador é, após a execução da função JavaScript, o evento retorna ao seu ciclo normal e o usuário será levado ao endereço declarado no link, nesse caso o topo da página (`href="#"`). Normalmente esse comportamento é indesejado, então vamos informar nossa função que queremos anular o restante do ciclo do evento:

  

```
 $('#additem').on('click', function(event) {  
     // Essa função anônima pode conter uma lógica mais complexa.  
     adicionaItem(1);  
     // Anular a continuação do ciclo do evento no navegador:  
     event.preventDefault();  
 });
```

  

Nos primeiros exemplos, quando passamos o nome da função diretamente à funcão `on()`, seria necessário adicionar a linha `event.preventDefault()` dentro da função `adicionaItem()` para obtermos o comportamento correto. Alguns desenvolvedores também utilizam `return false;` no lugar de `event.preventDefault();` para obter o mesmo resutado.

  

Esse tratamento direto do objeto *event* permite inclusive a adoção de um outro padrão recomendado: nenhum link deve levar ao destino “#” (topo da página), a não ser que seja essa sua finalidade. O ideal é que no atributo href seja utilizado um URL que realizará o mesmo comportamento que esperamos com o JavaScript, só que sem JavaScript. Esse *fallback* é importante para acessibilidade e atende dispositivos que não suportam JavaScript.

  

Podemos atribuir uma função ao `EventListener` de qualquer elemento, não só dos links. Nesses casos não precisamos anular o comportamento padrão do evento com “`event.preventDefault()`” visto que clicar em uma `<img>` ou `<div>` qualquer não tem efeito colateral na interação do usuário com a página.

  
  
  
from blog.caelum.com.br <http://blog.caelum.com.br/boas-praticas-com-javascript-e-jquery-codigo-nao-obstrusivo/>
