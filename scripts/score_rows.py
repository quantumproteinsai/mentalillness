#!/usr/bin/env python3
"""Compute the PREREGISTRATION 3.1 statistic for AggrescanAI. No tuning, no choices left.

  window = 6 (5.3: PLM tools per-residue, aggregated to 6-residue means)
  M = windows in protein; m = windows WHOLLY inside the region
  P = (# windows scoring <= region's best window) / M, MIDRANK ties
  v = 1 - P^m        ~ Uniform(0,1) under H0; small v = predictor succeeded

Combination: Stouffer's Z primary (equal weights, one-sided), Fisher secondary.
Both always reported (3.1).
"""
import csv
import json
import math
import os
import re
import sys

W = 6
BAR = 0.05          # PREREGISTRATION 4: a row is "recovered" iff v < BAR.
HERE = os.path.dirname(os.path.abspath(__file__))

# WHERE THE PROFILES LIVE. Corrected 17 Nov 2026. These paths used to carry a "runs/" prefix
# resolved against this script's own directory -- a working directory that was never
# committed and no longer exists, so THE SCRIPT AS COMMITTED COULD NOT BE RE-RUN, while
# results/aggrescanai_2026-11-17/REPORT.md said "Reproduce with ... scripts/score_rows.py".
# An archived output plus a script that cannot find it is not a reproducible result. The
# profiles ARE committed, under the dated results directory, which is now the path used.
RUNDIR = os.path.join(HERE, os.pardir, 'results', 'aggrescanai_2026-11-17')

# row protein -> the run file, and the frame that run is in.
RUNS = {
    'TRIOBP-1': ('Q9H2D6-7.csv', '652-residue (Q9H2D6-7)'),
    'DISC1': ('Q9NRI5.csv', '854-residue canonical (Q9NRI5)'),
    'tau': ('P10636-8.csv', 'tau441 / ht40 (P10636-8)'),
    'alpha-synuclein': ('P37840_asyn.csv', 'P37840, 140 aa'),
    'FUS': ('P35637.csv', 'P35637, 526 aa'),
    'hnRNPA1': ('P09651-2.csv', 'P09651-2, 320 aa'),
    # Added 17 Nov 2026 once the mature-chain frames were resolved AND verified.
    # hSAA1.1 is P0DJI8 mature with A52V -- NOT canonical, which differs inside the region.
    'serum amyloid A (hSAA1.1)': ('hSAA1.1_mature.csv', 'mature hSAA1.1, 104 aa (P0DJI8 mature + A52V)'),
    'LECT2': ('LECT2_mature.csv', 'mature LECT2, 133 aa (O14960[19:151])'),
    'TMEM106B': ('Q9NUM4.csv', '274-residue canonical Q9NUM4'),
    # Added 17 Nov 2026. The profile was generated in the 17 Nov run and archived, but
    # the row went unscored only because this dict had no entry for it. No signal peptide
    # and no transmembrane segment in P50995, so the frame carries no decoy windows --
    # see _A_HYDROPHOBIC_SEGMENT_THAT_IS_NOT_IN_THE_SAMPLE_IS_A_DECOY_WINDOW.
    'ANXA11': ('P50995.csv', '505-residue canonical P50995'),
    # Added 17 Nov 2026. SCORED ON THE A4 ACIDIC CHAIN, NOT THE PRECURSOR, and the row's
    # A_SIGNAL_PEPTIDE_IN_THE_SCORED_FRAME_BIASES_THE_STATISTIC key pre-registered that
    # decision BEFORE this run. P02858's 563-residue precursor is a signal peptide plus
    # three chains; scoring it would put 23 residues of almost unbroken hydrophobicity
    # into the window pool as a decoy. See OFFSET below -- this row and only this row
    # stores its residues in a frame that is NOT the frame of its profile.
    'glycinin G4 (soybean)': ('../glycinin_2026-11-17/P02858_A4.csv',
                              'A4 acidic chain, P02858[121:378], 258 aa'),
    # Added 18 Nov 2026, the three rows recruited under the eight-stage pipeline in
    # reports/recruitment_tracker.md. THE ORDER THESE ARRIVED IN IS THE POINT: the legacy
    # arm ran first, the stratum labels were committed (5048837) and pushed, and only then
    # was the modern arm pointed at these accessions. Their canonical frames carry no
    # signal peptide and no transmembrane segment, so no decoy windows enter the pool --
    # see _A_HYDROPHOBIC_SEGMENT_THAT_IS_NOT_IN_THE_SAMPLE_IS_A_DECOY_WINDOW.
    'TAF15': ('../recruited_2026-11-18/Q92804.csv', '592-residue canonical Q92804'),
    'CHCHD10': ('../recruited_2026-11-18/Q8WYQ3.csv', '142-residue canonical Q8WYQ3'),
    # 151, NOT 142: 142 is the length of the paralogue CHCHD10 and an easy slip to make
    # when the two are tabulated side by side. Verified against the fetched sequence.
    'CHCHD2': ('../recruited_2026-11-18/Q9Y6H1.csv', '151-residue canonical Q9Y6H1'),
}

