# The modern arm on the structurally recruited rows — 19 Nov 2026

AggrescanAI (ProtT5 → 5 CPAD90 MLPs, soft-voting mean) on Orb2 and mature
β2-microglobulin. SOD1 was not run at all: under §10c C3 no *v* exists for a discontinuous
region, so there is nothing the number could be used for.

**The §7a ordering is intact and externally verifiable.** The strata were committed at
**12:53:14** and pushed to `origin`; these profiles were written at **14:49:18**. Nearly
two hours and a push apart, in the commit graph, not in an assertion. This is the first
pair of rows in the project for which that is true from the start.

| | row | legacy *v* (TANGO) | modern *v* (AggrescanAI) | region's rank in chain |
|---|---|---|---|---|
| | Orb2 176-206 | 0.9717 | **0.1144** | **87/117 → 4/117** |
| ⚠️ | β2m 22-85 | 0.2720 | **0.2720** | 1/16 → 1/16 |

---

> ## ⛔ THE INTERPRETATION BELOW IS WITHDRAWN. READ §3 FIRST.
>
> §1 and §2 were written before the CPAD check in §3 was run. **All three recruited rows
> are CPAD-present**, and AggrescanAI is trained on CPAD90 = CPAD 2.0 plus homologues.
> **Every AggrescanAI number in this report is in-sample.** The measurements stand exactly
> as recorded; the generational reading of §1 does not, and is retracted there. The
> sections are left in place rather than rewritten, because what they claimed before the
> check is the evidence for why the check is a gate and not a formality.

## 1. Orb2 — the largest *measured* difference between the arms, and it cannot be read as generational

TANGO scored the best window inside the core at **exactly 0.0000**, ranked **87th of 117**.
AggrescanAI ranks the same region **4th of 117**. *v* falls from 0.9717 to **0.1144**.

**That is NOT an answer to this project's headline question, and §3 is why.** Orb2 is in
CPAD's APR protein list under its exact UniProt name, and so is the CPEB family it belongs
to, so AggrescanAI has seen this protein and TANGO has not in the same way. **A
training-set advantage and a generational advantage are indistinguishable here**, and this
row cannot separate them. What is left is a measurement: the two arms rank this region very
differently. Read against the §4 bar, it is still §4 requires *v* < 0.05; the floor at
*M* = 117, *m* = 4 is 0.0170, so the bar was reachable. At rank 4 it was not reached: to
clear 0.05 the region would need *P* > 0.9957, which at *M* = 117 means essentially rank 1.

**The shape of the profile matters and is not visible in *v*.** AggrescanAI is unconfident
everywhere on this chain — **0 of 117 windows score above 0.5**, chain maximum 0.4482. But
it is *relatively* most confident on the region: window means inside median **0.1032**
against **0.0448** outside, a factor of 2.3. So the modern tool has the region's signal in
roughly the right place at roughly the right strength, on a chain where it commits to
nothing.

## 2. β2-microglobulin — both arms, eighteen years apart, return the identical number, and both are wrong about it

**TANGO *v* = 0.2720. AggrescanAI *v* = 0.2720.** Not approximately — identically, because
both are sitting exactly on the floor, and the floor is a property of *M* = 16 and
*m* = 10, not of either predictor.

Both put their **chain maximum inside the region**, at the window starting at residue 61,
ranked **1 of 16**. Two predictors separated by eighteen years of method development both
achieve the best result the statistic can represent, and the statistic reports a number
that §7 reads as **DISCORDANT** for both.

**And a second defect is visible in the same row, from the opposite direction.** §3 opens by
forbidding a hit/miss criterion, because a predictor calling a large fraction of residues
positive "recovers" any region essentially always. AggrescanAI calls **14 of 16 windows
above 0.5** here, median window mean **0.9151** — it considers nearly the whole mature chain
aggregation-prone. Inside-region median is 0.9662 against 0.7407 outside, so the region *is*
elevated, but on a chain where almost everything is.

> So this one row exhibits **both** failure modes the pre-registration was built around: a
> hit/miss criterion would score it a trivial success, and the rank statistic cannot report
> the genuine rank-1 success because the region covers 62.5% of the scorable chain. The
> row is a good argument for §3 and a good argument against §7, at the same time.

---

## 3. THE CAVEAT IS NOT A CAVEAT. ALL THREE ROWS ARE IN CPAD.

Checked 19 Nov 2026 against all three CPAD 2.0 tables, each re-fetched and byte-identical
in size to the 17 Nov capture, by accession where a table carries one and by normalised
name elsewhere, **with positive controls through the same query** (β2m, lysozyme — both
found) **and negative controls** (DISC1, TRIOBP-1 — both still absent).

