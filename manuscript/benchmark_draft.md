# What a predictor benchmark can learn from experimentally mapped aggregation regions — and what it cannot

**An information limit, a pre-registered null, and a finding this study withdrew**

Bertrand Mercier des Rochettes

*Draft, 20 November 2026. Not submitted. Every number in this draft is traceable to a
committed script or a source document opened in full; see §8.*

---

## Abstract

Aggregation predictors are routinely validated against short peptides that form fibrils,
and rarely against the regions that deletion and truncation experiments show to be
*required* for a full-length protein to aggregate. We assembled 27 such regions across 17
proteins, each read from its source paper and labelled for three distinct forms of
circularity, and pre-registered a benchmark before running any predictor.

**The main result is a constraint, not a comparison, and it is computable before any
software runs.** For a statistic read from the region's **best window rank**, the smallest
attainable *p* for a region of *m* windows in a chain of *M* is exactly *m*/*M*.
**Thirteen of our 23 scored rows exceed *m*/*M* > 0.05 and are therefore beyond the reach
of any min-rank benchmark at α = 0.05**, whatever predictor is used — a verdict that needs
two integers and no predictor. (A rank-sum has a different and lower floor, 1/C(*M*,*m*);
that bounds how broadly the claim may be stated and rescues none of these rows. The general
result — minimum attainable *p* under discreteness — is Tarone's rule, Tarone 1990, whose
application to aggregation benchmarking we believe to be new.)

**This is not a defect of our statistic; it is a constraint on the design**, and it
disqualifies most of the published region-mapping literature as benchmark material. Applied
prospectively it rejects rows at the moment a candidate paper is identified, for the cost
of reading two numbers out of an abstract. We screened nine further candidate proteins in
one day and admitted none.

**The benchmark itself returns a null, and that null is the constraint's evidence.** A
protein-language-model predictor (AggrescanAI) does not outperform a 2004-generation
biophysical predictor (TANGO): modern is worse on 6 of 8 non-tied pairs, median
Δ*v* = +0.09, exact one-sided Wilcoxon *p* = 0.19. On the pre-registered confirmatory set
the test has *n* = 2 and returns *Z* = −0.79 — and at *n* = 2 the smallest attainable *p*
is 0.25, so **no data could have made that contrast significant.** Two tools eighteen years
apart return bit-identical *v* on two rows, because the scores drop out of the statistic
entirely.

**No positive association survives, and how it died is reported as a result.** Across
seven structurally characterised proteins, fibril cores with a higher buried polar fraction
Φ are recovered less well (Spearman ρ = +0.82, exact *p* = 0.017, direction registered in
advance). **A control registered before its variable was computed then withdrew the
structural reading.** The polar fraction of the region's own *sequence* predicts recovery
better (ρ = +0.89, *p* = 0.0062), the two are collinear at ρ = +0.96, and the partial
correlation of Φ with recovery given sequence polarity is negative. The association is
compositional, not structural, and is already established at far larger *n* by Louros
et al. (2020); what we add there is a replication on experimentally mapped regions of large
proteins rather than on peptide libraries, reported as a replication. **We report the
retraction in full rather than the finding**, because a pre-registration that never costs
its author anything is not evidence that pre-registration works.

---

## 1. Why the usual validation does not answer the usual question

Two literatures do not meet. One maps, by deletion and truncation, which part of a protein
a cell needs in order to form inclusions. The other predicts, from sequence, which hexamer
will form a cross-β spine. The first produces statements of *necessity in a construct*;
the second produces per-residue propensity profiles. Benchmarks are overwhelmingly built
on the second kind of evidence, because peptide fibrillation datasets are large and
machine-readable, while region-mapping results are scattered across figure legends.

