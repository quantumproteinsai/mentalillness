#!/usr/bin/env python3
"""TANGO v for the rows recruited under PREREGISTRATION 10b/10c. The legacy arm.

Uses scripts/score_rows.py's own `statistic`, imported rather than reimplemented, so the
legacy and modern arms cannot drift apart. TANGO's `Aggregation` column, per 5.3. The full
9-point pH/temperature grid is reported, because those parameters were never
pre-registered and the 17 Nov run established that reporting the grid turns an
unregistered free parameter into a measured sensitivity.

    python3 -I scripts/tango_v_structural.py <repo> <tango_out_dir> <out.json>

WHY THIS IS NOT tango_v_recruited.py. That script hardcoded three rows whose residues
parse as a single `a-b` pair and whose scored frame is the canonical UniProt sequence. The
10b/10c rows break both assumptions: one is a MATURE chain (beta2m, UniProt minus a signal
peptide) and one is a DISCONTINUOUS core (SOD1, "3-55,86-153"). Rather than widen the old
script's assumptions silently, this one states them and refuses what it cannot do.

TWO REFUSALS, BOTH DELIBERATE:

  * A NON-CONTIGUOUS region gets no v and no stratum. 10c C3: the 3.1 statistic tiles a
    contiguous span and has no defined behaviour on a segment list. The row is skipped by
    name with the reason printed, never scored on its first segment and never silently
    totalled. If this script ever scores SOD1, it is broken.

  * A FRAME MISMATCH aborts the run. The profile slice must equal the row's stored
    `sequence` character for character. Five frame traps have been found in this project,
    one of them inside a PDB deposit, so this is checked at every grid point rather than
    once.

AND ONE THING THIS SCRIPT REPORTS THAT NO EARLIER ONE DID: the SMALLEST v the statistic
can return for the row, 1 - ((M-0.5)/M)**m, which is what v becomes when the region's best
window is the single highest-scoring window in the whole chain. Where that floor is at or
above the 0.05 bar of section 4, the row's stratum call is FORCED: it must come out
DISCORDANT whatever TANGO says, and the label therefore carries no information about
agreement between predictor and experiment. This is the m/M information limit of 3.1b
reappearing in the section 7 stratum rule, where it was never stated. It is computed from
two integers and no predictor output.
"""
import json
import os
import sys

GRID = [(ph, te) for ph in ('5.0', '7.0', '7.4') for te in ('298', '303', '310')]
REPORTING = ('7.0', '310')   # the point the 17 and 18 Nov runs used; kept identical
BAR = 0.05                   # PREREGISTRATION 4

# row key -> (the accession naming the TANGO profile, the frame that profile is in).
# THE FRAME IS PART OF THE SPECIFICATION, NOT A COMMENT: beta2m is scored on the MATURE
# 99-residue chain because that is the frame its residues are stored in, and scoring the
# 119-residue precursor would put a 20-residue signal peptide into the window pool as a
# decoy -- the defect already registered for glycinin under
# A_SIGNAL_PEPTIDE_IN_THE_SCORED_FRAME_BIASES_THE_STATISTIC.
ROWS = [
    (('Orb2 (Drosophila melanogaster)', '176-206'), 'Q9VSR3',
     'Q9VSR3 canonical, 704 aa, which IS the Orb2B frame'),
    (('beta-2-microglobulin', '22-85'), 'B2M_mature',
     'P61769 MINUS the 20-residue signal peptide = mature 99 aa, I1..M99'),
]

# Named, with the reason, so the refusal is auditable rather than invisible.
REFUSED = {
    ('SOD1 (superoxide dismutase [Cu-Zn])', '3-55,86-153'):
        'NON-CONTIGUOUS (PREREGISTRATION 10c C3). The region is two segments with a '
        '30-residue disordered gap at 56-85. The 3.1 statistic tiles a contiguous span '
        'and has no defined behaviour on a segment list, so no v exists for this row. '
        'NOT refused on m/M, which is a different defect -- for reference only, m/M '
        'would also fail at ~0.80.',
}


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


def floor_v(M, m):
    """The smallest v the 3.1 statistic can return: region's best window is the chain max."""
    return 1.0 - ((M - 0.5) / M) ** m


