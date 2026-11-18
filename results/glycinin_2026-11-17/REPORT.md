# Glycinin G4 164-190 — both arms, and the first row whose verdict depends on the phase

**17 November 2026. Post-freeze, post-unblinding, therefore EXPLORATORY under §12.** The
row is `stratum: PENDING`, so nothing here enters a confirmatory statistic. The frame
decision below was written into `data/regions.json` **before** either predictor was run.

---

## The result

| arm | tool | m | M | P | **v (phase 0)** | across all 6 phases | recovered? |
|---|---|---|---|---|---|---|---|
| modern | AggrescanAI | 3 | 43 | 0.849 | **0.388** | 0.135 – 0.388 | **no** |
| legacy | TANGO, registered grid | 3 | 43 | 0.942 | **0.164** | 0.047 – 0.164 | **no** |
| legacy | TANGO, pH 2.0 (sensitivity) | 3 | 43 | 0.965 | **0.101** | 0.035 – 0.101 | **no** |

§4 fixes **v < 0.05** for a row to count as recovered. **Neither tool recovers the region.**
Δv = **+0.224**, modern worse than legacy — the seventh row of nine pointing that way.

**TANGO is completely insensitive to the registered grid here.** v = 0.164475 at *all nine*
points of pH {5.0, 7.0, 7.4} × T {298, 303, 310} K — identical to six decimal places. The
unregistered parameters change nothing for this protein.

## The frame, decided before the run

P02858's 563-residue precursor is a signal peptide (1-23) plus three chains: A5 (24-120),
**A4 (121-378)** and B3 (379-563). The region sits in A4, and **A4 is what was scored** —
258 residues, 43 tiles at W=6, rather than the precursor's 93.

Scoring the precursor would have put `MGKPFTLSLSSLCLLLLSSACFA` into the window pool: 23
residues of almost unbroken hydrophobicity, which every predictor in both arms scores
highly and is right to, because signal peptides thread a translocon rather than aggregate.
Under §3.1 each such decoy lowers *P* and raises *v*, pushing the verdict toward "the
predictor failed". **A region can be made to look missed by choosing a frame that includes
a hydrophobic segment that is not in the sample.**

So the choice was fixed in advance, in the dataset, with reasons — not after seeing a
number. See `A_SIGNAL_PEPTIDE_IN_THE_SCORED_FRAME_BIASES_THE_STATISTIC` on the row, and
`_A_HYDROPHOBIC_SEGMENT_THAT_IS_NOT_IN_THE_SAMPLE_IS_A_DECOY_WINDOW` for the general rule.

**The offset is machine-verified, not commented.** The row stores precursor numbering
(164-190) while the profile is A4-local (44-70). `score_rows.py` now carries an explicit
`OFFSET` table and **re-checks the converted indices against the row's own stored sequence
on every run**, refusing to score on a mismatch. Both arms were also checked per profile
file: every one of the 14 TANGO outputs has `PVVAISLLDTSNFNNQLDQTPRVFYLA` at local 44-70.

---

## The finding: §3.1 fixes no tiling phase, and here that decides the answer

The AggrescanAI report said *"No conclusion here depends on the phase."* **That is no
longer true.** For this row, on the legacy arm, it does.

| phase | m | M | P | TANGO v (pH 7.0, 310 K) | | TANGO v (pH 2.0) |
|---|---|---|---|---|---|---|
| **0 (primary)** | 3 | 43 | 0.9419 | **0.1645** | | **0.1010** |
| 1 | 4 | 42 | 0.9881 | **0.0468** ✓ | | **0.0468** ✓ |
| 2 | 4 | 42 | 0.9881 | **0.0468** ✓ | | **0.0468** ✓ |
| 3 | 4 | 42 | 0.9881 | **0.0468** ✓ | | **0.0468** ✓ |
| 4 | 4 | 42 | 0.9881 | **0.0468** ✓ | | **0.0468** ✓ |
| 5 | 3 | 42 | 0.9643 | 0.1034 | | **0.0353** ✓ |

✓ = below the registered v < 0.05 bar.

**Four of six phases say TANGO recovers this region. Phase 0 says it does not.** Phase 0 is
reported as primary by the convention set in the AggrescanAI report, so **the registered
answer is "not recovered"** — but it is a knife-edge, and reporting it without this table
would be a choice disguised as a result.

**Why it bites here and nowhere else.** The phase changes *both* terms of v = 1 − P^m. A
27-residue region tiled at W=6 holds either 3 or 4 whole tiles depending on where the
tiling starts, and M flips between 42 and 43. With *P* near 0.99 the statistic is brutally
sensitive to *m*: at P = 0.9881, m=3 gives v = 0.0353 and m=4 gives v = 0.0468 — both
below the bar — while phase 0's slightly worse P = 0.9419 with m=3 gives 0.1645, three and
a half times higher. Every other row in the set has either a much larger *m*, where one
tile more or less barely moves v, or sits far from the bar.

