"""Parse the three CPAD 2.0 browse pages into plain text rows. Untrusted input: paths as args."""
import html, re, sys

def rows(path):
    h = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', h, flags=re.S | re.I):
        cells = [html.unescape(re.sub(r'<[^>]+>', ' ', c)).strip()
                 for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, flags=re.S | re.I)]
        cells = [re.sub(r'\s+', ' ', c) for c in cells]
        if any(cells):
            out.append(cells)
    return out

for p in sys.argv[1:]:
    r = rows(p)
    print(f'=== {p}: {len(r)} <tr> rows, widths {sorted({len(x) for x in r})}')
    for x in r[:3]:
        print('   ', x)
