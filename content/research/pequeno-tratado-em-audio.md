---
title: "Pesquisa Viva: Pequeno Tratado em Áudio de Grandes Virtudes"
date: 2026-05-08T13:58:35+01:00
summary: "Roteiro para o podcast Pequeno Tratado em Áudio de Grandes Virtudes (EN: Pocket Compendium of the Great Virtues) — série de 5-15 episódios curtos sobre as 18 virtudes do tratado de André Comte-Sponville, cruzando o vault do Scholion (estoicos, moralistas franceses, Wilde, Pascal) com pensamento oriental e Kung Fu (德 dé, 仁 ren, Lao Tzu, Confúcio)."
tags: ["pesquisa-viva", "comte-sponville", "virtudes", "etica", "filosofia-pratica", "podcast", "pequeno-tratado-em-audio"]
status: "em andamento"
toc: true
---

## Método

(Regras gerais em `.claude/skills/research/SKILL.md`. Específicas desta pesquisa:)

- **Nome desta série**: *Pequeno Tratado em Áudio de Grandes Virtudes* (PT) / *Pocket Compendium of the Great Virtues* (EN). O título PT é trocadilho direto com Comte-Sponville (*Pequeno Tratado das Grandes Virtudes*); o EN refaz a piada com o oxímoro vivo em inglês (*Pocket × Compendium*). Buscar pelo nome em qualquer idioma deve cair aqui.
- **Padrão de série (umbrella)**: futuros *Pequenos Tratados* seguem a fórmula *Pequeno Tratado de X* (PT) / *Pocket Compendium of X* (EN). O "em Áudio" deste título marca o formato e adapta-se ao suporte (vídeo, texto, etc.).
- **Crédito ao autor-pai**: cada *Pequeno Tratado* da série assume explicitamente um livro/autor de referência. Crédito ao autor-pai e à edição usada vai no episódio piloto e na descrição da web-série — neste caso, Comte-Sponville e a edição Martins Fontes 2016.
- **Destino é roteiro de áudio**, não ensaio escrito. Cada bloco de pesquisa por virtude precisa caber em 5-15 minutos de fala — sobrevoo do argumento de Comte-Sponville, 1-2 pontes para o Scholion, 1 paralelo oriental ou Kung Fu, eventualmente uma anedota.
- **Eixo paralelo fixo: 德 (dé / dak)**. Toda virtude do Comte-Sponville passa por uma pergunta: o que dela aparece (ou se desfaz) quando lida pela tradição chinesa de virtude como força-em-via?
- **Fonte primária privada**: edição Martins Fontes 2016, no submódulo `fontes-privadas/pequeno-tratado-das-grandes-virtudes.{pdf,txt}`. O site público apenas referencia. Por se tratar de obra sob direito autoral, episódios e notas extraídas paráfrasem; só citações curtas literais.
- **Conversas de voz** (skill `dossie-voz`): o Claude da web lê um Claude Doc privado com os marcos consolidados desta pesquisa (link em `fontes-privadas/voz/pequeno-tratado-em-audio/README.md`), atualizado a cada rodada; cada fechamento é exportado para `fontes-privadas/voz/pequeno-tratado-em-audio/fechamentos/<data>-<tema>.md`, incorporado aqui e apagado do claude.ai.

## Estado

- **Em foco**: episódio de abertura sobre o que é uma virtude, com a definição fechada em 2026-10-01 (7.1), a sabedoria como horizonte (8.2) e os três presentes de Agostinho como possível arquitetura da série (7.4). A série tem 21 episódios (8.1).
- **Dossiê de voz**: v1, sincronizado em 2026-10-03 (link em `fontes-privadas/voz/pequeno-tratado-em-audio/README.md`).
- **Próximo**: (a) dossiê das 18 virtudes capítulo por capítulo, com trechos citáveis (pedido do autor). (b) Dar família às virtudes que ainda não têm (7.4). (c) Desenvolver a noção de "papel". (d) A curiosidade como candidata (7.5). (e) Os `?` que restam em 5.3: estoicos, *kathékon*, tradição chinesa. (f) Curar a lista de outras virtudes pelo filtro da definição (8.3). (g) Decidir onde Weil entra: no episódio do amor ou no da humildade (9.3).
- **Pesquisas-irmãs**:
  - [discursos-protrepticos](/research/discursos-protrepticos/) — Comte-Sponville é um protréptico moderno explícito; o tratado é exercício de conversão à filosofia prática.
  - [estoicismo-lusitano](/research/estoicismo-lusitano/) — sabedoria vivida como virtude difusa, ponte para a tradição estoica que Comte-Sponville cita o tempo inteiro.
  - [amor-desinteressado-anel-brilhantes](/research/amor-desinteressado-anel-brilhantes/) — cruza diretamente com o cap. 18 (Amor).
  - [o-que-faz-a-filosofia](/research/o-que-faz-a-filosofia/) — meta.

## Motivação

Comte-Sponville propõe um catecismo laico. 18 virtudes, cada uma com sua glosa, sua história filosófica e sua ironia. O livro entrou na minha vida por volta de 2007 e ficou como referência de que virtude se pratica, não se discute.

O projeto de podcast vem da intuição oposta à do tratado: cada uma das 18 virtudes pode caber num episódio curto, falado, com a fala fazendo o que o livro faz por extenso. Áudio reduz; bem reduzido, devolve ao ouvinte espaço para praticar.

## Perguntas em aberto

(Apenas as suas. A IA propõe direções abaixo, marcadas como "a confirmar".)

- O que ocupa o lugar do "fim" numa definição de virtude como o que qualifica alguém a agir de forma adequada a um fim?
- Abrir a série com a ideia de que forma sem conteúdo é perigosa (o nazismo como êxito de uma sociedade educada) cria que problema? O risco é cair na lei de Godwin logo no primeiro episódio: a comparação com o nazismo, que numa discussão longa acaba sempre aparecendo e banaliza o argumento. Ver [godwin-law](/notes/godwin-law/).
- A virtude ancorada no papel não vira apenas boa atuação?
- A série tem um telos, ou fica sem fim último?
- A curiosidade cabe na série?

## Direções a mapear / Leituras

(A confirmar com o autor antes de aprofundar.)

### 1. Agrupamento dos episódios

Superado em 8.1: a série tem 21 episódios, um por virtude.

Três modos possíveis, não exclusivos:

- **18 episódios solo** (um por virtude, na ordem do livro). Maximalista; longo.
- **Por afinidade temática** (5-7 episódios). Ex.: temperança + prudência + simplicidade num bloco "moderação"; compaixão + misericórdia + generosidade num bloco "outro".
- **Por densidade no vault** (10-12 episódios). Virtudes com muito material no Scholion ganham solo; as com pouco se agrupam.

### 2. Mapa preliminar — as 18 virtudes × Scholion × oriental

Por capítulo do livro, com matches já existentes no vault. Marcação: ✓ conexão clara, ⚠ conexão a verificar, ∅ sem nota direta (potencial extração nova).

