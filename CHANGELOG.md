# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/),
e o projeto segue [Semantic Versioning](https://semver.org/) quando aplicável.

## [0.2.0] — 2026-04-09

### Adicionado

- **Deploy CI**: workflow Azure Static Web Apps + pre-build com `peaceiris/actions-hugo`
  para contornar incompatibilidade glibc do Oryx.
- **OG images por nota** geradas em build time; usa Noto Sans SC para renderizar glifos CJK.
- **Home como vitrine curada**: home exibe notas fixadas (`pinned`), `/notes/` continua
  como índice completo. Cards fixados com colapso "ver mais" (mostra 3, esconde o resto)
  e ordenação por `pin_weight`.
- **Paginação** na home e em `/notes/`, com fundo mais suave.
- **Navegação prev/next** no rodapé da nota single, com link "voltar".
- **Busca via `Ctrl+K`** (além de `/`), com hint visual no teclado.
- **Página `/fontes/`**: índice de todas as fontes referenciadas, com dedup por URL
  sem fragmento.
- **Co-tags nas páginas de tag**: mostra tags relacionadas em cada `/tags/<slug>/`.
- **Nota single em card** estilo papel, com tipografia respirada.
- **Tag cloud e tag pages** com o mesmo mosaico da home e `/notes/`.
- **Links inline** diferenciados dentro do corpo da nota.
- **Tag chips dentro dos cards** de nota na listagem.
- **Cards em dark theme** com superfície mais clara para separação.
- **Subtítulo de cross-reference** com o silvae na home.
- **Data de última atualização** ao lado da contagem de notas.
- **Nota "O que é um Scholion (e o que é Marginalia)"** explicando o projeto.

### Melhorado

- **Grid responsivo**: `ResizeObserver` substitui media queries para detectar colunas
  reais; 4 colunas a partir de 1024px, 5 a partir de 1800px.
- **Cards sem aspect-ratio fixo**: altura responsiva ao conteúdo.
- **Visibilidade inteligente dos pinned cards**: esconde cards que não cabem no grid.
- **Limiar de notas relacionadas** elevado para que sobreposição de tags importe.
- **Indicador de nota fixada**: experimentou chip "fixada", reverteu para glifo ★ limpo.

### Acessibilidade

- Focus rings, `prefers-reduced-motion`, contraste em summaries, título em `/notes/`.

### Corrigido

- Header seal ficava vermelho no hover apenas sobre o ícone — agora em todo o menu.
- URLs relativas `.md` em sources agora reescritas para rotas do scholion.
- Parágrafos e listas dentro do corpo da nota tinham espaçamento insuficiente.
- Aspas no título da nota sobre Elena Verna.
- Citação duplicada na nota Elena Verna; intro movida para primeiro lugar.

### Removido

- Filtros (chips "Todas / Com comentário / Glosas") removidos da listagem `/notes/`.
- Nota "Confessions of a Millennial in Tech" de Elena Verna movida para o silvae.

## [0.1.0] — 2026-04-09

Primeira versão funcional do Scholion. Migração completa das notas curtas do silvae.

### Adicionado

- **Scaffold Hugo + Blowfish v2.101.0**, instalado como git submodule fixado na tag.
- **Schema novo de nota** em `content/notes/<slug>.md`:
  - `date` (ISO 8601 com offset)
  - `summary` (frase curta para os cards)
  - `tags` (array, kebab-case)
  - `has_commentary` (boolean: notas com análise própria vs glosas puras)
  - `sources` (array estruturado: `title`, `author`, `year`, `publisher`, `url`, `kind`)
- **Color scheme `scholion`** (paleta âmbar/sépia/stone) em `assets/css/schemes/scholion.css`.
- **Mosaico Layout A** em `layouts/notes/list.html` e `layouts/index.html`:
  - Grid CSS responsivo (`auto-fill`, `minmax(220px, 1fr)`), cards quadrados (`aspect-ratio: 1/1`)
  - Cada card mostra título, summary, tags, data
  - Notas com `has_commentary: true` recebem borda lateral âmbar e indicador no canto
  - Filtros "Todas / Com comentário / Glosas" em `/notes/` (removidos da home)
- **Página single** (`layouts/notes/single.html`) com tipografia legível (max-width 42rem,
  line-height 1.75), bloco de "Fontes" renderizado a partir do array estruturado.
- **Tags clicáveis** na single page, linkando para `/tags/<slug>/`.
- **Página de tags** (`layouts/_default/terms.html`) ordenada por contagem decrescente,
  estilo de chip bordado inspirado no Vox.
- **Header** com seal/carimbo do silvae como logo (grayscale, colorido no hover).
- **Favicon** com o ideograma Chi (智), mesma identidade visual do silvae.
- **Tipografia dos headers** no corpo da nota: h2 com border-bottom, h3 em âmbar (cor
  primária), h4 como rótulo uppercase.
- **165 notas migradas do silvae**, cada uma como commit individual com a data de
  publicação original preservada via `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE`.
- **`README.md`** explicando o projeto e as decisões de design.
- **`CHANGELOG.md`** (este arquivo).

### Decisões arquiteturais

- **Hugo em vez de Astro**: build sub-segundo mesmo com 1.000+ notas.
  Astro processava cada nota como componente, ficando lento na casa dos
  segundos com 165 notas.
- **Blowfish como base, não tema custom**: tema ativo, mantido,
  escolha que economiza dezenas de horas de plumbing visual.
- **Submodule em vez de Hugo Modules**: evita dependência de Go.
  `git submodule update --remote` resolve update; pin em tag mitiga
  risco de breaking changes.
- **Patches via lookup order do Hugo**: nenhum arquivo do tema é editado.
  Updates do Blowfish ficam triviais.

### Removido

- **`thluiz/scholion` antigo**: o repositório de mesmo nome (um experimento
  de chat com UI insatisfatória) foi renomeado para
  [`thluiz/scholion-chat`](https://github.com/thluiz/scholion-chat) e
  arquivado. A URL `thluiz/scholion` agora pertence a este projeto.

### Conhecido

- Notas em silvae (`E:/silva/src/content/note/`) ainda existem para não
  quebrar referências externas, mas estão **congeladas**: novas notas
  vão direto para scholion. Migração completa (remoção do silvae) será
  feita quando o scholion estabilizar.
- 16 notas têm `sources: []` por design (referências não verificadas no
  silvae original ou notas explicitamente sem fonte primária).
