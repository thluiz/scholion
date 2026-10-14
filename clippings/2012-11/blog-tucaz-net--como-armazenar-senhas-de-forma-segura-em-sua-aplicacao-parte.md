---
url: "http://blog.tucaz.net/2012/11/02/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-1/"
captured_at: "2012-11-03T08:00:06-03:00"
title: "Como armazenar senhas de forma segura em sua aplicaçao - Parte 1"
domain: "blog-tucaz-net"
---

Esse é um assunto básico e relativamente simples no contexto que vou apresentar. No entanto é algo largamente negligenciado por muitos sites e aplicaçoes que construimos e consumimos todo dia. Talvez pela aparente simplicidade.

  

Armazenar adequadamente as senhas dos nossos usuários é um dos muitos aspectos que compoe a segurança de nossas aplicaçoes e com poucas horas, ou até minutos, de estudo sobre o assunto é possível faze-lo de maneira bastante satisfatória.

  

Portanto, se você nao quiser fazer um papelao como o [LinkedIn, que armazenava suas senhas em plaintext](http://arstechnica.com/security/2012/06/8-million-leaked-passwords-connected-to-linkedin/) quando foi hackeado ou como o próprio [Yahoo que também nao utilizava melhores praticas](http://news.cnet.com/8301-1009_3-57471178-83/yahoos-password-leak-what-you-need-to-know-faq/) é fundamental levar este assunto a sério.

  

#### Conceitos Básicos

  

A idéia por trás do armazenamento seguro de senhas é garantir que mesmo que alguém nao autorizado tenha acesso a seu banco de dados nao irá conseguir tirar proveito dos dados que acessou.

  

A fim de atingir esse objetivo a prática mais utilizada (se nao única) é a de criptografia. De acordo com a definiçao do [Wikipedia](http://pt.wikipedia.org/wiki/Criptografia) *criptografia* significa:

  
> O estudo dos princípios e técnicas pelas quais a informaçao pode ser transformada da sua forma original para outra ilegível, de forma que possa ser conhecida apenas por seu destinatário

  

Em termos práticos, criptografar uma informaçao significa transformá-la, por meio de um algorítmo, em qualquer outra informacao diferente da original tornando possível a transmissao ou armazenamento de maneira segura.

  

Utilizamos criptografia reversível como [3DES](http://pt.wikipedia.org/wiki/3DES) ou [AES](http://pt.wikipedia.org/wiki/AES) em cenários onde recuperar a informaçao original é fundamental, como no caso de armazenamento de informaçoes confidenciais como por exemplo números de cartoes de crédito **[1]**. Sem que o número do cartao de crédito do cliente seja recuperado é impossível efetuar uma cobranca.

  

Um ponto importante a respeito de criptografia reversível é que a informaçao resultante do processo tem um tamanho variável e geralmente próximo do tamanho da informaçao original portanto uma entrada de dados com tamanho de 3mb, por exemplo, teria uma saída criptografada de aproximadamente 3mb, também.

  

#### Hashing

  

Contudo, em nosso cenário de armazenamento de senhas, nao estamos realmente interessados em conhecer a informaçao original (a senha do usuário), mas sim em garantir que ele tenha digitado-a corretamente quando quiser acessar nossa aplicaçao.

  

Ai entra um outro tipo de algoritmo criptográfico chamado de hashing.

  

Funçoes de hashing recebem uma entrada de dados de tamanho variável e através de um algoritmo fornecem uma saída de dados única e com tamanho fixo e irreversível nao importando o tamanho da entrada. Tomando [MD5](http://pt.wikipedia.org/wiki/MD5) como exemplo, uma entrada de dados de 100kb ou 3mb iriam produzir uma saída única e diferente para cada uma das entradas de dados com um tamanho de fixo 128 bits.

  

A unicidade da saída de dados é garantida até certo ponto e varia de acordo com o algoritmo utilizado e a entrada de dados passada para a funçao. No entanto as chances de colisao (mais de uma entrada mapear para a mesma saida de dados) sao pequenas o suficiente para ignorarmos na maioria dos casos. Ainda no caso de MD5, a primeira colisao apareceria depois de cerca de 2e64 hashes gerados.

  

#### Conclusao

  

Portanto, em nosso cenário a melhor saída é a utilizaçao de uma funçao de hashing ao invés de criptografia. Ainda assim, existem outros cuidados que devemos tomar no uso de funcoes de hashing e é sobre isso que falarei no próximo post quando mostrarei como aplicar tais funçoes no armazenamento e validaçao da senha de um usuário.

  

Até lá :)

  

**[1]** - Armazenar cartoes de crédito de seus clientes nao é uma boa idéia. Quando devemos fazer a cobrança apenas uma vez normalmente nao armazenamos esse número, mas no caso de cobranças recorrentes este é um mal necessário e existem outras regras além de criptografia pra garantir que este processo seja seguro.

  

[[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=Io9CNhElV8w:vVCqTuQE1cw:yIl2AUoC8zA) [![19573bccbf573b8326733b1261924f22.gif](blog-tucaz-net--como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte/19573bccbf573b8326733b1261924f22.gif)](http://feeds.feedburner.com/~ff/tucaz?a=Io9CNhElV8w:vVCqTuQE1cw:63t7Ie-LG7Y) [[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=Io9CNhElV8w:vVCqTuQE1cw:qj6IDK7rITs) [[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=Io9CNhElV8w:vVCqTuQE1cw:V_sGLiPBpWU) [[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=Io9CNhElV8w:vVCqTuQE1cw:7Q72WNTAKBA)

  
[anexo ausente]  
  
  
  
from tucaz [http://blog.tucaz.net/2012/11/02/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-1/?utm\_source=feedburner&utm\_medium=feed&utm\_campaign=Feed%3A+tucaz+%28tucaz.blog.now%28%29%29](http://blog.tucaz.net/2012/11/02/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-1/?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+tucaz+%28tucaz.blog.now%28%29%29)
