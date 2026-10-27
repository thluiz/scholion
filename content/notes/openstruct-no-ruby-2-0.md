---
title: "OpenStruct no Ruby 2.0"
date: '2013-01-21T10:12:50-03:00'
category: webclip
summary: 'A versão RC1 do Ruby 2.0.0 trouxe mudanças na OpenStruct: acesso por índice, atribuição por índice, conversão para Hash com `to_h` e criação a partir de OpenStruct ou Struct.'
tags: ["ruby", "openstruct", "ostruct", "hash"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "OpenStruct no Ruby 2.0"
    url: "https://nandovieira.com.br/openstruct-no-ruby-dois-ponto-zero"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/nandovieira-com-br--openstruct-no-ruby-2-0.md"
    kind: repo
---

A versão RC1 do Ruby 2.0.0 trouxe mudanças na classe OpenStruct que ampliam a forma de acessar e criar seus atributos. O texto destaca o uso por índice, a definição por índice, a conversão para Hash e a possibilidade de instanciar uma OpenStruct a partir de outra OpenStruct ou de um Struct.

## Fichamento

- OpenStruct permite criar uma estrutura de dados com atributos definidos de forma arbitrária.
- Ao instanciar com um Hash, cada chave gera um atributo equivalente.
- No Ruby 2.0, além dos readers, a OpenStruct passou a aceitar acesso por `[]` com chaves como `:name` e `"name"`.
- O método `OpenStruct#[]=` permite definir atributos por índice.
- O método `OpenStruct#to_h` passa a retornar a representação da OpenStruct como Hash; no Ruby 1.9 ele retornava `nil`.
- `OpenStruct.new` agora aceita instâncias de `OpenStruct` e `Struct`.
- O texto associa essa mudança ao interesse de quem gosta de `HashWithIndifferentAccess` no ActiveSupport.
