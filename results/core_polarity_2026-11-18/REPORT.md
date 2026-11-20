# Core polarity (Φ) — computed, 18 November 2026

> # ⛔ THE STRUCTURAL READING OF Φ IS WITHDRAWN — 20 November 2026
>
> **A control registered under PREREGISTRATION §10d, committed before the variable was
> computed, returned `COLLAPSED` at both pre-registered burial cutoffs.** The polar
> fraction of the mapped region's own **sequence** predicts *v* **better** than buried-core
> polarity does (ρ = +0.89, *p* = 0.0062, against +0.82, *p* = 0.0171); the two are
> collinear at ρ = +0.96; and the partial correlation of Φ with *v* given sequence polarity
> is **negative**.
>
> **Every measurement in this document stands exactly as recorded. The interpretation
> placed on them does not.** The association is real, compositional rather than structural,
> and already published — Louros et al. (2020) *Nat Commun* **11**:3314.
>
> This document is left as written rather than rewritten, because what it claimed before
> the control is the evidence for why the control was worth registering.
> See `results/seq_polarity_control_2026-11-20/`.

**Specification registered first** (`reports/core_polarity_metric_2026-11-18.md`,
PREREGISTRATION §10a), **structures committed second** (`9afee85`), **Φ computed here.**

**Φ HAS NOT BEEN JOINED TO ANY PREDICTOR SCORE.** `scripts/core_polarity.py` does not
import `score_rows`, does not open anything under `results/` and does not know what *v*
is. The join is a separate step in a later commit, so that the commit graph shows Φ was
fixed before it met *v*.

---

## 1. The calibration decides whether the metric lives, and it lives

S6's twelve published structures, classified by their own authors, against Φ computed
here. **The registered abandonment condition was AUROC < 0.80.**

| variant | SASA cut | AUROC | Youden J | Φ\* |
|---|---|---|---|---|
| **Φ (primary)** | **10 Å²** | **0.844** | 0.62 | **0.477** |
| Φ | 5 Å² | 0.906 | 0.88 | 0.526 |
| Φ | 20 Å² | 0.875 | 0.75 | 0.481 |
| Φ, glycine excluded | 10 Å² | 0.875 | 0.75 | 0.512 |
| Φ, Y and C non-polar | 10 Å² | 0.938 | 0.88 | 0.455 |

**All nine pre-specified cut × variant combinations pass**, so the verdict does not depend
on the three arguable assignments (Y, C, G) that the specification flagged in advance.
The primary is the weakest of them, which is the right way round: the registered number
is not the flattering one.

```
0.778  FUS 6XFM            HYDROPHILIC
0.563  tau 5O3L            hydrophobic     <- highest hydrophobic
0.543  FapC 9U4U           HYDROPHILIC
0.533  FapC 9NQD           HYDROPHILIC
0.504  AL59 9FAA           hydrophobic
0.478  transthyretin 7OB4  hydrophobic
0.477  CsgA 8ENQ           HYDROPHILIC     <- lowest hydrophilic, Φ* sits here
0.429  a-syn 6H6B          hydrophobic
0.400  prion 8WZX          hydrophobic
0.303  Abeta 7Q4B          hydrophobic
0.276  Abeta 7Q4M          hydrophobic
0.208  prion 7YAT          hydrophobic
```

**The separation is real but not clean**: four of the twelve sit within 0.03 of the
threshold. Φ is a weak classifier of S6's labels, not a proxy for them.

## 2. Φ for the seven eligible rows

Primary variant, SASA < 10 Å², region restricted to the row's own residue range.

| row | PDB | chain | core / range | **Φ** | vs Φ\* = 0.477 |
|---|---|---|---|---|---|
| FUS 39-95 | 5W3N | E | 40/57 | **0.675** | polar |
| TMEM106B 120-254 | 7U16 | B | 123/135 | **0.577** | polar |
| LECT2 55-75 | 8G2V | A | 19/21 | **0.526** | polar |
| glycinin G4 164-190 | 9V45 | F | 25/27 | **0.480** | polar, by 0.003 |
| hnRNPA1 251-295 | 7ZJ2 | G | 43/45 | **0.465** | non-polar |
| SAA 2-55 | 6MST | H | 52/54 | **0.462** | non-polar |
| ANXA11 39-74 | 9FOR | p | 34/36 | **0.441** | non-polar |

### The pre-registered check on the metric passed

