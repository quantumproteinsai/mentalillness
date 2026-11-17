# The control arm: does AggrescanAI fail everywhere, or only where CPAD is wrong?

**EXPLORATORY. 17 November 2026, post-freeze and post-unblinding.** §12 governs. Enters no
confirmatory statistic.

---

## Why this exists

The Cima external run (`results/cima2026_external_2026-11-17/`) left AggrescanAI at
AUROC 0.500 on 9 hexapeptides whose database annotation is demonstrably wrong — a number
that could mean either of two very different things:

- **the predictor is weak**, or
- **the predictor has memorised CPAD**, and so reproduces CPAD's errors.

These are indistinguishable without peptides where **the database is right**. That is the
control, and it was missing.

## The control set, specified before anything was scored

Pre-specified rule, applied to the complete CPAD 2.0 peptide table:

1. length **6**;
2. **wild-type only** (`Mutant = No`);
3. class exactly `amyloid` or `non-amyloid`;
4. carries a UniProt accession;
5. the peptide occurs **exactly once** in that canonical sequence (so it can be scored in
   context, and the location is unambiguous);
6. the protein contributes **≥ 4** such peptides **and both classes**, so every protein
   supplies a *within-protein* contrast and protein identity cannot drive the result.

**Result: 17 proteins, 540 peptides — 59 amyloid, 481 non-amyloid.** Scored exactly as the
Cima peptides were: per-residue AggrescanAI in full-chain context, mean over the six
residues.

**The wild-type filter was not cosmetic.** Before it, 303 of 889 peptides could not be
located. Every single failure was a mutant — a mutant hexapeptide is by construction
absent from the wild-type sequence. After filtering, **97.1%** located uniquely.

## Result

| set | database annotation | AUROC | 95% interval | p vs chance | n |
|---|---|---|---|---|---|
| **control** | uncontested | **0.703** | [0.639, 0.760] | **0.0005** | 59 vs 481 |
| **contested** (Cima) | demonstrably wrong | **0.500** | [0.111, 0.889] | 0.548 | 3 vs 6 |

Within-protein AUROCs, pair-weighted: **0.829**. Per-protein values are in the table below
the fold; all 17 are ≥ 0.61.

## What this settles — and it is the valuable part

> **AggrescanAI is not uninformative, and our pipeline reproduces its published
> performance.** On 540 hexapeptides it scores AUROC **0.703**, against the **0.69**
> Navarro et al. 2026 report for AggrescanAI on their own external benchmark (Fig. 2).

That is an independent 540-point validation of `scripts/run_aggrescanai.py`, far stronger
than the tau and α-synuclein smoke tests used before the first run. **It means the
registered null on DISC1 384-415 and TRIOBP-1 324-348 is not an artefact of a broken local
pipeline.** The predictor works here at the level its authors report, and still does not
find those regions.

## What this does NOT settle, despite appearances

**The memorisation hypothesis remains untested.** 0.500 against 0.703 looks like the
signature — but the contested set's interval, **[0.111, 0.889], contains 0.703**. The two
measurements are not distinguishable. Anyone quoting "0.50 versus 0.70" as evidence of
training-set memorisation would be over-reading a 9-peptide sample.

**How much more would be needed**, by simulation at balanced group sizes:

| contested peptides | power to show a real drop from 0.703 |
|---|---|
| 10 vs 10 | 0.34 |
| 25 vs 25 | 0.71 |
| **40 vs 40** | **0.86** |
| 50 vs 50 | 0.94 |

**We have 3 vs 6.** The experiment needs roughly an order of magnitude more peptides whose
database annotation has been experimentally overturned — and those are rare precisely
because overturning one costs a four-week TEM experiment. **This is a reason to stop, not a
reason to run more compute**, per `CLAUDE.md` rule 2.

## Two caveats that limit the control itself

**The control peptides are AggrescanAI's training data.** CPAD90 is CPAD plus homologues,
so 0.703 is an *in-sample* figure. In-sample AUROC of 0.70 is modest — but the comparison,
not the absolute level, is the point here.

**Severe class imbalance, unevenly distributed.** 59 amyloid against 481 non-amyloid, and
one protein (P05453) contributes 172 peptides with a single amyloid. The pooled figure is
therefore reported alongside the pair-weighted within-protein mean (0.829), which does not
let one protein dominate.

## Per-protein

| accession | amyloid | non-amyloid | AUROC |
|---|---|---|---|
| P05453 | 1 | 171 | 0.614 |
| P28307 | 6 | 94 | 0.855 |
| Q13148 | 2 | 68 | 0.956 |
| P35637 | 1 | 47 | 1.000 |
| P61769 | 7 | 37 | 0.826 |
| P00441 | 6 | 15 | 0.733 |
| P01308 | 3 | 13 | 0.846 |
| P04156 | 12 | 1 | 1.000 |
| G1UBC2 | 1 | 8 | 1.000 |
| Q5A8T4 | 3 | 5 | 0.667 |
| P32770 | 1 | 6 | 1.000 |
| P06280 | 1 | 6 | 1.000 |
| P02647 | 5 | 1 | 1.000 |
| E9P9G2 | 2 | 4 | 0.875 |
| P61823 | 4 | 1 | 1.000 |
| P02766 | 3 | 1 | 1.000 |
| P14922 | 1 | 3 | 1.000 |

## Reproducing this, and what is deliberately absent

**No CPAD content is stored in this repository** — not the peptide sequences, not their
labels. CPAD 2.0's terms forbid redistribution. What is stored is the **selection rule
above**, the **accession list** in the table, and **our own per-residue profiles**, which
are outputs of our run on public UniProt sequences. Anyone with their own CPAD access can
rebuild the peptide set exactly from the rule.

Profiles were produced by `scripts/run_aggrescanai.py`, pins and checksums in every file
header. Peptides were located by sequence search, never by a stated coordinate.
