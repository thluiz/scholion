import json, sys
import xml.etree.ElementTree as ET

src, dst = sys.argv[1], sys.argv[2]
x = json.load(open(src, encoding='utf-8'))['data']['xml']
root = ET.fromstring(x)


def inline(el):
    out = el.text or ''
    for c in el:
        t = inline(c)
        if c.tag == 'bold':
            t = f'**{t}**'
        elif c.tag == 'italic':
            t = f'*{t}*'
        elif c.tag == 'link':
            t = f"[{t}]({c.get('href')})"
        elif c.tag == 'date':
            t = c.get('value')
        elif c.tag == 'mention':
            t = '@autor'
        out += t + (c.tail or '')
    return out


lines = []


def block(el, depth=0, prefix=''):
    if el.tag == 'paragraph':
        h = el.get('heading')
        txt = inline(el)
        if h:
            lines.append('')
            lines.append('#' * int(h) + ' ' + txt)
            lines.append('')
        elif prefix:
            lines.append(prefix + txt)
        else:
            lines.append('')
            lines.append(txt)
    elif el.tag == 'list':
        ordered = el.get('kind') == 'ordered'
        lines.append('') if depth == 0 else None
        for i, li in enumerate(el, 1):
            mark = f'{i}. ' if ordered else '- '
            first = True
            for c in li:
                if c.tag == 'paragraph' and first:
                    block(c, depth + 1, '  ' * depth + mark)
                    first = False
                else:
                    block(c, depth + 1, '  ' * (depth + 1))
    elif el.tag == 'table':
        lines.append('')
        for ri, row in enumerate(el):
            cells = [' '.join(inline(p) for p in cell).replace('|', '/') for cell in row]
            lines.append('| ' + ' | '.join(cells) + ' |')
            if ri == 0:
                lines.append('|' + ' --- |' * len(cells))
        lines.append('')
    else:
        for c in el:
            block(c, depth, prefix)


for c in root:
    block(c)
open(dst, 'w', encoding='utf-8').write('\n'.join(lines).strip() + '\n')
