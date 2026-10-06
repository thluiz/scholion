---
title: "Dica Git da semana: Gollum"
date: '2012-04-20T13:13:16-03:00'
category: webclip
summary: 'Gollum é um servidor de wiki baseado em Git que permite editar páginas localmente, registrar cada mudança como commit e trabalhar offline até voltar a conectar.'
tags: ["gollum", "git", "wiki"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dica Git da semana: Gollum"
    url: "https://imasters.com.br/desenvolvimento/dica-git-da-semana-gollum"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/imasters-com-br--dica-git-da-semana-gollum.md"
    kind: repo
---

Gollum é apresentado como um servidor de wiki ligado a um repositório Git local. Ele permite ver, editar e salvar documentos, e cada gravação vira um commit individual.

## Fichamento

- É um servidor de wiki em Ruby criado pelo GitHub.
- Cada escrita corresponde a um commit no repositório Git.
- O campo de mensagem de mudança vira a mensagem do commit.
- As páginas do wiki mapeiam para arquivos no diretório configurado ou na raiz do repositório.
- Markdown é o formato padrão para novas páginas, e outros formatos wiki podem ser suportados com parsers separados.
- A instalação é mostrada com `gem install gollum`, seguida da criação do repositório e da inicialização do servidor local.
- O texto diz que ele pode ser usado para editar um wiki sem conexão e incorporar as mudanças depois de reconectar.
- Ele usa as credenciais de commit do usuário local, mas não passa a identidade do committer a partir dos commits nem por `GIT_AUTHOR_EMAIL` e `GIT_COMMITTER_EMAIL`.
- O texto diz que isso limita o uso em equipes, mas funciona bem para um wiki local de um único usuário.
