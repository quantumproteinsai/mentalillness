# Two dataset entries, for checking — DISC1 384-414 and TRIOBP-1 324-348

Prepared for **N. Bradshaw and B. Zaharija**, 19 November 2026, at their offer to confirm
the records. Extracted from `data/regions.json` (working file, ahead of the deposit).

**How to mark this up.** Every claim carries a tag saying where it came from. You only need
to look hard at the **[INTERPRETATION]** lines — those are mine, not yours, and they are
where I am most likely to have put a line in the wrong place.

| tag | means |
|---|---|
| **[READ]** | quoted or taken directly from your published text |
| **[COMPUTED]** | derived by me from a sequence database, arithmetic only |
| **[INTERPRETATION]** | **my judgement about what your data establish — please challenge** |
| **[PERS. COMM.]** | from your email of 19 Nov 2026 |

A "✗" anywhere, with a word or two, is all I need. **Nothing here is published**; the
analysis built on these rows is unfinished and unsubmitted.

---

## Entry 1 — DISC1, residues 384-414

**Frame:** UniProt Q9NRI5, canonical, 854 aa. **[COMPUTED]** Verified byte-identical to
RefSeq NP_061132.2, so the numbers in Beti's thesis transfer with no offset.

**Sequence (31 aa):** `EQEKISLHFQLPSRQPALSSFLGHLAAQVQA` **[COMPUTED]** — sliced from
Q9NRI5 at 384-414.

| # | claim | tag |
|---|---|---|
| 1.1 | The deleted region is **384-414**, 31 residues, the construct being DISC1 1-383 joined to DISC1 415-854. | **[PERS. COMM.]** |
| 1.2 | Deleting it abolishes aggregation in full-length 1-854, and in 1-836 and 1-655. | **[READ]** |
| 1.3 | 1-383 does not aggregate; 1-415 does. | **[READ]** |
| 1.4 | The whole linker 384-538 aggregates when expressed alone. | **[READ]** |
| 1.5 | **384-414 is recorded as NECESSARY but NOT as demonstrated SUFFICIENT**, because it was never expressed alone — what was expressed alone is 384-538 and 1-415. | **[INTERPRETATION]** |
| 1.6 | The region lies immediately C-terminal of the D domain (257-383) and outside all four ESPRIT domains. | **[READ]** |
| 1.7 | Region found by truncation and deletion, with **no aggregation predictor in the discovery path**. | **[INTERPRETATION]** |
| 1.8 | The five aggregation predictors in Beti's thesis §4.3.5 were run **after** the region was mapped, as a post-hoc check, so they do not make the row circular. | **[INTERPRETATION]** |

> **1.5 is the one I would most like your view on.** The Discussion of the 2024 paper says
> 384-415 "was both sufficient for aggregation", which reads stronger than what I have
> recorded. If you consider sufficiency established for the 31-mer itself, I have drawn the
> line in the wrong place and will change it.

> **1.8, for completeness rather than because I doubt it.** Four of the five predictors in
> the thesis gave hotspots dispersed through the whole protein and did not single out the
> linker. **ANuPP was the exception** and named 387-395 and 400-415, both inside this
> region. I record ANuPP as prior art on the prediction question, not as contaminating the
> mapping.

---

## Entry 2 — TRIOBP-1, residues 324-348

**Frame:** 652-residue, NP_008963.3 / UniProt Q9H2D6-7. **[COMPUTED]** Work in the older
593-residue frame needs **+59**.

**Sequence (25 aa):** `PLRENKRVPLTALLNQSRGERRGPP` **[READ]** — matches Figure 12B of
Bradshaw 2017 character for character, under its 324/330/340/348 scale.

| # | claim | tag |
|---|---|---|
| 2.1 | 324-652 aggregates; 349-652 does not — isolating 324-348. | **[READ]** |
| 2.2 | 190-652 aggregates; 190-652 Δ324-348 does not. | **[READ]** |
| 2.3 | The 25-mer is **essential but not in itself sufficient**: 1-382 does not aggregate, so at least some other part of the central domain is required. | **[READ]** |
| 2.4 | 333-652 aggregates indistinguishably from 324-652, so **324-332 is dispensable in that construct**. | **[READ]** |
| 2.5 | 333-340 is the narrowed critical region (Zaharija 2022, Fig. 6D), recorded as an assay-specific sub-annotation of 324-348 rather than a competing boundary. | **[INTERPRETATION]** |
| 2.6 | The Figure 6B legend's "AA 324-328" is a typographic slip for 324-348. | **[PERS. COMM.]** |
| 2.7 | Region found by experimental truncation scanning, explicitly **not** predicted. | **[READ]** |
| 2.8 | Against AGGRESCAN, FoldAmyloid, ProA and TANGO the region is **discordant**: a weak signal near 230-236 only, nothing on 324-348 from TANGO, and at least four sites elsewhere ranked higher in every case. | **[READ]** |
| 2.9 | The region is 48.0% proline-plus-charged (4 Pro + 8 charged of 25). | **[COMPUTED]** |

> **2.5 is the judgement call here.** I treat 324-348, 324-328 and 333-340 as one region
> with assay-specific sub-annotations rather than three competing claims, because a region
> can be necessary in one construct and dispensable in another and both results be correct.
> If you would rather 333-340 stood as its own entry, say so.

> **2.9 is yours before it is mine.** Your 2017 Discussion already notes the region
> "contains multiple proline residues" and is "rich in charged amino acids", and Figure 12B
> colours exactly those two classes. I have only put a number on an observation you
> published; it is cited to you, not claimed as new.

---

## What I have recorded that is *not* in either paper

Flagged so you can see what a third party has added around your data:

- **A one-residue discrepancy in the 2024 preprint**, now resolved by your sequencing: the
  body text writes Δ384-414 while Figure 5A and panels D-F label it Δ384-415, and the same
  sentence says "these 32 amino acids". **[READ]**
- **Figure 48's caption in Beti's thesis gives "AA 383-415"**, a third variant. **[READ]**
- **The 2022 paper's Figure 6B legend slip**, now confirmed by you. **[PERS. COMM.]**

None of these is offered as criticism — three of my own numbering errors are recorded in
the same dataset, and one of them was this boundary.

## Two things you should know before deciding whether to endorse anything

1. **The deposited version (v1.4.0, DOI 10.5281/zenodo.24290697) still records DISC1
   384-415.** It predates your correction. This extract is authoritative; the deposit will
   catch up in the next version.
2. **Venko K & Žerovnik E (2026)** place predictor calls inside this region: an
   aggregation-prone region at **403-411** called by ≥2 predictors, and amyloid-prone
   regions at **388-394** and **400-406** called by ≥4. All three sit strictly inside DISC1
   384-414. That cuts against a simple "the predictors miss it" framing for DISC1
   specifically, and I record it rather than only the half that helps my case.

   > **Corrected 19 Nov 2026 before sending.** This read "Venko et al. (2024)" — wrong on
   > the year and wrong on the author form, for a two-author paper. It was caught by
   > checking the citation against `data/references_to_check.json` rather than trusting
   > recall, and it was addressed to people likely to know the paper. The ≥2 / ≥4
   > distinction was also flattened into "consensus predictor calls"; those are two
   > different claims in their Table 3.
