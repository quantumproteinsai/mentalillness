# In silico aggregation in mental illness — state as of 17 Nov 2026

> **17 Nov 2026 — the project crossed from preparation into result.** The
> pre-registration is frozen (`freeze-2026-11-17`), the first predictor has been run,
> the dataset is published at **10.5281/zenodo.24306057**, and the headline question
> has an answer, with BOTH arms run. **Read the last section of this file first**; everything above it is
> the record of how the ground was prepared, and remains true.

Everything here was established by reading sources or parsing deposited files,
not by summarising abstracts. Where a claim rests on a snippet or a secondary
citation it says so. Papers nobody could open are listed in
`reports/PDFs_to_obtain.md`, ranked by what changes if you read them.

## The one-line position

The structural route is closed, the predictor route is open, and the reason the
predictors fail is now documented well enough to be the paper rather than the
result.

## What is closed, and how firmly

**No psychiatric aggregation system is structurally tractable.** Not "not yet
determined" — enumerated and absent.

- All **51** entities annotated as steric zippers in the PDB were listed by
  sequence: Sup35, PrP, Abeta, insulin, RNase A, IAPP, tau, TDP-43,
  beta-2-microglobulin, SOD1, curlin, PSM-alpha, Als5, porin. **Not one is a
  psychiatric protein.**
- Aggregate coordinates for the five candidates: **0 of 5.** TRIOBP, dysbindin
  and NPAS3 return nothing at all; CRMP1 has only its native fold; DISC1 has
  four entries, none an aggregate.
- The entire DISC1 structural corpus — 4 PDB entries, 1 EMDB map, 1 BMRB entry —
  carries **75 helix records and zero strand records**, confirmed by parsing the
  files rather than trusting annotations.
- **No patient-tissue structure exists for any psychiatric diagnosis**, by cryo-EM,
  ssNMR, microED or X-ray.

So no interaction energy across a sheet-against-sheet contact can be computed
for any of these proteins. The quantum-chemistry capability this author has does
not reach this disease area, and saying so precisely is worth more than saying
it vaguely.

## Three corrections to carry

**The DISC1 positive control does not exist as described.** Cukkemane 2021
deposited **nothing** — no coordinates, no chemical shifts, no EM map, no
accession, and the paper has no data-availability section. The EM was
negative-stain TEM at 120 kV with no resolution reported. The model is a
MODELLER protomer built with **antiparallel beta-strand restraints imposed as
input**, then docked into that envelope. The 2025 follow-up states verbatim
"No data was used for the research described in the article."

Consequence: the 716-761 beta-core is a *docking restraint*, not a measurement.
A prediction and a model that agree are not a confirmed prediction. The planned
positive/negative control pairing between DISC1 and TRIOBP-1 does not hold —
there may be two negative controls, which changes the benchmark design before
the pre-registration is written rather than after.

**The flagship tissue citation is the wrong paper.** PMC10378145 was recorded in
this project as "insoluble proteins in schizophrenia brain tissue". Its 33
donors are 15 suicide, 11 control, 4 depression and 3 Alzheimer — **zero
schizophrenia cases**. Western blot only, no fold changes, no p-values, no FDR;
positives called at 1.5x the cohort mean. On its own counts, 9/15 against 5/11:
**Fisher exact p = 0.69, odds ratio 1.7 (95% CI 0.4 to 7.8)**. It establishes no
case-control difference. The actual flagship is Nucifora 2019, whose MS is
published at pathway level only and whose full text nobody could open.

**The strongest result in this literature publishes no statistic for it.**
TRIOBP-1 insoluble in 12/25 schizophrenia, 15/25 depression, 2/50 controls,
called significant with no p-value for the headline comparison. Computed from
those counts: **p = 1.2e-05, OR 18.0** and **p = 1.4e-07, OR 28.6**. Strong — and
the counts are second-hand, and the same paper prints an impossible p-value of
"3.7 x 10^4". Verify before use.

## What is open, and it is the project

**No protein-language-model predictor has ever been run on DISC1 or TRIOBP-1.**
Not AggreProt (2024), not AggrescanAI (2026), not any of thirteen others. The
decisive evidence is structural rather than keyword-based: a September 2026
census of over forty prediction tools covering all five target proteins contains
no PLM predictor anywhere in its tool list. Both tools needed are installable,
maintained and sequence-only.

Of the four tools that failed in 2017: **TANGO and AGGRESCAN are live, the
FoldAmyloid server is unreachable and ProA returns 404.**

**But a dead server is not a dead method, and the two must not be stated as
one.** The FoldAmyloid primary paper was read in full on 15 Nov 2026
(Garbuzynskiy, Lobanov & Galzitskaya, *Bioinformatics* 26:326-332, 2010,
doi:10.1093/bioinformatics/btp691), and the method is **completely specified**:
three 20-value amino-acid scales — expected packing density, and
backbone-backbone hydrogen-bond probability assigned to donors and to acceptors
— a **5-residue sliding window**, a region called amyloidogenic when **five or
more consecutive residues** exceed the cutoff, cutoffs of 21.4 contacts/residue,
0.697 donor, 0.671 acceptor, 0.090 twice-hybrid and 0.062 triple-hybrid, and
hybrid scales built by z-normalising each scale to mean 0 and sd 1 and averaging
with equal weights.

The **only** missing piece is the 20 numeric values per scale: Figure 1 plots
them as bar charts, and the text refers the contact scale to Galzitskaya et al.
2006a. **Galzitskaya et al. 2006b, *PLoS Comput Biol* 2:e177, is open access**
and is the stated source of both the 3769-structure database and the
packing-density calculation. One fetch stands between this project and a
reimplementable FoldAmyloid, so the legacy baseline is **three of four runnable,
not two**, with the server's death a separate and still-publishable finding.

The server check has also been redone properly: the paper publishes
`http://antares.protres.ru/fold-amyloid/`, **not** the `bioinfo.protres.ru` host
this project tested. Both return 000 over http and https, as does the
`amyloid_base.html` dataset page. Dead or blocked from this host remains
undecided, so "down on 2026-11-15" stays the defensible claim.

**And a FoldAmyloid negative is worth very little even when it runs.** Three
things, all `[READ]` from the paper:

- **It misses VQIVYK.** "In the case of unstructured tau-protein, **only contact
  scale** finds the experimentally detected region (306-311)" — two of three
  scales miss the canonical steric zipper. The abstract's "10 out of 11" is
  reached twice by different routes: the packing-density scale gets 10/11
  missing a myoglobin fragment, and the **acceptor scale, its best performer on
  peptides, gets 10/11 by missing tau PHF6**. No single scale reaches 11.
- **Its decision unit is five residues**, which is primary-source support for
  the section below rather than an inference from it.
- **Its taxonomy has no category for these regions.** The paper names type I
  (hydrophobic) and type II (Gln/Asn-rich, GNNQQNY), states that "most methods
  of prediction of amyloidogenic fragments are designed for searching for the
  regions of type I", and that "our database contains **no** amyloidogenic
  peptides of the second type". A proline- and charge-rich region is neither.

**Its benchmark is also contaminated, and its published head-to-head is one
standard error wide.** The 407-peptide set (144 amyloidogenic, 263 not) is
merged from Fernandez-Escamilla 2004 — TANGO's own paper — and Thompson 2006,
the 3D-profile paper; cutoff and window were **optimised on it**, so the
headline 80%/72% is in-sample. Table 2's 179 peptides are "in fact a third of
our database", a subset of that same tuning set, while TANGO's row comes from a
set derived from TANGO's own paper and PASTA's row from PASTA's own paper. The
table spans 0.73-0.79 sensitivity and 0.73-0.79 specificity; at n <= 179 the
binomial standard error on any one value is about +/-0.04 to 0.06, so **no
method in it is distinguishable from another** — the CANYA conclusion already
recorded below, now reachable from a 2010 primary source.

### The Tier 0 risk to this is CLOSED. The gap holds. [READ, 15 Nov 2026]

**Samardžija B (2025), "Aggregation, parallel aggregation and co-aggregation of
proteins in chronic mental illnesses", PhD thesis, University of Rijeka, Faculty
of Biotechnology and Drug Development. Mentor: Nicholas J. Bradshaw. Defended
5 June 2025.** 274 pp. Supplied by the author on 15 Nov 2026 and **read in full**
after both recorded URLs 404'd and the institutional repository returned 418.

**It contains no aggregation predictor runs of any kind.** The methods chapter
(§3.1-3.19) has no bioinformatics section. Every named piece of software is
instrumentation or statistics: ImageLab, CellSens, ImageJ/Fiji, JASP, Prism,
MassHunter, FlyTracker/MATLAB, a Python script for social-interaction networks,
BioRender, and ProSite — the last used only to draw domain cartoons (Figures 2
and 3), not to score anything. **TANGO, AGGRESCAN, FoldAmyloid, ProA, WALTZ,
PASTA, AmylPred2, AggreProt and AggrescanAI appear nowhere, nor does any
protein language model, nor AlphaFold.** The thesis's only "in silico" phrase is
about *CRMP1* missense variants and is a citation to Ravindran et al. 2022, not
work done here.

~~So the claim stands as written: no aggregation predictor, of any generation,
has been run on DISC1 or TRIOBP-1 by the group that mapped their
aggregation-critical regions.~~

### FALSIFIED 16 Nov 2026. That claim was wrong, and the wrong thesis was read. [READ]

**Samardžija's thesis contains no predictor runs. ZAHARIJA'S DOES.** Her 2025
thesis — the one found by accident the same day, then supplied from the uniri
repository — contains **§4.3.5, "Assessing the aggregating potential of the
linker region using online prediction tools"**, Figures 40 and 41, and Table 5,
which lists the servers with URLs. **The group that mapped DISC1's
aggregation-critical region ran five aggregation predictors on it.**

| tool | year | status for this project |
|---|---|---|
| TANGO | 2004 | legacy baseline — **already run on DISC1** |
| AGGRESCAN | 2007 | legacy baseline — **already run on DISC1** |
| FoldAmyloid | 2010 | legacy baseline — **already run on DISC1** |
| MetAmyl | 2013 | not previously in our set — **already run** |
| ANuPP | 2021 | not previously in our set — **already run** |

Run on full-length DISC1 (**NP_061132.2**, not UniProt Q9NRI5 — check the frames
match), at default parameters, with **a per-residue consensus computed across
all six algorithms** (Figure 41B). That is, in outline, the retrospective
legacy arm of this project, already executed and already in a thesis.

**What this kills.** The sentence above, in that form. Any plan to run TANGO,
AGGRESCAN, FoldAmyloid, MetAmyl or ANuPP on DISC1 and present the result as new
is now reproducing published work. **Rule 2's cousin: check the prior art before
spending, and this time the prior art was inside a document the obtain list had
already flagged.**

**What survives, and it is the actual question.** `PREREGISTRATION.md` §5.2
states the novelty claim narrowly — *"no **PLM** predictor has ever been run on
DISC1 or TRIOBP-1"* — and **that is still true.** No protein language model, no
AggreProt (2024), no AggrescanAI (2026) appears anywhere in the thesis. The
project's question as CLAUDE.md states it — *do **modern** predictors recover
what the 2004-2010 generation missed* — is untouched. The pre-registration was
written more carefully than this file was.

**And their own result is evidence for the premise, not against it.** Zaharija
reports that four of the five tools returned "aggregation/amyloid formation
hotspots dispersed throughout the entirety of the protein sequence" — i.e. they
did **not** single out the linker. Only ANuPP did, calling AA **387-395** and
**400-415** the highest-nucleation segments. So the legacy generation missed it
and one 2021 tool found it, reported by the group itself. That is a sharper and
better-sourced starting point than the one we had — but it is **theirs**, and
must be cited, not rediscovered.

**Caveat on scope.** This is the *thesis*. Whether §4.3.5 also appears in the
published Zaharija & Bradshaw 2024 is unknown — the preprint (read in full) does
**not** contain it, so it was added later or is thesis-only. Either way the runs
exist. **TRIOBP-1 may still be clean:** nothing here shows predictors run on it,
and Zaharija 2022 (read in full) reports none.

**Three things the thesis changes anyway** (none of them the predictor question):

1. ~~**A numbering discrepancy inside the group's own work.**~~ **SETTLED 16 Nov
   2026 — see the next section. `regions.json` was right; the thesis is wrong by
   one.** p.48 states the TRIOBP-1 critical 25-mer was "later shortened to the
   **7 aa** domain"; `data/regions.json` carries **333-340, an 8-mer**.
2. **A DISC1 aggregation-region paper we did not have.** Reference 502: Zaharija
   B & Bradshaw NJ (2024), "Aggregation of Disrupted in Schizophrenia 1 arises
   from a central region of the protein", *Prog Neuropsychopharmacol Biol
   Psychiatry* **130**:110923. The thesis uses a Flag-DISC1 **257-655** construct
   ("D and I domain only") from it. This is experimental region-mapping of DISC1
   aggregation by the same group — **a candidate Tier A row, and possibly a
   better-sourced one than 384-415, whose range is still unverified.** Added to
   the obtain list.
3. **The disease contrast is weaker than the field's earlier papers implied, and
   the thesis says so itself.** Aggregation of DISC1, CRMP1 and TRIOBP-1 is
   present in controls, is region-specific, and the **highest DISC1 aggregation
   signal of any group was in controls** (lateral orbitofrontal gyrus). The
   author states plainly that earlier studies pooled all CMI patients against
   controls and that the phenomenon is a subset, not a diagnosis marker. **This
   does not touch our benchmark** — we score predictors against *fragment-level
   mapped regions*, not against disease association — but it is a reason never
   to describe these as "the schizophrenia aggregates" in print.

**What the thesis does NOT give us:** no new fragment-level mapped region, no
TRIOBP-1 25-mer sequence, and no DISC1 384-415. It confirms only the frames —
TRIOBP-1 "593 or 652 aa" (p.47) and DISC1 854 aa (p.38). The §6.3 blockers
survive it untouched.

### The TRIOBP-1 Tier A row is READ, and the thesis was the one that was wrong [READ, 16 Nov 2026]

Zaharija et al. 2022, *Int. J. Mol. Sci.* **23**:11048 — the paper the item
above said to resolve against — was supplied by the author and **read in full**
as the publisher PDF. It settles more than it was fetched for.

**1. The 7-vs-8 conflict: it is EIGHT, and `regions.json` was right.** The paper
says so three times — "just 8 amino acids (333-340 of the 652 amino acid-long
TRIOBP-1)" in the abstract, "just 8 amino acids (AA 333-340)" in the discussion
(p.13), and "narrow the critical region to AA 333-340" in the Figure 6D legend.
The 2025 thesis's "7 aa" (p.48) is a slip by one. **This is the third time a
secondary restatement has disagreed with the primary and lost** — the project's
rule about residue numbers from reviews holds again, and this time the review
was the group's own student's thesis.

**2. The 25-mer is no longer DERIVED. §6.3's TRIOBP-1 blocker is CLEARED.**
Figure 1B prints `ELEKL|PLRENKRVPLTALLNQSRGERRGPP|SDGHE` beneath its own
324-348 numbering row, five flanking residues either side. It reproduces the
reconstructed string **byte-for-byte**. Two alignment checks that could have
failed did not: 333-340 comes out `LTALLNQS`, zero charges, which the paper
independently calls "the uncharged region"; 341-345 comes out `RGERR`, which it
calls "the cluster of charged amino acids beginning at AA 341". **The 48.0%
gatekeeper headline no longer rests on a reconstruction**, and Figure 12B of
Bradshaw 2017 is no longer needed for the letters — only for that paper's
mechanistic half. The range is read too (§2.2, p.6).

