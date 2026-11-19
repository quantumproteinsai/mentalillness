#!/usr/bin/env python3
"""Does the rebuilt AggrescanAI stack change any NUMBER THIS PROJECT REPORTS?

CONTEXT. On 19 Nov 2026 the modern arm was rebuilt from scratch (see
scripts/verify_modern_arm.py for why). The pinned weights came back with identical
SHA-256s. The software around them was never pinned, and the rebuilt stack reproduces an
archived profile to 92 residues in 104 exactly, with the other 12 differing by 1e-06 --
the last decimal the CSV stores.

SO THE QUESTION IS NOT "are the profiles identical" -- they are not, at the sixth decimal.
The question is CLAUDE.md rule 2: is the difference smaller than the uncertainty of the
thing that consumes it? Two margins to compare it against:

  * the ENSEMBLE SPREAD already recorded for every run -- 0.85 for hSAA1.1, i.e. SIX
    ORDERS OF MAGNITUDE larger than the discrepancy, and already a standing caveat on
    every AggrescanAI number in this project;
  * and the one that actually decides things: whether any v MOVES. v depends only on the
    RANK of 6-residue window means, so a 1e-06 perturbation changes it only if two window
    means sit within 1e-06 of each other. That is a fact about the data, not an opinion,
    and this script measures it.

    python3 scripts/modern_arm_equivalence.py <repo> <rebuilt_dir> [out.json]

Re-run every archived profile into <rebuilt_dir> first. This script then recomputes the
section 3.1 statistic for every scored row from BOTH profile sets and reports any v that
differs. IT DOES NOT TUNE ANYTHING AND HAS NO TOLERANCE TO SET.
"""
import json
import os
import sys


def load_scores(path):
    seq, sc = [], []
    with open(path) as fh:
        for ln in fh:
            if ln.startswith('#') or ln.startswith('position,') or not ln.strip():
                continue
            p, a, s, d = ln.rstrip('\n').split(',')
            seq.append(a)
            sc.append(float(s))
    return ''.join(seq), sc


def main(repo, rebuilt, outpath=None):
    sys.path.insert(0, os.path.join(repo, 'scripts'))
    from score_rows import statistic, RUNS, RUNDIR

    rows = json.load(open(os.path.join(repo, 'data', 'regions.json')))['regions']
    report = {'rows': [], 'residue_level': []}
    worst_resid, n_resid_diff, n_resid = 0.0, 0, 0
    moved = []

    print('%-30s %-12s %12s %12s  %s' % ('row', 'archived v', 'rebuilt v', 'delta', 'moved?'))
    print('-' * 86)
    for r in rows:
        prot, res = r['protein'], r['residues']
        if prot not in RUNS or ',' in res:
            continue
        fn = RUNS[prot][0]
        a_path = os.path.normpath(os.path.join(RUNDIR, fn))
        b_path = os.path.join(rebuilt, os.path.basename(fn))
        if not (os.path.exists(a_path) and os.path.exists(b_path)):
            continue
        sa, ca = load_scores(a_path)
        sb, cb = load_scores(b_path)
        if sa != sb:
            raise SystemExit('SEQUENCE MISMATCH between archived and rebuilt %s' % fn)
        a, b = (int(x) for x in res.split('-'))
        st_a = statistic(ca, a, b, phase=0)
        st_b = statistic(cb, a, b, phase=0)
        if st_a is None or st_b is None:
            continue
        d = abs(st_a['v'] - st_b['v'])
        ismoved = ('%.6f' % st_a['v']) != ('%.6f' % st_b['v'])
        moved.append(ismoved)
        print('%-30s %12.6f %12.6f %12.3g  %s'
              % ((prot[:18] + ' ' + res)[:30], st_a['v'], st_b['v'], d,
                 'MOVED' if ismoved else '-'))
        report['rows'].append({'protein': prot, 'residues': res,
                               'v_archived': st_a['v'], 'v_rebuilt': st_b['v'],
                               'delta': d, 'moved_at_6dp': ismoved,
                               'P_archived': st_a['P'], 'P_rebuilt': st_b['P'],
                               'm': st_a['m'], 'M': st_a['M']})

    # residue-level summary across every profile pair
    seen = set()
    for prot, (fn, _frame) in RUNS.items():
        a_path = os.path.normpath(os.path.join(RUNDIR, fn))
        b_path = os.path.join(rebuilt, os.path.basename(fn))
        if b_path in seen or not (os.path.exists(a_path) and os.path.exists(b_path)):
            continue
        seen.add(b_path)
        _, ca = load_scores(a_path)
        _, cb = load_scores(b_path)
        diffs = [abs(x - y) for x, y in zip(ca, cb) if x != y]
        n_resid += len(ca)
        n_resid_diff += len(diffs)
        worst_resid = max([worst_resid] + diffs)
        report['residue_level'].append({'file': os.path.basename(fn), 'n': len(ca),
                                        'n_differing': len(diffs),
                                        'max_delta': max(diffs) if diffs else 0.0})

    print()
    print('RESIDUE LEVEL: %d of %d residues differ (%.3f%%), largest delta %.3g'
          % (n_resid_diff, n_resid, 100.0 * n_resid_diff / max(n_resid, 1), worst_resid))
    print('ROW LEVEL    : %d of %d v values move at the 6 dp this project reports'
          % (sum(moved), len(moved)))
    print()
    if not any(moved):
        print('VERDICT: NO REPORTED NUMBER MOVES.')
        print('  The two stacks differ only in float rounding at the storage precision.')
        print('  v depends on the RANK of window means, and no two window means in this')
        print('  dataset sit close enough together for a %.3g perturbation to reorder them.'
              % worst_resid)
        print('  The equivalence is MEASURED, not assumed, and it is a statement about')
        print('  THIS dataset -- a future row with near-tied windows could still move.')
        rc = 0
    else:
        print('VERDICT: AT LEAST ONE v MOVES. The stacks are not interchangeable.')
        print('  Record a second predictor_provenance entry and treat the new stack as a')
        print('  separate run. Do not average, and do not pick the nicer number.')
        rc = 1
    report['summary'] = {'n_residues': n_resid, 'n_residues_differing': n_resid_diff,
                         'max_residue_delta': worst_resid,
                         'n_rows': len(moved), 'n_rows_moved': sum(moved),
                         'equivalent_at_6dp': not any(moved)}
    if outpath:
        json.dump(report, open(outpath, 'w'), indent=1)
        print('\nwrote', outpath)
    return rc


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1], sys.argv[2],
                          sys.argv[3] if len(sys.argv) > 3 else None))
