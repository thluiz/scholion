---
title: "Pesquisa Viva: A Characteristica Universalis de Leibniz e os Vetores"
date: 2026-06-16T14:58:39+01:00
summary: "Até onde Leibniz chegou com a characteristica universalis, e até onde um LLM, na prática, realiza o que ele almejava? Ele foi um visionário a quem só faltava poder computacional, ou o projeto era de outra natureza?"
tags: ["pesquisa-viva", "leibniz", "filosofia-da-linguagem", "llm", "lingua-universal", "representacao"]
status: "em andamento"
toc: true
---

## Método (específico)

Regras gerais aplicadas: ver `.claude/skills/research/SKILL.md`.

- **Duas frentes que têm de se encontrar.** De um lado, reconstruir o que Leibniz de fato propôs e até onde levou (a *characteristica universalis* e o *calculus ratiocinator*). Do outro, entender como um modelo de linguagem funciona na prática (tokens, vetores, atenção, previsão do próximo passo). A pesquisa só vale quando as duas frentes se cruzam: medir a distância entre o projeto e o mecanismo.
- **A pergunta-crux:** Leibniz foi um visionário a quem faltou apenas poder computacional, ou o que ele queria era de outra natureza do que um LLM entrega? Não decidir cedo. Mapear os dois lados e deixar a resposta emergir.
- **Continuidade na forma, não no todo.** A hipótese é que o embedding realiza *a forma* do sonho leibniziano — ideia como ponto, raciocínio como cálculo, representação independente da língua natural. A posição do autor (ver Motivação) é que essa realização é sempre aproximação: o modelo não é o mundo. As duas coisas convivem; a continuidade formal não anula o resíduo inexprimível.
- **Bibliografia provisória.** Tudo marcado ⚠ é reconstruído de memória e será verificado quando a direção for exaurida. ✓ marca o que já foi conferido contra fonte nesta sessão.
- Pesquisa-irmã: [pensamento-linguagem-filosofia](/research/pensamento-linguagem-filosofia), onde Leibniz fica apenas tangenciado, no eixo universalista (o pensamento precede a língua). Aqui o recorte é a engenharia da representação e a comparação com o mecanismo real dos LLMs.

## Estado