**3. A new construct caveat, and it is the kind this project exists to catch.**
The Figure 6B legend restates **324-328 as "essential for aggregation"**, citing
Bradshaw 2017 — but the same paper's Figure 3D shows **333-652 aggregating
indistinguishably from 324-652**, and its text concludes "the first cluster of
charged amino acids is not required for aggregation". Both are correct:
necessary in the 324-vs-349 truncation comparison, dispensable in the 333-652
construct. The 324-328 row in `regions.json` now carries this and is marked **not
to be scored as an independent region.**

**4. The 593-vs-597 trap is confirmed, and 593 is the right number.** The paper
gives the short variant as **593 aa** on p.2 ("lacking this region and thus being
593 amino acids long") and as **597 aa** on p.13-14 ("expressed as a 597 AA long
protein, starting at AA 60"). It also fixes the frame: the two variants are
"amino acids 1-652 and 60-652 respectively", and 60 to 652 inclusive is **593**.
So the p.13 figure is the paper's own arithmetic slip. `CLAUDE.md`'s numbering
trap is now READ-confirmed rather than inherited.

**What it does not do:** it does not touch DISC1 — but the next two papers did.

### Both Tier A rows are now READ. §6.3 is cleared. [READ, 16 Nov 2026]

Two more PDFs arrived the same day, both supplied by the author.

**Zaharija & Bradshaw 2023 (bioRxiv 2023.08.03.551216v1) is the source of the
DISC1 384-415 row, and the range holds.** Three internal checks agree: the D
region ends at 383; construct 1-383 does not aggregate while 1-415 does; and
383 + 32 = 415 matches both "these 32 amino acids were deleted" and the
32-residue UniProt string we had already stored. `found_by` is clean — found by
truncation and deletion, no aggregation predictor — and the region sits outside
all four ESPRIT domains, "not found within any of 94 most stable DISC1
fragments", so the structural screen missed it too. That sharpens the central
pattern rather than weakening it.

**Two things must travel with that row.**

1. **The paper's sufficiency claim overreaches its own constructs.** The
   Discussion says 384-415 "was both sufficient for aggregation, and that
   aggregation was abolished when it was deleted". The second half is clean:
   deletion abolishes aggregation in 1-854, 1-836 and 1-655 alike. The first
   half is not — **384-415 was never expressed alone.** What was expressed alone
   is the whole linker, **384-538** (155 residues), and **1-415**. So
   sufficiency is established for the linker, and for 384-415 *in the context of
   1-383*. **Never write "384-415 is sufficient for aggregation" unqualified.**
   The `construct` column caught this, which is the second time this week that
   column has earned its place.
2. **It is a preprint, and the version of record is so far only an abstract.**
   *Prog Neuropsychopharmacol Biol Psychiatry* **130**:110923, PMID 38135095,
   epub 21 Dec 2023. Its **abstract was read 16 Nov 2026** and the claim
   survived peer review unchanged in substance. **But the abstract cannot close
   the item, for an exact reason:** both versions say only "approximately 30
   amino acids", and the number we carry is **32** (384-415). The case needing
   exclusion is a **one-residue** change at the C-terminal boundary — the
   preprint's body text wrote Δ384-**414** three times against Δ384-**415** in
   its figures — and "approximately 30" reads identically whether the answer is
   30, 31 or 32. **Only Figure 5 or the Results of the published version
   settles it.** The last freeze blocker is now one residue wide and precisely
   stated, which is better than open-ended, but it is not closed.

   *Note what just happened: the abstract of the version of record, read
   carefully, could not supply the number the row depends on. That is the rule
   about reading primaries restated from the other direction — a primary read at
   abstract depth is still a secondary for this purpose.*

**A third one-residue slip, in two days, from the same group.** The body text
writes the deletion constructs as **Δ384-414** three times (31 residues) while
Figure 5A and panels D-F label them **Δ384-415** and the same sentence says
"these 32 amino acids". 384-415 is right.

**Running tally of residue-number inconsistencies found by reading primaries,
all within single papers, 15-16 Nov 2026.** This is now a documented property of
the literature, not a run of bad luck:

| paper | prints | and also | right answer |
|---|---|---|---|
| Zaharija 2022 / 2025 thesis | 333-340, "8 amino acids" ×3 | thesis p.48: "the 7 aa domain" | **8** |
| Zaharija 2022 | short variant "593 aa" (p.2) | "597 AA long protein" (p.13) | **593** |
| Zaharija & Bradshaw 2023 | Δ384-**414** ×3 (body) | Δ384-**415** (Fig. 5) + "32 amino acids" | **384-415** |
| Zaharija & Bradshaw 2023 | "AA 539-738" for I+S | same string for S+C | S+C = **635-836** |
| Leliveld 2009 | "668-**747**" (Abstract, Discussion) | "668 and **748**" (Discussion) | **668-747** (2 of 3) |
| Leliveld 2009 | S704 throughout | "DISC1-S**707**Δ22" (p.7) | **S704** |
| Mizuguchi 2019 (JBC) | Δ**68-76** (Table 1, Results, Methods) | "Δ**68-78**" ×2 (p.13521) | **68-76** | 
| Seuma 2021 (eLife) | gatekeepers "...E11, **D22**, L17, A42" (Discussion) | "...L17, **E22**, A42" (Methods) | **E22** — Aβ22 is Glu; the Dutch mutation is E22Q |
| Giasson 2001 (JBC) | peptide `VTGVTAVAQKT**V**` (title, abstract, Results, Discussion) | Methods: `VTGVTAVAQKT**A**` | **V** — P37840 position 82 is Val. **A SEQUENCE slip, not a numbering slip, and it sits in the description of the peptide carrying the whole sufficiency claim** |
| von Bergen 2000 (PNAS) | Abstract: scan of "the **full** τ sequence" | Fig. 4: "the region of τ from **L253 ... to D348**" (96 aa of 441) | **L253-D348**. A SCOPE claim, not a number — it decides whether the row is an unbiased scan of a PROTEIN or of a PRE-SELECTED DOMAIN |
| von Bergen 2000 (PNAS) | Discussion (v): "the corresponding **hexapeptides** in R1 (`244QTAPVPM250`)" | that sequence is **SEVEN** residues, 244-250 | **7**. Verified against P10636-8: 244-250 is `QTAPVPM`. The R4 partner `337VEVKSE342` really is six, so only the R1 label is wrong |
| Sharma 2023 (JMB) | Methods: "**seven** different computational programs" | then lists **eight** (ZipperDB, LARKSdb, Waltz, Aggrescan, FoldAmyloid, PASTA 2.0, TANGO 2.2, Amylpred 2) | **seven** — LARKSdb never reappears in Results or Fig. 4 |
| Sharma 2023 (JMB) | truncated construct "residues **Met286**-Phe320" | 286 is **Ser**; cannot contain Asp262; cannot cover a 251-295 core | **Met186** — the unique Met satisfying all three constraints; a digit transposition |
| Richards 2023 — **preprint AND version of record** | Table 1: "Ramachandran favoured (%) **5.26**" with outliers **0** | and "Favored rotamers (%) **94.74**" | labels **swapped**. 18/19 = 94.74%, 1/19 = 5.26%; favoured 5.26% with zero outliers is impossible. **It survived peer review at *Structure*** |
| Richards 2023 — version of record | Intro: "have been identified **and assemble into** amyloid-forming LECT2 peptides **assemble into** amyloid-like fibrils" | preprint: "have been identified, and **PREDICTED** amyloid-forming LECT2 peptides assemble into..." | the **preprint**. Copyediting garbled the verb and **dropped "predicted"** — the word that flags ref 20 as circular |
| Cukkemane 2021 | "the entire C-region comprising **160** amino acid residues" | its own boundaries, 691-836, give **146** | **146**. The 19.4 kDa tagged mass fits 146 + tag, not 160 |
| Cukkemane 2021 | Abstract + Methods restraints: β-core starts at **716** | Discussion, reporting the RADAR output: **717**-737 | **unresolved** — the paper does not say which. Row is CIRCULAR so it does not reach the primary |

**Seventeen, across eleven papers and NINE independent groups** (updated 16 Nov 2026: the
Mizuguchi slip found by reading the apoA-I primary, the Seuma slip reported by the
unbiased-screen audit). None of them changed a row, because each was caught by
arithmetic, by a figure, or — in the Seuma and Giasson cases — by knowing the
residue identity. **The ninth broke the pattern: the first eight were all NUMBERS,
this one is a SEQUENCE.** So the habit of checking ranges is not sufficient on its
own — check the letters against the database too, every time.
**The pattern is now clearly a property of the field and not of one lab:** the first
six were Bradshaw/Korth-adjacent, the last two are from two unrelated groups. **Verify every
residue number in this literature against the figure or the arithmetic,
including numbers in the paper a row is sourced to, and including the abstract.**

**Leliveld et al. 2009 is assessed in its own section below** — it does not
touch 384-415, and it narrows the redox proposal rather than confirming it.

### The thioflavin T negative is not where we thought, and I put it there [READ, 16 Nov 2026]

**Correction of something this file asserted earlier the same day.** On
splitting the merged "Leliveld 2008/2009" obtain-list entry I wrote that the
2008 *J. Neurosci.* paper "carries the thioflavin T and cold-sarkosyl claims."
The cold-sarkosyl half is right. **The thioflavin T half was wrong.** Both
Leliveld papers have now been read in full and **neither contains a thioflavin
T experiment of any kind.** Cukkemane 2025 attributes the ThT negative to
"Leliveld 2009 and Korth 2012"; the Leliveld half of that attribution does not
hold. It rests on **Korth 2012 alone, still unread**, or it is a mis-citation.
**Nothing in this project may lean on the ThT negative until Korth 2012 is
read.** I inferred it from a citation instead of reading it, which is precisely
the line rule 1 draws.

**The question it was being used for is substantially answered anyway, by a
better measurement.** Leliveld 2008 reports that the rDISC598 dimer has
"essentially the same far-UV circular dichroism spectrum as the combined
oligomer plus multimer fraction, indicating that rDISC598 **self-associates as
folded subunits**", and its Discussion states plainly: "we do not think that
the type of Sarkosyl-resistant DISC1 aggregates described here are directly
comparable with those found in classic misfolding diseases, because we do not
have evidence of extensive conformational misfolding of multimeric DISC1."
**The originating group declined to call the disease species an ordered amyloid,
on CD evidence, in 2008.** That is firmer than a dye negative — a dye negative
in a dilute extract can be a sensitivity failure, CD on purified protein cannot
— and it is now READ rather than inherited.

**Two numbers in that paper do not match its own data, and one of them matters
to us.** The Discussion says "~20% of sporadic cases"; the reported subgroup is
**7 of 45 = 15.6%**. And the Abstract says insoluble DISC1 was found in patients
"**but not healthy controls**" — while Figure 1b shows a **nonzero control mean
of 0.4** and at least one control near 1.5, with the positivity threshold
*defined as* "strongest background immunoreactivity in normal controls".
**Controls are not clean, and the paper's own figure says so.** This is the same
pattern the 2025 thesis found independently seventeen years later. It is
corroboration, and it is a standing prohibition on "absent in controls" phrasing
anywhere in our write-up. Also stated by the authors and worth carrying: brain
samples were processed blinded, **but the Western blot analysis was unblinded.**

**The redox thread is now fully closed on the Leliveld side.** 20 mM β-ME in
inclusion-body solubilisation, 10 mM in on-column refolding, 5 mM DTT in the SEC
buffer and in DLS, 5 mM glutathione in the cell lysis buffers. Both Leliveld
papers used reductant throughout. **Only Narayanan 2011 remains unverified.**

**A premise to check in the DISC1 384-415 chain.** The 2023 preprint says the
~70 kDa insoluble brain species was "detected using an antibody that recognises
part of the C region of DISC1", citing this paper, and infers that the species
has lost roughly the first 250 residues. **This paper's Methods say its
antiserum was raised against full-length DISC1(1-854) and affinity-purified on
the same, and mAb 3D4 likewise against full-length.** A full-length immunogen
does not localise an epitope, so that inference loses the support it is given
here. The preprint cites Yerabham 2017 alongside — check there before calling it
an error.

**The pattern recorded earlier still stands:** both URLs the sweep logged are
dead and the repository blocks scripts, so this was obtained by asking the
author, not by retrieval. Availability recorded at sweep time is not
availability now — FoldAmyloid's server was the same day's other instance.

## Why the predictors fail — documented, not assumed

From the predictors' own method papers: Waltz is a position-specific matrix
built by exploring **hexapeptide** space; the 3D-profile method threads
six-residue windows onto templates generated from one crystal structure;
AGGRESCAN is a 20-value composition scale with no context term; TANGO was
validated on peptides with fully buried beta-cores. **A negative call on a
25-residue proline- and charge-rich turn is uninformative by construction.**
Peptide-to-protein performance is reported to fall from about 0.87 to 0.62
AuROCC, and the common benchmark set is not out-of-sample for several tools.

Then the inversion, which is the paper's spine. Proline and flanking charge are
**gatekeepers** — what the field deliberately engineers in to kill cross-beta.
Run `scripts/gatekeeper_density.py`:

    crystallised steric zippers:  0.0% to 16.7%   (n = 7)
    psychiatric regions:         18.8% to 48.0%   (n = 2)

> ### THE SEPARATION DOES NOT GENERALISE, and this is the paper's spine
>
> **Established 15 Nov 2026, once the clean DISC1 row was given its sequence from
> UniProt Q9NRI5 (854 aa, SV=3, retrieved from the REST API rather than transcribed).**
>
>     TRIOBP-1 324-348   48.0%   gatekeeper-rich, as claimed
>     DISC1    384-415   18.8%   +2.1 points above the WORST zipper (16.7%)
>
> DISC1 384-415 is `EQEKISLHFQLPSRQPALSSFLGHLAAQVQAA` — 2 prolines and 4 charges in 32
> residues. Against the worst crystallised zipper at 16.7%, that is **not a separation**.
> **18 of its 27 hexapeptide windows sit at or below the worst zipper**, minimum 0.0% at
> `ISLHFQ`.
>
> The published-looking "48.0% to 50.0% (n = 2)" was **TRIOBP-1 plus DISC1 716-761**, and
> 716-761 is the docking-restraint row whose `found_by` reads "RADAR sequence-repeat
> search" — found *by* a sequence search, which is precisely what that column exists to
> exclude. Swapping in the clean row **does not restore the headline. It breaks it.**
>
> **What survives, and it is narrower than the draft assumes:**
> - **n = 1 on the gatekeeper paradox.** One experimentally mapped region is half
>   proline and charge and is nonetheless aggregation-critical. That is a striking single
>   case, not a pattern across two proteins.
> - **n = 2 on the prediction failure**, which is untouched: both regions were found by
>   truncation, neither by prediction, and the predictors missed both.
>
> **These are two different claims with two different n, and the draft currently states
> them as one number.** The gatekeeper inversion cannot carry a paper about two proteins
> on one protein's worth of evidence. Either widen the validation set until the paradox
> has a second independent case, or demote it from the spine to a single striking
> observation and let the prediction failure carry the paper.

**Superseded note, kept for the record — corrected 15 Nov 2026 from n = 2 to n = 1,
then restored to a true n = 2 above.** The excluded row was DISC1
716-761, which `data/regions.json` flags in capitals as "THIS IS A DOCKING
RESTRAINT, NOT A MEASUREMENT" and whose `found_by` reads "RADAR sequence-repeat
search" — **found by a sequence search**, which is exactly what the `found_by`
column exists to catch. Scoring it put a predicted region inside a table about
predictor failure. The clean DISC1 row, **384-415** ("experimental; no
aggregation predictor involved"), is the one the N = 2 argument below rests on,
and it then carried **no sequence in `regions.json`** — which is why the table
briefly reported n = 1. **That sequence has since been supplied from UniProt
Q9NRI5 and the restored row broke the headline rather than restoring it**, as
the banner above records.

The cause was structural: the script **hardcoded sequences that duplicate
`regions.json`, and the two had drifted**. It now reads them from the
validation set and hard-fails on a mismatch, and names every excluded row with
its reason. The N = 2 claim below is unaffected — it is about two
experimentally mapped linkers, not about this table.

By the field's own published rules **TRIOBP-1 324-348** should be an aggregation
*suppressor*. Experiment says it is the aggregation-critical one. **That holds
for TRIOBP-1 and not for DISC1 384-415** — see the banner above.

**The separation is partly a window-length artefact, and that sharpens the
paper rather than weakening it.** The table compares **selected** 6-11 residue
cores against an **unselected** 25-residue region — a minimum against a mean.
Matched to the 5-6 residue window a predictor actually scores, TRIOBP-1 324-348
contains **7 of 20 hexapeptide windows at or below the worst crystallised
zipper**, with a minimum of **0.0%** at `LTALLN`. So "a negative call is
uninformative by construction" is too strong: a window-scanning predictor had a
0%-gatekeeper hexapeptide sitting inside the region and **missed the region
anyway**. That is a harder failure, and it does not depend on the whole-region
density at all.

**And one cheap computation still decides which paper this is.** The narrowed
8-mer `LTALLNQS` sits inside the 25-residue region and is itself **0%
gatekeeper** — indistinguishable from VQIVYK or GNNQQNY. Score it in isolation:
positive means the failure is about flanking context, negative means intrinsic
core chemistry. Different papers. Compute before framing — and **after** the
pre-registration, since scoring it is a predictor run.

## N = 2, not N = 1

TRIOBP-1 **324-348** is a 25-residue linker between the first two coiled coils.
DISC1 **384-415** is a ~32-residue linker C-terminal of the D region, outside all
four structured domains. Both found by truncation, neither by prediction. Two
coiled-coil scaffold proteins, two inter-domain linkers, two prediction failures.

Caveat that must travel with it: both come from the same laboratory, so this is
a second case rather than independent replication.

**"Register frustration" has no prior art as a phrase** — available to introduce,
citing the de novo coiled coil with a solved structure that converts to amyloid,
and the Q/N-rich work where aggregation tracks coiled-coil propensity. Claim the
determinant, not the sign: two papers disagree on whether stable coiled-coil
formation promotes or inhibits aggregation.

## The thing that is cheap and nobody has done — NARROWED 16 Nov 2026, it was partly done in 2009

The DISC1 fibril construct contains three free cysteines (C698, C762, C782), and
across the 2021, 2025 and 2026 papers there is **zero mention of DTT, TCEP,
mercaptoethanol, reducing conditions, disulfide or redox**. Those fibrils were
grown from a three-cysteine construct in air with the thiol state uncontrolled
and unreported. Non-reducing against reducing SDS-PAGE would settle it in an
afternoon.

**That still holds for the fibrils. It does NOT hold for the span.** Leliveld et
al. 2009 (*Biochemistry* **48**:7746, read in full 16 Nov 2026) worked on
rDISC1 **640-854**, which *contains the entire 691-836 fibril construct*, and
did the opposite of leaving redox uncontrolled:

- **β-mercaptoethanol at every step** — 20 mM in lysis, GnHCl solubilisation,
  GST wash and on-column refolding; 10 mM in preparative SEC, analytical SEC,
  DLS and the NDEL1 binding buffer; 1 mM DTT in the glycerol-gradient lysis.
- **The ±reductant experiment was run.** Figure 3A loads rDISC640 without
  reduction, with 2% β-ME, and with 10 mM DTT. Result, in their words: *"Adding
  reductant dissociated some of the slower migrating bands."* So some
  slow-migrating species in this span **are** reductant-sensitive.
- **And a thiol-blocking control exists.** Iodoacetamide treatment of reduced
  DISC640, to block disulfide formation by the extra cysteine of the C704
  variant, **did not** prevent 19F7 staining of the HMW multimers — so HMW
  multimer formation there is not disulfide-dependent.

**Why this matters more than a citation.** The plan was to put this to an
experimental group as a cheap decisive question. Put as previously written —
"nobody has checked whether disulfides matter for C-terminal DISC1 assembly" —
the group would answer that they published the ±reductant gel and the
iodoacetamide control seventeen years ago. **The question that survives is
strictly narrower:** the thiol state during *fibril growth* of 691-836 under
the 2021/2025/2026 protocols is still uncontrolled and unreported, and nothing
in Leliveld 2009 speaks to fibrils — it studies soluble dimers, oligomers and
HMW multimers. Ask that, not the broad version. [READ, 16 Nov 2026]

This is the third premise audit to change a proposal rather than a fact, and the
first to be caught by reading a paper the obtain list had already named.

Related and equally unexplored: **no seeding assay has ever been run on
psychiatric brain homogenate**, though FRET-biosensor and RT-QuIC are routine in
tau and alpha-synuclein. There is no published negative either, so "not
seeding-competent" and "never tested" are currently indistinguishable.

**That gap is wider than "routine", confirmed 15 Nov 2026.** These assays are
clinical-grade in the neurodegeneration field: CSF **seed amplification assays**
run on a longitudinal AD cohort to measure alpha-synuclein co-pathology
(Franzmeier 2025), alpha-synuclein **RT-QuIC** deployed as a differential
diagnostic across parkinsonisms (Quadalti 2021), and **Tau biosensor seeding
assays** run on brain extracts, where depleting TDP-43 from the extract measurably
reduced Tau seeding capacity (Tome 2023). All three `[READ]` as cited in
[Basha et al., *Ageing Res. Rev.* 118:103148 (2026)](https://doi.org/10.1016/j.arr.2026.103148).
The technique is not merely available; it is a working clinical instrument that
has never been pointed at a psychiatric diagnosis.

**A positioning point from the same read.** That review surveys protein
co-aggregation across Tau, alpha-synuclein, Abeta, TDP-43, huntingtin, p53, IAPP,
apoE and TFEB over 300-plus references, and **cites no psychiatric co-aggregation
work at all.** The DISC1/TRIOBP-1 literature is invisible to the field that owns
the concept — which is an argument for publishing into that field rather than
only into the psychiatric one.

**And a vocabulary trap recorded in `data/regions.json`.** "Co-aggregation" names
three unrelated phenomena: protein hetero-aggregation (our sense), **familial or
epidemiological** co-aggregation of diagnoses in pedigrees, and **bacterial**
cell-cell adhesion in biofilms. The middle one is the dangerous one here —
Liu et al., *Clin. Epidemiol.* 10:631-641 (2018) is titled "Familial aggregation
of Parkinson's disease and coaggregation with neuropsychiatric diseases" and
reports raised **schizophrenia** risk in first-degree relatives of PD patients, so
any query pairing the word with schizophrenia returns population genetics rather
than protein chemistry. This repository is currently clean of both foreign senses.

## Files here

    data/regions.json              the validation set, with construct context and
                                   a circularity column; 10 rows against a floor of 15
    data/references_to_check.json  sources nobody has opened; a lead is not a fact
    scripts/gatekeeper_density.py  reproduces the table above
    reports/PDFs_to_obtain.md      ranked by what changes if you read each one
    research_notes/                the six literature sweeps behind all of this

## The validation set can reach usable size — with a trap in the obvious route

A 146-row inventory across about 45 proteins now exists at
`research_notes/Mental illness aggregation structures/aggregation_region_ground_truth_inventory.md`.
Roughly **20 rows are circular** and roughly **40 are independent, across about
25 proteins** — five times the current table. The power problem is solvable.

**But the circular rows cluster in exactly the famous short-segment literature a
benchmark would reach for first**: p53 251-257, the hnRNPA1/A2 hexapeptides,
TDP-43's zippers, four SOD1 segments, alphaB-crystallin 90-100, the crystallised
Abeta hexapeptides, ataxin-3 73-96. **p53 has no predictor-free row at all.**
Neither does ataxin-3 73-96, whose downstream literature inherits from one paper
that opens "we first resorted to in silico predictions."

The independent rows sit in a different evidence class entirely: unbiased
truncation walks, limited proteolysis of real fibrils, exon-boundary fragment
series, patient-derived cleavage products, cryo-EM of ex vivo material.

**Do not bulk-import from CPAD.** The CANYA paper states verbatim that "several
of these methods (including TANGO, CamSol, and Aggrescan) were directly trained
on sequences within CPAD", violating out-of-sample evaluation on those datasets.
Importing rows from it without per-row provenance checks reproduces exactly the
violation that paper names. The same paper reports that on WALTZ-DB hexapeptides
"no method significantly outperformed hydrophobicity" — which is worth knowing
before treating any of them as a serious baseline.

**And the provenance column cannot be grepped.** Circularity is protein-specific,
not lab- or journal-specific: the same laboratory in the same era produced rows
of opposite status, and so did two segments of one protein. Four rows would be
wrongly flagged by keyword search, because a post-hoc remark about a predictor,
or the use of a disorder or helix-propensity tool, is not prediction-guided
discovery. Every row has to be read.

### Construct dependence is general, not a quirk of our two proteins

At least **15 rows independently record it**. A bacterial curli subunit is
defective in vivo yet polymerises with wild-type kinetics in vitro; a fungal
prion domain propagates in every transformant when GFP-tagged and in none of 24
untagged; gelsolin's short fragments fibrillise while its 68 kDa fragment cannot
even be seeded; one SOD1 proline gives opposite answers in vitro and in cells.

So the methodological claim survives in its narrow form and is reportable: **a
necessity result is a property of its construct**, which means one region can be
correctly reported as both critical and dispensable, and a benchmark treating
such rows as one fixed label scores against a moving target.

### Frame traps are worse than assumed

Beyond the TRIOBP-1 59-residue offset: **hnRNPA1's two frames differ by an
internal alternative exon**, so a commonly cited range exists only in the
minor-isoform frame and converting it by a constant offset produces a sequence
that does not occur. Tau's canonical accession is 758-residue big tau while the
whole literature uses the 441-residue frame. Huntingtin's frame shifts with the
repeat length.

### Two published predictor negatives worth citing

Amyloid predictors "were all unsuccessful in determining the beta-core interface
of DISC1". And the full-length hnRNPA1 cryo-EM core "does not encompass the most
aggregation-prone segments of the protein" — a second case of the same shape.

### Murray 2017 publishes both halves of this project's shape, for FUS [READ, 16 Nov 2026]

**Surfaced by the TDP-43/FUS audit and then verified directly** (WebFetch of
PMC5650524, not left at agent grade). Murray et al. 2017, *Cell* 171:615,
Discussion, "What determines the fibril core?":

> "Aggrescan, FISH, FoldAmyloid, MetAmyl, and PASTA 2.0 predict a low propensity
> for amyloid formation across the FUS-LC"

ZipperDB, Zyggregator and WALTZ "predict that certain short segments of FUS-LC
may form amyloidlike structures" but "with no consensus on the identities of
these segments." The experimentally determined core is **39-95**. And the
compositional argument is pre-empted in the same section:

> "The amino acid composition of residues 39-95 (21.1% Gly, 31.6% Ser, 17.5%
> Gln, 14.0% Tyr, and 10.5% Thr)" ... "is not very different from that of
> residues 1-214"

**So eight named predictors failing on an experimentally mapped core, AND
"composition does not explain it", are both in print in *Cell* since 2017.**

**What this does not touch.** The §5.2 novelty claim is **intact**: Murray 2017
is a 2017 paper on FUS, runs no PLM-era tool, and touches neither DISC1 nor
TRIOBP-1. The legacy-failure premise is **strengthened, not damaged** —
`CLAUDE.md` already declares that premise cited evidence rather than a result to
establish, and this is a third independent instance of it.

**What it does cost us.** The generic compositional move is gone. This project
cannot present *"and composition does not explain why the predictors missed it"*
as a new insight. What survives is the **inversion**, which is a different and
stronger claim: TRIOBP-1 324-348 is **48.0% proline-plus-charge**, i.e. built
from the residues the field deliberately engineers *in* to *suppress*
aggregation, and was mapped as aggregation-critical anyway. Murray says
composition is *uninformative*; we would be saying composition points the
*wrong way*.

**And the inversion is n = 1 by our own accounting.**
`scripts/gatekeeper_density.py` prints `THE SEPARATION DOES NOT GENERALISE`
because DISC1 384-415 came in at **18.8%**, 2.1 points above the worst deposited
zipper. So the one surviving novel compositional claim rests on a single region.
**This is a framing decision for the author, not a data problem:** is an n = 1
inversion with the generic version pre-empted a headline, or a discussion
paragraph? Claude should not decide it.

**Third prior-art hit, same audit round.** Seuma 2021 (*eLife* 10:e63364)
measures **"seven gatekeeper residues (D1, E3, D7, E11, L17, E22, A42)"** in
Aβ42 where mutations *increase* nucleation — charged residues acting as measured
aggregation suppressors. **The gatekeeper concept itself is prior art since
2021.** Cite it; do not re-introduce it.

### The FoldAmyloid host question, narrowed not solved

The audit noted that Murray 2017 ran FoldAmyloid successfully at
`bioinfo.protres.ru`, which bears on line 102 of this file naming
`antares.protres.ru` as the paper's host and `bioinfo` as the "wrong" one.
**Checked directly, 16 Nov 2026: both return 000.** So the correction is real
but narrow — `bioinfo.protres.ru` was a *legitimate* FoldAmyloid host, not a
mistake, and was working as recently as 2017. **It does not revive the tool.**
The §5.2 rule stands: a web form is not a reproducible tool.

### Giasson 2001 is CLEAN, and each clean row makes the inversion lonelier [ABSTRACT READ, 16 Nov 2026]

The audit left α-synuclein 71-82 UNDECIDABLE behind Cloudflare and warned the
whole α-synuclein branch might yield **no clean row at all** — 5 of the other 6
regions are CIRCULAR. **Settled from the structured abstract, read in full via
efetch.** The paper states its own discovery path:

> "1) human beta-synuclein is highly homologous to alpha-synuclein but **lacks
> these 12 residues**, and it does not assemble into filaments in vitro ... 3)
> this stretch ... **is resistant to proteolytic digestion** in alpha-synuclein
> filaments; and 4) **synthetic peptides** corresponding to this 12-amino acid
> stretch self-polymerize"

