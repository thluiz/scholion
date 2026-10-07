---
title: "O Guia Definitivo do deploy Rails App no Amazon EC2 em 15 passos"
date: '2015-01-30T12:21:54-03:00'
category: webclip
summary: 'Guia passo a passo para subir uma aplicação Rails na Amazon Linux AMI em EC2, com instalação de dependências, Redis, banco, Passenger, Nginx, ajuste de SSH e deploy via Capistrano.'
tags: ["rails", "amazon-ec2", "deploy", "capistrano"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "O Guia Definitivo do deploy Rails App no Amazon EC2 em 15 passos"
    url: "http://lucianosousa.net/2015/01/30/guia-definitivo-rails-amazon.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/lucianosousa-net--guia-definitivo-deploy-rails-app-amazon-ec2-15-passos.md"
    kind: repo
---

O texto reúne um roteiro para preparar uma instância EC2 para uma aplicação Rails. Ele cobre atualização do servidor, instalação de dependências do Ruby, banco de dados, RVM, Ruby, Node.js, Redis, SSH para deploy, Capistrano, Passenger, Nginx, memcached e liberação da porta 80 no security group.

## Fichamento

- O guia foi pensado como lembrete pessoal e também para ajudar outras pessoas a subir aplicações Rails em uma VPS.
- Os passos foram feitos para Amazon Linux AMI, baseada em CentOS, com possibilidade de reaproveitar a maior parte do processo em outras distribuições parecidas.
- O servidor deve ser atualizado antes das demais instalações.
- O guia lista pacotes de compilação e bibliotecas necessárias para Ruby e para a aplicação.
- O autor mostra instalação de PostgreSQL, e também cita MySQL como alternativa.
- O RVM é instalado junto com Ruby 2.2.0, e o cache global do RVM é ativado para evitar reinstalar gems iguais ao trocar de versão.
- O Node.js é compilado a partir do código-fonte e instalado manualmente.
- O kernel recebe a configuração `vm.overcommit_memory = 1` para evitar erro de memória no Redis.
- O Redis é compilado, testado e configurado como serviço do CentOS.
- O SSH é ajustado para permitir agent forwarding no deploy.
- O Capistrano recebe configuração de aplicação, repositório, diretório de deploy, arquivos vinculados e diretórios persistentes.
- A tarefa de deploy inclui restart da aplicação tocando `tmp/restart.txt`.
- O deploy é testado com `bundle exec cap *ENV* deploy:check`.
- No PostgreSQL, o banco e o usuário são criados, o método de autenticação é alterado para `md5` e o serviço é reiniciado.
- No MySQL, o serviço é iniciado, a senha do root é definida e um usuário novo é criado.
- O Passenger e o Nginx são instalados, o Nginx recebe configuração com `passenger_nodejs` e `passenger_default_user`, e o serviço é habilitado.
- O security group da Amazon deve aceitar tráfego na porta 80.
- O memcached é iniciado antes do deploy final com Capistrano.
- O texto termina com a indicação de que ainda faltaria automatizar cron para os serviços em um próximo post.
