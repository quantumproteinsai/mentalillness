# Route (b) recruitment — first screen, 19 November 2026

**The registered search shape**, written 18 Nov in `reports/recruitment_tracker.md` under
the §3.1b pause, before any of today's work:

> Proteins of **≥ 400 residues** with a mapped aggregation-critical region of **≤ 20
> residues**, found by **deletion, truncation, alanine scan or peptide-array**, **post-2015**,
> **CPAD-absent**.

**Why this is now the only route that can move the confirmatory cell.** Measured today:
*not one of the thirteen structural rows in the dataset is `power_eligible`*, and all four
rows in the benchmark's scarce cell have no structure at all. §10b selects for long ordered
cores and cannot produce a benchmark row. The scarce cell holds **4 rows across 2
proteins**; §4 needs **5 proteins**. **Three new proteins are required.**

## Result of this screen: ZERO candidates

**All provenance here is `[SNIPPET]` or `[EMPTY]`. Nothing was read, nothing is admitted,
and no row is proposed.** Recorded so the negative is reproducible rather than repeated.

| # | query (verbatim) | branch | outcome |
|---|---|---|---|
| 1 | `aggregation-critical region mapped by deletion truncation large protein "required for aggregation" cells 2020..2026` | deletion/truncation | **[EMPTY]** — top hit is our own DISC1 row's source |
| 2 | `UBQLN2 optineurin SQSTM1 aggregation-prone region deletion mapping necessary for inclusion formation` | deletion | **[EMPTY]** |
| 3 | `CRMP1 dysbindin aggregation-prone region mapped deletion Korth insoluble proteome schizophrenia` | deletion | **[SNIPPET]** — no short region mapped; see below |
| 4 | `Matrin-3 ataxin-2 aggregation "deletion" short region required for inclusion formation residues` | deletion | **[SNIPPET]** — two near-misses, both fail; see below |
| 5 | `alanine scanning peptide array identified short aggregation determinant segment necessary full-length protein inclusion bodies` | alanine scan / peptide array | **[EMPTY]** |

### The two near-misses, and why each fails the registered shape

**Matrin-3** (847 aa — the right size class). What is deleted is **whole RRM domains**,
roughly 80–100 residues, not a region ≤ 20. The reported phenotype is **phase separation
into intranuclear droplets**, and one report states that mutant Matrin-3 overexpression
*did not* produce obvious inclusion-like structures. **Fails on region length and on
evidence type:** droplet formation is not the aggregation this dataset records.

**Ataxin-2** (1313 aa). The mapped element is the **C-terminal intrinsically disordered
region**, again a whole domain rather than ≤ 20 residues. More decisively, the published
requirement is that the cIDR is needed for **the aggregation of *other* proteins** — FUS and
C9orf72 dipeptide repeats — and for RNP granule formation. **That is a trans requirement,
not a mapping of ataxin-2's own aggregation-critical region**, and admitting it would record
a claim the source does not make.

**CRMP1 and dysbindin** were the most promising names going in, because both are documented
as aggregating in schizophrenia brain. **They were found by antibody and by insoluble-proteome
proteomics, not by deletion mapping**, and no short necessary region appears to have been
published for either. They are candidates for a *protein*, not for a *region*, and this
dataset records regions.

## What the screen actually shows, which is more useful than the zero

**The three method branches in the registered shape are not used on large proteins.**
Alanine scanning and peptide arrays are applied almost exclusively to **short peptides
already known to aggregate** — Aβ40, Aβ42, isolated APRs — where the question is which
residue tunes a known aggregator, not which 20 residues of an 800-residue protein are
necessary. Deep mutational scanning has the same shape. So branch (iii) and branch (iv) of
the registered shape are, on this evidence, close to empty by construction.

**That leaves deletion and truncation mapping in cells — and that literature is dominated
by one group.** DISC1, TRIOBP-1 and NPAS3 all come from Korth and Bradshaw. The dataset
already carries this as a stated limitation on the DISC1 row: *"same lab as the TRIOBP-1
work, so this is a second case rather than independent replication."* **Widening the route
(b) pool by literature search is therefore not merely slow; it may be searching for a
literature that does not exist at the needed size.**

This should not be over-read from five queries. It is a **first screen**, not a systematic
review, and a targeted search on named proteins would still be worth running. But the
cheapest next action is not another query.

## Recommended next action: ask the one person who would know

**Nicholas Bradshaw is the corresponding author on both route (b) rows this project has,
he is in active correspondence as of today, and he offered unprompted to help.** He and
Beti Zaharija have spent a decade doing precisely the experiment this screen is looking
for, and they will know in one sentence what five more queries will not find:

> *Are there other proteins — in your work or anyone's — where a short region of a large
> protein has been shown necessary for aggregation by deletion or truncation, the way
> 384-414 and 324-348 were?*

**Cost: one paragraph in a reply he is already expecting.** Expected yield: higher than
anything in this screen. **And if the answer is "not really", that is the finding** — it
would mean the benchmark cannot reach *n* = 5 proteins on the current rule, which is a
result about the field rather than a failure of ours, and it should be reported as one
rather than absorbed as an unmet target.

## What must NOT happen

- **The *m*/*M* bar must not be relaxed to admit rows.** It is an information limit, not a
  convention: below it no rank-based statistic can return a significant *p*. Widening it
  would manufacture rows that cannot be recovered in principle, which is the opposite of
  more power.
- **Rows must not be drawn from the structural pool to make up the number.** They are
  benchmark-ineligible by construction, as the thirteen already here demonstrate.
- **Nothing in this file is a row.** Nothing here has been read past a search snippet.