Comparative homology against a paralogue that naturally lacks exactly those 12
residues, corroborated by limited proteolysis. **No predictor, and in 2001 none
of the tools under test existed.** `VTGVTAVAQKTV` verified residue-for-residue
against UniProt P37840 — the paper's numbering is right, so no ninth slip.
It is also the only candidate in the file shown **necessary *and* sufficient**,
with sufficiency in an isolated peptide.

**Full text still not obtained, and that is reproducible:** jbc.org 403 on
fulltext, legacy and PDF routes; Europe PMC `isOpenAccess=N`, no PMCID; OpenAlex
advertises `hybrid` but its `oa_url` is just the DOI, resolving to a
Cloudflare-gated Elsevier page.

**Two caveats that matter more than the row.**

1. **It is a region the predictors DO find.** 71-82 overlaps NACore 68-78 by
   eight residues, and NACore was later picked by ZipperDB. Clean by `found_by`,
   but it cannot test the central hypothesis — its honest role is a labelled
   **true positive**, good for the dataset, neutral for the headline.
2. **It does not support the gatekeeper inversion — it dilutes it.** Computed
   from the verified sequence: **8.3%** proline-plus-charge (one lysine), *below*
   the worst deposited zipper at 16.7%.

**The trend is now the finding, and it is going the wrong way for the
headline:**

