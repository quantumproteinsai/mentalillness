# Pre-registration — do modern predictors recover the experimentally mapped regions?

**STATUS: DRAFT, 15 Nov 2026. NOT YET IN FORCE.** Written by Claude, for the author to
amend, reject or ratify. Nothing in this document binds anything until §12 is signed and
the freeze commit exists.

**All three open decision points were resolved on 15 Nov 2026 by Claude, on the author's
instruction**, and each is marked **RESOLVED** at the point of use with the reasoning
attached: the combination statistic (§3.1), the handling of a FoldAmyloid
reimplementation that fails its own checks (§5.1), and the entry rule for modern
predictors (§5.2). **The author should read those three and overturn any of them — they
are judgement calls delegated, not facts established**, and a pre-registration is worth
nothing if its author has not actually agreed with it.

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

**Combination across rows — RESOLVED 15 Nov 2026, by Claude on the author's instruction.**

**Primary: Stouffer's Z**, equal weights, one-sided.
**Secondary, always reported alongside: Fisher's method**, χ² = −2 Σ ln(v_i) on 2n df.

Fisher is the conventional choice and is more powerful when one row is recovered
spectacularly and the rest are not. **That is exactly this project's recurring failure
mode** — on 15 Nov 2026 a two-protein gatekeeper claim turned out to rest on one protein
plus an excluded row (§9), and H1 is a claim about predictors *in general*, not about
there existing one region somewhere that a predictor finds. Stouffer weights rows
equally and cannot be carried by a single outlier, so it is primary.

Both are reported in every case, because a referee will expect Fisher and because a
disagreement between them **is itself informative**: Stouffer null with Fisher
significant means one row is doing all the work, and the paper must say which row.

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
the contact scale finds tau 306-311**. **RESOLVED 15 Nov 2026, by Claude on the author's instruction — and the answer is
neither of the two options originally offered.** If the reimplementation fails those
checks it is **excluded from the confirmatory legacy arm**, so that a bug in our code can
never masquerade as a 2010 tool's failure and contaminate the legacy-versus-modern
comparison. It is **reported in full anyway**, as a methods result, with the discrepancy
quantified against the paper's published figures.

Dropping it silently would hide a result; labelling it "FoldAmyloid" while unvalidated
would attribute our bug to Garbuzynskiy. The legacy arm then has **two live tools plus
one that could not be reconstructed**, which is a weaker comparison and must be stated as
one. That the method is fully specified in print and still could not be reproduced would
be the sharpest reproducibility finding available to this paper.

### 5.2 Modern generation

**AggreProt** (2024, installable Python) and **AggrescanAI** (2026, Colab + pretrained
weights), both sequence-only. Versions and commit hashes recorded in the freeze commit.

**RESOLVED 15 Nov 2026, by Claude on the author's instruction — as a rule rather than a
list**, so that the answer does not change every time a tool appears:

> **A predictor enters the confirmatory modern arm only if it is version-pinnable and
> runs locally.** Everything else is exploratory, reported separately, and excluded from
> the multiplicity correction.

That criterion is not invented here — it is this project's own finding, recorded in
`prior_computation_and_framing.md`: *"a web form is not a reproducible tool — it cannot
be version-pinned, and three of the services checked today were down or gone."* A
benchmark whose baseline evaporates between submission and review is not a benchmark, and
half the 2017 legacy set has already evaporated.

By that rule AggreProt and AggrescanAI are in, and the remaining eleven-plus PLM-era
tools from the September 2026 census are exploratory unless they ship installable
weights. **Any tool meeting the rule may be added freely before the freeze and none
after.** The novelty claim — that no PLM predictor has ever been run on DISC1 or
TRIOBP-1 — is unaffected either way, since it concerns the class, not our coverage of it.

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

### 6.3 Both Tier A rows now pass rule 5

**Updated 16 Nov 2026. Both blockers cleared in one day, each by a source this section
had not named.** The confirmatory analysis is no longer blocked on provenance.

| row | sequence | range | status |
|---|---|---|---|
| TRIOBP-1 324-348 | ~~DERIVED~~ **READ** — Zaharija 2022 Fig. 1B | **READ** — Zaharija 2022 §2.2 | **CLEARED** |
| DISC1 384-415 | **READ** — UniProt Q9NRI5, 854 aa, SV=3 | ~~unchecked~~ **READ** — Zaharija & Bradshaw 2023 preprint | **CLEARED, one caveat** |

**The caveat on DISC1, which is not a provenance problem but must travel with the row.**
The range is confirmed three ways in its source: the D region ends at 383, construct
1-383 does not aggregate while 1-415 does, and 383 + 32 = 415 matches both "these 32
amino acids were deleted" and the 32-residue UniProt string already stored. But:

1. **The source is a preprint, and the version of record is still only an abstract.**
   *Prog Neuropsychopharmacol Biol Psychiatry* **130**:110923, PMID 38135095. Its
   **abstract was read 16 Nov 2026** and confirms the claim survived peer review
   unchanged in substance — none of D, I, S or C aggregates alone, D+I+linker does,
   "a region of approximately 30 amino acids ... is critical for aggregation, and
   deletion of this region is sufficient to abolish the aggregation propensity".

   **It cannot close this item, and the reason is exact.** Both abstracts say only
   "approximately 30 amino acids". The claim we carry is **384-415 = 32 residues**,
   which appears nowhere in either abstract. And the case needing exclusion is a
   **one-residue** change at the C-terminal boundary — the preprint's body text wrote
   Δ384-**414** three times against Δ384-**415** in its figures. "Approximately 30" is
   equally consistent with 30, 31 and 32, so the abstract reads identically whichever
   way review resolved that slip. **Only the full text or its Figure 5 settles it.**
   This remains the only §6.3 item, it is a one-residue re-check, and it is now
   quantified rather than open-ended.
