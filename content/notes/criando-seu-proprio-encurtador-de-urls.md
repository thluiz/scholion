---
title: "Criando seu próprio encurtador de URLs"
date: '2012-12-28T10:44:11-03:00'
category: webclip
summary: 'O texto mostra como montar um encurtador de URLs com Ruby, Sinatra e Redis, usando base 36 para o id, MD5 para identificar a URL e uma gem chamada Dogo para simplificar a execução em produção.'
tags: ["encurtador-de-urls", "ruby", "sinatra", "redis"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Criando seu próprio encurtador de URLs"
    url: "http://simplesideias.com.br/criando-seu-proprio-encurtador-de-urls"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-12/simplesideias-com-br--criando-seu-proprio-encurtador-de-urls.md"
    kind: repo
---

O texto explica uma forma simples de criar um encurtador de URLs. A ideia é usar o id do registro em base 36 para gerar identificadores curtos, guardar as URLs no Redis e usar um hash MD5 para representar cada URL original.

## Fichamento

- O autor viu um domínio sem uso e decidiu criar um encurtador de URL com Sinatra e Redis.
- O id do registro pode ser convertido para base 36, o que gera identificadores curtos e reaproveita números grandes com poucos caracteres.
- O Redis é descrito como uma boa opção para armazenar as URLs por ser fácil de usar e rápido.
- A URL pode ser guardada em uma chave formada por uma identificação da URL original e pelo id curto.
- O comando `INCR` serve para obter o próximo id disponível.
- Um hash MD5 da URL ajuda a representar a URL original e a verificar se ela já foi salva.
- A recuperação da URL original pode ser feita buscando a chave pelo id curto e lendo o valor associado.
- O autor diz que empacotou essa ideia na gem Dogo, que já fornece um servidor Sinatra para lidar com as requisições.
- O projeto usa um `Gemfile` com `dogo`, `unicorn` e dependências de desenvolvimento como `pry`, `awesome_print` e `thin`.
- O arquivo `config.ru` define `Dogo.host`, `Dogo.api_key` e `Dogo.default_url`, e inicia o servidor com `Dogo::Server.new`.
- O servidor responde ao caminho raiz redirecionando para `Dogo.default_url`.
- A criação de URLs encurtadas pode ser feita por uma requisição `GET` no endpoint `/shorten`, para funcionar com o Tweetbot.
- A URL original fica acessível por `http://fnando.me/<id>`.
- O Dogo conta cliques por URL e armazena esses números em `clicks.<id curto>`.