| region | gatekeeper % | behaves as the field's rules predict? |
|---|---|---|
| TRIOBP-1 324-348 | **48.0%** | **no — the inversion** |
| DISC1 384-415 | 18.8% | yes |
| α-syn 71-82 | 8.3% | yes |
| α-syn NAC 61-95 | 8.6% | yes |

**Every clean row added so far has made the inversion lonelier rather than
better supported.** It stands at n = 1 against three. Combined with Murray 2017
pre-empting the generic compositional move and Seuma 2021 pre-empting the
gatekeeper concept, **the compositional strand of this project is now its
weakest, not its strongest.** Report the trend; do not wait for a fourth row to
rescue it.

### One comparator was an unlabelled disease mutant

`4ZNN` is deposited as `GVVHGVTTVA`, which is **A53T**, not wild type — UniProt
P37840 47-56 is `GVVHGVATVA`. Checked against the RCSB FASTA. The hardcoded
string was *right about the crystal*; the **label** implied wild type. Relabelled
`a-syn preNAC A53T (4ZNN)`. **Ala→Thr changes no gatekeeper count, so this moves
no number** (0.0% either way) — fixed anyway, because an unlabelled mutant in a
table intended for publication is a defect even when numerically inert.

### The clean rows are mostly regions the predictors FIND — and that limits the benchmark [READ, 16 Nov 2026]

**This is the most important design consequence of the 16 Nov sweep, and it is a
rule 2 problem rather than a sourcing problem.**

Three clean rows read in full on the same day all turn out to be regions the
predictors hit:

| row | why predictors find it |
|---|---|
| α-syn 71-82 | overlaps ZipperDB-selected NACore 68-78 by 8 residues |
| tau PHF6 306-311 | *"the only two spots in the τ sequence where a β conformation is strongly predicted"* |
| tau PHF6* 275-280 | the same sentence |

**That is not a coincidence and not an artefact of our sweep.** A region gets
mapped cleanly and early when it is a classic short hydrophobic or β-prone
motif — which is exactly what the predictors were built to detect. The regions
predictors *miss* are rare in the literature for the same reason they are
interesting: they are unusual.

**So widening the validation set mostly adds true positives, and true positives
cannot discriminate modern from legacy predictors, because both classes hit
them.** The rows that discriminate are the ones where experiment and prediction
*disagree* — currently TRIOBP-1 324-348 and DISC1 384-415, which is to say the
two we started with.

**Reaching the floor of 15 therefore does not buy 15 rows of statistical
power.** The pre-registered statistic should be computed on the **discordant
stratum**, with the true-positive stratum reported separately as a sanity check
that the predictors ran at all. **This must be decided before the freeze**, and
it changes what the floor of 15 means: 15 rows of *dataset*, far fewer rows of
*test*.

### von Bergen 2000 is clean, but not for the reason the audit gave

The subagent reported **"no algorithm named anywhere in the paper."** **That is
false.** Predicted β-structure appears at least five times, including in the
Abstract — *"This motif coincides with the highest predicted β-structure
potential in τ"* — in a Results heading, and in the Discussion.

**The row is still CLEAN**, because every one of those is *post hoc*: prediction
explains the scan result, it never selects the peptides, and the Methods name no
algorithm. The discovery path is GluC limited proteolysis → PHF43 → an
overlapping 15-mer peptide library probed against it → the hexapeptide; with
proline-scanning mutagenesis confirming necessity. But the honest claim is
**"prediction appears, in the permitted direction"**, not "prediction is
absent" — and a reviewer will find those sentences in ten seconds, so we should
state it first. **Treat subagent claims of absence as the weakest kind of
claim:** absence is what an agent is least able to establish and most likely to
assert.

**RESOLVED SAME DAY — the figures were open access all along.** PMC25793 carries
the figure images; both were downloaded and read directly, so the author was not
asked for a PDF that was already reachable.

**Figure 4 settles the stagger, in favour of the figure.** It prints every peptide
as a labelled row — `253-LKNVKSKIGSTENLK-267`, then 256, 259, 262 … up to
`340-KSEKLDFKDRVQSKI-354`. **15-mers at a 3-residue step: 30 peptides spanning
253-354.** Figure 4's "staggered by three residues" is right; Results (iii)'s
"overlaps of three residues" is the error. Both printed rows verify exactly
against P10636-8. **So 306-311 is a measurement at 3-residue resolution, not an
inference from a coarse grid — H4's control arm is sound and the critical path is
clear.**

*(The caption's "L253 … to D348" against a last row ending at 354 is **not** a
discrepancy: 348 is Asp, the region of interest ends there, and the final 15-mer
necessarily overruns. Recorded so it is not later mistaken for one.)*

**Figure 1 verifies the probe.** PHF43 = `[N265-E338 ΔR2]`: 74 residues minus R2's
31 = 43, matching the name, and residues 265-274 joined to 306-338 reconstruct
`NLKHQPGGGKVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVE` **byte-for-byte** against the
printed string.

### CORRECTION: I demoted PHF6* wrongly, and the full text says so

From the figures alone I concluded that PHF6* was named only by analogy, because
it sits in R2 and R2 is deleted from the PHF43 probe. **The full text, supplied
immediately afterwards, shows that is wrong.** Results (iii):

> "A **second maximum of interaction** was centered around Ile-278, covering the
> sequence 275VQIINK280 (PHF6*)."

and the Figure 4 caption: *"**Another cluster of strong interaction** occurs
around the spots that harbor the analogous sequence in R2."*

**PHF6\* has its own measured binding maximum.** My error was conflating the
probe with the membrane: the probe need not contain PHF6*, the **membrane** does,
and it spans 253-354 including all of R2. PHF43 binding a PHF6*-containing
peptide is a real heterotypic interaction — and the probe lacking R2 makes that
result *cleaner*, not weaker, since the signal cannot come from the probe's own
copy of the motif. **PHF6\* is restored to CLEAN.**

**The caveat that does survive is a different one, and it is real.** *Necessity
was demonstrated only for PHF6.* Every mutational experiment targets 306-311 —
the proline scan, K19ΔVQI, K19NAE, K19Y310E, and ΔVQI/NAE in full-length ht23.
PHF6* has a binding maximum and nothing else. So PHF6* enters as a clean row with
**sufficiency and necessity untested**, and **the H4 control arm stays n = 1** —
not because PHF6* is contaminated, but because it is detected inside the *same
single experiment* and carries no mutational validation.

### Two things the full text adds to the PHF6 row

**Necessity is strong, which is why this row can carry the control arm.** Proline
substitution inhibits aggregation at *every* residue of PHF6, while the outside
control G272P shows "no significant change". ΔVQI and NAE cause "a **complete
loss** of PHF formation" in full-length ht23 — necessity in an isolated construct
*and* in the intact protein.

**But the radiolabel sits inside the motif being mapped.** Methods: *"The purified
peptide PHF43 (50 μg) was **iodinated at Tyr-310**."* Tyr-310 is the fifth residue
of 306VQIVYK311 (verified against P10636-8). The probe therefore carries a bulky
iodine covalently attached inside its own PHF6 motif, and the assay then measures
that probe binding PHF6-containing peptides. The mutational work is independent
of the label and confirms the result, so this does not invalidate it — **but a
reviewer will spot it, and we should raise it rather than be shown it.**

**And the "no algorithm named anywhere" claim is now definitively dead.**
Discussion (v) cites **ref 30 = Street & Mayo 1999, *PNAS* 96:9074** for the
β-propensity argument. Still post hoc, so the row stays CLEAN — but note that
this sentence is itself a gatekeeper argument, *"β-sheet breakers such as P and
E"*, **published in 1999.** That is a fifth pre-emption of the compositional
strand, and the earliest.

### RATIFIED BY THE AUTHOR, 16 Nov 2026: the reframing is adopted

The recommendation below was put to the author and **accepted**. It is applied, not
pending. What changed in `PREREGISTRATION.md`, all as dated amendments rather than
silent edits:

- **H3 retired as a novelty claim** (§9.1). Gatekeeper composition becomes context with
  four citations. No sentence may imply it is new.
- **H4 promoted** (§2) and it is now the claim the project rests on: *a window-scanning
  predictor fails on a region containing a zipper-grade window it was built to detect,
  in a case structurally identical to one where it succeeds.*
- **Tau PHF6 306-311 is a REQUIRED control arm**, not an optional widening row. If it
  cannot be promoted, **H4 is withdrawn rather than reported without its control.**
- **The power calculation is stratified** (§7 amendment). The floor of 15 is restated as
  a floor on the *dataset*, not on the *test*; the primary statistic is computed on the
  **discordant stratum** and the concordant stratum becomes a pipeline positive control.
  If the discordant stratum cannot grow past n = 2, the quantitative claim is withdrawn
  and the project reports a case study plus a dataset — **pre-registered as an outcome,
  not a failure.**
- **`gatekeeper_density.py` rewritten at the top and the bottom** to say what the table
  is now for, and the tau PHF6 row flagged `[ROLE CONFLICT]`.

**The one thing deliberately left unresolved:** which role tau PHF6 keeps in which
table. It cannot be a deposited-crystal comparator and a validation control row in the
same comparison without putting the same hexapeptide on both sides. The script now
refuses to hide this; it does not decide it.

### Tau already is the gatekeeper paradox, in print since 2007, with its resolution [READ, 16 Nov 2026]

Mandelkow, von Bergen, Biernat & Mandelkow, *Brain Pathol* 2007;17:83-90, supplied
by the author. **It is a review, so by `CLAUDE.md` its numbers are checked against
UniProt and not trusted.** Every one of them holds against P10636-8 —
`306VQIVYK311` and `275VQIINK280` both exact, all four repeat boundaries exact
(R1 Q244-K274, R2 V275-S305, R3 V306-Q336, R4 V337-N368), and "only five types of
residues (G, K, P, S, T) make up half of the sequence" computes to **49.0%**.
**Zero discrepancies — the first paper in this entire sweep with none, and it is
the review.** That does not overturn the rule; one accurate review is not a
licence. It is recorded because the running tally would otherwise imply the
literature is uniformly sloppy, and it is not.

**The finding is not the numbers. It is that tau is our paradox, already solved.**

> "Tau is unusually rich in polar and charged amino acids... Only five types of
> residues (G, K, P, S, T) make up half of the sequence. This explains the high
> solubility and unfolded nature of the protein; **however, it renders its
> abnormal aggregation in Alzheimer's disease (AD) even more enigmatic.** In
> particular, at first glance, **the sequence contains no elements that are
> particularly amyloidogenic**"

Computed from P10636-8: **whole tau441 is 35.6% proline-plus-charge** (43 P,
44 K, 29 D, 27 E, 14 R) and it aggregates. That is the same shape as TRIOBP-1
324-348 at 48.0%, and the review calls it *enigmatic* — in 2007. **And it gives
the resolution:**

> "The puzzle was partially solved with the realization that the aggregation of
> tau is based on short hexapeptide motifs in the repeat domain"

PHF6 is **16.7%** gatekeeper against the repeat domain's 29.6% and the protein's
35.6%. **Globally gatekeeper-rich protein, locally zipper-grade hexapeptide,
aggregation driven by the local motif.** That is exactly the window-matched
control `scripts/gatekeeper_density.py` already computes — and it is the standard
tau story, twenty years old.

**This is the fourth and most direct pre-emption of the compositional strand**,
after Murray 2017 (composition does not discriminate), Seuma 2021 (gatekeeper
residues, measured) and our own n=1 problem. **The gatekeeper framing cannot be
the headline.** It is not merely pre-empted in general terms; the specific
paradox — gatekeeper-rich protein aggregating anyway — is the textbook tau case
with a textbook answer.

**The gatekeeper concept is also better supported than we need it to be**, which
is the same problem from the other side. Two FTDP-17 mutations that *delete a
gatekeeper residue* both *accelerate* aggregation: **ΔK280** removes a lysine,
**P301L** removes a proline, and both "strongly enhance the rate of PHF
aggregation by increasing the propensity for β-structure." That is the converse
of Giasson's A76E, where *adding* charge slowed assembly. Gatekeepers suppress,
graded, in both directions, measured, published. **Nothing is left to discover
there.**

### What survives is sharper than what it replaces

The distinction that tau does *not* pre-empt is about **prediction, not
composition**:

| | global gatekeeper | local hexapeptide | do the predictors find it? |
|---|---|---|---|
| tau | 35.6% | PHF6 16.7% | **YES** — *"the only two spots in the τ sequence where a β conformation is strongly predicted"* |
| TRIOBP-1 324-348 | 48.0% | contains a **0%** 6-mer | **NO** — missed |

**Same compositional architecture; opposite prediction outcome.** The claim worth
making is not "a gatekeeper-rich region aggregates" — tau, 2007 — but **"a
window-scanning predictor had a zipper-grade window to find and missed it, in a
case structurally identical to the one where it succeeds."** That is a
prediction-failure claim with tau as its built-in positive control, and
`gatekeeper_density.py`'s docstring already gropes toward it: *"a window-scanning
predictor had a 0%-gatekeeper hexapeptide to find inside TRIOBP-1 324-348 and
missed the region anyway."*

**Recommendation to the author, who decides it:** demote composition from
headline to context, promote the window-level prediction failure, and make tau
PHF6 a required comparator row rather than an optional one. This costs the
inversion, which was n=1 and getting lonelier, and buys a contrast with a control
arm. **It is a reframing, not a retreat — but it is the author's call, and it
should be made before the freeze.**

### The validation set is 14 rows, and the paper that pre-empted us handed back the best row [16 Nov 2026]

`data/regions.json` went from 10 to 14. Four promotions, all with the publisher
text read and the sequence verified against UniProt: **tau PHF6 306-311**, **tau
PHF6\* 275-280**, **α-syn 71-82**, **FUS 39-95**. Every row now carries a
`stratum` label, as the §7 amendment requires.

**The first three were all CONCORDANT — the dataset grew and the test did not.**
That is the pattern already recorded: the literature is enriched for regions the
predictors find. **So the audit was redirected to ask for *discordant* rows
specifically, and that worked immediately.**

**FUS 39-95 is DISCORDANT, documented in print, with the predictors named** —
*"Aggrescan, FISH, FoldAmyloid, MetAmyl, and PASTA 2.0 predict a low propensity
for amyloid formation across the FUS-LC"* — against a core determined by
solid-state NMR: *"residues 39-95 constitute the structurally ordered core."*
Verified independently: 39-95 is exactly 57 residues, matching the abstract's own
*"a segment of only 57 residues."*

