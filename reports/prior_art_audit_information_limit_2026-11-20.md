# Prior-art audit: the information-limit claim (m/M as a pre-run admission bound)

Date: 2026-11-20. Auditor: agent. Scope: the four sub-claims A-D as handed over.
Nothing outside this file was modified.

Provenance grades used throughout: **[READ]** = I opened the source and read the
passage; **[SNIPPET]** = appeared only in a search result or secondary summary;
**[EMPTY]** = structured query returned nothing relevant, verbatim query given;
**[COMPUTED]** = I calculated it here from stated inputs.

---

## 0. Search-engine calibration (do not skip; it invalidates one obvious shortcut)

Negatives are only worth publishing if the engine was working. Two calibrations:

- Europe PMC **has no `FULL_TEXT:` field**. Queries of the form
  `FULL_TEXT:"steric zipper"` and `FULL_TEXT:"Tarone"` both return
  **hitCount 0**, while `ABSTRACT:"steric zipper"` returns 148. **[READ]**
  Any audit that reported `FULL_TEXT:`-fielded zeros as evidence reported
  artefacts. I discarded four such queries of my own.
- Unfielded quoted queries *do* reach full text and *do* honour the phrase at
  the long end: `"purple elephant chromatography of narwhals"` -> 0,
  `"narwhal attainable p-value"` -> 0, `"minimum attainable p-value"` -> 28. I
  verified one of the 28 by downloading the article full text and grepping it:
  PMC13672667 genuinely contains the string. **[READ]**
  But the matching is **not reliably strict**: PMID 42589097 (strawberry
  rhizosphere) is returned for the same phrase and its downloaded full text
  contains `attainable` **0 times**. **[READ]** So non-zero Europe PMC hitCounts
  are an *upper bound* and were screened by hand; zeros are trustworthy.
- `"minimum attainable p-value"` is in common use, but almost entirely for a
  *different* quantity: the resolution floor `1/(nperm+1)` of a permutation
  test. That accounts for the junk in the 28. It is not our quantity and should
  not be cited as prior art for it.

---

## 1. Premise audit (the caller's own numbers)

I reproduced every number given, from the two integers, before touching the
literature.

All 15 quoted values are **exactly** `m/M` for integers consistent with
`M = floor(L/W)`, `W = 6`, and a **fixed-phase** tiling (windows `[6k+1 .. 6k+6]`,
region window counted only if wholly inside). **[COMPUTED]**

| row | m | M | m/M | floor_v = 1-((M-0.5)/M)^m |
|---|---|---|---|---|
| TMEM106B | 22 | 45 | 0.4889 | 0.2179 |
| serum amyloid A | 8 | 17 | 0.4706 | 0.2124 |
| TRIOBP-1 60-189 | 21 | 108 | 0.1944 | - |
| DISC1 691-836 | 24 | 142 | 0.1690 | - |
| TAF15 | 15 | 98 | 0.1531 | - |
| hnRNPA1 | 7 | 53 | 0.1321 | 0.0642 |
| FUS | 8 | 87 | 0.0920 | **0.0451** |
| TRIOBP-1 1-59 | 9 | 108 | 0.0833 | 0.0409 |
| ANXA11 | 5 | 84 | 0.0595 | 0.0294 |
| TRIOBP-1 324-348 | 4 | 108 | 0.0370 | 0.0184 |
| DISC1 384-414 | 5 | 142 | 0.0352 | 0.0175 |

- FUS at `m/M = 0.0920` but `floor_v = 0.0451` is the arithmetic that makes
  "13 of 23 by m/M, 9 of 23 by floor_v" internally consistent. It checks out.
- "about twice as strict": `floor_v` crosses 0.05 between `m/M = 0.100`
  (m=10, M=100, floor_v 0.0489) and `m/M = 0.110` (m=11, M=100, floor_v 0.0536).
  So the crossing is at `m/M ~ 0.103`. The factor is 2.05. **[COMPUTED]** Correct
  as stated.
