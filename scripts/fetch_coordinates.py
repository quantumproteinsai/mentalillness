#!/usr/bin/env python3
"""Fetch the deposited coordinates the Phi analysis needs, and verify them by checksum.

PREREGISTRATION 10a requires that Phi be reproducible from this repository. The
coordinate files are not committed (they are third-party data, several megabytes, and
RCSB is the canonical source), so this script stands in their place: it pins every
accession and the SHA-256 of the exact file that was analysed.

    python3 scripts/fetch_coordinates.py <destdir>          # fetch and verify
    python3 scripts/fetch_coordinates.py <destdir> --check   # verify only
    python3 scripts/fetch_coordinates.py <destdir> --write-manifest

A MISMATCH IS NOT A WARNING. If RCSB re-versions an entry the checksum changes, and the
Phi value computed from the new file is not the Phi value in results/. The script exits
non-zero and names the entry. Re-running the analysis is then a deliberate act with a
dated note, not a silent drift.

The destination directory is written to, and nothing in it is executed or imported.
"""
import hashlib
import json
import os
import sys
import urllib.request

URL = 'https://files.rcsb.org/download/%s.cif'
UA = {'User-Agent': 'research-script'}
MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'data', 'coordinate_manifest.json')


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def ids_from_spec():
    spec = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '..', 'data', 'phi_spec.json')))
    out = []
    for group in ('rows', 'calibration'):
        for job in spec.get(group, []):
            if job['pdb'] not in out:
                out.append(job['pdb'])
    return out


def fetch(pdbid, dest):
    path = os.path.join(dest, pdbid + '.cif')
    if os.path.exists(path):
        return path, False
    req = urllib.request.Request(URL % pdbid, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    with open(path, 'wb') as fh:
        fh.write(data)
    return path, True


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    dest = argv[0]
    check_only = '--check' in argv
    write_manifest = '--write-manifest' in argv
    os.makedirs(dest, exist_ok=True)

    manifest = {}
    if os.path.exists(MANIFEST):
        manifest = json.load(open(MANIFEST)).get('sha256', {})

    bad, missing, got = [], [], {}
    for pdbid in ids_from_spec():
        path = os.path.join(dest, pdbid + '.cif')
        if not os.path.exists(path):
            if check_only:
                missing.append(pdbid)
                print('%-6s MISSING' % pdbid)
                continue
            try:
                path, fetched = fetch(pdbid, dest)
            except Exception as exc:
                missing.append(pdbid)
                print('%-6s FETCH FAILED  %s' % (pdbid, exc))
                continue
        digest = sha256(path)
        got[pdbid] = digest
        want = manifest.get(pdbid)
        if want is None:
            print('%-6s %s  (not yet pinned)' % (pdbid, digest[:16]))
        elif want == digest:
            print('%-6s %s  OK' % (pdbid, digest[:16]))
        else:
            bad.append(pdbid)
            print('%-6s %s  MISMATCH, pinned %s' % (pdbid, digest[:16], want[:16]))

    if write_manifest:
        json.dump({'_what': 'SHA-256 of the exact deposited coordinate files analysed for '
                            'Phi. Pinned so a re-version at RCSB cannot silently change a '
                            'published number. Produced by scripts/fetch_coordinates.py '
                            '--write-manifest.',
                   '_source': 'https://files.rcsb.org/download/<ID>.cif',
                   'sha256': dict(sorted(got.items()))},
                  open(MANIFEST, 'w'), indent=1)
        print('\nwrote', os.path.normpath(MANIFEST), '(%d entries)' % len(got))

    if bad:
        print('\n%d CHECKSUM MISMATCH(ES): %s' % (len(bad), ', '.join(bad)))
        return 1
    if missing:
        print('\n%d missing: %s' % (len(missing), ', '.join(missing)))
        return 1
    print('\nall %d files present and verified' % len(got))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