| # | Virtude | Scholion (notas) | Oriental / Kung Fu |
|---|---|---|---|
| 1 | Polidez | ∅ | ⚠ propedêutica/forma — paralelo com 禮 (lǐ, ritualidade confuciana) a confirmar |
| 2 | Fidelidade | [twain-loyalty-to-petrified-opinions](/notes/twain-loyalty-to-petrified-opinions/) ⚠ contraponto | ⚠ paralelo com 信 (xìn) a confirmar |
| 3 | Prudência | ∅ | ∅ |
| 4 | Temperança | [wilde-resist-everything-except-temptation](/notes/wilde-resist-everything-except-temptation/) ✓ contraponto irônico, [comer-para-viver-nao-para-prazer](/notes/comer-para-viver-nao-para-prazer/) ✓ | [preparacao-corpo-tres-vicios-capitais](/notes/preparacao-corpo-tres-vicios-capitais/) ✓ Kung Fu |
| 5 | Coragem | [spinoza-arduum-rare-difficult](/notes/spinoza-arduum-rare-difficult/) ✓, [epictetus-it-is-difficulties-that-show-what-men-are](/notes/epictetus-it-is-difficulties-that-show-what-men-are/) ✓, [epictetus-no-thing-great-created-suddenly](/notes/epictetus-no-thing-great-created-suddenly/) ✓, [aurelius-death-hangs-over-thee-be-good](/notes/aurelius-death-hangs-over-thee-be-good/) ✓, [seneca-marcet-sine-adversario-virtus](/notes/seneca-marcet-sine-adversario-virtus/) ✓ | ⚠ |
| 6 | Justiça | [pascal-plaisante-justice-pyrenees](/notes/pascal-plaisante-justice-pyrenees/) ✓, [larochefoucauld-amour-justice-crainte-injustice](/notes/larochefoucauld-amour-justice-crainte-injustice/) ✓, [voltaire-all-mortals-equal-virtue-difference](/notes/voltaire-all-mortals-equal-virtue-difference/) ⚠ | [confucius-repay-injury-with-uprightness](/notes/confucius-repay-injury-with-uprightness/) ✓ |
| 7 | Generosidade | ∅ | ⚠ um dos três tesouros em [laozi-tres-tesouros-cap-67](/notes/laozi-tres-tesouros-cap-67/) |
| 8 | Compaixão | [larochefoucauld-maux-autrui](/notes/larochefoucauld-maux-autrui/) ⚠ contraponto cínico, [sou-humano-nada-do-que-e-humano-me-e-estranho](/notes/sou-humano-nada-do-que-e-humano-me-e-estranho/) ⚠ | [confucius-zhonggong-asks-about-ren](/notes/confucius-zhonggong-asks-about-ren/) ✓ 仁, [laozi-tres-tesouros-cap-67](/notes/laozi-tres-tesouros-cap-67/) ✓ |
| 9 | Misericórdia | ∅ direta | [confucius-repay-injury-with-uprightness](/notes/confucius-repay-injury-with-uprightness/) ✓ vs [laozi-bao-yuan-yi-de-cap-63](/notes/laozi-bao-yuan-yi-de-cap-63/) ✓ — Confúcio rejeita "responder mal com virtude"; Lao Tzu propõe. Episódio nasce desse confronto. |
| 10 | Gratidão | ∅ | ∅ |
| 11 | Humildade | [confucius-three-walking-my-teachers](/notes/confucius-three-walking-my-teachers/) ✓, [confucius-transmitter-not-maker](/notes/confucius-transmitter-not-maker/) ✓, [confucius-know-what-you-know](/notes/confucius-know-what-you-know/) ✓, [aurelius-never-esteem-anything-break-self-respect](/notes/aurelius-never-esteem-anything-break-self-respect/) ⚠ | [laozi-tres-tesouros-cap-67](/notes/laozi-tres-tesouros-cap-67/) ✓, [laozi-melhor-governante-mal-se-sabe-existir-cap-17](/notes/laozi-melhor-governante-mal-se-sabe-existir-cap-17/) ✓ |
| 12 | Simplicidade | [aurelius-very-little-needed-happy-life](/notes/aurelius-very-little-needed-happy-life/) ✓ | [laozi-perder-o-tao-cap-38](/notes/laozi-perder-o-tao-cap-38/) ⚠ |
| 13 | Tolerância | ∅ | ∅ |
| 14 | Pureza | ∅ | ⚠ jade em [etimologia-de-yuk-yu-7389](/notes/etimologia-de-yuk-yu-7389/) — talvez tangente |
| 15 | Doçura | ∅ | [laozi-suprema-bondade-como-agua-cap-8](/notes/laozi-suprema-bondade-como-agua-cap-8/) ✓ |
| 16 | Boa-fé | [wilde-lying-beautiful-untrue](/notes/wilde-lying-beautiful-untrue/) ⚠ contraponto | ∅ |
| 17 | Humor | [wilde-saint-sinner-past-future](/notes/wilde-saint-sinner-past-future/) ✓, [wilde-disobedience-original-virtue](/notes/wilde-disobedience-original-virtue/) ✓, [shaw-disobedience-rarest-virtue](/notes/shaw-disobedience-rarest-virtue/) ✓, [twain-virtue-respectable-as-money](/notes/twain-virtue-respectable-as-money/) ✓ | ∅ |
| 18 | Amor | pesquisa [amor-desinteressado-anel-brilhantes](/research/amor-desinteressado-anel-brilhantes/) ✓ + várias notas Cioran | ⚠ |

### 3. Eixo meta-virtude (sobre virtude em geral)

Notas que não pertencem a uma virtude específica mas ao argumento global:

- [larochefoucauld-vertus-vices-deguises](/notes/larochefoucauld-vertus-vices-deguises/) — virtudes como vícios disfarçados.
- [larochefoucauld-hypocrisie-hommage-vice-vertu](/notes/larochefoucauld-hypocrisie-hommage-vice-vertu/) — hipocrisia como homenagem do vício à virtude.
- [montaigne-vertu-refuse-facilite](/notes/montaigne-vertu-refuse-facilite/) — virtude rejeita facilidade.
- [spinoza-pax-non-belli-privatio-virtus](/notes/spinoza-pax-non-belli-privatio-virtus/) — virtude como afirmação, não privação.
- [seneca-marcet-sine-adversario-virtus](/notes/seneca-marcet-sine-adversario-virtus/) — virtude murcha sem adversário.
- [durant-excelencia-habito](/notes/durant-excelencia-habito/) — excelência por hábito (aretē / Aristóteles via Durant).
- [voltaire-all-mortals-equal-virtue-difference](/notes/voltaire-all-mortals-equal-virtue-difference/) — virtude como única hierarquia.

### 4. Eixo oriental — 德 (dé / dak)

- [etimologia-de-dak-de](/notes/etimologia-de-dak-de/) — a palavra chinesa para virtude. O ideograma une 彳 (andar) + 直 (reto) + 心 (coração): virtude é caminho reto do coração. Glosa clássica: "外得於人內得於已也" (o que se obtém externamente nos outros e internamente em si mesmo). Eixo retórico recorrente da série.
- Vários nomes da linhagem Moy Yat carregam 德 — [moy-mo-tak](/notes/moy-mo-tak/), [moy-on-dak-wah](/notes/moy-on-dak-wah/), [moy-tan-dak](/notes/moy-tan-dak/), [moy-dak-bei](/notes/moy-dak-bei/). Cabe um episódio (ou inserção) sobre a linhagem como prática de 德.

### 5. Arquitetura da série — conversa de 2026-09-29

Conversa de voz sobre a Polidez que acabou na arquitetura da série.

#### 5.1. Decisões do autor

