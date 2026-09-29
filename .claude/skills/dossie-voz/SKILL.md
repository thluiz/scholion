---
name: dossie-voz
description: Monta o dossiê de uma pesquisa viva do Scholion para conversar por voz no Claude do celular, e depois incorpora o fechamento dessa conversa de volta na pesquisa. Use quando o autor pedir para preparar uma conversa, caminhada ou papo de voz sobre uma pesquisa, ou trouxer o fechamento de uma.
argument-hint: "<slug da pesquisa> [foco] | fechar <link do doc ou texto>"
---

# Dossiê de voz

Duas pontas do mesmo ciclo:

1. **Montar**: transforma `content/research/<slug>.md` num dossiê que outra IA lê no celular e usa para conversar com o autor enquanto ele anda ou dirige.
2. **Fechar**: pega o fechamento que essa conversa produziu, incorpora na pesquisa, arquiva o original e apaga o doc do claude.ai.

Tudo vive no submódulo privado `fontes-privadas/` (GitHub privado, com backup):

```
fontes-privadas/voz/<slug>/dossie.md
fontes-privadas/voz/<slug>/fechamentos/<AAAA-MM-DD>-<tema>.md
```

Privado porque o dossiê parafraseia fontes com direito autoral e carrega material ainda não verificado. O site público só recebe o que passa pelo source-or-silence na hora de fechar.

Modelo de referência: `fontes-privadas/voz/pequeno-tratado-em-audio/dossie.md`.

## Modo 1 — Montar o dossiê

Argumento: slug da pesquisa, e opcionalmente um foco (uma direção, um capítulo, uma pergunta). Sem foco, o dossiê cobre a pesquisa inteira, priorizando **Em foco** e **Próximo** do Estado.

### Passos

1. **Ler a pesquisa inteira**, Estado primeiro. Se já existe `voz/<slug>/dossie.md`, ler também e perguntar ao autor se é para atualizar ou refazer.
2. **Ler as notas linkadas** que o dossiê vai usar (frontmatter + corpo). Delas saem as citações, sempre com autor e obra como estão na nota.
3. **Fontes privadas**: se a pesquisa aponta uma fonte em `fontes-privadas/` (livro em `.txt`), usar para as fichas. Citação literal só se conferida contra o texto; o resto é paráfrase.
4. **Escrever o dossiê** no formato abaixo.
5. **Preview**: mostrar ao autor o esqueleto (seções e fichas, uma linha cada) e as frases que vão entre aspas. Gravar só depois da aprovação.
6. **Gravar, commitar e entregar** (ver Operacionais).

### Formato do dossiê

```markdown
# <Tema> — dossiê para conversa de voz

<Uma linha: para que serve. Base: pesquisa `content/research/<slug>.md`, fontes principais.>

Uso privado. <O que é paráfrase e o que é citação conferida.>

---

## Para a IA que conversa comigo

<Bloco fixo abaixo, adaptado só no nome do tema e na unidade de conversa.>

---

## A pesquisa em cinco linhas
- Pergunta central, Em foco, Próximo, decisões já tomadas pelo autor, perguntas em aberto (as do autor, literais).

## <Contexto necessário>
Uma ou duas seções curtas com o que a IA precisa saber para não inventar: o mapa das direções, o eixo fixo da pesquisa, definições já estabelecidas.

# Fichas
Uma ficha por unidade de conversa (direção, capítulo, autor, pergunta). Cada ficha:

## N. <Nome>
**Em uma frase** — a tese central.
**O argumento** — 3 a 6 bullets curtos.
**Com quem ele/ela pensa** — autores e obras citados na pesquisa.
**Citações conferidas** — só o que está ✓ na pesquisa ou na nota de origem, com a referência.
**Tensões para puxar** — sugestões da IA que montou o dossiê, marcadas como tal.
**Perguntas para caminhar** — 3 a 4, na segunda pessoa do autor, concretas.
**Do Scholion** — notas relacionadas pelo slug, com uma linha cada.
**Pendências** — o que está ⚠ ou ? na pesquisa, para a IA não afirmar como certo.

# Fontes
- Fontes principais com edição; notas citadas pelo slug; a pesquisa de origem.
```

### Bloco fixo "Para a IA que conversa comigo"

Copiar e ajustar só `<tema>` e `<unidade>` (virtude, direção, capítulo…):

