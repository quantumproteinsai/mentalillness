#!/usr/bin/env python3
"""Integrity checks on data/regions.json, run before the dataset is released.

WHY THIS EXISTS. regions.json is the asset CLAUDE.md says to publish first, with
its own DOI. It grew organically into a working file, and a working file and a
published dataset are different objects. This script is the gate between them:
it fails loudly on anything a third party would trip over, so that WE find it
rather than a reviewer or a user.

    python3 scripts/validate_regions.py

It checks only what can be checked mechanically. It cannot check whether a row
is TRUE -- that is what verified_against_publisher_pdf and source_version are
for, and those were established by opening papers.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGIONS = ROOT / 'data' / 'regions.json'

# The twelve fields every row must carry. Anything else is optional commentary.
CORE = [
    'protein', 'residues', 'evidence', 'construct', 'found_by', 'source',
    'verified_against_publisher_pdf', 'circularity_status', 'circularity_basis',
    'stratum', 'stratum_basis', 'source_version', 'source_version_note',
]
CIRC_OK = {'CLEAN', 'CIRCULAR', 'UNDECIDABLE'}
STRAT_OK = {'DISCORDANT', 'DISCORDANT_DERIVED', 'DISCORDANT_PROVISIONAL',
            'CONCORDANT', 'PENDING'}
SRCVER_OK = {'version_of_record', 'author_manuscript', 'pmc_full_text',
             'preprint', 'source_not_opened', 'UNRECORDED'}
AA = set('ACDEFGHIKLMNPQRSTVWY')


def main():
    d = json.loads(REGIONS.read_text())
    rows = d['regions']
    errors, warnings = [], []

    def err(row, msg):
        errors.append(f"{row.get('protein','?')} {row.get('residues','?')}: {msg}")

    def warn(row, msg):
        warnings.append(f"{row.get('protein','?')} {row.get('residues','?')}: {msg}")

    # ---- 1. core schema present and in the allowed vocabulary
    for r in rows:
        for f in CORE:
            if f not in r:
                err(r, f'MISSING core field {f!r}')
        if r.get('circularity_status') not in CIRC_OK:
            err(r, f'circularity_status {r.get("circularity_status")!r} not in {sorted(CIRC_OK)}')
        if r.get('stratum') not in STRAT_OK:
            err(r, f'stratum {r.get("stratum")!r} not in {sorted(STRAT_OK)}')
        if r.get('source_version') not in SRCVER_OK:
            err(r, f'source_version {r.get("source_version")!r} not in {sorted(SRCVER_OK)}')

    # ---- 2. sequence must match the stated range, and be real amino acids
    #
    # A range may be DISCONTINUOUS (PREREGISTRATION 10c), written as comma-separated
    # segments, in which case `sequence` carries the segments separated by '|'. The
    # length check then runs against the SUM of the segment lengths and against each
    # segment individually -- a total-only check would pass a sequence whose internal
    # split is in the wrong place.
    for r in rows:
        seq = r.get('sequence')
        if not seq:
            continue
        segs = re.findall(r'(\d+)-(\d+)', str(r.get('residues', '')))
        if not segs:
            continue
        parts = str(seq).split('|')
        if len(parts) != len(segs):
            err(r, f'residues has {len(segs)} segment(s) but sequence has {len(parts)}; '
                   f"discontinuous rows separate segments with '|' (PREREG 10c)")
            continue
        for (a, b), part in zip(segs, parts):
            a, b = int(a), int(b)
            bad = set(part) - AA
            if bad:
                err(r, f'sequence segment {a}-{b} contains non-amino-acid '
                       f'characters {sorted(bad)}')
            want = b - a + 1
            if len(part) != want:
                err(r, f'sequence segment is {len(part)} aa but residues {a}-{b} '
                       f'implies {want}')

    # ---- 3. leftovers from earlier schema versions
    for r in rows:
        if 'sequence_unverified' in r:
            err(r, "carries the RETIRED field 'sequence_unverified' -- it was renamed to "
                   "'sequence'. A published row must not ship a field the schema no longer defines.")

    # ---- 4. the gate in PREREGISTRATION 12
    for r in rows:
        v = r.get('verified_against_publisher_pdf')
        sv = r.get('source_version')
        if v and sv in {'source_not_opened', 'UNRECORDED'}:
            err(r, f'verified_against_publisher_pdf is true but source_version is {sv!r}')
        if sv == 'preprint' and not r.get('citable_under_12_1_exception'):
            warn(r, 'source_version is preprint and no 12.1 exception is recorded -- NOT CITABLE')
        if sv in {'pmc_full_text', 'source_not_opened', 'UNRECORDED'}:
            warn(r, f'source_version {sv!r} -- NOT CITABLE under 12.1 decision 3')

    # ---- 5. duplicates
    keys = [(r.get('protein'), r.get('residues')) for r in rows]
    for k, n in Counter(keys).items():
        if n > 1:
            errors.append(f'DUPLICATE row key {k} appears {n} times')

    # ---- 6. schema drift: fields used once are commentary, not schema
    field_counts = Counter(f for r in rows for f in r)
    singletons = sorted(f for f, n in field_counts.items() if n == 1 and f not in CORE)

    # ---- 7. documented columns vs actual
    documented = set((d.get('_columns') or {}).keys())
    undocumented = [f for f in CORE if f not in documented]

    # ---- report
    print('VALIDATION OF data/regions.json')
    print(f'  rows: {len(rows)}')
    print(f'  core fields present on every row: '
          f'{sum(1 for f in CORE if field_counts.get(f) == len(rows))}/{len(CORE)}')
    print()
    print(f'ERRORS ({len(errors)})')
    print('-' * 70)
    for e in errors:
        print(f'  FAIL  {e}')
    if not errors:
        print('  none')
    print()
    print(f'WARNINGS ({len(warnings)})')
    print('-' * 70)
    for w in warnings:
        print(f'  warn  {w}')
    if not warnings:
        print('  none')
    print()
    print(f'SCHEMA DRIFT: {len(singletons)} fields appear on exactly ONE row')
    print('-' * 70)
    print('  These are per-row commentary, not schema. A consumer cannot rely on')
    print('  them and cannot enumerate them. They belong under a single `notes`')
    print('  object in the released version, not as top-level row keys.')
    for f in singletons:
        print(f'    {f}')
    print()
    print(f'UNDOCUMENTED CORE FIELDS: {len(undocumented)} of {len(CORE)}')
    print('-' * 70)
    print('  _columns documents only:', sorted(documented) or 'nothing')
    for f in undocumented:
        print(f'    {f} is on every row and is NOT documented in _columns')

    print()
    if errors:
        print('RESULT: NOT RELEASABLE. Fix the errors above.')
        return 1
    print('RESULT: no hard errors. Read the warnings and the drift list before release.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
