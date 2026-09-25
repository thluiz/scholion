---
title: "Why Use git switch Instead of git checkout?"
date: '2026-09-25T01:03:39+01:00'
category: webclip
summary: 'Explains that `git switch`, introduced in Git 2.23, focuses on branch switching and creation, while `git checkout` mixes branch and file operations and can be more confusing.'
tags: ["git", "git-switch", "git-checkout"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Use git switch Instead of git checkout?"
    url: "https://dev.to/softheartengineer/why-use-git-switch-instead-of-git-checkout-3ojb?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--why-use-git-switch-instead-of-git-checkout.md"
    kind: repo
---

`git switch` is presented as a newer command in Git 2.23 that makes branch changes more direct and easier to understand. The page contrasts it with `git checkout`, which can also handle file operations, and says that separation reduces mistakes when working across branches.

The article also shows common uses such as switching to an existing branch, creating a new one with `-c`, moving to a commit in detached HEAD with `--detach`, and forcing or discarding changes when local modifications block the switch. It closes by recommending thoughtful branch changes, `git stash`, descriptive branch names, and keeping Git updated.

## Fichamento

- `git switch` foi introduzido no Git 2.23 para trocar de branch de forma mais simples e focada.
- `git checkout` acumula troca de branch, operação em arquivos e criação de branch, o que pode gerar confusão.
- A separação de responsabilidades em `git switch` torna o fluxo mais intuitivo e reduz erros na gestão de branches.
- A sintaxe básica é `git switch [options] <branch>`.
- `-c <branch>` cria uma nova branch e já muda para ela.
- `--detach` leva para um commit específico sem associar a navegação a uma branch.
- `-f` força a troca e descarta mudanças não commitadas.
- `--discard-changes` também descarta modificações locais ao trocar de branch.
- Ao usar `git switch` em uma branch existente, as mudanças não commitadas são preservadas se não entrarem em conflito.
- Um fluxo prático descrito usa `git stash`, `git switch main`, correção do bug e depois retorno para `feature-branch` com `git stash pop`.
- A comparação final destaca que `git switch` cobre troca de branch, criação de branch e detached HEAD, mas não operações em arquivos.
- Os problemas comuns citados são mudanças locais que impedem a troca e branch inexistente.
- As boas práticas listadas são conferir a branch antes de alterar algo, combinar com `git stash`, usar nomes descritivos e manter o Git atualizado.
