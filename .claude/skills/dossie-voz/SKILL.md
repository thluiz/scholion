---
name: dossie-voz
description: Mantém o Claude Doc de marcos consolidados de uma pesquisa viva do Scholion, que o Claude da web lê pelo conector para conversar por voz com o autor no celular, e depois incorpora o fechamento dessa conversa de volta na pesquisa. Use quando o autor pedir para preparar uma conversa, caminhada ou papo de voz sobre uma pesquisa, para atualizar o doc consolidado, quando trouxer o fechamento de uma conversa, ou pedir para sincronizar (puxar o que avançou nas conversas do chat).
argument-hint: "<slug da pesquisa> [foco] | sincronizar <slug> | fechar [link do doc de fechamento ou texto]"
---

# Dossiê de voz

Duas pontas do mesmo ciclo:

1. **Consolidar**: cria ou atualiza, a partir de `content/research/<slug>.md`, um Claude Doc privado com os marcos consolidados da pesquisa. O Claude da web lê esse doc pelo conector Claude Docs e conversa com o autor enquanto ele anda ou dirige. Nada é anexado à mão.
2. **Fechar**: pega o doc de fechamento que a conversa produziu, incorpora na pesquisa, arquiva o fechamento, atualiza o doc consolidado e apaga o doc de fechamento do claude.ai.

Onde cada coisa vive:

```
claude.ai (Claude Docs, privado)       "<Título curto da pesquisa> — marcos consolidados"
fontes-privadas/voz/<slug>/README.md   link do doc consolidado + data da última atualização
fontes-privadas/voz/<slug>/fechamentos/<AAAA-MM-DD>-<tema>.md
```

O doc consolidado é derivado da pesquisa: a fonte de verdade continua sendo `content/research/<slug>.md`. Não guardar cópia local do doc; se ele se perder, refaz-se a partir da pesquisa. Os fechamentos, ao contrário, são material original do autor e ficam arquivados no submódulo privado `fontes-privadas/` (GitHub privado, com backup).

Doc de referência: "Pequeno Tratado em Áudio — marcos consolidados", link em `fontes-privadas/voz/pequeno-tratado-em-audio/README.md`.

## Versão do dossiê

Cada dossiê carrega um número de versão, para que a divergência entre pesquisa e doc salte aos olhos sem comparar hashes:

- **Na pesquisa**, no Estado: `- **Dossiê de voz**: v<N>, sincronizado em <AAAA-MM-DD> (link em fontes-privadas/voz/<slug>/README.md)`.
- **No doc**, na linha abaixo do byline: `Sincronizado com a pesquisa em <AAAA-MM-DD> (v<N>, commit <hash>)`.
- **No README**: `Última sincronização: <AAAA-MM-DD>, v<N>, pesquisa no commit <hash>, rev <r> da aba principal`.

`<N>` sobe em 1 a cada atualização do doc (Modo 1 sobre doc existente, ou passo 7 do Modo 2). `<hash>` é o commit da pesquisa que o doc reflete. Como a linha do Estado entra no mesmo commit, o hash só existe depois dele: commit primeiro, depois doc e README. Divergência: `git log -1 --format=%h -- content/research/<slug>.md` diferente do hash do README significa que a pesquisa avançou sem o doc; a skill `research-status` mostra isso e a `research` avisa ao retomar. Docs anteriores a esta convenção recebem v1 na próxima atualização.

## Antes de qualquer chamada de docs

Carregar a skill de docs (`anthropic-skills:docs`) e seguir as instruções do conector: `guide( items = ["topic.index"] )` uma vez por sessão, abrir o doc com `Artifact` (`action: "open"`) logo depois de criá-lo, preencher uma seção por chamada. Nunca usar WebFetch em link de doc.

## Modo 1 — Consolidar

Argumento: slug da pesquisa, e opcionalmente um foco (uma direção, um capítulo, uma virtude). Sem foco, o doc cobre a pesquisa inteira, priorizando **Em foco** e **Próximo** do Estado.

### Passos

