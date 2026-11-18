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

**1 admitted. 0 pending. 3 rejected.** Both pending PDFs were supplied and read in full on
18 Nov. Under §10b S5 the Φ–*v* test is **not** recomputed until **three** rows are
admitted, so the *n* = 7 result stands unchanged today.

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
