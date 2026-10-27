---
url: "https://tableless.com.br/reveal-js-criando-apresentacoes-no-navegador/"
captured_at: "2013-02-15T16:42:27-03:00"
title: "Reveal.js: criando apresentações no navegador"
domain: "tableless-com-br"
---

Apresentações não estão mais limitadas a softwares e plataformas específicas – hoje em dia é possível criar slides utilizando o navegador e tecnologias como HTML5, CSS3 e JavaScript.

  

Uma das responsáveis por isto é a biblioteca JavaScript [reveal.js](http://lab.hakim.se/reveal-js/), criada por Hakim El Hattab, desenvolvedor mais conhecido por seus [experimentos com animações CSS3](http://lab.hakim.se/).

  

Neste artigo vamos criar uma apresentação básica e conhecer as opções disponíveis para personalizar nossos slides.

  

## Estrutura da apresentação

  

Vamos começar fazendo o download da última versão da biblioteca reveal.js disponível no GitHub: <https://github.com/hakimel/reveal.js/downloads>.

  

Feito isso, basta criar um arquivo index.html e copiar os arquivos da biblioteca para o diretório da apresentação. Nosso HTML inicial fica assim:

  

```
 <!doctype html>  
 <html>  
   <head>  
     <meta charset="utf-8">  
     <title>Apresentação Exemplo Tableless</title>  
     <link rel="stylesheet" href="css/reveal.min.css">  
     <link rel="stylesheet" href="css/theme/default.css">  
   </head>  
   <body>  
     <div class="reveal">  
       <div class="slides"></div>  
     </div>  
     <script src="lib/js/head.min.js"></script>  
     <script src="js/reveal.min.js"></script>  
   </body>  
 </html>
```

  

A apresentação precisa seguir uma estrutura pré-definida: a biblioteca irá procurar um *div* com a classe *reveal* que contenha outro *div* com a classe *slides*.

  

O elemento *div.slides* receberá os slides de nossa apresentação. Os slides precisam ser elementos do tipo *section*. Vamos, então, adicionar nossos três slides à apresentação:

  

```
 ...  
 <div class="reveal">  
   <div class="slides">  
     <section>  
       <h1>Apresentações no navegador</h1>  
       <h3>Exemplo de apresentação Tableless</h3>  
     </section>  
     <section>  
       <h1>Sobre o autor</h1>  
       <ul>  
         <li>15 anos de experiência</li>  
         <li>desenvolvedor na globo.com</li>  
       </ul>  
     </section>  
     <section>  
       <h1>reveal.js</h1>  
         <ul>  
           <li>desenvolvida por Hakim El Hattab</li>  
           <li>open source</li>  
         </ul>  
     </section>  
   </div>  
 </div>  
 ...
```

  

O último passo é iniciar o objeto Reveal:

  

```
 ...  
 <script src="lib/js/head.min.js"></script>  
 <script src="js/reveal.min.js"></script>  
 <script>  
   Reveal.initialize();  
 </script>  
 ...
```

  

Agora basta abrir o arquivo index.html no seu navegador favorito e conferir o resultado.

  

## Opções

  

O método *initialize* pode receber como parâmetro um objeto com as opções da apresentação. É possível, por exemplo, esconder os controles de navegação, habilitar navegação via teclado, alterar o efeito de transição dos slides, entre outros.

  

Vamos agora mudar nossa inicialização, alterando algumas configurações:

  

```
 Reveal.initialize({  
   autoSlide: 6000,  
   center: true,  
   controls: false,  
   mouseWheel: true,  
   transition: 'concave'  
 });
```

  

Com as configurações acima nós habilitamos a troca automática de slides após 6 segundos, centralizamos o conteúdo dos nossos slides, desabilitamos os controles de navegação, habilitamos a navegação utilizando o scroll do mouse e alteramos a transição dos slides para o efeito ‘concave’.

  

Para conferir uma lista completa de opções disponíveis, leia o [README](https://github.com/hakimel/reveal.js/blob/master/README.md#configuration) do projeto no github.

  

## Fragmentos

  

Para utilizar fragmentos com reveal.js basta adicionar a classe *fragment* a um ou mais conteúdos dentro de um slide.

  

Vamos alterar o nosso slide “Sobre o autor” e exibir os ítens da lista de forma fragmentada:

  

```
 ...  
    <h1>Sobre o autor</h1>¬  
    <ul>¬  
      <li class="fragment">15 anos de experiência</li>¬  
      <li class="fragment">desenvolvedor na globo.com</li>¬  
    </ul>¬  
 ...
```

  

Atualizando a apresentação no navegador, ao chegar no slide acima, os elementos da lista serão exibidos passo a passo.

  

## Temas & Plugins

  

Além do tema padrão, a biblioteca reveal.js disponibiliza outros temas para nossas apresentações. São eles: *beige*, *night*, *serif*, *simple* e *sky*.

  

Para utilizar um tema diferente, basta alterar o link do CSS de *default* para o tema desejado. No exemplo abaixo passamos a utilizar o tema *night*.

  

```
 ...  
 <link rel="stylesheet" href="css/reveal.min.css">  
 <link rel="stylesheet" href="css/theme/night.css">  
 ...
```

  

Outra forma de alterar e estender nossa apresentação é utilizar o pacote de plugins que acompanha a biblioteca. Dentro do diretório *plugin* estão disponíveis extensões para adicionar conteúdo com Markdown, zoom, notas e highlight de código.

  

Para ativar um plugin, basta adicionar a opção *dependencies* na inicialização do objeto Reveal:

  

```
 Reveal.initialize({  
   autoSlide: 6000,  
   center: true,  
   controls: false,  
   mouseWheel: true,  
   transition: 'concave',  
   dependencies: [{ src: 'plugin/zoom-js/zoom.js' }]  
 });
```

  

No exemplo acima habilitamos o plugin de zoom. Agora, ao utilizar a combinação *alt + clique do mouse* aplicamos zoom in/zoom out nos slides.

  

## E mais…

  

Isso foi só uma parte do que a biblioteca reveal.js oferece. É possível ainda criar temas próprios (o diretório de temas inclui um esqueleto em Sass), tirar proveito da API JavaScript do objeto Reveal (com métodos para controlar a navegação dos slides), escutar os eventos disparados por trocas de slides e fragmentos, entre outras coisas.

  

Além do pacote JavaScript, você pode criar suas apresentações utilizando o serviço [www.rvl.io](http://www.rvl.io/), sem a necessidade de código.

  

Para finalizar, seguem os links do código fonte do exemplo e da apresentação criada aqui:

  

[código fonte da apresentação](https://github.com/tableless/exemplos/tree/gh-pages/revealjs)

  

[visualizar a apresentação no navegador](http://tableless.github.com/exemplos/revealjs/)

O post [Reveal.js: criando apresentações no navegador](http://tableless.com.br/reveal-js-criando-apresentacoes-no-navegador/) foi originalmente publicado em [Tableless](http://tableless.com.br/).

  

[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:yIl2AUoC8zA) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:D7DqB2pKExk) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:7Q72WNTAKBA) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:aKCwKftKxY0) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:dnMXMwOfBR0) [![461e440a1d3becc7e11e0f65f4ce18e3.gif](tableless-com-br--revealjs-criando-apresentacoes-no-navegador/461e440a1d3becc7e11e0f65f4ce18e3.gif)](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:YwkR-u9nhCs) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:JEwB19i1-c4) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:wF9xT3WuBAs) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:V_sGLiPBpWU) [![980a0ed8254c7a6a3722903cbad9d965.gif](tableless-com-br--revealjs-criando-apresentacoes-no-navegador/980a0ed8254c7a6a3722903cbad9d965.gif)](http://feeds.feedburner.com/~ff/tableless?a=avZzt_E0iCw:P680x1KmbIU:tYZ39nBRSfM)

  
[anexo ausente]  
  
  
  
from Tableless.com.br - Web Standards com Arroz e Feijão [http://tableless.com.br/reveal-js-criando-apresentacoes-no-navegador/?utm\_source=feedburner&utm\_medium=feed&utm\_campaign=Feed%3A+tableless+%28Tableless%29](http://tableless.com.br/reveal-js-criando-apresentacoes-no-navegador/?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+tableless+%28Tableless%29)
