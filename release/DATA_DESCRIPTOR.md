# Experimentally mapped aggregation-critical protein regions

**with circularity, prediction-concordance and training-set-contamination labels**

Version 1.5.0 · 27 regions across 17 proteins

---

## What this is

A hand-curated set of protein regions that **experiment** has shown to be
required for, or to constitute the core of, protein aggregation. Every row was
established by opening the source paper and checking the claim against it.

It is small on purpose. It is not a mined database, and it is not a
comprehensive survey. **Every row here is one somebody read.**

## What it is for

It was built to benchmark sequence-based aggregation predictors, and it carries
four columns that most aggregation datasets lack — each of which exists because
leaving it out produces a benchmark that silently measures the wrong thing.

### `construct` — which construct established the region

A region can be **necessary in one construct and dispensable in another**, and
both results can be correct. TRIOBP-1 324-348 is necessary in a 190-652
construct but, in the same paper, *not sufficient* in 1-382. TDP-43's RRM2
aggregates when truncated and not when intact. Without this column a benchmark
scores against a moving target.

The dataset also contains a case where construct **does not** matter — hnRNPA1's
fibril core is the same from full-length and truncated protein, RMSD 0.688 Å —
recorded because the exception is as informative as the rule.

### `circularity_status` — was a predictor in the discovery path?

**A region found *by* a predictor cannot be used to test that predictor.** This
sounds obvious and is pervasive in the literature: a predicted segment gets
deleted, the deletion works, and the result is published as experimental
mapping. Four of these 27 rows are `CIRCULAR`, and they are **kept and
labelled**, not dropped, because they are still evidence — just not evidence
about predictor accuracy.

**This cannot be determined by keyword.** The same laboratory in the same year
produced rows of opposite status. Every row therefore carries a written
`circularity_basis`, and assessing it required reading the Methods and the first
figure, not the abstract. In one case an abstract that read as clean — *"using a
series of deletion variants"* — turned out, on reading the paper, to describe
variants designed to delete segments two named predictors had ranked.

### `stratum` — do experiment and prediction agree?

Distinct from circularity: **circularity is about discovery, stratum is about
outcome.** A region can have a clean discovery path and still be one the
predictors find easily.

This matters more than it looks. **Regions that get mapped cleanly and early tend
to be exactly the ones predictors detect** — classic short hydrophobic or β-prone
motifs. So a dataset assembled by looking for well-mapped regions is *enriched
for agreement*, and agreement cannot discriminate between predictors, because
they all hit it. Only the **discordant** rows can.

| stratum | n | meaning |
|---|---|---|
| `DISCORDANT` | 15 | experiment and prediction disagree |
| `DISCORDANT_DERIVED` | 1 | disagreement established by comparing two papers, not stated by either — strictly weaker |
| `CONCORDANT` | 5 | the predictors find it |
| `PENDING` | 6 | not yet assessed; requires a predictor run or a published one |

**One of those six `PENDING` rows is not pending at all**, and the distinction matters more
than the count. SOD1 3-55,86-153 is a **discontinuous** core, and under the project's
pre-registration no statistic is defined across a gap — so the rule that assigned every
other stratum cannot run on it, now or later. It carries `stratum_not_assignable` with that
reason. The controlled vocabulary has no `NOT_APPLICABLE` value and inventing one is a
change to a published schema, so the distinction is carried in a separate field until that
decision is taken. **A consumer counting `PENDING` as "awaiting a predictor run" should
subtract any row carrying `stratum_not_assignable`.**

### `structure` — which deposited fibril structure, if any *(new in 1.4.0)*

**13 rows** describe the ordered core of a solved fibril — six more than in 1.4.0. Each
records the PDB entry, the chain, the modelled range, the method and resolution, the
helical rise and twist, **every candidate entry considered**, and the rule that chose among
them.

**Its absence carries information.** A row without `structure` has no deposited fibril
structure at all — true of every DISC1 and TRIOBP-1 row, which is why those rows cannot
take part in any structure-based analysis, including the core-polarity result reported with
1.4.0.

