---
name: add-scholion-webclip
description: Captura uma página web e gera uma nota category:webclip no Scholion com resumo e fichamento, via a API scholion-webclipper (fetch, extração e composição rodam server-side). Opcionalmente cria notas de citação a partir de frases da mesma página.
argument-hint: "[url ou caminho .md] | [frase1] | [frase2] | ..."
---

Captura uma página web e cria uma nota `category: webclip` no **Scholion** em
`E:/scholion/content/notes/<slug>.md`, apoiada num clipping bruto salvo em
`E:/scholion/clippings/<YYYY-MM>/<dominio>--<slug>.md`. Opcionalmente cria
notas `category: quote` a partir de frases da mesma página.

Fetch, extração (Playwright + Readability + Markdown) e composição (resumo +
fichamento + ghost-audit) rodam **server-side** na API `scholion-webclipper`
(`http://localhost:8080/api/webclip/`, deployada em HermesTools) — esta skill
não lê a página inteira no próprio contexto nem redige a nota à mão. Ver
`E:\scholion-webclipper\README.md` pro desenho completo (decisões 1–10).

---

## PORTÃO OBRIGATÓRIO — nota NÃO ESTÁ PRONTA sem passar aqui

Aplica-se à nota `webclip` e a cada nota `quote` gerada nesta skill — **não**
ao clipping bruto (extração automática, sem voz autoral).

Para a nota `webclip`, o ghost-audit **já rodou dentro do `compose`** (passo 1)
— não existe mais uma chamada HTTP separada pra essa nota. O campo `audit` da
resposta do `compose` **é** o portão. Ler `audit.verdict`/`audit.findings` e
mostrar ao autor antes de qualquer preview, escrita ou commit.

**Regras rígidas — sem exceção:**

- `verdict: red` → **não pode salvar**. A key desta skill (`add-scholion-webclip-skill`, role `write`) não tem `webclip.save.force` — só a key `admin` do Thiago tem, de propósito (ver Decision 3 do README do scholion-webclipper). Não existe "forçar" a partir daqui: o caminho é ajustar o que motivou o red (ex.: pedir pro autor decidir sobre um `relatedNotes` mal escolhido) e chamar `compose` de novo.
- `verdict: yellow` → mostrar findings ao autor, ele decide caso a caso.
- `verdict: green` → seguir.
- **PROIBIDO substituir por checklist mental.** Sem o JSON da resposta do `compose` visto, a auditoria não aconteceu.
- **Fail-open**: se `http://localhost:8080/api/webclip/health` não responder, dizer isso explicitamente ao autor e perguntar como proceder — **não** cair silenciosamente para composição manual. Isso reabriria o problema de custo de token que essa API existe pra resolver.

Notas `quote` (passo 5) continuam usando o fluxo antigo de `add-scholion-quote`, com sua própria chamada de `ghost-audit` HTTP — inalterado por esta skill.

---

## Parâmetros

Os argumentos vêm em `$ARGUMENTS` em formato livre, separados por ` | `:

- **Primeiro argumento** — URL (`http://` ou `https://`) **ou** caminho de um arquivo `.md` já existente. Se nenhum dos dois, pergunte.
- **Argumentos seguintes** (opcionais) — frases da página para virar notas de citação (`category: quote`). Podem vir agora ou numa invocação futura contra a mesma URL/clipping.

## Processo

### 1. Compor (fetch + extração + composição + auditoria num único passo)

Ler a API key uma vez:

```powershell
$webclipKey = Get-Content 'C:\Users\conta\.claude\secrets\scholion-webclipper.key' -Raw
```

Essa key **nunca** vai em nenhum arquivo do repo `scholion` (público) — vive só nesse arquivo local, fora de qualquer repo.

**Modo URL (padrão)**:

```powershell
$body = @{ url = '<url original>' } | ConvertTo-Json
$r = Invoke-RestMethod -Uri 'http://localhost:8080/api/webclip/webclip/compose' -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 300
```

