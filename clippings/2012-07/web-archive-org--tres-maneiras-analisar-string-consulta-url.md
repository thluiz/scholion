---
url: "https://web.archive.org/web/20150827064713/http://imasters.com.br:80/artigo/24967/desenvolvimento/tres-maneiras-para-analisar-uma-string-de-consulta-em-uma-url/"
captured_at: "2012-07-16T13:36:59-03:00"
title: "Três maneiras para analisar uma string de consulta em uma URL"
domain: "web-archive-org"
---

Não é muito frequente uma string de consulta precisar ser analisada com JavaScript, mas definitivamente não dá para dizer que isso nunca aconteça. Para aquelas raras ocorrências quando você precisa analisar a string de consulta sobre o front end, existem inúmeras maneiras para analisar uma string de consulta em um objeto com cada parâmetro sendo uma propriedade do objeto. Neste artigo, vou mostrar a você três dessas técnicas e te contar um segredo de como estou usando essas técnicas em meus próprios projetos.

  

#### Obtendo a string de consulta

  

Eu sei que o parágrafo introdutório pode ser um pouco enganador, mas as três técnicas não são realmente maneiras de analisar a string de consulta em si; são maneiras de recuperar a string de consulta a partir da URL. Há essencialmente apenas uma técnica que eu conheço e poderia encontrar para converter uma string de consulta em um objeto. Agora vamos listar as três maneiras de puxar a string de consulta a partir de uma URL.

  

**1) Use substring e indexOf**

  

Se você tem uma URL como uma string, você pode simplesmente usar uma combinação de *substring* e *indexOf* para retirar a parte da string que contém os parâmetros de consulta:

  

```
 var queryString = url.substring( query.indexOf('?') + 1 );
```

  

**2) Use as propriedades de location**

  

Se a URL que você precisa analisar é a URL da página em que você está no momento, então a URL é armazenada bem dentro de *window.location*. Melhor ainda, o *location* possui uma propriedade chamada *search*, que vai apenas te fornecer a string de consulta.

  

```
 var queryString = window.location.search;
```

  

Note, porém, que a string de consulta retornada aqui tem o ponto de interrogação na frente dela, então você terá que usar o código a seguir para se livrar dele:

  

```
 queryString = queryString.substring(1);
```

  

**3) Use um elemento âncora**

  

Em um artigo recente intitulado "[The Lazy Man's URL Parsing in JavaScript](http://www.joezimjs.com/javascript/the-lazy-mans-url-parsing/)" (inglês), discuti um método no qual você criou um elemento âncora que analisou URLs para você. Como em *location*, você pode recuperar a string de consulta usando a propriedade *search*. E também como em *location*, você terá que remover o ponto de interrogação principal. Eu sugiro que você leia o artigo acima para aprender como fazer isso.

  

#### Analisando a string de consulta com JavaScript

  

É agora que eu realmente vou te ensinar a analisar a string de consulta. Vamos criar uma função na qual você envia na string de consulta como um parâmetro, e o objeto da consulta é retornado.

  

```
  var parseQueryString = function( queryString ) {  
  var params = {}, queries, temp, i, l;  
   
  // Split into key/value pairs  
  queries = queryString.split("&");  
   
  // Convert the array of strings into an object  
  for ( i = 0, l = queries.length; i < l; i++ ) {  
  temp = queries[i].split('=');  
  params[temp[0]] = temp[1];  
  }  
   
  return params;  
  };
```

  

É realmente muito simples. Primeiro vamos apenas dividir a sequência em partes separadas por um e comercial. Agora temos um array de strings, cada uma das quais está no formato "chave=valor". Portanto, agora só precisamos separar cada um desses pares de chave-valor. Nós percorremos a matriz de strings que temos e dividimos também. Então, usamos o primeiro elemento desse array como a chave de propriedade, o segundo elemento do array como o valor para essa chave, e os adicionamos como uma propriedade para o nosso *queryObj*.

  

#### Usando isso em meus projetos

  

Recentemente, criei um projeto baseado na técnica discutida no artigo à que me referi acima. É uma biblioteca de plugin/standalone jQuery que utiliza essa técnica para analisar URLs para você. Dentro dessa biblioteca/plugin, eu decidi acrescentar algumas propriedades ao parser, incluindo uma propriedade que contém a sequência de consulta analisada, para que você não tenha que analisá-lo você mesmo. Fora isso, esse plugin irá corrigir dois bugs do Internet Explorer relacionados à técnica que lhe dá alguns pequenos recursos adicionais.

  

#### Finalizando

  

Isso conclui o artigo de hoje. Obrigado pela leitura, não se esqueça de compartilhar. E como sempre: Happy Coding!

  

⁂

  

*Texto original disponível em <http://www.joezimjs.com/javascript/3-ways-to-parse-a-query-string-in-a-url/>*

  
  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](web-archive-org--tres-maneiras-analisar-string-consulta-url/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Tr%C3%AAs+maneiras+para+analisar+uma+string+de+consulta+em+uma+URL&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24967%2Fdesenvolvimento%2Ftres-maneiras-para-analisar-uma-string-de-consulta-em-uma-url)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](web-archive-org--tres-maneiras-analisar-string-consulta-url/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Tr%C3%AAs+maneiras+para+analisar+uma+string+de+consulta+em+uma+URL&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24967%2Fdesenvolvimento%2Ftres-maneiras-para-analisar-uma-string-de-consulta-em-uma-url)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/139262262057/u/49/f/546640/c/33212/s/216498e4/a2.htm) ![](http://pi.feedsportal.com/r/139262262057/u/49/f/546640/c/33212/s/216498e4/a2t.img)  
  
[anexo ausente]  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/ceMVFjmJMPo/story01.htm>
