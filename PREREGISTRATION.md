# Pre-registration — do modern predictors recover the experimentally mapped regions?

**STATUS: DRAFT, 15 Nov 2026. NOT YET IN FORCE.** Written by Claude, for the author to
amend, reject or ratify. Nothing in this document binds anything until §12 is signed and
the freeze commit exists. Decision points the author must settle are marked
**[AUTHOR DECISION]**.

Read `STATE.md` first. This document assumes it.

---

## 1. The question

> Do modern aggregation predictors recover the experimentally mapped
> aggregation-critical regions of DISC1 and TRIOBP-1 that the 2004-2010 generation
> missed, and if not, what structural feature are they all missing?

**What is not being asked.** That the 2017-generation tools failed on these proteins is
already in print, stated by the primary papers themselves. It is cited evidence, not a
result to re-establish. Any analysis below that merely reproduces a published failure is
a positive control on our pipeline, not a finding.

## 2. Hypotheses, stated so they can fail

- **H1 (primary).** Modern sequence-only predictors rank the mapped region above chance
  within its own parent protein.
- **H0 (primary).** They do not: the mapped region's score is indistinguishable from
  that of ordinary windows of the same protein.
- **H2 (secondary).** Any failure is a *flanking-context* effect rather than core
  chemistry — i.e. the narrowed core scores positive in isolation and negative in
  context.
- **H3 (secondary, demoted).** Aggregation-critical psychiatric regions are
  gatekeeper-rich relative to crystallised steric zippers. **This is now n = 1 and is no
  longer a primary claim** — see §9.

---

## 3. The statistic, and why a hit/miss criterion is forbidden

**A binary "did it flag the region?" criterion is uninformative and must not be used.**
Computed on our own proteins `[COMPUTED 15 Nov 2026]`, the probability that a predictor
calling a fraction *f* of residues positive **at random** overlaps the mapped region at
least once:

| protein | length | region | f = 0.05 | f = 0.10 | f = 0.20 | f = 0.30 |
|---|---|---|---|---|---|---|
| TRIOBP-1 | 652 | 25 aa | 63.8% | 86.9% | 98.3% | 99.8% |
| DISC1 | 854 | 32 aa | 74.6% | 93.6% | 99.6% | 100.0% |

At any realistic call rate a random predictor "recovers" either region essentially
always. **Rank is mandatory.**

A naive rank threshold is not much better: for a 20-window region in a ~650-window
protein, the chance that its best window lands in the top 1% is **18.2%**, top 5%
**64.2%** `[COMPUTED]`. So the threshold must be calibrated against a null that accounts
for region length.

### 3.1 The pre-registered primary statistic

For each row *i* (one mapped region in one protein) and each predictor:

1. Score every window of the protein at the predictor's own native window size (§5.3).
2. Let **M** = number of windows in the protein, **m** = number of windows wholly inside
   the mapped region.