- Independent cross-check of the tiling convention, not just the arithmetic:
  TMEM106B, chain 274 aa, published ordered core 120-254, gives M=45, m=22,
  `m/M = 0.4889` on the nose. **[COMPUTED]**, core boundaries **[SNIPPET]**.
- CHCHD2 `0.2000` is the only value that does not resolve to an `m/M` with
  `M = floor(139/6) = 23`; it resolves as 4/20, 5/25, etc. Either the construct
  is not the 139-aa canonical chain or the row uses a different length. Worth one
  line of checking before the number goes in an abstract. **[COMPUTED]**

### 1.1 Two premise findings that change how the claim must be worded

**(i) The limit belongs to the statistic, not to the data.** `m/M` is the floor
only for tests whose single input is the *rank of the region's best window*.
Using all `m` in-region ranks instead of just the best one, the smallest
attainable p of an exact rank test is `1/C(M,m)`: **[COMPUTED]**

| row | min p from best window | min p from all m ranks |
|---|---|---|
| DISC1 384-414 | 0.0352 | 2.2e-09 |
| TRIOBP-1 324-348 | 0.0370 | 1.9e-07 |
| serum amyloid A | 0.4706 | 4.1e-05 |
| TMEM106B | 0.4889 | 2.4e-13 |
| TRIOBP-1 60-189 | 0.1944 | 8.1e-23 |

Every row the claim declares untestable becomes testable, by orders of
magnitude, under a statistic that reads all the windows in the region rather
than the best one. The information limit is real but it is **self-inflicted by
the choice of a max-statistic**, and the rows with the *worst* `m/M` are
precisely the rows with the *most* escape room. This must be in the paper, in
the paper's own voice, or a referee will put it there.

**(ii) "exactly m/M" is exact by construction of the null, not as a fact about
predictors.** It needs window scores exchangeable along the chain under H0.
Real TANGO/AggrescanAI profiles are smoothed and composition-driven, so the
exchangeability is a property of the registered permutation null, not of the
predictors. The statement is fine; the word "exactly" needs the null named in
the same sentence.

---

## 2. Sub-claim A - testability bound applied to aggregation-predictor benchmarking

### Reproducible negatives (verbatim queries)

- arXiv `all:"minimum attainable p-value" AND all:"benchmark"` -> **0** **[EMPTY]**
- arXiv `all:"amyloid" AND all:"predictor" AND all:"statistical power"` -> **0** **[EMPTY]**
- arXiv `all:"aggregation-prone regions" AND all:"benchmark"` -> **0** **[EMPTY]**
- arXiv `all:"Tarone" AND all:"benchmark design"` -> **0** **[EMPTY]**
- Europe PMC `ABSTRACT:"aggregation" AND ABSTRACT:"predictor*" AND ABSTRACT:"benchmark*" AND ABSTRACT:"statistical power"` -> **0** **[EMPTY]**
- Europe PMC `("aggregation-prone" OR amyloid) AND "minimum attainable p-value"` -> 1 hit, PMID 42941218, dairy-cow metabolomics; irrelevant on title **[READ title]**
- Europe PMC `"best-scoring window" AND (amyloid OR aggregation)` -> 1 hit, PMID 40662825 (amyloid signalling motifs, deep learning); not a testability bound **[READ title]**
- Europe PMC `"aggregation-prone region" AND "expected by chance"` -> 3 hits, all reviews/abstract books, none a per-region bound **[READ titles]**
- Europe PMC `(amyloid OR "protein aggregation") AND "Tarone" AND "p-value"` -> 40 hits, all surname-collision / loose-match noise on inspection of the first 6 **[READ titles]**

### The strongest positive control available

