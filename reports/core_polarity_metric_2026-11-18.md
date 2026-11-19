# The core-polarity metric — SPECIFICATION, 18 November 2026

**Registered before computation.** Nothing in this document has been run. No Φ has been
computed for any structure, and no Φ has been compared with any *v*. The commit carrying
this file precedes the commit carrying any number produced by it, which is checkable from
the commit graph and is the point of writing it first.

**Status: EXPLORATORY under §12**, permanently. The reason is structural rather than
procedural, and it is in §1 below.

---

## 0. What this is for

The glycinin paper reports a fibril core held together partly by **polar** contacts, and
its Figure S6 sorts twelve published structures into hydrophobic-core and
hydrophilic-core classes. Every predictor in both arms of this benchmark is built on
hydrophobicity and β-propensity. **If a core is held by polar contacts, it is by
construction the case those predictors should miss.** That is the hypothesis.

The first version of the test was to borrow S6's labels directly. **That version is dead**:
all three distinct hydrophilic-core proteins in S6 — FUS, FapC, CsgA — are CPAD 2.0
members (`reports/recruitment_screen_2026-11-18.md`), so their core architecture is
collinear with training-set membership and a comparison would measure both at once.

This document replaces it with a metric computed from deposited coordinates by a rule
fixed in advance, so the labels do not come from anyone's classification — ours or S6's.

## 1. THE LIMITATION THAT DECIDES THE STATUS, STATED FIRST

**DISC1 and TRIOBP-1 have no deposited fibril structures.** Not low-resolution ones: none.
Their regions were mapped by truncation, deletion and solid-state NMR, which is why they
are in this dataset at all.

So Φ cannot be computed for them, and **this analysis cannot touch the confirmatory
stratum**, whose two rows are DISC1 384-415 and TRIOBP-1 324-348. It runs on a different
subset of rows from the question the project was built to answer, and no result from it
can confirm or refute H1. **It is a hypothesis about *why* predictors fail, tested where
structures exist, and it stays exploratory no matter how it comes out.**

Eligible rows are those whose region is the ordered core of a deposited fibril structure:
at present FUS, hnRNPA1, serum amyloid A, LECT2, TMEM106B, ANXA11 and glycinin, pending
the structure-identification step in §2. **That is at most 7 rows, several of them CPAD
members.** The honest expectation is that this is underpowered; §6 fixes what is reported
anyway.

## 2. Inputs, fixed before any coordinate is read

**A new row field, `structure`**, recorded for every eligible row *before* Φ is computed:
PDB entry, the chain used, and the modelled residue range. It is populated from the row's
own source paper, not from a search.

**Which entry, when a paper deposits several.** In order:

1. the entry the source paper designates as the polymorph it models and discusses;
2. failing that, the entry whose modelled range matches the row's `residues`;
3. failing that, the row is **excluded** and the reason recorded. No tie is broken by
   looking at anything downstream.

