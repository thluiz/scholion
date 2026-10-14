---
title: "Como armazenar senhas de forma segura em sua aplicação - Parte 1"
date: '2012-11-03T08:00:06-03:00'
category: webclip
summary: 'O texto defende que senhas não devem ser armazenadas com criptografia reversível, mas com hashing, porque o objetivo é verificar o acesso sem recuperar a senha original.'
tags: ["senhas", "hashing", "criptografia"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Como armazenar senhas de forma segura em sua aplicaçao - Parte 1"
    url: "http://blog.tucaz.net/2012/11/02/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-1/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/blog-tucaz-net--como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte.md"
    kind: repo
---

O texto diz que armazenar senhas com segurança é um aspecto básico da segurança de aplicações e que isso costuma ser negligenciado. Usa exemplos de vazamentos para mostrar que levar o tema a sério evita problemas como guardar senhas em plaintext.

## Fichamento

- O armazenamento seguro de senhas deve impedir que alguém com acesso ao banco de dados consiga tirar proveito dos dados.
- Criptografia reversível é indicada quando recuperar a informação original é necessário, como em números de cartão de crédito.
- No caso de senhas, o objetivo não é recuperar a senha original, mas verificar se o usuário digitou a senha correta.
- Funções de hashing recebem entrada de tamanho variável e produzem saída de tamanho fixo e irreversível.
- O texto conclui que hashing é a melhor opção para esse cenário e antecipa que ainda existem cuidados adicionais no uso dessas funções.
