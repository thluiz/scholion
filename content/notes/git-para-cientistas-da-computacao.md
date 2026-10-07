---
title: "Git para Cientistas da Computação"
date: '2015-01-29T06:26:42-03:00'
category: webclip
summary: 'A introdução explica o Git como um DAG de objetos e post-its, mostra blobs, trees, commits, refs, tags e descreve como merge, fast-forward, rebase e garbage collection aparecem nesse modelo.'
tags: ["git", "controle-de-versao", "dag", "git-svn"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Git para Cientistas da Computação | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2008/02/12/git-para-cientistas-da-computa-o#.VMn8A8tqbqA"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/akitaonrails-com--git-para-cientistas-da-computacao.md"
    kind: repo
---

O texto apresenta o Git de forma introdutória, focando em como o repositório funciona por dentro. Ele trata o armazenamento como um DAG de objetos identificados por SHA-1 e explica o papel de blobs, trees, commits, refs, remote refs e tags.

Também compara situações de histórico com clone, fetch, merge, fast-forward e rebase. O autor destaca o git-svn como motivo importante para a adoção do Git, por permitir trabalho em paralelo com Subversion em modo read-write.

## Fichamento

- O artigo é uma introdução ao funcionamento interno do Git, pensada para quem quer entender a arquitetura do repositório.
- O armazenamento do Git é descrito como um DAG de objetos comprimidos e identificados por SHA-1.
- Blob é o objeto mais simples e representa bytes de conteúdo, normalmente um arquivo.
- Tree representa diretórios e aponta para blobs e outras trees.
- Commit aponta para uma tree e para zero ou mais commits pais; dois pais indicam merge, e nenhum pai indica commit inicial.
- Refs, heads e branches são comparadas a post-its que apontam para nós do DAG e podem ser movidos livremente.
- HEAD é uma ref especial que aponta para a ref do branch atualmente ativo.
- Remote refs são atualizadas por git fetch e funcionam como refs controladas pelo servidor remoto.
- Tag aponta para um commit e pode incluir mensagem opcional e assinatura GPG.
- O histórico do Git é mostrado por meio de clone, fetch, merge e fast-forward.
- Um merge sem fast-forward cria um novo commit com dois pais.
- Rebase substitui commits por outros com pai diferente e move o branch para essa nova linha.
- O texto recomenda não rebasear branches sobre os quais outras pessoas já criaram novos commits.
- O autor aponta o git-svn como principal motivo para a adoção do Git, por permitir integração read-write com Subversion.
