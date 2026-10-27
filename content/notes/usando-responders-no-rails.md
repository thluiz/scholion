---
title: "Usando responders no Rails"
date: '2012-09-03T10:51:25-03:00'
category: webclip
summary: 'O texto mostra como `respond_with` simplifica controllers que repetem `respond_to`, como a gem `responders` centraliza flash messages e como criar um responder próprio para casos fora do padrão.'
tags: ["rails", "responders", "controllers", "ruby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Usando responders no Rails"
    url: "https://nandovieira.com.br/usando-responders-no-rails"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-09/nandovieira-com-br--usando-responders-no-rails.md"
    kind: repo
---

O texto apresenta o Responder do Rails como uma forma de abstrair como controllers respondem a requisições. Em vez de repetir blocos `respond_to` em várias actions, `respond_with` deixa o controller mais conciso e usa o estado do recurso para decidir a resposta.

## Fichamento

- O Responder foi introduzido no Rails 3.0 para abstrair como controllers respondem às requisições.
- Um controller gerado por scaffold costuma repetir a mesma estrutura `respond_to` em várias actions.
- `respond_with` usa `ActionController::Responder` e torna o controller mais curto e simples.
- Antes de usar o Responder, o controller precisa declarar quais formatos aceita com `respond_to`.
- O Responder considera o estado do recurso e o formato solicitado para decidir entre comportamento de navegação ou de API.
- A gem `responders` reduz ainda mais a duplicação ao lidar com flash messages de forma automática.
- Para usar a gem, basta adicioná-la ao `Gemfile`, executar `bundle install` e definir `respond_to` e `responders` no `ApplicationController`.
- Com a gem, o controller pode remover as definições manuais de flash e continuar usando `respond_with`.
- A gem oferece suporte a flash messages internacionalizadas e também permite personalização por controller e action.
- Quando o fluxo foge do padrão, o texto recomenda criar um responder próprio em vez de voltar ao `respond_to` no controller.
- O exemplo de comentário cria um responder específico para a action `create`, com lógica própria para HTML.
- Um responder personalizado pode herdar de `ActionController::Responder`, incluir `Responders::FlashResponder` e delegar `t` e `flash` ao controller.
- O controller usa a opção `:responder` em `respond_with` para aplicar o responder específico da action.
- O texto encerra dizendo que a confirmação do comportamento deve vir de testes de integração, verificando a presença da mensagem conforme o estado do objeto.
