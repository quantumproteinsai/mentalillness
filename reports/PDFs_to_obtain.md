# Papers nobody could open — mental illness sweep, 15 Nov 2026

Reached only through an abstract, a snippet, a secondary citation or a metadata
record. Each is a **lead, not a fact**.

Ranked by what changes if you read it.

## Tier 0 — these decide whether the project is viable

1. **Samardžija (2025), PhD thesis, University of Rijeka (biotechnology).**
   Two PDF versions are online and neither was opened. **This is the single
   outstanding risk to the whole premise**: the literature search found no
   protein-language-model predictor ever run on DISC1 or TRIOBP-1, but a thesis
   from the experimental group is exactly where such runs would sit unindexed.
   Two downloads away, and it either confirms the gap or closes the project.

2. **Nucifora et al.**, *American Journal of Psychiatry* (2019) — **full text and the
   mass-spectrometry protein list.**
   PubMed returned a cookie notice, Europe PMC 403, publisher paywalled.
   The flagship study of the whole field: 42 schizophrenia against 41 controls,
   three brain banks, cold sarkosyl fractionation, 20 of 42 cases with elevated
   insoluble and ubiquitinated protein. **Its MS is published at pathway level only** —
   no named proteins, no fold changes, no FDR. Even the 42/41/20 counts we have are
   second-hand. If a per-protein table exists anywhere, it is in that supplement.

3. **Leliveld et al.**, *J. Neuroscience* (2008/2009), and **Korth (2012)**. Both 403.
   The primary sources for two things we are currently leaning on: cold-sarkosyl-insoluble
   DISC1 in patient brain but not controls, and — far more important — the report that
   **brain-derived aggregates do not stimulate thioflavin T** while recombinant DISC1
   fibrils do. That single observation decides whether the disease species is an ordered
   amyloid at all. We have it only as a statement inside a 2025 paper citing them.

## Tier 1 — these fix the validation table

4. **Bradshaw et al. (2017)**, *J. Biological Chemistry* — TRIOBP-1 aggregation-critical
   region. Europe PMC returned HTTP 500.
   The 324–348 ground truth and the proline/charge "turn and interaction surface"
   hypothesis both come from here. Your own plan already lists it for Week 1; it is still
   unread by any automated route, and the mechanistic half of the paper rests on it.

5. **Narayanan et al. (2011)**, *JBC*, PMC3243500. Europe PMC returned HTTP 500.
   Needed to close one specific question: whether **any** DISC1 study used a reducing
   agent. Established for Cukkemane 2021, Cukkemane 2025 and Zhou 2026 — all three never
   mention DTT, TCEP or mercaptoethanol — but unverified for this one and for Leliveld.

6. **Cukkemane et al. (2021) Figure S8**, and **Cukkemane et al. (2025) `mmc1.docx`** (5.2 MB).
   The 2021 paper deposited nothing anywhere. That supplementary file is the **only
   remaining candidate** for a coordinate file of the DISC1 β-core model. Unlikely to hold
   PDB-format coordinates, but it is not yet a verified negative.
   Related task, not a PDF: check **ModelArchive and PDB-Dev** for the same model.

7. **AggrescanAI**, *J. Molecular Biology* (2026), doi:10.1016/j.jmb.2026.169643.
   Publisher returned 403, so everything known about the model rests on its GitHub README.
   It is one of the two tools the first experiment would run, so its training set matters:
   if the mapped regions or their hexapeptides are in it, the retrospective test is
   contaminated and must say so.

8. **The *Cells* (2023) co-aggregation review** — never read.
   Cited into the DISC1/CRMP1/TRIOBP-1 co-aggregation claim.

9. **Galzitskaya OV, Garbuzynskiy SO, Lobanov MY (2006b), "Prediction of amyloidogenic
   and disordered regions in protein chains", *PLoS Comput Biol* 2(12):e177** —
   **OPEN ACCESS, so this is a fetch rather than a paywall.** Added 15 Nov 2026.

   **What it buys: the twenty numbers that make FoldAmyloid runnable again.** The
   FoldAmyloid primary paper (Garbuzynskiy et al. 2010, *Bioinformatics* 26:326-332)
   has been read in full and specifies the entire method — three scales, 5-residue
   window, call on 5 consecutive residues above cutoff, cutoffs 21.4 / 0.697 / 0.671 /
   0.090 / 0.062, hybrids by z-normalise-then-average. **The one thing it does not
   print is the 20 per-residue values for each scale**: Figure 1(a-e) plots them as bar
   charts only, and the text refers the contact scale to "our previous work
   (Galzitskaya et al., 2006a)". 2006b is the companion that documents the
   3769-structure database (<25% identity, SCOP a/b/c/d) and the packing-density
   definition (non-hydrogen atoms within 8 A, neighbours excluded).

   **Why it matters to the argument, not just the tooling.** The FoldAmyloid server is
   dead at the URL the paper itself publishes (`antares.protres.ru/fold-amyloid/`, 000
   over http and https, re-checked 15 Nov 2026). Without the scale values the legacy
   baseline is two of Bradshaw 2017's four tools; with them it is **three of four**, and
   a reviewer loses the objection that the 2017 comparison cannot be reproduced.

   **Check on arrival:** that 2006b actually prints the numeric scales rather than
   plotting them too. If it does not, the next target is Galzitskaya et al. 2006a,
   *J Bioinf Comp Biol* 4:373-388, which the 2010 paper names as the source. If
   neither prints them, say so and stop — a reimplementation from digitised bar charts
   is not a reproduction of FoldAmyloid and must not be labelled as one.

## Not a paywall — a search limit worth closing

9. A proper **forward-citation sweep** of the AggreProt (2024) and AggrescanAI (2026)
   papers, in Scopus or Google Scholar. Europe PMC's `CITES:` syntax failed, returning
   zero for bad syntax rather than for absence, so the "nobody has run these" negative
   rests on keyword search alone. A forward sweep would close it far harder — and it is
   the claim the first paper depends on.
