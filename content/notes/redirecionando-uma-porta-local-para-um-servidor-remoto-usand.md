---
title: "Redirecionando uma porta local para um servidor remoto usando SSH"
date: '2013-01-21T12:09:01-03:00'
category: webclip
summary: 'Mostra como usar SSH e NGINX para expor serviços locais num servidor remoto, evitando depender de serviços como localtunnel e mantendo um endereço estável para testes.'
tags: ["ssh", "nginx", "servidor-remoto", "redirecionamento-de-porta"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Redirecionando uma porta local para um servidor remoto usando SSH"
    url: "https://nandovieira.com.br/redirecionando-uma-porta-local-para-um-servidor-remoto-com-ssh"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/nandovieira-com-br--redirecionando-uma-porta-local-para-um-servidor-remoto-usand.md"
    kind: repo
---

Mostra uma forma simples de expor serviços que rodam na máquina local usando SSH e um servidor web. O texto compara essa abordagem com serviços como localtunnel e forward, destacando lentidão e troca de endereço quando a conexão cai.

## Fichamento

- O texto parte da necessidade de expor serviços locais na internet para integrações com serviços externos.
- Apresenta localtunnel e forward como alternativas para esse tipo de acesso.
- Diz que localtunnel era usado por ser gratuito, mas é lento.
- Observa que pagar por esse tipo de serviço não faz sentido quando o uso é ocasional.
- Aponta que, se a conexão cai, o localtunnel gera um novo endereço ao reconectar.
- Relata que isso atrapalha quando o serviço em teste precisa ser configurado com a URL nova.
- Propõe uma forma simples de fazer isso com SSH e um servidor web.
- Usa um servidor com NGINX como exemplo de configuração.
- Mostra um bloco `upstream` com portas usadas para Rails, Node.js, Rack e Sinatra.
- Explica que o bloco `upstream` define os servidores que o NGINX usa para responder à requisição.
- Indica que, na prática, o NGINX fica configurado como um load balancer.
- Afirma que o servidor responde a qualquer requisição em `*.dev.simplesideias.com.br`.
- Diz que isso é útil para testar apps que usam subdomínios.
- Menciona a criação de um registro `ALIAS` no DNSimple para configurar o DNS.
- Mostra o comando `ssh simplesideias.com.br -R 3000:localhost:3000` para redirecionar a porta local 3000.
- Explica que o comando envia `localhost:3000` para a porta 3000 do servidor remoto.
- Observa que não é necessária permissão especial nesse caso, porque a porta é maior que 1024.
