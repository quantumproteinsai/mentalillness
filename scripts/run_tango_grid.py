#!/usr/bin/env python3
"""TANGO over the pH/temperature grid. PREREGISTRATION 5.1a.

GENERALISED 17 Nov 2026, and the default behaviour is unchanged: run with no arguments
and it reproduces the original two-accession run exactly. What changed is that the paths
and the sequence list are no longer hardcoded, because the original form could not be
re-run for a new protein without editing the script -- the same defect fixed in
score_rows.py and run_aggrescanai.py the same day.

  run_tango_grid.py                      -> the original Q9NRI5 + Q9H2D6-7 run
  run_tango_grid.py <ident> <seq|fasta>  -> one protein, same grid, same parameters

Paths, all overridable by environment variable so a clean checkout can point at wherever
the (uncommitted, licence-restricted) binary actually lives:
  TANGO_BIN   default tango_run/tango_x86_64_release
  TANGO_OUT   default tango_out
  TANGO_SEQS  default seqs            (only used by the no-argument default run)

THE BINARY IS CHECKED BEFORE ANY RUN. data/predictor_provenance.json records that TANGO's
download carries no version number, so "THE PIN IS THE SHA256" -- the digest IS the
version. A different digest is a different tool and must be recorded as a separate run,
so this script refuses to proceed on a mismatch rather than silently producing numbers
under a tool nobody pinned.
"""
import hashlib
import json
import os
import subprocess
import sys

TANGO_SHA256 = 'd0e381c28f847487069b0df29bb9d4f766391066710500d3170ecb73d9f31dbf'
GRID = [(ph, te) for ph in ('5.0', '7.0', '7.4') for te in ('298', '303', '310')]
HERE = os.path.dirname(os.path.abspath(__file__))


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def read_seq(arg):
    """A literal sequence, or a path to a FASTA/plain file holding one."""
    if os.path.exists(arg):
        lines = open(arg).read().split('\n')
        if lines and lines[0].startswith('>'):
            lines = lines[1:]
        return ''.join(x.strip() for x in lines)
    return arg.strip().upper()


def main(argv):
    binary = os.path.abspath(os.environ.get('TANGO_BIN', 'tango_run/tango_x86_64_release'))
    out = os.path.abspath(os.environ.get('TANGO_OUT', 'tango_out'))
    seqdir = os.environ.get('TANGO_SEQS', 'seqs')
    os.makedirs(out, exist_ok=True)

    if not os.path.exists(binary):
        raise SystemExit(f'TANGO binary not found at {binary}; set TANGO_BIN')
    got = sha256(binary)
    if got != TANGO_SHA256:
        raise SystemExit(
            f'TANGO BINARY DIGEST MISMATCH.\n  expected {TANGO_SHA256}\n  got      {got}\n'
            'The digest IS the version (data/predictor_provenance.json). Refusing to run: '
            'this is a different tool and must be recorded as a separate run.')
    print(f'TANGO binary verified: {got}')

    if len(argv) >= 2:
        seqs = {argv[0]: read_seq(argv[1])}
    else:
        seqs = {acc: read_seq(os.path.join(seqdir, f'{acc}.fasta'))
                for acc in ('Q9NRI5', 'Q9H2D6-7')}

    bad = 0
    for acc, seq in seqs.items():
        for ph, te in GRID:
            ident = f"{acc.replace('-', '_')}_ph{ph}_T{te}"
            cmd = [binary, ident, 'nt=N', 'ct=N', f'ph={ph}', f'te={te}', 'io=0.05',
                   'tf=0', 'stab=-10', f'seq={seq}']
            r = subprocess.run(cmd, cwd=out, capture_output=True, text=True, timeout=600)
            f = os.path.join(out, ident + '.txt')
            # TRAP 1 from the provenance: exit code is 0 on failure. Check the FILE.
            ok = os.path.exists(f) and os.path.getsize(f) > 0
            n = sum(1 for _ in open(f)) - 1 if ok else 0
            good = ok and n == len(seq)
            bad += 0 if good else 1
            print(f'{ident:28s} exit={r.returncode} file={"yes" if ok else "NO"} '
                  f'rows={n} expected={len(seq)}' + ('' if good else '   <-- MISMATCH'))
            if not ok:
                print('   stdout:', r.stdout[:200])
                print('   stderr:', r.stderr[:200])
    if bad:
        raise SystemExit(f'{bad} run(s) failed the output-file check')
    print(f'all {len(seqs) * len(GRID)} runs produced one row per residue')


if __name__ == '__main__':
    main(sys.argv[1:])