Singh J, Jangid R, Srivastava A, *AmyloCore-ML*, bioRxiv
`10.64898/2026.09.25.754455`, v1 1 Oct 2026, v2 12 Oct 2026, Univ. of Denver.
I downloaded and parsed the v1 JATS source. **[READ]** This is the most recent
benchmark of a 2026-generation aggregation predictor against structurally
mapped regions. Occurrences in its full text: `power` **0**, `chance` **0**. It
computes AUROC/AUPRC and a mean peak distance, and never asks whether a given
protein could have produced a significant result.

Also to be engaged with, not a pre-emption: Stapor K, Lewandowska A, Fabian P,
Roterman-Konieczna I, *AmyloPick*, Proteins 2026, doi 10.1002/prot.70094.
**[READ abstract]** Its declared key contribution is "the statistical
methodology that enables a rigorous performance assessment and direct
comparison with other classifiers", but the methodology is classifier-vs-
classifier significance on AGM / accuracy / SOV metrics, not a per-instance
attainable-p bound. A referee in this field will ask why the manuscript does not
cite it.

### Verdict A: **NOVEL**

No reachable source computes a minimum-attainable-p or per-instance testability
bound for aggregation or amyloid predictor evaluation. Strength of the negative:
good (9 queries, 2 independent engines, one calibrated positive control read in
full). Weakness: the result is novel the way "nobody has divided two integers in
this context" is novel - see section 6.

---

## 3. Sub-claim B - a per-instance testability bound in computational-biology / ML benchmarking

This is where the pre-emption lives, and it does live here. Three findings,
ordered by how much they hurt.

### B1. Malekpouri M, Lotfi S, arXiv:2611.15555, submitted 11 Nov 2026, cs.LG **[READ abstract; READ extracted passages of the HTML full text]**

*"What Conformal Selection Can Certify in CRISPR Off-Target Design: Benchmark
Leakage, Free Baselines, and a Finite-Sample Cohort Requirement."*

Verbatim from the abstract: **"The constraint is arithmetic: a conformal p-value
cannot fall below one divided by the calibration cohort size plus one, so a
Benjamini-Hochberg selection certifies a single candidate only when that cohort
is at least the candidate pool size divided by the tolerated error rate. Public
cohorts supply ten validated guides, whereas a pool of two thousand at a ten
percent error rate needs twenty thousand; the accepted set is consequently empty
in over ninety-six percent of splits."**

From the body: *"Proposition 2 explains this without reference to the oracle:
with n_cal <= 7 the smallest attainable p-value is >= 0.125, while BH requires
p_(k) <= qk/m. Fig. 1(b) turns the bound into a design calculation."*

This is, in a computational-biology benchmark paper nine days older than this
audit: a minimum-attainable-p-value floor; derived from two integers (cohort
size, candidate pool size) plus alpha; shown to make a significant/certified
result impossible for the data that exist; and explicitly converted into a
**pre-run design calculation**. The word "arithmetic" is used for the same
rhetorical purpose the caller uses it for.

What distinguishes the caller's claim from it, exactly and only: B1's bound is
**dataset-level** (one bound for the whole benchmark, from cohort and pool
sizes); the caller's is **row-level** (one bound per benchmark instance, from
that instance's own geometry, used to admit or reject that instance while
keeping the rest). That is a real difference and it is thin.

### B2. Zhuang Z, Li Y, Fan Z, arXiv:2605.28873, submitted 25 May 2026 **[READ abstract]**

*"Pre-Registering the Detectable Effect: A Paired-MDE Budget for 4-bit
Quantization Benchmarks, with a Pilot Audit."* Verbatim: *"The bound turns 'how
reliable is my quantization claim?' into a one-line budget a benchmark designer
can commit to before running."* Conclusion: all observed deltas fall below the
implied MDE.

This pre-empts the *framing* - a one-line arithmetic detectability budget,
pre-registered, committed to by a benchmark designer before running - in ML
rather than biology, and via MDE/power rather than attainable-p.

