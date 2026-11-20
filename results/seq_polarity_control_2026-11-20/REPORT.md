# The sequence-polarity control — PREREGISTRATION §10d, run 20 November 2026

> ## REGISTERED VERDICT: **`COLLAPSED`**, at both registered burial cutoffs.
>
> **§10a's core-polarity claim is withdrawn as a structural finding.** The mapped region's
> **sequence** polar fraction predicts *v* **better** than the buried-core polarity does,
> and once sequence composition is controlled for, Φ's residual association with *v* is
> **negative**. The decision rule that produced this verdict was committed in `414b139`,
> **before the control variable was computed**.

---

## What was registered, and when

`PREREGISTRATION.md` §10d, commit **`414b139`**, 20 Nov 2026 — the variable, the three
statistics, the seven rows, both burial cutoffs and all four possible verdicts, written
down **before `Φ_seq` existed anywhere**. The commit message says so and the commit graph
proves the order.

**Φ_seq** = fraction of residues in the **whole registered range** that are in §10a's own
POLAR set `DEKRHNQSTYC` — not the buried subset, all of them. Computed from the **same
pinned coordinate files** Φ was computed from, over the **same ranges**, by importing
`scripts/core_polarity.py` rather than reimplementing its parser.

## Two gates passed before any new number was read

**1. All seven coordinate files match the pinned SHA-256s** in
`data/coordinate_manifest.json`.

**2. Φ–*v* reproduces at the published value.** ρ(Φ cut-10, *v*) = **+0.8214** against the
published +0.821. The script asserts this and stops if it fails. Without it, a mismatch in
how the inputs were assembled would have been indistinguishable from a real result — which
is exactly what happened on 19 Nov, when an ad-hoc reimplementation of the *v* step bypassed
a frame offset and returned ρ = +0.633.

**3. The curated sequence agrees with the coordinates on all seven rows**, residue for
residue. §10d made a disagreement a hard failure rather than a warning.

## The data

| row | Φ_seq | Φ (cut 5) | Φ (cut 10) | *v* |
|---|---|---|---|---|
| FUS 39-95 | 0.7719 | 0.6579 | 0.6750 | 0.9582 |
| TMEM106B 120-254 | 0.5852 | 0.5752 | 0.5772 | 0.9900 |
| LECT2 55-75 | 0.5238 | 0.5263 | 0.5263 | 0.4054 |
| hnRNPA1 251-295 | 0.4889 | 0.4651 | 0.4651 | 0.4626 |
| glycinin 164-190 | 0.4815 | 0.4583 | 0.4583 | 0.3884 |
| SAA 2-55 | 0.4630 | 0.4706 | 0.4615 | 0.2124 |
| ANXA11 39-74 | 0.4444 | 0.4412 | 0.4412 | 0.3315 |

## The result

| | cut 5 Å² | cut 10 Å² |
|---|---|---|
| ρ(Φ, *v*) | +0.6786 *(p = 0.0548)* | +0.8214 *(p = 0.0171)* |
| **ρ(Φ_seq, *v*)** | **+0.8929** *(p = 0.0062)* | **+0.8929** *(p = 0.0062)* |
| ρ(Φ, Φ_seq) — collinearity | +0.8929 | **+0.9643** |
| **partial ρ(Φ, *v* │ Φ_seq)** | **−0.5849** | **−0.3315** |
| **verdict** | **COLLAPSED** | **COLLAPSED** |

All *p* exact, one-sided, enumerated over all 7! = 5040 orderings.

### Three things this says, in order of how much they cost

**1. The sequence-only covariate does better than the structural one.** +0.8929 against
+0.8214, and *p* = 0.0062 against 0.0171. §10d's first clause fires: *"ρ(Φ_seq, v) ≥
ρ(Φ, v) → COLLAPSED."* **It does not merely tie. It wins.** You do not need a deposited
fibril structure to obtain this association; you need the region's sequence, which every
row in the dataset has and which costs nothing.

