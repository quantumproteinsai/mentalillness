"""Screen candidate proteins against all three CPAD 2.0 tables.

PREREGISTRATION 5.2b item 4: a protein is CPAD-implicated if it appears in ANY of the
three tables. One table is not CPAD (hnRNPA1 is in structures only; LECT2 in the APR list
only; Orb2 in the APR list only). Searched by accession where a table carries one
(peptides only) and by normalised name everywhere, with positive and negative controls
through the same query, because an absence is only as good as the demonstrated sensitivity
of the search that produced it.

Untrusted downloaded HTML: paths are arguments, parsed, never executed.
  python3 -I cpad_screen_ten.py <apr_names.txt> <pep_dir> <str_dir>
"""
import html, os, re, sys

CANDIDATES = [
    # label,            accession, name variants to match in the tables
    ('TAF15',          'Q92804', ['taf15', 'tata-binding protein-associated factor 2n', 'taf 15', 'rna-binding protein 56']),
    ('hnRNPA1',        'P09651', ['hnrnpa1', 'hnrnp a1', 'heterogeneous nuclear ribonucleoprotein a1']),
    ('FapC',           'Q9I2F0', ['fapc']),
    ('cruciferin-3',   'Q96318', ['cruciferin', 'crc', '12s seed storage', 'cru3']),
    ('Orb2',           'Q9VSR3', ['orb2']),
    ('RIPK3',          'Q9Y572', ['ripk3', 'rip3', 'receptor-interacting serine/threonine-protein kinase 3']),
    ('Lysozyme',       'P61626', ['lysozyme']),
    ('RIPK1',          'Q13546', ['ripk1', 'rip1', 'receptor-interacting serine/threonine-protein kinase 1']),
    ('PMEL',           'P40967', ['pmel', 'premelanosome', 'silver locus', 'melanocyte protein']),
    ('Sup35NM',        'P05453', ['sup35', 'erf3', 'eukaryotic peptide chain release factor gtp-binding']),
]
POS_CONTROL = [('tau', 'P10636', ['tau', 'microtubule-associated protein tau']),
               ('beta2-microglobulin', 'P61769', ['beta2-microglobulin', 'beta-2-microglobulin']),
               ('transthyretin', 'P02766', ['transthyretin'])]
NEG_CONTROL = [('DISC1', 'Q9NRI5', ['disc1', 'disrupted in schizophrenia']),
               ('TRIOBP-1', 'Q9H2D6', ['triobp', 'tara', 'trio and f-actin-binding'])]


def table_rows(d, width):
    out = []
    for fn in sorted(os.listdir(d)):
        h = open(os.path.join(d, fn), encoding='utf-8', errors='replace').read()
        for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', h, flags=re.S | re.I):
            c = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()
                 for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, flags=re.S | re.I)]
            if len(c) == width and not c[0].startswith('Entry'):
                out.append(c)
    # de-duplicate by entry id, keep order
    seen, uniq = set(), []
    for r in out:
        if r[0] not in seen:
            seen.add(r[0])
            uniq.append(r)
    return uniq


def main(apr_path, pep_dir, str_dir):
    apr = [l.strip() for l in open(apr_path, encoding='utf-8')
           if l.strip() and not l.startswith('#')]
    pep = table_rows(pep_dir, 10)    # Entry Peptide Length Class ProteinName UniProt Mutant Ref PMID SrcDB
    stc = table_rows(str_dir, 11)    # Entry PDB ProteinName Species Length Mutation Class Type Method Res PMID
    print(f'TABLES: APR names {len(apr)} | peptide entries {len(pep)} '
          f'(ids {pep[0][0]}..{pep[-1][0]}) | structure entries {len(stc)} '
          f'(ids {stc[0][0]}..{stc[-1][0]})\n')

    def hits(acc, variants):
        v = [x.lower() for x in variants]
        a_hit = [n for n in apr if any(x in n.lower() for x in v)]
        p_hit = [r for r in pep if (acc and acc.lower() == r[5].strip().lower())
                 or any(x in r[4].lower() for x in v)]
        s_hit = [r for r in stc if any(x in r[2].lower() for x in v)]
        return a_hit, p_hit, s_hit

    for title, group in (('POSITIVE CONTROLS (must hit)', POS_CONTROL),
                         ('NEGATIVE CONTROLS (must stay absent)', NEG_CONTROL),
                         ('CANDIDATES', CANDIDATES)):
        print('=' * 78)
        print(title)
        print('=' * 78)
        for label, acc, variants in group:
            a, p, s = hits(acc, variants)
            verdict = 'CPAD_MEMBER' if (a or p or s) else 'ABSENT from all three'
            print(f'\n{label}  ({acc})  -> {verdict}')
            print(f'   APR list     : {len(a)}  {a[:4]}')
            print(f'   peptide table: {len(p)}  '
                  f'{sorted({r[4] + " [" + r[5] + "]" for r in p})[:3]}')
            print(f'   structures   : {len(s)}  '
                  f'{sorted({r[2] + " / " + r[3] for r in s})[:3]}')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:4]))
