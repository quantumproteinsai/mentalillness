# Working on this project

This file is loaded into context at the start of every session in this folder.
Read `STATE.md` before proposing anything; parts of the original plan did not
survive contact with the primary sources, and `STATE.md` is where that is
recorded.

## What this project is

A benchmark of protein aggregation predictors against experimentally mapped
aggregation-critical regions in schizophrenia-associated scaffold proteins.
The question:

> Do modern aggregation predictors recover the experimentally mapped regions of
> DISC1 and TRIOBP-1 that the 2004-2010 generation missed, and if not, what
> structural feature are they all missing?

The earlier form -- *do predictors fail here?* -- is already answered in print by
both primary papers. Those failures are cited evidence, not a result to
establish. Do not propose re-establishing them.

## Three rules, each learned expensively

**1. A number is quoted from a source somebody opened, or it is declared
unmeasured.** Everything under `research_notes/` is machine-generated and
unverified. Entries in `data/references_to_check.json` carry
`verified_against_publisher_pdf`, false until a human opens the PDF and checks
the claim. Never cite across that line. When reporting a number found by search,
say whether it was READ, a SNIPPET, or an EMPTY query result.

**The same rule applies to claims about documents, including this project's own.**
Verify them by opening the passage, not by grepping for the words the claim uses.
On 20 Nov 2026 a literal grep for "Wilcoxon" and "confirmatory" in the explainer
script returned zero and nearly produced a confident correction of a `CLAUDE.md`
sentence that was in fact right — the explainers state those numbers in other words.
Reading the passage instead found the real defect: a false sentence about the
project's own data, in a public document, in both languages. **A grep that misses is
indistinguishable from an absence, and both read as evidence.**

**2. Check the margin against the error bar before spending anything.** If the
difference to be reported is smaller than the uncertainty of the method
reporting it, no further work rescues it. Say so and stop. This retired four
claims on the companion project after the compute had been spent.

**3. Audit the premises of the task, not only the literature.** The most
valuable findings here were facts about proposed comparisons, not about papers:
two crystals that were not independent determinations, two sequences identical
between species so a contrast could not exist, a residue number from a review
that disagreed with the database. If a proposed experiment is impossible or
uninformative, say so -- that is the finding.

## Pre-registration is the point, not a formality

The statistic, the decoy construction and the success threshold are written down
*before* any predictor is run. Scoring first and choosing the statistic
afterwards produces a result that looks convincing and means nothing. If asked
to run a predictor before the analysis is pre-registered, say no and explain why.

## Out of scope

**Quantum chemistry and interaction energies.** There are no deposited aggregate
coordinates for any psychiatric protein: 0 of 5 candidates, and none of the 51
steric-zipper entities in the PDB. That is enumerated in `STATE.md`, not
assumed. It is a finding to report, not a gap to work around. Related work on
amyloid segment crystals lives in a separate project and does not belong here.

**Platforms, databases and general tools.** They come later, if the first result
holds. Scope discipline is what makes the question answerable in months.

## The validation set is the core asset

`data/regions.json` is more important than any analysis built on it, and is
intended to be published first, as a dataset with its own DOI. Two columns carry
the weight and must never be dropped:

- `construct` -- a region can be necessary in one construct and dispensable in
  another, and both results can be correct. A benchmark that ignores this scores
  against a moving target.
- `found_by` -- a region discovered *by prediction* is circular for a predictor
  benchmark. Those rows are analysed separately, not silently included.

**Current count is 27 rows across 17 proteins. The floor of 15 was passed; this
paragraph said 10 until 20 Nov 2026 and was misdirecting every session that read
it.** Widening the set in general is NO LONGER the outstanding task.

**The scarcity is now specific, and it is measured.** The confirmatory cell --
DISCORDANT, circularity-clean, CPAD-absent and power-eligible -- holds **3 rows
across 2 proteins** (TRIOBP-1 324-348, DISC1 384-414, DISC1 748-769) against §4's
requirement of **5 PROTEINS** — and the protein count is the binding one. Recruiting from
deposited fibril cores does not fix it: screening 82 independently curated cores
from 69 proteins gives **10 power-eligible (12%) and 1 of those surviving the CPAD
check -- a joint yield of 1 in 82**, and the Amyloid Atlas is redundant by protein
(797 entries collapsed to 69), so the rest of it is worth about one further
candidate. `results/cpad_screen_ten_2026-11-20/`.

**So "there aren't many" is a result, not a gap to work around.** Do not propose a
general widening sweep; it has been run. Two traps if any screen is run anyway:
**eligibility is per-REGION, not per-protein** (a protein with a long core may also
have a short one), and **one orthology database is not orthology** (OMA alone missed
MPRIP for TRIOBP and FUS for TAF15 -- query OMA *and* OrthoInspector, and check every
in-group paralogue in its own right).

## Numbering traps, both real

- **TRIOBP-1**: use the 652-residue frame of NP_008963.3 (UniProt Q9H2D6-7).
  Papers on the older 593-residue frame need **59 added**. One paper gives the
  short variant as 593 in one place and 597 in another.
- **DISC1**: UniProt Q9NRI5, canonical, 854 aa. Verify residue numbers against
  UniProt, never against a review.

## The two explainers are part of the deliverable

`docs/explainer_en.pdf` and `docs/explainer_fr.pdf` explain the project **for
undergraduate readers** — first-year biology assumed, nothing more. They are not
summaries for the author and should not drift into the register of `STATE.md`.

**They are generated, never hand-edited:**

```
python3 scripts/make_explainer.py
```

Each figure has **one source** in that script and is rendered twice, once to a `.svg` in
`docs/` and once to PDF vector operators, so the two cannot disagree. Editing a PDF or an
SVG by hand breaks that guarantee silently.

**Rebuild when a number they quote has moved — not on a schedule, and not every session.**
The explainers state the row count, the number of scored regions, the 7-of-9 split, the
Wilcoxon p, the confirmatory n, the smallest attainable p at that n, and the v < 0.05 bar.
**Those are real results, and a stale figure in a document written for outsiders is worse
than no document.** If a result changes, the rebuild belongs in the same commit.

**The two languages are one document.** Any change to the English must be made to the
French in the same commit, and the French must keep its accents — the PDF writer encodes
cp1252 and handles them.

**Keep the honesty of the main record.** Figures drawn from a formula are labelled
schematic; figures showing real results say so. The explainers state plainly that nothing
is established yet, that the decisive subset holds two rows, and that §4's threshold was
unreachable at that n. Do not quietly upgrade that into a positive finding to make the
document more satisfying to read.

## Housekeeping

Commit before running anything that writes results; on the companion project
the only thing that saved six hours of computation was that its output file
happened to be tracked. The remote `origin`
(`quantumproteinsai/mentalillness`) is the private dev repository itself, not a
curated public mirror -- unlike the companion project, where the GitHub remote
is a mirror and must never be pushed to. Pushing here is therefore ordinary, but
still ask: the author authorises each push.

Two things in the working tree are deliberately untracked and must stay that
way: `tango2_3_1.linux64.zip` and `TANGO_Instructions.pdf`. TANGO is distributed
under an academic licence, and redistributing it -- even in a private repository
headed for publication -- is the author's decision, not an agent's. `git add -A`
swept them in once.

**Since then both have been added to `.gitignore`, so the protection is structural
rather than a matter of vigilance [verified 20 Nov 2026: present, untracked,
ignored]. Do not remove those entries, and do not use `git add -f` on them.** The
same rule will apply to the AggreProt weights if they ever arrive -- gitignore the
archive by name *before* it lands, not after.
