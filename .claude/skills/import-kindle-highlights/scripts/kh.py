"""Lógica comum de destaques do Kindle (usada por generate.py e verify.py)."""
import re

# Atribuição no fim do destaque, como o livro a traz: "... frase. nietzsche (1886)".
# Minúsculas curtas após a pontuação final; "h" solto é artefato de captura.
TAIL = re.compile(
    r'([.!?…\]”"])\s+([a-zà-ü][a-zà-ü ]{1,40}?)'
    r'(?:\s*\(((?:\d{4}|sem data))\))?h?$')


def split_attribution(text):
    """-> (frase_sem_atribuicao, nome_em_minusculas | None, ano | None)"""
    text = text.strip()
    m = TAIL.search(text)
    if not m:
        return text, None, None
    year = m.group(3) if m.group(3) and m.group(3) != 'sem data' else None
    return text[:m.end(1)], m.group(2).strip(), year


def highlights(path):
    """Destaques de library/<livro>.md -> [{'loc', 'raw', 'text', 'name', 'year'}]"""
    lib = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'((?:^>.*\n)+?)<!-- kh loc=(\d+)', lib, re.M):
        lines = [l[1:].strip() for l in m.group(1).splitlines()]
        lines = [l for l in lines if not l.startswith('— loc.') and not l.startswith('\U0001F4DD')]
        raw = ' '.join(lines).strip()
        text, name, year = split_attribution(raw)
        out.append({'loc': int(m.group(2)), 'raw': raw, 'text': text, 'name': name, 'year': year})
    return out
