# Structural recruitment for Φ — the rule, written before any candidate was searched for

**18 November 2026, registered as PREREGISTRATION §10b.** This file was committed
**before** the first search query was issued. Its purpose is that the rows admitted to the
core-polarity analysis are chosen by a criterion fixed in advance, not by what happens to
make ρ larger.

---

## Why recruit at all, and why this pool is different

§3.1b closed benchmark recruitment: a row is useless to the benchmark unless *m*/*M* ≤
0.05, and nine candidates screened on 18 Nov produced none. **That constraint does not
apply here.** Φ requires a *deposited fibril structure*; §3.1b requires a *short region in
a long chain*. The two criteria are nearly disjoint.

**All seven rows currently in the Φ analysis fail *m*/*M* > 0.05.** The row type that is
exhausted for the benchmark is the row type this analysis runs on.

The reason to grow it is stated plainly: at *n* = 7 the registered result
(ρ = +0.821, exact *p* = 0.0171) **dies if any one of four rows is dropped**. That is the
weakness a referee will find first, and *n* is the only thing that fixes it.

---

## Eligibility — all six must hold

**E1. An experimentally determined region, by EITHER route**, to the same standard as
every row in `data/regions.json`: a residue range in a **named frame**, with `construct`
and `found_by` recorded, from a source **read in full**. A region asserted in a review is
not a row. The two admissible routes are:

- **(a) structure determination** — the ordered fibril core read off density or
  solid-state NMR; or
- **(b) deletion or truncation mapping** — a region whose removal abolishes aggregation
  of a longer construct.

**In both cases no aggregation predictor may appear in the discovery path.**

> **E1 CORRECTED SAME DAY, BEFORE ANY CANDIDATE WAS ADMITTED.** As first written, E1
> demanded an *"aggregation-critical"* region, which reads as route (b) only. **All seven
> rows already in this analysis are route (a)** — FUS by solid-state NMR, the other six by
> cryo-EM density. Recruiting under the original wording would have admitted a **different
> evidence type** from the incumbents and silently made the association a comparison
> across two kinds of region. Found by checking the incumbent rows' `found_by` values
> against the rule, not by anything failing.
>
> **Consequence for E2:** for a route (a) row the region *is* the modelled core, so
> coverage is 100 % by construction and the ≥ 80 % threshold only bites on route (b) rows.
> **Which route a row took is recorded**, and if the final set mixes routes, the mix is
> reported and the test is repeated within the larger route.

**E2. A deposited structure of the aggregated state**, whose model covers **≥ 80 % of the
region's residues**. Below 80 % the row is rejected, not truncated to fit.

**E3. The deposit is of the aggregate, not the soluble native fold.** A crystal structure
of the folded protein is not a fibril core and tells us nothing about buried polarity in
the aggregated state.

**E4. Φ must be computable:** deposited helical rise and twist, **or** a genuine
multi-layer stack of ≥ 5 layers as deposited.

**E5. The frame is verified against UniProt or RefSeq**, and the region's residues match
the modelled sequence at those positions. Checked, not assumed — this project has found
four one-residue slips and two frame collisions in published work in three days.

**E6. `found_by` is not prediction.** A region nominated by a predictor and then confirmed
is circular for any predictor analysis. Such a row may be recorded, but is analysed
separately and never pooled.

