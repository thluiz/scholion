---
title: "Tipos de nota do Scholion"
date: '2026-04-23T18:57:32+01:00'
summary: "Referência dos tipos/categorias de nota no Scholion, com ícone, cores (light/dark) e quando usar cada um. Sistema via campo `category` no frontmatter."
toc: true
tags: ["scholion", "meta", "referencia"]
category: note
has_commentary: true
sources: []
---

Tipos são definidos pelo campo `category` no frontmatter. Cada tipo aplica três coisas visualmente: ícone no dateline do card, borda lateral colorida, e badge no topo da página individual.

**Cores são diferentes no light e dark.** No light usamos tons saturados; no dark, pastéis-claros. A CSS está em `assets/css/custom.css`.

## Mapa de categorias

| Tipo | `category:` | Ícone | Cor light | Cor dark | Quando usar |
|---|---|---|---|---|---|
| Podcast | `podcast` | 🎙 | `#db2777` (rosa) | `#f472b6` | Anotações de episódios Vox |
| Citação | `quote` | ❝ | `#0d9488` (teal) | `#2dd4bf` | Citações verificadas de terceiros |
| Comic | `comic` | 🖼 | `#ea580c` (laranja) | `#fb923c` | Tiras/quadrinhos |
| Etimologia | `etymology` | 📜 | `#d97706` (âmbar) | `#fbbf24` | Notas `etimologia-de-*.md` |
| Discípulo | `disciple` | 🙇 | `#7c3aed` (violeta) | `#a78bfa` | Notas `moy-*.md` do Clã Moy Jo Lei Ou |
| Filme | `movie` | 🎦 | `#0284c7` (sky) | `#38bdf8` | Notas sobre filmes |
| Caminhada | `walk` | 🗺 | `#78716c` (pedra) | `#a8a29e` | Notas sobre caminhadas |
| Pesquisa viva | (`.Section == "research"`) | 🔍 | `#6366f1` (índigo) | `#818cf8` | Em andamento (auto-detectado por seção) |
| Pesquisa publicada | `research: published` | 🔍 | `#22c55e` (verde) | — | Pesquisa finalizada |

## Sinal ortogonal: comentário próprio

Campo `has_commentary: true` adiciona o ícone 📝 (âmbar) **apenas quando a nota não tem `category` definida**. Indica que a nota tem comentário original do autor. É independente da categoria — pode coexistir, mas o ícone de categoria tem precedência no card.

## Como aplicar

```yaml
---
title: "Título da nota"
category: movie
tags: ["cinema"]
---
```

Se `category` não casar com nenhum tipo registrado, a nota fica sem ícone/borda (fallback limpo). Adicionar nova categoria exige:
1. CSS em `assets/css/custom.css` (card-type, type-badge, note-- border, cada um com variante `.dark`)
2. Branches nos 4 layouts: `layouts/notes/list.html`, `layouts/notes/single.html`, `layouts/index.html` (2 lugares), `layouts/_default/term.html`

## Paleta — princípio

Light mode usa Tailwind-600 (saturado). Dark mode usa Tailwind-300/400 (pastel claro). A escolha preserva hierarquia visual nos dois fundos sem exigir recálculo de contraste caso a caso.
