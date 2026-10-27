---
title: "Como armazenar senhas de forma segura em sua aplicação - Parte 2"
date: '2012-12-03T10:12:54-03:00'
category: webclip
summary: 'Explica como usar hashing para guardar senhas sem expor o valor original, mostra um exemplo simples de hash por soma de caracteres e aponta limites e colisões.'
tags: ["hashing", "senhas", "seguranca", "md5"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Como armazenar senhas de forma segura em sua aplicação - Parte 2"
    url: "https://blog.tucaz.net/2012/11/30/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-2/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-12/blog-tucaz-net--como-armazenar-senhas-de-forma-segura-parte-2.md"
    kind: repo
---

A página retoma a ideia de hashing para proteção de senhas e mostra um fluxo em que o sistema armazena o hash da senha no cadastro e, no login, compara o hash calculado com o hash guardado. O texto diz que isso impede o acesso à senha original mesmo se o banco de dados for comprometido, e também impede que os mantenedores da aplicação vejam a senha do usuário.

## Fichamento

- No cadastro, o sistema armazena o hash da senha em vez da senha em texto puro.
- No login, o sistema calcula o hash da senha informada e compara esse valor com o hash salvo.
- O texto afirma que esse método preserva a senha original mesmo se a base de dados cair em mãos erradas.
- O texto afirma também que os mantenedores da aplicação não têm acesso à senha original.
- O exemplo de hash simples soma o valor dos caracteres da entrada e retorna esse total como texto.
- O autor mostra que "senha" e "SENHA" geram hashes diferentes, porque o algoritmo diferencia maiúsculas e minúsculas.
- O mesmo exemplo produz colisão, já que "senha" e "ddddM2" geram o mesmo resultado.
- A colisão ocorre porque o algoritmo é simples demais e soma os valores ASCII dos caracteres.
- O texto conclui que esse algoritmo não deve ser usado para proteger aplicações.
- O post cita o MD5 como um algoritmo muito usado para gerar hashes e informa que ele existe nativamente em .NET.
- O texto diz que o MD5 não é mais considerado seguro e pode ser quebrado facilmente.
- O autor anuncia que vai falar de outras formas de manter as senhas seguras no próximo post.
