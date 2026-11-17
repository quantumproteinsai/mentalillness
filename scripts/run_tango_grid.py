import os, subprocess, sys
BIN = os.path.abspath('tango_run/tango_x86_64_release')
OUT = os.path.abspath('tango_out'); os.makedirs(OUT, exist_ok=True)
SEQS = {}
for acc, f in (('Q9NRI5','seqs/Q9NRI5.fasta'), ('Q9H2D6-7','seqs/Q9H2D6-7.fasta')):
    SEQS[acc] = ''.join(x.strip() for x in open(f).readlines()[1:])
GRID = [(ph, te) for ph in ('5.0','7.0','7.4') for te in ('298','303','310')]
for acc, seq in SEQS.items():
    for ph, te in GRID:
        ident = f"{acc.replace('-','_')}_ph{ph}_T{te}"
        cmd = [BIN, ident, 'nt=N', 'ct=N', f'ph={ph}', f'te={te}', 'io=0.05',
               'tf=0', 'stab=-10', f'seq={seq}']
        r = subprocess.run(cmd, cwd=OUT, capture_output=True, text=True, timeout=600)
        f = os.path.join(OUT, ident + '.txt')
        # TRAP 1 from the provenance: exit code is 0 on failure. Check the FILE.
        ok = os.path.exists(f) and os.path.getsize(f) > 0
        n = sum(1 for _ in open(f)) - 1 if ok else 0
        print(f'{ident:28s} exit={r.returncode} file={"yes" if ok else "NO"} rows={n} expected={len(seq)}'
              + ('' if n == len(seq) else '   <-- MISMATCH'))
        if not ok:
            print('   stdout:', r.stdout[:200]); print('   stderr:', r.stderr[:200])