### And the computation on it is better than the row

Computed from P35637: **FUS 39-95 is 3.5% proline-plus-charge, and all 52 of its
6-residue windows sit at or below the worst deposited zipper.**

| row | gatekeeper | windows zipper-grade | predictors |
|---|---|---|---|
| tau PHF6 306-311 | 16.7% | it *is* a zipper | **FOUND** |
| **FUS 39-95** | **3.5%** | **52 / 52** | **MISSED** |
| TRIOBP-1 324-348 | 48.0% | 7 / 20 | **MISSED** |

**This removes the compositional excuse entirely.** For TRIOBP-1 one can argue a
window-scanning predictor was not unreasonable to downweight a region that is 48%
gatekeeper. For FUS that defence is unavailable: there is nothing compositionally
unusual about the region at all, every window is zipper-grade, and five named
predictors still missed it.

**FUS 39-95 and tau PHF6 are the control pair H4 actually needed** — nearly the
same compositional profile, opposite prediction outcomes. That is a far tighter
contrast than tau versus TRIOBP-1, because it holds composition close to
constant. H4 was promoted on the weaker pairing; **this is the better test of
it.**

**Note what happened to Murray 2017.** It cost us the compositional headline
(§9.1) and then supplied the best test row in the set. The project's contribution
was never the composition observation; it is assembling the discordant set and
asking whether the PLM generation recovers it.

### The redirect is the transferable lesson

**The binding constraint is discordant rows, not clean rows.** Clean rows are
plentiful and mostly concordant. The cheapest source of discordant rows is
**papers that ran predictors post hoc and published the failure** — exactly how
FUS was found. Remaining sourcing effort should go there, not into widening the
clean set.

Discordant stratum now: **TRIOBP-1 324-348**, **FUS 39-95**, and **DISC1 384-415**
(provisional — Zaharija 2025 §4.3.5 ran five legacy predictors on DISC1, so the
assignment is recoverable from the literature rather than needing our own run;
**read it out before the freeze, do not assume it**).

### DISC1 384-415 resolves to DISCORDANT — and ANuPP is prior art on H1 [16 Nov 2026]

Resolved from the literature, no run of ours needed. Zaharija 2025 §4.3.5 ran five
predictors on full-length DISC1; **four of five gave hotspots "dispersed
throughout the entirety of the protein sequence"** and did not single out the
linker. Those four include **every tool in the frozen legacy arm** — TANGO,
AGGRESCAN, FoldAmyloid. So against §5.1 the row is unambiguously **DISCORDANT**.
The discordant stratum is now **three**: TRIOBP-1 324-348, FUS 39-95, DISC1
384-415.

**A frame task closed on the way.** The thesis used RefSeq **NP_061132.2**, not
UniProt Q9NRI5, and the register had flagged *"VERIFY THE FRAMES MATCH."* **They
are byte-identical — both 854 aa, sequences equal on direct comparison.** The
thesis's numbers transfer with no offset.

### But one of the five found it, and that is the uncomfortable part

**ANuPP (2021) named AA 387-395 and AA 400-415 as highest nucleation capacity.
Verified: both lie entirely inside 384-415** — a precise hit, not a vague
overlap.

ANuPP is not in the frozen legacy arm, so it does not muddy the stratum. **It
does something more awkward.** `CLAUDE.md`'s headline question is whether *modern*
predictors recover what the 2004-2010 generation missed. **For DISC1 a partial
answer is already in print, and it is yes** — published by the group that mapped
the region.

This is **not** a pre-emption of §5.2, which claims only that no **PLM** has been
run on DISC1 or TRIOBP-1; ANuPP is not a PLM and that claim survives. But the
project can no longer present *"a newer tool finds what the old ones missed"* as
its own discovery for DISC1. **Cite it as the starting point and position against
it.**

**Three questions it leaves open, and they are better than the one it closes:**

1. Does the **PLM** generation recover it? Nobody has tested this.
2. **Does ANuPP's success generalise?** It has **never been run on TRIOBP-1** —
   the thesis contains no TRIOBP-1 predictor runs at all — nor on FUS 39-95. One
   hit on one protein is not a trend.
3. **ANuPP currently has no home in the pre-registration.** §5.1 freezes the
   legacy arm without it; §5.2 freezes the modern arm as AggreProt and
   AggrescanAI. A 2021 tool that has already succeeded on one of our rows belongs
   explicitly in one arm or a named third category.

**That third point needs the author, and it carries a conflict of interest worth
naming out loud:** ANuPP succeeding is inconvenient for a project about predictor
failure. **Whichever way it is placed, say so in print.**

### The floor of 15 is reached, and the discordant stratum doubled [16 Nov 2026]

`data/regions.json` is **15 rows** — the floor named in `CLAUDE.md`. **But read
the §7 amendment before celebrating: 15 is a floor on the *dataset*, not on the
*test*.** The breakdown is **4 discordant, 3 concordant, 8 pending.**

**hnRNPA1 251-295** is the fourth discordant row and the strongest-worded yet.
Cryo-EM core from full-length protein (*"The fibril core is formed by 45 residues
(Gly251 to Tyr295)"*), and the predictor comparison **names the entire frozen
legacy arm as failing**:

> "Five out of seven tested methods (Aggrescan, FoldAmyloid, Pasta 2.0, TANGO 2.2
> and Amylpred 2)" … "lacked any hit within the fibril cross-β structure"

**The numbering trap was handled by lookup, not arithmetic.** This file's own
`_frame_traps_are_worse_than_assumed` warns that hnRNPA1's frames differ by an
*internal* alternative exon. P09651-1 is 372 aa, P09651-2 is 320 aa, the paper
uses 320. Searching the exact 45-mer in the 372-frame puts it at **303-347**, so
the +52 constant offset *happens* to be right here — because this core sits
C-terminal to the insert. **Verified, not assumed**, and it would not hold for a
range spanning the exon.

### The sourcing lesson, now with numbers

Searching for **clean** rows added three rows and **zero** test power — all three
concordant. Searching for **published post-hoc predictor failures** added **two
discordant rows in one afternoon**, both with the tools named in print, needing
no run of ours. **The binding constraint is discordant rows.**

### And a pattern the write-up must not hide

**In every discordant case where a paper ran several tools, at least one tool
succeeded.** On DISC1, ANuPP hit 387-395 and 400-415 precisely. On hnRNPA1, WALTZ
scored four true positives in the core (ZipperDB also hit, but alongside 85 false
positives). Murray's own phrasing for FUS is the same shape — the hitting tools
showed *"no consensus on the identities of these segments."*

**So the honest claim is not "the predictors fail."** It is *"the widely used
2004-2010 generation fails, while scattered other tools succeed sporadically and
without consensus."* A report that mentions only the failures would be selective
and would not survive review. **It also sharpens the real question:** not whether
prediction is possible, but whether any tool succeeds **reliably across rows**
rather than luckily on one — which is exactly what a stratified benchmark over
four discordant rows can answer and a case study cannot.

### I withdrew an inconsistency the same day I logged it [16 Nov 2026]

I recorded Sharma 2023's sentence — *"In all cases, it was found that the
predictions of the highly amyloidogenic regions **did match well** the
experimentally verified β-sheet structure [27-29]"* — as a dropped negation,
reasoning that it is introduced as *"Related conclusions"* to a statement of
predictor failure, so it must mean *did **not** match well*.

**I inferred that from context without opening the cited papers.** That is the
move `CLAUDE.md` rule 1 exists to forbid, and I made it while logging other
people's numbering errors.

A search of ref 28 (Liberta 2019, AA amyloidosis) reports — at **snippet** level
— that the N-terminal ~21 residues, *the most amyloidogenic stretch*, **are** the
fibril core. If that holds, the sentence is **literally true** for that
reference, and *"Related conclusions"* means *related comparisons were made*,
not *the same conclusion was reached*.

**Corrected status: the sentence is ambiguous, not demonstrably wrong.** It is
**removed from the tally**, which goes back to **thirteen**. The operational
instruction was right either way and stands: **the direction of refs 27-29 must
be read out of each primary and must not be taken from that sentence in either
reading.**

**And the lead itself may point the other way.** Liberta 2019 looks like it may
be **CONCORDANT**, not discordant — which would still be worth having, since it
is *ex vivo* human and mouse material and the concordant stratum is the pipeline
positive control. But that is snippet-grade, and our own premise audit records
that snippet assessment is biased. **Nothing moves until a primary is opened.**

### Liberta 2019 read in full: both my readings were wrong, and the truth is simpler [16 Nov 2026]

I guessed twice about this paper and was wrong twice. **It runs no aggregation
predictor at all.** The software in its Methods is structural and imaging only —
IMOD, MOTIONCOR2, Gctf, RELION, Coot, PHENIX, Molprobity, EMRinger, DSSP,
STRIDE, Chimera, PDBePISA, Fiji, FREALIGN. ZipperDB, TANGO, AGGRESCAN,
FoldAmyloid, PASTA, WALTZ, AmylPred and Zyggregator are **absent**.

So it is **neither concordant nor discordant**, and my snippet-based guess that
it might be concordant was meaningless. The phrase I had been reading is *"the
N-terminal ~21 residues … **the most hydrophobic and amyloidogenic segment** of
the protein sequence"* — and the three references attached to it are
**experimental** (CD spectroscopy of murine SAA; *"The N-terminal segment of
protein AA determines its fibrillogenic property"*; a C-terminal truncation
study). **"Amyloidogenic" there means experimentally amyloidogenic.**

**Two lessons, and the first is the one that generalises.**

1. **"Amyloidogenic" in this literature is ambiguous between *measured* and
   *predicted*, and that distinction is the entire basis of the `stratum`
   column.** Read the citation, never the adjective.
2. **Both of my readings of the Sharma sentence were wrong.** It is not a dropped
   negation, *and* it is not supported as written — because the paper it cites
   contains no predictions to match or mismatch. **The citation is simply loose.**

**New sweep rule, recorded in `regions.json`:** before assigning a stratum from a
paper, check that the paper *ran a predictor*. Two of Sharma's three leads appear
not to. A cryo-EM structure paper is a source of CLEAN rows by default and of
STRATUM assignments only when it happens to include a post-hoc comparison —
the exception, not the rule.

### The row itself is the best evidence class in the set

`regions.json` is **16 rows**. hSAA1.1 **2-55** enters CLEAN, stratum PENDING —
and it is the only row that is **not recombinant**: fibrils extracted from the
kidney of a deceased AA amyloidosis patient, cryo-EM at 2.7 Å, >98% one
morphology, the deposited protein itself a natural proteolytic fragment.

**An allelic trap, and it bites inside the region.** The mature chain of UniProt
P0DJI8 differs from the hSAA1.1 sequence printed in Figure 4a at residues **52,
57 and 59** — the known SAA1.1/1.3/1.5 allelic sites — and **residue 52 falls
inside the ordered core 2-55.** Pulling this sequence from the canonical UniProt
entry would silently give the wrong residue. **Always name the allele.** This is
a new member of the frame-trap family: not an isoform, not an offset, an
**allele**.

**And it speaks to the retired H3 better than anything we could have produced.**
The core is **27.8%** proline-plus-charge — higher than DISC1 384-415, far above
every deposited zipper — *in ex vivo human disease material*. The paper shows
charge is not merely tolerated but structural: *"the mutual charge compensation
of six buried ionic residues … that form a network of salt bridges"*, with six
more in the human fibril defining a water-filled cavity. **Gatekeeper residues
are not excluded from amyloid cores; they sit buried and charge-compensated in
real disease fibrils.** Cite it.

### The LECT2 branch: one row, one exclusion, and a snippet that would have lied [16 Nov 2026]

**The new sweep rule earned its keep immediately.** The search summary for LECT2
said the core *"has not been predicted by previous work."* Read in full, the
sentence continues: *"**and the newly identified core segment is predicted to
form steric zipper structures by the amyloid-prediction algorithm in ZipperDB**."*

Prior *literature* missed it; **ZipperDB, run post hoc, hits it.** Quoting only
the first half — which is what the snippet gave me — would have produced a **false
DISCORDANT assignment**. Only ZipperDB is run, so our frozen legacy arm is
untested and the row is **PENDING**.

**LECT2 55-75 enters CLEAN**, verified two ways (UniProt O14960 mature 55-75 =
`MIVGQEKPYQNKNAINNGVRI`, matching Figure 2A byte-for-byte; Met55/Ile75 and the
21-residue length both check), with the register independently confirmed by a
Rosetta threading search over *all* 21-residue windows.

**But it carries the sharpest construct conflict in the set.** The companion
*ex vivo* structure from a patient kidney reports that **all 133 residues** are
in the fibril. **21 residues versus 133, for the same protein.** The recombinant
authors flagged the risk themselves — *"It remains to be seen whether recombinant
LECT2 amyloid fibrils exactly match those present in the kidneys"* — and they
apparently do not. This row must never be called the ALECT2 disease core.

### And the ex vivo structure is excluded, with a reason worth generalising

**A whole-protein core cannot test a window predictor.** If the ordered core is
the entire sequence, every window is in the positive class, **specificity is
undefined**, and every predictor scores identically well by construction. The
ALECT2 paper shows the problem in its own analysis: it ran WALTZ, TANGO,
Aggrescan and AmylPred, but with the core spanning everything, its overlap claim
cannot be a per-tool test.

**Registered as a general exclusion rule:** any fibril whose ordered core is the
whole protein is uninformative for this benchmark and is excluded *with that
reason stated*. That is `CLAUDE.md` rule 3 — the proposed comparison is
impossible, and saying so is the finding.

**Best remaining lead from this branch:** Tsiolaki 2019 (*J Struct Biol*
207:260), described here as having *"identified the regions immediately preceding
and following"* the true core. A prediction-driven paper that **bracketed the
core without hitting it** is exactly the shape of a documented discordant
assignment.

### I called the Tsiolaki lead wrong — and the error was in the shape, not a fact [16 Nov 2026]

I flagged Tsiolaki 2019 as *"the best remaining discordant lead"* because it had
**bracketed the true LECT2 core without hitting it.** The observation was right.
**The inference was wrong.**

Methods: *"Aggregation-prone hot-spots … were identified with the aid of
AMYLPRED"*, and *"**Peptide design was based on the predicted** aggregation-prone
core of LECT2."* **Every tested peptide was nominated by an algorithm.** This is
a **CIRCULAR** paper in the same class as Mizuguchi 2019 apoA-I — not a
documented discordant assignment.

**The distinction worth keeping: a paper that *used* predictors and a paper that
*tested* predictors are different things, and only the second yields a stratum
assignment.** A prediction-driven paper that misses is circular with wrong
predictions; the discordance only becomes visible when someone compares it with
the later structure, and nobody published that comparison.

### But computing that comparison myself gives a real result

AMYLPRED2 — an 11-method consensus, **run before any structure existed** —
nominated **38-58** and **73-88**. The cryo-EM core is **55-75**.

| | |
|---|---|
| core residues predicted | **7 of 21** — and they are the two *ends*, 55-58 and 73-75 |
| core residues missed | **14** — the entire centre, 59-72 (`QEKPYQNKNAINNG`) |

**And the missed stretch is the structurally important one.** Richards 2023 names
what holds the core together: polar ladders **Q59, N65, N67, N71**, the central
**I69** that *"anchors the very center of the fibril core"*, and the **G58/G72**
pair. Of those, **Q59, N65, N67, I69, N71 and G72 are all in the missed
stretch.** The predictor found the hydrophobic flanks and missed the polar
machinery entirely.