Sucesso (HTTP 201): `$r` traz `operationId`, `clipping` (title/url/domain/capturedAt/markdown), `note` (slug/title/summary/tags/language/body), `audit` (verdict/findings/summary), `expiresAt`. Guardar `operationId` — é a chave de tudo daqui pra frente.

**Erro — decidir pelo `error.code`** (`Invoke-RestMethod` lança exceção em 4xx/5xx; ler o corpo do erro via `$_.ErrorDetails.Message | ConvertFrom-Json`):

| `code` | Ação |
|---|---|
| `fetch_timeout`, `fetch_failed` (`retryable: true`) | Tentar de novo uma vez. Se persistir, cair pro fallback Claude in Chrome abaixo. |
| `blocked_domain`, `consent_wall_unresolved`, `thin_content` (`retryable: false`) | Cair direto pro fallback Claude in Chrome — repetir a mesma chamada não muda nada. |
| Serviço inatingível (erro de conexão, não HTTP) | **Fail-open**: avisar o autor explicitamente, perguntar como proceder. Não presumir contingência manual sozinho. |

**Fallback Claude in Chrome** (sessão real e logada do autor, que o Playwright headless do serviço não tem): `tabs_context_mcp` → `tabs_create_mcp` → `navigate(url)` → `get_page_text(tabId)` → capturar título da tab → `tabs_close_mcp`. Depois, repetir o `compose` em modo texto:

```powershell
$body = @{ text = '<texto capturado>'; title = '<título da tab>'; url = '<url original>'; domain = '<dominio sem www., pontos trocados por ->' } | ConvertTo-Json
```

**Modo arquivo `.md`**: ler o arquivo. Se já tiver frontmatter de clipping (`url`/`title`/`domain`/`captured_at`), reaproveitar todos os quatro — `captured_at` vira `capturedAt` no body do `compose` (o endpoint aceita esse override pra não perder o timestamp original nem o mês `<YYYY-MM>` de captura real). Se não tiver frontmatter, perguntar URL de origem (obrigatória) e título; nesse caso `capturedAt` fica de fora e o endpoint usa "agora". Corpo do arquivo vira `text`.

### 2. Search-first interativo

**Depois** do `compose` (passo 1), não antes — agora dá pra buscar com base no `title`/`summary`/`tags`/`body` reais, não num palpite pré-captura. Buscar no vault (`Grep`/`Glob` em `E:/scholion/content/notes/` e `E:/scholion/content/research/`) por temas relacionados. Mostrar matches com contexto breve (1 linha: título + slug + 1 frase) e **esperar o autor apontar** o que linkar. Se nada relevante, dizer isso explicitamente.

Se o autor apontar notas: **recompor** — chamar `compose` de novo, mesma URL/texto do passo 1, agora com `relatedNotes`:

```powershell
$body = @{ url = '<mesma url>'; relatedNotes = @(@{ slug = '<slug>'; title = '<título>'; hint = '<por que conecta, opcional>' }) } | ConvertTo-Json -Depth 6
```

Isso gera um `operationId` novo (já auditado de novo) — usar esse daqui pra frente; o anterior simplesmente expira sem uso (nunca é salvo). Se nada relevante no search-first, seguir com o `operationId` do passo 1.

### 3. Preview e aprovação

Mostrar ao autor: `title`, `summary`, `tags`, `body` (resumo + fichamento), e o `audit` inteiro (verdict + findings) — aplicando as regras do PORTÃO OBRIGATÓRIO acima. Um trecho de `clipping.markdown` também ajuda o autor a conferir que a extração pegou o conteúdo certo (não menu/paywall/newsletter). Aguardar confirmação explícita antes de salvar.

### 4. Salvar

```powershell
$body = @{ mode = 'return' } | ConvertTo-Json
$s = Invoke-RestMethod -Uri "http://localhost:8080/api/webclip/webclip/$($r.operationId)/save" -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 60
```