- **Em foco**: direção 1 (Leibniz primário). Base da *characteristica* conferida em 1ª passagem contra a Wikipedia EN — ideografia que representa ideias e não palavras, par com o *calculus ratiocinator*, "alfabeto do pensamento humano" por combinação de signos simples. Falta verificar fontes primárias e a frase "Calculemus!" (ausente da Wikipedia).
- **Próximo**: exaurir Leibniz primário (verificar em fonte primária ou SEP até onde o projeto chegou e onde travou). Depois, direção 3 (como um LLM funciona na prática), que é a outra frente da comparação.
- Eixo: até onde a representação vetorial cumpre a *forma* do projeto, e onde a diferença é de grau (computacional) versus de natureza (o real não cabe no cálculo).
- **Já extraído** (16/06/2026): direção 6 ganhou duas notas — [o teorema da incompletude de Gödel](/notes/teorema-da-incompletude-de-godel) e [a numeração de Gödel](/notes/numeracao-de-godel) — e a direção 5 ganhou fonte atestada no [Naruhodo #461](https://vox.thluiz.com/2026/03/W11/naruhodo-461-o-que-e-a-teoria-da-incompletude-de-godel) para a posição do resíduo inexprimível.

## Motivação

A pesquisa nasce de um comentário já gravado. Em [systems-to-describe-for-everything-is-it-possible](/notes/systems-to-describe-for-everything-is-it-possible), a glosa do autor diz que tudo o que se faz hoje, "inclusive LLMs", são abstrações capazes de prever o próximo passo necessário, e que exigir um mapeamento completo do real é improdutivo — sempre aparece uma variável nova não prevista. O mesmo fio reaparece agora numa pergunta mais antiga: o sonho de Leibniz.

Leibniz quis uma notação em que cada ideia tivesse seu signo e o raciocínio virasse cálculo: a *characteristica universalis* acoplada a um *calculus ratiocinator*. O projeto não se completou. A forma da ambição, porém, voltou por uma porta que ele não imaginava — o espaço vetorial dos modelos de linguagem, onde a ideia é um ponto, a relação entre ideias é uma operação aritmética, e o resultado não depende da língua em que a palavra foi escrita. A pergunta é até onde essa volta é a mesma coisa, e onde só se parece.

**Posição do autor** (a testar e refinar ao longo da pesquisa, não conclusão fechada): não se pode reduzir o mundo a LLMs. Serão sempre aproximações. Como o próprio nome indica, são apenas *modelos*. A realidade é mais complexa e inexprimível do que cálculos simples conseguem capturar, ainda que esses cálculos tenham utilidade enorme. A pesquisa não existe para confirmar essa posição, mas para medi-la contra o que Leibniz quis e contra o que um LLM faz de fato.

## Perguntas em aberto

- Até que ponto estamos próximos do que Leibniz almejava?
- Ele foi um visionário a quem faltou apenas poder computacional, ou o que ele queria era de outra natureza do que um modelo estatístico entrega?
- (só o autor adiciona mais perguntas)

## Direções a mapear

A confirmar antes de aprofundar. Cada uma será exaurida antes de passar à próxima. Bibliografia ainda provisória.

### 1. Leibniz primário — o que ele propôs e até onde chegou

O projeto tem duas peças que andam juntas.

- ✓ **A *characteristica universalis*** é uma ideografia: um sistema de signos que representa diretamente as coisas (ou antes, as ideias), não as palavras. Meio de exprimir conceitos matemáticos, científicos e metafísicos numa notação universal e formal.
- ✓ **O *calculus ratiocinator*** é o par operacional: o meio de manipular, de modo computacional, o conhecimento registrado na *characteristica*. A notação guarda; o cálculo opera. (Formulação de Nicholas Rescher citada pela Wikipedia.)
- ✓ **"Alfabeto do pensamento humano".** As ideias complexas se exprimiriam pela combinação de signos que representam seus elementos simples. No limite, a linguagem seria composicional a partir de primitivos.
- ⚠ **Até onde chegou.** Leibniz produziu fragmentos, ensaios e tentativas de cálculo lógico, mas nunca o sistema completo. Mapear o que ele de fato construiu versus o que ficou como programa. (Verificar em fonte primária / SEP — distinguir realização de promessa.)
- ⚠ **"Calculemus!"** ("calculemos"). A imagem famosa: diante de uma divergência, em vez de discutir, dois pensadores pegariam as penas e calculariam. **A frase não consta da Wikipedia EN** consultada; verificar a fonte primária antes de citar.
- ⚠ **Cognitio caeca / symbolica** (conhecimento "cego" ou simbólico). Leibniz teria defendido que operamos com símbolos sem intuir a coisa a cada passo — manipulação formal cega que ainda assim chega ao verdadeiro. Conceito-chave para a ponte com o LLM (a máquina opera sem "entender"); a confirmar.

Links: [Characteristica universalis (Wikipedia)](https://en.wikipedia.org/wiki/Characteristica_universalis). A confirmar: [SEP "Leibniz's Logic"](https://plato.stanford.edu/entries/leibniz-logic/).

### 2. Precursores — a ars combinatoria e as línguas filosóficas

⚠ A linhagem que Leibniz herda e critica.

- ⚠ **Ramon Llull, *Ars Magna*** (séc. XIII–XIV). Roda de conceitos primitivos combináveis mecanicamente; o ancestral remoto da combinatória. (Não citado na Wikipedia consultada; verificar.)
- ✓ **John Wilkins, *An Essay towards a Real Character and a Philosophical Language*** (1668), e ✓ **George Dalgarno**. As "línguas filosóficas" do séc. XVII, que classificam o real e dão a cada categoria um signo. Leibniz os critica por mirarem a comunicação prática em vez da profundidade filosófica.
- ✓ **Caracteres chineses e hieróglifos egípcios** entram como modelo imaginado de escrita que representaria ideias, não sons — o atrativo da ideografia.

Links: [Characteristica universalis (Wikipedia)](https://en.wikipedia.org/wiki/Characteristica_universalis).

### 3. Como um LLM funciona na prática

⚠ A frente técnica. Reconstruir o mecanismo real, sem mística, para comparar com Leibniz peça a peça.

- ⚠ **Tokenização.** O texto é quebrado em tokens (pedaços de palavra), não em conceitos. Primeiro descompasso com Leibniz: a unidade não é a ideia, é o fragmento estatístico de escrita.
- ⚠ **Embedding.** Cada token vira um vetor num espaço de muitas dimensões. Posições próximas = usos próximos. É aqui que mora a analogia com a ideografia: representa-se por posição, não por cadeia de letras.
- ⚠ **Atenção / transformer.** O modelo pondera o contexto para ajustar a representação de cada token em função dos outros. (Verificar formulação correta; Vaswani et al., "Attention Is All You Need", 2017.)
- ⚠ **Previsão do próximo token.** O objetivo de treino é prever a continuação mais provável. O modelo não deduz: estima uma distribuição. Liga-se direto ao comentário do autor em [systems-to-describe-for-everything-is-it-possible](/notes/systems-to-describe-for-everything-is-it-possible) — "prever o próximo passo necessário".
- ⚠ **A base teórica — semântica distribucional.** ⚠ J. R. Firth (1957): "You shall know a word by the company it keeps." ⚠ Zellig Harris, hipótese distribucional (1954): palavras em contextos semelhantes têm sentidos semelhantes. O sentido emerge do uso, é opaco e estatístico — não decomposto em primitivos transparentes como Leibniz queria. (Verificar formulações e fontes.)

### 4. A comparação — até onde o vetor cumpre Leibniz

⚠ O cruzamento das frentes 1 e 3. Para cada peça do projeto, medir quanto o LLM realiza e quanto só se parece.

- ⚠ **Ideia como ponto, independente da palavra.** O embedding é a ideografia no sentido literal: representa-se por posição, não pela palavra da língua natural. *Mas* a unidade é o token, não a ideia primitiva — cumprimento parcial.
- ⚠ **Aritmética sobre o sentido — o *calculus ratiocinator* refeito.** O exemplo canônico do word2vec: *rei − homem + mulher ≈ rainha* (Mikolov et al., 2013). Operar com sentidos por adição e subtração de vetores tem a *forma* do cálculo do raciocínio. (Verificar a fonte e as críticas — o resultado é mais frágil e enviesado do que a vulgata sugere.)
- ⚠ **Espaço comum entre línguas — a "universalis".** Embeddings multilíngues alinham o mesmo conceito de línguas diferentes na mesma região. Seria a universalidade cumprida. (Verificar até onde o alinhamento é real e não imposto por projeção.)
- ⚠ **Cognitio caeca cumprida pela máquina.** O modelo opera sobre símbolos sem intuir o referente — o conhecimento cego/simbólico de Leibniz, agora literal. Liga-se à direção 1.

### 5. Visionário sem computador, ou diferença de natureza?

⚠ A pergunta-crux, a sintetizar depois de exauridas 1, 3 e 4. Dois lados a sustentar antes de decidir.

- ⚠ **Tese do grau** (faltou-lhe só poder computacional): Leibniz desenhou a representação calculável das ideias; nós a construímos. A diferença é de escala — bilhões de parâmetros versus a pena de um homem.
- ⚠ **Tese da natureza** (o que ele queria era outra coisa): Leibniz queria signos *transparentes e dedutíveis*, em que verdade = cálculo correto. O LLM dá signos *opacos e probabilísticos*, em que "verdade" = continuação plausível. Deduzir e estimar não são o mesmo ato. A semântica distribucional é o oposto metodológico do alfabeto de primitivos.
- ⚠ **O resíduo inexprimível** (posição do autor). Mesmo cumprida a forma, o modelo é modelo: aproximação útil, não o real. Conecta com a crítica do mapa × território e do "Deus de Spinoza" em [systems-to-describe-for-everything-is-it-possible](/notes/systems-to-describe-for-everything-is-it-possible), e com [borges-funes-pensar-e-esquecer](/notes/borges-funes-pensar-e-esquecer) (a representação total que deixa de ser pensamento).
- ✓ **Caminho formal para o resíduo — Gödel.** No [Naruhodo #461](https://vox.thluiz.com/2026/03/W11/naruhodo-461-o-que-e-a-teoria-da-incompletude-de-godel), Altair de Souza dá um argumento formal para essa posição: a linguagem é um sistema formal, o LLM a aproxima, e por Gödel a aproximação é por definição incompleta (a quantificação é injetora, "não volta em você"; AGI como construção ideológica). Notas de apoio: [o teorema da incompletude de Gödel](/notes/teorema-da-incompletude-de-godel) e [a numeração de Gödel](/notes/numeracao-de-godel).

### 6. A herança formal — de Frege a Gödel

⚠ O ramo que levou a *characteristica* a sério como lógica, não como semântica vetorial.

- ✓ **Frege, *Begriffsschrift*** (1879). A "escrita conceitual" é citada como sucessora direta do projeto leibniziano — a notação formal que realiza a parte lógica do sonho.
- ✓ **Gödel** teria considerado a *characteristica universalis* factível. (Wikipedia; verificar a fonte e o sentido exato.)
- ✓ **A incompletude como limite por dentro** (1931). O mesmo Gödel que achava a *characteristica* factível provou que todo sistema formal capaz de aritmética é incompleto: há verdades que ele não alcança a partir das próprias regras. O sonho dedutível encontra um teto vindo de dentro da lógica. Ver [o teorema da incompletude de Gödel](/notes/teorema-da-incompletude-de-godel) e o mecanismo em [a numeração de Gödel](/notes/numeracao-de-godel).
- ⚠ A bifurcação: Frege → lógica formal cumpre a *dedução*; a linhagem distribucional → vetores cumpre a *representação do sentido*. Os LLMs ficam do segundo lado, e é por isso que "calculam" sem deduzir. Material direto para a direção 5.

## Notas do Scholion já relacionadas

- [systems-to-describe-for-everything-is-it-possible](/notes/systems-to-describe-for-everything-is-it-possible) — o comentário do autor sobre LLMs como abstrações que preveem o próximo passo, e a crítica ao mapeamento total do real. Ponto de partida da pesquisa.
- [nietzsche-filosofia-da-gramatica](/notes/nietzsche-filosofia-da-gramatica) — a gramática conduz o sistema filosófico; o avesso da ambição leibniziana de uma notação que escaparia da língua.
- [borges-funes-pensar-e-esquecer](/notes/borges-funes-pensar-e-esquecer) — pensar como abstrair; a memória total que impede o conceito. Espelha a crítica ao mapa completo.

## Notas extraídas

- [o teorema da incompletude de Gödel](/notes/teorema-da-incompletude-de-godel) — o que Gödel provou em 1931, o que o teorema não diz, e a ponte com a incompletude dos LLMs (via [Naruhodo #461](https://vox.thluiz.com/2026/03/W11/naruhodo-461-o-que-e-a-teoria-da-incompletude-de-godel)).
- [a numeração de Gödel](/notes/numeracao-de-godel) — o mecanismo que faz a matemática falar de si mesma (codificação por potências de primos), o truque por trás do teorema.
