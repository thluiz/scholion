---
title: "Coleção curada de citações — autores canônicos"
date: 2026-05-08T19:30:00+01:00
summary: "Construção de coleção verificada de citações célebres em E:/scholion/content/notes/, com fonte primária inline (obra + ano + capítulo/poema). Inclui documentação de misatribuições virais. Trabalho via subagentes paralelos do Claude Code."
tags: ["pesquisa-viva", "citacoes", "atribuicao-erronea", "meta"]
status: "em andamento"
toc: true
---

## Método (específico)

Regras gerais aplicadas: source-or-silence rigoroso, ghost-writer (PT-BR, sem voz própria opinativa, sem aforismo sintetizador final), pre-flight grep antes de duplicar.

Cada autor segue rotina:

1. Wikiquote (PT/EN/ES/DE/FR conforme idioma) como ponto de partida — extrair candidatas com fonte (obra, ano, capítulo/poema/aforismo)
2. Cross-check em fonte primária (Gutenberg, Domínio Público, machado.mec.gov.br, Itaú Cultural, etc.)
3. Para cada citação: nota com original (no idioma de origem) + tradução PT-BR contextual no corpo
4. Misatribuição: nota separada com slug `*-misattributed-*` documentando autor real + mecanismo de migração
5. `python -m pytest tests/style/ -x -q -k "<autor>"` antes do commit

Cada par/round = 2 subagentes general-purpose lançados sequencialmente (não em paralelo, evita race no `git push`). Cada um cobre 15-30 notas + commit + push autônomo.

## Estado

**Em foco**: brasileiros primeiro, depois internacional.

**Próximo**: Vargas + José Bonifácio (Round 3 da fase atual).

## Concluído

### Antes de 2026-05-08 (autores diversos)

- Bertrand Russell (incluindo *Three Passions*)
- Mark Twain + misatribuições
- Voltaire + "originalidade não é nada além de imitação criteriosa" (Voltaire, autor correto)
- Pascal
- Montaigne
- Spinoza
- Nietzsche (com atenção ao *Ecce Homo* tardio)
- Camus
- Fernando Pessoa (incluindo misatribuições "valor das coisas" → Maria Júlia Paes da Silva e "há um tempo em que é preciso abandonar" → Fernando Teixeira de Andrade)
- Oscar Wilde (24 notas)
- George Bernard Shaw (26 notas, 5 misatribuições famosas: "youth wasted on young", "we don't stop playing", common language, "creating yourself", communication)
- Jorge Luis Borges (25 notas, misatribuição: "Instantes" → Don Herold, *Reader's Digest* 1953)
- Ludwig Wittgenstein (26 notas: Tractatus 7, IF 10, Cultura e Valor 6, On Certainty 3)

### 2026-05-08 — sessão atual

- **Machado de Assis** (22 notas, commit `493d0f8`): Memórias Póstumas 9, Dom Casmurro 6, Quincas Borba 3, Esaú e Jacó 1, Memorial de Aires 1, contos 6, crônica Bons Dias! 1, misatribuição 1
- **Carlos Drummond de Andrade** (30 notas, commit `7e1f7a0`): poesia 18 + prosa/aforismos 6, **5 misatribuições documentadas** ("A vida é a arte do encontro" → Vinicius, "Aceitar é como uma droga" → apócrifa, "Recomeçar" → Paulo Roberto Gaefke, "A dor é inevitável" → Tim Hansel, "Máscara" → Dante Milano)
- **Érico Veríssimo** (25 + 1 misatribuição, commit `5e2aca3`): Olhai os Lírios 9, Incidente em Antares 8, demais espalhados
- **Luis Fernando Veríssimo** (16 autênticas + **11 misatribuições**, commit `461f4dd`): O Analista de Bagé domina (5), confirma estatística do próprio LFV de 4-em-5 frases atribuídas serem apócrifas

## Pendente (na ordem aprovada)

### Brasileiros

3. Getúlio Vargas + José Bonifácio (políticos históricos, carta-testamento + Representação Constituinte)
4. Monteiro Lobato (sozinho — *A Barca de Gleyre*) — separado de Tom Jobim
5. Tom Jobim + Gilberto Gil (música)
6. Chico Buarque + Caetano Veloso (letras + prosa)
7. Jô Soares + Fernando Henrique Cardoso (contemporâneos; cuidado com "esqueçam o que escrevi")
8. Millôr Fernandes + Mário Quintana (aforistas)
9. Guimarães Rosa + Graciliano Ramos (romance)
10. Nelson Rodrigues + Rubem Braga (cronistas)
11. Clarice Lispector + Ariano Suassuna (alto risco misatribuição Clarice — caso clássico Pessoa-like)
12. Vinicius de Moraes + Manuel Bandeira (poesia)

### Internacional

13. Heráclito + Diógenes Laércio (gregos antigos, fragmentos DK / *Vidas dos Filósofos*)
14. Simone de Beauvoir + Simone Weil (Beauvoir antes — pedido explícito)
15. Walter Benjamin (sozinho — Arcades Project / Nachlass requer cuidado)
16. Ralph Waldo Emerson + Henry David Thoreau (transcendentalistas americanos)

## Misatribuições já documentadas

Casos canônicos a citar quando temas similares aparecerem:

- "Há um tempo em que é preciso abandonar" → Fernando Teixeira de Andrade (não Pessoa)
- "O valor das coisas não está no tempo" → Maria Júlia Paes da Silva (não Pessoa, Sabino, Baudelaire)
- "Instantes / Se eu pudesse viver novamente" → Don Herold (não Borges)
- "A vida é a arte do encontro" → Vinicius de Moraes (não Drummond)
- "The time you enjoy wasting" → Marthe Troly-Curtin 1912 (não Russell)
- "Youth is wasted on the young" → discutível; texto canônico em Shaw mas formulação atual é posterior
- "We don't stop playing because we grow old" → não-Shaw; provavelmente George Bernard Pulsifer
- "England and America two countries common language" → não-Shaw; provavelmente Wilde ou Dickens

## Domínios autorizados (settings.local.json)

200 domínios WebFetch autorizados em `E:/.claude/settings.local.json`. Lote brasileiro adicionado em 2026-05-08: letras.mus.br, vagalume.com.br, sites oficiais (chicobuarque, caetanoveloso, gilbertogil, jobim.org, claricelispector.ims, viniciusdemoraes, millorfernandes), arquivos (cpdoc.fgv, itaucultural, ims.com.br, bn.gov.br, bndigital, fundacaofhc, companhiadasletras), imprensa (folha, oglobo, estadao, veja, revistacult, revistapesquisa.fapesp), literatura (releituras, tirodeletra), estrangeiros (gallica.bnf, libcom, newleftreview, rwe, walden, sas.upenn).

## Critérios

- Alvo: 15-30 notas por autor (varia por densidade aforística)
- Toda nota: original + tradução PT-BR; capítulo/poema/proposição obrigatório
- Misatribuição: tag `atribuicao-erronea` + autor real
- Style-test obrigatório antes do commit
