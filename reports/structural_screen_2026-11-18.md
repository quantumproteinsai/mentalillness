# Structural recruitment for Φ — the screened candidate list

**Opened 18 November 2026**, after `reports/structural_recruiting_rule_2026-11-18.md` and
PREREGISTRATION §10b were committed (`660f863`). **Every candidate looked at appears here,
including the rejects**, as §10b requires.

**Provenance grading** is as the project rule requires: `[READ]` = the source PDF was
opened and the claim checked; `[SNIPPET]` = a search engine returned the words quoted;
`[EMPTY]` = the query returned nothing usable. **No row is admitted on a `[SNIPPET]`.**

**Status key.** `ADMITTED` · `REJECTED` · `PENDING-READ` (passes screening on snippets, needs
the PDF before it can be admitted or rejected).

---

## Current position

**1 admitted. 6 pending a PDF. 5 rejected.** Under §10b S5 the Φ–*v* test is **not**
recomputed until **three** rows are admitted, so the *n* = 7 result stands unchanged.

**Second screening round, 18 Nov, against the PDB itself.** Eight further proteins were put
through E2/E3/E4 using the RCSB REST API, which is a primary source and `[READ]` grade for
deposit facts: method, resolution, helical rise and twist, and the construct's UniProt
alignment. **E1, E5 and E6 cannot be settled this way** — they need the paper — so nothing
below is admitted.

---

## ADMITTED

### 1. Orb2 (Drosophila CPEB) — ADMITTED, 18 Nov 2026

**Hervás R *et al.* (2020)** *Science* **367**:1230–1234, doi:10.1126/science.aba3526.
Europe PMC Funders author manuscript **[READ IN FULL]**.

Passes all six criteria:

| | |
|---|---|
| **E1** | Route (a). *"the protofilament core structure extends from residues 176-206 of Orb2B"*, model built **de novo** from density |
| **E2** | The region *is* the modelled core — 100 % coverage |
| **E3** | Aggregated state, and **from endogenous tissue**: ~3 million adult fly heads, 97.5 % Orb2B by LC-MS/MS |
| **E4** | Helical rise 4.75 Å, twist −1.55°, C3; PDB **6VPS**, EMD-21316 |
| **E5** | **Verified, not assumed.** UniProt Q9VSR3 at 176–206 returns `QLHQQQHQQQHQQHQQHQQQQQLHQHQQQLS`, matching Figure 4F character for character; 704 aa matches the figure's 704 for Orb2B |
| **E6** | No aggregation predictor anywhere in the paper. Software named is cryo-EM and refinement only: RELION-3, MotionCor2, Gctf, Coot, REFMAC, MolProbity, PHENIX |

**The frame trap was real and was checked.** Orb2A and Orb2B share the prion-like domain
but differ in their N-terminal extension (9 residues vs 162; Orb2A is 551 aa), so the same
core carries different numbers in the two isoforms. The canonical UniProt entry is the long
one, so no conversion is needed — but it had to be confirmed, not assumed.

**The strongest construct provenance in the dataset.** The authors show the distinction
matters in their own hands: *"When we assembled Orb2 filaments from recombinant protein,
filaments were longer, morphologically distinct, less biochemically active, and had
negligible seeding capacity compared to endogenous ones."* A recombinant Orb2 row would not
be this row.

**The flag raised before the PDF was opened, kept and honoured.** This paper describes its
core as hydrophilic *in explicit contrast to pathogenic amyloids* — so it is a row the Φ
hypothesis predicts well, read in after the hypothesis existed. **It was admitted on E1–E6
alone, and its Φ has not been computed.**

**One consequence, computed after admission and not used to admit:** *L* = 704, *W* = 6,
*M* = 117, *m* = 4, ***m*/*M* = 0.0342** — below the §3.1b bar. *m*/*M* is explicitly not a
criterion under §10b and was not applied here. It is recorded because **this is the first
candidate in a week that is also usable by the benchmark arm**, where recruitment has been
exhausted. Admitting it there is a separate decision under the eight-stage pipeline and
§5.2b. Because no predictor has yet touched this chain, it would be **only the second row
in the project whose arm ordering can be intact from the start.**

Gaps recorded rather than glossed: the source is the **accepted manuscript**, not the
version of record (`source_version` governs); CPAD status is **unchecked**; the PDB deposit
itself has not been opened; Supplementary Material was not read.

---

## REJECTED

### TDP-43 — REJECTED on E6, by the paper's own Methods

**Guenther EL, Cao Q *et al.* (2018)** *Nat Struct Mol Biol* **25**:463–471,
doi:10.1038/s41594-018-0064-2. Author manuscript **[READ IN FULL]**.

**This is the failure mode named in advance as the likeliest way this candidate dies, and
it is stated by the authors in plain text.** Verbatim, Results:

> *"To identify which segments from the LCD of TDP-43 might be responsible for TDP-43
> aggregation, we consulted **ZipperDB**, (URL: https://services.mbi.ucla.edu/zipperdb). We
> selected the **top 10 hits scored by their adhesive energies**."*

and Methods:

> *"For computational prediction, we selected the segments that contain high rank
> predictions from ZipperDB (ranked by the predicted Rosetta energy)."*

**ZipperDB is an aggregation predictor** — the 3D-profile method, and one of the tools this
benchmark scores. Segments nominated by it and then confirmed are circular for any
predictor analysis. **E6 fails outright.**

**It fails E1 and E2 independently, and that matters more than it looks.** The ten
structures are **crystals of synthetic 6–11-residue peptides**, not an ordered core read
off the density of a protein fibril. The "region" was *chosen and then crystallised*, where
every incumbent Φ row's region was *discovered* in a reconstruction. The W-substitution
mutagenesis does show the segments matter for TDP-CTF aggregation — a genuine necessity
result — but it tests segments the predictor picked, which is where the circularity sits.

**The evidence I had flagged is not in this paper.** The deletion claims recorded as
`[SNIPPET]` on this candidate — Δ274-313 and Δ314-353 abolishing aggregation in cells, and
the SegA transplant into the aggregation-resistant *C. elegans* homolog — belong to other
papers (Jiang 2013; Cao *et al.*). **They remain unverified**, and the PDF supplied was a
different paper from the one those claims came from.

**And a structural reason for caution that outlives this rejection.** The paper states
there are four competing published "the amyloidogenic core" regions — 277–414, 286–331,
311–360, 342–366 — and says so directly: *"there is no consensus of which region is the
amyloidogenic core."* That is the NPAS3 problem again: a protein where a benchmark row
would require choosing between published results.

### PMEL17 / Pmel17 RPT domain — rejected on E2 and E4

`[SNIPPET]`, consistent across several sources: *"no three-dimensional structure has been
resolved for the RPT domain of Pmel17"*; the 2016 β-solenoid model is **computational**.
The 2025 *Nat Commun* PMEL paper concerns the **CAF/NTR** core, not RPT, and the region
literature is contradictory — RPT deletion *"blocks fibril formation in cells"* but RPT
*"is not necessary for fibril formation in vitro and in isolation is unable to adopt an
amyloid fold."* **No eligible deposit of the aggregated state covering a mapped region.**

A further disqualifier if a structure appears: *"glycosylation of Pmel17 appears to be
necessary for filament formation in vivo"*, so a recombinant core would not be the species
the mapping was done on.

### Aβ Uppsala (Δ690–695 / Aβ Δ19–24) — rejected on E1, and it is an instructive rejection

`[SNIPPET]`: the deletion mutant **still forms fibrils**, in four in-vitro polymorphs that
differ from the brain-derived fold. So the deleted residues are **not necessary** — this is
a deletion experiment that returns the opposite of a route (b) mapping. Recorded because
it is a reminder that *"a deletion construct exists"* is not *"a region was mapped"*, and
screening on the former would have admitted it.

---

## Not yet screened

Named here so the pool is visible and the search is auditable, not because any has passed
anything: β2-microglobulin (ΔN6), IAPP, SOD1 (Baek 2025 filament), αA-crystallin R116C,
medin, HET-s (218–289), Sup35 NM, ASC/PYD, gelsolin, apolipoprotein A-I N-terminal
fragment, β-endorphin, Pmel17 CAF.

**Excluded from the pool by construction:** the twelve structures in the §10a calibration
set (FapC 9U4U/9NQD, AL59 9FAA, transthyretin 7OB4, CsgA 8ENQ, α-synuclein 6H6B, prion
8WZX/7YAT, Aβ 7Q4B/7Q4M, tau 5O3L, FUS 6XFM). A structure used to calibrate Φ cannot also
test it. **This is why tau and α-synuclein — both of which have rows in
`data/regions.json` and abundant deposits — are not simply added here**; admitting them
would need a deposit outside the calibration set, which is possible and is left in the
pool above.


---

# Second round, 18 Nov 2026 — eight proteins screened against the PDB

**A discriminator worth stating, because it rejects a candidate cleanly.** A cross-β
amyloid stacks one β-strand per subunit along the fibril axis, so its deposited helical
rise is **≈ 4.75–4.85 Å**, or **≈ 2.4 Å with a ≈ 179° twist** when the asymmetric unit is
two rungs related by a 2₁ screw. Every incumbent Φ row sits in that band. A helical
filament with a rise far outside it is not a cross-β assembly, whatever it is called.

## Rejected in round two

### Gelsolin — REJECTED on E2 and E4

Seven EM entries, **none helical**: all are gelsolin domains bound to F-actin (12BW, 12BX,
12BY, 12BZ, 8VIZ, 8VKH, 9UG2). **There is no deposited structure of gelsolin in an
aggregated state at all**, so there is nothing for Φ to be computed on. Finnish-type
gelsolin amyloidosis is well described in the literature; the structure is not deposited.

### ASC / PYCARD — REJECTED on E3

Thirteen EM entries, most helical, and **none of them cross-β**. ASC-PYD filaments deposit
at **rise 13.7–13.95 Å, twist ≈ 53°** (3J63, 9WZ4, 9WZ7, 9WZ8, 9WZD, 9WZG) and ASC-CARD
filaments at **rise 5.0–5.27 Å, twist ≈ −100.6°** (6K99, 6N1H, 9WZ5, 9WZB, 9WZC). These are
helical polymers of **folded death-domain** subunits — inflammasome signalling filaments —
not amyloid. E3 asks for the aggregated state with a cross-β core, and this is a different
kind of object that the word "filament" disguises.

## Pending a PDF after round two

Each of the six below clears E2–E4 on deposit facts. **None can be admitted**: E1 (was a
predictor in the discovery path?), E5 (frame) and E6 require the paper, and in every case
**the modelled core range must be read from the deposit itself** — the alignments recorded
here are the *construct's* span, not the ordered core, and E2's ≥ 80 % test is against the
core.

| protein | deposit | res. | rise / twist | construct span (UniProt) | the issue to settle |
|---|---|---|---|---|---|
| **β2-microglobulin** | 6GK3 | 3.98 Å | 4.83 / −0.608 | P61769 42–105 | Is this wild type or the **ΔN6** truncation variant? The two are different rows |
| **SOD1** | 7VZF | 2.95 Å | 4.82 / −1.187 | P00441 1–154 | *"full-length human SOD1"* — the best WT candidate. 9JBO (3.39 Å) is the other WT |
| **human lysozyme** | 8QUT | 2.80 Å | 4.78 / −1.0 | P61626 19–148 | WT, *"heat-irreversible"*. Carries a second, **unidentified 10-residue peptide** entity |
| **apolipoprotein A-I** | 9PVY | 2.15 Å | 4.85 / −0.68 | P02647 25–267 | **Patient-derived cardiac fibril**, but of the **L90P variant**. Best resolution in the whole pool |
| **medin (lactadherin)** | 9U02 | 2.70 Å | 4.804 / −2.008 | Q08431 268–317 | **The only medin deposit, and it is heterotypic** — a co-fibril with Aβ40 |
| **IAPP / amylin** | 6Y1A | 4.20 Å | 2.351 / 178.23 | P10997 **34–70** | Many polymorphs; R1/R2 tie-breaks must be applied before, not after, looking |

### Four things these raise that are not bookkeeping

**1. Mutants and variants are not wild-type rows, and the pool is full of them.** SOD1's
other six deposits are G85R, H46R, G93A, D101N, C6A/C111A and G93A; lysozyme's other is
D87G; **all three** apolipoprotein A-I deposits are L90P or R173P. This is the same issue
that disqualified TDP-43's SegB structure (A315E, chosen *"to make the fibrils more
homogeneous"*) — but **apolipoprotein A-I is a different case and must not be lumped in**:
there the variant *is* the pathological species, taken from a patient, and the dataset
already carries hSAA1.1 with A52V on exactly that reasoning. **It is admissible if the
frame is explicit about the variant.** A row that silently used the canonical sequence
would be wrong.

**2. Medin's only structure is a two-protein interface.** 9U02 is a co-fibril of medin with
Aβ40. Φ computed on it would describe a heterotypic interface, not a homomeric core. The
dataset already carries exactly this caveat on **ANXA11 (9FOR), buried partly by TDP-43**,
so the precedent is admission-with-caveat rather than rejection — but it is the weakest
kind of row and should not be the one that carries the *n* from 7 to 8.

**3. The IAPP frame trap is real, and now verified.** UniProt P10997 is the **89-residue
precursor**; mature IAPP is the 37-mer at **P10997 34–70**, confirmed by the deposit
alignments for 6Y1A and 6ZRF. Any IAPP row must say which frame it is in, as the hSAA1.1
and LECT2 rows already do. Note also that **6VW2 is SUMO-tagged** (a second accession,
Q12306, in the same entity), which is a construct difference, not a frame one.

**4. β2-microglobulin's construct span is the question, not a detail.** 6GK3 aligns to
P61769 **42–105**. P61769 carries a 20-residue signal peptide, so mature β2m is 21–119 in
UniProt numbering. A span starting at 42 is **not** the mature N-terminus, and ΔN6 — the
truncation variant central to the β2m amyloid literature — starts six residues in. Whether
6GK3 is WT or ΔN6 decides what the row is, and the title does not say.

## What is needed next, in order of what it would settle

1. **SOD1 7VZF** — the cleanest wild-type, full-length, well-resolved candidate in the pool.
2. **Human lysozyme 8QUT** — wild type, 2.80 Å, and a classic systemic amyloidosis protein.
3. **β2-microglobulin 6GK3** — one sentence in the Methods decides WT versus ΔN6.

Apolipoprotein A-I, medin and IAPP are all live but each carries a caveat that must be
written into the row rather than discovered later.