**This is the fourth defect found in the pre-registration by executing it**, after §3.1's
sliding/tiling ambiguity, §3.1's inability to score regions shorter than its window, and
§4's threshold being unreachable at n=2. It is recorded, not patched: changing the phase
convention *after* seeing that it flips a verdict is exactly the move pre-registration
exists to prevent. **The honest statement is that this row's legacy verdict is
phase-dependent and the registered convention returns "not recovered".**

**The modern arm is not phase-dependent**: 0.135 – 0.388 across all six, never within a
factor of two of the bar. So the Δv *direction* is robust even where the legacy *verdict*
is not — modern is worse at every phase.

## An unregistered condition, run because withholding it would also be a choice

§5.1a's grid is pH {5.0, 7.0, 7.4}, chosen for physiological conditions. **These fibrils
were made at pH 2.0** — 20 mg/mL, 90 °C, 12 h, stirred. The matched condition is outside
the registered grid.

Running only the registered grid would quietly score a protein at a pH it never saw;
adding pH 2.0 silently would be an unregistered parameter choice. So it was run and is
**labelled as a sensitivity, not as the primary**: pH 2.0 at 298/303/310 K and at 363 K
(the 90 °C of the experiment). All four give **v = 0.1010**, identical to four decimals.

**The matched condition moves v toward recovery but does not reach it** (0.164 → 0.101 at
phase 0). The verdict is unchanged, and `predictor_provenance.json` already records that
pH moves TANGO's numbers substantially for other sequences, so this is a real sensitivity
that happens not to matter here.

---

## What this does to the legacy-versus-modern contrast

**n goes from 7 to 9**, and the conclusion does not move.

| row | TANGO *v* | AggrescanAI *v* | Δv |
|---|---|---|---|
| TRIOBP-1 1-59 | 0.9995 | 0.0409 | **−0.959** ← modern better |
| **ANXA11 39-74** | **0.4134** | **0.3315** | **−0.082** ← modern better |
| DISC1 748-769 | 0.9227 | 0.9955 | +0.073 |
| DISC1 384-415 | 0.3189 | 0.4164 | +0.097 |
| **glycinin G4 164-190** | **0.1645** | **0.3884** | **+0.224** |
| TMEM106B 120-254 | 0.7156 | 0.9900 | +0.274 |
| TRIOBP-1 333-340 | 0.0388 | 0.4240 | +0.385 |
| TRIOBP-1 324-348 | 0.1235 | 0.9079 | +0.784 |
| DISC1 691-836 | 0.0812 | 0.9994 | +0.918 |

**§4 requires Wilcoxon one-sided p < 0.05 AND median Δv < −0.10. Observed: p = 0.102,
median Δv = +0.224.** Both fail, and the effect-size criterion still fails **by sign**.

At pH 5.0 ANXA11's TANGO v is 0.3735, giving p = 0.082; **7 of 9 and the median are
unchanged at every grid point.**

**ANXA11 is the second row where modern wins**, and it only entered the contrast today —
its TANGO profile had existed since the 17 Nov run while its AggrescanAI score was blocked
by a missing line in a lookup table. Its margin is small (−0.082, and −0.042 at pH 5.0),
well inside the phase spread of either arm, so it is a tie more than a win.

**Reaching §4's threshold is now possible and was not before.** The minimum attainable
one-sided Wilcoxon p is 2⁻ⁿ: 0.25 at n=2, 0.0078 at n=7, **0.0020 at n=9**. The test can
now return significance; it does not.

**Not supported, still:** that legacy beats modern. Taken descriptively, 7 of 9 gives a
one-sided binomial p = 0.0898 — **neither direction is established.** And this remains one
tool against one tool, not a statement about generations.

---

## Exactly what was run

| | |
|---|---|
| modern | AggrescanAI, `alvaro-2/aggrescanai` rev `7aba68e6…3240e7`, 5-model `cpad_hotidp90` CV ensemble, soft-voting mean |
| embeddings | ProtT5 `Rostlab/prot_t5_xl_half_uniref50-enc` rev `94a6abc0…8dfbf`, float32 upcast, no smoothing |
| legacy | TANGO, binary SHA-256 `d0e381c28f847487069b0df29bb9d4f766391066710500d3170ecb73d9f31dbf`, **verified by the runner before any run** |
| TANGO invocation | `nt=N ct=N ph=<PH> te=<T> io=0.05 tf=0 stab=-10`, per §5.1a |
| scored column | TANGO `Aggregation` (§5.3); AggrescanAI raw per-residue probability |
| window | 6, non-overlapping tiling, phase 0 primary |
| input | P02858[121:378], 258 aa, A4 acidic chain |

Profiles: `P02858_A4.csv` (modern), `tango_profiles/` (9 registered), and
`tango_ph2_sensitivity/` (4 unregistered). Reproduce with `scripts/run_aggrescanai.py`,
`scripts/run_tango_grid.py` and `scripts/score_rows.py`.

**Three reproducibility defects were fixed to make this run possible**, all the same
defect: `score_rows.py`, `run_aggrescanai.py` and `run_tango_grid.py` each resolved their
inputs against uncommitted working directories, so none could be re-run from a clean
checkout. Paths are now overridable and defaults unchanged. `run_tango_grid.py` also
gained the binary checksum gate — the provenance file says "THE PIN IS THE SHA256", and
the script now refuses to run a binary that is not that one.