`mode: "return"` — não `"commit"` — porque o commit precisa acontecer no repo local do autor (`E:\scholion`), não no clone próprio do serviço em HermesTools (ver Decision 9 do README do scholion-webclipper: `"commit"` é pro Claudinho/agente autônomo, sem working tree local; `"return"` é pra quem já tem um checkout, como esta skill). `$s` traz `slug`, `notePath`, `clippingPath`, `clippingContent`, `noteContent` prontos — usar como vieram, sem editar (editar exigiria recompor, ver Decision 8).

1. Escrever os dois arquivos em `E:\scholion\<clippingPath>` e `E:\scholion\<notePath>` (criar diretórios se preciso).
2. `git add` os dois caminhos.
3. **Marcador do gate, a partir do veredito que já temos** — não deixar o hook `ghost-audit-gate.ps1` reauditar a nota (ela já foi auditada no `compose`; ver Decision 10 do README do scholion-webclipper). Só gravar se `audit.verdict` for `green` ou `yellow` — nunca pra um `red` não resolvido:
   ```powershell
   $o = git -C E:\scholion rev-parse ":$($s.notePath)"
   New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
   Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
   ```
4. **Um commit só**, cobrindo clipping + nota juntos (diferente da convenção antiga de dois commits — ver Decision 5/9 do scholion-webclipper: o `save` é uma decisão atômica do autor, não dois artefatos independentes): `git commit -m "webclip: $($s.slug)"`.
5. `git push` (se houver remoto).

### 5. Notas de citação (se houver frases)

Para cada frase recebida, gerar uma nota `category: quote` reaproveitando `add-scholion-quote`, **exceto**:
- **Pular a pesquisa externa de autoria** (Quote Investigator/Wikiquote/web search) — autor e URL já são conhecidos, vêm do clipping desta mesma página.
- `sources`: mesma URL do webclip (`$r.clipping.url`), `kind` igual ao inferido pelo endpoint (visível em `renderNote`/`inferSourceKind` do scholion-webclipper, mesma tabela de `add-scholion-note`).

Mantém do `add-scholion-quote`: tag do autor obrigatória, ghost-writer, ghost-audit (chamada própria, separada — inalterada), preview, commit próprio por nota.

## Regras

- **Voz e estilo**: resumo e fichamento vêm prontos do `compose` — já passaram pelas regras de `ghost-writer` no prompt do servidor. Não há mais "modo de contingência" de composição manual: se o serviço estiver fora, o comportamento é parar e avisar (ver Fail-open no PORTÃO OBRIGATÓRIO), não reverter para redigir à mão.
- **`captured_at`/`date` são OBRIGATÓRIOS** com timestamp real — o `compose` já cuida disso (agora, ou o `capturedAt` do modo arquivo); nunca inventar um valor manualmente.
- **`category: webclip` é OBRIGATÓRIO** na nota principal — o servidor já garante isso na renderização.
- Clipping bruto nunca é colado verbatim na nota — a nota é sempre prosa composta (garantido pelo prompt do servidor).
- **Um commit cobre clipping + nota juntos** (passo 4, item 4) — não é mais "um commit por artefato" pra esses dois; notas `quote` do passo 5 continuam com commit próprio cada.
- Sem `Co-Authored-By Claude` em nenhum commit.
- Não tocar em `E:/silva/src/content/note/`.
- **Nunca inventar** conteúdo do fichamento além do que está no texto capturado — garantido pelo prompt do servidor, mas o preview (passo 3) é a última checagem humana disso.
- Sem build do Hugo por nota: quem compila é o `\Claude\ScholionPublish` (a cada 30 min). Um build completo do site por item só gasta CPU.
- A API key da skill vive só em `C:\Users\conta\.claude\secrets\scholion-webclipper.key` — nunca em texto plano em nenhum arquivo deste repo.
