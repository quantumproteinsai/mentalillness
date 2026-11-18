# Experimentally mapped aggregation-critical protein regions

**with circularity, prediction-concordance and training-set-contamination labels**

Version 1.3.0 · 21 regions across 11 proteins

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
mapping. Four of these 21 rows are `CIRCULAR`, and they are **kept and
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
| `DISCORDANT` | 10 | experiment and prediction disagree |
| `DISCORDANT_DERIVED` | 1 | disagreement established by comparing two papers, not stated by either — strictly weaker |
| `CONCORDANT` | 5 | the predictors find it |
| `PENDING` | 5 | not yet assessed; requires a predictor run or a published one |

### `stratum_assignment` — was this label assigned blind? *(new in 1.3.0)*

**Not every `DISCORDANT` row counts the same, and this column says which is which.**

Of the 10 `DISCORDANT` rows, **4 were documented in print**, with the disagreeing tools
named by the source paper. **6 were assigned by us**, from our own legacy predictor run,
by a fixed rule: discordant iff the legacy score missed the region at the project's
pre-registered recovery bar. Neither the rule nor the bar was chosen after seeing a
score.

**But the order was wrong, and the column records that.** The protocol requires the label
to be fixed *before* the modern predictor is run on the row, and for these six it was
applied afterwards, when the modern scores were already known. The rule is mechanical and
leaves no threshold to tune — but the choice of *whether to apply it* was made with the
outcome visible. So every affected row carries:

```
stratum_assignment: { ..., confirmatory_eligible: false }
```

**A `DISCORDANT` label alone does not admit a row to the confirmatory set.** Read this
flag. It is why the confirmatory count below is 2 and not 8.

*For the record, applying the rule did not flatter the project's hypothesis: it made the
result worse. That is stated here because the usual objection to a rule applied late is
that it was applied because it helped.*

### `cpad_status` — is the row in the predictor's training set? *(new in 1.1.0)*

**A third kind of circularity, and the one most likely to be missed.** Not a predictor
in the *discovery* path, and not experiment–prediction *agreement*, but **training-set
membership of the benchmark row itself**. A modern predictor that hits a region whose
protein it was trained on has recalled, not predicted.

| value | n rows | meaning |
|---|---|---|
| `CPAD_MEMBER` | 7 | the protein is in CPAD 2.0 |
| `CPAD_ABSENT_ORTHOLOGY_CHECKED` | 10 | absent from CPAD 2.0 **and** from its orthologous group |

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

**Three of the eleven discordant-family rows are CPAD members**, and they are the three
below. The other eight are CPAD-absent and circularity-clean — but only **2 of those 8
are `confirmatory_eligible`** (see `stratum_assignment` above), which is why the usable
count has not moved.

| row | stratum | `cpad_status` |
|---|---|---|
| TRIOBP-1 324-348 | `DISCORDANT` | absent, orthology checked |
| DISC1 384-415 | `DISCORDANT` | absent, orthology checked |
| FUS 39-95 | `DISCORDANT` | **CPAD member** |
| hnRNPA1 251-295 | `DISCORDANT` | **CPAD member** |
| LECT2 55-75 | `DISCORDANT_DERIVED` | **CPAD member** |

The discordant stratum is the only one that can discriminate between predictors. Exclude
the contaminated rows and **2 remain**. Anyone benchmarking a modern predictor on this
dataset without this column would be measuring memorisation on most of the rows that
appear to matter.

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
paper; none was bulk-imported. That is why it is 21 rows and not 17,000.

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

## Composition

| | |
|---|---|
| **proteins** | DISC1 (6) · TRIOBP-1 (5) · tau (2) · α-synuclein · FUS · hnRNPA1 · serum amyloid A · LECT2 · TMEM106B · ANXA11 · **glycinin G4 (soybean)** |
| **circularity** | 17 CLEAN · 4 CIRCULAR |
| **source version** | 17 version of record · 3 author manuscript · 1 preprint |
| **with sequence** | 16 / 21 (each checked to match its stated range in length) |
| **with explicit numbering frame** | 21 / 21 |

Evidence classes span cell-based truncation series, unbiased peptide-array
scans, solid-state NMR, cryo-EM of recombinant fibrils, and **cryo-EM of fibrils
extracted from a patient's kidney** — the only row in the set that is not
recombinant.

## Read these before using a residue number

**Numbering frames in this literature are a trap, and three separate kinds of
trap appear in these 21 rows.**

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