**LECT2's own paper is titled "…reveals a network of polar ladders at its core."** That
claim was recorded on the row *before* Φ existed, precisely as a test of the metric. Φ
puts LECT2 at 0.526, above threshold, **agreeing with its authors**. One row is not a
validation, but it was a genuine opportunity for the metric to fail and it did not.

**Two independent FUS structures agree**: 5W3N (our row, 0.675) and 6XFM (S6's
calibration entry, 0.778) are different depositions of different FUS segments, and both
land well above threshold.

**Glycinin at 0.480 against a 0.477 threshold is a knife-edge** — fitting for a paper
titled *"Dual Hydrophilic-Hydrophobic Core Architecture"*, but it must not be reported as
a clean classification.

## 3. Two parser defects, both found by checking rather than by failing

**1. A silent truncation.** The first helical-parameter extraction read only the first
400 kB of each file and returned `rise = None` for 9V45, whose block sits past that point.
A missing rise would have meant "use as deposited" for a structure that should have been
replicated.

**2. A regex that crossed a newline into a `loop_` table.** 8WZX stores its helical
parameters in the tabular form; the scalar regex matched the tag, skipped the newline and
captured the first field of the *data row*, returning **rise = 1.0, twist = None** instead
of the true **2.38 / 179.217**. A wrong rise builds a wrong assembly, and the output would
have looked entirely normal.

`scripts/helix_extract.py` now handles both forms. **Neither defect was caught by anything
failing** — both were found by reading values that looked implausible against the physics
(a 1.0 Å rise is not a β-sheet), which is the only reason they were caught at all.

## 4. What was actually executed

| | |
|---|---|
| assembly | 13 copies (−6…+6) along **z**, from the deposited rise and twist |
| axis check | **verified, not assumed**: layer centroid spacings match the deposited rise in all seven (9FOR alternates 0.99/3.99 = 4.98, ANXA11 and TDP-43 interleaving) |
| as-deposited | 5W3N (9 chains, 39 Å) and 8ENQ (7 chains, 145 Å) carry no helical parameters; both are genuine multi-layer stacks, so neither is under-buried |
| SASA | Shrake–Rupley, probe 1.4 Å, 92 points, C 1.70 N 1.55 O 1.52 S 1.80 |
| analysis chain | the chain of the target entity nearest the middle of the deposit along z |

## 5. Standing caveats on three rows

- **ANXA11 (9FOR) is heteromeric.** Its residues are buried partly by TDP-43. Φ = 0.441
  describes a two-protein interface, not a homomeric core.
- **TMEM106B (7U16)** carries the transmembrane-helix confound already recorded on the row.
- **Glycinin (9V45) is PM1**, 27.8% of the fibrils; the 70.8% polymorph has no model.

## 6. What happens next, and what cannot

The join to *v* is the next commit. **Whatever it shows, it stays exploratory**: DISC1 and
TRIOBP-1 have no structures, so the confirmatory stratum is not in this analysis at all,
and seven non-independent rows cannot settle anything.

---

# The join to *v* — §10a §5, run after Φ was committed

## The registered primary test passes

**Spearman ρ = +0.821, exact one-sided p = 0.0171, n = 7.** The registered α was 0.05 and
the direction was named in advance: higher Φ → higher *v* → worse recovery.

| row | Φ | *v* (AggrescanAI) |
|---|---|---|
| FUS 39-95 | 0.675 | 0.9582 |
| TMEM106B 120-254 | 0.577 | 0.9900 |
| LECT2 55-75 | 0.526 | 0.4054 |
| glycinin G4 164-190 | 0.480 | 0.3884 |
| hnRNPA1 251-295 | 0.465 | 0.4626 |
| serum amyloid A 2-55 | 0.462 | 0.2124 |
| ANXA11 39-74 | 0.441 | 0.3315 |

p is **exact over all 5040 permutations**, not asymptotic; the smallest attainable value
at n = 7 is 0.0002, so 0.0171 is a real result rather than a floor.

**These seven rows are seven distinct proteins.** This is the only analysis in the project
where the independence assumption is actually satisfied — the confirmatory set's n = 8
collapsed to 5 proteins, and this one does not collapse at all.

## It is not a CPAD artefact, and that was the obvious way for it to be wrong

| | |
|---|---|
| ρ(CPAD membership, *v*) | **+0.000** |
| ρ(CPAD membership, Φ) | **+0.144** |

