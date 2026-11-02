"""Conferência mecânica das notas importadas de um livro do Kindle.

Uso:  python -I verify.py <library/livro.md> <tag-do-livro> [--drafts <pasta>]

Sem --drafts: confere as notas já gravadas em content/notes/ que têm a tag do livro.
Com --drafts: confere os drafts (antes de gravar). Sai com código 1 se algo divergir.

Para cada nota:
  1. TÍTULO  igual, caractere a caractere, ao destaque do Kindle sem a atribuição do fim
             (só o escape YAML de \\ e " é desfeito; o resto não pode mudar).
  2. ANO     se a nota diz "datada de X", X tem de ser o ano do destaque (ERRO se diferir);
             ano ausente na nota, ou que não está no destaque, sai como AVISO.
  3. FONTE   o bloco sources[0] é idêntico ao das outras notas do livro.
Notas antigas, com título editado à mão, saem como AVISO (sem destaque idêntico), não como erro.
"""
import glob, io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
AUTHOR_TAIL = re.compile(r'([.!?\u2026\]\u201d"])\s+([a-z\u00e0-\u00fc][a-z\u00e0-\u00fc ]{1,40}?)(?:\s*\(((?:\d{4}|sem data))\))?h?$')


def highlights(path):
    lib = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'((?:^>.*\n)+?)<!-- kh loc=(\d+)', lib, re.M):
        lines = [l[1:].strip() for l in m.group(1).splitlines()]
        lines = [l for l in lines if not l.startswith('— loc.') and not l.startswith('📝')]
        text = ' '.join(lines).strip()
        m2 = AUTHOR_TAIL.search(text)
        year = None
        if m2:
            year = m2.group(3) if m2.group(3) and m2.group(3) != 'sem data' else None
            text = text[:m2.end(1)]
        out.append({'loc': int(m.group(2)), 'text': text, 'year': year})
    return out


def parse(path):
    t = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    m = re.search(r'^title: "(.*)"$', t, re.M)
    title = m.group(1).replace('\\"', '"').replace('\\\\', '\\') if m else None
    src = re.search(r'^sources:\n((?:  .*\n)+?)(?=---|\S)', t, re.M)
    first = None
    if src:
        block = src.group(1)
        parts = re.split(r'(?m)^  - ', block)
        first = ('  - ' + parts[1]).strip() if len(parts) > 1 else None
        first = re.sub(r'\n    url: .*', '', first) if first else None  # url por trecho pode variar
    return {'title': title, 'summary': (re.search(r"^summary: (.*)$", t, re.M) or [None, ''])[1],
            'body': t.split('\n---\n', 1)[-1], 'source': first}


def main():
    lib, tag = sys.argv[1], sys.argv[2]
    if '--drafts' in sys.argv:
        files = glob.glob(sys.argv[sys.argv.index('--drafts') + 1] + r'\*.md')
    else:
        files = [f for f in glob.glob(r'E:\scholion\content\notes\*.md')
                 if f'"{tag}"' in open(f, encoding='utf-8').read()]
    hl = highlights(lib)
    by_text = {h['text']: h for h in hl}
    erros, avisos, ok, sources = [], [], 0, {}
    for f in sorted(files):
        name = f.split('\\')[-1]
        n = parse(f)
        if n['title'] is None:
            avisos.append(f'{name}: título fora do formato "..." (conferir à mão)'); continue
        h = by_text.get(n['title'])
        if not h:
            avisos.append(f'{name}: nenhum destaque idêntico ao título (nota antiga ou título editado)'); continue
        datada = re.search(r'datada de (\d{4})', n['summary'] + ' ' + n['body'])
        if h['year']:
            if datada and datada.group(1) != h['year']:
                erros.append(f'{name}: ano da nota ({datada.group(1)}) difere do destaque ({h["year"]})')
            elif not datada:
                avisos.append(f'{name}: o destaque traz {h["year"]} e a nota não o registra')
        elif datada:
            avisos.append(f'{name}: ano {datada.group(1)} não consta no destaque (confirmar que veio do autor)')
        sources.setdefault(n['source'], []).append(name)
        ok += 1
    if len(sources) > 1:
        comum = max(sources, key=lambda k: len(sources[k]))
        for k, nomes in sources.items():
            if k != comum:
                erros += [f'{x}: fonte diferente das demais notas do livro' for x in nomes]
    print(f'conferidas={len(files)} identicas_ao_destaque={ok} erros={len(erros)} avisos={len(avisos)}')
    for e in erros: print('ERRO ', e)
    for a in avisos: print('AVISO', a)
    sys.exit(1 if erros else 0)


main()
