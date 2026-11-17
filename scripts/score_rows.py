#!/usr/bin/env python3
"""Compute the PREREGISTRATION 3.1 statistic for AggrescanAI. No tuning, no choices left.

  window = 6 (5.3: PLM tools per-residue, aggregated to 6-residue means)
  M = windows in protein; m = windows WHOLLY inside the region
  P = (# windows scoring <= region's best window) / M, MIDRANK ties
  v = 1 - P^m        ~ Uniform(0,1) under H0; small v = predictor succeeded

Combination: Stouffer's Z primary (equal weights, one-sided), Fisher secondary.
Both always reported (3.1).
"""
import csv
import json
import math
import os
import re
import sys

W = 6
HERE = os.path.dirname(os.path.abspath(__file__))

# row protein -> the run file, and the frame that run is in.
RUNS = {
    'TRIOBP-1': ('runs/Q9H2D6-7.csv', '652-residue (Q9H2D6-7)'),
    'DISC1': ('runs/Q9NRI5.csv', '854-residue canonical (Q9NRI5)'),
    'tau': ('runs/P10636-8.csv', 'tau441 / ht40 (P10636-8)'),
    'alpha-synuclein': ('runs/P37840_asyn.csv', 'P37840, 140 aa'),
    'FUS': ('runs/P35637.csv', 'P35637, 526 aa'),
    'hnRNPA1': ('runs/P09651-2.csv', 'P09651-2, 320 aa'),
}


def load(path):
    out = []
    with open(os.path.join(HERE, path)) as fh:
        for r in csv.DictReader(l for l in fh if not l.startswith('#')):
            out.append(float(r['aggrescanai_score']))
    return out


def statistic(scores, a, b, phase=0):
    """a,b inclusive 1-based region bounds. NON-OVERLAPPING tiling, offset `phase`.

    WHY TILING AND NOT A SLIDING WINDOW. 3.1 states both a procedure and the property
    it must have: "v ~ Uniform(0, 1)" under H0. Sliding windows overlap by 5 of 6
    residues, so they are NOT exchangeable, and simulation on i.i.d. scores gives
    mean v = 0.663, median 0.767 -- biased toward "the predictor failed". Tiling gives
    mean 0.495 and quantiles within 0.006 of uniform. The document's own stated null
    therefore selects tiling. The criterion is the pre-registration's, not the analyst's.
    """
    wins, starts = [], []
    for i in range(phase, len(scores) - W + 1, W):
        wins.append(sum(scores[i:i + W]) / W)
        starts.append(i + 1)               # 1-based start
    M = len(wins)
    idx = [j for j in range(M) if starts[j] >= a and starts[j] + W - 1 <= b]
    m = len(idx)
    if m == 0:
        return None
    best = max(wins[i] for i in idx)
    less = sum(1 for x in wins if x < best)
    eq = sum(1 for x in wins if x == best)
    P = (less + 0.5 * eq) / M          # midrank
    v = 1.0 - P ** m
    return {'M': M, 'm': m, 'best_window_score': best, 'P': P, 'v': v}


def norm_isf(p):
    """One-sided z for upper-tail probability p, via inverse erf."""
    # z = sqrt(2) * erfinv(1 - 2p)
    x = 1.0 - 2.0 * p
    # Acklam-free: use math.erf inversion by bisection (exact enough, cheap)
    lo, hi = -40.0, 40.0
    for _ in range(300):
        mid = (lo + hi) / 2
        if math.erf(mid / math.sqrt(2)) < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def chi2_sf(x, k):
    """Upper tail of chi-square with k df (k even here: k=2n)."""
    if k % 2 == 0:
        m = k // 2
        t = math.exp(-x / 2)
        s = t
        for i in range(1, m):
            t *= (x / 2) / i
            s += t
        return min(1.0, max(0.0, s))
    raise ValueError('even df only')


