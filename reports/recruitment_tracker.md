# Recruiting five new proteins — tracker

**Opened 18 November 2026.** Live document: update the status column as stages complete,
and record refusals as well as additions.

## Why five, and why this is the binding task

The confirmatory stratum holds **2 rows** and §4 needs **n ≥ 5** before its test can fire
at all. `STATE.md` records that growing the dataset from 10 to 21 rows did not move that
cell, because row count was never the scarce resource. Under §7a the scarce thing is a row
that is **DISCORDANT, CPAD-absent, circularity-CLEAN, and labelled in the right order** —
and, as the n = 8 exercise showed, one that adds a *protein* rather than another interval
of a protein already present.

**So: five new proteins, one row each.**

## The pipeline, and the order that cannot slip

```
1  SCREEN     new protein · post-2020 · CPAD-absent (all three tables, with controls)
2  READ       publisher PDF INCLUDING SI; nothing is recorded from an abstract
3  FIX        frame + sequence verified; decoy segments excluded from the scored chain
4  CIRCULARITY  read out of the Methods, not the abstract: was a predictor in the path?
5  STRUCTURE  record the `structure` field: entry, chain, candidates, rule that chose
6  LEGACY     run TANGO
7  LABEL      assign stratum mechanically (v >= 0.05 -> DISCORDANT) and COMMIT IT
8  MODERN     only now run AggrescanAI
```

**Stage 7 must be in a commit before stage 8 runs.** That is checkable after the fact from
the commit graph, and it is the discipline whose loss on 17 Nov cost six rows their
confirmatory standing.

## Candidates: CPAD screen complete

All screened against the APR protein list, the peptide table **and** the structures table,
with tau, insulin, transthyretin and CsgA as positive controls — all of which hit.

| protein | accession | CPAD | structures | paper | OA | status |
|---|---|---|---|---|---|---|
| **TAF15** | Q92804 | **absent** | 8ONS (2023, 1.97 Å), 9THM+ (2025) | *TAF15 amyloid filaments in FTLD*, Nature 2024 | **yes**, PMC10781619 | **IN, stage 5 done** |
| **CHCHD10** | Q8WYQ3 | **absent** | 9CWW (2024, 2.3 Å) | *Amyloid fibril structures link CHCHD10 and CHCHD2 to neurodegeneration*, Nat Commun 2025 | **yes**, PMC12318133 | **IN, stage 5 done** |
| **CHCHD2** | Q9Y6H1 | **absent** | 9OYR (2025, 2.03 Å) | same paper as CHCHD10 | **yes**, PMC12318133 | **IN, stage 5 done** |
| **TFG** | Q92734 | **absent** | 8TEQ, 8TER (2023, 2.84 Å) | *Fibril structures of TFG protein mutants…*, PNAS Nexus 2023 | **yes**, PMC10703350 | **REJECTED: CIRCULAR** |
| **TPPP** | O94811 | **absent** | 9J4D–9J4F (2024, 2.93 Å) | *TPPP/p25 amyloid seeding…MSA*, Cell 2026 | **no** | **blocked: PDF** |
| **ApoA-II** | P09813 | **absent** | 8OQ4, 8OQ5 (2023, 2.6 Å) | *…Structural Basis of Amyloid Resistance…*, JMB 2024 | **no** | **blocked: PDF** |
| **sunflower 11S** | A0A9K3J848 | **absent** | 26SG (2026, 3.05 Å) | *Cryo-EM Structures of Sunflower Amyloid Fibrils…*, Small 2026 | **no** | **blocked: PDF** |
| Ninjurin-1 | Q92982 | **absent** | 9K8S, 9K8T (2024) | — | — | **held**: construct is a derived 30-mer, not the protein |

**Rejected as CPAD members**, lines inspected rather than trusted to a substring: Orb2
(`Translational regulator orb2`), FapC (`FapC amyloid-like fimbriae protein`), CsgA,
TIA-1 (`Nucleolysin TIA-1`), TGFBI, α-crystallin B, Nup98, myoglobin, Uperin-3.5.

## Selection, and one deliberate compromise