### Registered honestly as a weaker class: `DISCORDANT_DERIVED`

**This assignment is mine, not the literature's**, and that is a real difference
from FUS 39-95 and hnRNPA1 251-295, where the source paper itself ran the tools
and reported the failure. Tsiolaki 2019 claims *success* and never saw the
structure. Two further limits: AMYLPRED2 is a **consensus**, so there is no
per-tool result for the frozen legacy arm; and **ZipperDB does hit the core**, so
this is again a row where some tools succeed.

So it gets its own stratum value and **is not pooled into the primary statistic
unless the author ratifies it** — added to the §12.1 open-decisions list.

**Count: four documented discordant rows, one derived.** The sweep chased six
leads today and found exactly two papers that ran predictors post hoc and
published the failure. **The supply of documented discordant rows is thin, and
that is now a measured statement rather than an impression.**

### All five open decisions settled [16 Nov 2026]

Settled **before the freeze and before any predictor has run**, which is the only
ordering under which settling them is worth anything. Full text in
`PREREGISTRATION.md` §12.1.

**1. The three delegated decisions: RATIFIED** (§3.1 Stouffer primary / Fisher
secondary; §5.1 the FoldAmyloid reimplementation must pass Garbuzynskiy's own
checks or be excluded-but-reported; §5.2 version-pinnable-and-local for the
modern arm). Each is written out in §12.1 so ratification means something rather
than being a rubber stamp. **§12 step 3 is discharged.**

**2. ANuPP → a named third category, "intermediate generation (exploratory)."**
Not legacy (2021, and §5.1 is a frozen 2004-2010 baseline); not confirmatory
modern (**it is a web server and fails §5.2's rule** — the same rule that already
excluded eleven-plus PLM-era tools). **Bending that rule for ANuPP specifically
would be bending it for the one tool whose published result is inconvenient.**
Reported separately, out of the multiplicity correction, with Zaharija 2025 cited
as prior art. **Registered secondary analysis:** run ANuPP on TRIOBP-1 324-348,
FUS 39-95 and hnRNPA1 251-295 — it has never been run on any of them, and that is
the question it actually raises.

**3. The publisher-PDF gate: kept strict, made precise** — and the problem was
wider than FUS. One day's reading used a version of record, an NIHMS author
manuscript, an accepted manuscript and a **bioRxiv preprint**, and recorded all
four identically. Every row now carries **`source_version`**; author manuscripts
are citable with the version named, `pmc_full_text` and `preprint` are not.
**Two freeze blockers fall out: Murray 2017 *Cell* (FUS 39-95 is a
primary-stratum row and currently uncitable) and the published LECT2 paper.** A
rule is not weakened to accommodate a row when the row can be obtained.

**4. tau PHF6 — and ratifying §5.1 surfaced a THIRD role.** Beyond the crystal
comparator and the H4 control row, **PHF6 is the validation target for the
FoldAmyloid reimplementation** (*"only the contact scale finds tau 306-311"*).
Resolution: the **comparator is dropped** — PHF6 removed from `ZIPPERS`, and *the
headline band is unchanged at 0.0–16.7% because SOD1 30-35 is also 16.7%*, only
n falls 7→6. The FoldAmyloid check is kept (it is Garbuzynskiy's, not ours to
move). The control row is kept **with a pre-registered per-tool exclusion:
FoldAmyloid's score on PHF6 is not counted**, because a tool validated on a row
cannot then be tested on it.

**5. `DISCORDANT_DERIVED` is a separate stratum, not pooled.** Choosing which two
papers to compare is exactly the researcher degree of freedom pre-registration
exists to remove, and the four documented rows carry no such freedom. Reported
with the derivation shown; **if primary and derived disagree, that is reported,
not reconciled.**

**Remaining freeze blockers: the two PDFs, the ten `UNRECORDED` source versions,
then steps 4–5 (predictor versions, freeze commit).** No predictor may run until
then.

### Murray 2017 version of record: blocker cleared, and it hands over two things [READ, 16 Nov 2026]

The *Cell* PDF settles freeze blocker 15. **FUS 39-95 is now `version_of_record` and
citable** — which mattered, because it is a primary-stratum row that our own gate
had made uncitable. Every claim recorded on the row was re-checked against the
PDF and **all of them hold**, including the 57-residue arithmetic and the
predictor sentence.

**Our gatekeeper computation is independently confirmed by the paper's prose.**
We computed 3.5% for 39-95: one proline, one charge in 57. The Discussion says,
without having seen our arithmetic: *"The sidechain of D46, **the only charged
residue** in the core-forming segment"* and *"The absence of purely hydrophobic
sidechains (**except Pro72**)."* 2/57 = 3.5%. That is as good a check as this
project gets.

### The published predictor run is fully parameterised — a second §5.1 check

Murray 2017 publishes **every setting** for all eight tools on FUS-LC 2-214,
including **FoldAmyloid at `bioinfo.protres.ru/fold-amyloid`, scale "Expected
number of contacts 8 Å", averaging frame 5, threshold 21.4.** (That also settles
the host question: `bioinfo` is the URL published in *Cell*, not a mistake —
though both hosts return 000 today.)

**Figure S7's FoldAmyloid panel never crosses threshold anywhere across 213
positions.** So the published result is not "low propensity" — it is **zero
positive predictions on the entire sequence.** Registered in §5.1 as a *second*
validation target for the reimplementation, and a sharper one than a
sensitivity/specificity number because it is a whole-curve comparison on a named
sequence that is also one of our rows.

### And a mechanism that changes how a miss must be scored — new §5.2a

From the Figure S7 legend, which was **not** in the PMC text I read first:

> "For ZipperDB … **dotted red lines span segments where proline residues
> preclude a prediction.**"

**ZipperDB structurally cannot evaluate a proline-containing window.** It returns
nothing, not a low value. **TRIOBP-1 324-348 has four prolines in 25 residues**,
so a tool behaving this way has blind spots across our headline region *by
construction*.

**A predictor that cannot score the windows in question is not making a wrong
prediction; it is making no prediction.** Registered in a new §5.2a before any
run: every tool is checked for no-call behaviour first; a no-call is never
silently midranked but **excluded from both M and m**, with the count reported;
and a tool that cannot score most of a region's windows is reported
**INAPPLICABLE to that row, not failed on it.** Scoring a tool as having missed a
region it could never evaluate would be the mirror image of the circularity this
project exists to avoid.

### CORRECTION: `PMC9934627` IS the preprint, and my obtain-list request was wrong [16 Nov 2026]

I wrote that the supplied document "is not PMC9934627". **It is.** `PMC9934627`
is the bioRxiv preprint *hosted in PMC* under the NIH preprint pilot, carrying an
explicit *"This is a preprint. It has not yet been peer reviewed by a journal."*
banner. **Obtain-list item 16 asked for "the published version, PMC9934627" —
there is no such thing.** I had assumed a PMC identifier implied a published
version. The author supplied exactly what I asked for and I misdescribed it.

**The peer-reviewed version is a different record entirely:** *Structure*
31(11):1386-1393.e3, doi `10.1016/j.str.2023.08.007`, PMID 37657439,
**`PMC11456264`** (NIHMS author manuscript). Obtained and read.

**BLOCKER CLEARED.** The row is now `author_manuscript` and citable.

**The range survived peer review**, which was the whole point of checking: the
published version states **55-75 five times** — Summary, Introduction, Results
twice, Discussion. The disulfide argument and the *ex vivo* caveat both survive.
One wording change: the preprint says the fibrils may not *"exactly match"*
patient material, the published version drops *"exactly"*. Trivial in substance,
recorded because it is a concrete instance of why §12.1 requires naming the
version — **we quote that sentence.**

**Standing rule added to the obtain list: a PMC id is not evidence of
publication.** Name the journal and DOI, and check the PMC record for a preprint
banner before treating it as the version of record.

### What the preprint read still gave us

**Two things from reading it in full anyway.**

**ZipperDB hitting the core is worth much less than I recorded.** Figure S1A's
criterion is segments scoring **< −23.0 kcal/mol**, and the panel shows them
scattered across the whole 133-residue sequence — the Discussion concedes *"a
significant fraction of the LECT2 sequence is predicted to be amyloidogenic."*
**A tool that predicts most of a protein cannot be credited with predicting the
part that mattered.** Same failure mode hnRNPA1 quantified at 85 false positives.

**Fourteenth inconsistency**, in the table a referee would use to judge the
model: Supplementary Table 1 prints *Ramachandran favoured 5.26%* with *outliers
0%*. With 21 residues modelled, 19 have φ/ψ, and 18/19 = 94.74%, 1/19 = 5.26% —
**the labels are swapped**, since favoured 5.26% with zero outliers is
arithmetically impossible.

### A candidate answer to the second half of `CLAUDE.md`'s question — and it is a HYPOTHESIS

The headline question asks what structural feature the predictors *are all
missing*. **That half has had no candidate since the compositional answer was
retired on 16 Nov.** Here is one, and it comes from the papers rather than from
us:

> **Native structural context decides which predicted APRs can actually engage,
> and a sequence-only predictor cannot see it.**

**LECT2**, unprompted: *"much of the protein's globular fold is stabilized by
three disulfide bonds … **these bonds would likely prevent many of the predicted
amyloidogenic regions from assembling into fibrils.** However, the core segment
identified here is **not involved in any of the native disulfide bonds**."* The
core is not the best-predicted segment — it is the predicted segment that is
structurally **free**.

**hnRNPA1**, the same thing from the other side: the predictors *"consistently
identify segments within the two RRMs"* — inside **folded domains** — while the
core forms in the LCD.

**Why it is worth more than the compositional claim:** it is **not pre-empted**
by Murray, Seuma or Mandelkow, none of whom address sequestration; it is
*mechanistic* rather than descriptive; and it explains the **false-positive**
pattern, not just the miss.

**And the honest difficulty, stated now rather than after work is spent:** the
test needs a native structure or confident burial annotation per row. LECT2 has
PDB 5B0H and published per-residue solvent accessibility; hnRNPA1 has defined
RRMs; **FUS-LC is wholly disordered so the hypothesis makes no prediction
there**; and **DISC1 and TRIOBP-1 have no experimental structure at all.** **It
cannot be tested on the two rows this project exists for.**

**It must not become the new spine.** The gatekeeper claim became one on n = 1
and was retired four days later. This is a hypothesis drawn from two Discussion
sections with no measurement behind it. If it enters `PREREGISTRATION.md` it
enters as a pre-specified **secondary** analysis with its own falsification
condition — and only if the author decides it earns the space.

### The LECT2 version of record, read — and the preprint is better evidence [16 Nov 2026]

The NIHMS manuscript (`nihms-1928634.pdf`, the accepted *Structure* version) is
now read in full. **Both versions have been read**, which is what makes the
comparison below possible. Everything recorded from the web read holds.

**The frame is now pinned to a named accession**, which the preprint never gave:
the Key Resources table specifies *"residues 19-151 of the human LECT2 protein
(GenBank AAC17734.1)"*. Verified: 151 − 19 + 1 = **133**, matching the mature
chain and the paper's own *"21 of the 133 residues"*.

### §12.1's version rule just paid off, and it cut the unexpected way

I assumed the version of record would be the better evidence. **Here it is
worse.** The Introduction sentence about prior work:

> **Preprint:** "Amyloidogenic segments of LECT2 have been identified, and
> **predicted** amyloid-forming LECT2 peptides assemble into amyloid-like fibrils
> in isolation."
>
> **Published:** "Amyloidogenic segments of LECT2 have been identified **and
> assemble into** amyloid-forming LECT2 peptides **assemble into** amyloid-like
> fibrils in isolation."

Copyediting **garbled the verb and dropped the word "predicted"** — and that word
is precisely what flags reference 20 (Tsiolaki 2019) as **circular**. It is the
authors' own acknowledgement that the peptides tested there were chosen by an
algorithm.

**So: cite the published version per §12.1, but quote the preprint for that
sentence, naming the version each quotation comes from.** The assumption that the
version of record is always the better source is false here, and this is a
concrete counter-example rather than a hypothetical one.

**And the Ramachandran error survived peer review.** Table 1 of the published
version prints the same impossible figures — *favoured 5.26%* with *outliers 0%*
— so it is not a preprint artefact. It passed review at *Structure* and was
copyedited around. Tally **15**.

**Two more things from the published version**, recorded so the two are not
treated as interchangeable in either direction. The fibrils were grown in *"a
modified version of the fibrillization buffer used by Tsiolaki et al."* — the
growth conditions are inherited from the circular paper. **That does not make the
structure circular** (the core came from the density and from Rosetta threading
over all 21-residue windows, neither of which depends on buffer), but a reviewer
tracing provenance will land on Tsiolaki and we should say it first. And the
published version **adds** AFM confirming the left-handed twist (Figure S11) and
a domain-swapping model through loop 2 (Figure S10) — neither affects the core
range.

### The ten `UNRECORDED` rows are resolved — and the headline row's primary was never opened [16 Nov 2026]

By lookup, as the rule requires: each row's `verified_against` field read, then
each named source checked against the register for an entry recording that
anyone opened it. Full table in `PREREGISTRATION.md` §12.2. **Three**
`version_of_record`, **six** `source_not_opened`, **one** `preprint`.

**A fifth schema value was needed, and that is the finding.** My original four
values all presumed the source *had* been read in some version. **Six rows do not
satisfy that presumption.** Neither **Bradshaw 2017** nor **Cukkemane 2021** has a
register entry — Bradshaw appears only as a citation *inside* papers that were
read, Cukkemane only as a `claim_as_cited` in an entries list. All six already
carried `verified_against_publisher_pdf: false`, so nothing changes status; what
changes is that the reason is now written down.

**And a detail worth saying out loud: `TRIOBP-1 324-348` names Bradshaw 2017 as
its `source`, and Bradshaw 2017 has never been opened.** The row is real and
well-supported — but by **Zaharija 2022**, read in full, which is where the
sequence, the range and the figure all come from. **The project's headline row
rests on a restatement, not on the paper its source field names.** That is fine
provided we say so; it is not fine if a reader assumes the 2017 primary was
checked. Noted on all three Zaharija-backed rows.

### The one that is a freeze blocker

**`DISC1 384-415` is `preprint`, and it is a primary-stratum DISCORDANT row** —
one of the two the project was founded on. Its range rests on the **bioRxiv
preprint plus the 2025 thesis**. The version of record — Zaharija & Bradshaw
(2024) *Prog Neuropsychopharmacol Biol Psychiatry* 130:110923 — **has not been
obtained**; the register records *"FULL TEXT NOT OBTAINED — Elsevier/Ovid
paywall."*

**Under §12.1 decision 3 a preprint is not citable. So the primary analysis
would currently be computed on a stratum one of whose four members cannot be
printed** — exactly the position FUS 39-95 was in this morning before the *Cell*
PDF arrived.

This does not add a blocker; it **sharpens the one already in §12 step 1**, which
framed that paper as a re-check of Δ384-414 vs Δ384-415. It is now also the
difference between the row being citable and not.

**Flag conflict, and the rule.** That row carries
`verified_against_publisher_pdf: true` — defensible for what was opened, since
bioRxiv serves a real PDF, but misleading under §12.1. **Where the boolean and
`source_version` disagree, `source_version` governs.**

