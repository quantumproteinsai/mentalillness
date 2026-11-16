# Experimentally mapped aggregation-critical protein regions

**with circularity and prediction-concordance labels**

Version 1.0.0-draft · 17 regions across 8 proteins

---

## What this is

A hand-curated set of protein regions that **experiment** has shown to be
required for, or to constitute the core of, protein aggregation. Every row was
established by opening the source paper and checking the claim against it.

It is small on purpose. It is not a mined database, and it is not a
comprehensive survey. **Every row here is one somebody read.**

## What it is for

It was built to benchmark sequence-based aggregation predictors, and it carries
three columns that most aggregation datasets lack — each of which exists because
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
mapping. Three of these 17 rows are `CIRCULAR`, and they are **kept and
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
| `DISCORDANT` | 4 | experiment and prediction disagree, documented in print with the tools named |
| `DISCORDANT_DERIVED` | 1 | disagreement established by comparing two papers, not stated by either — strictly weaker |
| `CONCORDANT` | 4 | the predictors find it |
| `PENDING` | 8 | not yet assessed; requires a predictor run or a published one |

## Composition

| | |
|---|---|
| **proteins** | TRIOBP-1 (5), DISC1 (5), tau (2), α-synuclein, FUS, hnRNPA1, serum amyloid A, LECT2 |
| **circularity** | 14 CLEAN · 3 CIRCULAR |
| **source version** | 14 version of record · 2 author manuscript · 1 preprint |
| **with sequence** | 11 / 17 (each checked to match its stated range in length) |
| **with explicit numbering frame** | 13 / 17 |

Evidence classes span cell-based truncation series, unbiased peptide-array
scans, solid-state NMR, cryo-EM of recombinant fibrils, and **cryo-EM of fibrils
extracted from a patient's kidney** — the only row in the set that is not
recombinant.

## Read these before using a residue number

**Numbering frames in this literature are a trap, and three separate kinds of
trap appear in these 17 rows.**

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

- **It is small.** 17 rows. The discordant stratum — the only part that can
  discriminate between predictors — holds **4 documented rows**. That supports a
  case series, not a rate.
- **It is not a random sample of anything.** Rows were found by targeted search,
  including a deliberate search for papers that ran predictors post hoc and
  published the failure. Prevalence must not be estimated from it.
- **8 of 17 rows have `stratum: PENDING`.**
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
| `aggregation_regions_v1.0.0-draft.json` | **authoritative.** Full records, schema documentation, per-row `notes` |
| `aggregation_regions_v1.0.0-draft.csv` | core columns only, for quick inspection |

**The CSV cannot represent the `notes` object**, and 12 of 17 rows carry one.
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

Not yet deposited; no DOI assigned. **Do not cite this version as archival.**
See `CITATION.cff` for the intended citation once deposited.

## Licence

Not yet chosen — see the release checklist. Note that several rows quote
sentences from papers under varying licences; quotation for scholarly purposes
is normal practice, but the licence choice should be made deliberately rather
than inherited by default.