- **It is small, and the usable part is smaller than it looks.** 21 rows. The
  discordant stratum — the only part that can discriminate between predictors — holds
  10 rows and 1 derived, but **3 are CPAD members** and **6 more are not
  `confirmatory_eligible`**, their labels having been assigned after the modern
  predictor had already run. For a predictor trained on CPAD, **2 rows remain**, both of
  them TRIOBP-1 and DISC1, each from a single laboratory lineage. That supports a case
  series on two proteins, not a rate, and it should be read against the AUROC floor below
  before any compute is spent.
- **Rows are not independent, and row count overstates n.** The 8 discordant,
  CPAD-absent, circularity-clean rows span only **5 proteins**: three are intervals of
  one protein and two of another, scored on one profile by one tool. Any test assuming
  independent observations should take the protein as the unit, not the row.
- **It is not a random sample of anything.** Rows were found by targeted search,
  including a deliberate search for papers that ran predictors post hoc and
  published the failure. Prevalence must not be estimated from it.
- **5 of 21 rows have `stratum: PENDING`.**
- **Two rows rest on an author manuscript and one on a preprint**, each recorded
  as such. In one instance the preprint is *better evidence* than the version of
  record, because copyediting dropped a word that marked a cited study as
  prediction-driven.
- **Rows are not independent.** Five are TRIOBP-1 and five are DISC1, several
  from the same group.
- **This dataset cannot tell you whether a region aggregates *in a patient*.**
  Most rows are recombinant or cell-based. Separately, insolubility of these
  proteins is now reported in control brains as well as patient brains, so
  **these must not be described as disease-specific aggregates.**

## Files

| file | |
|---|---|
| `aggregation_regions_v1.3.0.json` | **authoritative.** Full records, schema documentation, per-row `notes` |
| `aggregation_regions_v1.3.0.csv` | core columns only, for quick inspection |

**The CSV cannot represent the `notes` object**, and 15 of 21 rows carry one.
Those notes often hold the row's most important caveat — an ex vivo structure
that contradicts it, a numbering error in the source, a sufficiency claim that
is explicitly negative. **Use the JSON for anything that matters.**

Inside the JSON, `dataset_documentation` describes the data; `project_notes`
records the hypotheses and workflow of the project that produced it and **can be
ignored by a consumer**. The partition is a judgement call, made explicit in
`scripts/build_release.py` so that it can be argued with.

## Provenance and reproducibility

`scripts/validate_regions.py` checks the core schema, the controlled
vocabularies, that every sequence matches its stated range in length, that no
row carries a retired field, and that the citability flags are mutually
consistent. **It found a real defect on its first run** — a sequence still
carrying a field name retired weeks earlier — which is the argument for shipping
it alongside the data.

`scripts/build_release.py` regenerates this release from the working file. The
working file is never edited by it.

## Citation

Mercier des Rochettes, B. (2026). *Experimentally mapped aggregation-critical
protein regions, with circularity, prediction-concordance and
training-set-contamination labels*, version 1.3.0 [Data set]. Zenodo.
**DOI-RESERVE-PENDING**

<https://doi.org/DOI-RESERVE-PENDING>

This is the **version DOI**: it resolves to 1.3.0 and only 1.3.0, which is what a
citation of a specific analysis needs. The **concept DOI**,
**10.5281/zenodo.24290697**, always resolves to whatever version is current — use that
one only when you mean "the latest".

**Previous version.** v1.2.0 is **10.5281/zenodo.24337561**
(<https://zenodo.org/records/24337561>). It remains citable and unchanged. It carries
seven rows at `stratum: PENDING` whose labels this version assigns from the legacy
predictor run, and it has no `stratum_assignment` column, so it cannot tell a reader
which stratum labels were assigned blind and which were not.

**v1.1.0** is **10.5281/zenodo.24306057**
(<https://zenodo.org/records/24306057>). It remains citable and unchanged. It holds 17
rows against this version's 21, and lacks the four rows added on 17 November 2026 —
ANXA11, TMEM106B, glycinin G4, and the DISC1 interval split into the two sub-intervals
its source actually tested. **Its deposited `CITATION.cff` also carries the pre-1.1.0
title**, a defect recorded in `RELEASE_CHECKLIST.md` and corrected here.

**v1.0.0** is **10.5281/zenodo.24290698** (<https://zenodo.org/records/24290698>). It
has no `cpad_status` column and therefore **cannot tell a reader which rows are
training-set contaminated**. Do not use it in preference to a later version.

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