### B3. Su Z, Zhang T, arXiv:2611.22434, submitted 17 Nov 2026 **[READ abstract]**

A five-layer benchmark measurement audit in which *"the decoding layer sets the
MDE at |r| = 0.599 at the multi-feature Bonferroni threshold (alpha = 0.00714,
power 0.80), and the observed r = +0.080 has power 0.00"* - i.e. a detectability
bound used to rule that a benchmark reading is unobtainable, with injection
experiments on both sides of the bound.

### B4. Card D, Henderson P, Khandelwal U, Jia R, Mahowald K, Jurafsky D, EMNLP 2020 **[SNIPPET]**

*"With Little Power Comes Great Responsibility."* Computes MDE / power for NLP
benchmark datasets, concludes many are too small to separate competing systems,
and recommends power analysis *prior* to evaluation. I did not open the PDF;
graded SNIPPET and must not be cited as read. Dataset-level, not item-level.

### B5. The useful negative on the other side

Weber LM et al., *Essential guidelines for computational method benchmarking*,
Genome Biology 2019 (PMC6584985). I downloaded the full JATS text and grepped
it. **[READ]** Occurrences: `statistical power` **0**; `discriminat*` **0**. The
canonical benchmarking guidance in this field contains no notion of per-instance
or per-dataset testability. Its dataset guidance is about "number and types of
datasets to include", not about whether a dataset can yield a result.

Further negatives, verbatim: Europe PMC `"cannot yield a significant" AND
"benchmark"` -> 1 hit, a 2008 AI journal paper on probabilistic networks,
irrelevant **[READ title]**; `"uninformative targets" AND ("CASP" OR "CAFA" OR
"benchmark")` -> 1 hit, a conference abstract book **[READ title]**;
`"discriminative power" AND "benchmark targets"` -> 2 hits, both about docking /
contact prediction performance, neither a bound **[READ titles]**; arXiv
`all:"uninformative" AND all:"benchmark items"` -> **0** **[EMPTY]**.

### Verdict B: **PRE-EMPTED in substance; NOVEL only in granularity**

Pre-empted by **arXiv:2611.15555** (11 Nov 2026) for "compute an arithmetic
floor on the attainable p-value from dataset sizes, show the benchmark cannot
return a significant result, and turn the floor into a pre-run design
calculation, in computational biology", and by **arXiv:2605.28873** (25 May
2026) for "pre-register a one-line detectability budget before running a
benchmark". What survives is the per-row application: admitting or rejecting
*individual benchmark instances* by a bound computed from each instance's own
geometry. I found nothing doing that, but I cannot certify the ML-benchmark item
literature exhaustively (section 7).

Note on priority rather than precedence: 2611.15555 is nine days old and
2611.22434 three days old. These are not papers that scooped a long-standing
idea; they are a cluster of near-simultaneous 2026 preprints converging on the
same move. That is itself the finding: the move is in the air, and a manuscript
whose sole contribution is this move needs to cite all three and say precisely
what is left.

---

## 4. Sub-claim C - prospective recruitment / inclusion criterion

- The significant-pattern-mining lineage uses the bound **at analysis time**, as
  a search-space pruning and multiplicity device. A secondary summary of that
  literature states it as *"if the minimum attainable P-value of the association
  test for feature subset S is above the corrected significance threshold, there
  is no need to inspect the inner cell counts; the test cannot possibly yield a
  significant result"*, and separately that *"keeping only those tests whose
  minimum attainable P-value is smaller than the threshold does not modify the
  null distribution"*. **[SNIPPET]** - this is a secondary paraphrase of a
  pattern-mining paper I did not open; per the project's rule 2 it must not be
  attributed to a named originator on this evidence. The originating attribution
  the project already holds (Gart/Chu/Tarone 1979; Mantel 1980 crediting Tukey)
  stands and is not improved by anything I found.
