# Papers nobody could open — mental illness sweep, 15 Nov 2026

Reached only through an abstract, a snippet, a secondary citation or a metadata
record. Each is a **lead, not a fact**.

Ranked by what changes if you read it.

## Tier 0 — these decide whether the project is viable

0. ~~**Zaharija B (2025), PhD thesis, University of Rijeka.**~~ **READ IN FULL 16 Nov
   2026 — obtained from the uniri repository by the author. THE SINGLE MOST CONSEQUENTIAL
   DOCUMENT READ ON THIS PROJECT, AND IT WAS FOUND BY ACCIDENT.** Defended 23 June 2025,
   245 pp, 48 figures, 392 references. urn:nbn:hr:193:978729.

   **It falsifies the broad novelty claim and clears the last freeze blocker.** §4.3.5 runs
   **five aggregation predictors on full-length DISC1** — TANGO, AGGRESCAN, FoldAmyloid,
   MetAmyl and ANuPP, six algorithms, with a per-residue consensus. The narrow claim in
   `PREREGISTRATION.md` §5.2 (*no **PLM** predictor*) survives untouched; the broad version
   in `STATE.md` did not and is struck. Four of five tools gave hotspots dispersed across
   the whole sequence; only ANuPP named the linker. **Their result supports H1 — but it is
   theirs, and must be cited rather than rediscovered.** Full assessment in
   `data/references_to_check.json`, key `zaharija2025thesis`.

   ~~Routes, neither automatable.~~ **The route that worked was asking.** The faculty PDF
   404s and `repository.biotech.uniri.hr` returns 418 to scripts; the author retrieved it
   by hand. *Fifth document in two days obtained by asking rather than by retrieval.*

   ~~Previously, when this entry was a lead:~~ [SNIPPET — superseded by the full read.]

   **It is wanted for two unrelated reasons, and it is the best remaining route to
   both.**
   - **It is the first author's own thesis on the DISC1 384-415 work.** Theses reproduce
     their papers' figures, so this is the most likely *free* source for the published
     Figure 5 — and therefore for Δ384-**414** vs Δ384-**415**, the last freeze blocker
     (item 4a).
   - **It is a SECOND 2025 thesis from this group, and §11 was discharged against the
     first one only.** Samardžija's thesis contained no predictor runs. This is a
     different document. The search summary says its aims include refining DISC1 domain
     borders "using earlier bioinformatics data and new empirical data" — domain-boundary
     bioinformatics is **not** aggregation prediction, and that distinction is the entire
     novelty claim, so it must be **checked, not assumed.**

   **Routes, neither automatable.** The faculty PDF
   (`biotech.uniri.hr/wp-content/uploads/2025/03/PhD_02_2025_Zaharija_Beti.pdf`) returns
   **HTTP 404** — the third instance of link rot on this same faculty site today. The
   repository holds it as object `biotechri:1106`, but `repository.biotech.uniri.hr`
   returns **HTTP 418** to scripted requests, an explicit anti-automation response that
   was **not worked around**. Manual browser, or ask the author.

1. ~~**Samardžija B (2025), PhD thesis, University of Rijeka.**~~
   **RESOLVED 15 Nov 2026 — READ IN FULL. The gap holds; this item is closed.**
   The author supplied the PDF after both recorded URLs returned **HTTP 404** and
   `repository.biotech.uniri.hr` returned **HTTP 418** to scripted requests (an explicit
   anti-automation response, not worked around). *Obtained by asking, not by retrieval.*

   "Aggregation, parallel aggregation and co-aggregation of proteins in chronic mental
   illnesses", 274 pp, mentor Nicholas J. Bradshaw, defended 5 June 2025.

   **It contains no aggregation predictor runs of any kind.** §3.1-3.19 has no
   bioinformatics section; all named software is instrumentation or statistics (ImageLab,
   CellSens, ImageJ/Fiji, JASP, Prism, MassHunter, FlyTracker/MATLAB, a Python SIN script,
   BioRender) plus **ProSite, used only to draw the domain cartoons in Figures 2 and 3**.
   TANGO, AGGRESCAN, FoldAmyloid, ProA, WALTZ, PASTA, AmylPred2, AggreProt and AggrescanAI
   are absent, as is any PLM and AlphaFold. The single "in silico" phrase concerns *CRMP1*
   variants and cites Ravindran et al. 2022, not work done here.

   **`PREREGISTRATION.md` §11's fourth falsification condition is discharged.** Full
   assessment, including the three things the thesis *does* change, in `STATE.md`.