**AMENDED 18 Nov 2026, BEFORE ANY Φ WAS COMPUTED, and the amendment is recorded rather
than folded in silently.** Applying rule 1-3 left two rows undecided, because a paper can
deposit many entries of *the same fold*: TMEM106B has nine (one per brain/disease,
the paper's whole point being that the fold is shared) and ANXA11 has two. Rules 1 and 2
cannot separate entries that are all the designated fold and all match the range, and
rule 3 would discard two of the seven eligible rows for being *too* well deposited.

**Added rule 4: among entries that satisfy 1 or 2, take the one with the best reported
resolution; ties broken by the lowest PDB ID.** Resolution is a property of the
experiment, fixed years before this project existed and independent of Φ and of *v*, so
this cannot be steered. Every candidate entry is recorded on the row, not just the chosen
one, so the choice is auditable.

**Polymorphism is recorded, not averaged.** Glycinin is the worked example: PM1 is 27.8%
of the fibrils and PM3, at 70.8%, has no atomic model at all (Figure S3b/S2). Φ therefore
describes *the modelled polymorph*, and the row says so.

## 3. The metric

### 3.1 Build the environment

A fibril core is buried by its neighbours, so burial must be computed in the assembly, not
in one chain.

- If the deposited entry contains **≥ 5 chains**, use it as deposited.
- Otherwise replicate the deposited chain(s) along the helical axis using the **deposited
  helical rise and twist**, to **11 layers**. (For glycinin PM1 those are 4.8 Å and
  −1.6°, confirmed by the authors' own supplementary script.)
- **The analysis chain is the central layer**, so that edge layers never contribute.

### 3.2 Solvent accessibility

**Shrake–Rupley**, implemented in pure Python with no dependencies:

- probe radius **1.4 Å**, **92** sphere points per atom, golden-spiral distribution;
- van der Waals radii, fixed here: C 1.70, N 1.55, O 1.52, S 1.80, else 1.70 Å;
- hydrogens ignored; waters, ions and ligands excluded.

For residue *i* of the analysis chain, **S_full(i)** is its total side-chain-plus-backbone
SASA **in the assembly**.

### 3.3 Which residues are "the core"

**Core residue iff S_full(i) < 10 Å².** Pre-specified sensitivities at **5 Å²** and
**20 Å²**, both reported whatever they show.

Restricted to residues inside the row's `residues` range, so Φ describes the region the
benchmark actually scores rather than the whole modelled chain.

### 3.4 Polarity assignment, fixed now

| class | residues |
|---|---|
| **polar / charged** | D E K R H N Q S T Y C |
| **non-polar** | A V L I M F W P G |

Three of these are arguable — Y, C and especially G — so **two sensitivities are
pre-specified**: Φ with glycine excluded from the denominator entirely, and Φ with Y and C
moved to non-polar. All three numbers are reported together. **Choosing among them after
seeing the result is forbidden; the primary is the table above.**

### 3.5 The metric

**Φ = (core residues that are polar or charged) / (core residues)**, in [0, 1].

A row with fewer than **6** core residues is **excluded as unmeasurable**, and the
exclusion is reported.

## 4. Calibration, and the condition for abandoning the metric

S6's twelve structures carry an **outside-sourced published classification** — 8
hydrophobic-core, 4 hydrophilic-core. Their CPAD membership is irrelevant here, because
**no *v* is computed for them**; they are used only to find out whether Φ measures what
S6's authors meant.

Procedure: compute Φ for all twelve, then set the threshold **Φ\*** at the value maximising
Youden's J against S6's labels; ties broken by the midpoint of the tied interval.

**THE ABANDONMENT CONDITION, FIXED NOW: if Φ separates the twelve with AUROC < 0.80, the
metric is abandoned.** Not re-tuned, not re-weighted, not swapped for a different radius
set or a different polarity table. The twelve are the only outside check available, and a
metric that cannot reproduce a published visual classification on them is not measuring
core polarity. **That failure would itself be the reportable result**, and it is the
likeliest single outcome of this exercise.

## 5. The test

With Φ computed and committed, and only then joined to the scores:

- **Primary:** Spearman ρ between Φ and *v* (modern arm, AggrescanAI, phase 0) across
  eligible rows. **One-sided**, in the direction the hypothesis names: higher Φ → higher
  *v* → worse recovery. α = 0.05.
- **Secondary:** the same on the legacy arm (TANGO), which should behave the same way if
  the mechanism is hydrophobicity rather than any one tool.
- **The CPAD confound is reported, not adjusted away:** ρ is reported for all eligible
  rows and again for CPAD-absent rows alone. With the numbers involved the second will be
  badly underpowered, and that is stated rather than hidden.

**The minimum attainable one-sided p is reported next to the observed p**, as §4 of the
pre-registration should have done from the start.

## 6. The ordering, which is the part that must not slip

```
identify structures  ->  record `structure` on each row  ->  COMMIT
  ->  compute Φ  ->  COMMIT Φ
  ->  only then join Φ to v and run the test
```

**Φ must be in a commit before the commit that compares it with *v*.** This is the same
discipline §7a imposes on stratum labels, imposed for the same reason and checkable the
same way. It exists because Φ has three pre-specified variants and a threshold, and
knowing *v* while finalising any of them would make the whole exercise worthless.

## 7. What a result would and would not license

**Permitted on a positive result:** *Across the structural rows of this dataset, cores
with a higher polar fraction are recovered less well by the predictors tested.* An
association, on fewer than ten non-independent rows, outside the confirmatory stratum.

**Not permitted, whatever comes out:**

- anything about DISC1 or TRIOBP-1, which have no structures and are not in this analysis;
- any claim that polarity is *why* a predictor failed on a particular row — the metric is
  a correlate, and hydrophobicity-based predictors failing on polar cores is close to
  tautological if the association is strong;
- any revision of the confirmatory result, which this analysis cannot reach.

**And the tautology deserves stating plainly:** if these predictors score hydrophobicity,
then "they score polar cores lower" is partly a restatement of how they work rather than a
discovery about amyloid. What would make it a finding is the *experimental* half — that
polar-core regions are nonetheless genuine aggregation determinants, which the rows
establish independently of any predictor. **The interesting claim is not that the tools
dislike polar cores; it is that nature does not.**

---

## Two deviations from this specification, recorded 18 Nov 2026

**1. Eleven layers were registered; thirteen were executed.** §10a and this file both say
the assembly is built to **11 layers**. `scripts/core_polarity.py` builds **13**
(`copies=6`, −6…+6), and its own docstring gives the reason: *"so the analysis chain
always has >= 5 subunits on each side"*.

**The direction is known and one-way.** More layers can only increase burial, never
decrease it, so Φ computed at 13 is an upper bound on Φ computed at 11. At a 4.8 Å rise
the sixth neighbour sits ~29 Å from the analysis chain and cannot occlude it against a
1.4 Å probe, so the two should be identical. **That is reasoning, not a measurement, and
it is recorded as reasoning.** The deviation is conservative and documented in the code,
but it is a deviation from a registered number and is not waved away.

**2. The Φ results cannot be re-run from this repository.** No coordinate file is
committed — `git ls-files` returns zero `.cif`/`.pdb` entries — and no reproduce command
for `core_polarity.py` appears in any report. The PDB IDs and chains are recorded, so the
analysis is **re-derivable** by someone who downloads them; it is not **re-runnable** as
committed.

This is the same defect class as the `score_rows.py` path bug of 17 Nov, whose comment
reads: *"An archived output plus a script that cannot find it is not a reproducible
result."* It has now recurred in a second analysis.

**Both are pre-submission blockers, not analysis blockers.** Neither changes a number
today. Before the manuscript is submitted: re-run Φ at 11 layers and report whether any
value moved, and either commit the coordinates or commit a fetch script that pins the
PDB IDs and checksums what it downloads.

---

# Both pre-submission blockers closed, 19 Nov 2026

## Blocker 1 — eleven layers registered, thirteen executed: CLOSED, and it was worth checking

Re-run at the registered **11 layers** across all 22 structures (10 rows, 12 calibration),
committed in `results/core_polarity_2026-11-19/`.

**Exactly one residue in one structure changed state.** In glycinin G4 (9V45) a single
arginine sits on the SASA < 10 Å² boundary: buried at 13 layers (core 25/27, Φ = 0.480),
exposed at 11 (core 24/27, **Φ = 0.458**). Every other row and **all twelve calibration
structures are identical to three decimals**, and AUROC holds at **0.844** against the
§10a abandonment bar of 0.80.

The registered *n* = 7 test, re-run at 11 layers on the same rows and the same *v*:
**ρ = +0.821, exact one-sided *p* = 0.0171** — identical to six decimal places.

> **DO NOT REPORT THAT AS ROBUSTNESS.** Glycinin's Φ **rank moved from 4th to 6th**. It fell
> two places while hnRNPA1 and SAA each rose one, and Σd² happened to stay at exactly 10 in
> both orderings. Spearman's ρ depends only on Σd², so it could not see the change. A
> different neighbour, or a different *v* for glycinin, and the number would have moved.
> **The deviation did change a Φ value and did change a rank; ρ was insensitive to that
> particular swap by arithmetic coincidence.**

The earlier note said the direction of the effect was one-way reasoning rather than a
measurement — *"That is reasoning, not a measurement."* It is now a measurement, and the
reasoning was right about the direction (fewer layers → fractionally more exposure → the
boundary residue leaves the core) and right that the magnitude was small. **That it was
right does not retire the rule that produced the warning.**

## Blocker 2 — Φ not reproducible from the repository: CLOSED

Three files now stand in for the uncommitted coordinates:

- **`data/phi_spec.json`** — every input, including deposited rise and twist, and which
  rows are frozen under §10b S3.
- **`data/coordinate_manifest.json`** — **SHA-256 of all 22 coordinate files analysed.**
- **`scripts/fetch_coordinates.py`** — fetches from RCSB and verifies each checksum;
  **a mismatch exits non-zero and names the entry**, so an RCSB re-version cannot silently
  change a published number.

The coordinates stay uncommitted (third-party data, ~90 MB, RCSB is canonical). The manifest
is what makes that defensible rather than merely convenient.

## One finding that came out of doing this

**6VPS numbers its residues 23-53, not 176-206** — an offset of −153, with the UniProt span
recorded only in `_entity.pdbx_fragment`. Requesting 176-206 selected **no atoms** and
`core_polarity.py` refused rather than scoring something. The fifth frame collision this
project has found, and the first inside a structural deposit rather than in prose. Recorded
in `data/phi_spec.json` as `range_note` and in the Orb2 row.