1. **Ler a pesquisa inteira**, Estado primeiro. Ler `fontes-privadas/voz/<slug>/README.md`: se já existe doc consolidado, ele é atualizado, nunca recriado.
2. **Ler as notas linkadas** que o doc vai usar. Delas saem as citações, com autor e obra como estão na nota.
3. **Fontes privadas**: se a pesquisa aponta um livro em `fontes-privadas/` (`.txt`), usar para conferir citações. Citação literal só se conferida contra o texto; o resto é paráfrase.
4. **Preview**: mostrar ao autor o esqueleto (seções, uma linha cada) e as frases que vão entre aspas. Escrever no doc só depois da aprovação.
5. **Escrever**:
   - Doc novo: nascer com o esqueleto (um bloco `pending` por seção), abrir, preencher seção a seção.
   - Doc existente: ler (`read` com `sinceRev` ou `outline`), trocar só as seções que mudaram. Edições que o autor fez no doc vencem; nunca usar `force`.
6. **Marcar na pesquisa e registrar**: no Estado da pesquisa, a linha `- **Dossiê de voz**: v<N>, sincronizado em <data> (link em fontes-privadas/voz/<slug>/README.md)`; `hugo --quiet`; commit `research: dossiê de voz v<N> em <tema>`. Com o hash desse commit, escrever a linha de sincronização no doc e atualizar `fontes-privadas/voz/<slug>/README.md` (link, data, v<N>, hash, rev). Commit no submódulo + push, e ponteiro no Scholion.
7. **Entregar**: uma linha com o link e como usar: abrir o Claude no celular, conversa nova com o conector Claude Docs ativo, pedir "leia o doc <título>" e ligar o modo voz.

### Seções do doc consolidado

1. **Para a IA que conversa comigo**: bloco fixo abaixo.
2. **A pesquisa em cinco linhas**: pergunta central, Em foco, Próximo, decisões do autor, perguntas em aberto (as do autor, literais).
3. **Marcos consolidados**: uma seção por resultado fechado (definições, decisões, eixos, tabelas de teste). Formulações do autor literais e marcadas [autor]; contribuições da IA marcadas ⚠.
4. **Fontes conferidas**: só o que está ✓ na pesquisa, com citação curta e referência.
5. **Pendências e modelo de fechamento**: o que está ⚠ ou `?` na pesquisa, para a IA não afirmar como certo; e o modelo de fechamento.

Quando o foco pede profundidade (um capítulo, um autor), acrescentar uma aba com fichas, uma por unidade de conversa: **Em uma frase**, **O argumento** (3 a 6 bullets), **Com quem pensa**, **Citações conferidas**, **Tensões para puxar** (marcadas como sugestão), **Perguntas para caminhar** (3 a 4, na segunda pessoa do autor), **Do Scholion**, **Pendências**.

### Bloco "Para a IA que conversa comigo"

As regras gerais de conversa (como falar, honestidade com as fontes, criação do Fechamento e comentário na caixa de entrada, encerramento) vivem na skill do chat `dossie-de-voz`, não no doc. O bloco do doc carrega só o que é desta pesquisa. Ajustar `<tema>`, `<unidade>` (virtude, direção, capítulo, bloco…) e o específico:

```markdown
Leia isto antes de tudo. O resto do documento é o estado consolidado da pesquisa `content/research/<slug>.md` do Scholion, conferido em <data>. Uso privado.

**Regras gerais** de conversa, registro e fechamento estão na skill `dossie-de-voz`, instalada no claude.ai. Se ela não carregou nesta conversa, diga isso antes de começar.

**Situação.** Estou andando na rua ou dirigindo, falando no celular. Vou escolher uma <unidade> (ou pedir que você sorteie) e pensar em voz alta. Você é o interlocutor: leu a pesquisa e as fontes com atenção e puxa conversa. Comece perguntando qual <unidade>; abra com o que já está fechado sobre ela em uma ou duas frases e me devolva a palavra.

**Específico desta pesquisa**
- <regras de atribuição próprias: quem é citado, o que é leitura minha sem fonte, o que não apresentar como ensinamento de alguém>
- O que está marcado ⚠ é formulação minha ou da IA, não do autor estudado. O que está em Pendências não é fato.

**Fechamento.** Nome do documento: "Fechamento — <tema> — <data>"; segunda linha "Status: em andamento · Base: dossiê v<N>, sincronizado em <data>". Modelo no fim deste documento.
```

