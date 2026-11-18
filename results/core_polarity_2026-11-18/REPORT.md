# Core polarity (Φ) — computed, 18 November 2026

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
