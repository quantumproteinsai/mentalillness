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