# ROW NUMBERING MINUS PROFILE NUMBERING. Zero for every row whose `residues` are in the
# same frame as its profile, which is every row but one. For glycinin the row stores the
# paper's and the PDB's precursor numbering (164-190) while the profile is the A4 chain,
# so local = precursor - 120. THIS IS DECLARED RATHER THAN APPLIED SILENTLY because an
# unannounced offset is exactly the frame trap this project has been bitten by four times;
# the conversion is asserted against the stored sequence at load time, below.
OFFSET = {
    'glycinin G4 (soybean)': 120,
}


def load(path):
    out, seq = [], []
    with open(os.path.join(RUNDIR, path)) as fh:
        for r in csv.DictReader(l for l in fh if not l.startswith('#')):
            out.append(float(r['aggrescanai_score']))
            for k in ('aa', 'residue', 'aminoacid'):
                if k in r:
                    seq.append(r[k])
                    break
    return out, ''.join(seq)


def statistic(scores, a, b, phase=0):
    """a,b inclusive 1-based region bounds. NON-OVERLAPPING tiling, offset `phase`.

    WHY TILING AND NOT A SLIDING WINDOW. 3.1 states both a procedure and the property
    it must have: "v ~ Uniform(0, 1)" under H0. Sliding windows overlap by 5 of 6
    residues, so they are NOT exchangeable, and simulation on i.i.d. scores gives
    mean v = 0.663, median 0.767 -- biased toward "the predictor failed". Tiling gives
    mean 0.495 and quantiles within 0.006 of uniform. The document's own stated null
    therefore selects tiling. The criterion is the pre-registration's, not the analyst's.
    """
    wins, starts = [], []
    for i in range(phase, len(scores) - W + 1, W):
        wins.append(sum(scores[i:i + W]) / W)
        starts.append(i + 1)               # 1-based start
    M = len(wins)
    idx = [j for j in range(M) if starts[j] >= a and starts[j] + W - 1 <= b]
    m = len(idx)

    if m == 0:
        # PREREGISTRATION 3.1a, AMENDMENT 17 Nov 2026, POST-UNBLINDING => EXPLORATORY.
        # No window fits wholly inside the region, so the region is scored as ONE window
        # of its own length against all same-length windows. m=1, v = 1-P. Uniform under
        # H0 by exchangeability of a single rank; overlap is irrelevant at m=1.
        # Applies ONLY here, never where the registered statistic is defined.
        L = b - a + 1
        if L < 1 or L > len(scores):
            return None
        sw = [sum(scores[i:i + L]) / L for i in range(len(scores) - L + 1)]
        mine = sw[a - 1]
        less = sum(1 for x in sw if x < mine)
        eq = sum(1 for x in sw if x == mine)
        P = (less + 0.5 * eq) / len(sw)
        return {'M': len(sw), 'm': 1, 'best_window_score': mine, 'P': P,
                'v': 1.0 - P, 'rule': '3.1a EXPLORATORY'}
    if m == 0:
        return None
    best = max(wins[i] for i in idx)
    less = sum(1 for x in wins if x < best)
    eq = sum(1 for x in wins if x == best)
    P = (less + 0.5 * eq) / M          # midrank
    v = 1.0 - P ** m
    return {'M': M, 'm': m, 'best_window_score': best, 'P': P, 'v': v}


