---
url: "https://imasters.com.br/front-end/serie-backbonejs-parte-01-introducao"
captured_at: "2012-06-11T12:08:24-03:00"
title: "Série Backbone.js: Parte 01 - Introdução"
domain: "imasters-com-br"
---

![39533ea5bc6b7836b4dfc910154489f2.png](imasters-com-br--serie-backbonejs-parte-01-introducao/39533ea5bc6b7836b4dfc910154489f2.png)  
  

O Backbone.js é um framework Javascript que fornece componentes para melhorar a estrutura de aplicações web. Entre estes componentes encontram-se **Models**, **Collections** e **Views**, além de meios nativos de interagir com backends RESTful e JSON. Nesta série de 6 artigos sobre Backbone.js serão abordados seus principais componentes e, ao final, será construída uma aplicação simples de contatos contemplando cada um dos componentes apresentados e com um "bônus" sobre o Slim framework.

  

#### Introdução

  

Ao se construir aplicações web, existe uma grande tendência de se codificar a UI acoplada à estrutura DOM existente, usando extensivamente seletores jQuery e callbacks, além de não se definir um padrão bem definido de mapeamento dos dados do servidor e muito menos a estrutura do código Javascript. Não se pode generalizar, mas boa parte das aplicações web sofrem com esse problema.

  

Com o Backbone.js é possível representar dados do servidor como **Models** no código Javascript, garantindo suporte à validação, exclusão, e gravação no servidor. O Model será apresentado para o usuário através de uma **View**, que irá manipular o Model em questão e poderá definir callbacks para eventos do Model, podendo ser eventos de mudanças nos atributos do Model, remoção, dentre outros, e através destes callbacks a View poderá manter o estado de sua apresentação sempre atualizado, refletindo as mudanças correspondentes no Model.

  

O principal resultado desta abordagem é um código que não inspeciona e nem depende de todo o DOM da aplicação, muito menos dos diversos seletores jQuery ou dos IDs dos elementos, para atualizar manualmente o HTML, pois com essa abordagem as Views sempre se manterão atualizadas conforme as mudanças aos Models. Além disso, é possível ter uma boa separação de cada parte do Javascript, tornando muito mais fácil a manutenibilidade do código. Isso não quer dizer que o código não dependerá de nenhum DOM, porém será minímo, conforme apresentado nos artigos que se sucedem.

  

#### Dependências

  

A principal dependência do [Backbone.js](http://backbonejs.org/) é o framework [Underscore.js](http://documentcloud.github.com/underscore/) que fornece diversos recursos para aplicações Javascript, como suporte a templates, e suporte a recursos de programação funcional.

  

Para utilização de RESTful, manipulação de DOM básico e de suporte a ações com histórico (explicado na parte 5 desta série) será necessário incluir as bibliotecas [json2.js](https://github.com/douglascrockford/JSON-js) e [jQuery](http://jquery.com/) ou [Zepto](http://zeptojs.com/).

  

#### Hello World

  

Implementar um Hello World com o Backbone é bem simples, basta implementar uma View e renderizá-la à página. Primeiramente é necessário baixar as bibliotecas jQuery, Backbone.js e Underscore.js, e colocá-las em alguma pasta da aplicação web, para este exemplo será utilizada a pasta **lib**.

  

A próxima etapa é criar a classe View para a aplicação Hello World. O código abaixo demonstra as etapas necessárias:

  

```
 var HelloView = Backbone.View.extend({  
     el: $('body'),  
     initialize: function() {  
         this.render();  
     },  
     render: function() {  
         $(this.el).append("<h1>Hello World</h1>");  
     }  
 });
```

  

Este código define um novo componente View, que irá renderizar seu conteúdo no elemento , e dois métodos: **initialize** e **render**. O método initialize é chamado quando uma instância da View é feita, funcionando de maneira similar a um construtor. O método render é responsável por gerar o HTML da View em questão, nesse caso somente um título contendo "Hello World". Vale notar que para adicionar o conteúdo à View é utilizado o atributo **this.el** como seletor jQuery, que está configurado como o **body** do HTML.

  

O próximo passo é instanciar a View, e o método initialize será automaticamente invocado, adicionando o H1 ao **body** da página.

  

```
 var helloView = new HelloView();
```

  

O exemplo completo é apresentado abaixo:

  

```
 <!DOCTYPE html>  
 <html>  
     <head>  
         <meta charset="UTF-8" />  
         <title>Hello World</title>  
         <script src="../lib/jquery-min.js"></script>  
         <script src="../lib/underscore-min.js"></script>  
         <script src="../lib/backbone-min.js"></script>  
         <script>  
             $(document).ready(function() {  
                 var HelloView = Backbone.View.extend({  
                     el: $('body'),  
                     initialize: function() {  
                         this.render();  
                     },  
                     render: function() {  
                         $(this.el).append("<h1>Hello World</h1>");  
                     }  
                 });  
                 var helloView = new HelloView();  
             });  
         </script>  
     </head>  
     <body></body>  
 </html>
```

  

#### Código-Fonte dos Artigos

  

Todo o código-fonte criado e apresentado nos diversos artigos desta série poderá ser encontrado no repositório [backbone-tutorial-series em meu GitHub](https://github.com/fernandomantoan/backbone-tutorial-series).

  

#### Referências

  

O Backbone.js conta com uma [boa documentação](http://backbonejs.org/), que apresenta seus componentes, exemplos de uso e, também, apresenta uma [lista com tutoriais](https://github.com/documentcloud/backbone/wiki/Tutorials%2C-blog-posts-and-example-sites) e uma [aplicação de exemplo](http://backbonejs.org/examples/todos/index.html).

  

Na segunda parte desta série de artigos será apresentado mais detalhadamente o componente **View**, responsável por gerenciar a apresentação dos **Models** de uma aplicação web.

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--serie-backbonejs-parte-01-introducao/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=S%C3%A9rie+Backbone.js%3A+Parte+01+-+Introdu%C3%A7%C3%A3o&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24577%2Fjavascript%2Fserie-backbonejs-parte-01-introducao)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--serie-backbonejs-parte-01-introducao/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=S%C3%A9rie+Backbone.js%3A+Parte+01+-+Introdu%C3%A7%C3%A3o&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24577%2Fjavascript%2Fserie-backbonejs-parte-01-introducao)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/136621574273/u/49/f/546640/c/33212/s/203c3fa9/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/HkNucrfP9zc/story01.htm>
