# Candidate screen for five new proteins — 18 Nov 2026

**Partial. Screening complete; no row promoted.** Nothing here is verified to row standard:
no primary paper has been opened for any candidate. Rows enter `data/regions.json` only
after the §7a pipeline, and candidates belong in `data/regions_candidates.json`.

## Method

1. **PDB search** (RCSB): cryo-EM entities, full-text "amyloid fibril", deposited after
   2021-01-01. **1607 hits, 500 retrieved, 94 distinct UniProt accessions.**
2. **CPAD 2.0 screen**, against all three tables as `_CPAD_MEMBERSHIP_CHECK_2026-11-17`
   requires: APR protein list (288), peptide table (2031), structures table (565).
   Today's re-fetch of the APR page differs from yesterday's **only in CSRF tokens and
   anti-bot nonces** — no data change — so the local extract is current.
3. **Controls, to demonstrate sensitivity**: transthyretin, CsgA and tau must all hit.
   All three did, in all three tables.

## THE FINDING THAT MATTERS, AND IT DAMAGES THE HYDROPHILIC-CORE LEAD

**Every hydrophilic-core protein in the glycinin paper's Figure S6 is a CPAD member.**

| S6 hydrophilic core | accession | CPAD |
|---|---|---|
| FUS 6xfm | P35637 | **member** (already a row, already labelled) |
| FapC 9nqd / 9u4u | P0DXF5 | **member** — "FapC amyloid-like fimbriae protein" in the APR list |
| CsgA 8enq | P28307 | **member** — in all three tables, and in our own CPAD control set |

So in the published structures S6 offers, **core architecture and training-set membership
are nearly collinear**. A comparison of hydrophilic-core against hydrophobic-core rows
would be measuring CPAD membership at the same time, and the dataset's one non-CPAD row
with a documented non-hydrophobic core component is glycinin itself — the row that
generated the hypothesis.

**This does not kill the lead. It kills the cheap version of it**, which was to take S6's
published classification as ready-made independent labels. What survives is harder and
better: **a pre-specified, computable core-polarity metric applied to deposited
coordinates** — polar fraction of the ordered core, by a rule fixed in writing before any
*v* is looked at. That keeps the labels independent of our scores without borrowing a
classification that is confounded with CPAD.

## CPAD-absent candidates, confirmed by targeted screen

Each checked by name variants **and** accession against all three tables:

| protein | accession | first deposit | organism | note |
|---|---|---|---|---|
| **TAF15** | Q92804 | 2025-12-03 | *H. sapiens* | 13 structures; FTLD ex vivo filaments |
| **TPPP** | O94811 | 2024-08-09 | *H. sapiens* | tubulin polymerization-promoting protein |
| **ApoA-II** | P09813 | 2023-04-11 | *M. musculus* | AApoAII amyloidosis |
| **Ninjurin-1** | Q92982 | 2024-10-24 | *H. sapiens* | already flagged: construct is a derived 30-mer |

**Rejected as CPAD members** (genuine matches, lines inspected, not substring artefacts):
Orb2 (`Translational regulator orb2`, APR list), FapC, TIA-1 (`Nucleolysin TIA-1`),
TGFBI (peptide table, Q15582 explicit), α-crystallin B (all three).

## A limitation of the bulk screen, stated

The 94-accession pass used a crude name-token heuristic and **over-excludes**: TAF15, TPPP
and ApoA-II were flagged as hits by it and shown absent by the targeted screen. So its
27-protein output is a **conservative lower bound**, not a candidate list, and every
candidate needs the targeted screen before it is called CPAD-absent.

Several of its entries are also not fibril cores at all — γ-secretase subunits, prefoldin
and T-complex chaperonin subunits appear because they co-occur in deposited assemblies.

## Where this stopped

Four CPAD-absent candidates, one short of five, and **none of them read**. The next step
per candidate is the expensive one: publisher PDF including SI, frame fixed and sequence
verified, circularity read out of the Methods, then the §7a ordering — legacy run,
stratum committed, and only then the modern arm.