def main(repo):
    d = json.loads(open(os.path.join(repo, 'data', 'regions.json')).read())
    cache = {}
    results = []
    skipped = []
    for r in d['regions']:
        prot = r['protein']
        res = r['residues']
        if prot not in RUNS:
            skipped.append((prot, res, 'no run: mature-chain frame not yet resolved'))
            continue
        if not re.fullmatch(r'\d+-\d+', res.strip()):
            skipped.append((prot, res, 'composite/irregular range -- not a single interval'))
            continue
        if not r.get('frame') or r['frame'] == 'ABSENT':
            skipped.append((prot, res, 'row carries NO frame; descriptor rule: do not assume'))
            continue
        path, frame = RUNS[prot]
        if path not in cache:
            cache[path] = load(path)
        sc = cache[path]
        a, b = (int(x) for x in res.split('-'))
        if b > len(sc):
            skipped.append((prot, res, f'range exceeds sequence length {len(sc)}'))
            continue
        st = statistic(sc, a, b, phase=0)
        if st is None:
            skipped.append((prot, res, f'region shorter than the {W}-residue window'))
            continue
        # Phase is a free parameter the pre-registration does not fix. Report the
        # spread across all 6 offsets so a conclusion that depends on it is visible.
        alt = [statistic(sc, a, b, phase=p) for p in range(W)]
        vs = [x['v'] for x in alt if x]
        st['v_phase_min'], st['v_phase_max'] = min(vs), max(vs)
        st.update(protein=prot, residues=res, stratum=r['stratum'],
                  cpad=r['cpad_status'], circ=r['circularity_status'], frame=frame)
        results.append(st)

    results.sort(key=lambda x: x['v'])
    print(f'{"protein":18s} {"region":12s} {"stratum":22s} {"cpad":30s} {"m":>4s} {"M":>5s} {"P":>8s} {"v":>10s}')
    print('-' * 125)
    for x in results:
        print(f'{x["protein"]:18s} {x["residues"]:12s} {x["stratum"]:22s} {x["cpad"]:30s} '
              f'{x["m"]:4d} {x["M"]:5d} {x["P"]:8.5f} {x["v"]:10.6f}  [{x["v_phase_min"]:.3f}-{x["v_phase_max"]:.3f}]')
    print()
    if skipped:
        print('NOT SCORED:')
        for p, res, why in skipped:
            print(f'  {p:18s} {res:18s} {why}')
        print()

    def combine(rows, label):
        if not rows:
            print(f'{label}: no rows'); return
        n = len(rows)
        vs = [min(max(x['v'], 1e-16), 1 - 1e-16) for x in rows]
        zs = [norm_isf(v) for v in vs]           # small v -> large positive z
        Z = sum(zs) / math.sqrt(n)
        pZ = 0.5 * math.erfc(Z / math.sqrt(2))
        chi = -2 * sum(math.log(v) for v in vs)
        pF = chi2_sf(chi, 2 * n)
        print(f'{label}  (n={n})')
        print(f'    rows        : ' + ', '.join(f'{x["protein"]} {x["residues"]}' for x in rows))
        print(f'    Stouffer Z  = {Z:+.4f}   one-sided p = {pZ:.4f}   [PRIMARY]')
        print(f'    Fisher chi2 = {chi:.4f} on {2*n} df   p = {pF:.4f}   [secondary]')
        print()

    conf = [x for x in results
            if x['stratum'].startswith('DISCORDANT')
            and x['cpad'] == 'CPAD_ABSENT_ORTHOLOGY_CHECKED'
            and x['circ'] == 'CLEAN']
    print('=' * 125)
    combine(conf, 'CONFIRMATORY (5.2b item 5: discordant, CPAD-absent, circularity CLEAN)')
    combine([x for x in results if x['cpad'] == 'CPAD_MEMBER'],
            'CPAD-CONTAMINATED ROWS (reported separately, EXCLUDED from the primary)')
    combine([x for x in results if x['circ'] == 'CLEAN'
             and x['cpad'] == 'CPAD_ABSENT_ORTHOLOGY_CHECKED'],
            'ALL CPAD-ABSENT, CIRCULARITY-CLEAN ROWS (exploratory: mixes strata)')


if __name__ == '__main__':
    main(sys.argv[1])