The five targets are **TAF15, CHCHD10, CHCHD2, TFG** and one of the blocked three.

**CHCHD10 and CHCHD2 come from the same paper**, which is a real compromise: two rows
sharing a laboratory, a sample preparation and an imaging pipeline are less independent
than two rows from different groups. They are two distinct proteins with distinct folds,
so they are not the DISC1-interval problem over again — but the correlation must be
recorded on both rows and in any analysis that pools them. **Taking both is a choice made
because the alternative is dropping to four**, and it is written here rather than left for
a reader to notice.

**TFG carries its own caveat**: the deposited fibrils are of TFG **mutants**, so the
`construct` column will say so and the row may not speak to the wild-type protein.

## What is blocked, and what would unblock it

**Three candidates need a publisher PDF** that this environment cannot reach: TPPP (Cell),
ApoA-II (JMB), sunflower 11S (Small). Any one of them completes the five.

**Preference order, if a PDF can be obtained:**

1. **sunflower 11S** — a second non-animal seed-storage protein, a direct parallel to
   glycinin, and the only candidate that would test whether the glycinin result generalises
   beyond one plant protein.
2. **ApoA-II** — *ex vivo* mouse amyloid, so the discovery path is structure rather than
   prediction, and a non-human row widens the set.
3. **TPPP** — human, MSA-linked, but the paper is about a seeding assay and the structure
   may be secondary to it.

**Nothing is recorded from an abstract.** The standing rule holds: four abstract-level
verdicts were overturned in one day on this project.

---

## TAF15 — stages 1–4 done, 18 Nov 2026

**Read from the Europe PMC full-text XML of PMC10781619** (Tetter *et al.*, *TAF15 amyloid
filaments in frontotemporal lobar degeneration*, Nature 2024). **NOT yet the publisher
PDF — see the caveat at the end, which is not a formality.**

| field | value | how established |
|---|---|---|
| region | **residues 7–99** | *"The filament fold is formed from residues 7–99 in the low-complexity domain (LCD) of TAF15 and was identical between individuals."* |
| frame | **UniProt Q92804, canonical, 592 aa** | fetched; length confirms canonical |
| sequence 7–99 | `YGQSGGEQQSYSTYGNPGSQGYGQASQSYSGYGQTTDSSYGQNYSGYSSYGQSQSGYSQSYGGYENQKQSSYSQQPYNNQGQQQNMESSGSQG` | 93 residues, taken from the fetched sequence, not transcribed |
| construct | **filaments extracted from human post-mortem brain (FTLD-FET)** — *ex vivo*, not recombinant | Methods |
| evidence | cryo-EM, 1.97 Å, fold identical across four individuals | Results |
| circularity | **CLEAN** | see below |
| CPAD | **absent**, all three tables, controls hit | screen of 18 Nov |

### Circularity: clean, and checked properly

**No aggregation predictor appears anywhere in the full text.** Searched with word
boundaries for TANGO, AGGRESCAN, FoldAmyloid, ZipperDB, Waltz, AmylPred, ProA, PASTA,
MetAmyl, ANuPP, AmyloGram, Zyggregator, CamSol and AlphaFold: **none.**

**A substring search first reported a hit on "ProA".** It was matching inside the word
*approach*, three times. Had that gone unchecked, a clean row would have been labelled
circular on the strength of a word that is not in the paper. The check that caught it cost
one line — requiring a word boundary.

The discovery path is **cryo-EM reconstructed *de novo* from reference-free 2D class
averages, with the protein identified by mass spectrometry**: *"Peptides mapping to the
TAF15 filament core were only identified for individuals with FTLD-FET."* No prediction
anywhere in the path.

### What is NOT yet established, and why it matters here specifically

**The publisher PDF has not been opened.** On the glycinin row, the XML pass **missed the
paper's own necessity claim**, which only appeared when the publisher PDF was read — and
that claim turned out to overstate its own supplementary figure. The same exposure applies
here, so this row is **not written into `data/regions.json` yet**, and when it is,
`verified_against_publisher_pdf` will be `false` until someone opens it.