- Design-time use **does** exist in adjacent statistics: exact tests for
  multiple binary endpoints compute attainable significance levels at the design
  stage (arXiv:1612.07561) **[SNIPPET]**; clinical-trial and GSEA practice
  impose size-based inclusion rules (GSEA FAQ: gene sets "should optimally
  contain between 15 and 500 genes") **[SNIPPET]**, though the stated rationale
  is reliability, not attainable p.
- arXiv:2605.28873 (B2) is explicitly pre-registration-before-running, at
  benchmark rather than row level. **[READ abstract]**
- Reproducible negative: Europe PMC `"testability" AND "benchmark" AND
  ("predictor" OR "method comparison")` -> 27 hits, none on topic on inspection
  of the first 8 **[READ titles]**; arXiv `all:"item response theory" AND
  all:"benchmark" AND all:"discrimination"` -> 16 hits, all response-based item
  calibration (IRT from observed model responses), none computing an a-priori
  bound from item geometry **[READ titles]**.

### Verdict C: **UNCERTAIN, and the weakest of the four**

Nothing found that uses the bound at recruitment time for dataset rows. But the
claim as written is a claim about *purpose*, and the arithmetic is admitted to
be Gart/Mantel/Tukey's. A purpose is not a result unless something follows from
it that does not follow from the analysis-time version. One thing does follow
and should be the actual claim: because the rows are rejected *before the source
paper is read*, the rejection cannot be influenced by the row's outcome, so the
admitted set is outcome-independent in a way an analysis-time filter is not.
That is a defensible, narrow, checkable statement. "We did it earlier in the
workflow" is not.

---

## 5. Sub-claim D - cryo-EM fibril cores systematically ineligible

### CONTRADICTED in the broad form, by a paper the repository does not know about

Singh J, Jangid R, Srivastava A, *AmyloCore-ML: AI/Machine Learning Enabled
Identification of Amyloid Fibril Core Regions Using Protein Language Models*,
bioRxiv `10.64898/2026.09.25.754455` (v1 1 Oct 2026, v2 12 Oct 2026). I parsed
the full v1 JATS source. **[READ]**

- Amyloid Atlas, **n = 797 entries as of April 2026**; de novo and synthetic
  assemblies excluded; yields **82 continuous core regions from 69 proteins**.
- Ordered residues = core (positives); **unresolved residues sampled from the
  same proteins** = matched non-core controls; three independently balanced 1:1
  datasets B1-B3 at window sizes W9/W15/W21.
- Head-to-head on the same core annotations: **CrossBeta** residue AUROC 0.718,
  AUPRC 0.659, mean peak distance 22.7 residues; **AggrescanAI** AUROC 0.719,
  AUPRC 0.621, larger mean peak distance; their best model (ESM-2/ExtraTrees
  W21) AUROC 0.833, AUPRC 0.751, mean peak distance 12.4 residues.
- Occurrences of `power` and `chance` in the full text: **0 each**.

So cryo-EM fibril cores are, right now, serving as predictor-benchmark material
at scale, for **AggrescanAI specifically** - the caller's own modern arm - using
a within-protein matched-control design that is structurally immune to the
core-length / chain-length ratio. "The fastest-growing source of mapped regions
cannot serve as benchmark material" is false as a statement about the material.

Grep of the working tree confirms `AmyloCore`, `Amyloid Atlas` return nothing in
`STATE.md`, `data/regions.json`, `data/references_to_check.json`. **[READ]** The
only `CrossBeta` hit is an unrelated internal note. This paper is new to the
project and it overlaps the project's own territory.

### The narrow form is arithmetically true, and I strengthened it

`m/M <= 0.05` requires the mapped region to be at most ~5% of the chain:
`m = 1` needs `L >= 120`, `m = 5` needs `L >= 600`. **[COMPUTED]** Against the
two canonical cryo-EM cores (core boundaries **[SNIPPET]**, lengths and
arithmetic **[COMPUTED]**):

- tau 2N4R, L = 441, PHF core 306-378: M = 73, m = 12, `m/M = 0.1644` - ineligible.
- alpha-synuclein, L = 140, core 37-99: M = 23, m = 10, `m/M = 0.4348` - ineligible.
- TMEM106B, L = 274, core 120-254: M = 45, m = 22, `m/M = 0.4889` - ineligible.

Neither tau nor alpha-synuclein could ever enter this benchmark. That is a
sharper illustration than "1 of 13" and costs nothing to state.

### Verdict D: **CONTRADICTED as written; NOVEL and true if rescoped**

Contradicted by Singh et al. 2026 as a claim about fibril cores. True as a claim
about *this statistic's* admission rule. Rescope or drop.

---

## 6. The narrowest true statement left

> For any benchmark whose per-region statistic depends on the experimentally
> mapped region only through the rank of its single best-scoring window among the
> `M = floor(L/W)` non-overlapping windows of the chain, the exchangeability null
> fixes the smallest attainable p-value at `m/M`, where `m` is the number of
> windows wholly inside the region; a row with `m/M > alpha` is therefore
> untestable for every predictor, this is computable from two integers before any
> predictor is run or any source paper is read, and on 23 curated
> aggregation-critical regions it excludes 13 - including every region that is
> the ordered core of a cryo-EM fibril structure but one, because an ordered core
> is a large fraction of a short construct while admissibility requires the
> region to be at most ~5% of the chain.

Every clause of that sentence is reproduced or verified above. Note what it does
**not** say: it does not say the regions are untestable, only that they are
untestable *by best-window-rank statistics*; and it does not claim the
arithmetic, only the application.

## 7. The sentence a hostile referee will use, per surviving claim

- **A (aggregation application):** "The result is that `m/M` is the probability a
  uniformly chosen window lands in a region occupying `m/M` of the chain; the
  authors have rediscovered the definition of a null hypothesis and applied it to
  eleven proteins."
- **B (benchmark-design bound):** "Malekpouri and Lotfi (arXiv:2611.15555, 11
  Nov 2026) already derive an arithmetic minimum-attainable-p floor for a
  computational-biology benchmark, show the certified set is empty in 96% of
  splits, and turn the floor into a pre-run design calculation; moving the same
  bound from the dataset to the row is a change of index, not a contribution."
