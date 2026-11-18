#!/usr/bin/env python3
"""Pre-upload gate for a Zenodo deposit. Run it immediately before uploading.

WHY THIS EXISTS. Every defect in the v1.0.0 and v1.1.0 deposits was caught by a
human eye or not at all, and two were not:

  - the v1.0.0 descriptor went up with no DOIs, because the DOI was filled in
    after publication and deposited files are frozen;
  - the v1.1.0 `CITATION.cff` went up with the PRE-1.1.0 TITLE, because the title
    was updated in three places and lives in four.

RELEASE_CHECKLIST.md records both as lessons addressed to the reader. This project's
own standing rule is that **a warning in prose is not a constraint**, so the lessons
are implemented here as checks a script performs. Nothing in this file deposits
anything: it reads, compares and refuses.

    python3 scripts/preflight_deposit.py

Exit 0 means the repository side is consistent and the five files are ready to upload
BY HAND, from the author's own account, per RELEASE_CHECKLIST.md. It does not mean the
deposit happened.
"""
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = 'DOI-RESERVE-PENDING'

fail = []
warn = []


def check(ok, msg):
    (print(f'  ok    {msg}') if ok else (fail.append(msg), print(f'  FAIL  {msg}')))


def load_build():
    spec = importlib.util.spec_from_file_location('br', ROOT / 'scripts' / 'build_release.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()


def main():
    br = load_build()
    version = br.VERSION
    print(f'Preflight for v{version}\n')

    cff = (ROOT / 'CITATION.cff').read_text()
    desc_md = (ROOT / 'release' / 'DATA_DESCRIPTOR.md').read_text()
    zen = json.loads((ROOT / '.zenodo.json').read_text())

    # 1. THE DOI MUST BE RESERVED AND WRITTEN IN BEFORE UPLOAD.
    print('DOI')
    check(PLACEHOLDER not in cff,
          f'CITATION.cff has a real DOI, not the {PLACEHOLDER} placeholder')
    check(PLACEHOLDER not in desc_md,
          f'release/DATA_DESCRIPTOR.md has a real DOI, not the {PLACEHOLDER} placeholder')
    m = re.search(r'^doi:\s*"([^"]+)"', cff, re.M)
    if m and m.group(1) != PLACEHOLDER:
        doi = m.group(1)
        check(re.fullmatch(r'10\.5281/zenodo\.\d+', doi) is not None,
              f'CITATION.cff doi looks like a Zenodo DOI: {doi}')
        check(doi in desc_md, 'the same DOI appears in release/DATA_DESCRIPTOR.md')
        check(doi not in json.dumps(zen),
              'that version DOI is NOT in .zenodo.json (which is a persistent template)')

    # 2. THE TITLE LIVES IN FOUR PLACES. This is the v1.1.0 defect, as a check.
    print('\nTitle, in all four places')
    titles = {
        '.zenodo.json': zen['title'],
        'CITATION.cff': re.search(r'^title:\s*"([^"]+)"', cff, re.M).group(1),
    }
    dh = re.search(r'^# (.+)\n\n\*\*(.+)\*\*', desc_md, re.M)
    if dh:
        titles['release/DATA_DESCRIPTOR.md'] = f'{dh.group(1)}, {dh.group(2)}'
    rel_path = ROOT / 'release' / f'aggregation_regions_v{version}.json'
    if rel_path.exists():
        titles[rel_path.name] = json.loads(rel_path.read_text())['_dataset']['title']
    norm = {k: ' '.join(v.split()).rstrip('.') for k, v in titles.items()}
    check(len(set(norm.values())) == 1,
          f'all {len(norm)} copies of the title agree')
    if len(set(norm.values())) != 1:
        for k, v in norm.items():
            print(f'          {k}: {v}')

    # 3. VERSION STRINGS AGREE.
    print('\nVersion')
    check(f'version: {version}' in cff, f'CITATION.cff says version: {version}')
    check(f'Version {version} ' in desc_md, f'DATA_DESCRIPTOR.md header says Version {version}')
    for suffix in ('json', 'csv'):
        p = ROOT / 'release' / f'aggregation_regions_v{version}.{suffix}'
        check(p.exists(), f'release/{p.name} exists')

    # 4. THE ROW COUNT IS THE SAME EVERYWHERE IT IS CLAIMED.
    print('\nRow count')
    rows = json.loads((ROOT / 'data' / 'regions.json').read_text())['regions']
    n = len(rows)
    if rel_path.exists():
        rel = json.loads(rel_path.read_text())
        check(rel['_dataset']['n_regions'] == n and len(rel['regions']) == n,
              f'release artefact holds {n} regions, matching data/regions.json')
    check(f'{n} regions across' in desc_md, f'DATA_DESCRIPTOR.md header claims {n} regions')
    check(f'{n} protein regions across' in zen['description'],
          f'.zenodo.json description claims {n} protein regions')

    # 5. ALREADY-DEPOSITED ARTEFACTS MUST BE BYTE-UNCHANGED.
    #    Their files are frozen; a modified one means a DOI no longer describes
    #    what this repository produces. Checked against git, not against memory.
    print('\nPreviously deposited artefacts (frozen)')
    reg = json.loads((ROOT / 'release' / 'deposited.json').read_text())['versions']
    deposited = {v: d['doi'] for v, d in reg.items()}
    # THE REGISTRY AND THE RESERVED DOI MUST AGREE. If CITATION.cff's doi is one that
    # release/deposited.json already lists, this version has been deposited and the
    # preparation is for a version that no longer needs one.
    if m and m.group(1) in deposited.values() and deposited.get(version) != m.group(1):
        fail.append(f'CITATION.cff doi {m.group(1)} belongs to a DIFFERENT deposited version')
        print(f'  FAIL  CITATION.cff doi belongs to another version in deposited.json')
    for dv, dd in sorted(deposited.items()):
        if dv == version:
            fail.append(f'VERSION is {version} but {version} is already deposited as {dd}')
            print(f'  FAIL  VERSION is still {version}, which is deposited as {dd}')
            continue
        for suffix in ('json', 'csv'):
            f = ROOT / 'release' / f'aggregation_regions_v{dv}.{suffix}'
            if not f.exists():
                warn.append(f'{f.name} absent from the working tree')
                print(f'  warn  {f.name} absent')
                continue
            r = subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', str(f.relative_to(ROOT))],
                               cwd=ROOT)
            check(r.returncode == 0, f'{f.name} unmodified vs HEAD  (md5 {md5(f)})')

    # 6. THE FIVE FILES TO UPLOAD, AND ONLY THOSE FIVE.
    print('\nThe five files to upload')
    five = [
        f'release/aggregation_regions_v{version}.json',
        f'release/aggregation_regions_v{version}.csv',
        'release/DATA_DESCRIPTOR.md',
        'LICENSE',
        'CITATION.cff',
    ]
    for rp in five:
        p = ROOT / rp
        check(p.exists(), f'{rp}  (md5 {md5(p) if p.exists() else "-"})')
    print('\n  .zenodo.json is NOT uploaded on the manual route, and is not read by it.')
    print('  RELEASE_CHECKLIST.md is NOT uploaded: it is addressed to the author.')

    # 7. THE DESCRIPTION SNIPPET MUST BE IN STEP WITH .zenodo.json.
    print('\nDescription staging files')
    snip = ROOT / 'release' / f'zenodo_description_v{version}.snippet.html'
    if snip.exists():
        # The generator puts each block element on its own line so the snippet is
        # reviewable in a diff. Whitespace BETWEEN block-level tags is not rendered,
        # so it is collapsed away here rather than treated as a difference.
        flat = lambda t: re.sub(r'>\s+<', '><', ' '.join(t.split()))
        check(flat(snip.read_text()) == flat(zen['description']),
              'snippet matches .zenodo.json description (regenerate if not)')
    else:
        check(False, f'{snip.name} exists — run scripts/build_zenodo_description.py')

    print()
    if fail:
        print(f'REFUSING: {len(fail)} check(s) failed.')
        for f in fail:
            print(f'  - {f}')
        print('\nNothing was uploaded. Fix these, re-run, and only then upload by hand.')
        return 1
    if warn:
        print(f'{len(warn)} warning(s):')
        for w in warn:
            print(f'  - {w}')
    print('PREFLIGHT PASSED. The repository side is consistent.')
    print('THE DEPOSIT ITSELF IS STILL A MANUAL ACTION from the author\'s own Zenodo')
    print('account, per release/RELEASE_CHECKLIST.md. This script deposits nothing.')
    print('\nAfter publishing, the check that actually proves a new version went live is')
    print('the CONCEPT DOI: 10.5281/zenodo.24290697 must resolve to the new record with')
    print('is_last: true. The form displaying a DOI is not a published record.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