**`m`/`M` IS NOT A CRITERION HERE, and must not be applied.** Screening these candidates
on *m*/*M* would reimport the constraint this analysis is free of, and would do it after
the rows' geometry is visible. Stated explicitly so it cannot drift in later.

---

## One row per protein — fixed now, because it is the obvious place to cherry-pick

**R1. If a protein yields several eligible regions**, take the one with the **greatest
fraction of region residues modelled**; tie broken by the **lowest start residue**.

**R2. If a region has several eligible structures**, take the one with the **highest
coverage** of the region; tie broken by **best resolution**, then by **lowest PDB ID**.

Both rules are mechanical and neither consults Φ or *v*.

---

## Ordering — checkable from the commit graph, as in §7a and §10a

1. **The screened candidate list is committed first**, with every candidate and its
   accept/reject reason, including the rejects.
2. **Φ is computed and committed.**
3. **Only then** is the predictor run and *v* computed.
4. **Only then** are the two joined.

---

## Stopping, and the one rule that matters most

**S1.** Search until the candidate pool is exhausted or **15 rows** are reached, whichever
comes first.

**S2. The Φ–*v* test is recomputed ONCE, at the final *n*.** No interim analysis. The
analysis is not run after each row, and recruitment does not stop because a *p* crossed a
threshold. **This is the rule that makes the exercise worth doing**; without it, growing
*n* with the result in view is optional stopping and the final *p* means nothing.

**S3.** The seven existing rows stay as they are and are not re-selected.

**S4.** The final *n* is reported whatever it is, with the smallest attainable *p* at that
*n* printed beside the observed one, and the leave-one-out table reported in full as it
was at *n* = 7.

**S5. If fewer than three new rows are admitted, the analysis is not re-run at all.** The
*n* = 7 result stands as it is, with its fragility, and the recruitment is reported as a
negative. Two extra rows cannot fix leave-one-out fragility and re-running to add them
would be a second look at the same data.

---

## What growing *n* cannot do

**This analysis remains permanently exploratory**, for the reason §10a already gives and
which no number of rows changes: **DISC1 and TRIOBP-1 have no deposited fibril
structures.** The confirmatory stratum is not in this analysis and cannot be put into it.
A larger *n* makes the association more credible; it does not make it a test of H1.

**And the registered near-tautology still stands.** A predictor built on hydrophobicity
scoring polar cores lower is partly a restatement of how it works. The claim worth making
is not that the tools dislike polar cores, but that nature does not.

---

# Amendment: §10c, discontinuous ordered cores — 19 Nov 2026

**Registered before any Φ was computed.** Full text in `PREREGISTRATION.md` §10c; this is
the summary and the reason.

**What broke.** E2 says a route (a) row's region *is* the modelled core. It assumed, without
saying so, that the core is **one contiguous span**. All eleven structure rows then in the
dataset are contiguous, so the assumption had never been tested. Reading the deposited
coordinates of the three candidates on 19 Nov broke it: **7VZF models 3-55 and 86-153**
(30-residue gap) and **8QUT models 22-34 and 50-128** (15-residue gap). Both papers describe
the gap themselves. It is a feature of the fold, not a modelling failure.

**Why R1 could not be stretched to cover it.** R1 picks among *several distinct regions in
one protein*. Applied to segments it would have taken SOD1 **3-55** and lysozyme **22-34** —
thirteen residues — discarding seventy-nine. **Φ computed on a fragment of a core is not Φ
of that core.**

**The rule.** One region, recorded as a segment list; `region_contiguous: false`; E5 verified
per segment; **Φ computed over all modelled residues, gaps excluded because they are not
there and never interpolated**; the row marked `benchmark_eligible: false` with reason
`NON_CONTIGUOUS`, **a ground separate from *m*/*M*** because the §3.1 statistic tiles a
contiguous span and has no defined behaviour on a segment list; and if the final set mixes
contiguous with discontinuous rows, the mix is reported and the association repeated within
the contiguous subset.

**Why admit rather than reject.** A contiguity filter is **a size filter wearing a
disguise**: the two gapped candidates are the two largest cores in the pool — SOD1 121
modelled residues, lysozyme 92, against a median of ~35 for the eleven incumbents. If buried
polarity varies with core size, excluding them biases the set in an unknown direction. The
argument is about geometry and says nothing about Φ.

> **The exposure, stated rather than buried.** This rule admits rows, so it makes S5's
> three-row threshold easier to reach, and it was written by the same agent that wanted the
> rows, on the day it wanted them. Φ had not been computed for SOD1, lysozyme or β2m, and no
> *v* had been computed for any of them; the rule is committed ahead of the first Φ call and
> the commit graph is the evidence. **The author should review it on exactly that ground.**

**One thing §10c does not do.** It does not relax S2. The pool is not exhausted — four
candidates pending, five unscreened — so the final *n* is unknown and **the Φ–*v* test must
not be recomputed now**, three rows or not.