2. **Nucifora et al.**, *American Journal of Psychiatry* (2019) — **full text and the
   mass-spectrometry protein list.**
   PubMed returned a cookie notice, Europe PMC 403, publisher paywalled.
   The flagship study of the whole field: 42 schizophrenia against 41 controls,
   three brain banks, cold sarkosyl fractionation, 20 of 42 cases with elevated
   insoluble and ubiquitinated protein. **Its MS is published at pathway level only** —
   no named proteins, no fold changes, no FDR. Even the 42/41/20 counts we have are
   second-hand. If a per-protein table exists anywhere, it is in that supplement.

3. ~~**Leliveld et al. (2008)**, *J. Neuroscience* **28**:3839~~ **— READ IN FULL
   16 Nov 2026, supplied by the author.** **Korth (2012) is still unread, and the
   thioflavin T item now rests on it alone.**

   **THE THIOFLAVIN T CLAIM IS IN NEITHER LELIVELD PAPER.** Both have now been read in
   full. Neither contains a thioflavin T experiment of any kind. Cukkemane 2025
   attributes the claim to "Leliveld 2009 and Korth 2012"; **the Leliveld half of that
   attribution does not hold.** Either it is Korth 2012 alone, or it is a mis-citation.
   Until Korth 2012 is read, *nothing in this project may lean on the ThT negative.*

   **CORRECTION OF A CORRECTION, same day.** This entry first read "*J. Neuroscience*
   (2008/2009)", merging two papers in two journals. On splitting them I asserted the
   2008 paper "carries the thioflavin T and cold-sarkosyl claims." **The cold-sarkosyl
   half is right; the thioflavin T half was wrong** — I inferred it from the citation
   rather than from the paper, which is the error this project's first rule exists to
   prevent.

   **What the 2008 paper does give, and it substantially answers the question the ThT
   claim was being used for.** It reaches the same conclusion by circular dichroism
   instead: the rDISC598 dimer has "essentially the same far-UV CD spectrum as the
   combined oligomer plus multimer fraction, indicating that rDISC598 **self-associates
   as folded subunits**." The Discussion is explicit — "we do not think that the type of
   Sarkosyl-resistant DISC1 aggregates described here are directly comparable with those
   found in classic misfolding diseases, because we do not have evidence of extensive
   conformational misfolding of multimeric DISC1." **So the authors themselves decline to
   call the brain species an ordered amyloid, on CD evidence, in 2008.** That is a
   stronger footing than a dye negative, and it is now READ rather than inherited. Full
   assessment in `data/references_to_check.json`, key `leliveld2008`.