> ### The structural rows and the benchmark rows are almost disjoint, and that is a fact about the field
>
> **Of the 13 rows with a deposited structure, exactly one is `power_eligible`** — and that
> one, Orb2, is a CPAD member, so it cannot enter the primary confirmatory statistic either.
> The reason is geometric and not a property of this dataset: a cryo-EM ordered core is a
> *large fraction of a short construct*, and `power_eligible` requires the opposite — a
> short region inside a long chain. **Every row in the confirmatory cell has no structure,
> and almost every row with a structure can never be in the confirmatory cell.**
>
> So the two analyses this dataset supports draw on **almost disjoint** sets of rows. A
> reader planning to extend it should know that recruiting more fibril structures, which is
> by far the easiest way to add rows, **adds nothing to the benchmark arm.**

### `stratum_assignment` — was this label assigned blind? *(new in 1.3.0)*

**Not every `DISCORDANT` row counts the same, and this column says which is which.**

Of the 16 rows in the discordant family, **5 were documented in print**, with the
disagreeing tools named by the source paper, and carry no `stratum_assignment` at all.
**11 were assigned by us**, from our own legacy predictor run, by a fixed rule: discordant
iff the legacy score missed the region at the project's pre-registered recovery bar.
Neither the rule nor the bar was chosen after seeing a score.

**But for most of them the order was wrong, and the column records that.** The protocol
requires the label to be fixed *before* the modern predictor is run on the row. **7 of the
11 were labelled afterwards**, when the modern scores were already known. The rule is
mechanical and leaves no threshold to tune — but the choice of *whether to apply it* was
made with the outcome visible. So those rows carry:

```
stratum_assignment: { ..., confirmatory_eligible: false }
```

**The other 4 were labelled in the right order**, and this is the first release where any
row can say so *from the commit graph rather than from an assertion*: their strata were
committed and pushed before the modern arm was run, and the two timestamps are in the
repository's history. They carry `confirmatory_eligible: true`.

**A `DISCORDANT` label alone does not admit a row to the confirmatory set.** Read this
flag — and read `power_eligible` with it. Together they are why the confirmatory count is
**2** and not 16.

*For the record, applying the rule did not flatter the project's hypothesis: it made the
result worse. That is stated here because the usual objection to a rule applied late is
that it was applied because it helped.*

### `power_eligible` — could *any* predictor have passed this row? *(core in 1.5.0)*

**This column is not about a predictor. It is about whether the row can be scored at all,
and it is the one most likely to be misread as a result.**

Tile the scored chain into non-overlapping 6-residue windows: *M* of them, *m* of them
inside the mapped region. Under the null hypothesis, the probability that the chain's
single top-ranked window falls inside the region is **exactly *m*/*M***. So *m*/*M* is the
smallest *p* a statistic that reads the region's **best window rank** can return for that
row — before any predictor is chosen, and whatever that predictor does.

```
power_eligible = (m / M <= 0.05)
```

**Where this is `false`, the row cannot produce a significant result no matter what.** No
better predictor rescues it; no amendment to the statistic rescues it. Only a **longer
protein** or a **shorter mapped region** would. **15 of 27 rows are in that state.**

