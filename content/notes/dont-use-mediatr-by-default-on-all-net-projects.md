---
title: "Don't use MediatR by default on all .NET projects"
date: '2026-09-25T09:00:42+01:00'
category: webclip
summary: 'O texto defende que MediatR não deve entrar por padrão em todo projeto .NET: a escolha depende do caso de uso, e usar mensageria interna em contextos dependentes pode criar complexidade desnecessária.'
tags: ["net", "mediatr", "clean-architecture", "cqrs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Don't use MediatR by default on all .NET projects"
    url: "https://goatreview.com/dont-use-mediatr-by-default-net-projects/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=lesser-known-clr-gc-handles&_bhlid=46b30461a47be60a285fd3e1c55ba62047e3509b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/goatreview-com--dont-use-mediatr-by-default-on-all-net-projects.md"
    kind: repo
---

The article argues that MediatR became common in .NET templates and tutorials, but that it should be added only when the use case justifies it. It shows a simpler use-case-based approach with commands and handlers, while keeping the option to switch to MediatR later if needed.

It also warns against using internal messaging between dependent contexts, especially when the operations must stay atomic. In that case, the text prefers direct service adapters over commands sent through MediatR, and says the same caution applies to other libraries such as EF Core and FluentValidation.

## Fichamento

- MediatR virou quase sinônimo de Clean Architecture em projetos .NET, mas isso não o torna uma dependência obrigatória.
- A biblioteca facilita o padrão mediator e o desacoplamento entre camadas, porém sua adoção deve ser pensada caso a caso.
- O texto propõe manter uma arquitetura centrada em casos de uso sem depender do sistema interno de mensagens do MediatR.
- A estrutura sem MediatR usa interfaces próprias para comandos e handlers, com declaração parecida à da biblioteca.
- As rotas da API ficam praticamente iguais nas duas abordagens, mudando apenas a injeção do handler ou do sender.
- A configuração sem MediatR pode ser feita com registro explícito do handler no container, e o autor diz que isso também poderia ser automatizado com uma extensão parecida com RegisterServicesFromAssemblies.
- O texto evita usar CQRS como rótulo para esse exemplo, porque associa CQRS a separação de leitura e escrita em banco de dados.
- A principal vantagem da abordagem sem MediatR é permitir voltar à biblioteca depois, com mudanças pequenas nas interfaces e nas declarações dos endpoints.
- Usar MediatR para disparar outras operações dentro de um handler vira um problema quando as operações são dependentes entre si.
- Se a criação de um goat e a gravação de um audit trail forem independentes, o texto defende publicar um evento ao final do processamento.
- Se as operações forem atômicas, enviar comandos depois do handler termina pode atrasar validações como a checagem de créditos.
- Nesse cenário, chamar outro contexto dentro do handler por meio de mensageria interna aumenta a complexidade e mistura serviços dependentes.
- A alternativa sugerida é usar adapters de serviço para comunicação entre contextos, mantendo a relação atômica quando ela for necessária.
- A conclusão amplia a crítica para outras bibliotecas usadas por hábito, como EFCore e FluentValidation, e pergunta se a escolha técnica é necessidade real ou gosto de desenvolvedor.
