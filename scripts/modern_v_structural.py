#!/usr/bin/env python3
"""AggrescanAI v for the rows recruited under PREREGISTRATION 10b/10c. The modern arm.

Mirrors scripts/tango_v_structural.py exactly: same imported section 3.1 statistic, same
frame assertion, same refusal of non-contiguous regions, same reporting of the smallest v
the statistic can return. The two arms must be compared, so they must be computed the same
way, and the only difference permitted here is which profile is read.

    python3 scripts/modern_v_structural.py <repo> <profile_dir> <out.json>

THIS SCRIPT DOES NOT ADMIT A ROW TO THE BENCHMARK. Computing v is not admission. Both rows
were recruited under section 10b FOR THE CORE-POLARITY ANALYSIS, where m/M is explicitly not
a criterion, and the Orb2 row's own power_limit field says so in capitals: entry to the
benchmark arm is a separate decision under the eight-stage pipeline and 5.2b. So these two
are deliberately NOT added to score_rows.RUNS, and nothing here feeds the confirmatory
statistic. What these numbers are FOR is the Phi-v join of section 10a section 5 -- which
PREREGISTRATION 10b S2 allows to be recomputed ONCE, at the final n, and the pool is not
exhausted, so not today.
"""
import json
import os
import sys

BAR = 0.05                   # PREREGISTRATION 4

ROWS = [
    (('Orb2 (Drosophila melanogaster)', '176-206'), 'Q9VSR3.csv',
     'Q9VSR3 canonical, 704 aa, which IS the Orb2B frame'),
    (('beta-2-microglobulin', '22-85'), 'B2M_mature.csv',
     'P61769 MINUS the 20-residue signal peptide = mature 99 aa, I1..M99'),
]

REFUSED = {
    ('SOD1 (superoxide dismutase [Cu-Zn])', '3-55,86-153'):
        'NON-CONTIGUOUS (PREREGISTRATION 10c C3). Two segments with a 30-residue gap at '
        '56-85; the 3.1 statistic tiles a contiguous span. Refused on contiguity, NOT on '
        'm/M. The modern arm was not run on this chain at all, because there is nothing '
        'the number could be used for.',
}


def load_profile(path):
    seq, sc = [], []
    with open(path) as fh:
        for ln in fh:
            if ln.startswith('#') or ln.startswith('position,') or not ln.strip():
                continue
            p, a, s, d = ln.rstrip('\n').split(',')
            seq.append(a)
            sc.append(float(s))
    return ''.join(seq), sc


def floor_v(M, m):
    return 1.0 - ((M - 0.5) / M) ** m


def main(repo, profdir, outpath):
    sys.path.insert(0, os.path.join(repo, 'scripts'))
    from score_rows import statistic, W

    idx = {(r['protein'], r['residues']): r
           for r in json.load(open(os.path.join(repo, 'data', 'regions.json')))['regions']}
    results = {}
    print('W = %d, non-overlapping tiling, phase 0, AggrescanAI per-residue probability\n' % W)

    for key, reason in REFUSED.items():
        print('=' * 76)
        print('%s %s' % key)
        print('  NO v COMPUTED, BY RULE. %s' % reason)
        results['%s %s' % key] = {'v': None, 'refused': True, 'reason': reason}
        print()

    for key, fn, frame in ROWS:
        prot, res = key
        a, b = (int(x) for x in res.split('-'))
        row = idx[key]
        seq, sc = load_profile(os.path.join(profdir, fn))
        got = seq[a - 1:b]
        if got != row['sequence']:
            raise SystemExit('FRAME MISMATCH on %s %s\n  profile[%d:%d] = %s\n'
                             '  row sequence     = %s' % (prot, res, a, b, got,
                                                          row['sequence']))
        st = statistic(sc, a, b, phase=0)
        if st is None:
            raise SystemExit('statistic returned None for %s %s' % key)
        fl = floor_v(st['M'], st['m'])
        forced = fl >= BAR

        # where does the predictor's own maximum sit?
        wins = [(sum(sc[i:i + W]) / W, i + 1) for i in range(0, len(sc) - W + 1, W)]
        inside = [w for w in wins if w[1] >= a and w[1] + W - 1 <= b]
        gmax, rmax = max(wins), max(inside)
        rank = sorted(wins, reverse=True).index(rmax) + 1

        print('=' * 76)
        print('%s %s   profile %s' % (prot, res, fn))
        print('  scored frame: %s' % frame)
        print('  frame check: profile[%d:%d] == row["sequence"]  (%d aa) OK'
              % (a, b, len(row['sequence'])))
        print('  chain L=%d  M=%d windows  m=%d wholly inside  m/M=%.4f'
              % (len(seq), st['M'], st['m'], st['m'] / st['M']))
        print('  P=%.4f  v=%.4f' % (st['P'], st['v']))
        print('  SMALLEST v ATTAINABLE AT THIS M,m: %.4f' % fl)
        print('  chain max window   : start %3d  score %.4f' % (gmax[1], gmax[0]))
        print('  region best window : start %3d  score %.4f  -> rank %d of %d'
              % (rmax[1], rmax[0], rank, st['M']))
        print('  region holds the chain maximum: %s' % (rmax == gmax))
        call = 'DISCORDANT' if st['v'] >= BAR else 'CONCORDANT'
        print('  at the %.2f bar this row reads: %s' % (BAR, call))
        if forced:
            print('  *** FORCED: the floor %.4f is at or above the bar, so this reads'
                  % fl)
            print('      DISCORDANT for ANY predictor output. The number is a fact about')
            print('      the region length, not about AggrescanAI.')
        results['%s %s' % key] = {
            'profile': fn, 'scored_frame': frame, 'chain_length': len(seq),
            'v': st['v'], 'P': st['P'], 'M': st['M'], 'm': st['m'],
            'm_over_M': st['m'] / st['M'], 'floor_v': fl,
            'call_forced_by_information_limit': forced,
            'region_best_window_start': rmax[1], 'region_best_window_score': rmax[0],
            'region_best_window_rank': rank,
            'chain_max_window_start': gmax[1], 'chain_max_window_score': gmax[0],
            'region_holds_chain_max': rmax == gmax,
            'call': call, 'refused': False}
        print()

    print('=' * 76)
    json.dump(results, open(outpath, 'w'), indent=1)
    print('wrote', outpath)
    print('\nNOT DONE HERE, DELIBERATELY: these rows are not added to score_rows.RUNS and')
    print('feed no confirmatory statistic, and the Phi-v join is not recomputed (10b S2:')
    print('once, at the final n; the pool is not exhausted).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