**The structure field is also unresolved**: Q92804 has 14 cryo-EM entries. **8ONS** is the
one deposited with this paper; the 2025 entries (9THM, 9THN, 9THP, 9TKE…) belong to a
*different, paywalled* paper on FTLD-TAF15 subtypes. Rule 1 of §10a §2 points at 8ONS, but
that needs confirming from the paper's own data-availability statement rather than from
deposit dates.

---

## 18 November 2026, later: three rows in, one rejected, and a correction

`data/regions.json` now holds **24 rows across 14 proteins**, up from 21 across 11.
**No stratum label was written with them** — that is stage 7, it is assigned mechanically
from the legacy arm, and it gets its own commit before any modern predictor runs.

### TFG — REJECTED AT STAGE 4, AND THE PAPER'S TITLE SAYS WHY

The title is *"Fibril structures of TFG protein mutants **validate the identification of
TFG as a disease-related amyloid protein by the IMPAcT method**"*. IMPAcT is a
**computational amyloid predictor** that "entails comparing the computed amyloidogenic
propensity of mutant protein sequences to their wild-type counterparts", and it **employs
the ZipperDB database**. TFG is in that paper *because a predictor nominated it*, and the
paper exists to validate the predictor.

**That is the exact circularity `found_by` was added to catch.** Scoring a predictor on a
region a predictor discovered measures the predictor against itself. Rejected — not
demoted to the exploratory arm, rejected, because there is a second disqualifier: the
structures are of the **G269V and P285L mutants**, and the paper states the WT sequence
does not form them.

**It cost one word-boundary grep to find, and it would have been invisible after
scoring.** The selection written in this file hours earlier called TFG a target and
flagged only the mutant caveat. The circularity was the bigger problem and was missed.

### TAF15 — the "blocked on a publisher PDF" note above was WRONG

This file recorded that the TAF15 publisher PDF had not been opened. **It was retrievable
all along**: Nature open access, `nature.com/articles/s41586-023-06801-2.pdf`, 28.2 MB,
22 pages including Extended Data. Read in full on 18 Nov. It **agrees with the Europe PMC
XML** on the region (7–99), the frame (Q92804, 592 aa) and the accession (8ONS), and it
contains no aggregation predictor. `verified_against_publisher_pdf` is `true`.

The lesson is not about TAF15. **"Blocked on a PDF" was asserted without trying the
publisher's own open-access URL**, and three candidates below still carry that label on
the same kind of evidence. Each should be retried before being reported as blocked.

### CHCHD10 and CHCHD2 — in, with a non-independence that is worse than "same lab"

Both rows carry a field, `NON_INDEPENDENT_WITH_THE_CHCHD2_ROW` / `..._CHCHD10_ROW`,
recording the real problem. It is **not** the shared laboratory that was flagged when
these two were proposed:

> CHCHD10 43–75 and CHCHD2 54–86 align over 33 residues at **28/33 = 84.8% identity**.
> Every predictor in both arms is a function of sequence, so **these two rows score almost
> identically by construction**, and a rank test that counts them twice inflates *n*
> without adding information.

**Rule, recorded on both rows:** any confirmatory or pooled statistic uses **at most one**
of the pair; the other is reported beside it as a near-replicate. So the pair contributes
**one** effective row to §5.2b, not two — which means the recruitment drive has delivered
**two** effective new candidates (TAF15, and one of the CHCHD pair), not three.

### What all three rows share, and what it costs

All three regions are **ordered cryo-EM cores, not necessity mappings**. The words
"necessary", "sufficient" and "required" do not occur in connection with the region in
any of the three papers, and no truncation series tests whether any part is dispensable.
They sit with ANXA11, one notch below DISC1 and TRIOBP-1, whose regions *were* mapped by
deletion. **The dataset is drifting towards structure-defined rows because those are the
papers being published** — worth stating before it becomes invisible.

| row | material | strength |
|---|---|---|
| TAF15 7–99 | *ex vivo* human post-mortem brain, FTLD-FET | strongest; ties ANXA11 |
| CHCHD10 42–75 | recombinant fragment 1–98, in vitro | weakest; mouse + fibroblast support only |
| CHCHD2 54–86 | recombinant fragment 1–113, in vitro | weakest; **no** in vivo arm of its own |

