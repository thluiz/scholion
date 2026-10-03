# Tradução e terminologia nas notas de etimologia

A prosa da nota é **português brasileiro**. Léxico PT-EU → PT-BR não se mantém aqui: a lista canônica (`LEXICON`) vive em `lint-notes.mjs`; rodar `node .claude/skills/research-chinese-etymology/lint-notes.mjs` (com `--fix` para aplicar) depois de gravar. Pares novos entram no script, aprovados pelo autor, não em tabela paralela.

Não traduzir termos técnicos chineses (Shuowen, fanqie, 段注, jyutping) nem o vocabulário linguístico de origem latina (radical, fonético, semântico, dialeto, fonossemântico). "Estar a + infinitivo" é válido no idioleto do autor (memória `user_periphrase_infinitivo`); não corrigir.

## Regras de citação

1. **Definições do chardb**: chinês verbatim + tradução PT-BR entre parênteses, uma por número. Preservar todas.
2. **Shuowen e comentários de estudiosos**: chinês original + tradução PT-BR entre parênteses. Atribuir ao rótulo certo (今按 = 小學堂; 略說/詳解/形義通解 = CUHK).
3. **段注 Duan Yucai**: só com texto obtido de fonte viva; hoje nenhuma das seis fornece — marcar como não obtido.
4. **MDBG**: definições traduzidas para PT-BR (o gabarito traduz; não deixar em inglês).
5. **Tabela de evolução de formas**: tudo traduzido — período, dinastia, estado, script, artefato — com pinyin quando o artefato tem nome próprio (ex.: 沈子它簋蓋 Shěnzǐ Tā guǐ gài). Identificadores de corpus (甲903, 包2.237, 璽彙1598) ficam verbatim, dígito a dígito.
6. **Fonologia**: rótulos bilíngues como no gabarito (`攝 Division`, `韻 Rhyme`, `聲 Tone`, `母 Initial`, `反切 Fanqie`, `等 Grade`, `開合 Open/Closed`, `清濁`).

## Glossário de fonologia

| Chinês | Tradução | Valores |
|---|---|---|
| 攝 | division | nome do 攝 + pinyin, ex.: 止 (Zhi) |
| 韻 | rhyme | nome do 韻目 + pinyin |
| 聲 / 聲調 | tone | 平 level · 上 rising · 去 departing · 入 entering |
| 母 / 字母 | initial | caractere + inicial aproximada, ex.: 書 (sh-) |
| 反切 | fanqie | os dois caracteres verbatim |
| 等 / 等第 | grade | 一 (I) · 二 (II) · 三 (III) · 四 (IV) |
| 開合 | open/closed | 開 open · 合 closed |
| 清濁 | — | 全清 totalmente surda · 次清 aspirada surda · 次濁 sonorante · 全濁 sonora plena |
| 韻部 | grupo de rima (上古音) | nome + pinyin |

Sistemas de reconstrução do 上古音, nesta ordem: 高本漢 Karlgren · 王力 Wang Li · 董同龢 Dong Tonghe · 周法高 Zhou Fagao · 李方桂 Li Fanggui · 鄭張尚芳 Zhengzhang Shangfang. Linha sem dado leva o marcador, não é omitida.

## Glossário de períodos e scripts (tabela de formas)

Períodos: 商 Shang · 西周 Zhou Ocidental (早/中/晚 = inicial/médio/tardio) · 春秋 Primaveras e Outonos · 戰國 Reinos Combatentes (早/中/晚; estado entre parênteses: 齊 Qi, 燕 Yan, 晉 Jin, 楚 Chu, 秦 Qin) · 秦 Qin · 西漢 Han Ocidental · 東漢 Han Oriental.

Scripts: 甲骨文 Oráculo (osso oracular) · 金文 Bronze · 璽 / 璽印 Selo (sigilográfico) · 貨幣 / 幣 Inscrição em moeda · 簡 Bambu (tiras) · 帛 Seda (manuscrito) · 小篆 Selo pequeno · 隸書 Clerical · 石經 Clássicos em Pedra.

Artefatos recorrentes: 說文‧X部 → "Shuowen, seção X" · 睡虎地簡 Shuihudi · 居延簡 Juyan · 包山簡 Baoshan · 熹平石經 Clássicos em Pedra de Xiping. Nome próprio não listado aqui: manter o chinês e acrescentar o pinyin, sem glosar.

## Datação sem fonte

Para caracteres ausentes do corpus filológico clássico (Shuowen, Guangyun, Kangxi), **não atribuir datação histórica como fato** ("Ming–Qing", "atestação tardia", "criação recente") sem fonte consultada que a sustente. Inferência razoável mas não verificada é marcada como inferência.

- ❌ "A atestação mais antiga de uso escrito é tardia (Ming–Qing em textos cantoneses regionais)."
- ❌ "É composto semântico puro de criação recente."
- ✅ "Provavelmente criação letrada cantonesa tardia — inferência a partir do registro 方言, sem datação direta nas fontes."

A observação que sempre pode ser feita com segurança, quando é o caso: "ausente do *Shuowen* (Han), *Guangyun* (Song), *Kangxi Zidian* (Qing); presente apenas em referência moderna como o *Hanyu Da Zidian*, sob etiqueta 方言."
