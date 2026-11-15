# Working on this project

This file is loaded into context at the start of every session in this folder.
Read `STATE.md` before proposing anything; parts of the original plan did not
survive contact with the primary sources, and `STATE.md` is where that is
recorded.

## What this project is

A benchmark of protein aggregation predictors against experimentally mapped
aggregation-critical regions in schizophrenia-associated scaffold proteins.
The question:

> Do modern aggregation predictors recover the experimentally mapped regions of
> DISC1 and TRIOBP-1 that the 2004-2010 generation missed, and if not, what
> structural feature are they all missing?

The earlier form -- *do predictors fail here?* -- is already answered in print by
both primary papers. Those failures are cited evidence, not a result to
establish. Do not propose re-establishing them.

## Three rules, each learned expensively

**1. A number is quoted from a source somebody opened, or it is declared
unmeasured.** Everything under `research_notes/` is machine-generated and
unverified. Entries in `data/references_to_check.json` carry
`verified_against_publisher_pdf`, false until a human opens the PDF and checks
the claim. Never cite across that line. When reporting a number found by search,
say whether it was READ, a SNIPPET, or an EMPTY query result.

**2. Check the margin against the error bar before spending anything.** If the
difference to be reported is smaller than the uncertainty of the method
reporting it, no further work rescues it. Say so and stop. This retired four
claims on the companion project after the compute had been spent.

**3. Audit the premises of the task, not only the literature.** The most
valuable findings here were facts about proposed comparisons, not about papers:
two crystals that were not independent determinations, two sequences identical
between species so a contrast could not exist, a residue number from a review
that disagreed with the database. If a proposed experiment is impossible or
uninformative, say so -- that is the finding.

## Pre-registration is the point, not a formality

The statistic, the decoy construction and the success threshold are written down
*before* any predictor is run. Scoring first and choosing the statistic
afterwards produces a result that looks convincing and means nothing. If asked
to run a predictor before the analysis is pre-registered, say no and explain why.

## Out of scope

**Quantum chemistry and interaction energies.** There are no deposited aggregate
coordinates for any psychiatric protein: 0 of 5 candidates, and none of the 51
steric-zipper entities in the PDB. That is enumerated in `STATE.md`, not
assumed. It is a finding to report, not a gap to work around. Related work on
amyloid segment crystals lives in a separate project and does not belong here.

**Platforms, databases and general tools.** They come later, if the first result
holds. Scope discipline is what makes the question answerable in months.

## The validation set is the core asset

`data/regions.json` is more important than any analysis built on it, and is
intended to be published first, as a dataset with its own DOI. Two columns carry
the weight and must never be dropped:

- `construct` -- a region can be necessary in one construct and dispensable in
  another, and both results can be correct. A benchmark that ignores this scores
  against a moving target.
- `found_by` -- a region discovered *by prediction* is circular for a predictor
  benchmark. Those rows are analysed separately, not silently included.

Current count is 10 rows against a floor of 15. Widening it to every protein
with fragment-level aggregation mapping -- not only the psychiatric ones -- is
the outstanding task.

## Numbering traps, both real

- **TRIOBP-1**: use the 652-residue frame of NP_008963.3 (UniProt Q9H2D6-7).
  Papers on the older 593-residue frame need **59 added**. One paper gives the
  short variant as 593 in one place and 597 in another.
- **DISC1**: UniProt Q9NRI5, canonical, 854 aa. Verify residue numbers against
  UniProt, never against a review.

## Housekeeping

Commit before running anything that writes results; on the companion project
the only thing that saved six hours of computation was that its output file
happened to be tracked. This repository has no remote, and whether to add one
is the author's decision.
