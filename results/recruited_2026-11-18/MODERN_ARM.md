# The modern arm on the three recruited rows — and a defect in §3.1 that outranks it

**18 November 2026.** AggrescanAI run on Q92804, Q8WYQ3 and Q9Y6H1 **after** their stratum
labels were committed and pushed (`5048837`), completing the eight-stage pipeline for the
first time.

---

## Headline

> **The confirmatory set reaches n = 5 and returns a null: Stouffer Z = +0.2963,
> one-sided p = 0.3835.**
>
> **But three of those five rows cannot pass §4's recovery bar at all**, and a null
> simulation at their own geometry gives P(*v* < 0.05) = **0.0000 exactly**. The bar has
> *no power* on them. That is a defect in the pre-registered statistic, it was computable
> before any predictor ran, and it matters more than the p-value above.

## The three new rows, both arms

| row | legacy *v* | modern *v* | Δ*v* | floor (min attainable *v*) |
|---|---|---|---|---|
| TAF15 7–99 | 0.9999915 | **0.78335** | **−0.2166** | 0.07386 |
| CHCHD10 42–75 | 0.1040714 | **0.1040714** | **0.0000000** | 0.10407 |
| CHCHD2 54–86 | 0.0960792 | **0.0960792** | **0.0000000** | 0.09608 |

**The two CHCHD rows are bit-identical between the arms.** Not approximately: the
difference is 1.4 × 10⁻¹¹ and 6.9 × 10⁻¹⁷, i.e. floating-point noise on an exact tie. Both
predictors place the single highest-scoring window of the chain inside the region, so
*P* = (*M*−0.5)/*M* for both, and *v* is then fixed by *M* and *m* alone — **the scores
drop out of the statistic entirely.**

That also confirms, on the second arm, the prediction made from 84.8% sequence identity
before either arm ran.

## The defect

*v* = 1 − *P*^*m*, and *P* is a midrank over *M* tiled windows, so *P* ≤ (*M*−0.5)/*M*.
Therefore

> **min *v* = 1 − ((*M*−0.5)/*M*)^*m***

attained by a *perfect* predictor — one that ranks the region's best window top of the
whole chain. When that floor exceeds 0.05, **§4's recovery criterion cannot fire.**

**Nine of twenty-three scored rows are in that state**, including all three recruited
today:

| row | *M* | *m* | min *v* |
|---|---|---|---|
| TMEM106B 120–254 | 45 | 22 | 0.21793 |
| serum amyloid A 2–55 | 17 | 8 | 0.21245 |
| **CHCHD10 42–75** | 23 | 5 | 0.10407 |
| **CHCHD2 54–86** | 25 | 5 | 0.09608 |
| TRIOBP-1 60–189 | 108 | 21 | 0.09285 |
| DISC1 691–836 | 142 | 24 | 0.08117 |
| **TAF15 7–99** | 98 | 15 | 0.07386 |
| LECT2 55–75 | 22 | 3 | 0.06664 |
| hnRNPA1 251–295 | 53 | 7 | 0.06420 |

`scripts/score_rows.py` now prints this column and flags these rows on every run, so the
defect cannot go quiet again.

## It is worse than a floor: the bar is miscalibrated in both directions

`scripts/v_floor_simulation.py`, 100 000 draws per geometry, i.i.d. continuous window
scores — **no predictor output is read, and nothing in it depends on any score.**

| row geometry | *M* | *m* | P(*v* < 0.05) under H0 |
|---|---|---|---|
| CHCHD10, CHCHD2, TAF15, TMEM106B, SAA, LECT2, hnRNPA1, DISC1 691–836, TRIOBP-1 60–189 | — | — | **0.0000** |
| FUS 39–95 | 87 | 8 | **0.0913** |
| TRIOBP-1 1–59 | 108 | 9 | **0.0838** |
| glycinin 164–190 | 43 | 3 | 0.0708 |
| ANXA11 39–74 | 84 | 5 | 0.0605 |
| alpha-synuclein 71–82 | 23 | 1 | 0.0446 |
| DISC1 748–769 | 142 | 3 | 0.0423 |
| TRIOBP-1 324–348 | 108 | 4 | 0.0370 |
| DISC1 384–415 | 142 | 5 | 0.0345 |
| tau 306–311 | 436 | 1 | 0.0497 |

**A criterion with a nominal 5% false-positive rate actually runs between 0% and 9.1%
across this dataset, decided by chain length and region length alone.** Rows are not being
judged on a common scale. The mean of *v* also departs from 0.5 where *m* is large
(TMEM106B 0.442, SAA 0.449), so §3.1's "*v* ~ Uniform(0, 1)" **holds where *m* is small
relative to *M* and fails where it is not.**

## What this does and does not invalidate

**Does not invalidate the Stouffer confirmatory statistic**, which uses *v* directly rather
than the 0.05 bar, and whose inputs are near-uniform in the bulk for the two original
confirmatory rows. **n = 5, Z = +0.2963, p = 0.3835** stands as computed — a null result,
with the sign moved from Z = −0.7896 at n = 2.

**Does invalidate any row-level statement of the form "the predictor failed to recover
this region at v < 0.05"** for the nine rows above. For them that sentence is true by
arithmetic before any predictor runs, and it points in the direction of the project's own
H1. Any such claim already in the record needs re-reading against this table.

**§4's contrast is now unreachable for a third independent reason.** The first was the
2⁻ⁿ Wilcoxon floor at small *n*. The second was the CHCHD pair's 84.8% identity. The
third: on the confirmatory five, two paired differences are **exact ties**, which Wilcoxon
drops, leaving n = 3 and a floor of 0.125.

## The honest position

The recruitment did what it was meant to do — the confirmatory set went from 2 rows to 5,
under an intact ordering, which no previous row in this project can claim. But **the rows
it added are the ones the registered statistic handles worst**, because short proteins and
long ordered cores are exactly the geometry that drives *m*/*M* up. CHCHD10 is a
142-residue protein with a 34-residue core; that is 5 windows out of 23.

