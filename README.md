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

Na migração, Hugo compilava as 300+ notas em ~60 ms. Hoje, com ~6.000 notas e processamento de imagens, o build completo leva ~80 s (medido na 0.5.14, depois de tirar o trabalho repetido por página dos templates). Para um site que é 95% renderização de markdown estático, segue sendo a ferramenta certa — o JS-runtime do Astro não traz benefício neste caso.

### Blowfish como base, customizado por patches

[Blowfish](https://blowfish.page) é um tema Hugo ativo (release a cada ~2 semanas, mantenedor responde rápido a deprecations do Hugo). Usado como **submodule**, com **zero edição dos arquivos do tema**:

- `assets/css/custom.css` — overrides de estilo (carregado depois dos estilos do tema)
- `assets/css/schemes/scholion.css` — color scheme próprio (paleta âmbar/sépia/stone)
- `layouts/notes/`, `layouts/sources/`, `layouts/quotes/`, `layouts/research/`, `layouts/places/`, `layouts/slides/` — templates próprios por section via Hugo lookup order
- `layouts/_default/baseof.html` — override fino do base, só para servir cabeçalho e busca via `partialCached`
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
rating: 3                       # opcional — escala "Nota", 0 a 5 (ver data/scales.yaml)
morbius: 4                      # opcional — escala "Morbius", 0 a 5
laughs: 5                       # opcional — escala "Gargalhadas", 0 a 5
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

As **escalas de 0 a 5** vivem em `data/scales.yaml`, uma lista de `key`/`label`/`emoji`. Hoje são três: `rating` ("Nota", 🎫), `morbius` ("Morbius", 🧛) e `laughs` ("Gargalhadas", 🤣, para comédias). Cada uma renderiza cinco ícones, com os não-atingidos esmaecidos, na página da nota e nos cards. Todas são opcionais e independentes — uma nota pode ter as três, uma só, ou nenhuma.

A lista é ordenada porque a ordem do YAML é a ordem de exibição; mapa em Hugo itera por ordem alfabética da chave. Para criar uma escala nova, basta uma entrada no YAML: o partial `scholion-scales.html` varre o registro e nenhum template muda.

Na página da nota as escalas saem num grid de duas colunas (rótulo | ícones), com cada escala ocupando uma linha via `grid-template-columns: subgrid`. A coluna do rótulo se dimensiona pelo rótulo mais largo, então os ícones ficam alinhados entre escalas sem nenhuma largura fixa para ajustar quando entrar uma escala nova. Nos cards a variante é inline e sem rótulo — o ícone e o `title` identificam a escala.

A checagem no template usa `isset` e não `with`, porque `0` é um valor válido da escala e `with` o trataria como ausente.

`sources` como array estruturado destrava agrupamento por autor, por tipo de fonte, por publisher — coisas impossíveis no formato antigo de "fonte como texto livre no rodapé".

### Páginas de livro nas tags

Uma tag pode representar um livro (ex.: as citações importadas do Kindle). Basta um `content/tags/<slug>/_index.md` com `book:`:

```yaml
---
title: "O livro das citações: um breviário de ideias replicantes"
description: "Antologia organizada por Eduardo Giannetti. As citações guardadas daqui aparecem abaixo."
book:
  author: "Eduardo Giannetti"
  publisher: "Companhia das Letras"   # opcional
  year: 2008                          # opcional
---
```

Com `book:`, `layouts/_default/term.html` mostra o título sem `#`, a linha autor · editora · ano e a descrição. Sem `book:`, a tag segue como `#slug`.

## Stack

- **[Hugo](https://gohugo.io)** v0.148+ extended — gerador estático
- **[Blowfish](https://blowfish.page)** — tema base (Tailwind, dark/light, busca client-side)
- **CSS Grid** puro para o mosaico (sem framework JS)
- **Git submodule** para o tema (não Hugo Modules — evita dependência de Go)
- **[reveal.js](https://revealjs.com)** 5.1 (via jsDelivr) — só nas apresentações de `/slides/`
- **pytest** — auditoria de estilo determinística das notas (`tests/style/`, skill `/style-test`)

## Estrutura do repositório

```
scholion/
├── .claude/skills/      # skills do Claude Code específicas do Scholion (add-scholion-*, import-kindle-highlights…)
├── archetypes/          # template para nota nova (hugo new notes/foo.md)
├── assets/
│   ├── css/
│   │   ├── custom.css           # overrides + layout do mosaico/single
│   │   └── schemes/scholion.css # color scheme âmbar
│   ├── fonts/, icons/, images/
│   └── img/seal.png
├── config/_default/     # hugo.toml, params.toml, markup.toml, languages, menus
├── content/
│   ├── notes/           # ~6.000 notas em markdown
│   ├── research/        # pesquisas vivas
│   ├── places/          # lugares (page bundles)
│   ├── slides/          # apresentações reveal.js
│   ├── quotes/, sources/  # só _index.md (listagens geradas a partir das notas)
│   └── tags/            # páginas de tag com texto próprio (incl. páginas de livro)
├── data/
│   ├── git_history/     # JSONs com histórico por nota (gerados)
│   └── scales.yaml      # escalas 0–5
├── layouts/             # templates próprios (override do Blowfish)
│   ├── _default/        # baseof.html, term.html, terms.html, index.json
│   ├── index.html
│   ├── notes/           # list.html, single.html
│   ├── places/          # list.html, single.html
│   ├── quotes/list.html
│   ├── research/single.html
│   ├── slides/single.html
│   ├── sources/list.html
│   └── partials/        # head, footer, OG image, backlinks, co-tags, escalas, wikilinks, paginação
├── scripts/             # gen_git_history.py, pre-push hook
├── tests/style/         # suíte pytest de auditoria de estilo
├── static/              # favicon.png, anexos estáticos
├── deploy.ps1           # build + sync incremental S3 + invalidação CloudFront
├── deploy-scheduled.ps1 # wrapper da publicação agendada
├── themes/blowfish/     # submódulo público
└── fontes-privadas/     # submódulo privado, não entra no build
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

Copie o hook pre-push para que os JSONs sejam regenerados antes de cada push:

```bash
cp scripts/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

Antes de cada push, o hook lê a faixa de commits sendo enviada (via stdin do git) e roda `gen_git_history.py --range <remote>..<local>`, regenerando JSON apenas dos notes alterados nessa faixa. Se houver mudança, faz um commit `chore: update git history`. Esse commit só sobe no *próximo* push (o push atual já tem as refs resolvidas). Implicação: uma nota nova estreia sem histórico no site e só ganha a linha de mudança no push seguinte.

Para forçar atualização imediata, rodar manualmente:

```bash
python scripts/gen_git_history.py --all
git add data/git_history/
git commit -m "chore: update git history"
git push
```

## Deploy

**AWS S3 + CloudFront** (us-east-1), publicado por script local (`deploy.ps1`), não pelo CI. O build local aproveita o cache de imagens processadas em `resources/_gen/`, que no Actions levava ~9 min para refazer.

```powershell
pwsh -NoProfile -File deploy.ps1                  # incremental
pwsh -NoProfile -File deploy.ps1 -ForceFullSync   # hash de todo o public/
```

O `deploy.ps1` sincroniza com `origin` (fetch + merge, best-effort: falha não impede a publicação) e compara `HEAD` com `last-published-commit.txt`; sem commit novo, sai sem buildar. Com commit novo, fixa o commit antes do build, roda o Hugo e deriva via `git diff` quais páginas mudaram (nota, OG image, seção, paginadores, tags, histórico). Depois sobe só os arquivos cujo hash difere do `public-manifest.json` e invalida o CloudFront.

**Publicação agendada:** a tarefa `\Claude\ScholionPublish` roda a cada 30 min (via `deploy-launcher.vbs`, sem janela, e `deploy-scheduled.ps1`, com saída em `deploy-scheduled.log`). A primeira execução a partir das 03:00 de cada dia faz o fullsync. Antes do deploy, o wrapper também commita e dá push do que houver de novo em `fontes-privadas/`.

### Workflow de emergência no CI

`.github/workflows/deploy.yml` continua existindo, só com `workflow_dispatch` (acionamento manual), para publicar se a máquina local estiver fora.

O `GITHUB_TOKEN` default do Actions só tem acesso ao repo do checkout. Se o workflow tenta clonar um submódulo privado (ex.: `fontes-privadas/`), o checkout falha antes do Hugo rodar.

Solução adotada: `submodules: false` no checkout, e `git submodule update --init themes/blowfish` num passo seguinte para puxar só o tema (público). O submódulo privado fica de fora — o site referencia esses textos, nunca os consome no build.

Se um dia um submódulo privado precisar entrar no build:

1. Criar Personal Access Token (fine-grained) com leitura nos dois repos.
2. Salvar como secret `SUBMODULE_TOKEN` no repo principal.
3. Trocar o passo de checkout por:

   ```yaml
   - uses: actions/checkout@v4
     with:
       token: ${{ secrets.SUBMODULE_TOKEN }}
       submodules: recursive
   ```

   E remover o `git submodule update --init themes/blowfish` (vira redundante).

## Histórico

Ver [CHANGELOG.md](./CHANGELOG.md).

## Licença

[MIT](./LICENSE) — código e estrutura. O conteúdo das notas é direito autoral do autor (Thiago Luiz Silva).