- **Abertura**: um episódio sobre o que é uma virtude, antes de qualquer virtude específica.
- **Polidez ganha episódio próprio.** Não é virtude do mesmo tipo que as outras dezessete: é porta de entrada. A criança finge respeito antes de senti-lo; imitando as maneiras da virtude, ganha a chance de se tornar virtuosa (paráfrase do cap. 1).
- **Par de vícios da Polidez** ⚠ formulação do autor, o livro não dá: apatia (quem nem se importa com os usos) e desrespeito ativo (o grosseiro que ofende de propósito).
- **Agrupamento Polidez + Doçura**, a confirmar. Critério: a apatia como abismo comum. O prefácio põe a doçura "entre cólera e apatia". Superado em 8.1: cada virtude tem episódio próprio.

#### 5.2. Três tipos de virtude

⚠ Hipótese do autor, candidatas ainda não conferidas capítulo a capítulo:

| Tipo | Candidatas |
|---|---|
| Porta de entrada | Polidez |
| Cumeada entre dois vícios | Prudência, Temperança, Coragem, Tolerância, Boa-fé |
| Sem par de vícios | Justiça, Compaixão, Gratidão, Amor |

Se a hipótese se sustenta, "cumeada entre dois abismos" não serve como definição única: exclui a Polidez e o Amor.

Revista em 7.6: gratidão e amor ganharam par de vícios.

#### 5.3. O que é uma virtude — mapa de definições

- **Comte-Sponville**: toda virtude é um ápice entre dois vícios, "uma cumeada entre dois abismos" (prefácio). ✓ edição Martins Fontes 2016.
- **Aristóteles**: aretê como adequação ao *ergon*, a função própria de cada coisa. ✓ ver [arete-adequacao-ao-cosmos](/notes/arete-adequacao-ao-cosmos/) (*Ética a Nicômaco* I.7).
- **Aristóteles**: virtude como meio-termo entre excesso e falta; o próprio texto exclui ações que não admitem meio (roubo, adultério, assassinato). ✓ *EN* II.6, ver 7.1.
- **Aristóteles**: virtude se forma pelo hábito. ✓ ver [durant-excelencia-habito](/notes/durant-excelencia-habito/). Sustenta o argumento da criança.
- **Tomás de Aquino**: aceita o meio-termo nas virtudes morais, mas não nas teológicas (fé, esperança, caridade). ? conferir *Suma Teológica* I-II. A definição de virtude como hábito operativo bom ✓ *ST* I-II q.55 a.3, ver 7.7.
- **Estoicos**: virtude sem graus nem meio-termo, viver conforme a natureza. ? conferir.
- **Tradição chinesa**: virtudes (仁, 義, 禮) definidas em função do 道. ? conferir; ver [etimologia-de-dak-de](/notes/etimologia-de-dak-de/).
- **Proposta do autor** ⚠: trocar "bem" por "adequado". Virtude é o que qualifica alguém a agir de forma adequada a um fim, qualquer que seja o fim. Paralelos: a aretê como adequação ao *ergon* (acima); o *kathékon* estoico, "o apropriado" (? conferir).

#### 5.4. 文/武

