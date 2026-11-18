#!/usr/bin/env python3
"""TANGO v for the three rows recruited on 18 Nov. PREREGISTRATION 3.1 statistic.

Uses scripts/score_rows.py's own `statistic`, imported rather than reimplemented, so the
legacy arm and the modern arm cannot drift apart. TANGO's `Aggregation` column, per §5.3.

The full 9-point pH/temperature grid is reported, because those parameters were never
pre-registered and the 17 Nov run established that reporting the grid turns an
unregistered free parameter into a measured sensitivity.

    python3 -I tango_v_new.py <repo> <tango_out_dir> <regions.json>
"""
import json
import os
import sys

GRID = [(ph, te) for ph in ('5.0', '7.0', '7.4') for te in ('298', '303', '310')]
REPORTING = ('7.0', '310')   # the point apply_strata.py used on 18 Nov; kept identical
ROWS = [('TAF15', '7-99', 'Q92804'),
        ('CHCHD10', '42-75', 'Q8WYQ3'),
        ('CHCHD2', '54-86', 'Q9Y6H1')]


def load_tango(path):
    agg, seq = [], []
    with open(path) as fh:
        hdr = fh.readline().rstrip('\n').split('\t')
        ia, ib = hdr.index('Aggregation'), hdr.index('aa')
        for ln in fh:
            f = ln.rstrip('\n').split('\t')
            if len(f) <= ia:
                continue
            agg.append(float(f[ia]))
            seq.append(f[ib].strip())
    return agg, ''.join(seq)


def main(repo, outdir, regions):
    sys.path.insert(0, os.path.join(repo, 'scripts'))
    from score_rows import statistic, W

    idx = {(r['protein'], r['residues']): r
           for r in json.load(open(regions))['regions']}
    results = {}
    print('W = %d, non-overlapping tiling, phase 0, TANGO Aggregation column\n' % W)
    for prot, res, acc in ROWS:
        a, b = (int(x) for x in res.split('-'))
        row = idx[(prot, res)]
        print('=' * 72)
        print('%s %s   (%s)' % (prot, res, acc))
        grid = {}
        for ph, te in GRID:
            p = os.path.join(outdir, '%s_ph%s_T%s.txt' % (acc, ph, te))
            agg, seq = load_tango(p)
            # ASSERT the profile is the frame the row is stored in. A silent frame
            # mismatch is the trap this project has hit four times.
            got = seq[a - 1:b]
            if got != row['sequence']:
                raise SystemExit(
                    'FRAME MISMATCH on %s %s at pH %s/%s K\n  profile[%d:%d] = %s\n'
                    '  row sequence     = %s' % (prot, res, ph, te, a, b, got,
                                                 row['sequence']))
            st = statistic(agg, a, b, phase=0)
            grid['ph%s_T%s' % (ph, te)] = st
        ref = grid['ph%s_T%s' % REPORTING]
        print('  sequence check: profile[%d:%d] == row["sequence"]  (%d aa) OK'
              % (a, b, len(row['sequence'])))
        print('  M=%d windows over the chain, m=%d wholly inside the region'
              % (ref['M'], ref['m']))
        print('  REPORTING POINT pH %s / %s K:  P=%.4f  v=%.4f'
              % (REPORTING[0], REPORTING[1], ref['P'], ref['v']))
        vs = sorted(s['v'] for s in grid.values())
        print('  grid range over all 9 points: v = %.4f .. %.4f' % (vs[0], vs[-1]))
        calls = {('DISCORDANT' if s['v'] >= 0.05 else 'CONCORDANT') for s in grid.values()}
        print('  call at the 0.05 bar: %s%s'
              % ('/'.join(sorted(calls)),
                 '' if len(calls) == 1 else '   <-- GRID-DEPENDENT, must be reported'))
        results[prot + ' ' + res] = {
            'accession': acc, 'reporting_point': 'pH %s / %s K' % REPORTING,
            'v': ref['v'], 'P': ref['P'], 'M': ref['M'], 'm': ref['m'],
            'grid': {k: {'v': s['v'], 'P': s['P'], 'm': s['m']} for k, s in grid.items()},
            'grid_v_min': vs[0], 'grid_v_max': vs[-1],
            'call_stable_across_grid': len(calls) == 1,
            'call': 'DISCORDANT' if ref['v'] >= 0.05 else 'CONCORDANT'}
    print('=' * 72)
    json.dump(results, open(os.path.join(outdir, 'v_summary.json'), 'w'), indent=1)
    print('wrote', os.path.join(outdir, 'v_summary.json'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
