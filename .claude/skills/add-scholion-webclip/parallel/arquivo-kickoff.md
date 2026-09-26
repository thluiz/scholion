# Lote "Arquivo" (favoritos do Edge): kickoff para sessão nova

Pasta de origem: perfil Default do Edge, barra de favoritos, `Arquivo` (650 links, 635 únicos).
482 já estavam no manifesto (mesmos links da pasta `processar`, processados em 2026-09-25).
Os 153 novos foram acrescentados em 2026-09-26 ao manifesto de sempre
(`C:\Users\conta\OneDrive\MD\_webclip_manifest.json`) com `"pool": "arquivo"`, `folder` e `title`:

| status | itens | o quê |
|---|---|---|
| `pending` | 91 | a fila deste lote (todos `url`) |
| `failed` | 16 | pré-filtrados: Pinterest, família Medium etc., que sempre falham no renderizador |
| `hold` | 46 | Cifra Club da subpasta `Gaita`: tablaturas, não artigos. **Não processar** até o Thiago decidir |

O Bookmarks do Edge **não** é editado: o manifesto é a única fonte de verdade.

## Comando (colar numa sessão nova com cwd `E:\scholion`)

```
Você é o orquestrador do lote "Arquivo" de webclips. Leia inteiro
E:\scholion\.claude\skills\add-scholion-webclip\parallel\arquivo-kickoff.md
e siga a seção "Como orquestrar". Comece relatando quantos itens
`pending` com pool "arquivo" existem no manifesto.
```

## Como orquestrar

Pasta de trabalho: `C:\Users\conta\AppData\Local\Temp\webclip-streams\arquivo\` (criar). Os scripts
ficam em `E:\scholion\.claude\skills\add-scholion-webclip\parallel\`.

1. Conferir antes: `curl http://localhost:8080/api/webclip/health` ok, `git status` limpo em
   `E:\scholion` (fora `.mcp.json` e `.claude/scheduled_tasks.lock`, que não são nossos).
2. Três fluxos em paralelo, A, B e C, cada um com 15 itens por rodada:
   `python partition.py <workdir> A 1 --pool arquivo` (idem B e C). O script pula itens que já
   estão com outro fluxo.
3. Despachar um subagente `general-purpose` por fluxo com o **prompt do worker** abaixo,
   trocando `<X>` pela letra, `<ROUND>` pelo número e `<WORKDIR>` pela pasta de trabalho.
4. Quando um fluxo terminar: `python merge.py <workdir> <X> <ROUND>` e, se ainda houver
   pendentes, particionar a próxima rodada dele e redespachar na hora, sem esperar os outros.
5. Git: os workers fazem commit, mas **nunca** push. O orquestrador faz `git push` (e `pull` só
   se o push for recusado) **apenas quando nenhum fluxo estiver no meio de uma rodada**. O hook
   de pre-push e o job "Gerando histórico de notas" varrem o index, e um `pull --autostash` com
   worker staged mexe no trabalho dele.
6. No fim: merge de tudo, push, e relatório para o Thiago (done/failed/skipped por motivo, notas
   que parecem página de venda/pessoal para ele decidir apagar).

Se um fluxo reportar algo estranho (resposta com URL trocada, serviço fora, erro repetido), parar
de despachar e avisar o Thiago em vez de contornar.

## Prompt do worker (modelo)

