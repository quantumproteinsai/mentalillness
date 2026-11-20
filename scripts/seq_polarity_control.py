#!/usr/bin/env python3
"""The sequence-polarity control on the Phi-v association. PREREGISTRATION 10d.

WHY THIS EXISTS. A prior-art audit on 19 Nov 2026 left 10a's Phi-v association as the
only part of the core-polarity work still standing, and gave it a survival condition
10a never tested: Phi may be a proxy for the mapped region's own SEQUENCE polar
fraction. Where a region is almost entirely buried, "buried and polar" and "polar" are
nearly the same statement, and if the sequence-only quantity explains v as well as Phi
does then 10a is Louros 2020 (Nat Commun 11:3314) by a more expensive route.

    python3 -I scripts/seq_polarity_control.py <repo> <coorddir> <out.json>

IT COMPUTES ONE NEW VARIABLE AND NOTHING ELSE.

    Phi_seq = fraction of residues in the WHOLE registered range that are in the SAME
              POLAR set 10a uses, DEKRHNQSTYC. Not the buried subset -- all of them.

Phi_seq is read from the SAME coordinate files Phi was computed from, over the SAME
registered ranges, by IMPORTING scripts/core_polarity.py rather than reimplementing its
parser. That matters: on 19 Nov an ad-hoc reimplementation of the v pipeline bypassed a
frame offset and produced rho = +0.633 where the committed pipeline gives +0.821. The
committed code was right and the reimplementation was wrong, so nothing is reimplemented
here.

Phi and v are READ from committed artefacts. This script computes no Phi and runs no
predictor; it cannot change either number, by construction.

THE VERDICT IS NOT CHOSEN HERE. The four outcomes and their thresholds are in
PREREGISTRATION 10d, committed in 414b139 BEFORE Phi_seq existed. This script applies
them and prints the one that fires.
"""
import importlib.util
import itertools
import json
import math
import os
import sys

POLAR = set('DEKRHNQSTYC')

# PREREGISTRATION 10d: the frozen seven, and no others. Orb2, b2m and SOD1 were recruited
# after the 10a freeze (10b S3) and are excluded from this control as they are from the
# primary. The labels are the ones used in results/core_polarity_2026-11-19/.
FROZEN = ['FUS 39-95', 'hnRNPA1 251-295', 'SAA 2-55', 'LECT2 55-75',
          'TMEM106B 120-254', 'ANXA11 39-74', 'glycinin 164-190']

# The regions.json row each label refers to, for the cross-check required by 10d.
# A disagreement here is a HARD FAILURE, not a warning: Phi and Phi_seq must be functions
# of the identical residue set, and if the curated sequence disagrees with the
# coordinates then one of the two carries a frame defect and the control stops.
ROW_OF = {
    'FUS 39-95': ('FUS', '39-95'),
    'hnRNPA1 251-295': ('hnRNPA1', '251-295'),
    'SAA 2-55': ('serum amyloid A (hSAA1.1)', '2-55'),
    'LECT2 55-75': ('LECT2', '55-75'),
    'TMEM106B 120-254': ('TMEM106B', '120-254'),
    'ANXA11 39-74': ('ANXA11', '39-74'),
    'glycinin 164-190': ('glycinin G4 (soybean)', '164-190'),
}


def load_core_polarity(repo):
    """Import the committed Phi implementation. Its parser is the one that produced the
    published numbers; using any other parser would make Phi_seq incommensurable."""
    path = os.path.join(repo, 'scripts', 'core_polarity.py')
    spec = importlib.util.spec_from_file_location('core_polarity', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- statistics
def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = math.sqrt(sum((a - mx) ** 2 for a in x))
    dy = math.sqrt(sum((b - my) ** 2 for b in y))
    return num / (dx * dy) if dx and dy else float('nan')


def spearman(x, y):
    return pearson(ranks(x), ranks(y))


def partial_spearman(x, y, z):
    """Spearman partial correlation of x with y controlling z: Pearson on the ranks."""
    rxy, rxz, ryz = spearman(x, y), spearman(x, z), spearman(y, z)
    den = math.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))
    return (rxy - rxz * ryz) / den if den else float('nan')


def exact_p(stat_fn, y, observed):
    """One-sided exact permutation p over all n! orderings of y. n = 7 gives 5040, so
    this is enumerated rather than sampled -- at this size a sampled p would add noise
    to a number whose whole purpose is to be exact."""
    hits = total = 0
    for perm in itertools.permutations(y):
        total += 1
        if stat_fn(list(perm)) >= observed - 1e-12:
            hits += 1
    return hits / total, total