- Analectos 19.22, fala de Zigong, não de Confúcio: 文、武之道，未墜於地，在人 ("o caminho de Wen e Wu não caiu por terra, está nas pessoas"). ✓ [Wikisource](https://zh.wikisource.org/wiki/論語/子張第十九).
- Frase atribuída a Moy Yat, "a erudição e a marcialidade se completam". ? fonte pendente. Eixo 文/武 já mapeado em [arte-marcial](/research/arte-marcial/), direção 4.

#### 5.5. Notas que apareceram

- [etimologia-de-lai-li](/notes/etimologia-de-lai-li/) (禮)
- [vladimir-anchieta-saber-se-adaptar-ao-outro](/notes/vladimir-anchieta-saber-se-adaptar-ao-outro/)
- [moy-wu-lai](/notes/moy-wu-lai/)
- [marcio-lopes-arete-arte-da-excelencia](/notes/marcio-lopes-arete-arte-da-excelencia/)

### 6. Episódios do Vox relacionados

Levantamento por título, descrição e anotações (2026-09-29). Nenhum episódio trata do livro de Comte-Sponville.

**O que é virtude**

- [Falando nIsso 554 — Estoicismo: filosofia da crise ou disciplina machista?](https://vox.thluiz.com/2026/09/W39/estoicismo-filosofia-da-crise-ou-disciplina-machista-falando-nisso-554/) — vício e virtude com o intervalo da indiferença (*adiáphora*) entre eles; terceira estrutura, nem meio-termo nem binário simples.
- [Falando nIsso 552 — O que é liderança?](https://vox.thluiz.com/2026/09/W38/o-que-e-lideranca-falando-nisso-552/) — virtudes clássicas a partir do Sonho de Cipião: coragem, prudência, justiça, magnificência, e a graça como síntese (clemência, perdão).
- [Gregory Sadler — Stoic Philosophy and Practice: The Four Virtues](https://vox.thluiz.com/2022/03/W10/stoic-philosophy-and-practice-the-basics-the-four-virtues-gregory-sadler/) — as quatro virtudes estoicas.
- [Imposturas Filosóficas #293 — Espinosa, conatus](https://vox.thluiz.com/2025/06/W23/293-essencialmente-desejante-espinosa-conatus/) — a virtude como prêmio da própria virtude; ética do que produz alegria.
- [HoP 494 — Tell the Truth While Laughing: The French Moralists](https://vox.thluiz.com/2026/05/W22/hop-494-tell-the-truth-while-laughing-the-french-moralists/) — a virtude como máscara do amor-próprio (eixo meta-virtude, direção 3).
- [Massimo Pigliucci — Stoicism as a philosophy for an ordinary life](https://vox.thluiz.com/2018/09/W39/stoicism-as-a-philosophy-for-an-ordinary-life-massimo-pigliucci-tedxathens/) e [The struggle for the good life](https://vox.thluiz.com/2025/09/W38/the-struggle-for-the-good-life-massimo-pigliucci-on-ancient-philosophy-for-the-m/).

**Virtudes específicas**

- [Filosofia Vermelha — O estoicismo de Musônio Rufo](https://vox.thluiz.com/2025/11/W46/o-estoicismo-de-musonio-rufo/) — a alimentação como campo de batalha mais frequente da virtude (Temperança); origem de [comer-para-viver-nao-para-prazer](/notes/comer-para-viver-nao-para-prazer/).
- [Filosofia Vermelha — O verdadeiro filósofo e o charlatão](https://vox.thluiz.com/2026/04/W18/o-verdadeiro-filosofo-e-o-charlatao/) — Epicteto e os três vícios capitais (Temperança); origem de [preparacao-corpo-tres-vicios-capitais](/notes/preparacao-corpo-tres-vicios-capitais/).
- [Elefantes na Neblina #133 — Culpados](https://vox.thluiz.com/2026/09/W37/133-culpados/) — virtudes e defeitos coexistindo nas épocas pagãs; culpa e perdão (Misericórdia).
- [Popcult #31 — Um ensaio sobre The Rehearsal](https://vox.thluiz.com/2022/09/W36/31-um-ensaio-sobre-the-rehearsal-com-gregorio-duvivier-e-pedro-falcao/) — protocolos e polidez como ensaio social; *O Homem Invisível* e o comportamento sem vigilância (Polidez, forma vazia).

**Eixo chinês**

- [Filosofia Pop #113 — Pensamento Chinês, Giorgio Sinedino](https://vox.thluiz.com/2020/12/W50/113-pensamento-chines-giorgio-sinedino/) — confucionismo, taoísmo e budismo; transmissão mestre-discípulo no modelo da família.
- [História FM 172 — Três Reinos](https://vox.thluiz.com/2024/06/W26/172-tres-reinos-a-fragmentacao-do-imperio-chines/) — Confúcio como transmissor; passagem do legalismo Qin ao confucionismo Han.

### 7. O que é uma virtude: segunda conversa de voz de 2026-09-29

Conversa de voz a partir do dossiê, com o fechamento arquivado em `fontes-privadas/voz/pequeno-tratado-em-audio/fechamentos/2026-09-29-o-que-e-uma-virtude.md`. Fontes conferidas em 2026-10-01. Comte-Sponville citado pela edição Martins Fontes de 1999 (trad. Eduardo Brandão), por capítulo: o texto privado não tem a paginação do livro.

#### 7.1. Definição

Formulação do autor (2026-10-01):

> Virtude são as disposições adquiridas que capacitam a existência. Elas permitem a perseverança do que passou, a constância no presente e a semeadura do que está por vir.

Versão de trabalho da conversa, de onde a de cima saiu: disposição adquirida e estável que torna alguém capaz de agir de forma adequada ao papel ou à posição que ocupa. Amoral por escolha, sem depender de um critério de bem. O corte entre talento e virtude é o trabalho: talento é dado, virtude é conquistada.

- ⚠ Observação da IA: a formulação final troca "papel" por "existência" e distribui as três orações pelos três presentes de Agostinho (7.4). "Adquiridas" mantém o corte do trabalho. O caráter amoral e o flanco do tirano (7.2) ficam implícitos.
- Aristóteles separa arte de virtude ✓: nas artes basta a obra ser boa; nas virtudes, o agente "must have knowledge, secondly he must choose the acts, and choose them for their own sakes, and thirdly his action must proceed from a firm and unchangeable character" (*EN* II.4, c. 1105a28–33, trad. Ross). É o argumento contra parar no degrau da faca. Links: [Wikisource](<https://en.wikisource.org/wiki/Nicomachean_Ethics_(Ross)/Book_Two>).
- Definição de Aristóteles ✓: "a state of character concerned with choice, lying in a mean, i.e. the mean relative to us, this being determined by a rational principle, and by that principle by which the man of practical wisdom would determine it" (*EN* II.6, 1106b36–1107a2, trad. Ross; no grego, ἕξις προαιρετική). Há ações sem meio-termo: "adultery, theft, murder" (II.6, c. 1107a8–12). Resolve o `?` de 5.3. Links: [Wikisource](<https://en.wikisource.org/wiki/Nicomachean_Ethics_(Ross)/Book_Two>).

#### 7.2. O flanco do tirano

Decisão do autor: a definição admite, em princípio, virtude dentro do papel de tirano. O corte fica no trabalho, não no bem.

- Maquiavel recua diante de Agátocles ✓: "Non si può chiamare ancora virtù ammazzare li suoi cittadini, tradire gli amici, essere senza fede, senza pietà, senza religione; li quali modi possono far acquistare imperio, ma non gloria" (*Il Principe*, cap. VIII). Links: [Wikisource](https://it.wikisource.org/wiki/Il_Principe/Capitolo_VIII).
- Comte-Sponville diverge do autor ✓: "Das quatro virtudes cardeais, a justiça é sem dúvida a única que é absolutamente boa." A serviço do mal, prudência, temperança e coragem "não seriam virtudes, mas simples talentos ou qualidades do espírito ou do temperamento, como diz Kant" (cap. A justiça).
- Nietzsche ✓: "nicht Tugend, sondern Tüchtigkeit (Tugend im Renaissance-Stile, virtù, moralinfreie Tugend)" (*Der Antichrist* §2). Links: [eKGWB](http://www.nietzschesource.org/#eKGWB/AC-2).

#### 7.3. O amor, cume da atenção

Decisão do autor (2026-10-01): o amor é a virtude-cume da família da atenção. Na conversa chegou a ficar fora da definição, tratado como fim (dois amores-fim, caridade e poder, além do bem e do mal no sentido de Nietzsche); essa posição foi deixada.

- Dois abismos: a indiferença, que nem olha o outro; a paixão ou posse, que olha o tempo todo e vê o próprio desejo projetado. No meio, a atenção que vê o outro como real.
- Os três amores ✓: Comte-Sponville divide o capítulo do amor em três seções, "Eros", "Philia" e "Agapé" (cap. O amor). ⚠ Na conversa, a IA leu éros como cumeada, entre indiferença e obsessão, e ágape como o amor sem abismo de excesso.
- Simone Weil ✓: "L'attention est la forme la plus rare et la plus pure de la générosité", carta a Joë Bousquet, 13 de abril de 1942 (*Correspondance*, Lausanne, L'Âge d'Homme, 1982, p. 18; a página só por Wikiquote). Já no Scholion: [attention-as-the-purest-form-of-generosity](/notes/attention-as-the-purest-form-of-generosity). Links: [Wikiquote](https://en.wikiquote.org/wiki/Simone_Weil).
- Weil ✓: "L'attention consiste à suspendre sa pensée, à la laisser disponible, vide et pénétrable à l'objet" e "La plénitude de l'amour du prochain, c'est simplement d'être capable de lui demander : « Quel est ton tourment ? »" ("Réflexions sur le bon usage des études scolaires en vue de l'amour de Dieu", em *Attente de Dieu*, Paris, Fayard, 1966). Ver [genuine-attention-clearing-space-not-forcing-will](/notes/genuine-attention-clearing-space-not-forcing-will). Links: [Classiques des sciences sociales](https://classiques.uqam.ca/classiques/weil_simone/attente_de_dieu/attente_de_dieu_1966.pdf).
- Spinoza ✓: "From the third kind of knowledge necessarily arises the intellectual love of God" (*Ética* V, prop. 32, cor., trad. Elwes). ⚠ Chamar isso de atenção é ponte da IA, não termo de Spinoza. Ver [spinoza-amor-erga-rem-aeternam-laetitia](/notes/spinoza-amor-erga-rem-aeternam-laetitia) e [spinoza-felicitas-quality-object-love](/notes/spinoza-felicitas-quality-object-love). Links: [Gutenberg](https://www.gutenberg.org/cache/epub/3800/pg3800.txt).
- Comte-Sponville ✓: "Na medida em que a virtude é um esforço – sempre o é, fora a graça ou o amor -, toda virtude é coragem" (cap. A coragem). No último capítulo cita Agostinho: "A melhor e mais curta definição da virtude [...] é esta: a ordem do amor" (cap. O amor).
- Tomás de Aquino ✓: "virtus dicitur ordo vel ordinatio amoris" (*ST* I-II q.55 a.1 ad 4). A objeção a que responde atribui a Agostinho, *De moribus Ecclesiae*, "virtus est ordo amoris". Links: [Corpus Thomisticum](https://www.corpusthomisticum.org/sth2055.html).

#### 7.4. Os três presentes

Ideia do autor: a memória e o tempo separam famílias de virtudes.

- Agostinho ✓: "tempora sunt tria, praesens de praeteritis, praesens de praesentibus, praesens de futuris [...] praesens de praeteritis memoria, praesens de praesentibus contuitus, praesens de futuris expectatio" (*Confissões* XI.20.26). Ver [tempo-em-agostinho](/notes/tempo-em-agostinho). Links: [The Latin Library](https://www.thelatinlibrary.com/augustine/conf11.shtml).
- Comte-Sponville já usa o eixo ✓: "Como o corpo é o presente do presente, o espírito é o presente do passado [...] É o que santo Agostinho chamava de 'presente do passado', e é isso a memória" (cap. A fidelidade). A prudência é "virtude presente, pois, como toda virtude, mas previsora ou antecipadora" (cap. A prudência). Na coragem, o presente é "uma distensão, como dizia santo Agostinho" (cap. A coragem).

| Família | Presente | Virtudes |
|---|---|---|
| Memória | do passado | fidelidade, gratidão, misericórdia, humildade |
| Atenção | do presente | simplicidade, pureza, tolerância, humor; amor como cume |
| Espera | do futuro | coragem, generosidade, esperança |

A atenção é o chão da família do presente, não uma virtude a mais (9.2).

⚠ Distribuição proposta na conversa, não fechada. A esperança não está entre as 18. Polidez, prudência, temperança, justiça, compaixão, doçura e boa-fé ainda sem família.

#### 7.5. Método: a definição como filtro

Decisão do autor: abordar candidatas a virtude, testá-las contra a definição e decidir no fim quais ficam. A discussão de cortar uma candidata pode virar episódio. Vale para as 18 de Comte-Sponville e para candidatas novas. Primeira candidata nova: a curiosidade.

#### 7.6. Teste das 18

Critérios da versão de trabalho: disposição adquirida, estável, adequada ao papel, separável do talento pelo trabalho. Revê a tabela de 5.2: gratidão e amor ganharam par de vícios.

| Virtude | Teste | Formulação | Cumeada |
|---|---|---|---|
| Polidez | passa | gesto adequado à convivência, sem exigir sentimento | — |
| Fidelidade | passa | manter o prometido contra a tentação de largar | — |
| Prudência | passa | a virtude que calcula o adequado | — |
| Temperança | passa | cumeada clássica | — |
| Coragem | passa | disposição firme conquistada por hábito | covardia / temeridade |
| Generosidade | passa | dar contra o egoísmo natural | — |
| Compaixão | passa | [autor] exige esforço, é mais fácil virar o rosto | — |
| Justiça | passa | [autor] aplicação constante do critério aceito, sempre circunstancial | — |
| Misericórdia | força | ⚠ soltar a ofensa sem esquecer que houve falta | [autor] rancor, memória que vira arma / complacência, memória traída |
| Gratidão | passa | [autor] fidelidade ao que se recebeu, de quem quer que venha | [autor] dívida / devoção |
| Humildade | força | [autor] lembra a própria posição e facilita o papel | [autor] vaidade / rebaixamento |
| Simplicidade | quase quebra | ⚠ o trabalho é parar de fazer: soltar o personagem | — |
| Tolerância | passa | conviver com o critério alheio | fanatismo / indiferença |
| Pureza | passa | [autor] entregar a coisa na coisa em si, nem mais nem menos | [autor] mistura / purismo |
| Doçura | passa | [autor] a força que poderia ferir e escolhe não ferir | [autor] brutalidade / moleza |
| Boa-fé | passa | não mentir, sobretudo para si | mentira / franqueza brutal |
| Humor | passa | rir de si | [autor] solene / gozador |
| Amor | cume da atenção | ver o outro como real | indiferença / posse |

Por virtude:

- **Fidelidade**: Nietzsche ✓, "Ein Thier heranzüchten, das versprechen darf" e "ein eigentliches Gedächtniss des Willens" (*Genealogia da moral* II §1). Links: [eKGWB](http://www.nietzschesource.org/#eKGWB/GM-II-1).
- **Justiça**: [autor] o reformador aponta um critério novo, vindo de outra coisa (a compaixão, ou até o interesse econômico). Comte-Sponville ✓: "A justiça se diz em dois sentidos: como conformidade ao direito (jus, em latim) e como igualdade ou proporção" (cap. A justiça). Perelman ✓, justiça formal, *De la justice*, Bruxelas, Office de publicité, 1945; a fórmula francesa da regra de justiça segue sem conferência. Abolição britânica ✓: Eric Williams, *Capitalism and Slavery* (Chapel Hill, UNC Press, 1944), contestado por Seymour Drescher, *Econocide* (Pittsburgh, University of Pittsburgh Press, 1977). Links: [Persée](https://www.persee.fr/doc/phlou_0035-3841_1946_num_44_1_4047_t1_0183_0000_3), [Open Library](https://openlibrary.org/works/OL1954987W/Econocide).
- **Misericórdia**: Comte-Sponville ✓, "Ela não abole a falta mas o rancor, não a lembrança mas a cólera, não o combate mas o ódio" (cap. A misericórdia). Ricœur ✓, epílogo "Le pardon difficile" de *La mémoire, l'histoire, l'oubli* (Paris, Seuil, 2000). Ver [larochefoucauld-pardon-ennui](/notes/larochefoucauld-pardon-ennui) e [forgive-enemies-nothing-annoys](/notes/forgive-enemies-nothing-annoys). Links: [Persée](https://www.persee.fr/doc/thlou_0080-2654_2001_num_32_2_3151).
- **Gratidão**: [autor] ciclo entre iguais; um pai pode ser grato ao filho. Mauss ✓, "l'obligation de donner, l'obligation de recevoir et l'obligation de rendre" (*Essai sur le don*, *L'Année sociologique*, 1923-1924; cap. II, §III). Ver [mauss-ensaio-dadiva-dar-receber-retribuir](/notes/mauss-ensaio-dadiva-dar-receber-retribuir). Sêneca ✓, "Quaeritur enim, an aliquando liberi maiora beneficia dare parentibus suis possint, quam acceperint" (*De Beneficiis* III.29); a resposta afirmativa corre até III.38. Links: [Classiques des sciences sociales](https://classiques.uqam.ca/classiques/mauss_marcel/socio_et_anthropo/2_essai_sur_le_don/essai_sur_le_don.pdf), [The Latin Library](https://www.thelatinlibrary.com/sen/ben3.shtml).
- **Humildade**: Comte-Sponville ✓, "É a virtude do homem que sabe não ser Deus" (cap. A humildade). Hume ✓ a recusa: "Celibacy, fasting, penance, mortification, self-denial, humility, silence, solitude, and the whole train of monkish virtues; for what reason are they every where rejected by men of sense, but because they serve to no manner of purpose" (*Enquiry Concerning the Principles of Morals* IX.1, M 9.3). Aristóteles ✓: "The man who thinks himself worthy of less than he is really worthy of is unduly humble" (*EN* IV.3, c. 1123b8–11, trad. Ross); a medida certa de si é a magnanimidade. Spinoza ✓: "Humility is pain arising from a man's contemplation of his own weakness of body or mind" (*Ética* III, def. dos afetos 26) e "Humility is not a virtue, or does not arise from reason" (IV, prop. 53). Ver [marcio-lopes-arete-arte-da-excelencia](/notes/marcio-lopes-arete-arte-da-excelencia) e [arete-adequacao-ao-cosmos](/notes/arete-adequacao-ao-cosmos). Links: [davidhume.org](https://davidhume.org/texts/m/9), [Wikisource](<https://en.wikisource.org/wiki/Nicomachean_Ethics_(Ross)/Book_Four>).
- **Boa-fé**: [autor] quatro figuras: o mentiroso esconde a verdade, o de má-fé se ilude, o cínico despreza a verdade, o canalha finge a verdade. Comte-Sponville ✓ escolheu "boa-fé" depois de pensar em sinceridade, veracidade e autenticidade; define-a como "uma sinceridade ao mesmo tempo transitiva e reflexiva" (cap. A boa-fé). Sartre ✓, a má-fé como mentira a si mesmo, *L'Être et le néant* (1943), parte I, cap. 2. Links: [IEP](https://iep.utm.edu/sartre-ex/).
- **Humor**: Comte-Sponville ✓, "A ironia ri do outro (ou do eu, na autoderrisão, como de um outro); o humor ri de si" e "A ironia é humilhante; o humor é humilde" (cap. O humor).

#### 7.7. Ética das virtudes moderna (conferido em 2026-10-01)

- Anscombe ✓, "Modern Moral Philosophy", *Philosophy* 33, nº 124, 1958, pp. 1–19. Três teses: não fazer filosofia moral "until we have an adequate philosophy of psychology"; obrigação, dever e o "deve" moral "ought to be jettisoned"; as diferenças entre os ingleses desde Sidgwick "are of little importance". Cunhou o termo: "consequentialism, as I name it". Links: [SEP](https://plato.stanford.edu/entries/anscombe/).
- Foot ✓, *Natural Goodness*, Oxford, 2001: a bondade moral como "natural normativity in its application to human beings". Links: [SEP](https://plato.stanford.edu/entries/philippa-foot/).
- Hursthouse ✓, *On Virtue Ethics*, Oxford, 1999: "An action is right iff it is what a virtuous agent would characteristically (i.e. acting in character) do in the circumstances". A p. 28 vem só da literatura secundária.
- Harman ✓, "Moral Philosophy Meets Social Psychology", *Proc. Aristotelian Society* 99, 1999, pp. 315–331; "The Nonexistence of Character Traits", *idem* 100, 2000, pp. 223–226. Links: [SEP](https://plato.stanford.edu/entries/moral-character-empirical/).
- Doris ✓, "Persons, Situations, and Virtue Ethics", *Noûs* 32, 1998; *Lack of Character*, Cambridge, 2002. Corrige o fechamento: Doris diz que "people typically lack character" (1998, p. 506) e aceita traços locais; a raridade é resposta dos defensores da ética das virtudes. Links: [SEP](https://plato.stanford.edu/entries/moral-character-empirical/).
- Sosa ✓, "The Raft and the Pyramid", *Midwest Studies in Philosophy* 5, 1980; *A Virtue Epistemology*, Oxford, 2007: modelo AAA, desempenho apto é "accurate because adroit". O arqueiro aparece na resenha de Ram Neta. Links: [SEP](https://plato.stanford.edu/entries/epistemology-virtue/), [NDPR](https://ndpr.nd.edu/reviews/a-virtue-epistemology-apt-belief-and-reflective-knowledge-volume-1/).
- Zagzebski ✓, *Virtues of the Mind*, Cambridge, 1996, p. 137: "a deep and enduring acquired excellence of a person, involving a characteristic motivation to produce a certain desired end and reliable success in bringing about that end". A faca tem o sucesso, não a motivação. Links: [IEP](https://iep.utm.edu/virtue-epistemology/).
- Tomás ✓: "virtus humana, quae est habitus operativus, est bonus habitus, et boni operativus" (*ST* I-II q.55 a.3). A fórmula *habitus operativus bonus* é resumo de comentadores. A definição "bona qualitas mentis, qua recte vivitur..." (q.55 a.4) é, nas palavras de Tomás, colhida de Agostinho ("ex cuius verbis praedicta definitio colligitur"); Pedro Lombardo a registra em *Sentenças* II d.27 c.5. Links: [Corpus Thomisticum](https://www.corpusthomisticum.org/sth2055.html), [Franciscan Archive](https://www.franciscan-archive.org/lombardus/II-Sent.html).
- Platão ✓, *Protágoras* 329d (as partes da virtude como as do rosto ou como pedaços de ouro) e 361b (se a virtude é conhecimento, pode ser ensinada). Tese socrática discutida no diálogo, não doutrina fechada. Links: [Perseus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Prot.:section=329d).

### 8. Outras virtudes e estrutura da série: conversa de voz de 2026-10-02

Fechamento arquivado em `fontes-privadas/voz/pequeno-tratado-em-audio/fechamentos/2026-10-02-outras-virtudes.md`. Fontes conferidas em 2026-10-02.

#### 8.1. Estrutura da série

Decisão do autor: 21 episódios. A abertura sobre o que é uma virtude; 18 episódios, um por virtude de Comte-Sponville, na ordem do livro; um episódio sobre outras virtudes; um encerramento.

- Comte-Sponville sobre a ordem ✓: "O fato de este conjunto começar pela polidez, que ainda não é moral, e terminar pelo amor, que não o é mais, obviamente é deliberado" (Preâmbulo).

#### 8.2. A sabedoria como horizonte

Posição do autor: a sabedoria não é uma virtude entre as outras, mas o fim para onde elas apontam. Entra na abertura, como horizonte da série. Responde em parte à pergunta sobre o telos. Decisão do autor (2026-10-02): a sabedoria também entra na lista de candidatas de 8.3, para o episódio de outras virtudes discutir por que ela fica acima das virtudes.

- Comte-Sponville separa prudência e sabedoria ✓: "A phronésis é como que uma sabedoria prática, sabedoria da ação, para a ação, na ação. No entanto, ela não faz as vezes de sabedoria (de verdadeira sabedoria: Sophia), porque tampouco basta agir bem para viver bem, ou ser virtuoso para ser feliz" (cap. A prudência). `?` Que Comte-Sponville trate a sabedoria como fim das virtudes não aparece no *Tratado*.
- Spinoza ✓, contra a esperança e a favor da razão: "the more we endeavour to be guided by reason, the less do we depend on hope; we endeavour to free ourselves from fear, and, as far as we can, to dominate fortune, directing our actions by the sure counsels of wisdom" (*Ética* IV, prop. 47, nota, trad. Elwes). Links: [Gutenberg](https://www.gutenberg.org/cache/epub/3800/pg3800.txt).

#### 8.3. O que ficou de fora

Critério de Comte-Sponville ✓: "Perguntei-me quais eram as disposições de coração, natureza ou caráter cuja presença, num indivíduo, aumentava a estima moral que eu tinha por ele e cuja ausência, ao contrário, a diminuía. Isso proporcionou uma lista de cerca de trinta virtudes." Saíram as redundantes, "por exemplo, bondade e generosidade, ou honestidade e justiça", e as que não lhe pareceram indispensáveis: "Restaram dezoito" (Preâmbulo).

Candidatas, todas aceitas pelo autor para a lista, a passar pelo filtro da definição (7.5):

- **Sugeridas pela mãe do autor**: o autocontrole, o controle das emoções como o que nos afasta do animal, e a elegância. O autor lê o autocontrole como racionalidade. [autor] A elegância vem de eleger: tem a ver com as escolhas que a pessoa tem que fazer.
- **Do autor**: a sabedoria (8.2).
- **Propostas da IA, ocidentais**: esperança, paciência, curiosidade, magnanimidade, serenidade, discrição, constância; autossuficiência (*autarkeia* estoica), amizade (Aristóteles), honestidade intelectual (Nietzsche), benevolência (Hume), responsabilidade (Hans Jonas).
- **Propostas da IA, outras tradições**: piedade filial, não-agir, harmonia, não-violência, equanimidade ou desapego, hospitalidade, reciprocidade, custódia da terra, ubuntu, responsabilidade intergeracional.

⚠ Sobreposições apontadas pela IA, para a curadoria: amizade e philia; benevolência e 仁; paciência e *ṣabr*; serenidade e *ḥilm*; autocontrole e temperança; honestidade intelectual e boa-fé; responsabilidade e responsabilidade intergeracional; magnanimidade e a humildade em Aristóteles (7.6). A constância já está na definição ("a constância no presente") e pode ser menos uma virtude a mais do que um traço de todas.

Título provisório sugerido pela IA: "O que ficou de fora". Pergunta que abre: por que estas 18, e não outras?

#### 8.4. Fontes das candidatas

- **Elegância** ✓: "from Latin elegantem (nominative elegans) "choice, fine, tasteful," collateral form of present participle of eligere "select with care, choose"" ([etymonline](https://www.etymonline.com/word/elegant)). O Wiktionary passa por um verbo não atestado, *ēlegāre*, "probably" de *ēligō* ([Wiktionary](https://en.wiktionary.org/wiki/elegans)). Ver [cioran-skepticism-elegance-anxiety](/notes/cioran-skepticism-elegance-anxiety) e [cioran-pas-elegant-dabuser-malchance](/notes/cioran-pas-elegant-dabuser-malchance).
- **Autocontrole**: ver [epictetus-no-man-is-free-master-of-himself-misattributed](/notes/epictetus-no-man-is-free-master-of-himself-misattributed), frase de atribuição falsa a Epicteto.
- **Esperança** ✓: Spinoza, "Hope is an inconstant pleasure, arising from the idea of something past or future, whereof we to a certain extent doubt the issue" e "there is no hope unmingled with fear, and no fear unmingled with hope" (*Ética* III, def. dos afetos 12 e 13 e explicação); "Emotions of hope and fear cannot be in themselves good" (IV, prop. 47). Comte-Sponville, na descrição editorial de *Le bonheur, désespérément* (Librio, 2003): "nous sommes séparés du bonheur par l'espérance même qui le poursuit". `?` Por que fé e esperança ficaram fora do *Tratado*. Ver [camus-esperanca-suicidio-filosofico](/notes/camus-esperanca-suicidio-filosofico).
- **Benevolência** ✓: Hume, "The epithets sociable, good-natured, humane, merciful, grateful, friendly, generous, beneficent, or their equivalents, are known in all languages, and universally express the highest merit, which human nature is capable of attaining" (*Enquiry Concerning the Principles of Morals* II, M 2.1). Links: [davidhume.org](https://davidhume.org/texts/m/2).
- **Honestidade intelectual** ✓: Nietzsche, "Redlichkeit, gesetzt, dass dies unsre Tugend ist, von der wir nicht loskönnen, wir freien Geister" (*Além do bem e do mal* §227). Links: [eKGWB](http://www.nietzschesource.org/#eKGWB/JGB-227).
- **Responsabilidade** ✓: Hans Jonas, *Das Prinzip Verantwortung* (1979); *The Imperative of Responsibility* (Chicago, University of Chicago Press, 1984). `?` A formulação literal do imperativo. Links: [University of Chicago Press](https://press.uchicago.edu/ucp/books/book/chicago/I/bo5953283.html).
- **Amizade**: Comte-Sponville trata a *philia* numa das três seções do capítulo do amor ✓ (7.3).
- **Serenidade**: ver [etimologia-de-jing-jing-975c](/notes/etimologia-de-jing-jing-975c) (靜).
- **Tradição chinesa** ✓ ([MDBG](https://www.mdbg.net/chinese/dictionary), [SEP, Confucius](https://plato.stanford.edu/entries/confucius/), [SEP, Daoism](https://plato.stanford.edu/entries/daoism/)): 仁 *rén*, humanidade, benevolência ([confucius-without-ren-cannot-endure](/notes/confucius-without-ren-cannot-endure)); 禮 *lǐ*, rito, propriedade ([etimologia-de-lai-li](/notes/etimologia-de-lai-li)); 義 *yì*, retidão ([confucius-gentleman-understands-rightness](/notes/confucius-gentleman-understands-rightness)); 孝 *xiào*, piedade filial; 智 *zhì*, sabedoria; 無為 *wúwéi*, "the Daoist doctrine of inaction" ([laozi-aprender-perder-cap-48](/notes/laozi-aprender-perder-cap-48)); 德 *dé*, "virtuosity" na tradução da SEP ([etimologia-de-dak-de](/notes/etimologia-de-dak-de)). ⚠ O 禮 conversa com a elegância, além da polidez (observação da IA).
- **Tradição indiana** ✓ ([wisdomlib](https://www.wisdomlib.org/)): *ahiṃsā*, não-violência, "abstaining from killing or giving pain to others in thought, word or deed"; *dharma*, "religious or moral merit, virtue, righteousness"; *satya*, veracidade; *dāna*, "Giving, liberality"; *karuṇā*, compaixão. O desapego budista aparece como *upekkhā*, "Equanimity"; na tradição hindu, *vairāgya*, "dispassion, detachment, or renunciation".
- **Tradição islâmica**: *ṣabr* (paciência) e *tawakkul* (confiança em Deus) estão entre as estações sufis listadas por Abū Naṣr al-Sarrāj ✓ ([St Andrews Encyclopaedia of Theology, "Sufism"](https://www.saet.ac.uk/Islam/Sufism)). ⚠ *ḥilm* (paciência, autodomínio) só com fonte não acadêmica. `?` *ʿadl* (justiça) e *karam* (generosidade, hospitalidade) sem fonte acadêmica conferida.
- **Haudenosaunee** ✓, com correção: a Grande Lei pede ter sempre em vista "not only the present but also the coming generations, even those whose faces are yet beneath the surface of the ground -- the unborn of the future Nation" (§28, [constitution.org](https://www.constitution.org/1-Constitution/cons/iroquois.htm)). A expressão "sétima geração" não está no texto escrito; a Confederação a apresenta como valor central ([Haudenosaunee Confederacy](https://www.haudenosauneeconfederacy.com/values/)).
- **Ayni** ✓: "Ayni, or reciprocity, historically characterizes Quechua culture as a fundamental aspect of ancient Andean societies" (Curran, Ursinus College, 2020, [Digital Commons](https://digitalcommons.ursinus.edu/spanish_hon/3/)).
- **Caring for country** ✓: "'Caring for country' means participating in interrelated activities on Aboriginal lands and seas with the objective of promoting ecological, spiritual and human health" (Burgess et al., *Medical Journal of Australia* 190, 2009, [MJA](https://www.mja.com.au/journal/2009/190/10/healthy-country-healthy-people-relationship-between-indigenous-health-status)).
- **Ubuntu** ✓: o provérbio nguni "umuntu ngumuntu ngabantu", uma pessoa é pessoa por meio das outras; a frase "I am, because we are; and since we are, therefore I am" é de John Mbiti (*African Religions and Philosophy*, 2. ed., 1990, p. 106), que não fala de ubuntu: a ligação é posterior ([HTS Teologiese Studies, 2024](https://scielo.org.za/scielo.php?script=sci_arttext&pid=S0259-94222024000100009)).

#### 8.5. Polidez: achado

- Nietzsche ✓: "Die guten Vier. — Redlich gegen uns und was sonst uns Freund ist; tapfer gegen den Feind; grossmüthig gegen den Besiegten; höflich — immer: so wollen uns die vier Cardinaltugenden" (*Aurora* §556). A cortesia entra entre as quatro virtudes cardeais. Links: [eKGWB](http://www.nietzschesource.org/#eKGWB/M-556).

### 9. Simone Weil e a atenção: conversa de voz de 2026-10-02

Fechamento arquivado em `fontes-privadas/voz/pequeno-tratado-em-audio/fechamentos/2026-10-02-weil-atencao.md`. Passagens conferidas nas "Réflexions sur le bon usage des études scolaires en vue de l'amour de Dieu", em *Attente de Dieu* (Fayard, 1966), na paginação do PDF dos Classiques des sciences sociales, pp. 67-75 ([UQAM](https://classiques.uqam.ca/classiques/weil_simone/attente_de_dieu/attente_de_dieu_1966.pdf)).

#### 9.1. O que chamou a atenção do autor

- [autor] "atenção ser suspender o pensamento". Depois de ler o conceito no texto: "estou achando difícil encaixar isso. mas gosto dessa leitura de atenção".
- Weil ✓: "L'attention est un effort, le plus grand des efforts peut-être, mais c'est un effort négatif. Par lui-même il ne comporte pas la fatigue" (pp. 71-72).
- ⚠ Paradoxo apontado pela IA: a definição pede disposição adquirida pelo trabalho, e o trabalho da atenção é parar. Mesmo problema da simplicidade (7.6).

#### 9.2. A atenção como chão da família do presente

- ⚠ Proposta da IA, aceita pelo autor ("alivia"): a atenção não precisa entrar como virtude. É o chão da família do presente, o *contuitus* de Agostinho (7.4), num lugar parecido com o da sabedoria (8.2).
- Weil ✓: "Bien qu'aujourd'hui on semble l'ignorer, la formation de la faculté d'attention est le but véritable et presque l'unique intérêt des études" (p. 67).
- Weil ✓: "La clef d'une conception chrétienne des études, c'est que la prière est faite d'attention" (p. 67).

#### 9.3. O que o ensaio toca no dossiê

- **Humildade** ✓: "s'astreindre rigoureusement à regarder en face, à contempler avec attention, pendant longtemps, chaque exercice scolaire manqué, dans toute la laideur de sa médiocrité, sans se chercher aucune excuse"; "Surtout la vertu d'humilité, trésor infiniment plus précieux que tout progrès scolaire, peut être acquise ainsi" (p. 70).
- **Talento e virtude** ✓: o esforço muscular, alunos que "froncer les sourcils, retenir la respiration, contracter les muscles"; estudos que dão boas notas "malgré l'effort et grâce aux dons naturels" (pp. 70-71).
- **Vontade e desejo** ✓: a vontade "n'a presque aucune place dans l'étude. L'intelligence ne peut être menée que par le désir" (p. 71).
- **Nenhum esforço se perde** ✓: "Jamais, en aucun cas, aucun effort d'attention véritable n'est perdu" (p. 68).
- **Esperar em vez de buscar** ✓: os erros vêm "de ce que la pensée s'est précipitée hâtivement sur quelque chose [...] La cause est toujours qu'on a voulu être actif ; on a voulu chercher" (p. 72); "Les biens les plus précieux ne doivent pas être cherchés, mais attendus" (pp. 72-73); o homem na montanha que vê "beaucoup de forêts et de plaines" sem olhar para elas (p. 72).
- **Amor ao próximo** ✓: o infeliz existe "non pas comme unité dans une collection [...] mais en tant qu'homme, exactement semblable à nous"; o olhar em que "l'âme se vide de tout contenu propre pour recevoir en elle-même l'être qu'elle regarde tel qu'il est" (pp. 74-75). Ver [weil-quel-est-ton-tourment](/notes/weil-quel-est-ton-tourment/).
- Fio aberto pelo autor: Weil cabe no episódio do amor, mas também toca a humildade (família da memória), pelo encarar o próprio erro. O autor encerrou antes de decidir.
- Título provisório sugerido pela IA: "Esperar em vez de buscar". Pergunta: prestar atenção é fazer força ou parar de fazer?
- `?` Em *A gravidade e a graça*, a atenção pura como oração: de memória, não conferido.
- Ver [weil-attention-suspendre-sa-pensee](/notes/weil-attention-suspendre-sa-pensee/), [attention-as-the-purest-form-of-generosity](/notes/attention-as-the-purest-form-of-generosity/), [genuine-attention-clearing-space-not-forcing-will](/notes/genuine-attention-clearing-space-not-forcing-will/), [tempo-em-agostinho](/notes/tempo-em-agostinho/); para a humildade, [aristoteles-magnanimidade-unduly-humble](/notes/aristoteles-magnanimidade-unduly-humble/), [spinoza-humility-is-not-a-virtue](/notes/spinoza-humility-is-not-a-virtue/), [hume-monkish-virtues](/notes/hume-monkish-virtues/); outras de Weil, [democracia-sem-partido](/notes/democracia-sem-partido/) e [porque-a-historia-das-mortes-dos-filosofos](/notes/porque-a-historia-das-mortes-dos-filosofos/).

## Notas extraídas

Citações conferidas na pesquisa, extraídas em 2026-10-02:

- [maquiavel-agatocles-imperio-nao-gloria](/notes/maquiavel-agatocles-imperio-nao-gloria/): Agátocles e a *virtù* que não dá glória (7.2).
- [nietzsche-moralinfreie-tugend](/notes/nietzsche-moralinfreie-tugend/): virtude livre de moralina (7.2).
- [aristoteles-arte-virtude-tres-condicoes](/notes/aristoteles-arte-virtude-tres-condicoes/): *EN* II.4, arte e virtude (7.1).
- [aristoteles-definicao-virtude-meio-termo](/notes/aristoteles-definicao-virtude-meio-termo/): *EN* II.6, a definição (7.1).
- [aristoteles-magnanimidade-unduly-humble](/notes/aristoteles-magnanimidade-unduly-humble/): *EN* IV.3, magnanimidade e humildade (7.6).
- [hume-monkish-virtues](/notes/hume-monkish-virtues/): as virtudes monásticas (7.6).
- [spinoza-humility-is-not-a-virtue](/notes/spinoza-humility-is-not-a-virtue/): *Ética* IV, prop. 53 (7.6).
- [seneca-filho-supera-pai-beneficios](/notes/seneca-filho-supera-pai-beneficios/): *De Beneficiis* III, gratidão (7.6).
- [nietzsche-thier-versprechen-darf](/notes/nietzsche-thier-versprechen-darf/): o animal que pode prometer, fidelidade (7.6).
- [weil-quel-est-ton-tourment](/notes/weil-quel-est-ton-tourment/): "Quel est ton tourment ?" (7.3).
- [weil-attention-suspendre-sa-pensee](/notes/weil-attention-suspendre-sa-pensee/): a atenção que suspende o pensamento (7.3).
- [aquino-virtus-ordo-amoris](/notes/aquino-virtus-ordo-amoris/): a virtude como ordem do amor (7.3).
- [anscombe-modern-moral-philosophy](/notes/anscombe-modern-moral-philosophy/): as três teses de 1958 (7.7).
- [zagzebski-virtude-excelencia-adquirida](/notes/zagzebski-virtude-excelencia-adquirida/): a virtude como excelência adquirida (7.7).
