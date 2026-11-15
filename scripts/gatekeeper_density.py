#!/usr/bin/env python3
"""Gatekeeper density of aggregation-critical regions, against real steric zippers.

WHY THIS EXISTS. Proline and flanking charge are what the field deliberately
engineers INTO a sequence to kill cross-beta aggregation -- the standard
anti-aggregation move in antibody design. So a region that is half proline and
charge should, by the field's own published rules, be an aggregation
SUPPRESSOR. Experiment says these are the aggregation-critical regions.

    python3 scripts/gatekeeper_density.py

TWO DEFECTS FIXED ON 15 Nov 2026, both found by checking this script against
the project's own data rather than against the literature.

(1) IT HARDCODED SEQUENCES THAT DUPLICATE data/regions.json, AND THE TWO HAD
    DRIFTED. The psychiatric sequences are now READ FROM regions.json and
    verified byte-for-byte; a mismatch is a hard failure, not a warning. The
    script can no longer disagree with the validation set.

(2) IT SCORED A ROW THE VALIDATION SET EXCLUDES. The second psychiatric region
    was DISC1 716-761, whose regions.json entry carries, in capitals,
    "THIS IS A DOCKING RESTRAINT, NOT A MEASUREMENT", and whose found_by reads
    "RADAR sequence-repeat search" -- found BY a sequence search, which is what
    the found_by column exists to catch. Meanwhile DISC1 384-415, the row
    STATE.md's N=2 spine actually names ("experimental; no aggregation
    predictor involved"), was not in the table and carries no sequence in
    regions.json at all. So the headline n=2 was one unverified row plus one
    circular row.

INCLUSION IS AN EXPLICIT DECISION, NOT A KEYWORD MATCH. regions.json warns that
circularity "cannot be grepped" -- the same laboratory in the same era produced
rows of opposite status. So every psychiatric row scored here is named below
with a written reason, and anything not named is reported as excluded rather
than silently dropped.

THE WINDOW-LENGTH CONTROL IS NOT OPTIONAL. The whole-region figure compares
SELECTED 6-11 residue cores against UNSELECTED 25-46 residue regions, which is
a comparison of a minimum against a mean. Matched to the 5-6 residue window the
predictors actually score, both psychiatric regions contain zipper-grade
windows -- which does not weaken the project, it sharpens it: a window-scanning
predictor had a 0%-gatekeeper hexapeptide to find inside TRIOBP-1 324-348 and
missed the region anyway.

PROVENANCE. The TRIOBP-1 25-mer is DERIVED, NOT TRANSCRIBED: its source paper
prints it only in Figure 12B. regions.json records the three consistency checks
it passes. The headline depends on it, so verify it against Figure 12B before
publishing anything from this. The zipper peptides are the segments whose
crystals this author has computed interaction energies for; they come from
deposited structures and are therefore hardcoded here by design, not read from
regions.json, which holds no crystal rows.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGIONS_JSON = ROOT / 'data' / 'regions.json'

GATEKEEPERS = 'P' + 'DEKR'          # proline, plus the charged residues

# Psychiatric rows scored here, keyed (protein, residues) into regions.json.
# Every entry carries the reason it is in. Sequences are NOT written here --
# they are read from regions.json and checked.
INCLUDE = {
    ('TRIOBP-1', '324-348'): (
        'region', 'found_by: experimental scanning, explicitly NOT predicted. '
        'regions.json names it THE GROUND TRUTH for TRIOBP-1.'),
    ('TRIOBP-1', '333-340'): (
        'the test', 'the narrowed 8-mer, found by experimental truncation. '
        'Sits INSIDE 324-348 and is itself 0% gatekeeper.'),
}

# Named, with the reason, so the exclusion is auditable rather than invisible.
EXCLUDE = {
    ('DISC1', '716-761'):
        'CIRCULAR AND NOT A MEASUREMENT. found_by is "RADAR sequence-repeat '
        'search", i.e. found BY a sequence search; and regions.json carries '
        'CAUTION_2026_11_15: "THIS IS A DOCKING RESTRAINT, NOT A MEASUREMENT". '
        'Scoring it put a predicted region in a table about predictor failure.',
    ('DISC1', '384-415'):
        'WANTED BUT UNAVAILABLE. This is the clean DISC1 row -- "experimental; '
        'no aggregation predictor involved" -- and the one STATE.md names in '
        'the N=2 argument. regions.json carries NO SEQUENCE for it. Supply the '
        'sequence from UniProt Q9NRI5 (854 aa, canonical) and it belongs here.',
}

ZIPPERS = [                         # deposited crystals, not validation rows
    ('tau PHF6 (2ON9)',      'VQIVYK'),
    ('a-syn NACore (4RIL)',  'GAVVTGVTAVA'),
    ('a-syn preNAC (4ZNN)',  'GVVHGVTTVA'),
    ('SOD1 30-35 (5WMJ)',    'KVWGSI'),
    ('SOD1 147-153 (4NIP)',  'GVIGIAQ'),
    ('IAPP 31-37 (3FTK)',    'NVGSNTY'),
    ('Sup35 GNNQQNY (1YJP)', 'GNNQQNY'),
]


def density(seq):
    """Fraction of residues that are proline or charged."""
    n = sum(1 for c in seq if c in GATEKEEPERS)
    return n, len(seq), 100.0 * n / len(seq)


def load_psychiatric():
    """Read the included rows out of regions.json. Hard-fails on drift."""
    rows = json.loads(REGIONS_JSON.read_text())['regions']
    by_key = {(r.get('protein'), r.get('residues')): r for r in rows}

    missing = [k for k in INCLUDE if k not in by_key]
    if missing:
        sys.exit(f'regions.json has no row for {missing} -- the script and the '
                 'validation set have drifted. Fix one or the other.')

    out = []
    for key, (kind, reason) in INCLUDE.items():
        row = by_key[key]
        seq = row.get('sequence_unverified') or row.get('sequence')
        if not seq:
            sys.exit(f'{key} carries no sequence in regions.json')
        unverified = not row.get('verified_against_publisher_pdf', False)
        out.append(dict(name=f'{key[0]} {key[1]}', seq=seq, kind=kind,
                        reason=reason, unverified=unverified,
                        derived='sequence_provenance' in row))
    out.sort(key=lambda r: (r['kind'] != 'region', r['name']))
    return out, by_key


def main():
    psy, by_key = load_psychiatric()

    print('GATEKEEPER DENSITY (proline + D/E/K/R)\n')
    print(f'{"region":26s} {"len":>4} {"Pro":>4} {"chg":>5} {"gatekeeper %":>13}  provenance')
    print('-' * 86)
    for r in psy:
        n, L, pct = density(r['seq'])
        p = r['seq'].count('P')
        prov = 'DERIVED, unverified' if r['derived'] else (
            'unverified' if r['unverified'] else 'verified')
        print(f'{r["name"]:26s} {L:4d} {p:4d} {n - p:5d} {pct:12.1f}%  {prov}')
    for name, seq in ZIPPERS:
        n, L, pct = density(seq)
        print(f'{name:26s} {L:4d} {seq.count("P"):4d} {n - seq.count("P"):5d} '
              f'{pct:12.1f}%  crystal')

    zip_pct = [density(s)[2] for _n, s in ZIPPERS]
    reg = [r for r in psy if r['kind'] == 'region']
    reg_pct = [density(r['seq'])[2] for r in reg]

    print()
    print(f'  crystallised steric zippers: {min(zip_pct):.1f}% to {max(zip_pct):.1f}% '
          f'(n = {len(zip_pct)})')
    print(f'  psychiatric regions:         {min(reg_pct):.1f}% to {max(reg_pct):.1f}% '
          f'(n = {len(reg_pct)})')
    if len(reg) < 2:
        print()
        print('  *** n = 1. The second psychiatric region is EXCLUDED, not absent. ***')

    print('\nEXCLUDED ROWS, named so the exclusion is auditable')
    print('-' * 86)
    for key, why in EXCLUDE.items():
        present = 'in regions.json' if key in by_key else 'NOT in regions.json'
        print(f'  {key[0]} {key[1]} ({present})')
        for line in (why[i:i + 76] for i in range(0, len(why), 76)):
            print(f'      {line}')

    print('\nWINDOW-MATCHED CONTROL -- the comparison above is not like-for-like')
    print('-' * 86)
    print('  The zippers are SELECTED 6-11 residue cores; the regions are')
    print('  UNSELECTED 25-46 residue stretches. Matched to the 5-6 residue')
    print('  window a predictor actually scores:')
    print()
    worst = max(zip_pct)
    for r in reg:
        s = r['seq']
        for w in (6, 7):
            if len(s) < w:
                continue
            wins = [s[i:i + w] for i in range(len(s) - w + 1)]
            best = min(wins, key=lambda x: density(x)[2])
            at_or_below = sum(1 for x in wins if density(x)[2] <= worst + 1e-9)
            print(f'  {r["name"]:22s} {w}-mer  min {density(best)[2]:5.1f}% '
                  f'({best})   {at_or_below}/{len(wins)} windows at or below '
                  f'the worst zipper ({worst:.1f}%)')
    print()
    print('  So both the paradox and its resolution are real: the REGION is')
    print('  gatekeeper-rich, and it CONTAINS zipper-grade windows. A')
    print('  window-scanning predictor had one to find, and missed the region.')
    print('  That is a sharper failure than "uninformative by construction".')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