### Still open

Two more proteins are wanted, and the three "blocked" candidates should each be retried
at the publisher's own URL before anyone is asked for a PDF.

### The retry, done rather than promised — 18 Nov 2026

All three "blocked" candidates were retried at the publisher's own URL and against Europe
PMC. **All three are genuinely blocked**, and the retry is recorded with its negatives so
nobody repeats it:

| candidate | retry | result |
|---|---|---|
| TPPP (Cell 2026) | PMID 42190663 | `isOpenAccess: N`, no PMCID, no PDF; publisher URL **HTTP 403** |
| sunflower 11S (Small 2026) | PMID 42801496 | `isOpenAccess: N`, no PMCID, no PDF; Wiley **HTTP 403** |
| ApoA-II (JMB 2024, 8OQ4/8OQ5) | searched by accession and title | no open-access record surfaces |

**The retry was worth running anyway: it is what proved TAF15 was never blocked.** One of
four assumed-blocked candidates was reachable, which is a high enough rate to justify
checking rather than asserting.

---

## RECRUITMENT IS PAUSED — 18 November 2026, and the reason is arithmetic

**Do not recruit another row until a candidate's m/M has been checked.** Registered as
**PREREGISTRATION §3.1b**.

### The rule, and it is checked at stage 1

> **A row is `power_eligible` iff m/M ≤ 0.05**, where *M* is the number of 6-residue
> tiled windows in the scored chain and *m* the number wholly inside the region.
> In residues, with W = 6: **m/M ≈ (region length) / (chain length)**, so the rule reads
> roughly **the mapped region must be at most 5% of the protein.**

Under H0 the chain's top-ranked window lands inside the region with probability exactly
*m*/*M*. **No rank-based statistic can return a p below that** — not §3.1's, not a
repaired one. Where *m*/*M* > 0.05 the row is beyond any test at α = 0.05, and "the
predictor missed it" is true before any software runs, in the direction of our own H1.

**This costs nothing.** It needs the chain length and the region length, both of which are
usually in the abstract. **Applied this morning it would have rejected all three of
today's recruits before a paper was opened:** TAF15 0.153, CHCHD2 0.200, CHCHD10 0.217.

Only **10 of the 23 scored** rows pass (11 of all 24, counting the excluded row).
*Corrected 18 Nov 2026 from “7 of 20” — see the §3.1a short-region fix.*
Both founding confirmatory rows do, narrowly —
DISC1 384–415 at 0.0352 and TRIOBP-1 324–348 at 0.0370 — so the project's own question
stays answerable.

### The pool has to change, and that is the real consequence

| what the rule wants | what recent cryo-EM fibril papers supply |
|---|---|
| **long protein, short mapped region** | short protein, long ordered core |
| necessity established by deletion | ordered core read off a density map |
| *m*/*M* ≈ 0.02–0.04 | *m*/*M* ≈ 0.15–0.49 |

**The cryo-EM core pool is close to exhausted for this purpose**, and not by accident:
the technique resolves the ordered core, and papers choose constructs in which that core
is a large fraction of the chain. CHCHD10 is a 142-residue protein with a 34-residue
core. Nine of the thirteen failing rows came from that literature.

**Search the other pool instead: deletion and truncation mapping on large proteins.** It
is where DISC1 and TRIOBP-1 came from. It yields the right geometry *and* the stronger
evidence type — a necessity claim rather than an ordered core — so it fixes both defects
named on 18 Nov at once.

**Concrete search shape:** proteins of ≥ 400 residues with a mapped aggregation-critical
region of ≤ 20 residues, found by deletion, truncation, alanine scan or peptide-array,
post-2015, CPAD-absent. The three blocked publisher PDFs (TPPP, ApoA-II, sunflower 11S)
should be **screened for m/M before anyone is asked for them again** — on the deposited
ranges, TPPP and sunflower 11S look likely to fail it.

### What happens to the rows already in

