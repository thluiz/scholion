---
title: "Micro Tutorial de Git"
date: '2015-01-30T11:13:31-03:00'
category: webclip
summary: 'O tutorial mostra como clonar um repositório Git, trabalhar em branches locais, fazer commits, mesclar correções, rebasing, usar stash, enviar mudanças e limpar branches e commits.'
tags: ["git", "branches", "merge", "rebase"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Micro Tutorial de Git | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2008/4/3/micro-tutorial-de-git#.VMuQ7WjF_oE"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/akitaonrails-com--micro-tutorial-de-git.md"
    kind: repo
---

O texto apresenta um fluxo prático de uso do Git com clone de repositório, branches separados para trabalho e correções rápidas, e histórico local que pode ser mesclado, rebaseado, guardado no stash, enviado ao remoto ou descartado com reset. Também mostra como o Git lida com renomeio de arquivos e reconcilia mudanças entre branches.

## Fichamento

- Clonar um projeto do Github traz o repositório completo e todo o histórico desde o primeiro commit.
- Criar um branch de trabalho com `git checkout -b` separa as alterações do `master`.
- `git status` mostra arquivos modificados, apagados e novos.
- `git add` inclui arquivos no que será commitado, inclusive no modo interativo.
- `git commit` registra as mudanças; `-a` inclui arquivos já rastreados e `-m` define a mensagem.
- Para uma correção rápida, o texto cria um branch próprio a partir do `master`.
- `git merge` traz a correção de volta ao `master`, e o branch temporário pode ser apagado depois.
- `git stash` guarda mudanças ainda não commitadas para retomá-las mais tarde com `git stash apply`.
- `git rebase master` reposiciona o branch de trabalho sobre o `master` atualizado.
- `git branch -m` renomeia um branch para reutilizá-lo em outro projeto clonado.
- `git push` envia as alterações do branch local para o repositório remoto, quando há permissão de escrita.
- `git branch -d` apaga um branch; `-D` força a exclusão quando o branch não é subtipo estrito do HEAD atual.
- `git reset --hard` volta o diretório ao estado de um commit anterior ou ao último commit feito.
- O Git reconhece renomeio de arquivo e consegue mesclar mudanças sobre o arquivo renomeado em outro branch.
