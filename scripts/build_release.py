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
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'data' / 'regions.json'
OUT = ROOT / 'release'
VERSION = '1.3.0'

CORE = [
    'protein', 'residues', 'frame', 'sequence', 'evidence', 'construct',
    'found_by', 'source', 'verified_against', 'verified_against_publisher_pdf',
    'source_version', 'source_version_note', 'circularity_status',
    'circularity_basis', 'stratum', 'stratum_basis',
    # Added 17 Nov 2026 by the PREREGISTRATION 5.2b item 4 check. These are CORE,
    # not commentary: a consumer who cannot see that a row's protein is in CPAD
    # cannot tell a modern predictor's recall from its prediction.
    'cpad_status', 'cpad_basis', 'cpad_checked',
    # Added 18 Nov 2026 by the §7a stratum assignment. CORE, not commentary: it carries
    # confirmatory_eligible, and a consumer who cannot see that flag cannot reproduce the
    # confirmatory set -- the stratum label alone does not admit a row.
    'stratum_assignment',
    'sequence_provenance', 'range_provenance', 'note',
]

# Versions already deposited under a DOI. Their files are frozen and MUST NOT be
# regenerated with different content: the DOI would then point at something other
# than what this script produces. Bump VERSION and deposit a new version instead.
# See release/RELEASE_CHECKLIST.md.
# WHICH VERSIONS ARE DEPOSITED IS NOW READ FROM release/deposited.json, NOT HARDCODED.
# This was a literal here, and twice in two days the just-deposited version was missing
# from it, so the guard below could not fire and overwrote deposited artefacts: 1.1.0 on
# 17 Nov, then 1.2.0 on 18 Nov -- the second time one day after the first was written up
# as a lesson. A literal is edited by whoever remembers. A file both scripts read, and
# that preflight_deposit.py refuses to let fall out of step, is edited because something
# checks it.
def _deposited():
    p = ROOT / 'release' / 'deposited.json'
    if not p.exists():
        raise SystemExit('release/deposited.json is missing: it records which versions are '
                         'frozen under a DOI, and without it the freeze guard cannot run.')
    return {v: d['doi'] for v, d in json.loads(p.read_text())['versions'].items()}


DEPOSITED = None  # populated in main(); see _deposited()

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
    # Added 17 Nov 2026. It documents the `cpad_*` columns and states what the
    # check could NOT reach, which a consumer needs in order to know how far to
    # trust an 'absent' verdict. Dataset documentation, not a project note.
    '_CPAD_MEMBERSHIP_CHECK_2026-11-17',
    # Both added 17 Nov 2026 for v1.2.0, and both qualify a column a consumer will
    # otherwise over-trust.
    #   The decoy-window rule is about how to read `frame`: it states that scoring a
    #   region inside a frame containing a hydrophobic segment that was never in the
    #   sample -- a signal peptide, a transmembrane helix -- inflates the apparent
    #   failure of every predictor. The glycinin row's own caveat points at it, and a
    #   consumer who re-scores these rows in a different frame will get different
    #   numbers for that reason and no other. Same class as
    #   `_frame_traps_are_worse_than_assumed`, which was already dataset documentation.
    #   The name-vs-accession limit states what the CPAD screen could NOT reach, and so
    #   how far a CPAD_ABSENT verdict can be trusted. An absence is only as good as the
    #   demonstrated sensitivity of the search that produced it.
    '_A_HYDROPHOBIC_SEGMENT_THAT_IS_NOT_IN_THE_SAMPLE_IS_A_DECOY_WINDOW',
    '_A_NAME_SEARCH_IS_NOT_AN_ACCESSION_SEARCH__A_LIMIT_OF_OUR_OWN_CPAD_CHECK',
    # Added 18 Nov 2026. It documents what stratum_assignment means, why six rows carrying
    # a DISCORDANT label are nonetheless not in the confirmatory set, and why the honest
    # unit of analysis is the protein rather than the row. A consumer who misses it will
    # read the stratum column as admitting rows it does not admit.
    '_THE_STRATUM_ASSIGNMENT_OF_18_NOV_2026__A_REGISTERED_RULE_APPLIED_TOO_LATE',
}
# Everything else is a project note: true, kept, but about THIS PROJECT's
# hypotheses and workflow rather than about the data.