```
You are ONE of three parallel workers processing the Scholion webclip queue. You are stream **<X>**.

Your assigned items are in <WORKDIR>\<X><ROUND>.json (field `items`). Process ONLY those items, in
that order, one at a time. Never touch any other queue item.

First, Read the whole playbook, top to bottom, no offset/limit:
E:\scholion\.claude\skills\add-scholion-webclip\batch-playbook.md. Follow its per-item pipeline
(compose, checks, save with mode return, write files, stage, audit marker), WITH THESE OVERRIDES
for parallel mode:
- DO NOT read or write the manifest (C:\Users\conta\OneDrive\MD\_webclip_manifest.json). At the end
  write your results to <WORKDIR>\results-<X>.json as a JSON array (UTF-8), one object per assigned
  item: {"url": <the item's url exactly as in the assignment>, "status": "done"|"failed"|"skipped",
  "reason": <string, omit for done>}.
- ISOLATION: run ONLY scripts that live in your own folder <WORKDIR>\work-<X>\ (create it; write your
  helpers there). NEVER execute or write anything outside it except the repo files the playbook
  writes. A shared `cur.json` once swapped responses between streams.
- MANDATORY: after every compose, verify the returned clipping URL equals the URL you requested. On
  mismatch, do not save; re-request once; if it mismatches again, mark failed / `response_mismatch`.
- Other workers stage and commit in E:\scholion at the same time, and a scheduled job ("Gerando
  histórico de notas") may commit staged files on its own. Only `git add` your own paths; commit once
  at the end with `git commit --only -m "<msg>" -- <your paths>`. If some paths were already swept
  into HEAD by that job, that is fine; report it. On `index.lock`, wait 5s and retry (up to 10x);
  never delete the lock. Do NOT push, pull, stash or reset.
- Do not append to clippings/_batch-log.md (shared file).

Rules:
- No hugo. No subagents. No Monitor tool. No Co-Authored-By in commits.
- Slug collision with a DIFFERENT url → skipped / `slug_collision`.
- Soft 404s (DMCA/takedown, missing article, "404 Not Found", hijacked/parked/spam domain, redirect to
  an unrelated page or blog listing, generic landing page, Cloudflare/HTTP error page, access-request
  screen, paywall teaser where only the intro was captured, newsletter subscribe page, link digest or
  ranking list, related-post teaser, search/listing/archive page, footer/sidebar, cookie/consent wall,
  login wall, survey form, map page, video/image page with no text) → do not save; failed / `soft_404`.
- Not articles: sales/product pages (course, book, crowdfunding, store product, product landing,
  pricing, feature list, product docs, tool front page) → failed / `promo_page`; personal homepages /
  site front pages → failed / `personal_homepage`; personal lifestyle interviews → failed / `off_topic`.
- LANGUAGE (strict), judged on the NOTE, not the source: one language per note, the page's language,
  including the frontmatter title. English note: heading `## Reading notes`, English
  summary/lead/bullets/tags, no Portuguese. Portuguese note: heading `## Fichamento`, Brazilian
  Portuguese everything including tags. A source in European Portuguese is fine; only a NOTE written in
  European Portuguese after one recompose → failed / `pt_eu`. Loanwords/quoted terms are fine. No stray
  words in other scripts. Server error "idioma misto" or wrong-language prose → failed / `language_mismatch`.
- TAG FIXES (the only allowed edit): strip accents from tags; if only the tags are in the wrong
  language, translate them yourself. Before staging and before the audit marker.
- Service hiccup: nginx 502/503 with an HTML body, or an `internal_error` ("browser has been closed",
  "page is navigating") → wait 15s, check /api/webclip/health, retry once. A 502 with a JSON fetch
  error body is a real result (playbook retry rule). 429 → wait 60s and retry. Renders can take ~45s.

Final report: done/failed/skipped with reasons, commit SHA, path of results-<X>.json, tag fixes, any
mismatches, anything odd (sales/personal pages kept, off-topic notes).
```

## O que já se sabe (lote de 2026-09-25, 1806 itens)

- Domínios que sempre falham e valem pré-filtro no manifesto em vez de gastar rodada: Pinterest,
  família Medium (medium.com, gitconnected, plainenglish, itnext, towardsdatascience, stackademic,
  uxdesign, faun.pub), twitter/x, threads, linkedin, instagram, facebook, reddit, msn (renderiza vazio),
  toptal, sitepoint, britannica, baeldung, blog antigo do sketchbook.
- Limites do webclipper estão em 30 composições/min e 5000/dia (`.env` do serviço em HermesTools).
- Rodada de 15 itens leva ~10 min por fluxo; três fluxos rendem ~40 notas a cada 12 min.
