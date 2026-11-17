# The legacy-versus-modern contrast — computed, and it runs the wrong way

**17 November 2026. Post-freeze.** The §4 contrast is a registered criterion; the row set
used to evaluate it is wider than the confirmatory set, so **the n = 7 analysis is
exploratory** under §12. The n = 2 confirmatory statement is registered but, as shown
below, **unreachable by construction**.

---

## Headline

> **Modern does not beat legacy. On 6 of 7 rows it is worse.**
>
> §4 requires, for "modern beats legacy": Wilcoxon one-sided **p < 0.05** *and* median
> paired **Δv < −0.10**. Observed: **p = 0.148**, median **Δv = +0.137**. Both criteria
> fail, and the effect-size criterion fails **by sign** — the paired difference points the
> opposite way from the one the pre-registration was written to detect.

**ROW SET CORRECTED 17 Nov 2026, same day.** TRIOBP-1 324-328 was **removed** — its range is a
typo in a figure legend (see `exclude_from_scoring` on that row), and the dataset had
said in prose not to score it while this script scored it anyway. TMEM106B 120-254 was
**added**. n is 7 either way, and **the conclusion is unchanged**: 6/7, p = 0.1484 before
and after. The median Δv moves from +0.137 to +0.274.

| row | stratum | TANGO *v* | AggrescanAI *v* | Δv (modern − legacy) |
|---|---|---|---|---|
| TRIOBP-1 1-59 | PENDING | 0.9995 | **0.0409** | **−0.959** |
| DISC1 748-769 | PENDING | 0.9227 | 0.9955 | +0.073 |
| **DISC1 384-415** | **DISCORDANT** | 0.3189 | 0.4164 | +0.098 |
| TMEM106B 120-254 | PENDING | 0.7156 | 0.9900 | +0.274 |
| TRIOBP-1 333-340 | PENDING | 0.0388 | 0.4240 | +0.385 |
| **TRIOBP-1 324-348** | **DISCORDANT** | 0.1235 | 0.9079 | +0.784 |
| DISC1 691-836 | PENDING | 0.0812 | 0.9994 | +0.918 |

Negative Δv favours modern. One row does: **TRIOBP-1 1-59**, which AggrescanAI recovers
(v = 0.041) and TANGO misses completely (v = 0.9995). It is `PENDING` and is not the
mapped region the project asks about.

## Three premises that had to be audited before anything could be computed

**1. The published legacy runs cannot supply a *v*.** §5.1a takes the legacy arm from
published runs, but those report thresholded calls and consensus rules — Bradshaw 2014's
*"at least 3 of these 6 methods"*, *"threshold = 5%"* — not per-window score profiles.
§4's Δv needs a *v* on both sides. **Not commensurable**, so the contrast could only be
computed by running a legacy tool ourselves.

**2. TANGO's pH, temperature and ionic strength were never pre-registered** — grep
`PREREGISTRATION.md` and they are absent — and `predictor_provenance.json` records, from
16 Nov, that **pH and temperature change the answer** (aggregation at one test residue
moved 4.73 → 12.37 between pH 7.4 and 2.0). Choosing values now would be a post-freeze,
post-unblinding choice on a parameter known to move the result.

**So they were not chosen. A 9-point grid was run instead** — pH {5.0, 7.0, 7.4} ×
T {298, 303, 310} K, ionic 0.05, nt=N ct=N tf=0 stab=−10:

| | median Δv | modern worse | Wilcoxon p |
|---|---|---|---|
| all 9 grid points | +0.124 … +0.179 | **6/7 at every point** | **0.148 at every point** |

The unregistered parameters **do not touch the conclusion**. An unregistered free
parameter became a measured sensitivity instead of a hidden choice.

**3. At n = 2 the registered test cannot reach its own threshold.** The exact one-sided
Wilcoxon signed-rank minimum for *n* pairs is 2⁻ⁿ:

| n | 1 | 2 | 3 | 4 | **5** | 6 | 7 |
|---|---|---|---|---|---|---|---|
| min attainable p | 0.50 | **0.25** | 0.125 | 0.0625 | **0.031** | 0.016 | 0.008 |

**The confirmatory set is n = 2, so the smallest p obtainable is 0.25.** No data could
have made §4's contrast significant on the confirmatory set. This was knowable without
running anything, and it is a defect in §4, not in the data: **§4 set a threshold the
design it sits in cannot reach.**

## The legacy arm narrows to one tool, exactly as the modern arm did

§5.1 freezes TANGO, AGGRESCAN, FoldAmyloid and ProA. Today: **ProA is dead**,
**AGGRESCAN is web-only** and fails the version-pinnable rule, and the **FoldAmyloid
reimplementation has not passed its registered validation**. Only **TANGO** is local and
checksum-pinned.

So the contrast is **one against one** — TANGO versus AggrescanAI — and the claim narrows
with it, in the same way and for the same reason §5.2b narrowed the modern arm. **It is
not a statement about generations.**

## Our TANGO run corroborates Bradshaw 2014 independently

TANGO gives TRIOBP-1 324-348 **v = 0.1235**, i.e. its best tile at roughly the **97th
percentile** with about **3–4 tiles scoring higher**.

