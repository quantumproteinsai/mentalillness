"""Extract the CPAD 2.0 APR protein dropdown. Untrusted input: path as arg."""
import html, re, sys
h = open(sys.argv[1], encoding='utf-8', errors='replace').read()
opts = re.findall(r'<option value="([^"]*)"', h)
names = [html.unescape(o).strip() for o in opts if o and o != 'None']
seen, uniq = set(), []
for n in names:
    k = n.lower()
    if k not in seen:
        seen.add(k)
        uniq.append(n)
print(f'# raw options {len(opts)}, non-placeholder {len(names)}, unique case-insensitive {len(uniq)}')
for n in uniq:
    print(n)
