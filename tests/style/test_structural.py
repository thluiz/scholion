"""Checks estruturais — heurísticas sobre o corpo (não puramente lexicais).

Atenção: heurísticas podem ter falso-positivo. Os limites foram calibrados
pra serem conservadores; falhas devem ser revisadas, não auto-corrigidas.
"""
from __future__ import annotations

import math
import re

import pytest

from conftest import Note, fail_if_hits, find_lines, strip_quotes_and_code

# ---------- 1. Travessões em excesso (em-dash, en-dash, hyphen-as-dash) ----------

# em-dash (—) e en-dash (–) só são problema quando usados como pausa dramática.
# Heurística: contar todos no corpo; flagar acima de N por nota OU se >50% das
# linhas com travessão usam padrão "X — Y" (pausa).
EM_DASH = "\u2014"  # —
EN_DASH = "\u2013"  # –

# Timestamps de notas-bookmark de podcast: `**HH:MM:SS** —` — não conta como
# travessão estilístico. Remover essas linhas antes de medir.
TIMESTAMP_BOOKMARK = re.compile(
    rf"^\s*[-*]?\s*\*\*\d{{1,2}}:\d{{2}}(?::\d{{2}})?\*\*\s*[{EM_DASH}{EN_DASH}]"
)


def _strip_bookmark_lines(body: str) -> str:
    return "\n".join(l for l in body.splitlines() if not TIMESTAMP_BOOKMARK.match(l))


def _is_etymology_note(note: Note) -> bool:
    """Notas de etimologia/chinês seguem convenções próprias de ritmo e
    pontuação (notação estrutural, glosas paralelas). Seções 1, 7 e 8 skipam.
    """
    tags = note.frontmatter.get("tags", []) or []
    if any("etimologia" in str(t).lower() or "chines" in str(t).lower() for t in tags):
        return True
    return note.slug.startswith("etimologia-de-")


def test_dash_overuse(note: Note):
    # Notas de etimologia usam em-dash como notação estrutural ("aak1 — segurar,
    # agarrar"), não como pausa dramática. Skipa.
    if _is_etymology_note(note):
        return

    body = strip_quotes_and_code(_strip_bookmark_lines(note.body))
    em = body.count(EM_DASH)
    en = body.count(EN_DASH)
    line_count = max(1, sum(1 for l in body.splitlines() if l.strip()))
    total = em + en
    ratio = total / line_count
    if ratio > 0.35 and total >= 4:
        pat = re.compile(rf"[{EM_DASH}{EN_DASH}]")
        hits = find_lines(body, pat)[:8]
        fail_if_hits(
            note, hits,
            f"travessões demais ({total} em {line_count} linhas, ratio {ratio:.2f} > 0.35)",
        )


# ---------- 2. "X — Y" como pausa dramática (setup/punch) ----------
#
# DESATIVADO: na prática a heurística regex não consegue distinguir inciso
# genuíno de pausa dramática (tarefa #57 do skill). O test_dash_overuse acima
# pega o vício pela densidade, sem falso-positivo individual. Manter a
# implementação caso queiramos refinar com LLM no Phase 2.


# ---------- 3. Negativa indireta: "X não é Y — é Z" ou "não é A, é B" ----------

NEG_INDIRETA = re.compile(
    rf"não\s+(?:é|são|foi|foram|tem|tinha|seria)\s+\S.+?[{EM_DASH}{EN_DASH},]\s+"
    r"(?:é|são|foi|foram|tem|tinha|seria|mas\s+sim)\s",
    re.IGNORECASE,
)


def test_no_negativa_indireta(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, NEG_INDIRETA)
    fail_if_hits(
        note, hits,
        "negativa indireta ('não é X — é Y') — reescrever na forma positiva",
    )


# ---------- 4. Three-beat: "X. Twist. Y." (três frases curtas em sequência) ----------
#
# DESATIVADO: heurística regex não distingue paralelismo mecânico de três
# frases curtas legítimas (etimologias, anotações de podcast, bullets). Manter
# pra Phase 2 com checagem de paralelismo gramatical via LLM.


# ---------- 5. Co-Authored-By no corpo da nota (memory: feedback_no_coauthored) ----------

CO_AUTHORED = re.compile(r"Co-Authored-By", re.IGNORECASE)