Bradshaw 2014 reported, of the same region and the same tool: *"at least four sites
elsewhere in the protein were more strongly predicted."*

**An independent run, on a pinned binary, with parameters the 2014 paper never stated,
reproduces that rank statement.** And it agrees on the verdict: v = 0.12 is above the
registered v < 0.05 bar, so **TANGO does not recover the region either**. The published
miss and our run agree.

## What this does and does not license

**Supported:** *AggrescanAI does not outperform TANGO on these regions; on 6 of 7 it is
worse, and the paired difference is robust to every TANGO parameter we varied.*

**Not supported:** *legacy predictors beat modern ones.* The reverse direction was not
registered, and taken descriptively it does not reach significance either — sign test on
6 of 7, one-sided binomial **p = 0.0625**. **Neither direction is established at n = 7.**

**Also not supported:** anything about *generations*. One tool against one tool.

## What it means for the project's question

`CLAUDE.md` asks whether modern predictors recover the regions the 2004-2010 generation
missed. For the one modern tool that can be run and the one legacy tool that can be run:
**no — and the modern tool is the worse of the two on these regions.** Both miss both
confirmatory rows under the registered bar.

That is a sharper answer than "both fail", and it is the opposite of the outcome §4 was
written to detect. **The pre-registration specified a test for the result it expected and
not for the result it got** — which is an argument for pre-registration, not against it:
the expectation is on the record, dated, and visibly wrong.

## Reproduce

`scripts/run_tango_grid.py` — binary SHA-256
`d0e381c28f847487069b0df29bb9d4f766391066710500d3170ecb73d9f31dbf`, archive
`bef9a73141f8af5e9818bb79fe4f441fda378a3441c5e5e26a9f6519dac4710c`, both verified against
`data/predictor_provenance.json` at extraction. All 18 raw profiles are in
`tango_profiles/`. Scoring uses the same `scripts/score_rows.py` statistic as the modern
arm, on TANGO's `Aggregation` column per §5.3.

**Trap handled:** TANGO exits 0 on failure, so the runner checks that the output file
exists, is non-empty, and has exactly one row per residue. All 18 runs passed that check.

---

## Appendix, later on 17 November: n goes from 7 to 9, and the conclusion does not move

Two rows joined the contrast the same day. **Glycinin G4 164-190** was added to the dataset
and both arms were run on it. **ANXA11 39-74** had had a TANGO profile since this run; what
was missing was its AggrescanAI score, blocked by a missing line in a lookup table.

| row | TANGO *v* | AggrescanAI *v* | Δv |
|---|---|---|---|
| TRIOBP-1 1-59 | 0.9995 | 0.0409 | **−0.959** ← modern better |
| **ANXA11 39-74** | **0.4134** | **0.3315** | **−0.082** ← modern better |
| DISC1 748-769 | 0.9227 | 0.9955 | +0.073 |
| DISC1 384-415 | 0.3189 | 0.4164 | +0.097 |
| **glycinin G4 164-190** | **0.1645** | **0.3884** | **+0.224** |
| TMEM106B 120-254 | 0.7156 | 0.9900 | +0.274 |
| TRIOBP-1 333-340 | 0.0388 | 0.4240 | +0.385 |
| TRIOBP-1 324-348 | 0.1235 | 0.9079 | +0.784 |
| DISC1 691-836 | 0.0812 | 0.9994 | +0.918 |

> **Modern still does not beat legacy. On 7 of 9 rows it is worse.**
>
> §4 requires Wilcoxon one-sided **p < 0.05** *and* median Δv **< −0.10**. Observed:
> **p = 0.102**, median Δv = **+0.224**. Both fail, and the effect-size criterion still
> fails **by sign**.

ANXA11's TANGO v is 0.3735 at pH 5.0 and 0.4134 at pH 7.0/7.4, giving p = 0.082 and 0.102;
**7 of 9 and the median are unchanged at every grid point.** Glycinin's TANGO v is
identical to six decimals at all nine points.

**§4's threshold is now reachable, and was not before.** The minimum attainable one-sided
Wilcoxon p is 2⁻ⁿ — 0.25 at n=2, 0.0078 at n=7, **0.0020 at n=9**. The earlier statement
that no data could make this significant applied to the *confirmatory* set at n=2 and still
does; this exploratory set has passed the point where the test is merely arithmetic.
It returns a non-significant result on the merits now, which is a different and better
kind of negative.

**ANXA11 is the second row where modern wins**, but its margin (−0.082, and −0.042 at
pH 5.0) is well inside the phase spread of either arm. It is a tie more than a win.

**Neither direction is established**: 7 of 9 gives a one-sided binomial p = 0.0898.
And this is still one tool against one tool, not a statement about generations.

**One caveat the earlier rows did not have.** The glycinin row's legacy verdict is
**phase-dependent** — TANGO reaches v = 0.047 at four of the six tiling phases §3.1 leaves
unfixed, against 0.164 at the primary phase 0. Its Δv *direction* is robust (modern worse
at every phase), so the contrast above is unaffected, but see
`results/glycinin_2026-11-17/REPORT.md` for why that row sits on a knife-edge and the
earlier claim that "no conclusion depends on the phase" no longer holds set-wide.