CPAD members span Φ 0.462–0.675 and *v* 0.212–0.958; CPAD-absent rows span Φ 0.441–0.577
and *v* 0.332–0.990. **The two factors are not collinear here**, which is precisely what
killed the first version of this test when it tried to borrow S6's labels. The association
survives the confound that the design was rebuilt to avoid.

## BUT IT IS FRAGILE, AND THIS IS THE QUALIFIER THAT MATTERS

Leave-one-out, unregistered, **all seven reported**:

| dropped | ρ | p |
|---|---|---|
| hnRNPA1 251-295 | +0.886 | 0.0167 |
| LECT2 55-75 | +0.829 | 0.0292 |
| glycinin G4 164-190 | +0.829 | 0.0292 |
| **FUS 39-95** | +0.771 | **0.0514** |
| **TMEM106B 120-254** | +0.771 | **0.0514** |
| **serum amyloid A 2-55** | +0.771 | **0.0514** |
| **ANXA11 39-74** | +0.771 | **0.0514** |

**Dropping any one of four rows takes p just above 0.05.** At n = 6 the smallest
attainable p is 0.0014, so 0.0514 is a genuine value and not a floor — the result simply
does not have room to spare. **The correct reading is "significant at the registered α on
seven rows, and not robust to the loss of any one of four of them."**

One of those four is **TMEM106B**, which carries the standing transmembrane-helix confound:
its frame contains a hydrophobic segment that was never in the fibril, which inflates its
*v* independently of anything about polarity. It is also the second-highest Φ. So the
single most influential point is the one with a known, unrelated reason to sit where it
sits.

## The two subgroup analyses say nothing, and were expected not to

- **CPAD-absent rows alone: ρ = +1.000, p = 0.1667, n = 3.** The association is as extreme
  as the data permit and **still cannot reach significance, because 0.1667 is the smallest
  attainable p at n = 3.** This is the same structural defect as §4 at n = 2: a test that
  could not have passed whatever the data did.
- **Legacy arm: ρ = +0.500, p = 0.50, n = 3.** TANGO was never run on FUS, hnRNPA1, SAA or
  LECT2, so the secondary analysis has three points. It neither supports nor contradicts.

## What this licenses, and what it does not

**Permitted:** *Across seven structurally characterised proteins, fibril cores with a
higher buried polar fraction are recovered less well by AggrescanAI (ρ = +0.82,
p = 0.017), and this is not explained by CPAD membership. The association is not robust to
leave-one-out.*

**Not permitted:**

- anything about **DISC1 or TRIOBP-1**, which have no structures and are not in this
  analysis — the confirmatory stratum is untouched and the headline question unmoved;
- any claim that the legacy generation behaves the same way: n = 3 cannot support it;
- **and the tautology registered in advance still applies.** A predictor built on
  hydrophobicity scoring polar cores lower is partly a restatement of how it works. The
  part that is not tautological is the experimental half: **these polar-core regions are
  genuine, experimentally mapped aggregation determinants.** The finding is not that the
  tools dislike polar cores. It is that nature does not, and the tools have not noticed.

---

## Geometry does not explain the association [18 Nov 2026, unregistered, exploratory]

The obvious second way for §10a's result to be wrong — after CPAD, which was already
excluded — is the *m*/*M* geometry that §3.1b showed drives everything else in this
project. **All seven structural rows fail *m*/*M* > 0.05**, and the mean of *v* is known
to depart from 0.5 where *m* is large. If Φ tracked *m*/*M*, the association would be a
restatement of region length.

| test | Spearman ρ | exact *p* |
|---|---|---|
| **Φ vs *v*** (registered primary) | **+0.821** | **0.0171**, one-sided |
| *m*/*M* vs *v* | +0.321 | 0.498, two-sided |
| *m*/*M* vs Φ | +0.321 | 0.498, two-sided |

**Spearman partial ρ(Φ, *v* | *m*/*M*) = +0.801**, against +0.821 unadjusted — a shift of
−0.021. The association is not geometric.

**The honest qualifier:** at *n* = 7 a test *for* confounding has very little power, so
this shows the confound is not large enough to generate the result, not that it is absent.
Both legs sit at ρ = +0.32, which is not nothing.

**And the observation that matters for what to do next: all seven of these rows are rows
the benchmark cannot use.** Φ needs a *deposited fibril structure*; §3.1b needs a *short
region in a long chain*. These are different, nearly disjoint criteria. The row type that
is exhausted for the benchmark is abundant for Φ.
