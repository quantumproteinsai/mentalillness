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

**0 admitted. 2 pending the PDF. 2 rejected.** The analysis stays at *n* = 7 until a row
clears a full read, and under §10b S5 it is not re-run at all unless **three** new rows
are admitted.

---

## PENDING-READ

### 1. TDP-43 — the strongest lead

- **Route (b) evidence, `[SNIPPET]`:** *"deleting residues 314-353 or 274-313 from
  full-length TDP-43 inhibits aggregation in SH-SY5Y cells"*, and separately that SegA
  *"was identified as an aggregation core because deleting it decreases TDP-43 aggregation
  in vitro and in cells, while adding SegA to the aggregation-resistant* C. elegans
  *homolog induces aggregation."* **A gain-of-function transplant plus a loss-of-function
  deletion is the strongest evidence type in this dataset** — stronger than anything the
  seven incumbents carry.
- **Route (a) evidence, `[SNIPPET]`:** 7KWZ, cryo-EM fibrils of the entire low-complexity
  domain, core mapping to **residues 276–414**, 3.20 Å — which spans both deleted regions.
  Also Cao et al.'s four polymorphic cores, SegA (311–360) and SegB (286–331).
- **Why it is not admitted yet.** Three things must be read, not snippeted: (i) the
  deletion claim in its primary paper, with the construct; (ii) whether SegA/SegB were
  nominated by a **predictor** — a 3D-profile or ZipperDB nomination would fail E6
  outright, and this is the single most likely way this candidate dies; (iii) the SegB
  structure carries the **A315E mutation** *"which makes the fibrils more homogeneous"*,
  and a mutant core is not the wild-type row.
- **Caveats already visible.** TDP-43 is almost certainly CPAD-contaminated (recorded, not
  disqualifying — §10a showed CPAD and Φ are not collinear). Under R1 only **one** region
  may be taken, and under R2 only one structure; both tie-breaks are mechanical and must
  be applied *before* Φ is computed.

### 2. Orb2 (Drosophila CPEB) — the highest-value row if it survives

- **Route (a) evidence, `[SNIPPET]`:** endogenous Orb2 purified from **adult fly heads**,
  cryo-EM at **2.6 Å**, three-fold symmetric filaments; protofilament core of **31
  residues of the prion-like domain, residues 176–206**, *"a cross-β unit with a single
  hydrophilic hairpin stabilized by a tight interdigitated glutamine packing."*
- **Why it matters more than its *n* contribution.** The authors contrast it explicitly:
  *"Unlike the hydrophobic core of pathogenic amyloids, the hydrophilic core of Orb2
  filaments…"* **This is a high-Φ row nominated by its own authors as high-Φ, in a
  functional amyloid, from endogenous tissue.** If the polarity association is real, this
  row should sit at the top of the Φ range and be badly missed by both predictors. If it
  does not, that is informative against the hypothesis.
- **Why it is not admitted yet.** The region boundary 176–206 reached us through a
  secondary summary, not the paper. The deposit and its helical parameters must be checked
  against E4, the frame against E5, and `found_by` against E6.
- **One flag raised in advance, so it cannot be rationalised later.** A row the hypothesis
  predicts well, read into the set after the hypothesis exists, is the classic way a
  fragile *n* = 7 result becomes a fragile *n* = 8 result that merely looks sturdier.
  **Orb2 is admitted or rejected on E1–E6 alone, and its Φ is not computed before the
  other candidates'.**

---

## REJECTED

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
