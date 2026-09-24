---
title: "A Go Microservices Demo using Go kit And API Gateway Pattern"
date: '2026-09-25T00:34:03+01:00'
category: webclip
summary: 'The article shows how to turn go-kit stringsvc3 into a more practical demo by adding Consul-based service discovery, an API gateway client, Docker images, and round-robin load balancing.'
tags: ["go-kit", "microservices", "api-gateway", "service-discovery"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Go Microservices Demo using Go kit And API Gateway Pattern"
    url: "https://dev.to/maxwellhertz/a-go-microservices-demo-using-go-kit-and-api-gateway-pattern-2321"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--go-microservices-demo-using-go-kit-and-api-gateway-pattern.md"
    kind: repo
---

The article says go-kit is useful but its examples can be hard to follow, so the author combines stringsvc3 with the apigateway example to build a more practical microservices demo. The focus is on implementing the API gateway with Consul-based service discovery, then packaging the services with Docker and testing them through a client that routes requests to multiple service instances.

## Fichamento

- O autor diz que encontrou go-kit interessante, mas com exemplos pouco claros, e que o tutorial stringsvc e a implementação de stringsvc3 o confundiram.
- Ele conclui que o exemplo original só simulava um API gateway, o que seria pouco prático no mundo real.
- Para montar uma demo mais útil, ele combina stringsvc3 com o exemplo apigateway.
- O texto afirma que a implementação vai focar no API gateway, não nos conceitos básicos de endpoint, transport ou service.
- A arquitetura usa service discovery como parte central da solução de microsserviços.
- O exemplo escolhe Consul para fazer um service discovery simples do lado do cliente.
- Na registration, o serviço stringsvc é registrado no Consul com um ID único, nome do serviço, address e port.
- O texto menciona que é preciso informar o endereço do Consul por variável de ambiente ou arquivo de configuração.
- Antes de encerrar o programa, o autor destaca que é importante chamar Deregister.
- Para empacotar a aplicação, ele cria uma imagem Docker do stringsvc com Go modules e um build em duas etapas.
- O gateway é outro projeto Go modules, chamado stringclient.
- Nesse cliente, o código cria um instancer do Consul para obter instâncias do serviço registradas.
- O autor explica que o quarto parâmetro de consul.NewInstancer filtra serviços por tags e o último controla se só instâncias saudáveis devem ser retornadas.
- O cliente cria endpoints para uppercase e count, usa round-robin load balancing e aplica retry.
- A função serviceFactoryBuilder monta uma factory que transforma uma instância em endpoint HTTP apontando para o path correto.
- O deploy usa Docker Compose com um contêiner do Consul, três instâncias de stringsvc e um stringclient exposto na porta 8080.
- Os testes mostram chamadas para uppercase e count, com respostas FOO e 3.
- Em uma sequência de chamadas, os logs mostram que as três instâncias do serviço são chamadas uma por uma.
- O texto atribui esse comportamento à política round-robin usada ao criar o endpoint.