This matters because the two kinds of evidence disagree where it counts. For the two
scaffold proteins that motivated this work, both primary papers state in print that
predictors failed. Bradshaw et al. (2017) titled their TRIOBP-1 result *"An unpredicted
aggregation-critical region"*. Zaharija & Bradshaw located DISC1's aggregation determinant
in a central linker that the structural screen had also missed. Those failures are cited
evidence here, not a result we set out to re-establish.

The question we pre-registered is narrower and newer: **do modern predictors recover what
the 2004–2010 generation missed, and if not, what feature do they all miss?**

## 2. The dataset, and the four columns that decide what it can test

`data/regions.json` holds 27 rows across 17 proteins (v1.5.0,
10.5281/zenodo.24394773; concept DOI 10.5281/zenodo.24290697, CC BY 4.0). Each row records the residue range, the exact
sequence, the frame it is numbered in, and the source paper. Two columns carry most of the
*curatorial* weight, and two more decide what the dataset can be used to test:

**`construct`.** A region can be necessary in one construct and dispensable in another,
and both results can be correct. TRIOBP-1 1–59 is a second aggregation route that only
exists in the full-length protein; it is not a competing claim about 324–348. A benchmark
that ignores construct scores against a moving target.

**`found_by`.** A region discovered *by prediction* and then confirmed is circular
evidence for a predictor benchmark. Those rows are analysed separately, never silently
pooled.

Three independent forms of circularity are tracked and must not be conflated:
`circularity_status` (was the region found by a predictor?), `stratum` (do experiment and
prediction agree on this row?), and `cpad_status` (is the region in a predictor training
database?). A row can be clean on one and contaminated on another.

**A fourth column is not about circularity at all and decides more than the other three
together.** `power_eligible` records whether *m*/*M* ≤ 0.05 — whether a min-rank statistic
could return a significant result for the row **at all**, before any predictor is chosen.
It is false on 15 of the 27 rows. Its companion `power_limit` carries the *m*, the *M* and
the chain length, so the verdict can be recomputed rather than trusted. **Without this
column a reader cannot distinguish a row the predictors missed from a row no predictor
could ever have passed**, and §4.2 is the argument that this distinction is the most
consequential one in the dataset.

**Frames are a live hazard, not a formality.** TRIOBP-1 requires the 652-residue frame of
NP_008963.3; papers on the older 593-residue frame need 59 added, and one paper gives the
short variant as 593 in one place and 597 in another. During this work we found the same
collision in a 2026 review, which compares predictions computed in the 593 frame against
an experimental region quoted in the 652 frame.

## 3. Pre-registration

The statistic, the decoy construction and the success threshold were written down before
any predictor was run (`PREREGISTRATION.md`, frozen as `freeze-2026-11-17`).

**The statistic (§3.1).** A chain of length *L* is tiled into *M* = ⌊*L*/*W*⌋
non-overlapping windows of *W* = 6 residues. *m* is the number of windows lying wholly
inside the mapped region. *P* is the midrank fraction of windows scoring at or below the
region's best window. The row statistic is

> ***v* = 1 − *P*^*m***

which is approximately Uniform(0,1) under the null; small *v* means the predictor
succeeded. Rows shorter than one window are scored by a registered fallback (§3.1a) that
treats the region as a single window of its own length against the sliding pool, giving
*m* = 1.

**The thresholds (§4).** A row is *recovered* iff *v* < 0.05. Modern beats legacy iff a
one-sided Wilcoxon signed-rank test on paired Δ*v* gives *p* < 0.05 **and** median
Δ*v* < −0.10.

**The confirmatory set (§5.2b).** Rows that are discordant, CPAD-absent and
circularity-clean, combined by Stouffer's *Z* (primary) and Fisher (secondary).

**Ordering (§7).** The stratum label comes from the legacy arm and must be committed
before the modern arm is run on that row.

**Everything else is exploratory (§12)** and is labelled as such below.

## 4. Results

### 4.1 The benchmark returns a null, and the effect points the wrong way

Paired *v* for TANGO 2.3.1 (legacy) and AggrescanAI (modern) on the ten rows where both
arms have run:

| row | TANGO *v* | AggrescanAI *v* | Δ*v* |
|---|---|---|---|
| TRIOBP-1 1–59 | 0.9995 | 0.0409 | **−0.959** |
| TAF15 7–99 | 0.99999 | 0.7834 | **−0.217** |
| CHCHD10 42–75 | 0.10407 | 0.10407 | **0.000** (exact tie) |
| CHCHD2 54–86 | 0.09608 | 0.09608 | **0.000** (exact tie) |
| DISC1 748–769 | 0.9227 | 0.9955 | +0.073 |
| DISC1 384–414 | 0.3189 | 0.4164 | +0.098 |
| TMEM106B 120–254 | 0.7156 | 0.9900 | +0.274 |
| TRIOBP-1 333–340 | 0.0388 | 0.4240 | +0.385 |
| TRIOBP-1 324–348 | 0.1235 | 0.9079 | +0.784 |
| DISC1 691–836 | 0.0812 | 0.9994 | +0.918 |

*Exploratory (§12): this row set is wider than the confirmatory set.* Two pairs are exact
ties and are dropped by Wilcoxon, leaving *n* = 8. Modern is worse on **6 of 8**, median
Δ*v* over all ten pairs is **+0.086**, and the exact one-sided *p* is **0.191**. Both §4
criteria fail, and the effect-size criterion fails **by sign**.

At *n* = 8 the smallest attainable Wilcoxon *p* is 2⁻⁸ = 0.0039, so for the first time in
this project the test fails on the data rather than on arithmetic. On the pre-registered
confirmatory set it does not: there *n* = 2 and the smallest attainable *p* is **0.25**, so
no data could have made §4's contrast significant.

**TANGO's physical parameters were never pre-registered.** Rather than choose them after
unblinding, we ran a 9-point grid (pH {5.0, 7.0, 7.4} × T {298, 303, 310} K). The
conclusion is identical at every grid point: 6 of 7 on the original row set, *p* = 0.148
throughout. An unregistered free parameter became a measured sensitivity instead of a
hidden choice.

**Two pairs are bit-identical between arms.** CHCHD10 and CHCHD2 differ between the two
predictors by 1.4 × 10⁻¹¹ and 6.9 × 10⁻¹⁷. Both tools place the single highest-scoring
window of the chain inside the region, so *P* = (*M*−0.5)/*M* for both and *v* is fixed by
*M* and *m* alone — **the scores drop out of the statistic entirely.** This is the floor
described in §4.2, observed.

### 4.2 The floor, and then the limit

*v* = 1 − *P*^*m* with *P* ≤ (*M*−0.5)/*M*, so

> **min *v* = 1 − ((*M*−0.5)/*M*)^*m***

attained by a *perfect* predictor. **Nine of 23 scored rows have a floor above 0.05**, so
§4's recovery criterion cannot fire on them whatever the predictor does (TMEM106B 0.218,
SAA 0.212, CHCHD10 0.104, CHCHD2 0.096, TRIOBP-1 60–189 0.093, DISC1 691–836 0.081, TAF15
0.074, LECT2 0.067, hnRNPA1 0.064).

A 100 000-draw null simulation per geometry shows the problem is two-sided: a criterion
with a nominal 5 % false-positive rate actually runs **between 0.000 and 0.091** across
this dataset, decided by *M* and *m* alone. Exact calibration against the discrete null
(`scripts/calibrate_v.py`; *P*(rank = *k*) = C(*k*−1, *m*−1)/C(*M*, *m*)) shows *v* is well
calibrated where *m* is small relative to *M* (0.99–1.08×) and **anti-conservative by
2.1× at the floor**.

That is a defect in our statistic and could be repaired. The next one cannot be.

> **Under the null, the chain's top-ranked window falls inside the region with probability
> exactly *m*/*M*. No statistic read from that rank — not this one, not a repaired one —
> can return a *p* below *m*/*M*.**

**That bound is exact for the min-rank family and not for every rank-based statistic**, and
the distinction is worth stating because an earlier version of this manuscript overstated
it. A rank-sum over the *m* in-region against the *M*−*m* out-of-region window scores has
minimum attainable one-sided *p* = 1/C(*M*,*m*) — on β2-microglobulin 22–85 (*m* = 10,
*M* = 16) that is 1.25 × 10⁻⁴ against *m*/*M* = 0.625. **It is a limit on the wording, not
a rescue**: a rank-sum answers a different question, the tiled windows are not independent,
and changing statistics after unblinding is what pre-registration forbids. The general
result — minimum attainable *p* under discreteness, used to exclude untestable hypotheses —
is **Tarone's rule** (Tarone 1990, *Biometrics* **46**:515–522); what is new here is its
application to aggregation benchmarking, for which a literature search returned nothing.