**Nothing is removed.** Dropping rows after seeing their scores is the post-hoc selection
the pre-registration exists to prevent. They are **labelled** with `power_eligible` and
their m/M, reported, and excluded from any statistic that uses §4's recovery criterion —
with both versions shown wherever a statistic is recomputed on the eligible subset.

---

## NPAS3 — REJECTED, on three independent grounds. 18 Nov 2026

**Source PDFs supplied by the author** and read in full: Samardžija *et al.* (2021)
*J. Pers. Med.* **11**:1070; Samardžija *et al.* (2023) *Cells* **12**:1848; Samardžija
*et al.* (2026) *Sci. Rep.* **16**:8240. All three are Bradshaw's group — the same
laboratory as the DISC1 and TRIOBP-1 rows.

NPAS3 was the strongest lead the literature search produced: a schizophrenia-associated
protein, CPAD-absent, 933 residues, aggregating in post-mortem brain. **It fails anyway,
and each reason would be sufficient alone.**

**1. Geometry. Both candidate regions fail §3.1b**, and they fail in opposite directions:

| claimed region | source | length | *m*/*M* |
|---|---|---|---|
| **PAS1 domain, aa 157–208** | Samardžija 2021, Discussion, verbatim | 52 aa | **0.0516** |
| **inter-PAS linker, aa 211–331** | Nucifora 2016, as cited by Samardžija 2021 | 121 aa | **0.1290** |

**2. The two groups disagree about which region it is**, and the 2021 paper says so in
print: *"In contrast, previous studies showed NPAS3 protein aggregation to be dependent
instead on the unstructured linker region between the two PAS domains (aa 211-331)."* The
regions **do not overlap**. A benchmark row needs one region, not a choice between two
published ones made by us.

**3. The readout is a declared surrogate, not aggregation.** Verbatim: *"We therefore used
cytoplasmic expression of NPAS3 as a surrogate for its misfolding and aggregation."* The
PAS1 result is a **localisation** result — the fragments lacking PAS1 are nuclear, those
containing it are cytoplasmic — and the paper's own heading for it is *"the critical domain
for **mislocalization**"*. Visible aggregates appeared in **14% of cells**. The row would
record a region necessary for *cytoplasmic residence*, which is not what this dataset
scores.

**The frame is confirmed and worth keeping** even though the row is rejected: the paper
states *"All amino acid numbers refer to the 933 long amino acid splice variant of human
NPAS3 (NP_001158221.1)"*, which happens to match canonical Q8IXF0 at 933 aa.

### What the three PDFs did give the project

- **CRMP1** is a genuine family member — insoluble in patient brain alongside DISC1 and
  TRIOBP-1, and a confirmed DISC1 co-aggregation partner — but **no fragment-level mapping
  of CRMP1 aggregation exists in any of the three papers.** Not recruitable until one does.
- **A lead on an existing row, not a new one:** Zaharija B & Bradshaw NJ (2024),
  *"Aggregation of disrupted in schizophrenia 1 arises from a central region of the
  protein"*, *Prog. Neuropsychopharmacol. Biol. Psychiatry* **130**:110923. Cited in the
  2026 Methods as the source of *"the aggregation prone-region between"* the D and I
  domains of DISC1 (construct aa 257–655). **This is the paper the outstanding Δ384-414/415
  query to Bradshaw concerns.** It has not been read.
- **TRIOBP-1 Δ1–59 Δ333–340 abolishes aggregation** (*Cells* 2023, citing Zaharija 2022) —
  a genuine necessity claim, and both regions are already rows. TRIOBP-1 333–340 is 8
  residues in 652 (*m*/*M* = 0.0016) and is **power_eligible**; it is, however,
  **CONCORDANT**, so it cannot enter the confirmatory stratum.

### The search result, stated plainly

**No power-eligible recruitment candidate has been found.** Screened and rejected on
18 Nov: TFG (circular), TAF15, CHCHD10, CHCHD2 (admitted, then found power-ineligible),
TPPP, ApoA-II, sunflower 11S ×2 (all fail *m*/*M*), Ninjurin-1 (derived 30-mer), NPAS3
(above). **The constraint is real and it is biting.**