- **C (prospective recruitment):** "Gart et al. (1979) excluded hypotheses that
  could not reach alpha; doing so before rather than after reading the source
  paper changes the authors' workflow, not the statistics, and no property of the
  resulting estimator is shown to depend on the order."
- **D (fibril cores):** "Singh et al. (bioRxiv 2026) benchmark AggrescanAI and
  CrossBeta against 82 cryo-EM core regions from 69 proteins with a within-
  protein matched control, so fibril cores plainly can serve as benchmark
  material; the reported ineligibility is a property of the authors' own
  max-statistic, which a rank test over all `m` in-region windows would reduce
  from p_min = 0.49 to p_min = 2e-13 on the same data."

The last of those is the one to worry about. It is correct, it is cheap to
verify, and it says the only surviving contribution is a limitation of a
statistic the authors chose.

## 8. Most dangerous remaining unknowns, and what settles each

1. **Does the max-statistic survive its own limit?** If the registered `v` is
   replaced by a statistic reading all `m` in-region ranks, the information
   limit vanishes and with it the contribution. Settled by: a paragraph in the
   manuscript justifying the max-statistic on grounds independent of the result
   (e.g. that a predictor is *used* by reading its top peak), written before any
   re-scoring. If no such justification exists, stop - this is the "stop" case.
