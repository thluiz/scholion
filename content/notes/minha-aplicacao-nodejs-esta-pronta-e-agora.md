---
title: "Minha aplicação NodeJS está pronta! E agora?"
date: '2017-03-21T17:02:17-03:00'
category: webclip
summary: 'O texto mostra como publicar uma aplicação NodeJS em um servidor Linux usando NGINX como proxy reverso, instalar NodeJS, NPM e Forever, e manter o processo em execução.'
tags: ["nodejs", "nginx", "deploy", "forever"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Minha aplicação NodeJS está pronta! E agora? - Código Simples .NET"
    url: "https://codigosimples.net/2017/03/21/minha-aplicacao-nodejs-esta-pronta-e-agora/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-03/codigosimples-net--minha-aplicacao-nodejs-esta-pronta-e-agora.md"
    kind: repo
---

O texto apresenta um passo a passo para colocar uma aplicação NodeJS no ar fora do ambiente de desenvolvimento. A proposta é usar Linux Ubuntu 16, NGINX, NodeJS, NPM e Forever para disponibilizar o site no servidor, com NGINX cuidando do acesso externo e do conteúdo estático, enquanto a aplicação roda em localhost.

Depois de instalar e testar o NGINX, o autor mostra como configurar o bloco server, definir server_name, proxy_pass para a porta 8000 e o diretório de arquivos estáticos. Em seguida, instrui a instalar NodeJS, NPM e Forever, usar o Forever para iniciar a aplicação, ver os logs, listar processos e executar restart e stop.

## Fichamento

- O texto se concentra no deploy de aplicações NodeJS em um servidor web, não na arquitetura ou no desenvolvimento da aplicação.
- A configuração usa Linux Ubuntu 16, NGINX, NodeJS e Forever.
- O NGINX é apresentado como servidor web e proxy reverso, com boa escalabilidade e configuração simples para trabalhar com NodeJS.
- A configuração sugerida define um server que escuta na porta 80, aponta o host com server_name e encaminha as requisições para http://127.0.0.1:8000.
- O conteúdo estático da aplicação fica em uma pasta separada, usada para CSS, JavaScript e imagens.
- O texto orienta testar a configuração com nginx -t e reiniciar o serviço depois da alteração.
- NodeJS é instalado pelo repositório da NodeSource, e o NPM é instalado separadamente para permitir a instalação do Forever.
- Forever é descrito como uma ferramenta para executar scripts continuamente e disponível globalmente com npm install forever -g.
- Os comandos destacados para uso do Forever são start, list, restart e stop.
- O texto diz que o Forever grava logs da aplicação e reinicia automaticamente o processo quando ocorre uma exceção não tratada.
- Na conclusão, o autor afirma que a mesma lógica do Forever pode servir também para outros tipos de scripts que precisem rodar continuamente.
