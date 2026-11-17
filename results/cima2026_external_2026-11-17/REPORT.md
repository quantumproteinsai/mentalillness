# The modern arm against Cima 2026's blind hexapeptide experiment

**EXPLORATORY. 17 November 2026, after the freeze and after scores were seen.** §12 governs:
this is an exploratory analysis and is reported as one. **It enters no confirmatory
statistic, and nothing in it bears on the registered DISC1/TRIOBP-1 result.**

---

## The headline, stated before the numbers so it cannot be mistaken for one

> **This exercise is uninformative at the available sample size, and that is its result.**
> AggrescanAI scores AUROC **0.500** on the firm-label set — but with 3 amyloid against 6
> non-amyloid, the exact permutation null puts **any AUROC between 0.11 and 0.89 within
> chance** (p = 0.548). The measurement cannot distinguish "no information" from
> "substantial information". Per `CLAUDE.md` rule 2, no further work on this set rescues it.

The 4/9 figure below is **not** evidence that AggrescanAI is poor, and the 9/9 figure is
**not** evidence that AggreProt is good. Both are explained before they are reported.

## Why this set looked worth running

Cima et al. 2026 (*Commun Chem* **9**:229, CC BY; data at doi:10.5281/zenodo.18670709)
synthesised hexapeptides from seven AmyPro proteins and classified them by TEM **blind to
the predicted scores** — *"by the experimentalist without knowledge of the predicted
aggregation scores of the hexapeptides to avoid biased assessment."*

Blind experimental labels are the rarest thing in this field. And the set is **circular
for AggreProt but not for AggrescanAI**, which had no part in choosing it.

## What the labels actually support — fewer than 17

**Only 9 of the 17 carry a firm amyloid / non-amyloid call**, and establishing that was
most of the work.

The supplementary table's `Aggregation +/-` column is **not** an amyloid call. It records
whether aggregates of *any* kind appeared, and the paper classifies TEM structures into
five categories including amorphous clumps and hydrogels. The proof that `+` ≠ amyloid is
internal: **DYRRYQ carries `+` in the table and is called non-amyloid in Fig. 3a.**

So the firm labels are only:

- the **five γ-crystallin D peptides**, which Fig. 3a labels explicitly, and
- the **four peptides scored `-`**, meaning no aggregates of any kind, which is
  unambiguously non-amyloid.

The remaining 8 are `+` with the amyloid/amorphous distinction carried only by the
micrographs — that call belongs to the experimentalist who made it blind, not to us.

| | n |
|---|---|
| firm **amyloid** | 3 (SWVLYE, IHSLNV, GCWMLY) |
| firm **non-amyloid** | 6 (EREDYR, DYRRYQ, ARTLKR, VEADIA, RDMWRA, GEEQGS) |
| ambiguous, excluded | 8 |

## Results on the 9

Every peptide was located **by sequence search**, not by trusting a stated range. The
method validated itself: the γ-crystallin D hits reproduce the paper's own ranges exactly
(121-126, 41-46, 94-99, 150-155).

| peptide | protein | pos | AggreProt | AggrescanAI mean | label |
|---|---|---|---|---|---|
| SWVLYE | γ-crystallin D | 130-135 | 0.497 | 0.190 | amyloid |
| IHSLNV | γ-crystallin D | 121-126 | 0.393 | 0.549 | amyloid |
| GCWMLY | γ-crystallin D | 41-46 | 0.407 | 0.468 | amyloid |
| EREDYR | γ-crystallin D | 94-99 | 0.014 | 0.153 | non-amyloid |
| DYRRYQ | γ-crystallin D | 150-155 | 0.014 | 0.073 | non-amyloid |
| ARTLKR | lysozyme C | 27-32 | 0.025 | 0.924 | non-amyloid |
| VEADIA | apomyoglobin | 18-23 | 0.077 | 0.516 | non-amyloid |
| RDMWRA | serum amyloid A | 33-38 | 0.017 | 0.718 | non-amyloid |
| GEEQGS | galectin-7 | 40-45 | 0.087 | 0.284 | non-amyloid |

| | AUROC | accuracy at threshold | best over **all** thresholds |
|---|---|---|---|
| AggreProt (0.25) | **1.000** | 9/9 | 9/9 |
| AggrescanAI (0.5) | **0.500** | 4/9 | **6/9** |

**6/9 is exactly what "always answer non-amyloid" scores.** No threshold rescues it.

## The two reasons neither number means what it looks like

**AggreProt's 1.000 is circular by construction.** These peptides were selected *because*
AggreProt disagreed with AmyPro/CPAD, and the experiment was run to adjudicate. A perfect
score is close to guaranteed by the selection rule. The authors do not claim otherwise;
the circularity is in their stated selection criteria. **This is exactly what
`circularity_status` exists to catch, and it would mark all 17 rows `CIRCULAR`.**

**AggrescanAI's 0.500 is not a fair failure either.** The set is adversarially selected
against the database annotation, and AggrescanAI ships the **CPAD90** model. A predictor
trained on CPAD is *expected* to reproduce CPAD's errors on peptides chosen for being
CPAD's errors. **That is this project's contamination thesis, and this set is too small to
demonstrate it** — it would need peptides where the database is right as a control, which
by construction this set does not contain.

## One methodological finding that does survive

**The same hexapeptide scores differently depending on the frame it is scored in.**
RDMWRA scores **0.641** in the mature hSAA1.1 chain and **0.718** in the P0DJI8 precursor —
the same six residues, differing only by an 18-residue N-terminal signal peptide 14
residues away.

A PLM-based predictor's output is **context-dependent**, so a hexapeptide score is a
property of *(peptide, construct)*, not of the peptide. This is the dataset's `construct`
lesson reappearing inside the predictor, and it means **a frame choice is a scoring choice**.
Anyone comparing predictors on hexapeptides must state the chain they were scored in.

## Reproduce

`scripts/run_aggrescanai.py` on the seven canonical UniProt sequences — P61626, P68082,
P0DJI8, P59637, P0A734, P47929, P07320 — pins and checksums in every output header.
Raw per-residue profiles are archived beside this file.