2. **Is the admissible population large enough to exist?** Admission requires
   region <= ~5% of chain. Tau, alpha-synuclein and every cryo-EM core but one
   are out. Settled by: screening Singh et al.'s 82 regions / 69 proteins
   (Amyloid Atlas, n = 797, April 2026) for `m/M <= 0.05` - two integers per row,
   no PDFs needed. If that yields ~0 admissible rows, the 15-row floor is
   unreachable by this route and that is a publishable negative in itself.
3. **Is the per-row-versus-per-dataset distinction defensible?** Settled by
   reading arXiv:2611.15555 in full (open access, free) and arXiv:2605.28873,
   and writing the one sentence that says what the row-level version buys. If
   that sentence cannot be written, B collapses into B1.

## 9. Sources I could not open, ranked by what changes if the caller opens them

1. **Card et al., EMNLP 2020, "With Little Power Comes Great Responsibility"**
   (free: aclanthology.org/2020.emnlp-main.745). If it already frames per-dataset
   MDE as an admission criterion for benchmark *items*, sub-claim B weakens
   further. Everything I have on it is **[SNIPPET]**.
2. **AmyloCore-ML v2** (bioRxiv returned HTTP 429; I read the **v1** JATS source
   instead). v2 reportedly adds residue-level comparison text. If v2 contains a
   statement about core length relative to construct length, D becomes fully
   pre-empted rather than merely contradicted.
3. **AmyloPick, Proteins 2026, doi 10.1002/prot.70094** (paywalled). Its
   "statistical methodology for rigorous performance assessment" of APR
   prediction is the nearest thing in the aggregation field to an evaluation-
   methodology contribution; if it contains any attainable-p or power argument,
   sub-claim A is pre-empted inside the caller's own field.
4. **Gart, Chu & Tarone 1979, JNCI 62:957-974** (not open). Does not affect the
   verdicts - the project already read Tarone 1990 and holds the attribution -
   but it is the paper the originator claim rests on, and it is currently
   attributed on the strength of Tarone's own introduction rather than on the
   1979 text.
5. **arXiv:1612.07561, "Optimal exact tests for multiple binary endpoints"**
   (free; I read only a secondary summary). Relevant to C: if it computes
   attainable significance levels at the *design* stage, C's purpose-novelty
   narrows again.

---

## Verdict table

| Sub-claim | Verdict | By what |
|---|---|---|
| A - testability bound for aggregation/amyloid predictor benchmarking | **NOVEL** | 9 calibrated EMPTY queries across 2 engines; AmyloCore-ML full text has 0 occurrences of `power`/`chance` |
| B - per-instance testability bound in comp-bio / ML benchmarking | **PRE-EMPTED in substance** | arXiv:2611.15555 (11 Nov 2026) attainable-p floor as pre-run design calculation; arXiv:2605.28873 pre-registered one-line detectability budget. Novel only at row-level granularity |
| C - prospective recruitment criterion | **UNCERTAIN** | No instance found at data-collection time; but the claim is about purpose and the arithmetic is conceded to Gart/Mantel/Tukey |
| D - cryo-EM cores systematically ineligible | **CONTRADICTED as written** | Singh et al., bioRxiv 10.64898/2026.09.25.754455: 82 core regions / 69 proteins used to benchmark AggrescanAI and CrossBeta. True only as a property of the chosen statistic |

---

# VERIFICATION OF THIS REPORT BY THE CALLING SESSION — 20 Nov 2026

**Nothing below was taken on the auditor's word.** The 19 Nov audit of the Φ claim handed
this project a citation (`Tarone 1990`) that reading the primary overturned, so every
load-bearing reference here was checked at source before the report was committed.

## One finding of the auditor's is WRONG, and it is the trap the row documents

> *"CHCHD2 0.2000 does not resolve to any m/M with M = floor(139/6) = 23."*