def norm_isf(p):
    """One-sided z for upper-tail probability p, via inverse erf."""
    # z = sqrt(2) * erfinv(1 - 2p)
    x = 1.0 - 2.0 * p
    # Acklam-free: use math.erf inversion by bisection (exact enough, cheap)
    lo, hi = -40.0, 40.0
    for _ in range(300):
        mid = (lo + hi) / 2
        if math.erf(mid / math.sqrt(2)) < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def chi2_sf(x, k):
    """Upper tail of chi-square with k df (k even here: k=2n)."""
    if k % 2 == 0:
        m = k // 2
        t = math.exp(-x / 2)
        s = t
        for i in range(1, m):
            t *= (x / 2) / i
            s += t
        return min(1.0, max(0.0, s))
    raise ValueError('even df only')


def main(repo):
    d = json.loads(open(os.path.join(repo, 'data', 'regions.json')).read())
    cache = {}
    results = []
    skipped = []
    for r in d['regions']:
        prot = r['protein']
        res = r['residues']
        if prot not in RUNS:
            # NOT necessarily a frame problem. Corrected 17 Nov 2026: this message used to
            # claim the frame was unresolved, which was false for glycinin G4 -- that row's
            # frame is resolved and verified, there is simply no predictor profile for the
            # protein yet. A skip reason that names the wrong cause sends the next reader
            # to fix something that is not broken.
            skipped.append((prot, res, 'NO PREDICTOR RUN for this protein (see the row for whether a frame is also needed)'))
            continue
        if not re.fullmatch(r'\d+-\d+', res.strip()):
            skipped.append((prot, res, 'composite/irregular range -- not a single interval'))
            continue
        if r.get('exclude_from_scoring'):
            # Added 17 Nov 2026. A row can be excluded for reasons the statistic cannot see --
            # e.g. a range that turns out to be a typo in the source. This check exists because
            # TRIOBP-1 324-328 carried a PROSE note saying "DO NOT score this row" and was scored
            # anyway, by this very script. A warning in prose is not a constraint.
            skipped.append((prot, res, 'exclude_from_scoring: ' + r.get('exclude_from_scoring_reason', '')[:70]))
            continue
        if not r.get('frame') or r['frame'] == 'ABSENT':
            skipped.append((prot, res, 'row carries NO frame; descriptor rule: do not assume'))
            continue
        path, frame = RUNS[prot]
        if path not in cache:
            cache[path] = load(path)
        sc, profseq = cache[path]
        a, b = (int(x) for x in res.split('-'))
        off = OFFSET.get(prot, 0)
        if off:
            # THE OFFSET IS VERIFIED AGAINST THE ROW'S OWN STORED SEQUENCE, EVERY RUN.
            # A frame conversion that is merely commented is a frame conversion that will
            # one day be wrong. If the profile's residues at the converted indices are not
            # the residues the row says are there, the row is NOT scored.
            a, b = a - off, b - off
            want = (r.get('sequence') or '').strip().upper()
            have = profseq[a - 1:b].upper()
            if not profseq:
                skipped.append((prot, res, f'OFFSET {off} declared but profile carries no '
                                           'residue column to verify it against'))
                continue
            if want and have != want:
                skipped.append((prot, res, f'OFFSET {off} FAILED VERIFICATION: profile has '
                                           f'{have[:14]}... row says {want[:14]}...'))
                continue
        if b > len(sc):
            skipped.append((prot, res, f'range exceeds sequence length {len(sc)}'))
            continue
        st = statistic(sc, a, b, phase=0)
        if st is None:
            skipped.append((prot, res, f'region shorter than the {W}-residue window'))
            continue
        # Phase is a free parameter the pre-registration does not fix. Report the
        # spread across all 6 offsets so a conclusion that depends on it is visible.
        alt = [statistic(sc, a, b, phase=p) for p in range(W)]
        vs = [x['v'] for x in alt if x]
        st['v_phase_min'], st['v_phase_max'] = min(vs), max(vs)
        sa = r.get('stratum_assignment') or {}
        st.update(protein=prot, residues=res, stratum=r['stratum'],
                  cpad=r['cpad_status'], circ=r['circularity_status'], frame=frame,
                  # A STRATUM LABEL ALONE DOES NOT ADMIT A ROW TO THE CONFIRMATORY SET.
                  # Added 18 Nov 2026: rows relabelled from PENDING by the mechanical
                  # PREREGISTRATION 7 rule carry confirmatory_eligible: false, because the
                  # ordering §7 calls part of the freeze was broken -- the modern arm had
                  # already run on them. The flag defaults to True so every other row is
                  # unaffected, and it is read HERE rather than trusted to a reader.
                  conf_ok=sa.get('confirmatory_eligible', True))
        results.append(st)

    # MINIMUM ATTAINABLE v, ADDED 18 Nov 2026, AND IT IS NOT A COSMETIC COLUMN.
    # P is a midrank over M tiled windows, so its largest possible value is (M-0.5)/M --
    # attained when the region contains the single highest-scoring window in the chain.
    # Hence v = 1 - P^m can never fall below 1 - ((M-0.5)/M)^m, WHATEVER THE PREDICTOR
    # OUTPUTS. When that floor exceeds §4's recovery bar of 0.05 the row CANNOT be scored
    # as recovered even by a perfect predictor, and a 200k-draw simulation of the null at
    # that geometry gives P(v < 0.05) = 0.0000 exactly. The floor depends only on M and m
    # -- chain length and region length -- so it was computable before any predictor ran.
    for x in results:
        x['v_floor'] = 1.0 - ((x['M'] - 0.5) / x['M']) ** x['m']
    results.sort(key=lambda x: x['v'])
    print(f'{"protein":18s} {"region":12s} {"stratum":22s} {"cpad":30s} {"m":>4s} {"M":>5s} '
          f'{"P":>8s} {"v":>10s} {"min v":>8s}')
    print('-' * 140)
    for x in results:
        flag = '  <-- v<0.05 UNREACHABLE' if x['v_floor'] >= BAR else ''
        print(f'{x["protein"]:18s} {x["residues"]:12s} {x["stratum"]:22s} {x["cpad"]:30s} '
              f'{x["m"]:4d} {x["M"]:5d} {x["P"]:8.5f} {x["v"]:10.6f} {x["v_floor"]:8.5f}'
              f'  [{x["v_phase_min"]:.3f}-{x["v_phase_max"]:.3f}]{flag}')
    print()
    unreach = [x for x in results if x['v_floor'] >= BAR]
    if unreach:
        print(f'*** {len(unreach)} of {len(results)} SCORED ROWS CANNOT REACH §4\'s RECOVERY BAR '
              f'(v < {BAR}) ***')
        print('    v = 1 - P^m and P <= (M-0.5)/M, so min v = 1 - ((M-0.5)/M)^m. For these')
        print('    rows that floor is ABOVE the bar: a perfect predictor -- one that puts the')
        print('    highest-scoring window in the chain inside the region -- still fails. The')
        print('    floor is a function of M and m alone and was computable before any')
        print('    predictor ran. This is a defect in §4, like the 2^-n Wilcoxon floor.')
        for x in sorted(unreach, key=lambda z: -z['v_floor']):
            print(f'      {x["protein"]:18s} {x["residues"]:12s} M={x["M"]:4d} m={x["m"]:3d} '
                  f'min v = {x["v_floor"]:.5f}')
        print()
    if skipped:
        print('NOT SCORED:')
        for p, res, why in skipped:
            print(f'  {p:18s} {res:18s} {why}')
        print()

    def combine(rows, label):
        if not rows:
            print(f'{label}: no rows'); return
        n = len(rows)
        vs = [min(max(x['v'], 1e-16), 1 - 1e-16) for x in rows]
        zs = [norm_isf(v) for v in vs]           # small v -> large positive z
        Z = sum(zs) / math.sqrt(n)
        pZ = 0.5 * math.erfc(Z / math.sqrt(2))
        chi = -2 * sum(math.log(v) for v in vs)
        pF = chi2_sf(chi, 2 * n)
        print(f'{label}  (n={n})')
        print(f'    rows        : ' + ', '.join(f'{x["protein"]} {x["residues"]}' for x in rows))
        print(f'    Stouffer Z  = {Z:+.4f}   one-sided p = {pZ:.4f}   [PRIMARY]')
        print(f'    Fisher chi2 = {chi:.4f} on {2*n} df   p = {pF:.4f}   [secondary]')
        print()

    def eligible(x):
        return (x['stratum'].startswith('DISCORDANT')
                and x['cpad'] == 'CPAD_ABSENT_ORTHOLOGY_CHECKED'
                and x['circ'] == 'CLEAN')

    conf = [x for x in results if eligible(x) and x['conf_ok']]
    held = [x for x in results if eligible(x) and not x['conf_ok']]

    print('=' * 125)
    combine(conf, 'CONFIRMATORY (5.2b item 5: discordant, CPAD-absent, circularity CLEAN)')

    if held:
        print(f'HELD OUT OF THE CONFIRMATORY SET ({len(held)} rows) — they meet every stratum')
        print('criterion but carry confirmatory_eligible: false. Their stratum was assigned')
        print('from the legacy arm on 18 Nov 2026, AFTER the modern arm had already run on')
        print('them, breaching the ordering PREREGISTRATION 7 calls part of the freeze.')
        for x in held:
            print(f'    {x["protein"]} {x["residues"]}')
        print()
        combine(conf + held,
                'EXPLORATORY (§12): the confirmatory set PLUS the held-out rows. '
                'NOT A CONFIRMATORY RESULT')
        prots = sorted({x['protein'] for x in conf + held})
        print(f'    AND THE UNIT IS WRONG: {len(conf + held)} rows but only {len(prots)} '
              f'proteins — {", ".join(prots)}.')
        print(f'    Stouffer and Wilcoxon both assume independent pairs; overlapping')
        print(f'    intervals of one protein on one profile are not independent. Treat the')
        print(f'    honest n as {len(prots)}, where the minimum attainable one-sided')
        print(f'    Wilcoxon p is {2**-len(prots):.4f} against the 0.05 of §4.')
        print()

    stuck = [x for x in results if x['stratum'] == 'PENDING']
    if stuck:
        print(f'STILL PENDING ({len(stuck)} rows) — scored by the modern arm with NO stratum.')
        print('Under §7 the stratum comes from the legacy arm, so each of these needs a')
        print('legacy run, and the label must be COMMITTED BEFORE the modern arm is run on')
        print('it. For these rows that ordering is already lost; for new rows it is not.')
        for x in stuck:
            print(f'    {x["protein"]} {x["residues"]}')
        print()
    combine([x for x in results if x['cpad'] == 'CPAD_MEMBER'],
            'CPAD-CONTAMINATED ROWS (reported separately, EXCLUDED from the primary)')
    combine([x for x in results if x['circ'] == 'CLEAN'
             and x['cpad'] == 'CPAD_ABSENT_ORTHOLOGY_CHECKED'],
            'ALL CPAD-ABSENT, CIRCULARITY-CLEAN ROWS (exploratory: mixes strata)')


if __name__ == '__main__':
    main(sys.argv[1])