**Thirteen of 23 scored rows exceed *m*/*M* > 0.05**, from TMEM106B at 0.489 and SAA at
0.471 down to ANXA11 at 0.060. **Ten can ever reach *p* < 0.05.** The two founding
confirmatory rows are among them, narrowly: DISC1 384–414 at 0.0352 and TRIOBP-1 324–348
at 0.0370.

**This needs only the chain length and the region length.** It costs nothing, requires no
predictor, and can be applied at the moment a candidate paper is identified. We registered
it as §3.1b — a row is *power-eligible* iff *m*/*M* ≤ 0.05 — and applied it to every row
without removing any, since dropping rows after seeing their scores is the post-hoc
selection pre-registration exists to prevent.

Applied prospectively it would have rejected all three of the rows we recruited that week
at stage 1. Applied to nine further candidates screened in a single day — including every
remaining lead from a systematic search — it admitted **none**. The constraint is not an
artefact of our protein set. Short proteins and long ordered cores are exactly the
geometry that cryo-EM core papers produce by construction, and the geometry that makes a
region unsurprising to rank.

**The pool that yields eligible rows is deletion and truncation mapping on large
proteins** — which is where DISC1 and TRIOBP-1 came from, and which yields the stronger
evidence type (necessity) as a side effect.

### 4.3 The confirmatory arm

| set | *n* | Stouffer *Z* | one-sided *p* |
|---|---|---|---|
| Confirmatory (§5.2b) | 5 | +0.296 | 0.384 |
| Confirmatory, power-eligible only (§3.1b) | 2 | **−0.790** | **0.785** |
| CPAD-contaminated, reported separately | 7 | **+2.171** | **0.015** |

The confirmatory arm is null, and on the two rows where the test has any power it is null
with the sign reversed.

**The one significant combination in the study is the contaminated one.** Rows whose
regions are present in a predictor training database are recovered; rows that are not,
are not. We do **not** present this as a clean demonstration of training-set leakage,
because the two factors are confounded in our data: the three rows driving that *Z* (tau
306–311, tau 275–280, α-synuclein 71–82) are simultaneously the rows with the most
favourable geometry, at *m*/*M* = 0.0023, 0.0023 and 0.0435. Short regions in long chains
are both easy to rank and over-represented in peptide databases. Disentangling the two
would need CPAD-absent rows at comparable *m*/*M*, which is exactly the row type §3.1b
says is scarce.

### 4.4 Polar cores: a positive association, and its withdrawal

> **Reported here as a methods result, not as a finding.** This subsection registered a
> metric, obtained a significant association with it, and then withdrew the reading on the
> strength of a second control registered before its variable existed. The sequence is the
> contribution; the association is not.

For the seven rows with a deposited fibril structure, we registered a metric — Φ, the
fraction of buried residues (SASA < 10 Å² in an 11-layer assembly) that are polar — and its
abandonment condition (AUROC < 0.80 against twelve independently classified structures)
**before computing it on any row**, and committed Φ before joining it to *v*.

