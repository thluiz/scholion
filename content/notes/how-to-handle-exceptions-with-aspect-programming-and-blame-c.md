---
title: "How To Handle Exceptions With Aspect Programming And Blame Covfefe"
date: '2026-09-25T00:21:09+01:00'
category: webclip
summary: 'O texto mostra como usar AOP com kaop-ts para tratar exceções e outras preocupações comuns em um só lugar, acessar metadados do join point e até injetar dados assíncronos em métodos decorados.'
tags: ["aspect-oriented-programming", "kaop-ts", "exceptions", "react"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Handle Exceptions With Aspect Programming And Blame Covfefe"
    url: "https://dev.to/k1r0s/how-to-handle-exceptions-with-aspect-programming-and-blame-covfefe"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-handle-exceptions-with-aspect-programming-and-blame-c.md"
    kind: repo
---

The page uses kaop-ts to show how Aspect Oriented Programming can centralize exception handling and other repeated concerns. It first decorates a React render method to append text to an exception, then shows an advice that can replace the result with an error component. The rest of the text explains that AOP helps manage common problems in one place, gives access to join points and metadata, and can work with async requests while keeping the code declarative.

## Fichamento

- O exemplo inicial usa `onException` e `afterMethod` para tratar um erro lançado no `render` de um componente React.
- A classe `Advices` mostra duas ações: uma altera a mensagem da exceção e outra relança a exceção quando ela existe.
- O texto diz que AOP serve para lidar com problemas comuns em um só lugar e acessar o contexto necessário.
- O autor liga AOP à redução de repetição e à organização de lógica em vários pontos de execução chamados join points.
- O artigo afirma que frameworks já tratam muitos problemas comuns, e cita o Express como exemplo em ambientes NodeJS.
- O texto compara frameworks modernos como Vue, Angular e React, destacando programação declarativa e menos efeitos colaterais.
- A biblioteca kaop-ts é apresentada como uma forma de construir aplicações grandes com mais abstração e acesso a join points.
- O texto lista os join points disponíveis como `AfterInstance`, `BeforeInstance`, `AfterMethod`, `BeforeMethod` e `OnException`.
- O exemplo de `Registry` mostra que um advice pode ler `args`, `propertyKey`, `scope`, `rawMethod`, `target` e `result`.
- O autor diz que esses dados podem ser lidos e escritos e que também é possível fazer requisições assíncronas sem bagunçar a call stack.
- No exemplo com `View` e `PersistanceAdvices`, o método `update` recebe dados de uma requisição inseridos pelo advice.
- O texto explica que `this.next` indica ao kaop-ts que a operação atual ainda precisa terminar antes das próximas continuarem.
