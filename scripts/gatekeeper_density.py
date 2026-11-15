#!/usr/bin/env python3
"""Gatekeeper density of aggregation-critical regions, against real steric zippers.

WHY THIS EXISTS. Proline and flanking charge are what the field deliberately
engineers INTO a sequence to kill cross-beta aggregation -- the standard
anti-aggregation move in antibody design. So a region that is half proline and
charge should, by the field's own published rules, be an aggregation
SUPPRESSOR.

Both psychiatric regions mapped by experiment are about half gatekeeper
residues. Every peptide that actually crystallised as a steric zipper is at or
near zero. That is the paradox the benchmark has to explain, and it is why a
hexapeptide-trained predictor scoring these regions negative is uninformative
by construction rather than wrong.

The 8-mer is the test that decides which paper this is. It sits INSIDE the
25-residue region and is itself 0% gatekeeper -- indistinguishable from VQIVYK.
If a hexapeptide-trained predictor scores it POSITIVE in isolation, the failure
is about flanking context, not core chemistry.

    python3 scripts/gatekeeper_density.py

Sequences for the two psychiatric regions are an unverified UniProt mapping and
are labelled as such. The zipper peptides are the segments whose crystals this
author has computed interaction energies for.
"""
GATEKEEPERS = 'P' + 'DEKR'          # proline, plus the charged residues

REGIONS = [
    ('TRIOBP-1 324-348',   'PLRENKRVPLTALLNQSRGERRGPP',  'unverified', 'psychiatric'),
    ('DISC1 716-761',      'VEDERQMDDLEGAAPPIPPRLHSEDKRKTPLKVLEEWKTHLIPSLH',
                                                          'unverified', 'psychiatric'),
    ('  -> 8-mer 333-340', 'LTALLNQS',                    'unverified', 'the test'),
    ('tau PHF6 (2ON9)',    'VQIVYK',                      'crystal',    'zipper'),
    ('a-syn NACore (4RIL)', 'GAVVTGVTAVA',                'crystal',    'zipper'),
    ('a-syn preNAC (4ZNN)', 'GVVHGVTTVA',                 'crystal',    'zipper'),
    ('SOD1 30-35 (5WMJ)',  'KVWGSI',                      'crystal',    'zipper'),
    ('SOD1 147-153 (4NIP)', 'GVIGIAQ',                    'crystal',    'zipper'),
    ('IAPP 31-37 (3FTK)',  'NVGSNTY',                     'crystal',    'zipper'),
    ('Sup35 GNNQQNY (1YJP)', 'GNNQQNY',                   'crystal',    'zipper'),
]


def density(seq):
    """Fraction of residues that are proline or charged."""
    n = sum(1 for c in seq if c in GATEKEEPERS)
    return n, len(seq), 100.0 * n / len(seq)


def main():
    print(f'{"region":24s} {"len":>4} {"Pro":>4} {"charged":>8} {"gatekeeper %":>13}  source')
    print('-' * 74)
    for name, seq, prov, _kind in REGIONS:
        n, L, pct = density(seq)
        p = seq.count('P')
        print(f'{name:24s} {L:4d} {p:4d} {n - p:8d} {pct:12.1f}%  {prov}')

    zip_pct = [density(s)[2] for _n, s, _p, k in REGIONS if k == 'zipper']
    psy_pct = [density(s)[2] for _n, s, _p, k in REGIONS if k == 'psychiatric']
    print()
    print(f'  crystallised steric zippers: {min(zip_pct):.1f}% to {max(zip_pct):.1f}% '
          f'(n = {len(zip_pct)})')
    print(f'  psychiatric regions:         {min(psy_pct):.1f}% to {max(psy_pct):.1f}% '
          f'(n = {len(psy_pct)})')
    print()
    print('  The separation is the finding. It is also the paradox: by the')
    print('  field\'s own engineering rules these regions should not aggregate,')
    print('  and experiment says they are the aggregation-critical ones.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
