"""Gera os drafts de notas category:quote a partir dos destaques pendentes de um livro.

Uso:
  python -I generate.py --lib <library/livro.md> --hl <pendentes.json> --out <pasta-drafts> \
                        --book <book.json> [--confirm <confirm.json>] [--skip 76,100] [--accept 293,712]
                        [--since YYYY-MM-DD] [--auto] [--skip-collision]

  --hl        saída de crossmatch.py --json (os pendentes, com texto completo).
  --book      {"title","short_title"(opcional),"author","publisher"(opcional),"year"(opcional),
               "tag","anthology": true|false, "lang": "pt"|"en" (idioma das notas; padrão pt),
               "pronoun": "ele"|"ela" (padrão ele), "sections": [...] (opcional, ver abaixo)}
  --confirm   antologia: {"<loc>": {"author": "Nome Completo", "tag": "slug-tag", "year": "1785"}}
              autor único: {"<loc>": {"cites": true}}  (cita outro autor, não identificado)
                           {"<loc>": {"cites": "Montaigne", "tag": "michel-de-montaigne",
                                      "ref": "*Ensaios* I.20", "url": "https://..."}}  (identificado)
                           {"<loc>": {"cites": false}}  (desfaz um falso positivo das heurísticas)
  --skip      locs a ignorar (decisão do autor).
  --accept    locs de destaques curtos/cortados que o autor mandou importar assim mesmo.
  --since     só destaques com added >= data (importação autônoma de livro já em andamento).
  --auto      rotina autônoma: destaque curto/cortado vira nota com a tag destaque-cortado (não pendência).
  --skip-collision  só para testes: não trata slug existente como erro.

Antologia (anthology=true): o título é a frase sem a atribuição do fim (kh.split_attribution) e o autor vem
de authors.json ou de --confirm. Livro de autor único (false): título = destaque inteiro; autor = o do livro.

Seções ("sections": [{"from_loc": 1072, "to_loc": null, "author": "David Hume", "tag": "david-hume"}]):
trecho de outro autor dentro de livro de autor único (apêndice, prefácio). O destaque no intervalo é
"Citação de <autor da seção> reunida por <autor do livro>", com a tag do autor da seção.

Heurísticas (autor único, fora de seção; --confirm prevalece):
  A. destaque abre com aspas («“‘") -> cita outro autor.
  B. destaque menciona o sobrenome do autor do livro -> texto de outro autor sobre a obra (prefácio etc.).
  Ambas gravam a nota com a tag de autor não confirmado no idioma da nota (pt: autor-nao-confirmado,
  en: author-to-be-confirmed). Melhor marcar à toa do que atribuir errado.

Nome ausente de authors.json, destaque sem autor, destaque cortado (fora de --accept/--auto) e slug que
já existe NÃO viram draft: saem como PENDENTE e o código de saída é 2.
"""
import argparse, glob, json, os, re, sys, io, unicodedata

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kh  # noqa: E402

TAG_UNCONFIRMED = {'pt': 'autor-nao-confirmado', 'en': 'author-to-be-confirmed'}
TAG_CUT = 'destaque-cortado'   # uma tag só, em qualquer idioma: o autor busca os cortados de uma vez
OPEN_QUOTES = ('«', '“', '‘', '"', "'")


def slugify(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def yaml_dq(s):
    return s.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))