**This is rule 2 of `CLAUDE.md` arriving one step late.** The margin was checked against
the error bar *after* the compute rather than before — though the compute was ten seconds
per protein, and the check needed only *M* and *m*, which the dataset fixed days ago.

## Reproduce

```
AGGAI_HOME=<dir with protT5/ and aggai/> python3 scripts/run_aggrescanai.py \
    results/recruited_2026-11-18/Q92804.csv Q92804 <sequence>      # and Q8WYQ3, Q9Y6H1
python3 -I scripts/score_rows.py .
python3 -I scripts/v_floor_simulation.py 100000
```

ProtT5 revision `94a6abc029ae13029317b140b7424e012bf8dfbf`, AggrescanAI weights revision
`7aba68e65d620aa55b10f9550005efff3f3240e7`, both pinned and checksummed by the runner.
Ensemble spread is recorded per run: 0.893, 0.899 and 0.867 maximum across the five CV
models — **large**, and a standing caveat on every AggrescanAI number in this project.

---

## Addendum, same day: the floor is the smaller of two problems

### *v* is anti-conservative at the floor, by a factor of two

The floor is not merely unreachable — where it *is* attained, the number reported is
wrong in the dangerous direction. Calibrating each row's *v* against its own null
(200 000 draws):

| row | *M* | *m* | nominal *v* | **calibrated p** | ratio |
|---|---|---|---|---|---|
| CHCHD10 42–75 | 23 | 5 | 0.104071 | **0.21816** | **2.10×** |
| CHCHD2 54–86 | 25 | 5 | 0.096079 | **0.20022** | **2.08×** |
| TAF15 7–99 | 98 | 15 | 0.783350 | 0.82718 | 1.06× |
| ANXA11 39–74 | 84 | 5 | 0.331484 | 0.35828 | 1.08× |
| TRIOBP-1 324–348 | 108 | 4 | 0.907876 | 0.91533 | 1.01× |
| DISC1 384–415 | 142 | 5 | 0.416408 | 0.41107 | 0.99× |

The two floor-attaining rows report a *v* that **understates the probability of the
observation by a factor of 2.1**. The calibrated values match theory exactly:
0.218 ≈ 5/23 and 0.200 = 5/25.

**Away from the floor — large *M*, small *m* — *v* is well calibrated** (0.99–1.08×). The
defect is specific to small *M* with large *m*, and the two founding confirmatory rows are
not affected.

### The information limit, which no amendment can repair

Under H0 the chain's top-ranked window falls inside the region with probability **exactly
*m*/*M***. So **no rank-based statistic — not this one, not a repaired one — can return a
p below *m*/*M*.**

**Only 7 of 20 rows have *m*/*M* ≤ 0.05.** The other thirteen are beyond rescue by any
amendment to §3.1: the region is simply too large a fraction of its own protein for its
ranking to be surprising.

| passes *m*/*M* ≤ 0.05 | *m*/*M* |
|---|---|
| TRIOBP-1 333–340 | 0.0016 |
| tau 306–311, tau 275–280 | 0.0023 |
| DISC1 748–769 | 0.0211 |
| **DISC1 384–415** | **0.0352** |
| **TRIOBP-1 324–348** | **0.0370** |
| alpha-synuclein 71–82 | 0.0435 |

**Both founding confirmatory rows pass, narrowly.** The project's own question remains
answerable. It is the recruited rows — and most of the widening done on 17 Nov — that are
not.

**This is the criterion that should govern recruitment**, and it costs nothing to apply:
*m*/*M* needs only the chain length and the region length, both of which a candidate row
carries before any paper is read in full. **Applied on 18 Nov it would have rejected all
three of today's recruits at stage 1.**
