#!/usr/bin/env python3
"""Is a deposit owed, and what would be in it?

WHY THIS EXISTS. The policy is to BATCH changes rather than mint a DOI per edit: three
deposits were made in two days, and a dataset whose version number moves faster than its
content is harder to cite, not easier. But "batch it" becomes "forget it" unless something
can say what has accumulated. This says it.

    python3 scripts/deposit_status.py

It compares the CURRENT data/regions.json, passed through the same transform
build_release.py uses -- imported, not reimplemented, so the two cannot drift -- against
the artefact of the most recently deposited version. It reads only, writes nothing, and
touches no network.

IT DOES NOT DECIDE. Whether an accumulated change is worth a version is a judgement about
what a reader of the DOI would be misled by, and that is the author's.
"""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_builder():
    spec = importlib.util.spec_from_file_location('br', ROOT / 'scripts' / 'build_release.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def latest(reg):
    return sorted(reg, key=lambda v: [int(x) for x in v.split('.')])[-1]


def key(r):
    return (r.get('protein'), r.get('residues'))


def main():
    br = load_builder()
    reg = json.loads((ROOT / 'release' / 'deposited.json').read_text())['versions']
    dv = latest(reg)
    dep_path = ROOT / 'release' / f'aggregation_regions_v{dv}.json'

    print(f'Latest deposit: v{dv}  {reg[dv]["doi"]}')
    print(f'                {reg[dv]["record"]}')
    if not dep_path.exists():
        raise SystemExit(f'{dep_path.name} is missing; cannot compare.')

    dep = json.loads(dep_path.read_text())
    now = br.build(dv)          # same transform, same version string, so only DATA differs

    if json.dumps(dep, sort_keys=True) == json.dumps(now, sort_keys=True):
        print('\nNO DEPOSIT OWED. The working file reproduces the deposited artefact exactly.')
        return 0

    print('\nA DEPOSIT IS OWED. What has accumulated since:\n')

    dr = {key(r): r for r in dep['regions']}
    nr = {key(r): r for r in now['regions']}

    added, removed = sorted(set(nr) - set(dr)), sorted(set(dr) - set(nr))
    if added:
        print(f'  ROWS ADDED ({len(added)}):')
        for k in added:
            print(f'      + {k[0]} {k[1]}')
    if removed:
        print(f'  ROWS REMOVED ({len(removed)}):')
        for k in removed:
            print(f'      - {k[0]} {k[1]}')

    # Field-level changes on rows present in both, split into the ones a reader of the
    # dataset acts on and the ones that are commentary.
    CORE = set(br.CORE)
    changed = []
    for k in sorted(set(dr) & set(nr)):
        a, b = dr[k], nr[k]
        diffs = sorted({f for f in set(a) | set(b)
                        if json.dumps(a.get(f), sort_keys=True)
                        != json.dumps(b.get(f), sort_keys=True)})
        if diffs:
            changed.append((k, diffs))
    if changed:
        print(f'  ROWS CHANGED ({len(changed)}):')
        for k, diffs in changed:
            core = [f for f in diffs if f in CORE]
            other = [f for f in diffs if f not in CORE]
            print(f'      ~ {k[0]} {k[1]}')
            if core:
                print(f'          CORE   : {", ".join(core)}')
            if other:
                print(f'          notes  : {", ".join(other)}')

    da, na = set(dep.get('dataset_documentation', {})), set(now.get('dataset_documentation', {}))
    if na - da:
        print(f'  DATASET DOCUMENTATION ADDED ({len(na - da)}):')
        for k in sorted(na - da):
            print(f'      + {k}')
    if da - na:
        print(f'  DATASET DOCUMENTATION REMOVED ({len(da - na)}):')
        for k in sorted(da - na):
            print(f'      - {k}')

    # Project notes are in the artefact too, so a change there is a change to the
    # deposited object. Reported separately because they are provenance rather than
    # data: a reader of the dataset can ignore them, a reader auditing it cannot.
    dp = set(dep.get('project_notes', {})) - {'_what_these_are'}
    np_ = set(now.get('project_notes', {})) - {'_what_these_are'}
    if np_ - dp:
        print(f'  PROJECT NOTES ADDED ({len(np_ - dp)}):')
        for k in sorted(np_ - dp):
            print(f'      + {k}')
    if dp - np_:
        print(f'  PROJECT NOTES REMOVED ({len(dp - np_)}):')
        for k in sorted(dp - np_):
            print(f'      - {k}')
    both = dp & np_
    moved = [k for k in sorted(both)
             if json.dumps(dep['project_notes'][k], sort_keys=True)
             != json.dumps(now['project_notes'][k], sort_keys=True)]
    if moved:
        print(f'  PROJECT NOTES CHANGED ({len(moved)}):')
        for k in moved:
            print(f'      ~ {k}')

    print('\n  Row count: %d deposited -> %d now.' % (len(dr), len(nr)))
    print('\nWHETHER THIS IS WORTH A VERSION IS A JUDGEMENT, NOT A COUNT.')
    print('The question RELEASE_CHECKLIST.md asks: would a reader who found the DOI and')
    print('not the repository be misled by what is missing? A corrected claim or a changed')
    print('label says yes. More commentary on a row says no, and can wait for the next one.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