Calibration gave AUROC = 0.844 for the primary variant; all nine pre-specified
cut × variant combinations passed, and the registered primary was the weakest of them. A
pre-registered opportunity for the metric to fail did not fire: LECT2, whose own paper is
titled *"…reveals a network of polar ladders at its core"*, scored 0.526, above threshold,
agreeing with its authors.

The registered test passes:

> **Spearman ρ = +0.821, exact one-sided *p* = 0.0171, *n* = 7**, direction named in
> advance (higher Φ → higher *v* → worse recovery). *p* is exact over all 5040
> permutations; the smallest attainable value at *n* = 7 is 0.0002, so this is not a floor.

> ### §4a The structural reading of that number is WITHDRAWN
>
> **A control registered under §10d on 20 Nov 2026, committed before the variable was
> computed, returned the verdict `COLLAPSED` at both pre-registered burial cutoffs.**
>
> | | cut 5 Å² | cut 10 Å² |
> |---|---|---|
> | ρ(Φ, *v*) | +0.6786 (*p* = 0.0548) | +0.8214 (*p* = 0.0171) |
> | **ρ(Φ_seq, *v*)** | **+0.8929 (*p* = 0.0062)** | **+0.8929 (*p* = 0.0062)** |
> | ρ(Φ, Φ_seq) | +0.8929 | **+0.9643** |
> | **partial ρ(Φ, *v* │ Φ_seq)** | **−0.5849** | **−0.3315** |
>
> where **Φ_seq** is the polar fraction of the whole mapped region's sequence, on the same
> POLAR set, over the same residues, needing no structure at all.
>
> **The sequence-only covariate does not tie with Φ. It beats it**, and the partial
> correlation reverses sign. At ρ(Φ, Φ_seq) = +0.96 the two are barely distinguishable and
> burial is subtracting information rather than adding it.
>
> **Note also the first row of that table.** At the 5 Å² burial cutoff — a registered
> variant, not a post-hoc one — the headline result gives *p* = 0.0548 and **fails this
> study's own α**. That number had never been computed before the control.
>
> **So §4.4's finding is not new and not structural**, and those are two separate
> retractions. See Louros et al. (2020) *Nat Commun* **11**:3314, who report a 20% increase
> in polar and charged side chains in APRs missed by sequence predictors, at far larger *n*
> and five years earlier.

**These are seven distinct proteins** — the only analysis in this study whose independence
assumption is actually satisfied. It is not a CPAD artefact: ρ(CPAD, *v*) = +0.000 and
ρ(CPAD, Φ) = +0.144, and the two factors are not collinear here.

**It is fragile.** Dropping any one of four rows takes *p* to 0.0514. At *n* = 6 the
smallest attainable *p* is 0.0014, so that is a genuine value and not a floor — the result
simply has no room to spare. One of the four most influential rows is TMEM106B, which
carries a known, unrelated transmembrane-helix confound and is also the second-highest Φ.
The correct reading is **"significant at the registered α on seven rows, and not robust to
the loss of any one of four of them."**

**And the tautology, registered in advance, still applies** — now with more force than
when it was written. A predictor built on hydrophobicity scoring polar regions lower is
partly a restatement of how it works, and the control above shows the *sequence* is where
that restatement lives. The part that is not tautological is the experimental half: these
polar regions are genuine, experimentally mapped aggregation determinants. **The surviving
claim is not that the tools dislike polar cores. It is that nature does not, and the tools
have not noticed — and that this holds on mapped regions of large proteins, not only on
peptide libraries.** Stated as a replication of Louros et al. (2020), not as a discovery.

## 5. What this does not show

- **Nothing about DISC1 or TRIOBP-1 and polarity.** Neither protein has a deposited
  structure; neither is in the Φ analysis. The confirmatory stratum is untouched by §4.4
  and the headline question is unmoved by it — **before or after §4a's withdrawal.** The
  withdrawal costs the manuscript a positive finding and costs the headline question
  nothing, because §4.4 could never have spoken to it.