def is_cut(title, anthology):
    if anthology:
        return title.endswith('...') or len(title) < 12
    return len(title) < 25 or title.rstrip().endswith(('...', '…', ',', ';'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lib', required=True)
    ap.add_argument('--hl', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--book', required=True)
    ap.add_argument('--confirm')
    ap.add_argument('--skip', default='')
    ap.add_argument('--since', default='')
    ap.add_argument('--accept', default='')
    ap.add_argument('--auto', action='store_true')
    ap.add_argument('--skip-collision', action='store_true')
    a = ap.parse_args()

    book = json.load(open(a.book, encoding='utf-8'))
    anthology = book.get('anthology', True)
    lang = book.get('lang') or 'pt'
    pron = book.get('pronoun') or 'ele'
    sections = book.get('sections') or []
    tag_unc = TAG_UNCONFIRMED[lang]
    authors = json.load(open(os.path.join(HERE, 'authors.json'), encoding='utf-8'))
    confirm = json.load(open(a.confirm, encoding='utf-8')) if a.confirm else {}
    skip = {int(x) for x in a.skip.split(',') if x.strip()}
    accept = {int(x) for x in a.accept.split(',') if x.strip()}
    # Pendente = par (loc, texto): dois destaques podem dividir a mesma loc, e indexar só pela loc
    # descartava um deles em silêncio (Notes on Suicide, 2026-11-02: 4 pares).
    pending = {(int(h['loc']), h['text'].strip()) for h in json.load(open(a.hl, encoding='utf-8'))}
    todos = [h for h in kh.highlights(a.lib) if (h['loc'], h['raw']) in pending]
    existing = {os.path.basename(f)[:-3] for f in glob.glob(r'E:\scholion\content\notes\*.md')}
    os.makedirs(a.out, exist_ok=True)
    editora = book.get('publisher')
    ano_livro = book.get('year')
    ed_ano = ' (' + ', '.join(str(x) for x in (editora, ano_livro) if x) + ')' if (editora or ano_livro) else ''
    livro, autor_livro = book.get('short_title', book['title']), book['author']  # livro = nome nos textos
    tag_livro_autor = slugify(autor_livro)
    sobrenome = re.compile(r'\b' + re.escape(autor_livro.split()[-1]) + r'\b')

    def secao(loc):
        for s in sections:
            if loc >= s['from_loc'] and (s.get('to_loc') is None or loc <= s['to_loc']):
                return s
        return None

    gerados, pendencias = [], []
    for h in sorted(todos, key=lambda h: h['loc']):  # sort estável: mantém a ordem do livro na mesma loc
        loc = h['loc']
        if loc in skip:
            continue
        if a.since and h['added'] and h['added'] < a.since:
            continue
        title, year = h['text'], h['year']
        flags = []
        sec = None
        cites = None   # None | True (não identificado) | dict (identificado)
        sobre = False
        c = confirm.get(str(loc)) or {}
        if anthology:
            if c.get('author'):
                nome, tag, year = c['author'], c['tag'], c.get('year', year)
            elif h['name'] is None:
                pendencias.append(f'loc {loc}: SEM AUTOR no destaque: "{h["raw"][:80]}..."'); continue
            elif h['name'] not in authors:
                pendencias.append(f'loc {loc}: nome "{h["name"]}" fora de authors.json'); continue
            else:
                nome, tag = authors[h['name']]['name'], authors[h['name']]['tag']
        else:
            title, year = h['raw'], None
            sec = secao(loc)
            if sec:
                nome, tag = sec['author'], sec['tag']
            else:
                nome, tag = autor_livro, tag_livro_autor
                if 'cites' in c:
                    if isinstance(c['cites'], str):
                        cites = c
                    elif c['cites']:
                        cites = True
                elif title.lstrip().startswith(OPEN_QUOTES):
                    cites = True                                   # heurística A
                if cites is None and 'cites' not in c and sobrenome.search(title):
                    sobre = True                                   # heurística B
        if is_cut(title, anthology):
            if loc in accept or (a.auto and not anthology):
                flags.append('cortado')
            else:
                pendencias.append(f'loc {loc}: destaque curto ou cortado: "{title[:60]}"'); continue
        base = slugify(title)[:50].rstrip('-')
        if base in existing and not a.skip_collision:
            pendencias.append(f'loc {loc}: slug "{base}" já existe (nota existente? voltar ao crossmatch)'); continue

        extra_tags = []
        if year:
            de = 'do' if str(year).startswith('século') else 'de'   # "datada do século IV a.C."
            summ = f'Citação de {nome}, datada {de} {year} em {livro}, de {autor_livro}{ed_ano}.'
            corpo = f'Passagem de {nome}, datada {de} {year} em {livro}, de {autor_livro}.'
        elif anthology or sec:
            summ = f'Citação de {nome} reunida por {autor_livro} em {livro}{ed_ano}.'
            corpo = f'Passagem de {nome} reunida por {autor_livro} em {livro}.'
        elif sobre:
            summ = f'Trecho de {livro}, de {autor_livro}{ed_ano}, escrito por outro autor sobre a obra.'
            corpo = f'Trecho de {livro}, de {autor_livro}, escrito por outro autor sobre a obra.'
            extra_tags.append(tag_unc); flags.append('sobre-a-obra')
        elif isinstance(cites, dict):
            quem = cites['cites']
            summ = f'Passagem de {livro}, de {autor_livro}{ed_ano}, em que {pron} cita {quem}.'
            det = (f', {cites["ref"]}' if cites.get('ref') else '') + (f' ([fonte]({cites["url"]}))' if cites.get('url') else '')
            corpo = f'Passagem de {livro}, de {autor_livro}, em que {pron} cita {quem}{det}.'
            if cites.get('tag'):
                extra_tags.insert(0, ('quoted', cites['tag']))
            flags.append(f'cita:{quem}')
        elif cites:
            summ = f'Passagem de {livro}, de {autor_livro}{ed_ano}, em que {pron} cita outro autor.'
            corpo = f'Passagem de {livro}, de {autor_livro}, em que {pron} cita outro autor.'
            extra_tags.append(tag_unc); flags.append('cita-outro')
        else:
            summ = f'Passagem de {livro}, de {autor_livro}{ed_ano}.'
            corpo = f'Passagem de {livro}, de {autor_livro}.'

        if sec:
            tags = [tag]
        elif sobre:
            tags = []          # o autor do livro não é o autor do trecho
        else:
            tags = [tag] if tag == tag_livro_autor else [tag, tag_livro_autor]
        tags += [t[1] for t in extra_tags if isinstance(t, tuple)]
        tags.append(book['tag'])
        tags += [t for t in extra_tags if isinstance(t, str)]
        if 'cortado' in flags:
            tags.append(TAG_CUT)
        fonte = (f'  - title: "{yaml_dq(book["title"])}"\n'
                 f'    author: "{autor_livro}"\n')
        if ano_livro: fonte += f'    year: {ano_livro}\n'
        if editora: fonte += f'    publisher: "{editora}"\n'
        fonte += '    kind: book\n'
        md = (
            '---\n'
            f'title: "{yaml_dq(title)}"\n'
            "date: 'DATE'\n"
            'category: quote\n'
            f"summary: '{summ.replace(chr(39), chr(39) * 2)}'\n"
            'tags: [' + ', '.join(f'"{t}"' for t in dict.fromkeys(tags)) + ']\n'
            'has_commentary: false\n'
            'sources:\n'
            + fonte +
            '---\n\n'
            f'{corpo}\n')
        existing.add(base)
        open(os.path.join(a.out, base + '.md'), 'w', encoding='utf-8', newline='\n').write(md)
        gerados.append((loc, nome, year, base, flags))

    marcadas = sum(1 for g in gerados if any(f in ('cita-outro', 'sobre-a-obra') for f in g[4]))
    cortadas = sum(1 for g in gerados if 'cortado' in g[4])
    print(f'gerados={len(gerados)} pendencias={len(pendencias)} '
          f'pulados={sum(1 for h in todos if h["loc"] in skip)} autor_nao_confirmado={marcadas} cortados={cortadas}')
    for loc, nome, year, base, flags in gerados:
        print(f'  loc {loc} | {nome} ({year or "s/d"}) | {base}' + (f' | {",".join(flags)}' if flags else ''))
    for p in pendencias:
        print('PENDENTE', p)
    sys.exit(2 if pendencias else 0)


main()