3. Let **P** = (number of windows scoring **≤** the region's best-scoring window) / M.
   Ties resolved by the **midrank** convention.
4. Define **v = 1 − P^m**.

Under H0 (the predictor carries no information about this region), the region's *m*
windows are an exchangeable subset, the best-of-*m* percentile has CDF *x^m*, and
therefore **v ~ Uniform(0, 1)**. Small *v* means the region scored high — the predictor
succeeded.

This transformation is the reason for the whole construction: it makes a 25-residue
region in a 652-residue protein and a 32-residue region in an 854-residue protein
directly comparable, with no tuning.

**Combination across rows:** Fisher's method, **χ² = −2 Σ ln(v_i)** on 2n degrees of
freedom, one-sided. **[AUTHOR DECISION]** Fisher weights small *v* heavily and is the
conventional choice; Stouffer's Z weights rows equally. Fisher is pre-registered unless
the author substitutes Stouffer here, in writing, before the freeze.

### 3.2 The legacy-versus-modern comparison

The generations are run on **the same rows**, so the comparison is **paired**:
Wilcoxon signed-rank on per-row *v*, modern against legacy, one-sided (modern better).
Reported with the median paired difference and its 95% CI, never as a bare p-value.

---

## 4. Success thresholds, fixed now

| | threshold |
|---|---|
| A single row counts as **recovered** by a predictor | **v < 0.05** |
| A predictor counts as **succeeding on the set** | Fisher combined p **< 0.01** across the confirmatory rows |
| Modern counts as **beating legacy** | Wilcoxon one-sided p **< 0.05** *and* median paired Δv **< −0.10** |
| Multiplicity across predictors | **Benjamini-Hochberg at q = 0.10**, applied across all predictors within each family (legacy, modern), reported alongside raw p |

The effect-size floor on the paired comparison is deliberate: a significant p with a
median Δv of −0.01 is a null result with a small standard error, and this project does
not report those as findings.

---

## 5. The predictors, frozen

### 5.1 Legacy generation (the 2017 baseline)

| tool | status 15 Nov 2026 | how it will be run |
|---|---|---|
| **TANGO** | live, `tango.crg.es` | web, settings recorded verbatim |
| **AGGRESCAN** | live, `andromeda.uab.cat/bioinf/aggrescan/` | web, settings recorded verbatim |
| **FoldAmyloid** | **server dead**, method fully specified | **reimplemented** from Garbuzynskiy 2010 + the scales in Galzitskaya 2006b |
| **ProA** | **dead, HTTP 404, no replacement** | **cannot be run. Recorded as unavailable, not as a failure.** |

**The FoldAmyloid reimplementation is itself a pre-registered object.** It must reproduce
the paper's own published checks before it may score our rows: the reported 80%/72%
sensitivity/specificity on its 407-peptide set, and the protein-level result that **only
the contact scale finds tau 306-311**. If it cannot reproduce those, it is not
FoldAmyloid and must be reported as "FoldAmyloid, reimplemented, unvalidated" or dropped.
**[AUTHOR DECISION]** Which of those two.

### 5.2 Modern generation

**AggreProt** (2024, installable Python) and **AggrescanAI** (2026, Colab + pretrained
weights), both sequence-only. Versions and commit hashes recorded in the freeze commit.
**[AUTHOR DECISION]** Whether to add further PLM-era tools. Adding tools after unblinding
is forbidden; adding them before the freeze is free.

### 5.3 Window size and score normalisation

Each predictor is scored at **its own native window**: FoldAmyloid 5, Waltz/3D-profile
6, TANGO and AGGRESCAN per-residue (aggregated to 6-residue means), PLM tools per-residue
(aggregated to 6-residue means). **The statistic in §3.1 is invariant to window size by
construction**, which is why no cross-predictor rescaling is applied. Raw per-residue
outputs are archived.

---

## 6. The validation set, and what may enter it

### 6.1 Two tiers, never pooled

- **Tier A — confirmatory.** DISC1 and TRIOBP-1 only. This is the project's question.
  **n = 2 proteins. It is a case study, not a test** — see §7 — and must be reported as
  such regardless of outcome.
- **Tier B — powered generalisation.** Every protein with fragment-level aggregation
  mapping, psychiatric or not. This is where a real recovery rate can be estimated.

Tier A and Tier B are analysed and reported separately. **Pooling them would let a
40-row Tier B result speak for a 2-row Tier A question.**

### 6.2 Inclusion rules

A row enters the confirmatory analysis only if **all** of the following hold:

1. `found_by` records discovery by **experiment, not prediction**. Rows found by
   prediction are analysed **separately** and never pooled (§8).
2. `construct` is recorded. A region may be necessary in one construct and dispensable in
   another, and **both results are correct**; a benchmark that ignores this scores against
   a moving target.
3. The **sequence** has been read from a primary source or a database, not inferred.
4. The **residue range** has been checked against the frame recorded in `_numbering`.
5. `verified_against_publisher_pdf` is **true**.

### 6.3 Both Tier A rows currently fail rule 5

**The confirmatory analysis cannot run today.** Stated plainly because it is the single
most actionable item in this document:

| row | sequence | range | blocker |
|---|---|---|---|
| TRIOBP-1 324-348 | **DERIVED** from UniProt Q9H2D6, printed only in Figure 12B | from the source paper | **read Figure 12B** |
| DISC1 384-415 | **READ** from UniProt Q9NRI5 REST, 854 aa, SV=3 | from the source paper, **unchecked** | **confirm the range in the source** |

UniProt confirms DISC1's *letters*; it does not confirm that 384-415 is the right range.

### 6.4 Exclusions fixed now

- **DISC1 716-761 is excluded** from every analysis in this document. Its `found_by` is
  "RADAR sequence-repeat search" — found *by* a sequence search — and `regions.json`
  records it as a **docking restraint, not a measurement**. Including a predicted region
  in a benchmark about prediction failure is the error this project exists to avoid.
- **No bulk import from CPAD.** TANGO, CamSol and AGGRESCAN were trained on sequences
  within it; importing without per-row provenance checks reproduces the out-of-sample
  violation that the CANYA paper names.
- **Provenance cannot be grepped.** Circularity is protein-specific, not lab- or
  era-specific. Every row is read before it enters.

---

## 7. The power problem, computed rather than asserted

95% Wilson intervals on a recovery rate `[COMPUTED 15 Nov 2026]`:

| n rows | at p̂ = 0.50 | width | at p̂ = 0.80 | width |
|---|---|---|---|---|
| **2** | [0.09, 0.91] | **0.81** | [0.34, 1.00] | **0.66** |
| 10 | [0.24, 0.76] | 0.53 | [0.49, 0.94] | 0.45 |
| **15** | [0.30, 0.75] | 0.45 | [0.55, 0.93] | 0.38 |
| 25 | [0.30, 0.67] | 0.36 | [0.61, 0.91] | 0.30 |
| 40 | [0.35, 0.65] | 0.30 | [0.65, 0.90] | 0.24 |

- **At n = 2 the interval spans almost the whole unit line.** Tier A cannot estimate a
  rate. It can only show that a specific, named, published failure does or does not
  persist — which is worth reporting, and is a case study.
- **n = 11** is the smallest set at which an observed 80% recovery excludes 50%.
- **n = 15 per arm** separates a legacy 20% from a modern 70% at 80% power, α = 0.05.

**The floor of 15 in `CLAUDE.md` is therefore not arbitrary — it is the number this
design needs, and it is confirmed independently by both calculations.** Tier B is not
optional; without it there is no quantitative claim.

---

## 8. Rows found by prediction

Analysed separately, reported separately, never pooled. They are not useless: they
measure **how well a predictor reproduces a region another predictor found**, which
bounds the circularity in the published literature. They cannot speak to H1.

---

## 9. The gatekeeper analysis is demoted, with its reason

`STATE.md` called the gatekeeper inversion "the paper's spine". On 15 Nov 2026, with the
clean DISC1 row supplied from UniProt:

```
crystallised steric zippers   0.0% – 16.7%   (n = 7)
TRIOBP-1 324-348                    48.0%
DISC1    384-415                    18.8%     +2.1 points above the WORST zipper
```

The reported "48.0% to 50.0% (n = 2)" was TRIOBP-1 plus the excluded 716-761 row. **The
separation does not generalise.** H3 is therefore **n = 1**, pre-registered as a
**secondary, descriptive observation**, and may not be stated as a two-protein result.

What is untouched is the **prediction failure at n = 2**: both regions were found by
truncation, neither by prediction, and the predictors missed both. These are two claims
with two different n and must never be written as one number.

---

## 10. Secondary analyses, each with its decision rule fixed

**10.1 The context test (H2).** Score `LTALLNQS` (TRIOBP-1 333-340, 0% gatekeeper) in
isolation and in its 25-residue context.
- Positive in isolation, negative in context → **the failure is flanking context.**
- Negative in both → **intrinsic core chemistry.**
- Positive in both → the region-level miss is a thresholding artefact, not a chemistry
  failure, and the paper changes.

These are three different papers. The decision rule is fixed **now**, before scoring.

**10.2 Window-level versus region-level.** Report *v* (region-level, primary) alongside
the **minimum per-window *v* inside the region**. TRIOBP-1 324-348 contains hexapeptide
windows at **0.0% gatekeeper**, and 7 of its 20 windows are at or below the worst
crystallised zipper `[COMPUTED]`. If a window-scanning predictor misses a region that
contains a zipper-grade window, that is a **harder** failure than "uninformative by
construction", and the draft should claim the harder one.

**10.3 The legacy baseline is itself a finding.** Of four 2017 tools, two are live, one
is dead, and one requires reimplementation. Reported regardless of outcome.

---

## 11. What would falsify the project's thesis

Stated so it cannot be quietly avoided:

- Modern predictors rank both Tier A regions at **v < 0.05** → the premise is wrong, the
  paper becomes "modern predictors fixed it", and that is publishable.
- The FoldAmyloid reimplementation fails its own published checks → the legacy arm is
  two tools, not three, and the comparison weakens.
- Tier B recovery rates for legacy and modern are **indistinguishable within their CIs**
  → there is no generational effect, and the paper is about hexapeptide training, not
  about progress.
- The 2025 PhD thesis from the experimental group contains modern predictor runs → the
  novelty claim changes. **This is a Tier 0 obtain-list item and must be read before the
  freeze.**

---

## 12. Freeze protocol

1. Clear §6.3: read Figure 12B, confirm the DISC1 range.
2. Read the 2025 thesis (§11).
3. Settle every **[AUTHOR DECISION]**.
4. Record predictor versions, commit hashes and web-form settings.
5. Commit this file with the SHA-256 of `data/regions.json` recorded in the commit
   message. **That commit is the freeze.**
6. Only then run a predictor.

**Amendments** after the freeze are permitted, made as commits to this file, each stating
what changed, why, and **whether any score had been seen at the time**. An amendment made
after unblinding is an exploratory analysis and is reported as one.

**`scripts/prescreen.py`-style gate:** no manuscript may cite a row whose
`verified_against_publisher_pdf` is false.

---

## 13. Signature

- Pre-registration ratified by: ____________________  date: __________
- `data/regions.json` SHA-256 at freeze: ____________________
- Tier A rows at freeze: ____  Tier B rows at freeze: ____