- **No claim that a fibril core's *structure* predicts anything here.** §4a withdrew that
  reading. What survives is compositional and is Louros et al. (2020); the structural
  apparatus bought a weaker version of it.
- **No claim that any predictor "failed" on the nine floor-bound rows.** For them that
  sentence is true by arithmetic before any predictor runs, and it points in the direction
  of our own hypothesis. Such claims elsewhere in the literature deserve the same check.
- **No claim that the legacy generation behaves like the modern one on polarity.** TANGO
  was not run on four of the seven structural rows; *n* = 3 supports nothing.
- **No aggregate-structure modelling of any psychiatric protein.** There are no deposited
  aggregate coordinates for any of five candidates, and none among the 51 steric-zipper
  entities in the PDB. That is an enumerated absence, reported, not worked around.

## 6. Discussion

The practical recommendation is a single inequality. **Before reading a candidate paper in
full, compute *m*/*M*.** If it exceeds the intended α, no amount of curation, no
amendment to the statistic and no better predictor will make that row informative. Only a
longer protein or a shorter mapped region can.

We arrived at this the expensive way: by recruiting three rows through an eight-stage
pipeline, running both predictor arms on them, and only then computing a ratio that needed
two integers the dataset had held for days. The margin was smaller than the resolution of
the instrument, and that was knowable in advance.

The consequence for the field is uncomfortable but not pessimistic. It is not that
aggregation predictors are untestable against region-mapping data. It is that **most
published region-mapping results cannot serve as test cases**, and the subset that can is
identifiable for free. A benchmark that reports accuracy over a pooled set of such regions
without reporting *m*/*M* per row is reporting a number whose null distribution varies
across its own rows by an order of magnitude.

Our own benchmark is underpowered and we state it plainly: the decisive subset holds two
rows. **Three things here do not depend on that *n*.**

**The eligibility criterion**, which tells the next group which rows are worth their
compute and costs two integers to apply. **The dataset**, curated row by row from source
papers, with three-way circularity labelling and a published DOI. And **the withdrawal in
§4a**, which we regard as the third contribution rather than an embarrassment attached to
the other two.

That last claim deserves its reason. The polar-core association was this study's only
positive result; it was registered in advance, it passed its own abandonment condition, it
survived a prior-art audit, and it had already been written into a deposited dataset's
description. **It was withdrawn by a control that cost about ten minutes of computation and
was committed before the variable it tested existed.** A pre-registration that never costs
its author a result is not evidence that pre-registration works — it is evidence that
nothing was at stake. Readers of benchmark papers are entitled to ask how many unreported
controls of this kind were available and not run.

**And the defect that control exposed is the one we would most want others to look for in
their own work** (§9, defect 6): a sensitivity analysis registered with two settings and
reported at one. Nothing fails when that happens. No test errors, no reviewer objects, and
the published number is the favourable arm of a comparison the author never shows.

## 7. Methods (summary)

**Legacy arm.** TANGO 2.3.1, 9-point grid (pH {5.0, 7.0, 7.4} × T {298, 303, 310} K,
ionic strength 0.05, nt=N, ct=N, tf=0, stab=−10); reporting point pH 7.0 / 310 K; grid
range reported per row. §5.1's other three tools were dropped for stated, checkable
reasons: ProA is dead, AGGRESCAN is web-only and fails the version-pinnability rule, and
the FoldAmyloid reimplementation did not pass its registered validation.

**Modern arm.** AggrescanAI over ProtT5 embeddings; ProtT5 revision
`94a6abc029ae13029317b140b7424e012bf8dfbf`, AggrescanAI weights revision
`7aba68e65d620aa55b10f9550005efff3f3240e7`, both pinned and checksummed by the runner.
**Ensemble spread across the five CV models is large** (max 0.893, 0.899, 0.867 on the
three most recent runs) and is a standing caveat on every AggrescanAI number here.