def main(repo, outdir, outpath):
    sys.path.insert(0, os.path.join(repo, 'scripts'))
    from score_rows import statistic, W

    idx = {(r['protein'], r['residues']): r
           for r in json.load(open(os.path.join(repo, 'data', 'regions.json')))['regions']}
    results = {}
    print('W = %d, non-overlapping tiling, phase 0, TANGO Aggregation column' % W)
    print('reporting point pH %s / %s K; full %d-point grid reported\n'
          % (REPORTING[0], REPORTING[1], len(GRID)))

    for key, reason in REFUSED.items():
        if key not in idx:
            print('REFUSED row %s %s is not in regions.json -- check this list' % key)
            continue
        print('=' * 76)
        print('%s %s' % key)
        print('  NO v COMPUTED, BY RULE. %s' % reason)
        results['%s %s' % key] = {'v': None, 'refused': True, 'reason': reason,
                                  'stratum': None}
        print()

    for key, acc, frame in ROWS:
        prot, res = key
        a, b = (int(x) for x in res.split('-'))
        row = idx[key]
        print('=' * 76)
        print('%s %s   profile %s' % (prot, res, acc))
        print('  scored frame: %s' % frame)
        grid = {}
        for ph, te in GRID:
            p = os.path.join(outdir, '%s_ph%s_T%s.txt' % (acc, ph, te))
            agg, seq = load_tango(p)
            got = seq[a - 1:b]
            if got != row['sequence']:
                raise SystemExit(
                    'FRAME MISMATCH on %s %s at pH %s/%s K\n  profile[%d:%d] = %s\n'
                    '  row sequence     = %s' % (prot, res, ph, te, a, b, got,
                                                 row['sequence']))
            st = statistic(agg, a, b, phase=0)
            if st is None:
                raise SystemExit('statistic returned None for %s %s' % key)
            grid['ph%s_T%s' % (ph, te)] = st
        ref = grid['ph%s_T%s' % REPORTING]
        fl = floor_v(ref['M'], ref['m'])
        forced = fl >= BAR
        print('  frame check: profile[%d:%d] == row["sequence"]  (%d aa) OK'
              % (a, b, len(row['sequence'])))
        print('  chain L=%d  M=%d windows  m=%d wholly inside  m/M=%.4f'
              % (len(seq), ref['M'], ref['m'], ref['m'] / ref['M']))
        print('  REPORTING POINT:  P=%.4f  v=%.4f' % (ref['P'], ref['v']))
        vs = sorted(s['v'] for s in grid.values())
        print('  grid range over all 9 points: v = %.4f .. %.4f' % (vs[0], vs[-1]))
        print('  SMALLEST v ATTAINABLE AT THIS M,m: %.4f' % fl)
        calls = {('DISCORDANT' if s['v'] >= BAR else 'CONCORDANT') for s in grid.values()}
        call = 'DISCORDANT' if ref['v'] >= BAR else 'CONCORDANT'
        print('  call at the %.2f bar: %s%s'
              % (BAR, '/'.join(sorted(calls)),
                 '' if len(calls) == 1 else '   <-- GRID-DEPENDENT, must be reported'))
        if forced:
            print('  *** THE CALL IS FORCED, NOT EARNED. The floor %.4f is at or above the'
                  % fl)
            print('      %.2f bar, so this row reads DISCORDANT for ANY predictor output.'
                  % BAR)
            print('      The label is a fact about the region length, not about TANGO.')
        else:
            print('  the call is EARNED: v < %.2f was attainable (floor %.4f) and %s.'
                  % (BAR, fl, 'was not reached' if call == 'DISCORDANT' else 'was reached'))
        results['%s %s' % key] = {
            'accession': acc, 'scored_frame': frame,
            'reporting_point': 'pH %s / %s K' % REPORTING,
            'chain_length': len(seq), 'v': ref['v'], 'P': ref['P'],
            'M': ref['M'], 'm': ref['m'], 'm_over_M': ref['m'] / ref['M'],
            'grid': {k: {'v': s['v'], 'P': s['P'], 'm': s['m']} for k, s in grid.items()},
            'grid_v_min': vs[0], 'grid_v_max': vs[-1],
            'call_stable_across_grid': len(calls) == 1,
            'floor_v': fl, 'call_forced_by_information_limit': forced,
            'refused': False, 'call': call, 'stratum': call}
        print()

    print('=' * 76)
    json.dump(results, open(outpath, 'w'), indent=1)
    print('wrote', outpath)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
