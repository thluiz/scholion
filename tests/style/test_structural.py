"""Checks estruturais — heurísticas sobre o corpo (não puramente lexicais).

Atenção: heurísticas podem ter falso-positivo. Os limites foram calibrados
pra serem conservadores; falhas devem ser revisadas, não auto-corrigidas.
"""
from __future__ import annotations

import re

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


def test_dash_overuse(note: Note):
    # Notas de etimologia usam em-dash como notação estrutural ("aak1 — segurar,
    # agarrar"), não como pausa dramática. Skipa.
    tags = note.frontmatter.get("tags", []) or []
    if any("etimologia" in t.lower() or "chines" in t.lower() for t in tags):
        return
    if note.slug.startswith("etimologia-de-"):
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