def main():
    global DEPOSITED
    DEPOSITED = _deposited()
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
            # THE TITLE LIVES IN FOUR PLACES, NOT THREE. RELEASE_CHECKLIST.md's
            # "lesson for next time" names .zenodo.json, CITATION.cff and
            # DATA_DESCRIPTOR.md -- and misses this one, which is why the deposited
            # v1.1.0 artefact carries the pre-1.1.0 title. It was corrected here on
            # 17 Nov 2026 for v1.2.0. Changing it in three places and diffing those
            # three against each other is precisely the check that passes while this
            # line stays stale.
            'title': 'Experimentally mapped aggregation-critical protein regions, '
                     'with circularity, prediction-concordance and '
                     'training-set-contamination labels',
            'version': VERSION,
            'n_regions': len(clean),
            'generated_by': 'scripts/build_release.py, from data/regions.json',
            'READ_THIS_FIRST': 'release/DATA_DESCRIPTOR.md',
            'WHAT_MAKES_THIS_DIFFERENT_FROM_OTHER_AGGREGATION_DATASETS':
                'FOUR columns that aggregation datasets usually lack -- four since 1.1.0, and '
                'this sentence said three until v1.2.0 corrected it. `construct` records WHICH '
                'construct established the region, because a region can be necessary in one and '
                'dispensable in another. `circularity_status` records whether a PREDICTOR was in '
                'the discovery path, which makes a row unusable for benchmarking the predictor '
                'family that found it. `stratum` records whether experiment and prediction AGREE, '
                'which is what decides whether a row can discriminate between predictors at all. '
                '`cpad_status` records whether the row\'s protein is in CPAD 2.0, and therefore '
                'whether a modern predictor\'s hit on it may be recall of training data rather '
                'than prediction. THESE ARE THREE DIFFERENT KINDS OF CIRCULARITY -- the discovery '
                'path, experiment-prediction agreement, and training-set membership -- and a row '
                'can be clean on one and contaminated on another.',
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
    payload = json.dumps(release, indent=2, ensure_ascii=True) + '\n'

    # A DEPOSITED VERSION IS FROZEN: refuse to rewrite it with different content,
    # rather than let a DOI quietly stop describing what this script produces.
    #
    # REWRITTEN 17 Nov 2026, BECAUSE THE PREVIOUS FORM OF THIS GUARD DID NOT WORK AND
    # WAS PROVED NOT TO WORK BY RUNNING IT. It compared the set of CORE FIELD NAMES in
    # the working file against those in the deposited artefact, and refused only when a
    # field had been ADDED. Four rows were added to the dataset between v1.1.0 and
    # v1.2.0 and not one new field, so the check passed and the deposited v1.1.0 files
    # were overwritten with 21 rows. They were recovered from git, and their md5s
    # re-verified against the ones in the `deposited-v1.1.0` tag message, which is the
    # only reason this is a near miss and not a lost deposit.
    #
    # The guard now compares THE BYTES IT IS ABOUT TO WRITE against the bytes on disk.
    # That is the property actually wanted -- the artefact is unchanged -- and it does
    # not depend on anyone predicting which kind of change matters. The lesson is the
    # project's own: a check that interrogates a proxy for the thing is not a check on
    # the thing.
    if VERSION in DEPOSITED and jf.exists():
        if jf.read_text() != payload:
            have = json.loads(jf.read_text())
            raise SystemExit(
                f'REFUSING TO REBUILD v{VERSION}: it is deposited as '
                f'{DEPOSITED[VERSION]} and its files are frozen, but this build would '
                f'change them.\n'
                f'  on disk (deposited): {len(have.get("regions", []))} regions\n'
                f'  this build would write: {len(clean)} regions\n'
                f'Bump VERSION in this script and deposit a new version. '
                f'See release/RELEASE_CHECKLIST.md.')

    jf.write_text(payload)

    cf = OUT / f'aggregation_regions_v{VERSION}.csv'
    rendered = io.StringIO()
    w = csv.DictWriter(rendered, fieldnames=CORE, extrasaction='ignore', lineterminator='\r\n')
    w.writeheader()
    for r in clean:
        w.writerow({k: r.get(k, '') for k in CORE})
    if VERSION in DEPOSITED and cf.exists() and cf.read_bytes() != rendered.getvalue().encode():
        raise SystemExit(
            f'REFUSING TO REBUILD v{VERSION}: the CSV is deposited as '
            f'{DEPOSITED[VERSION]} and this build would change it. '
            f'Bump VERSION. See release/RELEASE_CHECKLIST.md.')
    with cf.open('w', newline='') as fh:
        fh.write(rendered.getvalue())

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
