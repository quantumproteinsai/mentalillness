#!/usr/bin/env python3
"""Stage 7: stratum labels for the three rows recruited 18 Nov 2026.

UNLIKE apply_strata.py (17 Nov), THE ORDERING IS INTACT HERE. The legacy arm has run on
these three rows and the modern arm has NOT. No AggrescanAI score exists for Q92804,
Q8WYQ3 or Q9Y6H1, so nothing downstream was visible when this rule was applied. That is
the whole purpose of the eight-stage pipeline, and it is what makes these three rows
confirmatory_eligible where the 17 Nov six are not.

THIS SCRIPT MUST BE COMMITTED AND THE LABELS PUSHED BEFORE run_aggrescanai.py IS POINTED
AT ANY OF THESE THREE ACCESSIONS. That is checkable after the fact from the commit graph.
"""
import json
import sys

BAR = 0.05
ASSIGNED = '2026-11-18'

# TANGO v at the pH 7.0 / 310 K reporting point, phase 0, from
# results/recruited_2026-11-18/ -- 27 profiles and v_summary.json, both committed.
# The call is identical at all nine grid points for all three rows.
TANGO = {
    ('TAF15', '7-99'): (1.0000, 0.4592, 15, 'identical at all 9 grid points'),
    ('CHCHD10', '42-75'): (0.1041, 0.9783, 5, 'identical at all 9 grid points'),
    ('CHCHD2', '54-86'): (0.0961, 0.9800, 5, 'identical at all 9 grid points'),
}

BASIS = (
    'ASSIGNED MECHANICALLY FROM THE LEGACY ARM ON {assigned}, UNDER PREREGISTRATION 7 '
    '(amended 16 Nov 2026, before any predictor ran): stratum is taken "from the '
    'published predictor results where they exist, and otherwise from the LEGACY ARM\'S '
    'OWN OUTPUT". No published predictor run exists for this region, so the legacy arm '
    'decides it. RULE: DISCORDANT iff TANGO v >= {bar}, the recovery bar fixed in '
    'PREREGISTRATION 4. OBSERVED: TANGO v = {v} at pH 7.0 / 310 K, phase 0 '
    '(P = {P}, m = {m} tiled windows wholly inside the region), so {call}. '
    'The call is {stab}, so the two parameters that were never pre-registered do not '
    'decide this label. '
    '|| THE ORDERING IS INTACT, AND THIS IS THE DIFFERENCE FROM THE SIX ROWS LABELLED '
    'EARLIER THE SAME DAY. Section 7 requires the assignment to be made AFTER the legacy '
    'run and BEFORE the modern run. For this row that is exactly what happened: TANGO ran '
    'on {acc} on 18 Nov, this label was committed, and NO AggrescanAI run on {acc} '
    'existed at that moment -- the accession appears nowhere in '
    'results/aggrescanai_2026-11-17/. Nothing downstream was visible when the rule was '
    'applied, and there was no discretion left in whether to apply it, because the row '
    'was recruited under a pipeline that fixes this order in advance '
    '(reports/recruitment_tracker.md). So this row IS confirmatory_eligible.'
)


def main(path):
    d = json.load(open(path))
    idx = {(r['protein'], r['residues']): r for r in d['regions']}
    changed = 0
    for key, (v, P, m, stab) in TANGO.items():
        r = idx[key]
        if 'stratum' in r and r['stratum'] != 'PENDING':
            print('  skip %s: stratum is already %s' % (key, r['stratum']))
            continue
        acc = {'TAF15': 'Q92804', 'CHCHD10': 'Q8WYQ3', 'CHCHD2': 'Q9Y6H1'}[key[0]]
        call = 'DISCORDANT' if v >= BAR else 'CONCORDANT'
        r['stratum'] = call
        r['stratum_basis'] = BASIS.format(assigned=ASSIGNED, bar=BAR, v=v, P=P, m=m,
                                          call=call, stab=stab, acc=acc)
        r['stratum_assignment'] = {
            'rule': 'PREREGISTRATION 7: DISCORDANT iff legacy v >= 0.05 (the §4 bar)',
            'legacy_tool': ('TANGO, SHA-256 d0e381c2...9f31dbf, pH 7.0 / 310 K, phase 0, '
                            'Aggregation column, W=6 non-overlapping tiling'),
            'legacy_v': v, 'legacy_P': P, 'legacy_m': m,
            'grid_sensitivity': stab,
            'profiles': 'results/recruited_2026-11-18/tango_profiles/ (9 per accession)',
            'assigned': ASSIGNED,
            'previous_value': 'none (row created 18 Nov with no stratum field)',
            'ordering': ('INTACT -- the modern arm had NOT run on this accession when the '
                         'label was applied, and the label is committed before it does'),
            'confirmatory_eligible': True,
            'reported_as': 'CONFIRMATORY under PREREGISTRATION 5.2b',
        }
        changed += 1
        print('  %-10s %-8s  v=%.4f  P=%.4f  m=%2d  -> %s' % (key[0], key[1], v, P, m, call))
    json.dump(d, open(path, 'w'), indent=1, ensure_ascii=True)
    print('\n%d rows labelled' % changed)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1]))
