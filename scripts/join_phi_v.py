#!/usr/bin/env python3
"""Join core polarity (Phi) to the predictor scores (v). PREREGISTRATION 10a §5.

Run only AFTER Phi is committed. The ordering is the point: Phi has three pre-specified
variants and a calibrated threshold, and this is the first moment either is allowed to
meet a predictor score.

    python3 scripts/join_phi_v.py <repo> [--phi <phi_rows.json>] [--expect-n <k>]

--phi selects which Phi file to join. It defaults to the 18 Nov run for backward
compatibility, but SHOULD BE GIVEN EXPLICITLY: the 19 Nov run exists at two layer counts
and over ten rows rather than seven, and a silent default is how an n changes without
anyone deciding that it should.

--expect-n asserts the size of the PRIMARY set and exits non-zero if it differs. PREREGISTRATION
10b S2 allows the Phi-v test to be recomputed ONCE, at the final n; the pool is not
exhausted, so any run today must be at n = 7 and must be a correction of the executed
layer-count deviation, not a new look at a larger set. The assertion is there so that
growing n requires editing a number on the command line.

v is taken from scripts/score_rows.py by running it and parsing its table, so the numbers
here are the committed pipeline's, not transcribed ones. Spearman rho with an EXACT
one-sided permutation p: at these sample sizes an asymptotic p would be meaningless, and
the minimum attainable p is printed beside the observed one.
"""
import itertools
import json
import math
import os
import re
import subprocess
import sys

CPAD_ABSENT = 'CPAD_ABSENT_ORTHOLOGY_CHECKED'
# TANGO v, phase 0, from the committed legacy runs (results/legacy_vs_modern_2026-11-17,
# results/glycinin_2026-11-17). The legacy arm was never run on FUS, hnRNPA1, SAA or
# LECT2, so the secondary analysis is necessarily smaller than the primary.
TANGO = {('TMEM106B', '120-254'): 0.7156, ('ANXA11', '39-74'): 0.4134,
         ('glycinin G4 (soybean)', '164-190'): 0.1645}


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def spearman(x, y):
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    dy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return num / (dx * dy) if dx and dy else 0.0


def exact_p(x, y):
    """One-sided: P(rho_permuted >= rho_observed). Exact over all n! permutations."""
    obs = spearman(x, y)
    n = len(x)
    cnt = tot = 0
    for perm in itertools.permutations(y):
        tot += 1
        if spearman(x, list(perm)) >= obs - 1e-12:
            cnt += 1
    return obs, cnt / tot, 1.0 / math.factorial(n)


def get_v(repo):
    out = subprocess.run([sys.executable, '-I', os.path.join(repo, 'scripts', 'score_rows.py'), repo],
                         capture_output=True, text=True, timeout=900).stdout
    v = {}
    for ln in out.split('\n'):
        m = re.match(r'^(.+?)\s+(\d+-\d+)\s+\S+\s+\S+\s+\d+\s+\d+\s+[\d.]+\s+([\d.]+)', ln)
        if m:
            v[(m.group(1).strip(), m.group(2))] = float(m.group(3))
    return v


def report(label, pairs, arm):
    if len(pairs) < 3:
        print(f'\n{label} ({arm}): n = {len(pairs)} — not reported, too few to rank.')
        return
    phi = [p[1] for p in pairs]
    vv = [p[2] for p in pairs]
    rho, p, minp = exact_p(phi, vv)
    print(f'\n{label} ({arm})  n = {len(pairs)}')
    for name, a, b in sorted(pairs, key=lambda z: -z[1]):
        print(f'    {name:26s} Phi={a:.3f}   v={b:.4f}')
    print(f'    Spearman rho = {rho:+.3f}   one-sided exact p = {p:.4f}'
          f'   (smallest attainable at this n: {minp:.4f})')
    if p > 0.05:
        print(f'    NOT SIGNIFICANT at the registered alpha = 0.05.')


def main(repo, phipath=None, expect_n=None):
    if phipath is None:
        phipath = os.path.join(repo, 'results', 'core_polarity_2026-11-18', 'phi_rows.json')
    print('Phi source:', os.path.relpath(phipath, repo))
    phis = json.load(open(phipath))
    rows = json.load(open(os.path.join(repo, 'data', 'regions.json')))['regions']
    idx = {(r['protein'], r['residues']): r for r in rows}
    v = get_v(repo)

    # map Phi labels back to rows via the structure field
    pairs_all, pairs_clean, pairs_tango = [], [], []
    for rec in phis:
        if rec.get('error'):
            continue
        pdb = rec['pdb']
        key = next((k for k, r in idx.items()
                    if (r.get('structure') or {}).get('pdb') == pdb), None)
        if key is None or key not in v:
            print('no v for', rec['label'])
            continue
        phi = rec['cut_10']['phi']
        name = '%s %s' % key
        pairs_all.append((name, phi, v[key]))
        if idx[key]['cpad_status'] == CPAD_ABSENT:
            pairs_clean.append((name, phi, v[key]))
        if key in TANGO:
            pairs_tango.append((name, phi, TANGO[key]))

    print('=' * 78)
    print('PREREGISTRATION 10a §5 — Phi vs v.  EXPLORATORY, PERMANENTLY.')
    print('Hypothesis: higher Phi (more polar core) -> higher v (worse recovery).')
    print('One-sided, alpha = 0.05.')
    print('=' * 78)
    report('PRIMARY: all eligible rows', pairs_all, 'modern / AggrescanAI')
    report('CPAD-absent rows only', pairs_clean, 'modern / AggrescanAI')
    report('SECONDARY: legacy arm', pairs_tango, 'legacy / TANGO')
    print('\nDISC1 and TRIOBP-1 have no deposited fibril structures and are absent from')
    print('every line above. The confirmatory stratum is not in this analysis.')
    if expect_n is not None and len(pairs_all) != expect_n:
        print('\n*** STOP. PRIMARY n = %d, but --expect-n said %d.' % (len(pairs_all), expect_n))
        print('    PREREGISTRATION 10b S2: the Phi-v test is recomputed ONCE, at the final n.')
        print('    If n has genuinely moved, that is a decision to record, not a default.')
        return 1
    return 0


if __name__ == '__main__':
    argv = sys.argv[1:]
    _phi = _expect = None
    if '--phi' in argv:
        i = argv.index('--phi'); _phi = argv[i + 1]; del argv[i:i + 2]
    if '--expect-n' in argv:
        i = argv.index('--expect-n'); _expect = int(argv[i + 1]); del argv[i:i + 2]
    raise SystemExit(main(argv[0] if argv else '.', _phi, _expect))
