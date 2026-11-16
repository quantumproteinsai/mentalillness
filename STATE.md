# In silico aggregation in mental illness — state as of 15 Nov 2026

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

**Ten, across eight papers and SIX independent groups** (updated 16 Nov 2026: the
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

### But Figure 1 also demotes PHF6*, and the reason is structural

**PHF6\* (275-280) sits in the first six residues of R2 — and R2 is DELETED from
the probe.** The scan was run with PHF43, which is ΔR2. This experiment therefore
could not establish PHF6* the way it established PHF6, and the paper does not
claim it did: the Abstract names **one** motif, *"a minimal hexapeptide
interaction motif of 306VQIVYK311"*, and Figure 4 calls PHF6* *"the **analogous**
sequence in R2."*

**PHF6\* is identified by sequence analogy, not by its own signal.** That is not
predictor-circular — analogy to an experimentally mapped motif is not an
algorithm — but it is a homology inference, and entering it as a second
independent clean row would have **double-counted one experimental result**.

**Consequence for H4: the control arm is n = 1, not n = 2**, and must be stated
that way. Independent support for PHF6* would have to come from von Bergen 2001
(*JBC* 276:48165), where ΔK280 — which sits inside PHF6* — is characterised.

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

### What that inventory is not

Its author read only the TRIOBP-1 rows and the contamination material itself;
the other rows came from four parallel delegated searches with their labels
reproduced as reported, and four rows are flagged as retrieved-but-not-verbatim-
checked. One delegate caught its own summariser **inventing two residue ranges**
and corrected them before tabling; that check was not run on those four. Nothing
migrates into `data/regions.json` without being read first.