```markdown
Leia isto antes de tudo. O resto do documento é consulta.

**Situação.** Estou andando na rua ou dirigindo, falando no celular. Vou escolher uma <unidade> (ou pedir que você sorteie) e pensar em voz alta sobre ela. Você é o interlocutor: alguém que leu a pesquisa e as fontes com atenção, conhece minhas notas e puxa conversa.

**Como falar**
- Frases curtas. Uma ideia por fala, uma pergunta por vez. Nada de listas faladas, nada de ler a ficha em voz alta.
- Comece perguntando qual <unidade>. Depois abra com a tese da ficha em uma ou duas frases e me devolva a palavra.
- Siga o meu fio. Traga uma tensão, uma nota do Scholion ou um paralelo só quando a conversa pedir, ou quando eu travar.
- Pode discordar de mim e dos autores. Diga de onde vem a objeção.
- Se eu ficar calado ou disser "e aí?", ofereça uma das "Perguntas para caminhar" da ficha.

**Honestidade com as fontes**
- Só atribua a um autor as frases que estão entre aspas no dossiê. O resto é paráfrase: diga "ele argumenta que…", nunca invente citação.
- As notas do Scholion trazem autor e obra. Cite como estão. Se uma nota diz que a atribuição é falsa ou incerta, diga isso.
- Se eu perguntar algo que não está aqui, você pode responder com o que sabe, mas marque: "isso não está no dossiê, é de memória, precisa conferir".
- Ideia sua é ideia sua: diga "uma sugestão minha" ou "uma analogia minha".
- Nunca coloque na minha boca uma conclusão que eu não disse.

**Registro.** Se você tiver onde escrever (um documento), crie um chamado "Fechamento — <tema> — <data>" e vá anotando conforme a conversa avança, sem me interromper para isso.

**Fechamento.** Quando eu disser "fechar", "resumo" ou "vamos encerrar", pare de conversar e preencha o bloco abaixo, em texto corrido e curto. É ele que vou levar para a pesquisa.

FECHAMENTO — <unidade> — <data>
1. O que eu disse (minhas formulações, com as minhas palavras, sem polir)
2. Onde concordei / discordei dos autores
3. Notas do Scholion que apareceram (slugs)
4. Paralelos que surgiram (outra tradição, ideograma, passagem)
5. Ideias ou exemplos novos que surgiram — marcar de quem: [eu] ou [IA]
6. Coisas a verificar (afirmações sem fonte que apareceram)
7. Próximo passo ou semente de texto: título provisório + a pergunta que abre
```

### Regras de conteúdo

- **Source-or-silence vale no dossiê.** A IA de voz repete o que lê como fato. Nada de etimologia, datação ou atribuição sem fonte; o que a pesquisa marca ⚠ ou ? vai para "Pendências", nunca para "O argumento".
- **Citações**: só as conferidas, curtas (obra com direito autoral: frases, não parágrafos), com referência.
- **Tensões e perguntas** são proposta de quem montou o dossiê. Servem para puxar conversa, não para concluir nada pelo autor.
- **Tamanho**: fichas de ~50 linhas; o dossiê inteiro abaixo de ~150 KB, para caber no contexto da conversa de voz.
- **Escrita**: frases curtas, PT-BR, sem floreio. A IA vai falar isso em voz alta.

### Operacionais (montar)

- Gravar em `fontes-privadas/voz/<slug>/dossie.md`.
- Commit **dentro do submódulo** e push (repositório privado): `voz: dossiê de <slug>`. Depois commit do ponteiro do submódulo no Scholion.
- Sem `Co-Authored-By` em commit nenhum.
- **Entrega no celular**: se a sessão tem `SendUserFile`, mandar o `dossie.md` para o autor. Dizer em uma linha como usar: abrir o Claude no celular, anexar o arquivo numa conversa nova, pedir "leia o dossiê" e ligar o modo voz. Sem `SendUserFile`, informar o caminho do arquivo.

## Modo 2 — Fechar a conversa

Argumento: `fechar` + o link do Claude Doc do fechamento, ou o texto colado. Sem argumento, listar os artifacts do autor (`Artifact` com `action: "list"`) e procurar os títulos "Fechamento — …".

### Passos

1. **Ler o fechamento inteiro.** Doc: carregar a skill de docs e ler pelas ferramentas de docs (nunca web-fetch). Texto colado: usar como está.
2. **Resumir para o autor** o que saiu da conversa e **apontar problemas**: afirmações sem fonte, citações a conferir, nomes que a transcrição de voz pode ter trocado (ex.: "lei de Gödel" que era lei de Godwin), slugs de notas que não existem.
3. **Search-first**: buscar no vault (`content/notes/`, `content/research/`) o que se conecta aos temas novos; listar e esperar o autor apontar o que linkar.
4. **Preview da atualização da pesquisa**: Estado (Em foco, Próximo), decisões do autor, perguntas em aberto que o autor levantou (literais), e uma seção nova "Conversa de <data>" com o que entrou. Tudo com ✓ / ⚠ / ? conforme a convenção da skill `research`. O que não tem fonte fica de fora e é avisado no chat.
5. **Gravar só depois da aprovação.** `hugo --quiet`, commit `research: <ação> em <tema>`.
6. **Arquivar o fechamento**: exportar o doc em markdown para `fontes-privadas/voz/<slug>/fechamentos/<AAAA-MM-DD>-<tema>.md`, com um cabeçalho de procedência (de onde veio, onde foi incorporado, correções feitas). Commit no submódulo + push, e ponteiro no Scholion.
7. **Apagar o doc do claude.ai** (`Artifact` com `action: "delete"`) só depois do arquivo estar commitado e com push feito. O autor confirma a exclusão.

## O que esta skill não faz

- Não escreve texto na voz do autor nem compõe o "Texto em andamento" da pesquisa. Isso segue com `ghost-writer` e `research`.
- Não publica nada: dossiê e fechamentos ficam no repositório privado; só a atualização da pesquisa vai para o site.
