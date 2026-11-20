# An external fibril-core dataset screened against §3.1b — 20 November 2026

> ## The headline is not the one anybody expected: **10 of 82 regions are power-eligible, across 10 proteins.**
>
> The prior-art audit and this session both predicted ≈ 0. **The measured base rate of
> `power_eligible` among independently curated deposited fibril cores is ~12%**, and that
> is enough proteins to satisfy §4's requirement of five — from a dataset somebody else
> assembled, with two integers per row and no PDFs read.

---

## What was screened, and why this dataset

**Singh J, Jangid R, Srivastava A — *AmyloCore-ML*, bioRxiv `10.64898/2026.09.25.754455`,
v1 1 Oct 2026, v3 18 Nov 2026.** Found by the 20 Nov prior-art audit. It trains a PLM
predictor on Amyloid Atlas fibril cores and **benchmarks AggrescanAI — this project's own
modern arm — on them.**

Screened here is its supplementary `media-2.csv`, whose caption states: *"The non-redundant
dataset comprised 82 continuous amyloid regions corresponding to 69 unique proteins."* It
carries `Protein_length` and `Core_ranges` per protein, which is exactly and only what
§3.1b needs.

**Why their dataset rather than ours.** This project's own claim — that cryo-EM cores are
systematically ineligible — rested on **13 structural rows we selected ourselves**, of which
1 is eligible. A base rate measured on rows we chose is not a base rate. This is 82 rows
chosen by somebody else, for a different purpose, before they had heard of us.

## The arithmetic is the project's own

`scripts/screen_amylocore.py` imports *W* from `scripts/score_rows.py` and reproduces the
tiling of `apply_power_eligible.py`, including the §3.1a short-region fallback. **It
re-derives nothing the committed code already defines** — on 19 Nov an ad-hoc
reimplementation of the *v* pipeline bypassed a frame offset and produced a wrong
correlation.

### Validated against known values before any new number was read

Three rows appear in **both** datasets, curated independently. *m*/*M* agrees **exactly**:

| row | ours | theirs |
|---|---|---|
| TMEM106B 120-254 | 0.488889 | 0.488889 |
| CHCHD2 54-86 | 0.200000 | 0.200000 |
| Orb2 176-206 | 0.034188 | 0.034188 |

## The result

**9 of 81 parsed regions eligible (11.1%), across 9 proteins.** Plus one row their table
records defectively — see below — which is eligible once corrected: **10 of 82, 12.2%.**

| protein | region | chain | *m* | *M* | *m*/*M* |
|---|---|---|---|---|---|
| TAF15 | 135-145 | 592 | 1 | 98 | **0.0102** |
| hnRNPA1 | 209-217 | 372 | 1 | 62 | **0.0161** |
| FapC | 173-185 | 340 | 1 | 56 | **0.0179** |
| cruciferin-3 | 12-26 | 524 *(corrected)* | 2 | 87 | **0.0230** |
| Orb2 | 176-206 | 704 | 4 | 117 | **0.0342** |
| RIPK3 | 447-469 | 518 | 3 | 86 | **0.0349** |
| Lysozyme | 40-52 | 148 | 1 | 24 | **0.0417** |
| RIPK1 | 516-551 | 671 | 5 | 111 | **0.0450** |
| PMEL | 148-183 | 661 | 5 | 110 | **0.0455** |
| Sup35NM | 217-229 | 250 | 2 | 41 | **0.0488** |

Median *m*/*M* across all 81: **0.3158**, six times the bar. Maximum 1.0000.

### A defect in their supplementary, and correcting it adds an eligible row

Their cruciferin-3 row gives `Protein_length` = **12** for a core at **12-26** — a
15-residue region in a 12-residue chain, which is impossible. UniProt **Q96318**
(`CRU3_ARATH`, 12S seed storage protein CRC) is **524** residues [verified at
rest.uniprot.org, 20 Nov 2026]. In the correct frame the row gives *m* = 2, *M* = 87,
**m/M = 0.0230 — eligible.** Reported rather than silently patched; their data is not
edited here.

## What this does to this project's claims

### §4.2's "systematically ineligible" is too strong, and now quantified

**Our 1 of 13 was not bad luck — it is the base rate.** 7.7% against their 11.1%; the two
agree. So the true statement is not *"cryo-EM cores cannot serve as benchmark material"* but:

> **About nine in ten deposited fibril cores cannot enter a min-rank benchmark, and the
> tenth can.** Recruitment from this literature is not impossible; it is roughly ten times
> less efficient than the raw count of structures suggests, and the inefficiency is
> computable in advance from two integers.

That is a weaker claim and a more useful one, because it is actionable rather than closing.

### It reopens a route the 19 November screen closed

`reports/route_b_screen_2026-11-19.md` concluded that recruitment was exhausted and that
**the benchmark might not reach §4's five proteins.** On this evidence that conclusion was
premature. **Ten eligible proteins sit in one externally curated table**, and Amyloid Atlas
itself held **902 entries** as of this check — their 82 is a non-redundant subset of it.

**The gates these ten have NOT passed, and none is a formality:**

1. **CPAD contamination (§5.2b).** Several are near-certain CPAD members — lysozyme,
   hnRNPA1, Sup35, Orb2 (already ours and already `CPAD_MEMBER`). The check is all three
   CPAD tables plus orthology in both OMA and OrthoInspector, per row.
2. **Evidence class.** These are **ordered cryo-EM cores, not necessity mappings.** Under
   §10b route (a) they are weaker evidence than the deletion-mapped DISC1 and TRIOBP-1 rows,
   and the dataset records that distinction on every such row.
3. **Circularity (§5.2b, `found_by`).** Unchecked. Each needs its source read.
4. **The eight-stage recruitment pipeline.** Eligibility is not admission, and this screen
   admits nothing.

### Eligibility is per-REGION, not per-protein — and the dataset proves it

**TAF15 appears in both datasets.** Ours is 7-99: *m*/*M* = 0.1531, **ineligible**. Theirs
also lists 135-145: **0.0102, eligible.** Same protein, same structure class, two cores,
opposite verdicts. **hnRNPA1 likewise** — ours 251-295 at 0.1321, theirs 209-217 at 0.0161.
FapC has four cores of which exactly one passes.

> **So "this protein is ineligible" is a category error.** A protein with a long core may
> also have a short one, and the short one is the benchmark row. Any future screen must
> enumerate every core of every candidate, not take the first or the largest.

## Reproducing this

```
python3 -I scripts/screen_amylocore.py . <their_media-2.csv> out.json
```

The CSV is untrusted downloaded data: it is passed as a path, parsed as CSV, never
executed, and nothing from it reaches `data/regions.json`. **This screen admits no row and
changes no project data.**
