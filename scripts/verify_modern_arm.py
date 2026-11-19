#!/usr/bin/env python3
"""Re-run an ARCHIVED AggrescanAI profile and compare it to the committed CSV, bit for bit.

WHY THIS EXISTS. On 19 Nov 2026 the modern arm had to be rebuilt from scratch: the venv,
the site-packages and the multi-gigabyte weights from the 17-18 Nov runs were all gone,
having lived in a session scratchpad that was cleared. The WEIGHTS are pinned by revision
and checksummed, and they came back identical. THE SOFTWARE THAT RUNS THEM WAS NEVER
PINNED: data/predictor_provenance.json holds exactly one record, TANGO, and no report in
this project names a torch, tensorflow, keras or transformers version.

So the rebuilt stack may or may not be the tool that produced the committed numbers, and
NOTHING IN THE PIPELINE WOULD NOTICE. By this project's own TANGO precedent -- "the digest
IS the version; a different digest is a different tool and must be recorded as a separate
run" -- a changed software stack is a changed tool until shown otherwise.

    python3 scripts/verify_modern_arm.py <repo> <archived.csv> <out.csv>

This re-runs the archived case and compares every residue. It is the cheap output that
decides whether the expensive ones are trustworthy, and it runs BEFORE any new sequence is
scored. If it fails, the correct response is NOT to adjust a tolerance: it is to record a
second predictor_provenance record and treat every number produced by the new stack as
belonging to a different run.

EXIT 0 only if every residue matches to the 6 decimal places the CSV stores.
"""
import os
import subprocess
import sys


def read_profile(path):
    """Returns (header_lines, [(pos, aa, score, spread)])."""
    head, rows = [], []
    with open(path) as fh:
        for ln in fh:
            ln = ln.rstrip('\n')
            if ln.startswith('#'):
                head.append(ln)
                continue
            if ln.startswith('position,'):
                continue
            if not ln.strip():
                continue
            p, a, s, d = ln.split(',')
            rows.append((int(p), a, s, d))
    return head, rows


def main(repo, archived, out):
    head, old = read_profile(archived)
    meta = {}
    for h in head:
        if '=' in h:
            k, _, v = h.lstrip('# ').partition('=')
            meta[k.strip()] = v.strip()
    ident = meta.get('id')
    seq = ''.join(a for _, a, _, _ in old)
    if not ident:
        raise SystemExit('archived CSV has no id= header: %s' % archived)
    print('archived : %s  (%s, %d residues)' % (os.path.relpath(archived, repo), ident, len(seq)))

    cmd = [sys.executable, '-I', os.path.join(repo, 'scripts', 'run_aggrescanai.py'),
           out, ident, seq]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
    if r.returncode != 0:
        print(r.stdout[-3000:])
        print(r.stderr[-3000:])
        raise SystemExit('THE RUNNER FAILED. The rebuilt stack cannot reproduce the '
                         'archived case at all, which is a stronger negative than a '
                         'numeric mismatch.')
    print(r.stdout.strip())

    newhead, new = read_profile(out)
    if len(new) != len(old):
        raise SystemExit('LENGTH MISMATCH: archived %d rows, rebuilt %d' % (len(old), len(new)))

    # the model digests must match too -- same weights, or the comparison is meaningless
    om = sorted(h for h in head if h.startswith('# model '))
    nm = sorted(h for h in newhead if h.startswith('# model '))
    print('model digests identical: %s' % (om == nm))
    if om != nm:
        raise SystemExit('THE WEIGHTS DIFFER. Fix that before reading anything below.')

    bad = []
    worst = 0.0
    for (p1, a1, s1, d1), (p2, a2, s2, d2) in zip(old, new):
        if (p1, a1) != (p2, a2):
            raise SystemExit('ALIGNMENT MISMATCH at %d: %s vs %s' % (p1, a1, a2))
        worst = max(worst, abs(float(s1) - float(s2)))
        if s1 != s2:
            bad.append((p1, a1, s1, s2))

    print()
    print('residues compared      : %d' % len(old))
    print('exact string matches   : %d' % (len(old) - len(bad)))
    print('differing residues     : %d' % len(bad))
    print('largest absolute delta : %.6g' % worst)
    for p, a, s1, s2 in bad[:10]:
        print('   %4d %s  archived %s  rebuilt %s' % (p, a, s1, s2))
    if len(bad) > 10:
        print('   ... and %d more' % (len(bad) - 10))

    print()
    if not bad:
        print('VERDICT: BIT-IDENTICAL. The rebuilt stack reproduces the committed profile '
              'exactly.')
        print('         New runs on this stack belong to the same run as 17-18 Nov.')
        return 0
    print('VERDICT: THE REBUILT STACK IS A DIFFERENT TOOL.')
    print('         Do NOT widen a tolerance to make this pass. Record a second')
    print('         predictor_provenance entry and treat new numbers as a separate run,')
    print('         exactly as the TANGO digest rule requires.')
    return 1


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