### Cukkemane 2021 read: four rows closed, and a caution we wrote blind is confirmed [16 Nov 2026]

The *Translational Psychiatry* PDF closes **four** `source_not_opened` rows at
once — DISC1 691-836, 716-761, 717-737/739-761 and 748-769 all name this paper,
and none of us had opened it. Springer Nature, open access CC BY, so the PDF **is**
the version of record. Only **two** `source_not_opened` rows remain, both
Bradshaw 2017.

**The best outcome is that our own blind caution turns out to be exactly right.**
`regions.json` already carried, in capitals, *"THIS IS A DOCKING RESTRAINT, NOT A
MEASUREMENT"* on the 716-761 row — written without having read the paper. The
paper confirms it almost word for word:

> "The proposed β-structure was **introduced into the model** using MODELLER 9.23
> **after adding restraints** defining antiparallel β-strands in segments 716-737
> and 739-761"

The β-strands were **imposed and then docked**, not observed. The ssNMR evidence
is chemical shifts *"reminiscent of residues in β-strands"* for Ala, Gly, Leu,
Pro, Ser, Thr and Val — composition-level, not site-resolved — and the authors
concede *"the ultimate proof is still lacking."* **The circularity is confirmed at
source too:** *"A manual search … using the program RADAR identified one such long
tandem motif."*

### The predictor negative is real but weaker than it reads

`STATE.md` carried this second-hand as one of "two published predictor negatives
worth citing". Verbatim at source:

> "these programs were all unsuccessful in determining the β-core interface of
> DISC1"

**But no tools are named.** No list, no settings, no figure, no supplementary
panel. Compare Murray 2017, which names five and publishes every parameter, or
Sharma 2023, which names seven and quantifies 85 false positives. **This is an
assertion, not a result, and it cannot assign DISCORDANT to anything under
§5.1.** Cite it as corroborating context only.

And the paper's own narrative undercuts it: sequence tools failed, a *different*
sequence tool (RADAR) succeeded, and the region it found is the **CIRCULAR**
716-761 row. That is not a predictor benchmark; it is the circularity this
project exists to label.

**Two new inconsistencies**, tally **17**: the C-region is called *"160 amino acid
residues"* when 691-836 is **146** (the 19.4 kDa tagged mass fits 146); and the
β-core starts at **716** in the abstract and Methods but **717** in the Discussion
where the RADAR output is reported.

**One thing for the obtain list.** The ThT item says the claim "rests on Korth
2012 alone" — that is the *negative* half. Cukkemane 2021 sources the **positive**
half to neither Leliveld nor Korth but to **Tanaka 2017** (*J Clin Invest*
127:1438), and it **runs its own ThT assay** on the C-region (Fig 3C), positive,
plateau after 8 h at 37 °C. Also worth keeping: *"DISC1 amyloid has not been
reported either in human post-mortem brains or in animal models."*

### The 2017 citation is pinned, and its title is our premise [16 Nov 2026]

