"""Cruza os destaques de um livro do kindle-scrapper com as notas do vault.

Uso:  python -I crossmatch.py <library/livro.md> [--json saida.json]

Imprime: quantos destaques o livro tem, quais já viraram nota (em QUALQUER nota
do vault, com ou sem a tag do livro) e quais não. Com --json grava os pendentes
(loc + texto completo) para o passo de geração de drafts.
O texto completo vem inteiro: nunca truncar na listagem, porque em antologias o
autor da frase fica no FIM do destaque.
"""
import glob, io, json, re, sys, unicodedata

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
PREFIX = 60  # caracteres normalizados comparados


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def strip_author(text):
    """Tira a atribuição do fim ("nietzsche (1886)"): minúsculas curtas após a pontuação final."""
    m = re.search(r'([.!?…\]”"])\s+([a-zà-ü][a-zà-ü ]{1,40}?)(?:\s*\((?:\d{4}|sem data)\))?h?$', text)
    return text[:m.end(1)] if m else text


def highlights(path):
    lib = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'((?:^>.*\n)+?)<!-- kh loc=(\d+)', lib, re.M):
        lines = [l[1:].strip() for l in m.group(1).splitlines()]
        lines = [l for l in lines if not l.startswith('— loc.') and not l.startswith('📝')]
        out.append((int(m.group(2)), ' '.join(lines)))
    return out


def main():
    path = sys.argv[1]
    hl = highlights(path)
    corpus = {}
    for f in glob.glob(r'E:\scholion\content\notes\*.md') + glob.glob(r'E:\scholion\content\notes\*\index.md'):
        corpus[f] = norm(open(f, encoding='utf-8').read())
    done, pending = [], []
    for loc, text in hl:
        key = norm(strip_author(text))[:PREFIX]
        hit = [f for f, t in corpus.items() if key and key in t]
        (done if hit else pending).append((loc, text, hit))
    print(f'total={len(hl)} ja_nota={len(done)} pendentes={len(pending)}')
    print('\n== JA TEM NOTA (confira se tem a tag do livro) ==')
    for loc, text, hit in done:
        print(f'loc {loc}: {text[:60]}... -> {hit[0].split(chr(92))[-1]}')
    print('\n== PENDENTES (texto completo) ==')
    for i, (loc, text, _) in enumerate(pending, 1):
        print(f'{i}. [loc {loc}] {text}')
    if '--json' in sys.argv:
        dest = sys.argv[sys.argv.index('--json') + 1]
        json.dump([{'loc': l, 'text': t} for l, t, _ in pending], open(dest, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)


main()
