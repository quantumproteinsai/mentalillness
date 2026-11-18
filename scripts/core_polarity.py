#!/usr/bin/env python3
"""Core polarity (Phi) from deposited fibril coordinates. PREREGISTRATION 10a.

Specification: reports/core_polarity_metric_2026-11-18.md, committed first.

THIS SCRIPT NEVER READS A PREDICTOR SCORE. It does not import score_rows, does not open
any file under results/, and does not know what v is. That is deliberate: Phi has three
pre-specified variants and a calibration threshold, and knowing v while computing any of
them would void the exercise. Joining Phi to v is a separate step, in a later commit.

    python3 scripts/core_polarity.py <coorddir> <out.json>

Method, exactly as registered:
  * assembly replicated along the helical axis from the DEPOSITED rise and twist, 13
    copies (-6..+6), so the analysis chain always has >= 5 subunits on each side;
    entries without helical parameters are used as deposited and flagged;
  * analysis chain = the chain of the target entity nearest the middle of the deposit
    along the helical axis, so edge layers never contribute;
  * Shrake-Rupley SASA, probe 1.4 A, 92 points, radii C 1.70 N 1.55 O 1.52 S 1.80;
  * core residue iff SASA < 10 A^2 (sensitivities 5 and 20 reported);
  * Phi = polar-or-charged fraction of core residues inside the row's range.
"""
import json
import math
import os
import sys

PROBE = 1.4
NPTS = 92
RADII = {'C': 1.70, 'N': 1.55, 'O': 1.52, 'S': 1.80}
CUTS = (5.0, 10.0, 20.0)          # 10.0 is primary; the others are pre-specified
POLAR = set('DEKRHNQSTYC')
NONPOLAR = set('AVLIMFWPG')
THREE = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C', 'GLN': 'Q',
         'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
         'MET': 'M', 'MSE': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S', 'THR': 'T',
         'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'}


def parse_cif(path):
    cols, rows = [], []
    with open(path, errors='ignore') as fh:
        inloop = False
        for ln in fh:
            if ln.startswith('loop_'):
                if rows:
                    break
                cols, inloop = [], True
                continue
            if inloop and ln.startswith('_atom_site.'):
                cols.append(ln.strip().split('.')[1])
                continue
            if cols and ln.startswith(('ATOM', 'HETATM')):
                rows.append(ln.split())
                continue
            if cols and rows and ln.startswith('#'):
                break
    ix = {c: i for i, c in enumerate(cols)}
    out = []
    for r in rows:
        if len(r) < len(cols):
            continue
        comp = r[ix['label_comp_id']]
        if comp not in THREE:
            continue
        el = r[ix['type_symbol']].strip().upper()
        if el == 'H' or el == 'D':
            continue
        try:
            num = int(r[ix.get('auth_seq_id', ix['label_seq_id'])])
            x = float(r[ix['Cartn_x']]); y = float(r[ix['Cartn_y']]); z = float(r[ix['Cartn_z']])
        except ValueError:
            continue
        out.append({'ch': r[ix.get('auth_asym_id', ix['label_asym_id'])],
                    'ent': r[ix['label_entity_id']], 'num': num, 'aa': THREE[comp],
                    'el': el, 'xyz': (x, y, z),
                    'r': RADII.get(el, 1.70)})
    return out


def sphere(n=NPTS):
    pts, off, inc = [], 2.0 / n, math.pi * (3.0 - math.sqrt(5.0))
    for i in range(n):
        y = i * off - 1 + off / 2
        rr = math.sqrt(max(0.0, 1 - y * y))
        phi = i * inc
        pts.append((math.cos(phi) * rr, y, math.sin(phi) * rr))
    return pts


SPHERE = sphere()


def replicate(atoms, rise, twist, copies=6):
    """Helical replication about z: the deposition convention for fibril reconstructions."""
    out = []
    for n in range(-copies, copies + 1):
        if n == 0:
            for a in atoms:
                b = dict(a); b['copy'] = 0
                out.append(b)
            continue
        th = math.radians(twist * n)
        c, s = math.cos(th), math.sin(th)
        dz = rise * n
        for a in atoms:
            x, y, z = a['xyz']
            b = dict(a)
            b['xyz'] = (c * x - s * y, s * x + c * y, z + dz)
            b['copy'] = n
            out.append(b)
    return out


