---
title: "Helix: editor de terminal modal (alternativa ao vim)"
date: 2026-04-29T11:41:20+01:00
summary: "Editor modal em Rust com LSP, tree-sitter e fuzzy finder embutidos. Zero config. Modelo seleção-primeiro inverte a lógica do vim."
tags: ["helix", "editor", "terminal", "windows"]
has_commentary: true
sources:
  - title: "Helix Editor"
    url: "https://helix-editor.com/"
    kind: other
  - title: "helix-editor/helix"
    url: "https://github.com/helix-editor/helix"
    kind: repo
---

Acesso a Hermes-PT muitas vezes via SSH. Editar arquivo no terminal vira problema: vim funciona perfeito no Linux, mas no Windows (e via SSH para Windows) sempre tive atrito. Clipboard, paths, plugins que não carregam.

Resolvi tentar Helix.

## O que é

Editor modal escrito em Rust. Single binary, sem dependência de Python ou Node. Vem com LSP, tree-sitter, fuzzy finder e file picker embutidos. Zero config para começar.

## Seleção primeiro, ação depois

**O modelo é invertido em relação ao vim.** No vim, `dw` significa "delete word". Verbo primeiro, objeto depois, e o usuário não vê o que vai apagar. No Helix, `wd` é "select word, delete". Objeto primeiro, verbo depois. A seleção fica visível antes da ação.

Em refactor complexo, ver o que está selecionado antes de aplicar a operação muda a sensação de pilotar o editor.

## Multi-cursor nativo

`C` desce o cursor pra próxima linha mantendo seleção. `s` filtra dentro da seleção via regex. Renomear todas as ocorrências dentro de um bloco vira trivial. Sem `:s/.../g`, sem plugin.

## Instalação

```powershell
winget install Helix.Helix
```

Para autocompletar de cmdlets do PowerShell, Helix usa o `powershell-editor-services` como LSP. Detecta automaticamente se estiver no PATH.

## Primeiros passos

```bash
hx --tutor
```

Tutorial embutido. Em ~30 minutos passa toda a lógica nova. Os keybindings parecem vim, mas o modelo de seleção é diferente o bastante para exigir prática.

Atalhos essenciais:

- `i`: modo insert
- `Esc`: volta pro modo normal
- `:w` / `:q` / `:wq`: salvar/sair
- `Space + f`: file picker fuzzy
- `Space + s`: symbol picker (precisa LSP)
- `gd`: go to definition
- `Space + ?`: abre todos os comandos

## Quando não vale

Para quem já tem `.vimrc` configurado com plugins na mão, Helix é regressão. O ecossistema de plugins é praticamente inexistente. A filosofia é "tudo built-in". Para quem apanha de configurar Neovim e só quer abrir um arquivo no terminal com LSP funcionando, vence.
