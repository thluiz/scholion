---
title: "Instalando o PostgreSQL 9.3 no Ubuntu 14.04 LTS"
date: '2016-03-14T18:29:10-03:00'
category: webclip
summary: 'O post mostra como instalar o PostgreSQL no Ubuntu 14.04 LTS com apt-get, alterar a senha do usuário postgres, liberar acesso remoto e criar usuários e databases.'
tags: ["postgresql", "ubuntu", "banco-de-dados"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Instalando o PostgreSQL 9.3 no Ubuntu 14.04 LTS"
    url: "http://localhost:2368/instalando-o-postgresql-9-3-no-ubuntu-14-04-lts/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/localhost--instalando-postgresql-9-3-no-ubuntu-14-04-lts.md"
    kind: repo
---

O post mostra como instalar o PostgreSQL 9.3 no Ubuntu 14.04 LTS com os recursos padrão do sistema, ajustar a senha do usuário postgres, liberar acesso remoto e alterar as permissões de autenticação. Também descreve como criar um novo usuário, vincular um database a ele e conceder privilégios a um desenvolvedor.

## Fichamento

- Verifica a versão do PostgreSQL disponível no Ubuntu com `apt-get update` e `apt-cache show postgresql`.
- Instala o PostgreSQL com `sudo apt-get install postgresql` e observa que o serviço deve iniciar ao fim da instalação.
- Troca para o usuário `postgres`, entra no `psql` e altera a senha com `ALTER USER postgres with PASSWORD ...`.
- Para acesso remoto, orienta alterar `listen_address` em `postgresql.conf` para `'*'` e reiniciar o serviço.
- Em `pg_hba.conf`, manda trocar `peer` por `md5` para exigir usuário e senha do PostgreSQL nas conexões.
- Explica que `peer` permite conexão pelo nome do usuário do Ubuntu quando existe um database com o mesmo nome.
- Mostra como criar um novo usuário com `createuser -d -R -P NOME_DO_USUARIO` e um database ligado a ele com `createdb -O NOME_DO_USUARIO NOME_DO_DATABASE`.
- Para dar acesso a um database já existente, cria o usuário e depois usa `GRANT ALL PRIVILEGES ON DATABASE ... TO ...`.
- Diz que o novo usuário pode acessar pelo terminal com `psql --username=... --password --dbname=...` ou por softwares como PgAdmin e PhpPgAdmin.
