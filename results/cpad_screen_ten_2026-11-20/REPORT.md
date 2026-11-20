# The ten power-eligible regions against CPAD 2.0 — 20 November 2026

> ## **One of the ten survives.** Eight are CPAD members outright; TAF15 is training-set-uncertain
> through FUS. The survivor is **cruciferin-3 (Q96318) 12-26** — a plant seed-storage protein.
>
> **The two gates compound: 10 of 82 regions passed §3.1b, and 1 of those 10 passes §5.2b.
> The joint yield from an externally curated fibril-core dataset is 1 in 82.**

---

## What was checked, and against what

`PREREGISTRATION.md` §5.2b item 4: every row is checked against **all three** CPAD 2.0 datasets,
plus an orthologue check in **both** OMA and OrthoInspector, because AggrescanAI's shipped CPAD90
model is CPAD plus homologues transferred through HoTIDP.

**All three tables were read complete and verified against the database's own totals:**

| table | read | stated | contiguous |
|---|---|---|---|
| APR protein list | 286 option strings / **259 unique names** | 268 | n/a |
| peptide table | **2031** | 2031 | P-0001..P-2031, zero gaps |
| structures table | **565** | 565 | S-0001..S-0565, zero gaps |

**Controls, through the same query.** Positive: tau (APR 1 / pep 139 / str 17), β2-microglobulin
(1 / 72 / 33), transthyretin (1 / 9 / 152) — all three hit in all three tables. Negative: **DISC1 and
TRIOBP-1 return zero in all three**, as they have since 17 November. An absence is only as good as
the demonstrated sensitivity of the search that produced it.

## The result

| protein | APR | pep | str | verdict |
|---|---:|---:|---:|---|
| Sup35NM | 1 | **253** | 9 | CPAD_MEMBER |
| Lysozyme | 2 | 34 | 13 | CPAD_MEMBER |
| FUS *(not a candidate — see TAF15)* | 1 | 49 | 5 | CPAD_MEMBER |
| hnRNPA1 | 0 | 0 | 4 | CPAD_MEMBER |
| PMEL | 1 | 3 | 0 | CPAD_MEMBER |
| RIPK3 | 1 | 1 | 2 | CPAD_MEMBER |
| RIPK1 | 1 | 0 | 2 | CPAD_MEMBER |
| FapC | 1 | 0 | 0 | CPAD_MEMBER |
| Orb2 | 1 | 0 | 0 | CPAD_MEMBER |
| **TAF15** | 0 | 0 | 0 | **TRAINING_SET_UNCERTAIN** — see below |
| **cruciferin-3** | 0 | 0 | 0 | **CPAD_ABSENT_ORTHOLOGY_CHECKED** |

**Four of the eight members would have been cleared wrongly by a one-table check.** hnRNPA1 is in
the structures table only; FapC, Orb2 and RIPK1 are in the APR list only. The 17 November rule
*"any future row must be checked against all three"* earned its keep four more times today.

## TAF15 — a correction to an existing row, not just a screen result

TAF15 is absent from all three CPAD tables. But **its OrthoInspector Eukaryota2023 group contains
four human proteins** — TAF15 (Q92804), **FUS (P35637)**, EWSR1 (Q01844) and ZRANB2 (O95218) — and
**FUS is CPAD-present in all three tables** (APR 1, peptides 49, structures 5) and is already a row
in this dataset.

Under §5.2b item 4 — *"a row whose protein has an orthologue in CPAD is flagged
`TRAINING_SET_UNCERTAIN`"* — **TAF15 is training-set-uncertain.**

> **The dataset already knew this and recorded the opposite.** The TAF15 row's own `cpad_basis`
> says, verbatim: *"NOTE THAT ITS HOMOLOGUE FUS IS A CPAD MEMBER and is already a row in this
> dataset; TAF15 itself is not."* — and then assigns `CPAD_ABSENT_ORTHOLOGY_CHECKED`. The field
> recorded the homologue-transfer risk and the status denied it. That is now corrected.

**OMA alone would have missed it.** OMA group 1120003 holds **exactly one** human protein, TAF15
itself. This is the FUS/TAF15 repeat of the 17 November MPRIP/TRIOBP finding, and it is the second
time one orthology database has been demonstrably insufficient. **Querying one is not querying
orthology.**

