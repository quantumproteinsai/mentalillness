#!/usr/bin/env python3
"""Screen an external fibril-core dataset against PREREGISTRATION 3.1b's m/M bar.

WHY. The 20 Nov prior-art audit found AmyloCore-ML (Singh J, Jangid R, Srivastava A,
bioRxiv 10.64898/2026.09.25.754455), which benchmarks AggrescanAI -- this project's own
modern arm -- on exactly the deposited fibril cores that PREREGISTRATION 3.1b excludes.
It does so with a PER-RESIDUE design (ordered = core, unresolved from the same protein =
matched control, AUROC/AUPRC), where the region-to-chain length ratio never enters.

So the question this script answers is NOT "is their work valid" -- it plainly is -- but:

    HOW MANY OF THEIR 82 REGIONS COULD ENTER A MIN-RANK BENCHMARK LIKE OURS?

A near-zero answer is a reportable fact about the field, and it is the sharpest available
statement of what 3.1b actually excludes. It also tests, on somebody else's independently
curated data, the claim that cryo-EM cores are systematically ineligible -- a claim our own
13 structural rows can only weakly support, being 13 rows we chose.

    python3 -I scripts/screen_amylocore.py <their_supplementary.csv> [out.json]

THE INPUT IS UNTRUSTED DOWNLOADED DATA and is read as a path argument, parsed as CSV, and
never executed. Nothing from it reaches data/regions.json; this script writes a report and
changes no project data.

THE ARITHMETIC IS THE PROJECT'S OWN, NOT A FRESH IMPLEMENTATION. It imports
scripts/score_rows.py for W and reproduces the tiling of apply_power_eligible.py exactly,
including the 3.1a short-region fallback. On 19 Nov an ad-hoc reimplementation of this
project's v pipeline bypassed a frame offset and produced a wrong correlation; nothing is
re-derived here that the committed code already defines.
"""
import csv
import importlib.util
import json
import os
import re
import sys

BAR = 0.05


def load_w(repo):
    spec = importlib.util.spec_from_file_location(
        'score_rows', os.path.join(repo, 'scripts', 'score_rows.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.W


def m_over_M(L, a, b, W):
    """PREREGISTRATION 3.1 tiling, with the 3.1a fallback. Returns (m, M, rule)."""
    starts = list(range(0, L - W + 1, W))
    M = len(starts)
    m = sum(1 for s in starts if s + 1 >= a and s + W <= b)
    rule = '3.1 tiling'
    if M and m == 0:
        Lr = b - a + 1
        if 1 <= Lr <= L:
            M, m = L - Lr + 1, 1
            rule = '3.1a sliding (region shorter than the window)'
    return m, M, rule


def main(repo, csvpath, outpath=None):
    W = load_w(repo)
    rows = []
    with open(csvpath, newline='', encoding='utf-8-sig') as fh:
        for rec in csv.DictReader(fh):
            name = (rec.get('Protein_name') or '').strip()
            if not name:
                continue
            try:
                L = int(str(rec.get('Protein_length')).strip())
            except (TypeError, ValueError):
                print(f'  SKIP {name}: unparseable Protein_length '
                      f'{rec.get("Protein_length")!r}')
                continue
            segs = re.findall(r'(\d+)\s*-\s*(\d+)', str(rec.get('Core_ranges') or ''))
            if not segs:
                print(f'  SKIP {name}: no parseable range in '
                      f'{rec.get("Core_ranges")!r}')
                continue
            for a, b in segs:
                a, b = int(a), int(b)
                if not (1 <= a <= b <= L):
                    print(f'  SKIP {name} {a}-{b}: outside a chain of {L}')
                    continue
                m, M, rule = m_over_M(L, a, b, W)
                if M == 0 or m == 0:
                    print(f'  SKIP {name} {a}-{b}: no window fits (L={L})')
                    continue
                r = m / M
                rows.append({
                    'protein': name, 'uniprot': (rec.get('UniProt_ID') or '').strip(),
                    'range': f'{a}-{b}', 'region_len': b - a + 1, 'chain_len': L,
                    'm': m, 'M': M, 'm_over_M': round(r, 6),
                    'rule': rule, 'power_eligible': r <= BAR,
                })

    rows.sort(key=lambda x: x['m_over_M'])
    elig = [x for x in rows if x['power_eligible']]
    prots = {x['protein'] for x in rows}

    print('\nSCREEN OF AN EXTERNAL FIBRIL-CORE DATASET AGAINST PREREGISTRATION 3.1b')
    print(f'  source CSV      : {csvpath}')
    print(f'  regions parsed  : {len(rows)} across {len(prots)} proteins')
    print(f'  window W        : {W} (imported from scripts/score_rows.py)')
    print(f'  bar             : m/M <= {BAR}')
    print()
    print(f'{"protein":28s} {"range":>12s} {"len":>5s} {"chain":>6s} {"m":>4s} '
          f'{"M":>4s} {"m/M":>8s}  eligible')
    print('-' * 86)
    for x in rows:
        print(f'{x["protein"][:28]:28s} {x["range"]:>12s} {x["region_len"]:>5d} '
              f'{x["chain_len"]:>6d} {x["m"]:>4d} {x["M"]:>4d} {x["m_over_M"]:>8.4f}'
              f'  {"YES" if x["power_eligible"] else ""}')

    print()
    print('=' * 86)
    print(f'ELIGIBLE: {len(elig)} of {len(rows)} regions '
          f'({len(elig) / len(rows) * 100:.1f}%), '
          f'across {len({x["protein"] for x in elig})} of {len(prots)} proteins')
    if elig:
        for x in elig:
            print(f'    {x["protein"]} {x["range"]}  m/M = {x["m_over_M"]:.4f}')
    print()
    med = sorted(x['m_over_M'] for x in rows)[len(rows) // 2]
    print(f'  median m/M : {med:.4f}   ({med / BAR:.0f}x the bar)')
    print(f'  minimum m/M: {rows[0]["m_over_M"]:.4f}  ({rows[0]["protein"]} '
          f'{rows[0]["range"]})')
    print(f'  maximum m/M: {rows[-1]["m_over_M"]:.4f}  ({rows[-1]["protein"]} '
          f'{rows[-1]["range"]})')

    if outpath:
        json.dump({
            '_what': 'PREREGISTRATION 3.1b applied to an externally curated fibril-core '
                     'dataset. Reports eligibility only; admits nothing and changes no '
                     'project data.',
            '_source': csvpath,
            '_window': W, '_bar': BAR,
            'n_regions': len(rows), 'n_proteins': len(prots),
            'n_eligible': len(elig), 'rows': rows,
        }, open(outpath, 'w'), indent=1)
        print(f'\nwrote {outpath}')
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None))
