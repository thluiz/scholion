# Scholion

> σχόλιον — *gloss marginal em manuscrito antigo*

Site estático de marginalia, glosas e fragmentos do que leio, escuto e assisto. Cada nota é um cartão num mosaico, com fontes estruturadas e (opcionalmente) o meu comentário em cima.

🌐 [scholion.thluiz.com](https://scholion.thluiz.com)

## Por que esse projeto existe

As notas curtas viviam em [`thluiz/silva`](https://github.com/thluiz/silva) (Astro). Quando passaram de 150, três problemas começaram a aparecer:

1. **Build lento**. Cada nota era processada como componente Astro. A 165 notas o `astro build` já estava na casa dos segundos, e a perspectiva de chegar a 1.000 era desencorajadora — eu me peguei *evitando capturar notas* para não pagar o custo de publicação.
2. **Fontes em texto livre**. As referências viviam no rodapé do markdown, sem estrutura. Reagrupar por autor, fonte ou tipo era impraticável.
3. **UI feita para textos longos**. O silvae é um blog. Mosaico de cartões, filtros por tipo, busca rápida — nada disso fazia sentido lá.

Scholion nasceu como um spin-off otimizado para o caso "marginalia ao estilo cartões": **escala**, **busca**, **publicação rápida**.

## Decisões de design

### Hugo, não Astro

Hugo compila 300+ markdowns em ~60 ms. A 1.000 notas continua sub-segundo. Para um site que é 95% renderização de markdown estático, é a ferramenta certa — o JS-runtime do Astro não traz benefício neste caso.

### Blowfish como base, customizado por patches

[Blowfish](https://blowfish.page) é um tema Hugo ativo (release a cada ~2 semanas, mantenedor responde rápido a deprecations do Hugo). Usado como **submodule**, com **zero edição dos arquivos do tema**:

- `assets/css/custom.css` — overrides de estilo (carregado depois dos estilos do tema)
- `assets/css/schemes/scholion.css` — color scheme próprio (paleta âmbar/sépia/stone)
- `layouts/notes/`, `layouts/fontes/`, `layouts/research/` — templates próprios por section via Hugo lookup order
- `layouts/partials/` — partials sobrescritos (head, footer, paginação)

Updates do Blowfish: `git submodule update --remote themes/blowfish` + bump pra próxima tag testada. Os overrides são poucos e auditáveis, então o risco de quebra em update é baixo.

### Layout em mosaico (Layout A)

Cards quadrados (1:1, `grid-template-columns: repeat(auto-fill, minmax(220px, 1fr))`) optimizados para *scanning* rápido. Cada card mostra título, summary curto, tags e data. Notas com comentário do autor recebem uma borda lateral âmbar e um indicador no canto — diferenciação visual sem ocupar espaço extra.

A página da nota individual abre com tipografia legível (max-width 42rem, line-height 1.75), e as fontes são renderizadas a partir do array estruturado em frontmatter — não do corpo do markdown.

### Schema das notas

```yaml
---
title: "Título"
date: 2026-04-09T17:30:00+01:00
category: quote                 # opcional — aciona layout/ícone específico (quote, podcast, etc.)
summary: "Frase curta usada nos cards."
tags: [tag-1, tag-2]
has_commentary: true            # true se contém análise do autor; false para citação/glosa pura
sources:
  - title: "Título da fonte"
    author: "Autor"             # opcional
    year: 2024                  # opcional
    publisher: "Editora"        # opcional
    url: "https://..."          # opcional
    kind: book | article | wiki | podcast | video | paper | poem | repo | film | other
---

Corpo em markdown.
```

`has_commentary` é a separação que importa: notas que são apenas excerto/citação de uma fonte (glosa) versus notas onde adicionei análise, conexão ou síntese própria (commentary). Os filtros em `/notes/` permitem ver só um ou só outro.

`category` diferencia tipos visuais de nota: `quote` (citações com estilo itálico e aspas decorativas), `podcast` (anotações de episódios), entre outros. Cada tipo tem cor, ícone e badge próprios nos cards.

`sources` como array estruturado destrava agrupamento por autor, por tipo de fonte, por publisher — coisas impossíveis no formato antigo de "fonte como texto livre no rodapé".

## Stack

- **[Hugo](https://gohugo.io)** v0.148+ extended — gerador estático
- **[Blowfish](https://blowfish.page)** — tema base (Tailwind, dark/light, busca client-side)
- **CSS Grid** puro para o mosaico (sem framework JS)
- **Git submodule** para o tema (não Hugo Modules — evita dependência de Go)

## Estrutura do repositório

```
scholion/
├── archetypes/          # template para nota nova (hugo new notes/foo.md)
├── assets/
│   ├── css/
│   │   ├── custom.css           # overrides + layout do mosaico/single
│   │   └── schemes/scholion.css # color scheme âmbar
│   └── img/seal.png
├── config/_default/     # hugo.toml, params.toml, markup.toml, languages, menus
├── content/notes/       # 300+ notas em markdown
├── data/git_history/    # JSONs com histórico por nota (gerados)
├── layouts/             # templates próprios (override do Blowfish)
│   ├── _default/term.html, terms.html
│   ├── fontes/list.html
│   ├── index.html
│   ├── notes/list.html
│   ├── notes/single.html
│   ├── research/single.html
│   └── partials/        # extend-head-uncached, favicons, footer, scholion-pagination
├── scripts/             # gen_git_history.py, pre-commit hook
├── static/              # favicon.png
└── themes/blowfish/     # submodule
```

## Desenvolvimento local

```bash
# clone com submodule
git clone --recurse-submodules https://github.com/thluiz/scholion.git
cd scholion

# servidor com hot reload
hugo server
# → http://localhost:1313
```

## Criar uma nota nova

Idealmente via skill `add-scholion-note` (Claude Code), que cuida do schema, slug, hora real do sistema, inferência de tags e detecção de `kind` da fonte por domínio.

Manualmente:

```bash
hugo new notes/<slug>.md
# editar o frontmatter e o corpo
hugo server  # ver no browser
git add content/notes/<slug>.md
git commit -m "feat: <título>"
git push
```

## Histórico de alterações nas notas

Cada nota exibe as 3 últimas alterações (data + mensagem de commit) e um link para o histórico completo no GitHub.

Os dados vêm de arquivos JSON em `data/git_history/`, gerados por `scripts/gen_git_history.py`.

### Bootstrap (primeira vez)

```bash
python scripts/gen_git_history.py --all
```

### Atualização automática via hook

Copie o hook pre-commit para que os JSONs sejam atualizados a cada commit:

```bash
cp scripts/pre-commit .git/hooks/pre-commit
```

O hook detecta notas staged, atualiza só os JSONs correspondentes e faz `git add` deles automaticamente.

## Deploy

**AWS S3 + CloudFront** (us-east-1). Push para `main` dispara build Hugo + sync S3 + invalidação CloudFront via GitHub Actions (`.github/workflows/deploy.yml`).

## Histórico

Ver [CHANGELOG.md](./CHANGELOG.md).

## Licença

[MIT](./LICENSE) — código e estrutura. O conteúdo das notas é direito autoral do autor (Thiago Luiz Silva).
