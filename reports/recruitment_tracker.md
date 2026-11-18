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
| **TAF15** | Q92804 | **absent** | 8ONS (2023, 1.97 Å), 9THM+ (2025) | *TAF15 amyloid filaments in FTLD*, Nature 2024 | **yes**, PMC10781619 | **stage 2** |
| **CHCHD10** | Q8WYQ3 | **absent** | 9CWW (2024, 2.3 Å) | *Amyloid fibril structures link CHCHD10 and CHCHD2 to neurodegeneration*, Nat Commun 2025 | **yes**, PMC12318133 | stage 1 done |
| **CHCHD2** | Q9Y6H1 | **absent** | 9OYR (2025, 2.03 Å) | same paper as CHCHD10 | **yes**, PMC12318133 | stage 1 done |
| **TFG** | Q92734 | **absent** | 8TEQ, 8TER (2023, 2.84 Å) | *Fibril structures of TFG protein mutants…*, PNAS Nexus 2023 | **yes**, PMC10703350 | stage 1 done |
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