Bradshaw & Korth 2018 (*Mol Psychiatry* 24:936) is a **Perspective, not a
primary**, so by `CLAUDE.md` nothing in it promotes a row. Its two arithmetic
claims were checked anyway and both hold — TRIOBP-1 324-348 is 25 residues
("just 25 amino acids"), NPAS3 211-331 is 121 ("a 121-amino acid-long central
region").

**What it is actually for: reference 110 pins the citation of the only
never-opened primary left.**

> Bradshaw NJ, Yerabham ASK, Marreiros R, Zhang T, Nagel-Steger L, Korth C
> (2017). **"An *unpredicted* aggregation-critical region** of the
> actin-polymerizing protein TRIOBP-1/Tara, determined by elucidation of its
> domain structure." *J Biol Chem* **292:9583-9598**.

Until now the project recorded it only as "Bradshaw et al. 2017", with no volume
or page anywhere. **And note the title: the word *unpredicted* is in it.** The
predictor-failure premise this whole project treats as cited evidence is the
title of the paper nobody here has opened.

The review corroborates our row at review grade — Table 2 gives "324-348 [110]"
and the text calls it "a loop between two predicted coiled coils" — but
corroboration is not substitution.

### The thioflavin T trail is corrected a second time

The obtain list says the ThT claim "now rests on **Korth 2012** alone." This
review points somewhere else entirely:

> "aggregates of DISC1 … have been tested with dyes associated with classic
> amyloid-based aggregation (thioflavin T and thioflavin S), yielding
> **potentially contradictory results in different expression systems** [62, 82]"

Reference 62 is **Tanaka 2017** (*J Clin Invest* 127:1438) and 82 is **Trossbach
2016** (*Mol Psychiatry* 21:1561). **Korth 2012 is reference 9 here and is cited
for "DISC1opathies", not for ThT.** That is the **second independent pointer away
from Korth 2012** — Cukkemane 2021 also sourced the ThT-positive claim to Tanaka
2017. **The honest statement is that the ThT evidence is contradictory between
expression systems and traces to Tanaka 2017 and Trossbach 2016.**

### Two review-grade leads, neither promoted

**NPAS3 211-331** (Nucifora 2016) is a possible row — NPAS3 is on the project's
psychiatric list — but 121 residues is a domain, not a motif, and the primary is
unopened. **CRMP1 "1-127"** must **never** become a row: the table's own asterisk
reads *"Implied as only region unique to the long variant"* — an inference from
isoform difference, not a mapping. A good reminder that the footnote matters as
much as the table.

### The last never-opened primary is closed, and it upgrades the headline row [READ, 16 Nov 2026]

Bradshaw et al. 2017, *J Biol Chem* 292:9583-9598, CC BY. **Zero rows now carry
`source_not_opened`.** Every primary named by every row has been opened.

**The sequence is confirmed a third independent way.** Figure 12B prints the
25-mer under a 324/330/340/348 scale: `PLRENKRVPLTALLNQSRGERRGPP` —
byte-for-byte what the row already held, which came first from reconstruction and
then from Zaharija 2022's Figure 1B.

### The stratum assignment is now the strongest in the set

The Discussion names **all four tools**, and they **are** the frozen legacy arm of
§5.1:

> "this portion of TRIOBP-1 was one of the **less strongly predicted** to contain
> an 'aggregation motif,' with only the sequence around aa 230-236 predicted to
> have some aggregate-forming propensity by the **AGGRESCAN**, **FoldAmyloid**,
> and **ProA** servers. **It was not predicted as such by TANGO.** In all
> instances, however, **at least four sites elsewhere in the protein were more
> strongly predicted**"

**230-236 is outside 324-348.** Three tools put a weak signal *near but not on*
the region, TANGO put none there, and all four ranked at least four other sites
higher. **Stronger than FUS 39-95 or hnRNPA1 251-295, because the named tools are
not merely comparable to our arm — they are our arm.**

**One more link to follow:** the runs are "In our **previous** analyses (8)" —
Bradshaw 2014, *PLoS ONE* 9:e111196, open access. Cite 2017 for the region, but
open 2014 for the predictor settings.

### The gatekeeper observation is theirs, and they offer a different mechanism

**This is the fifth pre-emption of the compositional strand and by far the most
direct, because it is on our own headline region:**

> "The 25-aa region **contains multiple proline residues** (Fig. 12B), suggesting
> that it likely represents a **turn** between CC1 and CC2. It is also **rich in
> charged amino acids**, allowing for the possibility that TRIOBP-1 aggregation
> is dependent on **protein-protein interactions**."

Figure 12B colours the prolines purple and the charges red and blue — the two
residue classes this project counts. **Computed from their printed sequence:
4 + 8 = 12/25 = 48.0%**, reproducing our headline figure from the source. H3 was
already retired for other reasons; this shows it was **less novel than the
retirement assumed.**

**And they propose a mechanism we did not, which is a live alternative to H4:**

> "That this region was **not strongly predicted** to have an innate aggregation
> propensity might further implicate the **involvement of additional proteins or
> other cellular factors**"

Their reading is that the region matters because **other proteins bind there**,
not because of its own propensity. **That must be stated alongside H4, not
omitted.**

### Two rows corrected against the primary

**324-328 is an over-attribution.** Bradshaw 2017 makes *no* claim about it. Its
constructs are 324-652 vs 349-652; Figure 12A lists 323/324 and 348/349 as
**construct borders**. Zaharija 2022's Figure 6B legend attributes to the primary
a claim it does not make. The row's existing "do not score independently"
instruction is **verified, not inferred**.

**60-189 does not aggregate.** It is the PH domain, shown "with **no sign of
aggregation**", and deleting it "did not ablate its aggregation propensity". If
kept at all it is a **negative control**, never an aggregation-critical region.

**Sufficiency is explicitly negative**, which the construct column must carry:
aa 1-382 does not aggregate, so the linker "is **not in itself sufficient**".
Necessity is shown twice and quantified blind — ≥1.3 aggregates per cell with
the region versus ≤0.1 without, p < 0.001.

### Bradshaw 2014: the legacy-arm run, parameterised — and a false positive on our own protein [READ, 16 Nov 2026]

*PLoS ONE* 9:e111196, CC BY. Bradshaw 2017 attributes its predictor result to "our
**previous** analyses (8)". **This is paper 8**, and the run is specified well
enough to reproduce:

| tool | URL | threshold |
|---|---|---|
| AGGRESCAN | `bioinf.uab.es/aggrescan` | A4V value of 0, per residue |
| FoldAmyloid | `bioinfo.protres.ru/fold-amyloid/oga.cgi` | default parameters, **21.4** |
| ProA | `www.abl.ku.edu/ProA` | ProA-SVM *and* ProA-RF, 0.5 |
| TANGO | `tango.crg.es` | α-helix *and* β-sheet, default, 5% |

Four servers, **six measures**, with an explicit consensus rule: *"stretches of 5
or more consecutive amino acids which were each predicted to have aggregation
propensity by at least 3 of these 6 methods."* **All four are the frozen legacy
arm of §5.1.**

**It cross-validates Murray 2017 independently.** Murray gives FoldAmyloid as
threshold **21.4** at `bioinfo.protres.ru`, scale "contacts 8 Å", frame 5.
Bradshaw gives **21.4** at the same host with "default parameters". Same
threshold, same host, unrelated groups — and Murray names the defaults Bradshaw
leaves implicit. **Together they pin the §5.1 reimplementation target from two
directions.**

**One reproducibility gap, recorded:** the 2014 Methods give **no accession and no
reading frame**. The 652-aa frame arrived in 2017. So the "aa 230-236" quoted in
2017 could be either frame — but **checked, and it does not matter**: 230-236, or
289-295 if converted from the 593 frame, both fall **outside** 324-348. The
stratum assignment is robust either way.

### A documented false positive, this time on our own protein

The predictors' **only** β-sheet call on TRIOBP-1 was the **PH domain** — and the
same paper refutes it:

> "The alternative, aggregation occurring through the interaction of β-strands,
> is seemingly discounted as deletion of **the only region of the TRIOBP-1 protein
> with a predicted β-strand**, the Pleckstrin homology domain, **has no effect on
> the aggregation propensity**"

ΔPH aggregates identically to full length, by microscopy and by aggregome
Western blot, in **two** cell types.

**So `TRIOBP-1 60-189` is reclassified as CONCORDANT of an unusual and useful
kind: the predictors found it and experiment says they were wrong.** It is a
**negative control** — a region the tools called and experiment rejected — paired
with 324-348, a region experiment found and the tools missed. **The two together
state the failure more cleanly than either alone.**

**And it is a third instance of the structural-context hypothesis, on this
project's own protein** — removing the objection that the idea could not be
tested here. hnRNPA1: predictors hit the folded **RRMs**. LECT2: disulfides lock
down the predicted regions. TRIOBP-1: the only β-prone call is the folded **PH
domain**. In all three the tools flag something **structurally sequestered** and
miss what is free to engage. Still a hypothesis from three Discussion sections,
and still silent on FUS-LC, which is wholly disordered.

### Samardzija 2026, and the 2024 paper is genuinely unobtainable [READ, 16 Nov 2026]

*Sci Rep* 16:8240, published 11 Feb 2026 — the newest output of the group that
mapped both founding regions. **No predictor runs and no new mapped regions**, so
it adds no row. Three things it does give:

**1. The §5.2 novelty claim survives another check.** Named software is
**ImageLab only**. No TANGO, AGGRESCAN, FoldAmyloid, ProA, WALTZ, PASTA,
AmylPred2, ZipperDB, AggreProt, AggrescanAI or any PLM. The gap holds in the
group's most recent paper.

**2. The controls caveat is now peer-reviewed**, not thesis-only: *"Five of the
eight controls also showed some protein insolubility"*, and flatly, **"the mere
presence of insoluble protein cannot be used for diagnostic reference."** Cite
this rather than the thesis.

**3. It corroborates DISC1 384-415 from a third document.** Methods: *"amino
acids 257-655 of human DISC1, representing the D and I domains, **as well as the
aggregation prone-region between them** [44]"* — and **reference 44 is Zaharija &
Bradshaw 2024**, the unobtainable version of record. Verified: with D at 257-383
and I at 539-655, our row lies strictly between them and inside the 257-655
construct. Both checks pass.

*(A caveat on the premise, not on our rows: the paper's actual finding is that
insolubility is heterogeneous across brain regions and even between hemispheres.
That bears on the post-mortem evidence motivating the field, not on fragment-level
mapping in cells. No statistics were performed; the 1.5-fold threshold is
explicitly exploratory.)*

### The 2024 paper cannot be obtained, and that changes a rule

Checked directly, and the author reports the same. **OpenAlex gives
`oa_status: green` with exactly one open location — the bioRxiv preprint already
in hand — and no PMCID.** Europe PMC: `pmcid None, isOpenAccess N, inEPMC N,
hasPDF N`. No author manuscript, no repository copy.

§12.1 decision 3 said *"a rule is not weakened to accommodate a row when the row
**can** be obtained."* **This row cannot** — and it is a primary-stratum row.
Leaving it uncitable would be the rule defeating its own purpose. So a **narrow,
dated amendment**, with all three conditions required:

> a preprint may be cited only when **(i)** the version of record is
> **demonstrably unobtainable**, as a documented negative; **(ii)** the claim is
> **corroborated by an independent document read in full**; and **(iii)** the
> citation **names the preprint** and states the VOR was not consulted.

**All three hold here**, with (ii) met twice — the 2025 thesis Table 11 plasmid
names, and now Samardzija 2026.

**This buys citability, not certainty.** It does **not** settle Δ384-414 versus
Δ384-415; that still rests on the thesis plasmid names, and **the published
boundaries remain unchecked.** The exception is deliberately hard to reuse, and
**overturn it if you would rather carry the row as uncitable** — that is
defensible, and costs one row out of the primary stratum.

### What that inventory is not

Its author read only the TRIOBP-1 rows and the contamination material itself;
the other rows came from four parallel delegated searches with their labels
reproduced as reported, and four rows are flagged as retrieved-but-not-verbatim-
checked. One delegate caught its own summariser **inventing two residue ranges**
and corrected them before tabling; that check was not run on those four. Nothing
migrates into `data/regions.json` without being read first.

---

## A ref is not the object store — 16 Nov 2026

`research_notes/` was removed from all 69 commits with `git filter-repo` before
the repository was made public. The removal was verified two ways and **both
checks were insufficient in the same way**:

- `git log --all -- research_notes` → 0
- `git ls-tree -r origin/main | grep research_notes` → 0

Both interrogate **what the refs reach.** Neither interrogates **what the host
still stores.** GitHub retains objects orphaned by a force-push and serves them
by SHA, so after the repository went public:

```
https://github.com/<repo>/commit/4319b7d                      -> 200
https://raw.githubusercontent.com/<repo>/4319b7d/research_notes/... -> 200
```

**The files I had reported as "truly gone" were publicly readable.** They were
exposed for the minutes the repository was public, and only to someone holding a
pre-rewrite SHA — but the claim was wrong, not merely imprecise.

Closed by making the repository private again; verified from outside,
unauthenticated.

### Two transferable rules

**1. To show a hosted remote is clean, probe the object store, not the branch.**
Fetch a known-bad path at a known-bad SHA and require a 404. A local rewrite is
necessary and nowhere near sufficient: the authoritative copy is the host's.

**2. A 200 immediately after a permission change proves nothing.**
`raw.githubusercontent.com` kept serving the file for ~7 minutes after the
repository went private. The tell was that a **current** file 404'd on the same
schedule — if a control you expect to break is still working, you are reading a
cache, not the resource. This is the same shape as the earlier finding that *a
status code is not reachability*, now extended: **a status code is not current
state.**

### Closed, same day, by deleting and recreating the repository

`git gc` locally cannot reach objects held by the host, so the repository was
deleted and recreated under the same name — preserving the URL the deposited
`CITATION.cff` points at — and the clean history pushed into it.

**Two things surfaced only by doing it, both worth knowing in advance:**

- **The deploy key died with the repository.** Deploy keys are per-repository, so
  authentication succeeded while every operation returned *"Repository not
  found"*. Re-adding the same key failed with *"Key is already in use"*, which is
  itself diagnostic: GitHub still had it registered, so the deletion had not
  fully propagated. A fresh key pair sidesteps the uniqueness constraint, and
  retires the deleted repository's credential rather than reusing it.
- **A private repository cannot be audited by HTTP.** Everything 404s whether it
  is clean or merely hidden, so the two cases are indistinguishable. The test
  that works is to ask the server for the object: `git fetch origin <bad-sha>`,
  and an independent `git clone --mirror` audited for the path. Both were run and
  both were clean, before visibility was changed.

**Verified afterwards, unauthenticated:** `commit/4319b7d` → 404, where it had
been 200; the old path at the old SHA → 404; and every path the deposited files
promise — `CITATION.cff`, `LICENSE`, `PREREGISTRATION.md`, both scripts, the
descriptor, the dataset — → 200.

**The order that made this safe: private, verify the object store, then public.**
The first attempt went public before anyone had looked past the branch.

**The Zenodo deposit is unaffected**: it holds its own copies, never contained a
sweep, and no row of `data/regions.json` rests on one.

---

# 17 November 2026 — the freeze, the first run, and the answer

## The one-line position, updated

**Both arms have now been run, and the answer is a negative that survives its own
controls — with a twist nobody registered for.** AggrescanAI, the entire confirmatory
modern arm, does not recover the experimentally mapped aggregation-critical regions of
either DISC1 or TRIOBP-1. The pipeline that produced that negative reproduces the
predictor's *published* performance on 540 independent peptides, so the null is a
property of the predictor, not of our code. **And against TANGO, the one legacy tool that
can still be run, the modern tool is the worse of the two on 6 of 7 rows.** Both
generations miss both confirmatory regions; the newer one misses by more.

## The result

Against thresholds fixed before any score existed (§4: recovered = `v < 0.05`; predictor
succeeds on the set = Fisher p < 0.01):

| row | v | phases | recovered? |
|---|---|---|---|
| DISC1 384-415 | **0.416** | 0.331 – 0.463 | no |
| TRIOBP-1 324-348 | **0.908** | 0.777 – 0.922 | no |

Stouffer Z = −0.790, p = 0.785 (primary). Fisher p = 0.746 (secondary).

**The permitted claim is about AggrescanAI, not about modern predictors** (§5.2b). The
modern arm is one tool because AggreProt's weights are published nowhere.

**All 18 rows now score.** The DISC1 C-region rows fail hardest: 716-761 and 748-769 put
their best window at the **16th percentile** of the protein, and 717-737 at the **6th**.
Those are `PENDING` and partly `CIRCULAR`, so they are not confirmatory — but they point
the same way as the rows that are.

## Why the negative is believable — the control arm

A null is worth nothing if the instrument cannot produce a positive. Three checks, in
increasing strength:

1. **α-synuclein and tau, before any row was scored.** The top 12 residues of the whole
   441-residue tau protein are exactly VQIVYK and VQIINK.
2. **The statistic can fire.** Under amendment §3.1a the two tau hexapeptides score
   v = 0.0034 and 0.0080, an order of magnitude below the 0.05 bar.
3. **540 CPAD hexapeptides, scored in context: AUROC 0.703** [0.639, 0.760], p = 0.0005 —
   against the **0.69** Navarro et al. publish for AggrescanAI on their own external
   benchmark.

**That third check is the one that matters.** It is an independent, 540-point validation
that our local pipeline reproduces the predictor at its published level. The registered
null is therefore not an artefact of a broken local run.

## The contamination result, which cost more than the headline

§5.2b item 4 executed against **all three** CPAD 2.0 datasets, each read complete and each
matching the database's own stated totals — APR list 286 names, peptides 2031/2031
contiguous, structures 565/565 — plus an orthologue check in **both** OMA and
OrthoInspector, because CPAD90 transfers annotations to homologues.

- **The registered prediction held**: TRIOBP-1 and DISC1 are absent from CPAD.
- **The cost falls on the discordant stratum**, the only one that can discriminate
  between predictors. Of its five rows, **three are CPAD members** (FUS, hnRNPA1, LECT2)
  and are excluded under item 5. **Two survive.**
- Item 6 does not fire — the stratum is not empty — but **n = 2 is a case series on two
  proteins, not a rate**, and the write-up must not promote it.

**Three findings from that check are worth more than the verdict:**

- **One dataset is not CPAD.** hnRNPA1 is absent from the APR list *and* the peptide table
  and present three times in the structures table. LECT2 is the mirror image. Checking a
  single table would have cleared one of them wrongly.
- **One orthology database is not enough.** OMA alone would have missed MPRIP (Q6WCQ1),
  TRIOBP's human in-paralogue, which OrthoInspector reports and which had to be checked
  in its own right.
- **A status code is not content, again.** The CPAD harvest stopped at 1590 of 2031
  entries because the server began serving a CAPTCHA **under HTTP 200**. Trusting the 200
  would have published an incomplete table as a complete one.

## The legacy-versus-modern contrast — computed, and it runs the wrong way

`results/legacy_vs_modern_2026-11-17/`. §4 requires, for *modern beats legacy*, Wilcoxon
one-sided **p < 0.05** *and* median paired **Δv < −0.10**. Observed: **p = 0.148, median
Δv = +0.137**. Both fail, and the effect size fails **by sign**.

| | TANGO *v* | AggrescanAI *v* | Δv |
|---|---|---|---|
| DISC1 384-415 | 0.319 | 0.416 | +0.098 |
| TRIOBP-1 324-348 | 0.124 | 0.908 | +0.784 |

**6 of 7 scorable rows have the modern tool worse.** The single exception is TRIOBP-1
1-59, which AggrescanAI recovers (v = 0.041) and TANGO misses outright (0.9995) — and
which is not the mapped region the project asks about.

**The legacy arm is one tool, for the same reason the modern arm is.** ProA dead,
AGGRESCAN web-only, FoldAmyloid reimplementation unvalidated. One against one, so this is
**not** a statement about generations.

**An unplanned corroboration.** TANGO puts TRIOBP-1 324-348 at the ~97th percentile with
3–4 windows above it. Bradshaw 2014 wrote of the same region and tool: *"at least four
sites elsewhere in the protein were more strongly predicted."* An independent run on a
pinned binary, with parameters that paper never stated, reproduces its rank statement —
and agrees on the verdict, since 0.12 is still above the registered 0.05 bar.

**Neither direction is established.** The reverse was not registered and does not reach
significance descriptively either (sign test p = 0.0625, n = 7).

## Three defects in the pre-registration, found by running it rather than reading it

**§3.1 does not say whether windows slide or tile, and the two give different answers.**
The section states the property its null must have — *v ~ Uniform(0,1)* — and that
decides it: sliding windows overlap by 5 of 6 residues, are not exchangeable, and give
mean v = 0.663 on i.i.d. scores; tiling gives 0.495. **Tiling adopted on the
pre-registration's own criterion**, with no v computed for any row at the time.

**§3.1 cannot score a region shorter than its window** — so it silently dropped the two
tau rows that demonstrate the pipeline works. Amendment **§3.1a** scores such a region as
one window of its own length (m = 1, v = 1 − P), which preserves the registered null
because a single rank is uniform under exchangeability alone. **Post-unblinding, so
exploratory by §12**, and it cannot move the headline: all four affected rows are either
CPAD members already excluded or `PENDING`.

**§4 set a significance threshold its own design cannot reach.** The exact one-sided
Wilcoxon signed-rank minimum for *n* pairs is 2⁻ⁿ, so at the registered confirmatory
size of **n = 2 the smallest attainable p is 0.25**. §4 demands p < 0.05. **No data could
ever have satisfied it on the confirmatory set.** n ≥ 5 is needed for the test to be
capable of firing at all.

**This one was knowable before a single CPU cycle**, and nobody noticed until the test was
attempted. It is the clearest instance in the project of `CLAUDE.md` rule 3 — audit the
premises of the task, not only the literature — and the premise that failed was our own.

## What the AggreProt paper settled

Cima et al. 2026, *Commun Chem* **9**:229 [READ, CC BY], and its data deposit
(10.5281/zenodo.18670709):

- **The weights are "available upon request"** — the authors' own words in the version of
  record. Not hidden, not missing: **not deposited, by policy.** AggreProt still fails
  §5.2 and stays UNAVAILABLE rather than failing. The 16 Nov email was the sanctioned
  route.
- **Licence resolved**: CC BY-NC-SA 4.0, overriding both Zenodo's metadata and bio.tools.
  Defaults answered too — linear model, average metric, threshold 0.25.
- **AggreProt is trained on WaltzDB 2.0, not CPAD.** Our contamination column is specific
  to AggrescanAI and does not transfer.
- **A fourth published statement against the standard benchmarks — and the first that is a
  measurement**: 17 hexapeptides, TEM and ThT, classified blind, 8 false positives and 6
  false negatives in AmyPro/CPAD.
- **Serum amyloid A is one of the seven proteins**, and the peptide is **RDMWRA at mature
  15-20** — inside one of our rows. It does not invalidate the row: ours is the ordered
  core of an *ex vivo* patient fibril, theirs an isolated hexapeptide in buffer. That is
  the `construct` column's reason for existing.

## The memorisation question: posed, and deliberately not answered

On peptides where CPAD is demonstrably wrong, AggrescanAI scores AUROC 0.500. On
uncontested CPAD peptides it scores 0.703. That looks like a memorisation signature and
**is not evidence of one**: the contested interval [0.111, 0.889] contains 0.703.

Simulation puts the requirement at **~40 vs 40** contested peptides for 0.86 power. **We
have 3 vs 6**, and each additional one costs a four-week TEM experiment. **Rule 2 says
stop**, and we stopped.

## Transferable rules earned today

- **A status code is not content.** HTTP 200 served a CAPTCHA page for a table that had
  returned data minutes earlier.
- **A form displaying a DOI is not a registered DOI.** `10.5281/zenodo.24306057` was
  reserved on an unsaved draft; doi.org said *DOI Not Found*. The check that proves a new
  version is live is the **concept DOI** — if it still resolves to the previous version,
  nothing published.
- **Reserve the DOI before uploading, not after.** Deposited files are frozen, so
  publish-then-patch can only ever fix the repository copy. The deposited v1.1.0
  `CITATION.cff` carries the *old title* because that file was the one place of three the
  title was not updated in time. Recorded, not hidden.
- **Verify a frozen artefact by digest, not by size.** All five deposited files were
  confirmed by md5 against the local copies.
- **Tag after the final rebuild, immediately before upload.** The `v1.1.0` tag predates the
  morning's frame fixes and reproduces none of the deposited files but `LICENSE`; the real
  tree is tagged **`deposited-v1.1.0`**.
- **A 404 from a guessed filename is a wrong filename, not a broken pin.**
- **A frame choice is a scoring choice.** The same hexapeptide scores 0.641 in the mature
  hSAA1.1 chain and 0.718 in the P0DJI8 precursor — the `construct` lesson appearing
  inside the predictor itself.
- **Check the null before trusting the statistic**, and check it on simulated data where
  the answer is known.
- **Check that a test can reach its own threshold before running it.** §4's Wilcoxon
  cannot produce p < 0.05 at n = 2. Minimum attainable p is a property of the design, not
  of the data, and costs nothing to compute first.
- **An unregistered free parameter is a grid, not a choice.** TANGO's pH and temperature
  were never registered and are known to move the answer. Running all nine combinations
  and showing the conclusion identical at every one is honest; picking one after
  unblinding is not.
- **A published rank statement can validate an independent run.** Bradshaw 2014's "at
  least four sites elsewhere were more strongly predicted" is qualitative, but it pinned
  our TANGO run to within a window or two — useful where the paper's own parameters are
  unrecoverable.

## Where the dataset stands

**18 rows, all scored. Published as v1.1.0, DOI 10.5281/zenodo.24306057**, superseding
v1.0.0, which cannot tell a reader which rows are training-set contaminated. Every row now
carries a `frame`, and the last six were **verified by sequence rather than assumed** —
including serum amyloid A, where the allelic trap fired exactly as documented: the row is
right at mature residue 52 and canonical UniProt would have been wrong, inside the region.

## What is open

- **The AggreProt weights.** No reply as of the freeze. If they arrive it is exploratory,
  post-freeze, per §5.2b item 8 — and it would need its own WaltzDB contamination check.
- **Zaharija & Bradshaw 2024**, Elsevier, absent from PMC. Cannot move the 384-415 number,
  which the thesis's plasmid names settle, but that row is now one of only two surviving.
- **§12's prescreen gate checks *a* publisher PDF, not *the* one.** Left unchanged at the
  freeze deliberately; recorded so a later tightening is a visible amendment.
- ~~The legacy-versus-modern contrast is not yet computed.~~ **DONE, 17 Nov 2026** — see
  the section above. It required running TANGO ourselves, because published runs report
  thresholded calls and consensus rules rather than per-window profiles and so **cannot
  supply a *v*** for §4's Δv.
- **AGGRESCAN and FoldAmyloid remain unrun.** AGGRESCAN is web-only and fails the
  version-pinnable rule; the FoldAmyloid reimplementation must first pass its registered
  validation (Garbuzynskiy's 80%/72%, and Murray 2017's published zero-positive curve on
  FUS 2-214). Until then the legacy arm is TANGO alone.
- **n is the binding constraint everywhere.** The confirmatory set is 2 rows; §4 needs 5
  to be able to fire; the memorisation test needs ~40 vs 40 contested peptides against
  the 3 vs 6 that exist. **Widening `data/regions.json` beyond DISC1 and TRIOBP-1 is the
  one piece of work that unblocks more than one of these at once** — which is what
  `CLAUDE.md` already says the outstanding task is.
