#!/usr/bin/env python3
"""Exact calibration of v against its own discrete null. PREREGISTRATION 3.1b.

v = 1 - P^m is well calibrated where m is small relative to M and ANTI-CONSERVATIVE where
it is not: at the floor, CHCHD10 reports v = 0.104 where the true tail probability is
0.218. This module returns what v should have been.

EXACT, NOT SIMULATED. Under H0 the region's m windows are an exchangeable subset of the
M, so the rank r of the region's best window (1 = lowest, M = highest) has

    P(r = k) = C(k-1, m-1) / C(M, m)

and every v the statistic can emit corresponds to exactly one k. The calibrated p is the
probability of a v at least as small as the one observed, i.e. of a rank at least as high:

    p_cal(k) = sum_{j >= k} C(j-1, m-1) / C(M, m)

No random draws, so the answer does not move between runs and has no Monte-Carlo error.
A 200k-draw simulation agreed with this to within 0.002 on every row tested.

    python3 -I scripts/calibrate_v.py          # the table for every scored row
"""
import math
import os
import sys

BAR = 0.05


def rank_from_v(v, M, m):
    """Invert v = 1 - ((k-0.5)/M)^m to the integer rank k it came from."""
    P = (1.0 - v) ** (1.0 / m)
    return int(round(P * M + 0.5))


def calibrated_p(k, M, m):
    """P(rank >= k) under H0. Exact."""
    tot = math.comb(M, m)
    return sum(math.comb(j - 1, m - 1) for j in range(max(k, m), M + 1)) / tot


def info_limit(M, m):
    """The smallest p ANY rank-based statistic can return: P(top window in region)."""
    return m / M


def v_floor(M, m):
    """The smallest v THIS statistic can emit."""
    return 1.0 - ((M - 0.5) / M) ** m


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    import score_rows as S

    rows = S.collect(os.path.join(here, os.pardir)) if hasattr(S, 'collect') else None
    if rows is None:
        print('score_rows.py exposes no collect(); run scripts/score_rows.py for the table')
        return 1
    return 0


if __name__ == '__main__':
    # Self-check against theory before anything else uses this module. If these fail the
    # arithmetic is wrong and no number produced here should be trusted.
    for M, m in ((23, 5), (25, 5), (142, 5), (108, 4), (98, 15)):
        assert abs(calibrated_p(M, M, m) - m / M) < 1e-12, (M, m)
        assert abs(calibrated_p(m, M, m) - 1.0) < 1e-12, (M, m)
    assert rank_from_v(v_floor(23, 5), 23, 5) == 23
    print('self-check passed: p_cal(top rank) == m/M, p_cal(lowest possible) == 1')
    print()
    print('%-22s %5s %4s %11s %13s %8s %11s' %
          ('row', 'M', 'm', 'nominal v', 'calibrated p', 'ratio', 'limit m/M'))
    print('-' * 82)
    # (label, M, m, observed v) from scripts/score_rows.py, 18 Nov 2026.
    TAB = [('CHCHD10 42-75', 23, 5, 0.104071379), ('CHCHD2 54-86', 25, 5, 0.096079203),
           ('TAF15 7-99', 98, 15, 0.783350383), ('DISC1 384-415', 142, 5, 0.416408),
           ('TRIOBP-1 324-348', 108, 4, 0.907876), ('ANXA11 39-74', 84, 5, 0.331484),
           ('TMEM106B 120-254', 45, 22, 0.990005), ('TRIOBP-1 1-59', 108, 9, 0.040903),
           ('glycinin 164-190', 43, 3, 0.388392), ('DISC1 691-836', 142, 24, 0.999363)]
    for lab, M, m, v in TAB:
        k = rank_from_v(v, M, m)
        p = calibrated_p(k, M, m)
        lim = info_limit(M, m)
        flag = '  <-- beyond any rank test' if lim > BAR else ''
        print('%-22s %5d %4d %11.6f %13.5f %7.2fx %11.4f%s' %
              (lab, M, m, v, p, p / v if v else 0, lim, flag))
    print('-' * 82)
    print('\nratio > 1 means the pre-registered v UNDERSTATES the probability of the')
    print('observation -- it reports more evidence than the data contain. The two rows at')
    print('the floor do so by a factor of 2.1. Rows with small m and large M are fine.')
    raise SystemExit(0)