`power_limit` carries the *m*, the *M*, the chain length and the ratio on every row, so the
flag can be recomputed rather than trusted. Note that *M* is computed on the **scored
frame** named in `frame`, not on the precursor — re-deriving *m*/*M* from a UniProt length
will disagree wherever the two differ, which is what the `frame` column is for.

**Two limits on the bound, both recorded here rather than discovered by a reader.**

1. ***m*/*M* is the floor for the min-rank family of statistics, not for every rank-based
   statistic.** This project's statistic reads the best window rank alone, so the bound is
   exact for it. A **rank-sum** over the *m* in-region against the *M*−*m* out-of-region
   window scores has a different minimum attainable one-sided *p*, namely 1/C(*M*,*m*) — on
   the β2-microglobulin row (*m* = 10, *M* = 16) that is **1.25×10⁻⁴**, against *m*/*M* =
   0.625. That is a limit on how broadly the claim may be stated, **not a rescue of the
   ineligible rows**: a rank-sum answers a different question, the tiled windows are not
   independent, and switching statistics after seeing scores is what pre-registration
   exists to forbid.
2. **The general result is published and named.** Minimum attainable *p* under
   discreteness, used to exclude untestable hypotheses, is **Tarone's rule** — Tarone RE
   (1990), *Biometrics* **46**:515–522. Cite that; what is new here is only its application
   to aggregation benchmarking.

> **The practical consequence for anyone using this dataset.** Check `power_eligible`
> before you score a row, not after. A region that is a large fraction of its chain —
> which describes nearly every cryo-EM fibril core — will make any predictor look as
> though it failed, and the failure is in the arithmetic.

### `cpad_status` — is the row in the predictor's training set? *(new in 1.1.0)*

**A third kind of circularity, and the one most likely to be missed.** Not a predictor
in the *discovery* path, and not experiment–prediction *agreement*, but **training-set
membership of the benchmark row itself**. A modern predictor that hits a region whose
protein it was trained on has recalled, not predicted.

| value | n rows | meaning |
|---|---|---|
| `CPAD_MEMBER` | 10 | the protein is in CPAD 2.0 |
| `CPAD_ABSENT_ORTHOLOGY_CHECKED` | 17 | absent from CPAD 2.0 **and** from its orthologous group |

**These are the only two values that occur, and as of 1.5.0 that is enforced rather than
observed.** Three rows added in 1.5.0 were written with an undocumented third token,
`CPAD_PRESENT`. No verdict was wrong — all three are members — but every documented way of
excluding contaminated rows is written `cpad_status == "CPAD_MEMBER"`, so a consumer doing
exactly what this file says **would have readmitted all three**, which is the precise error
the column exists to prevent. A synonym is more dangerous here than a wrong value, because
it passes silently through the filter. The token is normalised and
`scripts/validate_regions.py` now enforces the vocabulary.

Every row was checked, on 17 November 2026, against **all three** CPAD 2.0 datasets — the
APR protein list (286 names), the peptide table (2031/2031, contiguous) and the structures
table (565/565) — each read complete and each matching the database's own stated total.

**Checking one CPAD dataset is not checking CPAD.** hnRNPA1 is absent from the APR list
*and* from the peptide table, and present three times in the structures table. LECT2 is
the exact mirror: APR list only. A check against either single table would have cleared
one of these proteins wrongly.

**Absence was then tested against the homologue route.** AggrescanAI ships the CPAD90
model, which transfers annotations from CPAD proteins to their homologues. So absence
only means something if the protein's *orthologous group* is also free of CPAD entries.
Both sources that transfer was built from were queried. DISC1 has one human protein in
its group — itself. TRIOBP has two: itself and MPRIP (Q6WCQ1), and that paralogue was
checked separately and is also absent. **OMA alone would have missed MPRIP**; one
orthology database under-reports the group.

**`CPAD_ABSENT_ORTHOLOGY_CHECKED` is not a certificate.** The CPAD90 membership list is
unpublished. It is the strongest statement public sources support, and no more.

### What that costs, and why it is the most important number here

**5 of the 16 discordant-family rows are CPAD members** — FUS 39-95, hnRNPA1 251-295,
LECT2 55-75, Orb2 176-206 and β2-microglobulin 22-85. The remaining 11 are CPAD-absent and
circularity-clean, and **the count that matters is what happens to those 11.**

### The funnel, in the order the pre-registration applies it

**This is the single most important table in this file.** Each line is a registered
criterion, not a judgement made after seeing a score.

| after applying | rows | proteins |
|---|---|---|
| — all rows | 27 | 17 |
| `stratum` in the discordant family | 16 | 13 |
| **+** `cpad_status` absent | 11 | 8 |
| **+** `circularity_status: CLEAN` | 11 | 8 |
| **+** `confirmatory_eligible` not false | 5 | 5 |
| **+** `power_eligible` | **2** | **2** |

The two survivors are **TRIOBP-1 324-348** and **DISC1 384-414**, the two proteins the
project was built around.

**Read the last two lines before reading anything else into the row count.** The dataset
grew from 21 rows to 27 and the confirmatory cell did not move off 2. Six rows fall at
`confirmatory_eligible`, because their labels were assigned after the modern predictor had
run; three more fall at `power_eligible`, because no rank-based statistic could return a
significant result for them *whatever predictor is used*. **Those are different kinds of
failure and must not be pooled**: the first is a procedural defect of ours, repairable in
principle; the second is arithmetic, and no better predictor repairs it.

Anyone benchmarking a modern predictor on this dataset without the `cpad_status` column
would be measuring memorisation on most of the rows that appear to matter.

## Why a hand-read set, when curated APR databases already exist

**Because three independent groups have now stated in print that those databases
cannot support predictor comparison** — and two of the three are the authors of
the predictors being compared.

**Thompson et al. 2025**, *Sci. Adv.* **11**(18):eadt5111, doi:10.1126/sciadv.adt5111 (CANYA), on training contamination:

> "several of these methods (including TANGO, CamSol, and Aggrescan) were
> directly trained on sequences within CPAD"

and, on WALTZ-DB hexapeptides, that "no method significantly outperformed
hydrophobicity".

**Planas-Iglesias et al. 2024**, *Nucleic Acids Res.* **52**:W159–W169
(AggreProt), on the labels themselves:

> "AmyPro and CPAD 2.0 … are widely used for predictor benchmarking. However, we
> and other groups have recently contested this relatively common practice by
> experimentally investigating the amyloid propensity of some of the sequences
> and revealed **many inaccuracies in the database labels**. As a result,
> comparing protein-level predictions … based on these databases is potentially
> biased, and their performance **should always be validated by an experiment**."

**Navarro et al. 2026**, *J. Mol. Biol.* **438**:169643 (AggrescanAI), stating
the remedy:

> "These observations highlight the need for a more specific, **gold-standard
> reference set of APRs** to improve benchmarking across prediction tools."

Its conclusions ask for "improved … experimental annotation of APRs at
residue-level resolution, which would reduce label ambiguity and upper-bound
limitations."

**This dataset is an attempt at that object.** Every row was read from its source
paper; none was bulk-imported. That is why it is 27 rows and not 17,000.

### The same three papers set a floor on what a benchmark can claim

Navarro's Figure 2 reports AUROC on an external benchmark: **AggrescanAI 0.69,
ANuPP 0.60, AggreProt 0.60, AGGRESCAN 0.58, Aggrescan3D 0.51** — the last
indistinguishable from random. **No confidence intervals are given.** Anyone using
this dataset to separate two predictors should size the expected difference
against that, before spending anything.

### The contamination check, and the part of it that remains open

AggrescanAI is trained on **CPAD90** — CPAD 2.0 *plus homologous sequences*
transferred through the HoTIDP server from OrthoInspector and OmaDB orthologues
(Navarro 2026, Methods). **So confirming that a row's protein is absent from CPAD
is not sufficient**: an orthologue of a CPAD protein can carry a transferred
annotation into training.

**Version 1.1.0 introduced that check, and 1.2.0 carries it on every row** — see `cpad_status` above — against all three
CPAD 2.0 datasets and against both orthology sources. Several proteins here, tau and
α-synuclein in particular, are heavily annotated in CPAD and are labelled accordingly.

**What it cannot settle for you.** The CPAD90 membership list is not published ("Data
will be made available on request"), so no row can be certified training-set-clean in
absolute terms, and **the check is specific to CPAD**. A predictor trained on some other
corpus needs its own check, and this column will not do it. The method is written out in
`_CPAD_MEMBERSHIP_CHECK_2026-11-17` inside the JSON so it can be repeated against a
different training set.

## What changed in 1.5.0

**Six new rows, a corrected residue range, and one new core column. The confirmatory cell
did not move.**

### A residue range was corrected by the corresponding author, and every earlier version is wrong about it

**DISC1's deleted region is 384-414, not 384-415.** Versions 1.0.0 through 1.4.0 all record
384-415, a 32-residue range. It is 31 residues. The correction comes from the corresponding
author of the source, by email on 19 November 2026, and rests on **sequencing of the actual
plasmids**, quoted verbatim in the row's `range_provenance`:

> "I checked the sequencing of our DISC1 vectors and the region deleted is 384-414
> (generated by attaching DISC1 1-383 to DISC1 415-854)."

1-383 joined to 415-854 leaves 384-414 absent. **Ala415 is present in the construct and was
therefore never part of the deleted region.** The value this project had recorded came from
plasmid *names* in a PhD thesis table and from a preprint sentence reading "these 32 amino
acids" — while the same preprint's body text writes Δ384-414 three times. **A number from a
plasmid name disagreed with the sequencing of that plasmid, and the name was wrong.**

> **If you are using 384-415 from any earlier version of this dataset, or from the
> preprint's abstract, the range is off by one residue at the C-terminus.** This is the
> change that decided 1.5.0 was owed rather than optional.

The same correspondence confirmed a second thing: a published figure legend giving a
TRIOBP-1 region as **324-328** should read **324-348**. That row already carried the
conflict and the instruction not to score it as an independent region; it is now confirmed
at source rather than inferred.

### Six rows, and the useful result is that they changed nothing

Added: **CHCHD10** 42-75, **CHCHD2** 54-86, **TAF15** 7-99, **Orb2** 176-206
(*Drosophila*), **β2-microglobulin** 22-85, and **SOD1** 3-55,86-153. Four of the six are
the first rows in this dataset whose stratum was assigned **before** the modern predictor
ran on them, verifiable from the repository's commit history rather than asserted.

**And the confirmatory cell is still 2 rows.** Three of the six are CPAD members; five of
the six are not `power_eligible`; SOD1 cannot carry a statistic at all. See the funnel table
above. **That is the finding, not a disappointment:** the rows that are easy to add are
systematically the rows that cannot discriminate between predictors.

### `power_eligible` and `power_limit` are now core columns

They were on 26 and 27 of the 27 rows respectively and were documented nowhere — so a
consumer could not see the flag that decides the confirmatory cell, and could not tell a
row the predictors failed from a row no predictor could ever have passed. `power_limit` was
also an object on 25 rows and a prose string on 2, so it could not be read mechanically on
exactly the two rows whose eligibility is unusual. Both are fixed, and the Orb2 row's flag —
`null` while its own recorded arithmetic put it below the bar — is resolved to `true` from
the *m* and *M* already on the row.

### `cpad_status` had an undocumented synonym

Three rows carried `CPAD_PRESENT`, which this file never defined. All three are members, so
no verdict was wrong, but the documented filter would have readmitted them. Normalised, and
now enforced as a controlled vocabulary.

## Composition

| | |
|---|---|
| **proteins** | DISC1 (6) · TRIOBP-1 (5) · tau (2) · α-synuclein · FUS · hnRNPA1 · serum amyloid A · LECT2 · TMEM106B · ANXA11 · glycinin G4 (soybean) · **CHCHD10** · **CHCHD2** · **TAF15** · **Orb2** *(Drosophila)* · **β2-microglobulin** · **SOD1** |
| **circularity** | 23 CLEAN · 4 CIRCULAR |
| **source version** | 22 version of record · 4 author manuscript · 1 preprint |
| **with sequence** | 22 / 27 (each checked to match its stated range in length) |
| **with explicit numbering frame** | 27 / 27 |
| **with a deposited fibril structure** | 13 / 27 |
| **`power_eligible`** | 12 / 27 |

Evidence classes span cell-based truncation series, unbiased peptide-array
scans, solid-state NMR, cryo-EM of recombinant fibrils, and **cryo-EM of fibrils
extracted from a patient's kidney** — the only row in the set that is not
recombinant.

## Read these before using a residue number

**Numbering frames in this literature are a trap, and three separate kinds of
trap appear in these 27 rows.**

- **A constant offset.** TRIOBP-1 is numbered here in a 652-residue frame; much
  of the literature uses 593. Convert by subtracting 59.
- **An internal alternative exon.** hnRNPA1's two isoforms differ by an internal
  insert, so a constant offset is *not* generally valid. The offset happens to
  work for the row here, and that was verified by sequence lookup rather than
  assumed.
- **An allele.** The serum amyloid A core sequence differs between SAA1.1, 1.3
  and 1.5 at residue 52 — **inside the region**. Taking that sequence from the
  canonical UniProt entry silently gives the wrong residue.

The `frame` field records the frame and, where available, the accession. **Where
`frame` is absent, do not assume.**

## Honest limitations

- **It is small, and the usable part is smaller than it looks — and it did not grow.**
  27 rows, up from 21. The discordant family holds 16, but 5 are CPAD members, 6 more are
  not `confirmatory_eligible`, and 3 more are not `power_eligible`. **2 rows remain**,
  TRIOBP-1 324-348 and DISC1 384-414, each from a single laboratory lineage. That supports
  a case series on two proteins, not a rate, and it should be read against the AUROC floor
  below before any compute is spent. **Six new rows moved that number by zero**, which is
  the most useful thing this release has to say to anyone planning to extend the dataset.
- **Rows are not independent, and row count overstates n.** The 11 discordant,
  CPAD-absent, circularity-clean rows span **8 proteins**: three are intervals of one
  protein and two of another. Any test assuming independent observations should take the
  protein as the unit, not the row.
- **`power_eligible: false` is not a predictor's failure and must never be reported as
  one.** It means the region is too large a fraction of its chain for *any* rank-based
  statistic to return a significant result — a property of the geometry, fixed before any
  score exists. 15 of 27 rows are in that state, and almost every row with a deposited
  fibril structure is. Read `power_limit` for the m, M and chain length behind each one.
- **It is not a random sample of anything.** Rows were found by targeted search,
  including a deliberate search for papers that ran predictors post hoc and
  published the failure. Prevalence must not be estimated from it.
- **6 of 27 rows have `stratum: PENDING`**, one of which can never be resolved — see
  `stratum_not_assignable` above.
- **Four rows rest on an author manuscript and one on a preprint**, each recorded
  as such. In one instance the preprint is *better evidence* than the version of
  record, because copyediting dropped a word that marked a cited study as
  prediction-driven.
- **Rows are not independent.** Five are TRIOBP-1 and six are DISC1, several
  from the same group. CHCHD10 and CHCHD2 are a further non-independent pair, each row
  recording the other.
- **This dataset cannot tell you whether a region aggregates *in a patient*.**
  Most rows are recombinant or cell-based. Separately, insolubility of these
  proteins is now reported in control brains as well as patient brains, so
  **these must not be described as disease-specific aggregates.**

## Files

| file | |
|---|---|
| `aggregation_regions_v1.5.0.json` | **authoritative.** Full records, schema documentation, per-row `notes` |
| `aggregation_regions_v1.5.0.csv` | core columns only, for quick inspection |

**The CSV cannot represent the `notes` object**, and 18 of 27 rows carry one.
Those notes often hold the row's most important caveat — an ex vivo structure
that contradicts it, a numbering error in the source, a sufficiency claim that
is explicitly negative. **Use the JSON for anything that matters.**

Inside the JSON, `dataset_documentation` describes the data; `project_notes`
records the hypotheses and workflow of the project that produced it and **can be
ignored by a consumer**. The partition is a judgement call, made explicit in
`scripts/build_release.py` so that it can be argued with.

## Provenance and reproducibility

`scripts/validate_regions.py` checks the core schema, the controlled
vocabularies, that every sequence matches its stated range in length — segment by segment
for discontinuous rows, because a total-only check passes a sequence split in the wrong
place — that no row carries a retired field, that the citability flags are mutually
consistent, that **no row contradicts itself** about whether its own source has been read,
and that **no field carried by every row is left undocumented**. **It found a real defect
on its first run** — a sequence still carrying a field name retired weeks earlier — and
each check added since was added because it had just caught something: the
self-contradiction check found four rows whose notes still said a source was unread after
it had been read, and the undocumented-schema check found the `power_eligible` and
`power_limit` columns documented nowhere while being on every row. **Every check in that
file exists because the thing it checks for had already happened.**

`scripts/build_release.py` regenerates this release from the working file. The
working file is never edited by it.

## Citation

Mercier des Rochettes, B. (2026). *Experimentally mapped aggregation-critical
protein regions, with circularity, prediction-concordance and
training-set-contamination labels*, version 1.5.0 [Data set]. Zenodo.
**DOI-RESERVE-PENDING**

<https://doi.org/DOI-RESERVE-PENDING>

This is the **version DOI**: it resolves to 1.5.0 and only 1.5.0, which is what a
citation of a specific analysis needs. The **concept DOI**,
**10.5281/zenodo.24290697**, always resolves to whatever version is current — use that
one only when you mean "the latest".

> ### A warning about the v1.4.0 version DOI, which does not work
>
> **`10.5281/zenodo.24342313` never registered.** The v1.4.0 record is published and live
> at <https://zenodo.org/records/24342313>, holds all five files, and displays that DOI —
> but the DOI itself was never registered with DataCite. `doi.org` returns **404** and the
> DataCite API returns **404**, re-checked 20 November 2026, two days after publication.
> Every other version resolves correctly, including the v1.3.0 DOI minted 2½ hours
> earlier on the same day from the same account, so this is a one-off registration
> failure on Zenodo's side and not a problem with the deposit.
>
> **If you need to cite v1.4.0, cite the record URL, not the DOI.** A request has been
> sent to Zenodo support to register it. This was found because **an external
> correspondent could not open a DOI he had been sent**, which is the second instance of
> a rule this project had already written down: *a form displaying a DOI is not a
> registered DOI.* The first instance was caught before anything was published. This one
> was not, and it reached a third party.

**Previous version.** v1.4.0 is **10.5281/zenodo.24342313**
(<https://zenodo.org/records/24342313>, and see the warning above — use the record URL).
It remains citable and unchanged, but **it records DISC1's deleted region as 384-415,
which is wrong by one residue**: the correct range is 384-414, settled from plasmid
sequencing by the corresponding author. It also lacks the six rows added in 1.5.0 and the
`power_eligible` column, so a reader of it cannot tell which rows no predictor could ever
have passed.

**v1.3.0** is **10.5281/zenodo.24339193**
(<https://zenodo.org/records/24339193>). It remains citable and unchanged, but it has no
`structure` column, so it cannot say which deposited fibril structure a row's ordered core
comes from — nor which rows have none at all. It carries the same DISC1 384-415 error.

**v1.2.0** is **10.5281/zenodo.24337561**
(<https://zenodo.org/records/24337561>). It remains citable and unchanged. It carries
seven rows at `stratum: PENDING` whose labels this version assigns from the legacy
predictor run, and it has no `stratum_assignment` column, so it cannot tell a reader
which stratum labels were assigned blind and which were not.

**v1.1.0** is **10.5281/zenodo.24306057**
(<https://zenodo.org/records/24306057>). It remains citable and unchanged. It holds 17
rows against this version's 27, and lacks the four rows added on 17 November 2026 —
ANXA11, TMEM106B, glycinin G4, and the DISC1 interval split into the two sub-intervals
its source actually tested. **Its deposited `CITATION.cff` also carries the pre-1.1.0
title**, a defect recorded in `RELEASE_CHECKLIST.md` and corrected here.

**v1.0.0** is **10.5281/zenodo.24290698** (<https://zenodo.org/records/24290698>). It
has no `cpad_status` column and therefore **cannot tell a reader which rows are
training-set contaminated**. Do not use it in preference to a later version.

> **One correction applies to every version before this one.** v1.0.0, v1.1.0, v1.2.0,
> v1.3.0 and v1.4.0 all record DISC1's deleted region as **384-415**. It is **384-414**.
> Deposited files are frozen and cannot be corrected in place, which is why the correction
> is stated here instead.

## Licence

Copyright © 2026 Bertrand Mercier des Rochettes.

**CC BY 4.0.** Full legal code in `LICENSE`; `CITATION.cff` and `.zenodo.json`
carry the same.

*The copyright line is here, and not in `LICENSE`, because `LICENSE` holds the
unmodified Creative Commons legal code, which names no rights holder by design.
Editing it to insert one would make it something other than the licence it
claims to be. CC BY requires that the licensor be identifiable; this is where
this dataset does that.*

CC BY rather than CC0 because the value here is **curatorial**. The provenance,
the circularity calls and the stratum labels are the work, and attribution is
what lets a reader trace a row back to the sentence that justifies it. CC0 would
maximise reuse but detach the rows from that reasoning.

**What the licence does not cover.** Several rows quote sentences from papers
published under varying licences, some of them closed — Navarro 2026 is Elsevier
and reserves text-and-data-mining rights. Those quotations are made for
scholarly purposes and remain the property of their publishers. **CC BY 4.0
applies to this dataset's curation — the row structure, the labels, the bases
and the notes — not to the quoted material it cites.**
