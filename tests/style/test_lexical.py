"""Checks lexicais — detectáveis por regex sobre o corpo da nota.

Regras vêm da skill ghost-writer (vocabulário banido, voz, registro).
Strip-out de blockquotes/code/links é feito antes da checagem.
"""
from __future__ import annotations

import re

from conftest import Note, fail_if_hits, find_lines, strip_quotes_and_code

# Word boundary que respeita acentos: usar lookarounds em vez de \b (pois \b
# em Python só vê [A-Za-z0-9_] como "word", não acentos).
WB = r"(?<![\wÀ-ÿ])"
WBE = r"(?![\wÀ-ÿ])"


def _w(*terms: str) -> re.Pattern[str]:
    """Compila uma alternância case-insensitive com word boundaries."""
    alt = "|".join(re.escape(t) for t in terms)
    return re.compile(WB + r"(?:" + alt + r")" + WBE, re.IGNORECASE)


# ---------- 1. Vocabulário banido (skill ghost-writer) ----------

# Conservador: removidos termos que aparecem demais em contextos legítimos
# (notas em inglês, citações filosóficas, traduções de Laozi/Aristóteles, etc.):
# crucial, vital, fundamental, profundo/a, transformador/a, poderoso/a,
# robusto/a, abrangente, fascinante, incrível, extraordinário/a.
# Se quiser banir, adicionar de volta — mas espere muitos falso-positivos
# em notas em inglês ou que citam fontes filosóficas que usam esses termos.
BANNED_VOCAB = _w(
    "essencialmente", "notavelmente",
    "é importante notar que", "é importante notar",
    "vale ressaltar", "cabe destacar",
    "nesse sentido", "nesse contexto", "nessa perspectiva",
    "em última análise",
    "pode-se argumentar que", "de certa forma", "em muitos aspectos",
    "ademais", "outrossim", "não obstante", "destarte",
    "imagine que", "considere o seguinte",
    "como dizia o filósofo",
    "indubitavelmente", "inegavelmente",
    "rica tapeçaria", "delicado equilíbrio",
)

JARGON_FECHO = _w(
    "concluindo", "finalizando", "em suma", "em resumo", "em síntese",
    "portanto", "enfim",
)


def test_no_banned_vocab(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, BANNED_VOCAB)
    fail_if_hits(note, hits, "vocabulário banido")


def test_no_jargon_fecho(note: Note):
    body = strip_quotes_and_code(note.body)
    # Só sinaliza se aparece como ABERTURA de parágrafo (jargão de fechamento)
    pattern = re.compile(
        r"(?:^|\n\n)\s*(?:" +
        "|".join(["concluindo", "finalizando", "em suma", "em resumo",
                  "em síntese", "portanto[,.]", "enfim[,.]"]) +
        r")",
        re.IGNORECASE,
    )
    hits = find_lines(body, pattern)
    fail_if_hits(note, hits, "jargão de fechamento como abertura de parágrafo")


# ---------- 2. PT-EU forms ----------

PT_EU = _w(
    "facto", "factos",
    "reacção", "reacções", "acção", "acções",
    "comboio", "autocarro", "telemóvel",
    "raparigas", "rapariga",
    "casa-de-banho",
    "estás", "estavas", "tu fazes", "tu vais", "tu és",
    "imenso giro",
)


def test_no_pt_eu(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, PT_EU)
    fail_if_hits(note, hits, "PT-EU (use PT-BR)")


# ---------- 3. Wing Chun (Moy Yat usa Ving Tsun) ----------

WING_CHUN = _w("Wing Chun", "wing chun", "WingChun")


def test_no_wing_chun(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, WING_CHUN)
    fail_if_hits(note, hits, "use 'Ving Tsun' (linhagem Moy Yat), não 'Wing Chun'")


# ---------- 4. Termos da família aglutinados (devem ter espaço) ----------

# Detecta "Sifu", "Sihing", "Sigung" etc. mas NÃO casa "Si Fu", "Si Hing"
AGGLUTINATED = re.compile(
    r"(?<![\wÀ-ÿ])"
    r"(Sifu|Sihing|Sigung|Sitaaigung|Todai|Todais|Sije)"
    r"(?![\wÀ-ÿ])",
)


def test_no_agglutinated_terms(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, AGGLUTINATED)
    fail_if_hits(note, hits, "termos da família devem ter espaço (Si Fu, Si Hing, To Dai...)")


# ---------- 5. Romanização errada Moy Yat ----------

WRONG_ROMAN = re.compile(
    r"(?<![\wÀ-ÿ])"
    r"(Moy Lima|Moy Quelo Si|Moy Quelo|Moy Joleu|Moy Joleou)"
    r"(?![\wÀ-ÿ])",
)


def test_no_wrong_moy_yat_romanization(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, WRONG_ROMAN)
    fail_if_hits(
        note, hits,
        "romanização Moy Yat: usar Moy Lim Ma, Moy Kei Lo Si, Moy Jo Lei Ou (Whisper erra)",
    )


# ---------- 6. Conectivos burocráticos ----------

# Como ABERTURA de parágrafo (regex: depois de \n\n ou início, com vírgula seguindo)
CONECTIVOS_INICIO = re.compile(
    r"(?:^|\n\n)\s*"
    r"(além disso|por outro lado|nesse contexto|nessa perspectiva|"
    r"nesse sentido|em última análise|por conseguinte|"
    r"dessa forma|dessa maneira|desse modo)",
    re.IGNORECASE,
)


def test_no_bureaucratic_openers(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, CONECTIVOS_INICIO)
    fail_if_hits(note, hits, "conectivo burocrático abrindo parágrafo (use corte seco)")


# ---------- 7. Hedges covardes ----------

HEDGES = _w(
    "para mim,", "na prática,",
    "por assim dizer", "de certa forma", "em muitos aspectos",
    "por algum motivo,",
)


def test_no_hedges(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, HEDGES)
    fail_if_hits(note, hits, "hedge covarde — afirme ou não afirme")


# ---------- 8. CTAs ----------

CTAS = re.compile(
    r"(?<![\wÀ-ÿ])"
    r"(comente abaixo|deixe seu comentário|compartilhe (?:este post|esse post|nas redes)|"
    r"se inscreva|inscreva-se|like e siga|curta e compartilhe)"
    r"(?![\wÀ-ÿ])",
    re.IGNORECASE,
)


def test_no_cta(note: Note):
    body = strip_quotes_and_code(note.body)
    hits = find_lines(body, CTAS)
    fail_if_hits(note, hits, "CTA / call-to-action (não há)")