**Φ.** **11-layer** assembly (−5…+5) along *z* from the deposited helical rise and twist,
with the stacking axis verified rather than assumed; Shrake–Rupley SASA, probe 1.4 Å, 92
points. *The 18 Nov run executed 13 layers, which is a deviation from the registered 11;
it was found and closed on 19 Nov by recomputing every row and all twelve calibration
structures at 11. Every number reported here is the 11-layer one. The deviation changed no
calibration value and did not move the headline ρ, but it did reorder two of the seven
rows, so it is reported as a measured deviation rather than as an equivalence.*

**Scripts.** `scripts/score_rows.py` (statistic, floor and limit warnings),
`calibrate_v.py` (exact calibration), `v_floor_simulation.py` (null simulation),
`apply_power_eligible.py` (§3.1b labelling), `core_polarity.py` (Φ).

## 8. Data, code and provenance

Dataset: **10.5281/zenodo.24394773** (v1.5.0, the version these numbers were computed
against) or 10.5281/zenodo.24290697 (concept DOI, always the latest), CC BY 4.0. *Note for
anyone citing an earlier version: the v1.4.0 version DOI, 10.5281/zenodo.24342313, does not
resolve — the record is published but was never registered with DataCite, and a request is
with Zenodo. Cite its record URL if you need it.* Code and the full research
record, including the pre-registration and every amendment with the date and whether
scores had been seen: `github.com/quantumproteinsai/mentalillness`.

**Provenance rule applied throughout.** A number is quoted from a source somebody opened,
or it is declared unmeasured. Claims reached by search are graded READ, SNIPPET or EMPTY.
Rows whose source is a preprint or thesis rather than a version of record are marked by
`source_version`, which governs over any boolean flag; **DISC1 384–414 is such a row** and
is flagged here rather than silently cited.

**That row's boundary was corrected during this work, and the correction is not cosmetic.**
It read 384–415 in every version of this draft and in every deposited version of the
dataset up to v1.4.0. The corresponding author of the source settled it at **384–414** from
sequencing of the actual plasmids (personal communication, 19 Nov 2026): the construct
joins DISC1 1–383 to 415–854, so Ala415 was never deleted. The value we had carried came
from plasmid *names* in a thesis table, which disagree with the sequencing of those same
plasmids. **No number in this manuscript moves** — under §3.1 the two readings select the
same five tiles, since residue 415 falls in no scored tile — but the range as published was
wrong by one residue.

## 9. Known defects in this work

Six, all recorded in the project history rather than discovered by reviewers:

1. **§4's contrast was unreachable at the confirmatory *n*** (min *p* = 0.25 at *n* = 2) —
   a threshold the design could not reach.
2. **§3.1's *v* is anti-conservative at small *M* with large *m*** (2.1× at the floor), and
   its nominal 5 % criterion runs 0.0–9.1 % across this dataset.
3. **Nine rows cannot reach the recovery bar**, and thirteen cannot reach α = 0.05 under
   any min-rank statistic. *An earlier draft wrote "any rank statistic"; see §4.2.*
4. **Six rows have a stratum assigned after the modern arm had run on them**, breaching the
   §7 ordering; they are held out of the confirmatory set and reported separately.
5. **CHCHD10 and CHCHD2 are 84.8 % identical over the scored span** and are one measurement
   for any sequence-based predictor, not two. They were admitted knowingly and the
   non-independence is recorded on both rows.
6. **§10a registered two burial cutoffs and reported one.** At the unreported one, 5 Å²,
   the headline correlation is ρ = +0.6786, *p* = 0.0548 — **it fails this study's own α at
   its own alternative setting.** That number did not exist until the §10d control computed
   it on 20 Nov, two days after the result was written up and one day after it survived a
   prior-art audit. **Registering a sensitivity analysis and then reporting only the
   favourable arm of it is the defect**, and it is a more dangerous one than the other five
   here, because nothing fails when it happens.