## What this licenses

**Permitted:** *Neither AggrescanAI nor TANGO recovers the ordered fibril core of soy
glycinin G4 under the registered statistic at its primary phase; TANGO is close, and four
of six tiling phases would call it recovered.*

**Not permitted:** anything about this region being *necessary* for aggregation. No
construct lacking 164-190 was ever made — see
`AN_ORDERED_CORE_IS_NOT_A_DEMONSTRATED_REQUIREMENT__NO_MUTAGENESIS_HERE` on the row. And
the protein's identity rests on one residue of density at 3.6 Å; **if the fibril is G5
rather than G4 this row must be rescored**, since G5's acidic chain is 320 residues, not
258.

---

## The Supporting Information, read 18 November 2026

Obtained as `ADVS-12-e09821-s002.pdf` from the **Europe PMC `supplementaryFiles` API** for
PMC12591115. PMC's own article pages served a **reCAPTCHA** to a scripted client, so that
route yielded a challenge page rather than the article; the Europe PMC route was checked
against a control request that returned *"not open access"*, so a hit there means the files
exist rather than that the query was malformed.

**All three claims that rested on unread figures are now resolved. One of them corrects
this row's own previous reading.**

### S4 — the necessity claim is weaker than the main text says

Section 3.3 says removing Pro164-Ala190 *"resulted in markedly poorer fitting (Figure S4c),
underscoring the necessity of this region for structural integrity."*

**Figure S4's own caption calls the figure "Sequence validation of PM1"**, and S4c reads,
verbatim:

> *Control reconstruction with the Pro164-Ala190 segment excluded **from the input
> sequence**, resulting in significantly poorer map-model fit.*

So the segment was withheld from the **sequence supplied to ModelAngelo** and the model
rebuilt. That tests whether the density is correctly assigned to Pro164-Ala190 — a sound
sequence-assignment control — and says nothing about whether the region is required for
aggregation. **No construct lacking 164-190 was made, nothing was mutated, nothing was
assayed for fibril formation.** The main text's word *necessity* overstates its own
supplementary figure; the caption is the better guide.

### S3b — the abundances, and the polymorph nobody modelled

By contour-length measurement of AFM images (FiberApp): **PM1 27.8%, PM2 1.4%,
PM3 70.8%.** This row is built on PM1, so **it rests on 27.8% of the fibrils.**

**The dominant form was never modelled.** Figure S2 records PM3 at 3.23 Å auto-refine and
FSC 0.143 of 3.13 Å, annotated *"(not suitable for model building)"*. The species that is
70.8% of the sample has no atomic model and no assigned sequence. Height distributions
confirm these are distinct species, not views of one: PM1 5.4 nm, PM2 6.9 nm, PM3 3.7 nm.

### S5 — this row had it wrong, and the correction matters

The row previously recorded *an alternative conformation inside the modelled region*. S5
says otherwise, verbatim:

> *Note that Val165–Asp172 (highlighted in purple) belongs to **an adjacent chain**, not
> the Pro164–Ala190 chain.*

**Within the span of this region, part of the density belongs to a neighbouring chain
threaded through it.** S7's note calls these *"extensive interchain interaction interfaces
between the two primary chains"*. So the ordering of 164-190 is a **quaternary** property,
not a property of the sequence alone — **a single-sequence predictor is being asked to find
a region whose order depends on a partner chain it cannot see.** That is a limitation of
the benchmark question as posed, and it applies to any cryo-EM row with an interdigitated
core.

### A lead the SI hands us, recorded as a lead

`CLAUDE.md` asks what structural feature the predictors are all missing. The paper's title
is *"**Dual Hydrophilic-Hydrophobic Core Architecture** in Soy Glycinin Amyloid Fibrils"*,
and **Figure S6 sorts twelve published fibril structures into hydrophobic-core (Aβ 7q4b,
Aβ 7q4m, α-syn 6h6b, tau 5o3l, prion 7yat, prion 8wzx, transthyretin 7ob4, AL59 9faa) and
hydrophilic-core (FUS 6xfm, FapC 9nqd, FapC 9u4u, CsgA 8enq).**

Every predictor in both arms is built on hydrophobicity and β-propensity. **A core held by
polar contacts is by construction the case they should fail on** — and the dataset already
contains a coincidence worth checking: **FUS is in S6's hydrophilic list, and FUS 39-95 is
among the worst-scored rows in the set (AggrescanAI v = 0.958).**

**Two rows is not evidence.** A test needs core-architecture labels assigned from the
structures *independently of the scores*, or it repeats the select-on-the-outcome error
retracted in `reports/recruiting_rule_2026-11-18.md`. S6 is a published, outside-sourced
classification, which is the independent labelling such a test needs. **The confound to
handle: FUS is a CPAD member and glycinin is not**, so a naive comparison mixes training-set
membership with core architecture.

### Also in the package

`ADVS-12-e09821-s001.py` — **read, not run.** A CCTBX helical-replication utility, which
independently confirms the PM1 helical parameters: **rise 4.8 Å, twist −1.6°.**
