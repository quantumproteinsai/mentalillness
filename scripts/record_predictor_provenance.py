#!/usr/bin/env python3
"""Capture an immutable record of a locally installed predictor binary.

WHY THIS EXISTS. PREREGISTRATION.md §12 step 4 requires predictor versions to be
recorded before the freeze, and §5.2's whole rule for admitting a tool is that it
be VERSION-PINNABLE. But the TANGO academic download page (16 Nov 2026) offers
files named only "Executable Tango - Linux 64bits", with NO VERSION NUMBER
anywhere on the page.

A tool that ships no version string is not pinnable by version. It is pinnable by
CHECKSUM, and nothing else. This script makes that pin, so that "version-pinned"
is a fact on disk rather than an aspiration.

    python3 scripts/record_predictor_provenance.py TANGO /path/to/tango_x86_64

It appends to data/predictor_provenance.json. It never overwrites an existing
record for the same (tool, sha256) pair -- if the checksum changes, that is a
NEW record and the divergence is visible.

WHAT IT CANNOT DO. It cannot tell you the tool is correct, only which exact bytes
you ran. Whether those bytes reproduce the published 2014 behaviour is a separate
question and is §5.1's reimplementation-validation problem.
"""
import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / 'data' / 'predictor_provenance.json'


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def probe_version(p: Path) -> dict:
    """Try, without assuming, to coax a version string out of the binary."""
    out = {}
    for flag in ('--version', '-v', '-V', '--help', '-h'):
        try:
            r = subprocess.run([str(p), flag], capture_output=True, timeout=10, text=True)
            txt = ((r.stdout or '') + (r.returncode and (r.stderr or '') or '')).strip()
            if txt:
                out[flag] = txt[:2000]
        except Exception as e:
            out[flag] = f'<{type(e).__name__}: {e}>'
    try:
        r = subprocess.run(['strings', '-n', '4', str(p)], capture_output=True, timeout=20, text=True)
        hits = [l for l in (r.stdout or '').splitlines()
                if any(k in l.lower() for k in ('version', 'tango', '20', 'v1.', 'v2.'))]
        out['_strings_candidates'] = hits[:40]
    except Exception as e:
        out['_strings_candidates'] = f'<{type(e).__name__}: {e}>'
    return out


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    tool, path = argv[1], Path(argv[2]).resolve()
    if not path.is_file():
        print(f'ERROR: not a file: {path}')
        return 1

    digest = sha256(path)
    try:
        ftype = subprocess.run(['file', '-b', str(path)], capture_output=True,
                               timeout=10, text=True).stdout.strip()
    except Exception:
        ftype = '<file(1) unavailable>'

    record = {
        'tool': tool,
        'sha256': digest,
        'size_bytes': path.stat().st_size,
        'file_type': ftype,
        'local_path_at_capture': str(path),
        'captured_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'captured_on': {
            'platform': platform.platform(),
            'machine': platform.machine(),
            'python': platform.python_version(),
        },
        'version_probe': probe_version(path),
        'THE_PIN_IS_THE_SHA256': (
            'The TANGO academic download page carries NO version number -- its files are named '
            'only by platform, e.g. "Executable Tango - Linux 64bits". So the sha256 above IS the '
            'version for the purposes of PREREGISTRATION 5.2 and 12 step 4. Cite it as such. If a '
            'future download of "the same" file yields a different digest, that is a different '
            'tool and must be recorded as a separate run.'),
        'STILL_TO_BE_FILLED_BY_THE_AUTHOR': {
            'download_url': '',
            'download_date': '',
            'licence_type': 'academic',
            'exact_invocation': '',
            'parameters_vs_bradshaw_2014': (
                'Bradshaw 2014 (PLoS ONE 9:e111196) ran TANGO with "both alpha helix and beta '
                'sheet aggregation using default parameters, threshold = 5%". Record here whether '
                'this build exposes those as flags and whether the defaults match. IF THEY DIVERGE, '
                'THAT IS A FINDING ABOUT TOOL DRIFT, not an error to reconcile away.'),
        },
    }

    store = json.loads(STORE.read_text()) if STORE.exists() else {
        '_what': 'Immutable provenance records for locally installed predictors, required by '
                 'PREREGISTRATION.md 12 step 4. Append-only: a changed checksum makes a NEW '
                 'record, it never edits an old one.',
        'records': [],
    }
    for r in store['records']:
        if r['tool'] == tool and r['sha256'] == digest:
            print(f'Already recorded: {tool} sha256={digest[:16]}... (no change)')
            return 0
    store['records'].append(record)
    STORE.write_text(json.dumps(store, indent=2, ensure_ascii=True) + '\n')

    print(f'RECORDED  {tool}')
    print(f'  sha256     {digest}')
    print(f'  size       {record["size_bytes"]} bytes')
    print(f'  file       {ftype}')
    print(f'  -> {STORE.relative_to(ROOT)}  ({len(store["records"])} record(s))')
    print()
    print('NOW FILL IN by hand, in that file:')
    for k in record['STILL_TO_BE_FILLED_BY_THE_AUTHOR']:
        print(f'  - {k}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