def sasa(target, env):
    """Shrake-Rupley SASA for the target atoms, with env as the burying environment."""
    grid, cell = {}, 8.0
    for a in env:
        x, y, z = a['xyz']
        grid.setdefault((int(x // cell), int(y // cell), int(z // cell)), []).append(a)
    out = []
    for a in target:
        x, y, z = a['xyz']
        ra = a['r'] + PROBE
        near = []
        gx, gy, gz = int(x // cell), int(y // cell), int(z // cell)
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    for b in grid.get((gx + i, gy + j, gz + k), ()):
                        if b is a:
                            continue
                        bx, by, bz = b['xyz']
                        d2 = (bx - x) ** 2 + (by - y) ** 2 + (bz - z) ** 2
                        rb = b['r'] + PROBE
                        if d2 < (ra + rb) ** 2:
                            near.append((bx, by, bz, rb * rb))
        acc = 0
        for px, py, pz in SPHERE:
            tx, ty, tz = x + ra * px, y + ra * py, z + ra * pz
            for bx, by, bz, rb2 in near:
                if (tx - bx) ** 2 + (ty - by) ** 2 + (tz - bz) ** 2 < rb2:
                    break
            else:
                acc += 1
        out.append(4 * math.pi * ra * ra * acc / len(SPHERE))
    return out


def phi_variants(core):
    """core: list of (resnum, aa). Returns the primary and the two pre-specified variants."""
    def frac(sel, polar):
        if not sel:
            return None
        return sum(1 for _, aa in sel if aa in polar) / len(sel)
    primary = frac(core, POLAR)
    no_gly = frac([c for c in core if c[1] != 'G'], POLAR)
    yc_np = frac(core, POLAR - set('YC'))
    return primary, no_gly, yc_np


def analyse(path, entity, lo, hi, rise, twist, label):
    atoms = parse_cif(path)
    ent = [a for a in atoms if a['ent'] == entity]
    if not ent:
        return {'label': label, 'error': 'entity %s not found' % entity}
    # analysis chain: nearest the middle of the deposit along z (the helical axis)
    zs = {}
    for a in ent:
        zs.setdefault(a['ch'], []).append(a['xyz'][2])
    mid = sorted((sum(v) / len(v), ch) for ch, v in zs.items())
    chain = mid[len(mid) // 2][1]
    if rise and twist is not None:
        env = replicate(atoms, rise, twist)
        mode = 'replicated 13 copies (rise %.3f A, twist %.3f deg)' % (rise, twist)
    else:
        env = [dict(a, copy=0) for a in atoms]
        mode = 'AS DEPOSITED (no helical parameters)'
    target = [a for a in env if a.get('copy') == 0 and a['ch'] == chain
              and lo <= a['num'] <= hi]
    if not target:
        return {'label': label, 'error': 'no atoms in range %d-%d of chain %s' % (lo, hi, chain)}
    vals = sasa(target, env)
    per = {}
    for a, v in zip(target, vals):
        per.setdefault((a['num'], a['aa']), 0.0)
        per[(a['num'], a['aa'])] += v
    res = {'label': label, 'pdb': os.path.basename(path)[:4], 'chain': chain,
           'mode': mode, 'n_res_in_range': len(per),
           'n_env_atoms': len(env), 'range': '%d-%d' % (lo, hi)}
    for cut in CUTS:
        core = sorted([k for k, v in per.items() if v < cut])
        p, g, y = phi_variants(core)
        res['cut_%g' % cut] = {'n_core': len(core), 'phi': p, 'phi_no_gly': g,
                               'phi_YC_nonpolar': y,
                               'core_seq': ''.join(aa for _, aa in core)}
    return res


def main(coorddir, outpath, spec):
    results = []
    for job in spec:
        p = os.path.join(coorddir, job['pdb'] + '.cif')
        if not os.path.exists(p):
            results.append({'label': job['label'], 'error': 'missing ' + p})
            continue
        lo, hi = (int(x) for x in job['range'].split('-'))
        r = analyse(p, job['entity'], lo, hi, job.get('rise'), job.get('twist'), job['label'])
        r['group'] = job.get('group', '')
        results.append(r)
        e = r.get('error')
        if e:
            print('%-26s ERROR %s' % (job['label'], e))
        else:
            c = r['cut_10']
            print('%-26s %s/%s  core %2d/%2d  Phi=%s  [%s]'
                  % (job['label'], r['pdb'], r['chain'], c['n_core'], r['n_res_in_range'],
                     ('%.3f' % c['phi']) if c['phi'] is not None else '  n/a',
                     c['core_seq']))
    json.dump(results, open(outpath, 'w'), indent=1)
    print('\nwrote', outpath)
    return 0


if __name__ == '__main__':
    spec = json.load(open(sys.argv[3]))
    raise SystemExit(main(sys.argv[1], sys.argv[2], spec))