**What this correction does and does not move.** TAF15 7-99 is `stratum: DISCORDANT` but
`power_eligible: false` (*m*/*M* = 0.1531), so it was **already excluded from the confirmatory
statistic by §3.1b** before this check ran. **No reported number changes.** What changes is
§5.2b's statement that *"No row carries `TRAINING_SET_UNCERTAIN`"*, which is now false.

## Cruciferin-3 — the one survivor, checked properly

Absent from all three CPAD tables. Its orthology group was enumerated in both databases and
**every member was checked in its own right**, per the MPRIP precedent:

- **OrthoInspector** in-group paralogues: CRU1_ARATH (P15455), CRU2_ARATH (P15456),
  CRU4_ARATH (Q9ZWA9) — all three **absent from all three CPAD tables**.
- **OMA** group 1133828 (37 members) contains **GLYG4_SOYBN** — glycinin G4, which is *already a row
  in this dataset* and is itself `CPAD_ABSENT_ORTHOLOGY_CHECKED`. Re-checked here: absent.
- A generic `legumin` sweep of all three tables: zero.

### But it is not independent of a row we already hold

**Cruciferin-3 and glycinin G4 are orthologues in the same OMA group.** §3's Stouffer and Fisher
combinations treat rows as independent. **Two orthologous seed-storage globulins are not two
independent tests of a predictor.** If cruciferin-3 is ever admitted, that dependence must be
declared and the combination adjusted or one row dropped. *Recorded now, before either is scored.*

## What this does to the recruitment question — including a correction to this session's own claim

Earlier today this session wrote that ten eligible proteins meant *"the confirmatory cell has a route
it didn't have this morning."* **With the CPAD gate applied, that route yields one protein, and
scaling it will not yield many more.**

The arithmetic, stated plainly:

- AmyloCore-ML drew **82 non-redundant regions from 69 unique proteins** out of an Amyloid Atlas
  snapshot of **797 entries** (April 2026). Our 20 Nov check of the Atlas found **902 entries**.
- The Atlas is **heavily redundant by protein** — their Figure 2a gives tau 200, α-synuclein 191,
  amyloid-β 94, IAPP 38, transthyretin 29, TMEM106B 27, prion 16, TDP-43 15. **797 entries collapsed
  to 69 proteins.**
- So 902 entries would be expected to collapse to roughly the same order — perhaps **75-80 unique
  proteins**, not 900. At a joint yield of **1 in 82 regions**, the whole remaining Atlas is worth on
  the order of **one more candidate**.

> **`reports/route_b_screen_2026-11-19.md` concluded that recruitment was exhausted. Its reasoning
> was wrong — it screened per-protein where eligibility is per-region, and it found zero where the
> true eligible rate is ~12%. Its conclusion was close to right anyway.** §4's requirement of five
> proteins is not reachable from deposited fibril cores. That is a fact about how the field measures
> aggregation, and it is a result, not a failure to work around.

## One comparison deliberately NOT made

**90% of the power-eligible regions are CPAD-implicated. Whether that is higher than the background
CPAD rate among all 69 of their proteins is UNMEASURED.** It is tempting to say the two gates are
anti-correlated — that short well-defined cores belong to the famous amyloids, which are the ones in
CPAD — but that is a hypothesis, and the measurement that would test it (all 69 proteins against all
three tables) has not been run. **No such claim is made here.**

## Reproducing this

```
python3 -I scripts/cpad_apr_list.py <aprs_page.html> > apr_names.txt
python3 -I scripts/cpad_screen.py apr_names.txt <pep_dir> <str_dir>
```

**No CPAD content is stored in this repository** — CPAD 2.0's terms forbid redistribution. What is
stored is the selection rule, the accessions, the scripts and the verdicts. Anyone with their own
access can rebuild the check exactly.

**A note on the fetch, because it nearly produced a false result.** The browse pages serve 30 entries
per request. A 68-request sweep triggered the server's `error code : 338` validation interstitial at
page 57, and every subsequent request — including all 19 structure pages — returned a 1 kB CAPTCHA
page instead of data. The first parse of that partial capture reported **"1680 entries, contiguous
from P-0001"**, which is true and completely misleading: contiguity from the start says nothing about
a tail that was never served. **The integrity check that caught it is comparing the row count against
the database's own stated total**, not checking that the ids are contiguous. Pages were refetched
with backoff until all three tables matched their stated totals.