| row | peptide table (by accession) | structures (by name) | APR protein list | verdict |
|---|---|---|---|---|
| **Orb2** Q9VSR3 | 0 | 0 | **PRESENT** | **CPAD_PRESENT** |
| **β2m** P61769 | **72** (17 amyloid) | **34** | **2 variants** | **CPAD_PRESENT** |
| **SOD1** P00441 | **30** (8 amyloid) | **11** | **1** | **CPAD_PRESENT** |

**Orb2 is the LECT2 pattern exactly, and it nearly escaped.** Two of three tables return
nothing. It appears only in the APR protein list, as `Translational regulator orb2` — an
**exact normalised match** to Q9VSR3's UniProt protein name. The peptide table is the only
one carrying accessions and therefore the tempting one to check; **checking it alone would
have cleared this row wrongly.** The rule written on 17 Nov — *any future row must be
checked against all three* — earned its keep on the very next row to need it. The
orthologue route is positive too: `Cytoplasmic polyadenylation element-binding protein`,
the CPEB family, is separately in the list.

**β2-microglobulin was never unknown.** The answer had been in the repository since 17 Nov,
under `_A_NAME_SEARCH_IS_NOT_AN_ACCESSION_SEARCH`: *"Beta-2 microglobulin carries 72 rows in
the CPAD peptide table and 34 in the structures table."* This protein is the origin of this
project's own cautionary tale about name searches. It is also **in the control set of**
`results/cpad_control_2026-11-17`, whose report states in plain words that *"the control
peptides are AggrescanAI's training data."* The row nonetheless carried
`cpad_status: UNCHECKED` for a day, and a predictor was run on it in that state. **The
failure was not of knowledge but of sequencing: the gate was passed rather than opened.**

### 3a. This is a structural problem with §10b, not an accident of three rows

**§10b recruits from deposited fibril structures. Deposited fibril structures are mostly of
classic disease amyloids. Classic disease amyloids are mostly in CPAD.** The project already
measured the base rate on 17 Nov: *of fourteen well-known amyloid proteins tested, **eleven**
are CPAD members.*

So §10b and §5.2b pull against each other, and §10b has now produced **three rows out of
three that are CPAD-present**. That is not bad luck; it is what the recruitment rule selects
for. The already-registered escape route is the calendar — `_CPAD_IS_FROZEN_AT_2020` — and
it does not save any of these three: CPAD 2.0 is frozen at 2020 and Orb2's core was
published *in* 2020.

**What this does and does not cost.** It costs nothing for Φ: core polarity is a geometric
measurement from coordinates and does not care what a predictor was trained on, so all
three rows remain valid members of the Φ set. It is fatal to using any of them in a
predictor comparison. **The two arms' numbers on Orb2 and β2m are recorded as measurements
and must not be cited as evidence about predictor generations.**

## 4. What was NOT done, deliberately

- **Neither row was added to `score_rows.RUNS`.** Computing *v* is not admission.
  Both were recruited under §10b **for the core-polarity analysis**, where *m*/*M* is
  explicitly not a criterion, and the Orb2 row's own `power_limit` says in capitals that
  entry to the benchmark arm is a separate decision under the eight-stage pipeline and
  §5.2b. Nothing here feeds the confirmatory statistic, which remains *n* = 5 / *n* = 2.
- **The Φ–*v* join was not recomputed.** §10b S2 allows it once, at the final *n*; the pool
  is not exhausted (lysozyme 8QUT pending its unidentified peptide, three candidates
  pending a PDF, five unscreened). These two rows now have both Φ and *v* and are ready for
  that join whenever *n* is final. **SOD1 has Φ = 0.438 and can never have a *v***, so it
  contributes to the Φ set but can never enter the Φ–*v* test — a mix §10c C4 requires to
  be reported.
- **The modern arm was not run on SOD1.** Not an omission: there is no statistic to feed.

## 5. Reproducing this

```
AGGAI_HOME=<dir with protT5/ and aggai/> python3 -I scripts/run_aggrescanai.py \
    results/modern_structural_2026-11-19/Q9VSR3.csv Q9VSR3 <sequence>
python3 -I scripts/modern_v_structural.py . results/modern_structural_2026-11-19 \
    results/modern_structural_2026-11-19/v_summary.json
```

The scored sequences are committed with the legacy run, in their scored frames. **The
software stack is now pinned** in `data/predictor_provenance.json` — it was not before
today, and `stack_equivalence.json` records the measurement that licenses comparing today's
numbers with the 17-18 Nov ones: 218 of 5092 residues differ by at most 1e-06, and **0 of
24 *v* values move**.