Docs criados antes desta convenção ainda trazem o bloco longo com as regras gerais; trocar pelo curto na próxima atualização (Modo 1, passo 5).

Modelo de fechamento (vai na última seção do doc):

```
FECHAMENTO — <unidade> — <data>
1. O que eu disse (minhas formulações, com as minhas palavras, sem polir)
2. Onde concordei / discordei dos autores
3. Notas do Scholion que apareceram
4. Paralelos que surgiram (outra tradição, ideograma, passagem)
5. Ideias ou exemplos novos, marcando de quem: [eu] ou [IA]
6. Coisas a verificar (afirmações sem fonte que apareceram)
7. Próximo passo ou semente de texto: título provisório + a pergunta que abre
```

### Regras de conteúdo

- **Source-or-silence vale no doc.** A IA de voz repete o que lê como fato. Nada de etimologia, datação ou atribuição sem fonte; o que a pesquisa marca ⚠ ou `?` vai para Pendências.
- **Citações**: só as conferidas, curtas (obra com direito autoral: frases, não parágrafos), com referência.
- **O doc é privado.** Nunca compartilhar: carrega paráfrase, citação e, por decisão do autor, o texto integral das fontes privadas que ele usa como base de pesquisa.
- **Fontes integrais**: aba "Fontes" com os textos de domínio público (trecho usado + link) e, em sub-abas, o texto integral da fonte privada, um capítulo por aba. No modo automático o upload de texto protegido é barrado pelo classificador; fazer com o autor fora do modo automático, aprovando o passo.
- **Escrita**: frases curtas, PT-BR, sem floreio. A IA vai falar isso em voz alta.

## Sincronização chat ↔ Scholion

O ponto de encontro entre o Claude do chat (que conversa por voz) e esta skill é o próprio dossiê:

- **Caixa de entrada = comentários do dossiê.** Ao criar um Fechamento, o Claude do chat deixa um comentário no topo da aba principal do dossiê com `FECHAMENTO: <link> — <tema> — <data>`. Ele não edita o texto do dossiê.
- **Status no Fechamento.** A segunda linha do Fechamento é `Status: em andamento` ou `Status: fechado` e `Base: dossiê v<N>, sincronizado em <data>`. Só se incorpora Fechamento com `Status: fechado`. Se a versão da base for anterior à atual do doc, avisar o autor: a conversa partiu de um estado antigo.
- **Linha de sincronização no dossiê.** Logo abaixo do byline: `Sincronizado com a pesquisa em <data> (v<N>, commit <hash>)`. Atualizada a cada incorporação.
- **Skill do chat.** A versão em uso fica em `fontes-privadas/voz/skills/dossie-de-voz/SKILL.md`; o autor a instala no claude.ai. Mudou o protocolo aqui, mudar lá também e avisar o autor para reinstalar.
- A caixa de entrada é a única fonte de fechamentos. Não listar artifacts para procurá-los.

## Modo 3 — Sincronizar

Argumento: `sincronizar <slug>`. Também roda quando a skill `research` retoma uma pesquisa que tem dossiê.

1. Ler o link do dossiê em `fontes-privadas/voz/<slug>/README.md`.
2. Ler os comentários abertos da aba principal: `query( object = "utterance", container = <doc>, payload = {"under":{"object":"node","id":"<body id>"}} )`. Cada comentário `FECHAMENTO: …` não resolvido é um pendente.
3. Para cada pendente, ler o Fechamento. `Status: em andamento` → só avisar o autor. `Status: fechado` → rodar o Modo 2.
4. Ler também `read( …, payload = {"kind":"view","sinceRev":<rev registrado no README>} )` do dossiê: edições feitas lá pelo autor entram como insumo e são mostradas a ele.
5. Ao terminar cada um: responder no comentário com o que entrou (seção da pesquisa + commit) e resolvê-lo; atualizar a linha de sincronização e o `rev` no README.
6. Nada pendente: dizer isso em uma linha.

## Modo 2 — Fechar a conversa

Argumento: `fechar` + o link do doc de fechamento, ou o texto colado. Sem link, rodar o Modo 3: a caixa de entrada do dossiê é a única fonte.