def test_no_co_authored_by(note: Note):
    hits = find_lines(note.raw, CO_AUTHORED)
    fail_if_hits(note, hits, "Co-Authored-By proibido (memory: feedback_no_coauthored)")


# ---------- 6. Markup alucinado de ChatGPT/Grok (colagem crua) ----------
#
# Âncoras que os chats injetam em citações e que nunca deveriam sobreviver à
# edição: marcadores de citação do ChatGPT (oaicite, contentReference,
# turnNsearchM, citeturn), cards do Grok, e os delimitadores invisíveis de
# citação que o ChatGPT esconde no bloco private-use U+E200-U+E20F e que
# sobrevivem a copiar/colar.
#
# A faixa private-use INTEIRA (U+E000-U+F8FF) não serve: calibração de
# 2026-09-10 sobre 2136 notas achou 3 notas de etimologia com U+E815, U+F6DD
# e U+F6E7 — glifos CJK raros não codificados, que 小學堂/CUHK/hanziyuan
# servem por fonte private-use. Uso legítimo, e o único uso de PUA no corpus.
#
# Roda sobre note.raw, sem strip: dentro de blockquote ou code fence o
# marcador continua sendo colagem crua.

HALLUCINATED_MARKUP = re.compile(
    r"oaicite"
    r"|contentReference"
    r"|citeturn"
    r"|turn\d+(?:search|view|news|image)\d+"
    r"|grok_card"
    r"|【\d+†"  # 【N† — âncora de citação do ChatGPT
    r"|[-]",  # delimitador invisível de citação do ChatGPT
    re.IGNORECASE,
)


def test_no_hallucinated_markup(note: Note):
    hits = find_lines(note.raw, HALLUCINATED_MARKUP)
    fail_if_hits(note, hits, "colagem crua de ChatGPT/Grok sem edição")


# ---------- 7. Uniformidade de parágrafos (ritmo mecânico) ----------
#
# LLM tende a produzir parágrafos do mesmo tamanho, um atrás do outro. Prosa
# humana varia: um parágrafo de quatro linhas, um de uma, um de seis.
# Métrica: coeficiente de variação (desvio-padrão populacional / média) do
# número de palavras por parágrafo de prosa. CV baixo = ritmo de máquina.
#
# Calibração 2026-09-10, corpus de 2166 notas: 39 chegam ao mínimo de 6
# parágrafos de prosa; 1 falha (maturana-varela-autopoiese, CV=0.13, seis
# parágrafos entre 37 e 57 palavras) = 0.05% do corpus. Mediana do CV entre
# as avaliadas: 0.30.
#
# O limiar de 5 parágrafos (primeira tentativa) reprovava mais duas notas de
# forma legítima: krenak-vida-nao-e-util (CV=0.150, sumários "Sobre X:" de
# tópicos de uma entrevista) e naturalizacao-desejo-e-estrategia-politica
# (CV=0.108, anotação de podcast). Cinco parágrafos são amostra fina demais
# pra sustentar um CV; daí MIN_PARAGRAPHS=6. As notas de bookmark saem por
# _is_bookmark_note: ali um parágrafo por timestamp é a forma, não o vício.

WORD_RE = re.compile(r"[^\W\d_]+")

# Linhas que não são prosa corrida: heading, bullet, lista numerada, tabela.
NON_PROSE_LINE = re.compile(r"^\s*(?:#|[-*+]\s|\d+[.)]\s|\|)")

MIN_PARA_WORDS = 20   # abaixo disso é fragmento legítimo, não entra na média
MIN_PARAGRAPHS = 6    # amostra menor que isso não sustenta a estatística
MIN_CV = 0.15
MIN_BOOKMARKS = 3     # a partir daqui a nota é lista de anotações, não prosa


def _prose_paragraphs(note: Note, min_words: int = MIN_PARA_WORDS) -> list[str]:
    """Parágrafos de prosa corrida do corpo da nota.

    Tira citação/código/link/HTML (strip_quotes_and_code), linhas de bookmark
    de podcast, headings, bullets, listas numeradas e linhas de tabela — sobra
    o que o leitor lê como prosa. Fragmentos curtos são legítimos e ficam de
    fora da conta. Seções 7 e 8 usam a mesma definição.
    """
    body = strip_quotes_and_code(_strip_bookmark_lines(note.body))
    kept = [l for l in body.splitlines() if not NON_PROSE_LINE.match(l)]
    paras = []
    for block in re.split(r"\n\s*\n", "\n".join(kept)):
        text = " ".join(block.split())
        if text and len(WORD_RE.findall(text)) >= min_words:
            paras.append(text)
    return paras


