# In silico aggregation in mental illness

A benchmark of protein aggregation predictors against experimentally mapped
aggregation-critical regions, in schizophrenia-associated scaffold proteins.

**The validation set is published.** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24290697.svg)](https://doi.org/10.5281/zenodo.24290697)

> Mercier des Rochettes, B. (2026). *Experimentally mapped aggregation-critical
> protein regions, with circularity, prediction-concordance and
> training-set-contamination labels*, v1.5.0 [Data set]. Zenodo.
> <https://doi.org/10.5281/zenodo.24290697>

**Cite the concept DOI `10.5281/zenodo.24290697`, not the v1.4.0 version DOI.**
It resolves correctly to the latest record. The version DOI
`10.5281/zenodo.24342313` **does not resolve**: the record is published at Zenodo
and displays that DOI, but it was never registered with DataCite — `doi.org`
returns 404, the DataCite API returns 404 and the handle API returns
`responseCode 100`, handle not found, re-checked **20 Nov 2026**, two days after
publication. **v1.4.0 is the only version that failed.** The v1.3.0 DOI, minted
2½ hours earlier the same day from the same account, resolves; so do v1.1.0,
v1.2.0 and the concept DOI. So this is a one-off registration failure on Zenodo's
side, not an account or workflow problem, and it cannot be repaired from this
repository — see
[`correspondence/2026-11-20_zenodo_support_request.md`](correspondence/2026-11-20_zenodo_support_request.md).

This was found on 19 Nov 2026 because **an external correspondent could not open
a DOI we had sent him**, and it is the second instance of the rule already in
`STATE.md`: *a form displaying a DOI is not a registered DOI.* The first instance
was caught before anything was published; this one was not, and it reached a
third party.

**The deposited version v1.4.0 holds 21 regions across 11 proteins** — this line
said 24 and 14 until 20 Nov 2026, and both were wrong; the deposited artefact
itself says 21 and 11. Every row read from its source paper. CC BY 4.0. The
analysis built on it is **not** published and is not finished; the dataset stands
on its own and was deposited first deliberately.

**v1.5.0 is prepared and awaiting its reserved DOI**: 27 regions across 17
proteins. It corrects DISC1's deleted region from 384-415 to **384-414**, settled
from plasmid sequencing by the corresponding author — **every deposited version
so far carries the wrong value**. It also adds CHCHD10, CHCHD2, TAF15, Orb2,
β2-microglobulin and SOD1, admitted 18–19 November 2026 under the
structural-recruitment rule ([`PREREGISTRATION.md`](PREREGISTRATION.md) §10b),
and promotes `power_eligible` to a core column. Cite the deposit for a specific
analysis; read `data/regions.json` for the current position.

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
| `PREREGISTRATION.md` | the statistic, the thresholds and the eligibility rule, frozen at `freeze-2026-11-17`, with every amendment dated and marked for whether scores had been seen |
| `data/regions.json` | **the validation set: 27 rows** (deposit v1.4.0 has 21), with construct, circularity, stratum, power-eligibility and source-version columns. The working file |
| `release/` | what was deposited at 10.5281/zenodo.24290697, derived from it by `scripts/build_release.py` |
| `manuscript/benchmark_draft.md` | the write-up: a null benchmark, an information limit, a polar-core association, and five named defects. **Draft, not submitted** |
| `data/references_to_check.json` | sources nobody has opened. A lead is not a fact |
| `scripts/score_rows.py` | the §3.1 statistic, and the floor and information-limit warnings it prints on every run |
| `scripts/gatekeeper_density.py` | reproduces the gatekeeper separation (`python3 scripts/gatekeeper_density.py`) |
| `data/phi_spec.json`, `data/coordinate_manifest.json` | every input to the core-polarity metric, and the SHA-256 of all 22 deposited coordinate files analysed |
| `scripts/fetch_coordinates.py` | fetches those coordinates from RCSB and verifies each checksum; a mismatch exits non-zero rather than warning |
| `reports/PDFs_to_obtain.md` | papers behind paywalls, ranked by what changes if you read one |

## Before you benchmark anything against regions like these

Under the null, the top-ranked window of a chain falls inside a mapped region of
*m* windows, out of *M*, with probability **exactly *m*/*M***. That is the
smallest *p* obtainable from the region's **best window rank** — the family this
project's statistic belongs to. Where it exceeds your α, no better predictor and
no amendment *within that family* rescues the row; only a longer protein or a
shorter mapped region.

**That sentence said "any rank-based statistic" until 20 Nov 2026, and it was too
strong.** A rank-sum over the *m* in-region against the *M*−*m* out-of-region
scores has minimum attainable one-sided *p* = 1/C(*M*,*m*) — on this project's
β2-microglobulin row (*m* = 10, *M* = 16) that is 1.25×10⁻⁴ against *m*/*M* =
0.625. It is a limit on how broadly the claim may be stated and **not a rescue**:
a rank-sum answers a different question, the tiled windows are not independent,
and changing statistics after seeing scores is what the pre-registration exists
to forbid. The general result — minimum attainable *p* under discreteness, used
to exclude untestable hypotheses — is **Tarone's rule**, Tarone RE (1990),
*Biometrics* **46**:515–522. Cite that; what is new here is the application.

**13 of the 23 scored rows here exceed *m*/*M* > 0.05.** The check needs two
integers, no predictor and no compute, and it is worth running before a candidate
paper is read in full.


## Three standing rules, all learned the hard way

**A number is quoted from a source you opened, or it is declared unmeasured.**
Entries in `data/references_to_check.json` carry
`verified_against_publisher_pdf`, and it is `false` until somebody opens the PDF
and checks the claim.

*Machine-generated literature sweeps were used as leads during this work and are
deliberately not published here. Nothing in `data/` or `release/` rests on them:
every row of the dataset cites a source somebody opened, and the sweeps were
never citable under the rule above. They are kept privately because an unverified
lead presented in a public repository is read as a finding no matter how it is
labelled.*

**Check the margin against the error bar before spending anything.** If the
difference you want to report is smaller than the uncertainty of the method
reporting it, no amount of further work rescues it. The *m*/*M* bound above is
this rule in its cheapest form, and it was still found one step too late.

**Audit the premises of the task, not only the literature.** The most useful
findings here were facts about proposed comparisons rather than about papers:
two crystals that were not independent determinations, two sequences identical
between species so the intended contrast could not exist, a residue number from a
review that disagreed with the database, and a 2026 paper comparing predictions
in one numbering frame against an experimental region quoted in another. **If a
proposed experiment is impossible or uninformative, that is the finding.**

## Not in scope

Quantum chemistry. There are no deposited aggregate coordinates for any
psychiatric protein — 0 of 5 candidates, and none of the 51 steric-zipper
entities in the PDB is a psychiatric protein — so interaction energies cannot be
computed here. That is a finding, recorded in `STATE.md`, not a gap to work
around.