**2. The partial correlation is NEGATIVE at both cutoffs.** Controlling for sequence
polarity, what remains of Φ points the *other way* — −0.3315 at cut 10, −0.5849 at cut 5.
**Φ is not adding structural information to a compositional signal; it is a noisier
measurement of the compositional signal.** At ρ(Φ, Φ_seq) = +0.9643 the two are barely
distinguishable, and burial is subtracting information rather than adding it.

**3. And the headline result was never stable across its own registered cutoffs.** At the
5 Å² burial threshold — **a registered variant, not a post-hoc one** — ρ(Φ, *v*) = +0.6786,
*p* = **0.0548**. **The §10a result fails the project's own α = 0.05 at the other
pre-specified cutoff.** The 19 Nov audit flagged that the cut-5 sensitivity was owed and
had been kept in reserve; this is the first time the number has existed. It should have
been computed and reported in §10a.

## What this means for the claim

**It collapses into Louros 2020 — and by a more expensive route, on seven points.**

> **Louros N, Orlando G, De Vleeschouwer M, Rousseau F, Schymkowitz J (2020),
> *Nat Commun* 11:3314** — APRs missed by sequence predictors carry **a 20% increase in
> polar and charged side chains**, quantified, with ANOVA and 85 of 96 designed peptides
> validated.

That is this result, established at vastly larger *n*, five years earlier, **without
needing a single deposited structure.** The structural apparatus — 22 coordinate files,
Shrake-Rupley SASA, 11-layer helical replication, a calibrated AUROC — bought a *weaker*
version of a published finding.

**What is NOT being claimed.** Not that polar regions are unrelated to predictor failure:
that association is real here, at ρ = +0.89, and is the strongest thing in this part of the
project. **It is not new, and it is not structural.** Those are two different retractions
and both apply.

### Where this leaves the four audited claims

| claim | status after 19–20 Nov |
|---|---|
| **1 — Φ as a metric** | **PRE-EMPTED.** García-Pardo et al. (2023) *Nat Commun* 14:239, with a numerical collision on 6MST: their 46% against our 0.4615. |
| **2 — the Φ–*v* association** | **COLLAPSED** (this document). Compositional, not structural; and weaker than the compositional version. |
| **3 — the information limit** | Universal form **contradicted**; the bound is Tarone's rule (1990). **The application to aggregation benchmarking is novel** and survives. |
| **4 — competitor sweep** | No pre-emption found. |

**One of four survives, and it is the one that needed no compute at all.** §3.1b's
information limit is arithmetic on chain lengths and region lengths — the cheapest thing in
the project, and now the only part of this strand that is both true and new.

## The honest reading of the process, not only the result

**The rule was written down before the number existed, and it fired against the hypothesis
it was written to protect.** That is the entire argument for pre-registration, demonstrated
on this project's own most attractive finding — a finding already written into a deposited
dataset's description, already in the manuscript draft, and already surviving one audit.

**It cost about ten minutes of compute.** The alternative was publishing a structural claim
that a referee with `DEKRHNQSTYC` and a text editor could have falsified in an afternoon —
and the audit on 19 Nov named this exact risk, in writing, as the claim's survival
condition.

**The Φ set remains a valid dataset.** The 22 structures, the checksummed manifest, the
edge-free replication and the per-structure values are correct measurements and stay. What
is withdrawn is the *interpretation* placed on them.

## Reproducing this

```
python3 -I scripts/seq_polarity_control.py . <coorddir> out.json
```

`<coorddir>` holds the deposited `.cif` files; `scripts/fetch_coordinates.py` fetches them
and verifies every checksum against `data/coordinate_manifest.json`, exiting non-zero on a
mismatch rather than warning. The script recomputes no Φ and runs no predictor: Φ is read
from `results/core_polarity_2026-11-19/phi_rows_11layers.json` and *v* comes from
`scripts/score_rows.py` through `join_phi_v.get_v()`, so neither can be altered here.

**It computes exactly one new number per row, and the verdict is applied rather than
chosen** — the four outcomes and their thresholds are in §10d, committed first.
