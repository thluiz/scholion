---
title: "Criando aplicativos Rails multi-tenant com PostgreSQL schemas"
date: '2013-01-15T17:25:28-03:00'
category: webclip
summary: 'O texto explica como usar schemas do PostgreSQL para separar dados por tenant em Rails, definindo search_path por subdomínio, criando schemas novos e ajustando migrações e tabelas compartilhadas.'
tags: ["rails", "postgresql", "multi-tenant", "schemas"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Criando aplicativos Rails multi-tenant com PostgreSQL schemas"
    url: "http://imasters.com.br/banco-de-dados/postgresql/criando-aplicativos-rails-multi-tenantrails-com-postgresql-schemas/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/imasters-com-br--criando-aplicativos-rails-multi-tenant-com-postgresql-schema.md"
    kind: repo
---

O texto apresenta uma forma de construir aplicativos Rails multi-tenant usando schemas do PostgreSQL. A ideia central é definir o schema correto a cada requisição, com base no subdomínio, para que as consultas acessem automaticamente as tabelas do tenant correspondente. O artigo também mostra como criar schemas novos, carregar as tabelas de cada tenant e adaptar migrações para esse modelo.

## Fichamento

- O artigo compara três estratégias para multi-tenancy em Rails e indica o uso de schemas do PostgreSQL quando os dados de cada tenant precisam ficar privados, as consultas cruzadas são pouco necessárias e a quantidade de tenants torna a administração pesada.
- Schemas no PostgreSQL funcionam como namespaces para tabelas; quando o search_path é ajustado, uma consulta como `SELECT count(*) FROM users;` passa a procurar a tabela no schema prioritário antes de usar o schema público.
- A implementação sugerida usa um `before_filter` no `ApplicationController` para localizar o tenant pelo subdomínio e chamar `PgTools.set_search_path` com o id do tenant, ou restaurar o caminho padrão quando não houver correspondência.
- Ao criar um tenant, o código gera um schema próprio, carrega `db/schema.rb` nesse schema e faz isso sem incluir o schema público quando a intenção é preencher apenas as tabelas privadas do tenant.
- Como cada tenant passa a ter suas próprias tabelas, o artigo propõe uma task de Rake que percorre todos os tenants, ajusta o search_path de cada um e executa as migrações em cada schema privado.
- O deploy também precisa acionar essa tarefa extra, além de `rake db:migrate`, para que as alterações de banco cheguem aos schemas de todos os tenants.
- Nem todas as tabelas são privadas. O texto cita `tenants` e possíveis tabelas de login compartilhado como exemplos de tabelas que precisam continuar acessíveis a partir do schema público.
- Para lidar com tabelas compartilhadas, o artigo sugere manter uma lista de tabelas comuns e removê-las dos schemas privados depois de carregar as estruturas, para evitar conflitos com versões privadas dessas mesmas tabelas.
- Migrações que alteram tabelas compartilhadas devem interromper a execução quando o search_path atual for privado, usando um método como `private_search_path?` para evitar mudanças indevidas durante as migrações dos tenants.
