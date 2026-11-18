#!/usr/bin/env python3
"""Is v ~ Uniform(0,1) under H0 at the geometries this dataset actually contains?

PREREGISTRATION 3.1 states the null the statistic must satisfy: "v ~ Uniform(0, 1)".
That property was checked when tiling was chosen over sliding windows, but it was checked
in the abstract. This script checks it at each row's OWN (M, m), because the statistic is
discrete and the discreteness is not uniform across rows.

    python3 -I scripts/v_floor_simulation.py [draws]

It reads nothing and depends on no predictor output: M and m are chain length and region
length in windows, fixed by the dataset alone. Every number here was therefore computable
BEFORE any predictor ran, which is why reporting it after the fact is not a post-hoc
choice -- it is arithmetic that should have been done first.
"""
import random
import statistics
import sys

BAR = 0.05
SEED = 20261118

# (label, M, m) for every scored row, from scripts/score_rows.py on 18 Nov 2026.
GEOM = [
    ('TMEM106B 120-254', 45, 22), ('serum amyloid A 2-55', 17, 8),
    ('CHCHD10 42-75', 23, 5), ('CHCHD2 54-86', 25, 5),
    ('TRIOBP-1 60-189', 108, 21), ('DISC1 691-836', 142, 24),
    ('TAF15 7-99', 98, 15), ('LECT2 55-75', 22, 3),
    ('hnRNPA1 251-295', 53, 7), ('FUS 39-95', 87, 8),
    ('TRIOBP-1 1-59', 108, 9), ('glycinin 164-190', 43, 3),
    ('ANXA11 39-74', 84, 5), ('alpha-synuclein 71-82', 23, 1),
    ('TRIOBP-1 324-348', 108, 4), ('DISC1 384-415', 142, 5),
    ('DISC1 748-769', 142, 3), ('tau 306-311', 436, 1),
]


def floor(M, m):
    """The smallest v any predictor can produce at this geometry."""
    return 1.0 - ((M - 0.5) / M) ** m


def simulate(M, m, draws):
    """v under H0: window scores i.i.d. continuous, region position irrelevant."""
    out = []
    for _ in range(draws):
        w = [random.random() for _ in range(M)]
        best = max(random.sample(w, m))
        less = sum(1 for x in w if x < best)
        out.append(1.0 - ((less + 0.5) / M) ** m)
    return out


def main(draws=200000):
    random.seed(SEED)
    print('PREREGISTRATION 3.1 states the null: v ~ Uniform(0, 1).')
    print('Under that null, mean = 0.500, median = 0.500, P(v < %.2f) = %.3f.\n' % (BAR, BAR))
    print('%-24s %5s %4s %9s %8s %8s %12s' %
          ('row geometry', 'M', 'm', 'min v', 'mean', 'median', 'P(v<0.05)'))
    print('-' * 78)
    broken = []
    for lab, M, m in sorted(GEOM, key=lambda g: -floor(g[1], g[2])):
        vs = simulate(M, m, draws)
        pw = sum(1 for x in vs if x < BAR) / len(vs)
        f = floor(M, m)
        mark = '   <-- NO POWER' if f >= BAR else ''
        print('%-24s %5d %4d %9.5f %8.4f %8.4f %12.4f%s' %
              (lab, M, m, f, statistics.mean(vs), statistics.median(vs), pw, mark))
        if f >= BAR:
            broken.append(lab)
    print('-' * 78)
    print('\n%d of %d geometries have P(v < %.2f) = 0 EXACTLY under the null.' %
          (len(broken), len(GEOM), BAR))
    print('For those rows §4\'s recovery criterion has no power: it cannot fire, so it')
    print('cannot distinguish a predictor that works from one that does not. A row that')
    print('can only ever return "not recovered" contributes a foregone conclusion to any')
    print('statistic built on that criterion, in the direction of the project\'s own H1.')
    print('\nAND THE REST OF THE TABLE IS WORSE THAN "CONSERVATIVE", WHICH IS WHAT A FIRST')
    print('READING OF IT SUGGESTS. The rows that CAN fire do not fire at 0.05 either, and')
    print('they miss in BOTH directions: FUS 39-95 reads 0.091 and TRIOBP-1 1-59 reads')
    print('0.084 -- nearly TWICE the nominal level -- while DISC1 384-415 reads 0.035 and')
    print('TRIOBP-1 324-348 reads 0.037. So a criterion with a nominal 5% false-positive')
    print('rate actually runs anywhere from 0% to 9% across this dataset, decided by chain')
    print('length and region length alone. Rows are NOT being judged on a common scale.')
    print('\nThe mean is also not 0.5 where m is large (TMEM106B 0.442, SAA 0.449), so v is')
    print('not uniform in the bulk at those geometries either -- the departure is not')
    print('confined to the lower tail. §3.1 asserted v ~ Uniform(0,1); that holds where m')
    print('is small relative to M and fails where it is not.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 200000))