2. **The paper's sufficiency claim overreaches its constructs, and §6.2's `construct`
   rule is what catches it.** The Discussion says 384-415 "was both sufficient for
   aggregation", but **384-415 was never expressed alone.** What was expressed alone is
   the whole linker, **384-538** (155 aa), and **1-415**. Necessity is clean — deletion
   abolishes aggregation in 1-854, 1-836 and 1-655 alike. Sufficiency is established for
   the linker, and for 384-415 *in the context of 1-383*. **Do not state 384-415 as
   "sufficient for aggregation" in print without that qualifier.**
3. **`found_by` is clean.** Found by truncation and deletion, no aggregation predictor
   involved. The region also falls outside all four ESPRIT domains — "not found within
   any of 94 most stable DISC1 fragments" — so the structural screen missed it too.

**How the TRIOBP-1 row cleared.** Figure 1B of Zaharija et al. 2022 (*Int. J. Mol. Sci.*
**23**:11048, publisher PDF read in full) prints
`ELEKL|PLRENKRVPLTALLNQSRGERRGPP|SDGHE` beneath a 324-348 numbering row, the coloured
segment flanked by five residues either side. It reproduces the derived string
**byte-for-byte**, and two alignment checks that could have failed did not: 333-340 comes
out `LTALLNQS`, which carries zero charges and which the paper calls "the uncharged
region", and 341-345 comes out `RGERR`, which the paper calls "the cluster of charged
amino acids beginning at AA 341". **The 48.0% gatekeeper figure is no longer a
reconstruction.** Figure 12B of Bradshaw 2017 is no longer required for the letters.

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
- **The 2025 PhD thesis from the experimental group contains modern predictor runs → the
  novelty claim changes.** ~~DISCHARGED 15 Nov 2026 against Samardžija's thesis.~~
  **RE-OPENED AND PARTLY TRIGGERED, 16 Nov 2026 — THERE WERE TWO 2025 THESES.**

  Samardžija's contains no predictor runs. **Zaharija's (read in full, 16 Nov 2026) runs
  five**, in §4.3.5 on full-length DISC1 (NP_061132.2): **TANGO, AGGRESCAN, FoldAmyloid,
  MetAmyl and ANuPP**, six algorithms, default parameters, with a per-residue consensus.

  **The condition is triggered for the legacy arm and NOT for the modern arm.** No PLM, no
  AggreProt, no AggrescanAI appears. §5.2's claim — *"no PLM predictor has ever been run
  on DISC1 or TRIOBP-1"* — is **intact**, and it is the claim this document rests on. What
  changes:

  1. **The retrospective legacy comparison on DISC1 is pre-empted.** Running TANGO,
     AGGRESCAN, FoldAmyloid, MetAmyl or ANuPP on DISC1 and reporting it as new would
     reproduce a published thesis. Cite Zaharija 2025 for it instead.
  2. **Their result strengthens H1 rather than weakening it.** Four of five tools gave
     hotspots "dispersed throughout the entirety of the protein sequence"; only ANuPP
     named the linker (AA 387-395, 400-415). Legacy missed it; one 2021 tool found it.
  3. **TRIOBP-1 is still clean** on present evidence, so the legacy arm survives there.

  **Before the freeze:** restate §5.2's novelty sentence in the abstract and §1 so it says
  *PLM-era* explicitly, and add Zaharija 2025 §4.3.5 as cited prior art for the legacy
  DISC1 scores. See `STATE.md` and `reports/PDFs_to_obtain.md` item 0.

---

## 12. Freeze protocol

1. Clear §6.3. ~~Read Figure 12B~~ **— done 16 Nov 2026, via Zaharija 2022 Fig. 1B
   instead; the TRIOBP-1 sequence and range are READ.** ~~(a) settle the TRIOBP-1 minimal
   region: the thesis says **7 aa**, `regions.json` says **333-340, an 8-mer**~~
   **— SETTLED 16 Nov 2026 at EIGHT. The 2022 paper says "8 amino acids" three times
   (abstract, discussion p.13, Figure 6D legend); the thesis is wrong by one, and
   `regions.json` was right.** ~~Confirm the DISC1 384-415 range in its source~~
   **— done 16 Nov 2026 against the Zaharija & Bradshaw 2023 preprint, which IS that
   source; range confirmed three ways.** **One item left, and it is a re-check rather
   than a gap:** obtain the **full text** of Zaharija & Bradshaw **2024**
   (*Prog Neuropsychopharmacol Biol Psychiatry* 130:110923, PMID 38135095) — its
   abstract was read 16 Nov 2026 and confirms the substance but **not** the boundaries,
   since both versions' abstracts say only "approximately 30 amino acids". What is
   needed is Figure 5 or the Results: **does the published version write Δ384-414 or
   Δ384-415?** Carry the sufficiency qualifier in §6.3(2) with the row regardless.
2. ~~Read the 2025 thesis (§11).~~ **Done 15 Nov 2026 — read in full, condition
   discharged, novelty claim unchanged.**
3. ~~Settle every **[AUTHOR DECISION]**.~~ **Done 15 Nov 2026** (§3.1, §5.1, §5.2),
   delegated to Claude. **The author must still read and ratify or overturn those three**
   — delegation is not agreement, and §13 is the place it becomes binding.
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