def main(repo, coorddir, outpath):
    cp = load_core_polarity(repo)
    assert cp.POLAR == POLAR, (
        f'POLAR set disagrees with core_polarity.py: {sorted(cp.POLAR)} vs {sorted(POLAR)}. '
        f'10d requires the SAME set 10a used.')

    spec = json.load(open(os.path.join(repo, 'data', 'phi_spec.json')))
    phi_rows = {r['label']: r for r in json.load(open(os.path.join(
        repo, 'results', 'core_polarity_2026-11-19', 'phi_rows_11layers.json')))}
    regions = {(r['protein'], r['residues']): r for r in json.load(open(os.path.join(
        repo, 'data', 'regions.json')))['regions']}
    out = {'_what': 'PREREGISTRATION 10d: the sequence-polarity control on the Phi-v '
                    'association. Phi_seq is computed here; Phi and v are read from '
                    'committed artefacts and are not recomputed.',
           '_registered': 'PREREGISTRATION 10d, commit 414b139, BEFORE Phi_seq existed.',
           '_polar_set': ''.join(sorted(POLAR)),
           'rows': []}

    print('PHI_SEQ, computed from the pinned coordinates over the registered ranges')
    print('-' * 78)
    for label in FROZEN:
        srow = next(r for r in spec['rows'] if r['label'] == label)
        pr = phi_rows[label]
        path = os.path.join(coorddir, srow['pdb'] + '.cif')
        atoms = cp.parse_cif(path)
        rngs = cp.parse_ranges(srow['range'])
        ent = srow['entity']
        # One residue per (entity, number) in the registered range, in sequence order.
        seen, res = set(), []
        for a in atoms:
            if a['ent'] != ent or not cp.in_ranges(a['num'], rngs):
                continue
            if a['num'] in seen:
                continue
            seen.add(a['num'])
            res.append((a['num'], a['aa']))
        res.sort()
        seq = ''.join(aa for _, aa in res)
        n_pol = sum(1 for c in seq if c in POLAR)
        phi_seq = n_pol / len(seq)

        # ---- the cross-check 10d requires. A mismatch stops the control.
        prot, resid = ROW_OF[label]
        curated = (regions[(prot, resid)].get('sequence') or '').replace('|', '')
        agree = (curated == seq)
        note = ''
        if not agree:
            if len(curated) == len(seq):
                note = 'SAME LENGTH, DIFFERENT RESIDUES'
            else:
                note = f'LENGTH {len(curated)} vs {len(seq)}'

        assert len(seq) == pr['n_res_in_range'], (
            f'{label}: {len(seq)} residues parsed but the Phi run recorded '
            f'n_res_in_range={pr["n_res_in_range"]}')

        print(f'{label:22s} n={len(seq):3d}  phi_seq={phi_seq:.4f}  '
              f'phi(cut10)={pr["cut_10"]["phi"]:.4f}  '
              f'curated seq {"AGREES" if agree else "DISAGREES: " + note}')
        out['rows'].append({
            'label': label, 'pdb': srow['pdb'], 'range': srow['range'],
            'n_res': len(seq), 'region_seq': seq, 'n_polar': n_pol,
            'phi_seq': phi_seq,
            'phi_cut_5': pr['cut_5']['phi'], 'phi_cut_10': pr['cut_10']['phi'],
            'n_core_cut_5': pr['cut_5']['n_core'], 'n_core_cut_10': pr['cut_10']['n_core'],
            'curated_sequence_agrees': agree, 'curated_sequence_note': note,
        })

    mismatches = [r['label'] for r in out['rows'] if not r['curated_sequence_agrees']]
    if mismatches:
        print()
        print('STOP. The curated sequence disagrees with the coordinates on: '
              + ', '.join(mismatches))
        print('PREREGISTRATION 10d makes this a HARD FAILURE, not a warning: Phi and '
              'Phi_seq must be')
        print('functions of the identical residue set. Resolve the frame defect before '
              'reading any')
        print('statistic below.')
        out['HALTED'] = mismatches
        json.dump(out, open(outpath, 'w'), indent=1)
        return 1

    # ---------------------------------------------------------------- the three statistics
    # v COMES FROM THE COMMITTED PIPELINE, BY IMPORTING THE COMMITTED JOIN. get_v() runs
    # scripts/score_rows.py and parses its table, so these are the pipeline's numbers and
    # not transcribed ones. On 19 Nov an ad-hoc reimplementation of this step bypassed a
    # frame offset and gave rho = +0.633 where the committed pipeline gives +0.821.
    jspec = importlib.util.spec_from_file_location(
        'join_phi_v', os.path.join(repo, 'scripts', 'join_phi_v.py'))
    jpv = importlib.util.module_from_spec(jspec)
    jspec.loader.exec_module(jpv)
    vtab = jpv.get_v(repo)
    V = {label: vtab[ROW_OF[label]] for label in FROZEN}
    v = [V[r['label']] for r in out['rows']]
    s = [r['phi_seq'] for r in out['rows']]

    out['v'] = {r['label']: V[r['label']] for r in out['rows']}
    out['_v_source'] = ('scripts/score_rows.py, via join_phi_v.get_v() -- the committed '
                        'pipeline, run here, not transcribed.')

    # THE REPRODUCTION CHECK. If rho(Phi_cut10, v) does not come back at the published
    # +0.821, then the inputs assembled here are not the inputs 10a used and nothing
    # below means anything. Checked before any new statistic is read.
    repro = spearman([r['phi_cut_10'] for r in out['rows']], v)
    out['_reproduction_check'] = {'rho_phi_v_cut_10': repro, 'published': 0.821}
    print()
    print(f'REPRODUCTION CHECK: rho(Phi cut_10, v) = {repro:+.4f}, published +0.821')
    assert abs(repro - 0.821) < 0.001, (
        f'rho(Phi,v) reproduces as {repro:+.4f}, not the published +0.821. The inputs '
        f'assembled here are NOT the inputs 10a used. STOP.')
    print('  reproduced -- the inputs are 10a\'s inputs.')
    out['cutoffs'] = {}
    verdicts = {}
    for cut in ('cut_5', 'cut_10'):
        p = [r['phi_' + cut] for r in out['rows']]
        r_phi_v = spearman(p, v)
        r_seq_v = spearman(s, v)
        r_phi_seq = spearman(p, s)
        pr_partial = partial_spearman(p, v, s)

        p_seq_v, n_perm = exact_p(lambda yy: spearman(s, yy), v, r_seq_v)
        p_phi_v, _ = exact_p(lambda yy: spearman(p, yy), v, r_phi_v)
        p_partial, _ = exact_p(lambda yy: partial_spearman(p, yy, s), v, pr_partial)

        # PREREGISTRATION 10d decision rule. Applied, not chosen.
        if r_seq_v >= r_phi_v:
            verdict = 'COLLAPSED'
        elif pr_partial < 0.5:
            verdict = 'NOT_SEPARABLE'
        elif pr_partial >= 0.7 and r_phi_v > r_seq_v:
            verdict = 'SURVIVES'
        else:
            verdict = 'INCONCLUSIVE'
        verdicts[cut] = verdict

        out['cutoffs'][cut] = {
            'rho_phi_v': r_phi_v, 'p_phi_v': p_phi_v,
            'rho_phiseq_v': r_seq_v, 'p_phiseq_v': p_seq_v,
            'rho_phi_phiseq': r_phi_seq,
            'partial_rho_phi_v_given_phiseq': pr_partial, 'p_partial': p_partial,
            'n_permutations': n_perm,
            'verdict': verdict,
        }

        print()
        print(f'=== {cut}  (burial threshold {cut.split("_")[1]} A^2)')
        print(f'  rho(Phi,     v)              = {r_phi_v:+.4f}   exact one-sided p = {p_phi_v:.4f}')
        print(f'  rho(Phi_seq, v)              = {r_seq_v:+.4f}   exact one-sided p = {p_seq_v:.4f}')
        print(f'  rho(Phi, Phi_seq)            = {r_phi_seq:+.4f}   <- collinearity')
        print(f'  partial rho(Phi, v | Phi_seq)= {pr_partial:+.4f}   exact one-sided p = {p_partial:.4f}')
        print(f'  VERDICT (PREREG 10d)         : {verdict}')

    # ---- rule 2: a verdict that differs between the registered cutoffs is unresolved
    final = verdicts['cut_10'] if verdicts['cut_5'] == verdicts['cut_10'] \
        else 'UNRESOLVED_AT_THIS_N'
    out['registered_verdict'] = final
    out['verdict_by_cutoff'] = verdicts

    print()
    print('=' * 78)
    print(f'REGISTERED VERDICT: {final}')
    if final == 'UNRESOLVED_AT_THIS_N':
        print('  The two registered burial cutoffs give different verdicts '
              f'({verdicts["cut_5"]} at 5 A^2, {verdicts["cut_10"]} at 10 A^2).')
        print('  PREREGISTRATION 10d: that is UNRESOLVED_AT_THIS_N, not the cut-10 answer')
        print('  with the cut-5 answer in a footnote.')
    elif final == 'SURVIVES':
        print('  READ 10d BEFORE QUOTING THIS. SURVIVES excludes ONE way of being wrong at')
        print('  n = 7. It does not promote the claim and licenses no stronger wording')
        print('  anywhere. The association remains not robust and not established.')
    print()
    print('  The p-values are exact and cheap. They are NOT evidence: at n = 7 with two')
    print('  collinear predictors a partial correlation is a descriptive quantity. The')
    print('  point estimates and the collinearity are the result.')

    json.dump(out, open(outpath, 'w'), indent=1)
    print(f'\nwrote {outpath}')
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
