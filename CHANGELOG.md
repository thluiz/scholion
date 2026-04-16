# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/),
e o projeto segue [Semantic Versioning](https://semver.org/) quando aplicável.

## [0.5.0] — 2026-04-16

### Alterado

- **Deploy migrado para AWS S3 + CloudFront** (us-east-1). GitHub Actions builda
  Hugo, sync S3 com cache diferenciado (HTML 1h, assets 1y immutable) e invalida
  a distribution. Substitui Azure Static Web Apps.
- **Hook de git history migrado para pre-push**. O pre-commit antigo falhava no
  primeiro commit de uma nota — `git log --follow` retornava vazio para ficheiro
  apenas staged e nenhum JSON era escrito. O pre-push roda `gen_git_history.py
  --all` antes do envio; se houver diff, cria `chore: update git history` que
  sobe no push seguinte.
- **Mensagem de histórico ausente** passou a indicar que o JSON chega no próximo
  deploy, em vez de apontar para docs de configuração.

### Melhorado

- **`gen_git_history.py` idempotente**: só escreve o JSON quando o conteúdo
  diverge do existente. Escrita incondicional bumpava mtime em 310 ficheiros a
  cada pre-push e forçava o `hugo server` a re-renderizar tudo.

## [0.4.0] — 2026-04-15

### Adicionado

- **Sistema de tipos visuais** (`category` no frontmatter): notas ganham ícone e cor
  por tipo na dateline do card e badge na página individual.
  - `podcast` (🎙 rosa `#db2777`) — 119 notas de anotações de episódios Vox.
  - `quote` (❝ teal `#0d9488`) — 15 notas de citações verificadas.
  - `has_commentary` (📝 âmbar) — notas com comentário original do autor.
- **Skill `add-scholion-quote`**: cria nota de citação verificada. Pesquisa autoria
  em Quote Investigator, Wikiquote e busca geral. Tags de autor obrigatórias.
- **Badges de tipo na single page**: 🎙 Podcast e ❝ Citação no header, mesmo
  padrão do 🔍 Pesquisa Viva.
- **Cores dark mode** para todos os tipos (quote, podcast, research, publicada).
- **Suporte a page bundles** no git history e links GitHub (`dir/index.md`).
- **Imagens centralizadas** no corpo das notas (`scholion-note-body img`).

### Melhorado

- **Ícones de tipo na dateline**: movidos do canto superior direito para a mesma
  linha da data, evitando sobreposição com títulos longos.
- **Logo colorido em mobile/tablet** (até 1024px) — sem hover em touch, fica
  sempre visível.
- **Cards pinned**: padding-top no body para não colar no ★.

### Corrigido

- **`type` renomeado para `category`**: `type` é palavra reservada do Hugo e
  causava uso de layout errado (ex: `layouts/podcast/single.html` em vez de
  `layouts/notes/single.html`). Renomeado em 134 notas, 4 templates e 2 skills.
- **Border-left do commentary removida** — confundia visualmente com podcast no
  light mode.
- **`has_commentary` corrigido** em 23 notas de Chinês Instrumental (eram `false`,
  agora `true`) e em Jevons Paradox.
- **Tags de autor adicionadas** a 12 notas de citação existentes.
- **Travessões dramáticos** removidos da nota "O que é um Scholion".

## [0.3.0] — 2026-04-11

### Adicionado

- **Pesquisa Viva**: novo tipo de conteúdo em `content/research/` para pesquisas
  de longa duração com fontes verificadas, texto em andamento e notas extraídas.
- **Layout single para pesquisas** (`layouts/research/single.html`): caixa estilo
  nota com borda azul, badge "🔍 Pesquisa Viva" e status.
- **Cards de pesquisa no grid**: pesquisas aparecem junto com notas na home e em
  `/notes/`, com borda azul e ícone de lupa para diferenciação.
- **TOC sidebar**: notas e pesquisas com `toc: true` no frontmatter ganham
  índice sticky à direita (h2/h3), colapsado no topo em mobile.

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
