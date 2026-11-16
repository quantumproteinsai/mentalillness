#!/usr/bin/env python3
"""Build the publishable dataset from the working file.

WHY THIS EXISTS. CLAUDE.md says data/regions.json is the asset to publish first,
with its own DOI. But regions.json is a WORKING FILE: it has grown 41 fields that
appear on exactly one row, and top-level keys that are project notes rather than
dataset documentation. A working file and a published dataset are different
objects, and conflating them would hand a stranger something they cannot parse.

THIS SCRIPT DOES NOT EDIT regions.json. It derives a release from it, so the
working file keeps its full history and nothing is lost. Re-run it whenever the
working file changes.

    python3 scripts/build_release.py

WHAT IT CHANGES, AND WHAT IT DELIBERATELY DOES NOT.
  - Per-row commentary (the 41 singleton fields) moves under a single `notes`
    object. Nothing is deleted; it becomes enumerable.
  - Top-level keys are PARTITIONED into `dataset_documentation` and
    `project_notes`, rather than the latter being dropped. A consumer learns
    which is which; a reader loses nothing. The partition below is a judgement
    call and is listed explicitly so it can be argued with.
  - Row content is otherwise untouched. No value is rewritten, rounded or
    summarised.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'data' / 'regions.json'
OUT = ROOT / 'release'
VERSION = '1.0.0-draft'

CORE = [
    'protein', 'residues', 'frame', 'sequence', 'evidence', 'construct',
    'found_by', 'source', 'verified_against', 'verified_against_publisher_pdf',
    'source_version', 'source_version_note', 'circularity_status',
    'circularity_basis', 'stratum', 'stratum_basis',
    'sequence_provenance', 'range_provenance', 'note',
]

# Top-level keys that document the DATASET and belong in the release.
DOC_KEYS = {
    '_what', '_why', '_numbering', '_columns',
    '_SCHEMA_CIRCULARITY', '_SCHEMA_STRATUM', '_SCHEMA_SOURCE_VERSION',
    '_circularity_cannot_be_grepped', '_frame_traps_are_worse_than_assumed',
    '_CPAD_CONTAMINATION_WARNING', '_COAGGREGATION_IS_THREE_DIFFERENT_PHENOMENA',
    '_rows_deliberately_excluded',
    '_A_WHOLE_PROTEIN_CORE_CANNOT_TEST_A_WINDOW_PREDICTOR',
    '_THE_DOCUMENTED_PREDICTOR_FAILURE_IN_CUKKEMANE_2021',
    '_THE_LEGACY_ARM_RUN_ON_TRIOBP_1_IS_PUBLISHED_AND_FULLY_PARAMETERISED',
    '_A_DOCUMENTED_FALSE_POSITIVE_ON_OUR_OWN_PROTEIN',
    # Both added 16 Nov 2026. They are about HOW TO READ THE ROWS -- a consumer who
    # misses either will misread a stratum label or mistake training-set recall for
    # prediction -- so they are dataset documentation, not project notes.
    '_STRATUM_IS_A_PROPERTY_OF_A_PAIR_NOT_OF_A_REGION',
    '_AGGRESCANAI_HITS_ON_OUR_ROWS_ARE_NOT_EVIDENCE_OF_PREDICTION',
}
# Everything else is a project note: true, kept, but about THIS PROJECT's
# hypotheses and workflow rather than about the data.


def main():
    d = json.loads(SRC.read_text())
    rows = d['regions']
    OUT.mkdir(exist_ok=True)

    clean = []
    for r in rows:
        row = {k: r[k] for k in CORE if k in r}
        notes = {k: v for k, v in r.items() if k not in CORE}
        if notes:
            row['notes'] = notes
        clean.append(row)

    doc = {k: v for k, v in d.items() if k in DOC_KEYS}
    proj = {k: v for k, v in d.items() if k not in DOC_KEYS and k != 'regions'}

    release = {
        '_dataset': {
            'title': 'Experimentally mapped aggregation-critical protein regions, '
                     'with circularity and prediction-concordance labels',
            'version': VERSION,
            'n_regions': len(clean),
            'generated_by': 'scripts/build_release.py, from data/regions.json',
            'READ_THIS_FIRST': 'release/DATA_DESCRIPTOR.md',
            'WHAT_MAKES_THIS_DIFFERENT_FROM_OTHER_AGGREGATION_DATASETS':
                'Three columns that aggregation datasets usually lack. `construct` records WHICH '
                'construct established the region, because a region can be necessary in one and '
                'dispensable in another. `circularity_status` records whether a PREDICTOR was in '
                'the discovery path, which makes a row unusable for benchmarking the predictor '
                'family that found it. `stratum` records whether experiment and prediction AGREE, '
                'which is what decides whether a row can discriminate between predictors at all.',
            'HOW_TO_READ_A_ROW_HONESTLY':
                'Check `source_version` before citing: not every row rests on a version of '
                'record. Check `frame` before using a residue number: numbering frames in this '
                'literature differ by isoform, by allele and by constant offset. Check '
                '`construct` before treating a region as a property of the protein.',
        },
        'dataset_documentation': doc,
        'regions': clean,
        'project_notes': {
            '_what_these_are': 'Kept for provenance, NOT part of the dataset. These top-level '
                               'keys concern the hypotheses and workflow of the project that '
                               'produced the dataset, not the data itself. A consumer of the '
                               'dataset can ignore them; a reader auditing how the rows came to '
                               'exist may want them.',
            **proj,
        },
    }

    jf = OUT / f'aggregation_regions_v{VERSION}.json'
    jf.write_text(json.dumps(release, indent=2, ensure_ascii=True) + '\n')

    cf = OUT / f'aggregation_regions_v{VERSION}.csv'
    with cf.open('w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=CORE, extrasaction='ignore')
        w.writeheader()
        for r in clean:
            w.writerow({k: r.get(k, '') for k in CORE})

    singles = sum(1 for r in clean if 'notes' in r)
    print(f'wrote {jf.relative_to(ROOT)}  ({len(clean)} regions)')
    print(f'wrote {cf.relative_to(ROOT)}')
    print(f'  rows carrying per-row notes: {singles}/{len(clean)}')
    print(f'  dataset_documentation keys : {len(doc)}')
    print(f'  project_notes keys         : {len(proj)}')
    print()
    print('CSV carries the core columns only. The JSON is authoritative:')
    print('  the CSV cannot represent the `notes` object, and a row without its')
    print('  notes may be missing its most important caveat.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
