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

So the claim stands as written: **no aggregation predictor, of any generation,
has been run on DISC1 or TRIOBP-1 by the group that mapped their
aggregation-critical regions.** The project's novelty does not change, and
`PREREGISTRATION.md` §11's fourth falsification condition is discharged.

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
2. **It is a preprint.** The version of record is *Prog Neuropsychopharmacol
   Biol Psychiatry* **130**:110923 (2024), still unread. Re-check the boundaries
   against it — that is now the single remaining §6.3 item, and it is a
   re-check, not a gap.

**A third one-residue slip, in two days, from the same group.** The body text
writes the deletion constructs as **Δ384-414** three times (31 residues) while
Figure 5A and panels D-F label them **Δ384-415** and the same sentence says
"these 32 amino acids". 384-415 is right. With 7-vs-8 and 593-vs-597 that is
three; a fourth, unrelated, is in the same paper's Results, which prints
"AA 539-738" for both I+S and S+C (S+C is 635-836). **Verify every residue
number in this literature against the figure or the arithmetic, including
numbers in the paper that the row is sourced to.**

**Leliveld et al. 2009 is assessed in its own section below** — it does not
touch 384-415, and it narrows the redox proposal rather than confirming it.

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

### What that inventory is not

Its author read only the TRIOBP-1 rows and the contamination material itself;
the other rows came from four parallel delegated searches with their labels
reproduced as reported, and four rows are flagged as retrieved-but-not-verbatim-
checked. One delegate caught its own summariser **inventing two residue ranges**
and corrected them before tabling; that check was not run on those four. Nothing
migrates into `data/regions.json` without being read first.
