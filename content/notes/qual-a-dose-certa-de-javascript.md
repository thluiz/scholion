---
title: "Qual a dose certa de JavaScript"
date: '2014-06-14T15:41:02-03:00'
category: webclip
summary: 'O texto defende que JavaScript deve melhorar a usabilidade sem tomar o papel do servidor, sem depender da linguagem para tudo e com atenção a performance, acessibilidade e planos alternativos.'
tags: ["javascript", "acessibilidade", "performance", "web"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Qual a dose certa de JavaScript"
    url: "http://tableless.com.br/qual-dose-certa-de-javascript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/tableless-com-br--qual-a-dose-certa-de-javascript.md"
    kind: repo
---

O texto defende que a dose certa de JavaScript depende de como ele melhora a experiência do usuário. A linguagem deve acrescentar interatividade sem exigir que a aplicação dependa totalmente dela, com cuidado para não transferir para o navegador tarefas que cabem ao servidor.

Também propõe práticas para uso responsável de JavaScript, como carregar o código no fim do documento, escrever de forma não obstrusiva, tratar acessibilidade com WAI-ARIA, modularizar o código, carregar partes sob demanda e oferecer versões alternativas quando o peso da aplicação exigir.

## Fichamento

- JavaScript deve servir para melhorar a usabilidade das páginas por meio de interatividade.
- O cliente não deve assumir o papel do servidor nem montar a página toda no front-end.
- A experiência do usuário não deve depender do correto funcionamento de JavaScript.
- O HTML deve chegar primeiro ao usuário e o JavaScript deve ser postergado ao máximo.
- Bibliotecas e frameworks continuam úteis, mas devem entrar em ação depois que o conteúdo principal estiver carregado.
- Código não obstrutivo permite que funcionalidades continuem acessíveis mesmo sem JavaScript.
- Em aplicações de tempo real, quando faltam recursos, podem ser usados paliativos como meta refresh ou botão de atualizar.
- Acessibilidade melhora quando a aplicação não depende exclusivamente de JavaScript.
- WAI-ARIA ajuda a tornar aplicações ricas acessíveis, incluindo modais e conteúdo dinâmico.
- `aria-live` pode indicar ao usuário que uma área sofreu atualização.
- Modularização reduz complexidade e pode permitir carregamento sob demanda de pacotes.
- Uma versão alternativa da aplicação pode oferecer uma experiência limitada quando os recursos forem pesados demais.
- Não existe relação direta entre a quantidade de linhas de JavaScript e a adequação do código.
- A dose certa de JavaScript é a que glorifica a experiência do usuário.