3a. ~~**Leliveld et al. (2009)**, *Biochemistry* **48**:7746.~~ **READ IN FULL 16 Nov
   2026, supplied by the author.** Not on this list under its own name before — it was
   hidden inside the "2008/2009" conflation above.

   **It closes the reducing-agent question for this span and narrows a proposal.**
   The register recorded that question as "unverified for Narayanan 2011 and Leliveld
   2009". Verified now, and the answer is the opposite of the modern papers': β-ME at
   every step, a published ±reductant gel (Figure 3A: no reduction / 2% β-ME / 10 mM
   DTT), and an iodoacetamide thiol-blocking control. See `STATE.md` — **the "nobody has
   checked disulfides" proposal must be narrowed to fibril growth before it is put to
   anyone.**

   **It does not give a DISC1 aggregation-critical region.** Its mapped regions —
   765-854 dimerisation, 668-747 oligomerisation — are *ordered self-association*, which
   the paper explicitly distinguishes from aggregation ("we presently do not know whether
   this HMW multimer arises through simple misfolding or in a more coordinated process").
   Considered and rejected for `data/regions.json`; scoring them as aggregation regions
   would be a category error.

## Tier 1 — these fix the validation table

4. **Bradshaw et al. (2017)**, *J. Biological Chemistry* — TRIOBP-1 aggregation-critical
   region. Europe PMC returned HTTP 500. **RETARGETED 16 Nov 2026 — still wanted, but no
   longer a freeze blocker.** Figure 12B was the reason this sat at the top of Tier 1;
   Zaharija 2022 Figure 1B has since supplied the same 25 letters and the same range
   (item 4b), so §6.3's TRIOBP-1 row is closed without it. What remains here is the
   **mechanistic half**: the proline/charge "turn and interaction surface" hypothesis,
   the SEC/CD evidence for the isolated PH domain dimer (the negative-control row in
   `regions.json`), and whether any reducing agent was used.

4a. **Zaharija B & Bradshaw NJ (2024)**, "Aggregation of Disrupted in Schizophrenia 1
   arises from a central region of the protein", *Prog Neuropsychopharmacol Biol
   Psychiatry* **130**:110923. **Added 15 Nov 2026 from the thesis reference list
   (ref. 502). SUBSTANTIALLY ADDRESSED 16 Nov 2026, NOT CLOSED.**

   **Its preprint was read in full** — bioRxiv 2023.08.03.551216v1, supplied by the
   author — and it is the source of our DISC1 384-415 row. **The range is confirmed**
   three ways (D ends at 383; 1-383 does not aggregate, 1-415 does; 383+32=415 matches
   both "these 32 amino acids" and the stored 32-residue string). The Flag-DISC1
   **257-655** construct the thesis cites is its Figure 3E. `found_by` is clean: no
   aggregation predictor, and the region falls outside all four ESPRIT domains.

   **ABSTRACT READ 16 Nov 2026** (PubMed record, PMID 38135095; *Prog
   Neuropsychopharmacol Biol Psychiatry* **130**:110923, epub 21 Dec 2023). It confirms
   the claim survived peer review **unchanged in substance**.

   **NO FREE FULL TEXT EXISTS — reproducible negative, 16 Nov 2026.** Europe PMC's REST
   record for the DOI returns `isOpenAccess: "N"`, `inEPMC: "N"`, `inPMC: "N"`,
   `hasPDF: "N"`, no PMCID, and a single full-text URL marked *"Subscription required"*.
   bioRxiv has **only v1** (4 Aug 2023) — no revised post-acceptance version and no "Now
   published in" link, so there is no free text to diff against. The remaining free
   route is **item 0**, the first author's thesis.

   **What is still wanted, and it is now a single question.** Both abstracts say only
   "approximately 30 amino acids" — the figure 384-415 (32 residues) appears in neither.
   The preprint's body text writes the deletion as Δ384-**414** three times against
   Δ384-**415** in its figures, and *"approximately 30" is equally consistent with 30,
   31 and 32*, so the abstract cannot discriminate. **Get Figure 5 or the Results of the
   published version and read which one it prints.** That is the last freeze blocker,
   and it is one residue wide.

   Carry regardless: the Discussion's claim that 384-415 is "sufficient for aggregation"
   is **not supported by its constructs** — 384-415 was never expressed alone; 384-538
   and 1-415 were. Full assessments in `data/references_to_check.json`, keys
   `zaharija2023preprint` and `zaharija2024`.

   **Potentially a better-sourced Tier A DISC1 row than 384-415.** It is experimental
   region-mapping of DISC1 aggregation by the same group, and the thesis uses its
   Flag-DISC1 **257-655** construct, described there as "D and I domain only". Our current
   DISC1 Tier A row, 384-415, sits inside that span and has an **unverified range** — this
   paper may be where the boundaries actually come from, or may supersede them.
   **Check `found_by` carefully:** a region found by an aggregation predictor is circular
   for this benchmark no matter how good the paper is.

4b. ~~**Zaharija et al. (2022)**, *Int. J. Mol. Sci.* **23**:11048.~~
   **RESOLVED 16 Nov 2026 — READ IN FULL, supplied by the author. It is EIGHT
   residues; `regions.json` was right and the thesis is wrong by one.** The paper says
   "8 amino acids (333-340)" in its abstract, its discussion (p.13) and its Figure 6D
   legend.

   **It also cleared a blocker it was not fetched for.** Figure 1B prints the 25-mer —
   `ELEKL|PLRENKRVPLTALLNQSRGERRGPP|SDGHE` under its own 324-348 numbering row — which
   reproduces our DERIVED string byte-for-byte. **The TRIOBP-1 half of §6.3 is closed**,
   and the 48.0% gatekeeper headline no longer rests on a reconstruction. Full
   assessment in `STATE.md`; two further findings there (a construct-specific conflict
   over 324-328, and READ confirmation that 593, not 597, is the short-variant length).

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
   **STILL OPEN, and do not confuse it with Basha et al. 2026.** A different
   co-aggregation review — [*Ageing Res. Rev.* 118:103148
   (2026)](https://doi.org/10.1016/j.arr.2026.103148) — was read in full on 15 Nov 2026.
   It covers Tau, α-syn, Aβ and TDP-43 only, **pre-empts nothing**, and **does not cite
   the *Cells* 2023 review or any psychiatric co-aggregation work**. Full assessment in
   `data/references_to_check.json`, key `basha2026`.

8a. **Bondarev SA, Antonets KS, Kajava AV, Nizhnikov AA, Zhouravleva GA (2018)**,
   "Protein co-aggregation related to amyloids: methods of investigation, diversity, and
   classification", *Int. J. Mol. Sci.* **19**:2292, doi:10.3390/ijms19082292.
   Added 15 Nov 2026 from Basha et al.'s reference list. **Open access (MDPI), so this is
   a fetch rather than a paywall.** It classifies co-aggregation into **titration,
   sequestration, axial and lateral** modes, each with different functional consequences
   and different intervention strategies. **Our DISC1 × CRMP1 and DISC1 × TRIOBP-1
   results do not say which mode they are**, and the tag-orientation dependence of the
   TRIOBP-1 × CRMP1 result is exactly what a sequestration-versus-direct-binding
   distinction would have to settle. Obtain before the co-aggregation claim is written up.

8b. **Two experimental co-aggregation interfaces worth a row each**, both from Basha
   et al.'s citations and both **not** simulation-derived — unlike nearly everything else
   in that review, which is MD or REMD and therefore circular under `found_by`:
   - **Sun C, et al. (2025)**, *J. Biol. Chem.* **301**:108351 — cryo-EM of an α-synuclein
     polymorph ("strain B") that promotes Tau aggregation via a critical C-terminal
     segment **D105–E115**.
   - **Yin H, et al. (2025)**, *Cell Death Discov.* **11**:76 — PS1/γ-secretase cleaves
     TDP-43 at residue **315**, upregulating APP and increasing Aβ production.
   Check the construct and the frame before either is considered for `data/regions.json`.

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

---

## Added 16 Nov 2026 by the three parallel audits

Ordered by how much each one decides. Every row these would promote is currently
at **READ-BY-SUBAGENT** grade, which is weaker than READ and cannot be published.

10. **Giasson et al. 2001, *J. Biol. Chem.* 276:2380** — α-synuclein 71-82.
   **PARTLY RESOLVED 16 Nov 2026 WITHOUT THE PDF.** The structured abstract,
   read in full via efetch, states the discovery path outright and the row is
   **CLEAN**; the sequence is verified against UniProt. The branch is not empty.
   Downgraded from highest priority: the full text is now needed only to trace
   whether anything narrowed *within* the hydrophobic domain beyond the
   β-synuclein alignment. All free routes are 403/closed — see STATE.md.
   **The highest-value request in the α-synuclein branch, because it decides the
   whole branch.** Five of the six other α-synuclein regions assessed are
   CIRCULAR (2-7, P1 36-42, P2 45-57 from a Zyggregator/CamSol pass; NACore
   68-78 and preNAC 47-56 from a ZipperDB track in Figure 1). If 71-82 is also
   circular, **α-synuclein contributes no clean row at all** — which is itself a
   finding worth reporting. Agent reports the full text sits behind Cloudflare.

11. **von Bergen et al. 2000, *PNAS* 97:5129, Figures 1 and 4** — tau PHF6
   306-311 and PHF6* 275-280. Confirms the **two strongest clean candidates in
   the entire sweep**: agent reports a systematic 15-mer peptide walk from L253
   to D348 with no algorithm named anywhere, four years before TANGO. Already on
   the obtain list; this raises its priority.

12. **Shimonaka et al. 2016, *J. Biol. Chem.* 291:8896** — TDP-43 tiles 274-313,
   314-353, 354-373. **Three rows from one PDF**, and the only window-tiling
   aggregation screen the unbiased-screen audit found in the whole field. Also
   settles whether 314-353 really is assay-discordant.

13. **The three complete-scan papers nobody could open.** All closed access, all
   yield regions, and two of them disagree with each other and with Gray 2019 at
   24-28:
   - Williams et al. 2004, *J. Mol. Biol.* 335:833 (proline scan, Aβ40) —
     abstract gives 15-21, 24-28, 31-36. **Whether all 40 positions were
     substituted is not in the abstract**, so completeness is unverifiable
     without the PDF.
   - Williams et al. 2006, *J. Mol. Biol.* 357:1283 (alanine scan) — abstract
     gives 18-21, 25-26, 32-33, and **says the scan is incomplete**: "most
     N-terminal residues were not tested."
   - Morimoto et al. 2004, *J. Biol. Chem.* 279:52781 — "34 proline-substituted
     mutants" of 42 positions, so **also incomplete**; which 8 were skipped is
     not in the abstract. The JBC URL OpenAlex advertises returns 403.

14. **Jiang et al. 2013, PMC3707662** — to settle the **DISPUTED** row C1 of
   `aggregation_region_ground_truth_inventory.md`. Our note says the 318-343
   patch came out of an unbiased N→C truncation walk; an audit subagent says it
   was named by sequence analysis first. Both claim to be from reading the paper.
   **Check whether 318-343 is introduced before the truncation series or as its
   output.** Until settled, that row is scored by neither arm.


---

## FREEZE BLOCKERS created by PREREGISTRATION §12.1 decision 3 (16 Nov 2026)

The publisher-PDF gate was made precise, and two promoted rows fail it. **Neither
may be cited in a manuscript until obtained.**

15. ~~**Murray et al. 2017, *Cell* 171:615 — the version of record.**~~ **OBTAINED AND READ
    IN FULL, 16 Nov 2026. CLEARED.** Every recorded claim re-checked and all hold. It also
    supplied a fully parameterised published run of all eight predictors on FUS-LC 2-214,
    which becomes a second validation target for the §5.1 FoldAmyloid reimplementation, and
    the Figure S7 legend revealing that ZipperDB cannot score proline-containing windows at
    all. Original entry follows for the record.**
    **Highest priority of anything on this list.** FUS 39-95 is a **primary-stratum
    discordant row**, and it was read as PMC5650524 web text with no PDF opened,
    so `source_version` is `pmc_full_text` and it is **not citable**. The quoted
    predictor sentence and the 39-95 core definition both need checking against
    the published article. The gate bites on the main analysis, not a side row.

16. ~~**Richards et al., the PUBLISHED version — PMC9934627.**~~ **THE REQUEST WAS WRONG, AND
    IS NOW CLEARED.** `PMC9934627` **is the preprint**, hosted in PMC under the NIH preprint
    pilot with an explicit "has not yet been peer reviewed" banner. I had assumed a PMC id
    implied a published version. **The peer-reviewed version is *Structure* 31(11):1386-1393.e3,
    doi 10.1016/j.str.2023.08.007, PMID 37657439, `PMC11456264`** — obtained and read 16 Nov
    2026, and the 55-75 core range is confirmed unchanged through review (stated five times).
    **Rule for this list from now on: name the journal and DOI, never a bare PMC id, and check
    the PMC record for a preprint banner.** Original entry follows for the record.**
    LECT2 55-75 rests on the **bioRxiv preprint** (10.1101/2023.02.08.527771),
    which was never peer reviewed. **Re-check the 55-75 core range against the
    published version**, since a range can change in review — and this row's whole
    value is that its range disagrees with the ex vivo ALECT2 structure.

17. **The `UNRECORDED` rows.** Every row promoted before 16 Nov carries
    `verified_against_publisher_pdf: true` but no record of *which version* was
    opened. **This is a lookup, not a re-read, and it must not be guessed.**
    Resolve before the freeze.
