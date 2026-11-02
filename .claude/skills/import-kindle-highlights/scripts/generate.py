"""Gera os drafts de notas category:quote a partir dos destaques pendentes de um livro.

Uso:
  python -I generate.py --lib <library/livro.md> --hl <pendentes.json> --out <pasta-drafts> \
                        --book <book.json> [--confirm <confirm.json>] [--skip 76,100] [--skip-collision]

  --hl        saída de crossmatch.py --json (os pendentes, com texto completo).
  --book      {"title","short_title"(opcional, nome do livro nos textos),"author","publisher","year","tag","anthology": true|false}
  --confirm   {"<loc>": {"author": "Nome Completo", "tag": "slug-tag", "year": "1785"}}  autoria
              confirmada pelo autor para destaques sem atribuição no livro. Nunca preencher por conta própria.
  --skip      locs a ignorar (decisão do autor).
  --skip-collision  só para testes: não trata slug existente como erro.

Regras: o título é a frase do destaque sem a atribuição do fim (kh.split_attribution), sem nenhuma outra
edição. Nome ausente de authors.json, destaque sem autor e slug que já existe NÃO viram draft: saem na
lista final e o código de saída é 2, para a skill perguntar ao autor.
"""
import argparse, glob, json, os, re, sys, io, unicodedata

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kh  # noqa: E402


def slugify(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def yaml_dq(s):
    return s.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lib', required=True)
    ap.add_argument('--hl', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--book', required=True)
    ap.add_argument('--confirm')
    ap.add_argument('--skip', default='')
    ap.add_argument('--skip-collision', action='store_true')
    a = ap.parse_args()

    book = json.load(open(a.book, encoding='utf-8'))
    authors = json.load(open(os.path.join(HERE, 'authors.json'), encoding='utf-8'))
    confirm = json.load(open(a.confirm, encoding='utf-8')) if a.confirm else {}
    skip = {int(x) for x in a.skip.split(',') if x.strip()}
    pending = {int(h['loc']) for h in json.load(open(a.hl, encoding='utf-8'))}
    by_loc = {h['loc']: h for h in kh.highlights(a.lib)}
    existing = {os.path.basename(f)[:-3] for f in glob.glob(r'E:\scholion\content\notes\*.md')}
    os.makedirs(a.out, exist_ok=True)

    gerados, pendencias = [], []
    for loc in sorted(pending - skip):
        h = by_loc[loc]
        title, year = h['text'], h['year']
        if book.get('anthology', True):
            c = confirm.get(str(loc))
            if c:
                nome, tag, year = c['author'], c['tag'], c.get('year', year)
            elif h['name'] is None:
                pendencias.append(f'loc {loc}: SEM AUTOR no destaque: "{h["raw"][:80]}..."'); continue
            elif h['name'] not in authors:
                pendencias.append(f'loc {loc}: nome "{h["name"]}" fora de authors.json'); continue
            else:
                nome, tag = authors[h['name']]['name'], authors[h['name']]['tag']
            if title.endswith('...') or len(title) < 12:
                pendencias.append(f'loc {loc}: destaque curto ou cortado: "{title}"'); continue
        else:
            nome, tag, title, year = book['author'], slugify(book['author']), h['raw'], None
        base = slugify(title)[:50].rstrip('-')
        if base in existing and not a.skip_collision:
            pendencias.append(f'loc {loc}: slug "{base}" já existe (nota existente? voltar ao crossmatch)'); continue
        livro, autor_livro = book.get('short_title', book['title']), book['author']  # livro = nome nos textos
        if year:
            summ = f'Citação de {nome}, datada de {year} em {livro}, de {autor_livro} ({book["publisher"]}, {book["year"]}).'
            corpo = f'Passagem de {nome}, datada de {year} em {livro}, de {autor_livro}.'
        elif book.get('anthology', True):
            summ = f'Citação de {nome} reunida por {autor_livro} em {livro} ({book["publisher"]}, {book["year"]}).'
            corpo = f'Passagem de {nome} reunida por {autor_livro} em {livro}.'
        else:
            summ = f'Passagem de {livro}, de {autor_livro} ({book["publisher"]}, {book["year"]}).'
            corpo = f'Passagem de {livro}, de {autor_livro}.'
        tags = [tag] if tag == slugify(autor_livro) else [tag, slugify(autor_livro)]
        tags.append(book['tag'])
        md = (
            '---\n'
            f'title: "{yaml_dq(title)}"\n'
            "date: 'DATE'\n"
            'category: quote\n'
            f"summary: '{summ.replace(chr(39), chr(39) * 2)}'\n"
            'tags: [' + ', '.join(f'"{t}"' for t in dict.fromkeys(tags)) + ']\n'
            'has_commentary: false\n'
            'sources:\n'
            f'  - title: "{yaml_dq(book["title"])}"\n'
            f'    author: "{autor_livro}"\n'
            f'    year: {book["year"]}\n'
            f'    publisher: "{book["publisher"]}"\n'
            '    kind: book\n'
            '---\n\n'
            f'{corpo}\n')
        existing.add(base)
        open(os.path.join(a.out, base + '.md'), 'w', encoding='utf-8', newline='\n').write(md)
        gerados.append((loc, nome, year, base))

    print(f'gerados={len(gerados)} pendencias={len(pendencias)} pulados={len(skip & pending)}')
    for loc, nome, year, base in gerados:
        print(f'  loc {loc} | {nome} ({year or "s/d"}) | {base}')
    for p in pendencias:
        print('PENDENTE', p)
    sys.exit(2 if pendencias else 0)


main()
