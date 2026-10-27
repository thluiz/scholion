---
title: "Nodejs - A performance que eu sempre quis ter"
date: '2012-07-21T00:35:19-03:00'
category: webclip
summary: 'A apresentação relaciona o crescimento de usuários de internet e redes sociais com a necessidade de arquiteturas que respondam rápido e lidem com muitos requests, destacando I/O não bloqueante e o V8 do Node.js.'
tags: ["nodejs", "performance", "escalabilidade", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Nodejs - A performance que eu sempre quis ter"
    url: "http://www.slideshare.net/emerleite/nodejs-a-performance-que-eu-sempre-quis-ter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/slideshare-net--nodejs-a-performance-que-eu-sempre-quis-ter.md"
    kind: repo
---

A apresentação liga o aumento de usuários de internet e de redes sociais à pressão por sistemas que atendam muitos requests com rapidez. O foco está em como arquiteturas web precisam lidar com concorrência e em por que tecnologias baseadas em I/O não bloqueante ganham espaço nesse cenário.

## Fichamento

- O autor mostra o crescimento do número de usuários de internet de 2000 a 2010 no mundo e no Brasil.
- A apresentação contrasta um cenário de poucos usuários, em que qualquer tecnologia funciona, com outro de muitos usuários, em que nem toda tecnologia dá conta.
- O texto compara tecnologias web surgidas em épocas diferentes, como PHP, Java EE, ASP.Net, Ruby on Rails e Django.
- A pergunta central é por que adotar mais uma tecnologia quando já existem várias opções.
- O material relaciona escalabilidade com estrutura física de servidores e com estratégias de escala vertical e horizontal.
- Em bancos de dados, o slide aponta escalonamento horizontal com shards e separação entre read e write.
- Para atender muitos requests, a orientação é finalizar a requisição o mais rápido possível.
- A apresentação sugere que, em 2014, cerca de 70% dos adultos seriam usuários regulares de redes sociais.
- O problema das tecnologias atuais é descrito como a dificuldade de manter 10, 20 ou 30 mil usuários simultâneos conectados.
- O slide destaca Node.js como "Evented, non-blocking I/O" e usa o Google V8 Engine como parte da proposta.
- O texto critica o padrão em que o software fica travado esperando a resposta de uma query.
- Rails e Django aparecem associados a runtime, block e process em um diagrama de processamento.
- Java aparece com servlet container e threads, mostrando que cada request pode abrir uma thread e bloquear recursos.
- A apresentação conclui a comparação com gráficos de concurrency versus reqs/sec e concurrency versus memory em Apache e NGINX.
