#!/usr/bin/env python3
"""Write `power_eligible` and the m/M ratio onto every row. PREREGISTRATION 3.1b.

m/M is the probability, under H0, that the chain's top-ranked window falls inside the
region. It is therefore the smallest p ANY rank-based statistic can return for that row,
and where it exceeds 0.05 the row is beyond §4's criterion no matter which statistic is
used. The ratio needs the chain length and the region length and NOTHING ELSE -- no
predictor, no score, no compute.

NO ROW IS REMOVED OR RESCORED HERE. Dropping rows after seeing their scores is the
post-hoc selection the pre-registration exists to prevent. This only labels them.

    python3 -I scripts/apply_power_eligible.py <repo>
"""
import json
import os
import sys

BAR = 0.05


def main(repo):
    sys.path.insert(0, os.path.join(repo, 'scripts'))
    import score_rows as S

    path = os.path.join(repo, 'data', 'regions.json')
    d = json.load(open(path))
    lens = {}
    for prot, (f, _frame) in S.RUNS.items():
        try:
            scores, _ = S.load(f)
            lens[prot] = len(scores)
        except (OSError, KeyError):
            pass

    done = skipped = 0
    for r in d['regions']:
        prot = r['protein']
        if prot not in lens:
            skipped += 1
            continue
        L = lens[prot]
        off = S.OFFSET.get(prot, 0)
        a, b = (int(x) for x in r['residues'].split('-'))
        a, b = a - off, b - off
        starts = list(range(0, L - S.W + 1, S.W))
        M = len(starts)
        m = sum(1 for s in starts if s + 1 >= a and s + S.W <= b)
        rule = 'PREREGISTRATION 3.1 (tiling, W=%d)' % S.W
        if M and m == 0:
            # PREREGISTRATION 3.1a: no tile fits inside the region, so the region is
            # scored as ONE window of its own length against all same-length windows.
            # The window pool is then the SLIDING one, m = 1, and the information limit
            # is 1/M' -- NOT zero, which is what the tiling arithmetic returns and which
            # would have mislabelled all four short-region rows as ineligible.
            Lr = b - a + 1
            if 1 <= Lr <= L:
                M, m = L - Lr + 1, 1
                rule = 'PREREGISTRATION 3.1a (region shorter than the window; m = 1)'
        if M == 0 or m == 0:
            skipped += 1
            continue
        ratio = m / M
        ok = ratio <= BAR
        r['power_eligible'] = ok
        r['power_limit'] = {
            'm_over_M': round(ratio, 6), 'm': m, 'M': M, 'chain_length': L,
            'rule': ('PREREGISTRATION 3.1b: power_eligible iff m/M <= %.2f' % BAR),
            'statistic': rule,
            'meaning': ('m/M is P(the chain\'s top-ranked window falls inside this region) '
                        'under H0, hence the smallest p ANY rank-based statistic can '
                        'return for this row. Where it exceeds the bar, no amendment to '
                        'the statistic can rescue the row -- only a longer protein or a '
                        'shorter mapped region.'),
            'assigned': '2026-11-18',
            'consequence': ('ELIGIBLE: this row can in principle be recovered at v < 0.05.'
                            if ok else
                            'NOT ELIGIBLE: this row CANNOT reach v < 0.05 under any '
                            'rank-based test. It is retained, labelled and reported, and '
                            'excluded from statistics that use PREREGISTRATION 4\'s '
                            'recovery criterion. The benchmark has no opinion on whether a '
                            'predictor succeeded here, and saying so is the honest report.'),
        }
        done += 1
        print('  %-26s %-10s m/M = %.4f  (m=%2d M=%4d)  %s'
              % (prot, r['residues'], ratio, m, M, 'eligible' if ok else 'NOT ELIGIBLE'))
    json.dump(d, open(path, 'w'), indent=1, ensure_ascii=True)
    el = sum(1 for r in d['regions'] if r.get('power_eligible'))
    print('\n%d rows labelled, %d skipped (no predictor profile, so no chain length).'
          % (done, skipped))
    print('%d of %d labelled rows are power_eligible.' % (el, done))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else '.'))