### Passos

1. **Ler o fechamento inteiro** pelas ferramentas de docs. O `export` em markdown volta em base64 inline; para docs grandes, ler o corpo com `read( ref = {"object":"node","id":"<body id>"}, engine = "prose" )`: o resultado é salvo em arquivo e `python .claude/skills/dossie-voz/doc2md.py <arquivo salvo> <saída.md>` converte o XML em markdown. Se o autor colar trecho da conversa (link de share), usar o texto colado; não abrir o link.
2. **Resumir para o autor** o que saiu da conversa e **apontar problemas**: afirmações sem fonte, citações a conferir, nomes que a transcrição de voz pode ter trocado, slugs que não existem, contradições internas do fechamento.
3. **Search-first**: buscar no vault (`content/notes/`, `content/research/`) o que se conecta aos temas novos; listar e esperar o autor apontar o que linkar.
4. **Conferir** o que o autor pedir. Fontes primárias em sites distintos podem ir para subagentes em paralelo, um site por agente, fetches seriais dentro de cada um.
5. **Preview da atualização da pesquisa**: Estado, decisões do autor, perguntas em aberto que o autor levantou (literais), e uma seção nova com o que entrou. Tudo com ✓ / ⚠ / `?` conforme a convenção da skill `research`. O que não tem fonte fica de fora e é avisado no chat.
6. **Gravar só depois da aprovação.** A atualização inclui a linha do Estado `**Dossiê de voz**: v<N+1>, sincronizado em <hoje>`. `hugo --quiet`, commit `research: <ação> em <tema>`.
7. **Fechar o ciclo**, num passo só, com o hash do commit anterior:
   - arquivar o fechamento em `fontes-privadas/voz/<slug>/fechamentos/<AAAA-MM-DD>-<tema>.md`, com cabeçalho de procedência (de onde veio, onde foi incorporado, correções feitas, decisões posteriores do autor);
   - atualizar o README (data, v<N+1>, hash, rev);
   - um commit no submódulo + push, e um commit de ponteiro no Scholion;
   - atualizar o doc consolidado (Modo 1, passo 5, doc existente) com o que entrou na pesquisa e a linha de sincronização nova;
   - responder o comentário do Fechamento na caixa de entrada com a seção da pesquisa e o commit, e resolvê-lo.
8. **Apagar o doc de fechamento do claude.ai** (`Artifact` com `action: "delete"`) só depois do arquivo commitado e com push feito. O autor confirma a exclusão. O doc consolidado não é apagado.

## Subir texto longo para uma aba

O conteúdo de um arquivo local não passa pelas chamadas de docs; ele sobe como anexo e o conector o lê do anexo:

1. `Artifact( action = "publish", url = <link do doc>, asset = true, file_path = <arquivo .md> )`: um arquivo de texto por chamada; devolve o id do asset.
2. `batch`: `create` do blob (`{"object":"blob","engine":"blob","payload":{"asset":"<id>"}}`) + a aba (file + node com um parágrafo provisório + pointer) + o `patch` que nomeia e aninha a aba (`subtabOf`, `order`). O blob não pode ser lido dentro do `batch`.
3. `update` isolado no node da aba: `replace` do parágrafo provisório (com `ifHash`/`ifRev` do ack) por `{"from":{"kind":"blob","id":"<id do blob>"},"as":"markdown"}`.

Para dividir um livro `.txt` por capítulo, localizar os títulos pelo texto da linha (não por número de linha: há quebras de linha mistas) e juntar as linhas quebradas em parágrafos.

## O que esta skill não faz

- Não escreve texto na voz do autor nem compõe o "Texto em andamento" da pesquisa. Isso segue com `ghost-writer` e `research`.
- Não publica nada no site: o doc é privado e os fechamentos ficam no repositório privado; só a atualização da pesquisa vai para o Scholion.

## Operacionais

- Sem `Co-Authored-By` em commit nenhum.
- O hook ghost-audit do `git commit` audita tudo o que está staged no Scholion, inclusive em commits do submódulo. Se ele travar por causa de nota alheia staged, avisar o autor; não liberar o gate por conta própria.
