---
title: "[Heroku Tips] Enciclopédia do Heroku"
date: '2012-04-20T18:27:47-03:00'
category: webclip
summary: 'O post reúne dicas práticas de configuração do Heroku para apps Rails, cobrindo dynos, concorrência, versão do Ruby, jobs em background, uploads no S3, assets, New Relic e domínios.'
tags: ["heroku", "rails", "amazon-s3", "tarefas-em-background"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[Heroku Tips] Enciclopédia do Heroku"
    url: "http://www.akitaonrails.com/2012/04/20/heroku-tips-enciclopedia-do-heroku"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/akitaonrails-com--heroku-tips-enciclopedia-do-heroku.md"
    kind: repo
---

O post explica como usar o Heroku para publicar aplicações Rails com rapidez. Ele descreve os dynos como máquinas virtuais voláteis, mostra os limites de uma configuração gratuita com um único dyno e lembra que tutoriais antigos precisam ser conferidos pela stack usada.

## Fichamento

- Heroku é apresentado como um PaaS sobre o Amazon EC2 que automatiza a criação de uma máquina virtual volátil e prepara o ambiente para Ruby.
- Um dyno é descrito como uma máquina virtual pequena, com 4 cores, até 512 MB de RAM, sem swap file e sem persistência de arquivos, por isso uploads devem ir para o Amazon S3.
- A configuração gratuita com um único dyno e PostgreSQL compartilhado serve para testes, mas não basta para uma aplicação séria em produção.
- Para Ruby e Rails, o texto aponta a stack Cedar e recomenda verificar qual stack um tutorial usa antes de segui-lo.
- Thin aparece como a recomendação padrão, mas Passenger é sugerido quando a ideia é rodar mais de um processo Ruby e atender mais requisições ao mesmo tempo.
- O exemplo troca thin por passenger no Gemfile e usa o Procfile para subir o Passenger com max-pool-size.
- O texto diz que o ideal é entre 3 e 4 processos, dependendo de a dyno ser 1X ou 2X, e que o uso de memória precisa ficar abaixo de 512 MB.
- Git é obrigatório, e o deploy é feito por um remote do Heroku, com git push heroku master acionando bundle install e a pré-compilação de assets.
- O post recomenda fixar Ruby 1.9.3 ou 2.0.0 adicionando a versão no Gemfile.
- Tarefas pesadas, como relatórios, emails e chamadas a APIs externas, devem rodar em background com Resque e Redis.
- O texto mostra como adicionar o add-on de Redis, configurar as gems e tasks do Resque, definir REDISTOGO_URL nos ambientes de desenvolvimento e teste e criar entradas web, scheduler e worker no Procfile.
- Ele explica que os workers do Resque fazem fork, então as conexões com o banco precisam ser refeitas depois do fork.
- O scheduler pode criar tarefas duplicadas se uma execução durar mais do que o intervalo de agendamento, e resque-lock é sugerido para jobs que não podem rodar em paralelo.
- Para escalar workers, o post usa o exemplo web=4, scheduler=1 e worker=2, e estima as conexões simultâneas necessárias para Redis e PostgreSQL.
- Assets estáticos devem ser servidos por Amazon S3 ou por uma CDN, com buckets criados na AWS, policies corretas e variáveis de configuração para credenciais e FOG.
- O artigo diz que o asset pipeline deve usar helpers em vez de URLs fixas, para manter o desenvolvimento local e apontar a produção para o S3.
- asset_sync é configurado para enviar os assets compilados para o S3, com opções de gzip, região, manifest e falha silenciosa.
- Para uploads de usuários, o texto mostra CarrierWave usando fog e um bucket separado no S3, e lembra que os dynos do Heroku não preservam arquivos locais.
- New Relic precisa de um reconnect after_fork quando o Unicorn faz fork.
- As notas finais recomendam múltiplos dynos web em produção, upgrade de Redis e PostgreSQL conforme a necessidade e configuração de domínios customizados no Heroku.
- O post encerra dizendo que o Heroku pode sair mais barato do que contratar um sysadmin sênior e montar a própria infraestrutura do zero.