**CHCHD2 is 151 residues** — UniProt Q9Y6H1, `CHCH2_HUMAN`. 142 is the length of its
**paralogue CHCHD10** (Q8WYQ3), and the CHCHD2 row's own `frame` field says so verbatim:
*"151-residue canonical UniProt Q9Y6H1 (CHCH2_HUMAN) — NOT 142, which is the length of the
paralogue CHCHD10 and an easy transcription error to make."* M = ⌊151/6⌋ = 25, m = 5,
**m/M = 5/25 = 0.2000, as recorded.** No defect. The auditor made the error the row was
written to prevent, which is the best possible evidence that writing it there was worth it.

## Three citations, checked at source

| source | status |
|---|---|
| **arXiv:2611.15555**, Malekpouri & Lotfi, 11 Nov 2026 | **CONFIRMED [READ abstract].** Real. Title is *"What Conformal Selection Can Certify in CRISPR Off-Target Design…"* — the domain is CRISPR guide design, not benchmarking generally. The bound (conformal *p* cannot fall below 1/(calibration cohort + 1); accepted set empty in >96% of splits) is as the auditor described. |
| **arXiv:2605.28873**, Zhuang, Li & Fan, 25 May 2026 | **CONFIRMED [READ abstract]**, and it is the *closer* of the two. *"Pre-Registering the Detectable Effect: A Paired-MDE Budget for 4-bit Quantization Benchmarks, with a Pilot Audit"* — a minimum-detectable-effect bound presented as *"a one-line budget that benchmark designers can commit to before running experiments."* That is this project's move, six months earlier, at dataset level in ML benchmarking. |
| **AmyloCore-ML**, Singh J, Jangid R, Srivastava A, bioRxiv `10.64898/2026.09.25.754455` | **CONFIRMED [READ abstract, bioRxiv API, first-hand].** v1 2026-10-01, v2 2026-10-12, **v3 2026-11-18 — two days before this audit.** Abstract verbatim: *"Ordered residues in the experimental structures were designated as core, and unresolved sampled from the same proteins as matched controls as non-core"*; *"In comparative benchmarking, our predictor showed better performance metrics than CrossBeta and AggrescanAI."* |

**NOT verified, and therefore not to be cited from this report:** the auditor's specific
figures *AggrescanAI AUROC 0.719 / AUPRC 0.621* and the *82 regions / 69 proteins* count
(bioRxiv returned HTTP 429 on the full text). The abstract confirms the design and the
AggrescanAI comparison; it does not carry those numbers. **Open the full text before
quoting them.**

## The arithmetic of the lead finding reproduces

1/C(142,5) = **2.23×10⁻⁹** against the row's m/M = 0.0352 for DISC1 384-414. Confirmed
independently. The auditor's framing is correct and sharper than this project's own: §3.1b
was corrected on 20 Nov to say the bound holds for the min-rank family, but its defence —
*"switching statistics after unblinding is what pre-registration forbids"* — **defends this
study and does not defend the claim about the field.** Those are different claims and the
manuscript conflates them.

## What this changes, stated plainly

**Sub-claim D is contradicted by a working counterexample, not by an argument.**
AmyloCore-ML benchmarks *this project's own modern arm* on *exactly the fibril-core regions*
§4.2 declares unusable, under a per-residue design with within-protein matched controls
where the length ratio never enters. So the manuscript's sentence **"most published
region-mapping results cannot serve as test cases" is false as written** and must become
*"cannot serve as test cases for a min-rank benchmark."*

**That narrowing is survivable.** Sub-claim A came back NOVEL on nine EMPTY queries, and the
narrowed statement is still true and still unsaid in this field. What it costs is the broad
version of the Discussion's recommendation.

**And AmyloCore-ML is a prior-art gap in its own right**, independent of the audit: a 2026
preprint training a PLM on Amyloid Atlas fibril cores and benchmarking AggrescanAI overlaps
this project's structural arm directly, and `AmyloCore`, `Amyloid Atlas` and
`Srivastava` appear nowhere in `STATE.md`, `data/regions.json` or
`data/references_to_check.json`. It belongs in the register whatever happens to the audit.