def _is_bookmark_note(note: Note) -> bool:
    """Nota de anotação de podcast: um parágrafo por timestamp. A uniformidade
    é a forma (o anotador gera um bloco por marcação), não vício de escrita.
    """
    marks = sum(1 for l in note.body.splitlines() if TIMESTAMP_BOOKMARK.match(l))
    return marks >= MIN_BOOKMARKS


def test_paragraph_uniformity(note: Note):
    if _is_etymology_note(note) or _is_bookmark_note(note):
        return
    paras = _prose_paragraphs(note)
    if len(paras) < MIN_PARAGRAPHS:
        return
    counts = [len(WORD_RE.findall(p)) for p in paras]
    mean = sum(counts) / len(counts)
    if mean <= 0:
        return
    cv = math.sqrt(sum((c - mean) ** 2 for c in counts) / len(counts)) / mean
    if cv < MIN_CV:
        pytest.fail(
            f"\n[parágrafos uniformes demais] {note.relpath}: "
            f"{len(paras)} parágrafos, CV={cv:.2f} < {MIN_CV} "
            f"(média {mean:.0f} palavras)\n"
            f"  palavras por parágrafo: {counts}\n"
            f"  variar o tamanho: cortar um curto, deixar outro respirar.",
            pytrace=False,
        )


# ---------- 8. Densidade de conectivos abrindo parágrafo ----------
#
# Lista separada da CONECTIVOS_INICIO do test_lexical: aqueles são
# burocráticos e reprovam em qualquer ocorrência única. Estes são legítimos um
# a um ("Mas o problema é outro.") e só viram vício em volume — parágrafo após
# parágrafo pendurado no anterior por uma dobradiça, em vez de corte seco.
#
# Calibração 2026-09-10, corpus de 2166 notas: 51 chegam ao mínimo de 5
# parágrafos de prosa; nenhuma reprova. A mais carregada é
# deus-antes-de-criar-o-mundo, com 1 de 6 parágrafos (17%), metade do limiar
# de 30%. Contar também os parágrafos curtos (< 20 palavras) não muda o
# quadro: 62 avaliadas, máximo de 17%, zero reprovações. O autor não tem o
# tique; o teste é guarda de regressão, com margem de 13 pontos.

CONECTIVOS_BRANDOS = (
    "mas", "porém", "então", "assim", "ou seja", "no entanto", "contudo",
    "entretanto", "também", "aliás", "na verdade", "de fato", "por isso",
    "logo", "e",
)

# Word boundary que respeita acentos (\b em Python não vê À-ÿ como word char).
ABRE_CONECTIVO = re.compile(
    r"^(?:" + "|".join(CONECTIVOS_BRANDOS) + r")(?![\wÀ-ÿ]),?\s",
    re.IGNORECASE,
)

# Ênfase/citação markdown na abertura do parágrafo, tirada antes de casar.
LEADING_MARKUP = re.compile(r"^[\s*_>#`\"'“”]+")

MIN_TRANSITION_PARAGRAPHS = 5
MAX_TRANSITION_RATIO = 0.30
MIN_TRANSITION_HITS = 3


def test_transition_density(note: Note):
    if _is_etymology_note(note) or _is_bookmark_note(note):
        return
    paras = _prose_paragraphs(note)
    if len(paras) < MIN_TRANSITION_PARAGRAPHS:
        return
    hits = [p for p in paras if ABRE_CONECTIVO.match(LEADING_MARKUP.sub("", p))]
    ratio = len(hits) / len(paras)
    if ratio > MAX_TRANSITION_RATIO and len(hits) >= MIN_TRANSITION_HITS:
        abre = "\n".join(f"  «{p[:90]}…»" for p in hits[:6])
        pytest.fail(
            f"\n[conectivo abrindo parágrafo] {note.relpath}: "
            f"{len(hits)} de {len(paras)} parágrafos ({ratio:.0%}) abrem com "
            f"conectivo\n{abre}\n"
            f"  usar corte seco: começar pela afirmação, não pela dobradiça.",
            pytrace=False,
        )
