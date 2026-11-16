# In silico aggregation in mental illness

A benchmark of protein aggregation predictors against experimentally mapped
aggregation-critical regions, in schizophrenia-associated scaffold proteins.

**The validation set is published.** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24290698.svg)](https://doi.org/10.5281/zenodo.24290698)

> Mercier des Rochettes, B. (2026). *Experimentally mapped aggregation-critical
> protein regions, with circularity and prediction-concordance labels*, v1.0.0
> [Data set]. Zenodo. <https://doi.org/10.5281/zenodo.24290698>

17 regions across 8 proteins, every row read from its source paper. CC BY 4.0.
The analysis built on it is **not** published and is not finished; the dataset
stands on its own and was deposited first deliberately.

**Start with [`STATE.md`](STATE.md).** It is the current position, and parts of
the original plan did not survive contact with the primary sources.

## The question

Do modern aggregation predictors recover the experimentally mapped regions of
DISC1 and TRIOBP-1 that the 2004–2010 generation missed, and if not, what
structural feature are they all missing?

The earlier form of this question — *do predictors fail here?* — is already
answered in print, by both primary papers. The failures are now cited evidence
rather than a result to establish.

## What is here

| path | what it is |
|---|---|
| `STATE.md` | current position, with the three corrections that matter |
| `data/regions.json` | **the validation set: 17 rows**, with construct, circularity, stratum and source-version columns. The working file |
| `release/` | what was deposited at 10.5281/zenodo.24290698, derived from it by `scripts/build_release.py` |
| `data/references_to_check.json` | sources nobody has opened. A lead is not a fact |
| `scripts/gatekeeper_density.py` | reproduces the gatekeeper separation (`python3 scripts/gatekeeper_density.py`) |
| `reports/PDFs_to_obtain.md` | papers behind paywalls, ranked by what changes if you read one |
| `research_notes/` | six literature sweeps. **Machine-generated and unverified** |

## Two standing rules, both learned the hard way

**A number is quoted from a source you opened, or it is declared unmeasured.**
Everything under `research_notes/` is a lead. Entries in
`references_to_check.json` carry `verified_against_publisher_pdf`, and it is
`false` until somebody opens the PDF and checks the claim.

**Check the margin against the error bar before spending anything.** If the
difference you want to report is smaller than the uncertainty of the method
reporting it, no amount of further work rescues it.

## Not in scope

Quantum chemistry. There are no deposited aggregate coordinates for any
psychiatric protein — 0 of 5 candidates, and none of the 51 steric-zipper
entities in the PDB is a psychiatric protein — so interaction energies cannot be
computed here. That is a finding, recorded in `STATE.md`, not a gap to work
around.
