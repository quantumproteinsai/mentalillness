# AggrescanAI — the confirmatory modern-arm run

**17 November 2026.** First predictor run of the project, executed after the freeze
(`freeze-2026-11-17`, SHA-256 of `data/regions.json`
`be9fbf180e6f75e19bae4aaf48d22c9a92725c8fbccf839718fac56134f32f9a`).

---

## The result, against thresholds fixed before the run

§4 fixes **v < 0.05** for a row to count as recovered, and **Fisher combined p < 0.01**
for a predictor to count as succeeding on the set.

| row | m | M | P | **v** | v across all 6 phases | recovered? |
|---|---|---|---|---|---|---|
| DISC1 384-415 | 5 | 142 | 0.898 | **0.416** | 0.331 – 0.463 | **no** |
| TRIOBP-1 324-348 | 4 | 108 | 0.551 | **0.908** | 0.777 – 0.922 | **no** |

**Confirmatory set (n = 2):** Stouffer Z = **−0.790**, one-sided p = **0.785** (primary).
Fisher χ² = 1.946 on 4 df, p = **0.746** (secondary).

> **AggrescanAI does not recover either region.** Both v values are consistent with a
> predictor carrying no information about these regions; TRIOBP-1 324-348 sits on the
> wrong side of chance. The verdict does not depend on the phase choice — no phase
> brings either row near 0.05.

**This is a case series on two proteins, not a rate**, exactly as §6.1 and §5.2b require,
and the claim permitted is about *AggrescanAI*, not about *modern predictors*.

## What the run is worth: two validations before any row was scored

A null result is only worth reporting if the pipeline can produce a positive one.

- **α-synuclein (P37840).** NAC region 61-95 mean **0.778**, our row 71-82 mean **0.806**,
  acidic C-terminal tail 96-140 mean **0.149**. The known non-aggregating tail is
  correctly flat.
- **tau (P10636-8).** The **top 12 residues of the entire 441-residue protein** are
  exactly VQIVYK (306-311) and VQIINK (275-280) — the two canonical tau hexapeptides,
  which are this dataset's two CONCORDANT tau rows. Whole-protein mean 0.072.

The pipeline recovers known aggregation cores on two independent proteins. **Both are
CPAD members**, so this is a check that the pipeline works, **not** evidence that
AggrescanAI predicts: on those rows a hit is recall of training data (§5.2b item 5).

## Rows excluded, and rows that could not be scored

CPAD-contaminated rows, reported separately and excluded from the primary (n = 3):
α-synuclein 71-82 (v 0.109), hnRNPA1 251-295 (v 0.463), FUS 39-95 (v 0.958).
Stouffer Z = −0.233, p = 0.592; Fisher p = 0.416.

**Exploratory, and the one positive in the set:** TRIOBP-1 **1-59** reaches
**v = 0.041**, below the v < 0.05 bar, stable across all six phases (0.041 – 0.041).
It is `stratum: PENDING`, so it is **not** in the confirmatory set and this is not a
registered success. It says AggrescanAI finds *something* in TRIOBP-1 — just not the
experimentally mapped region.

### Updated the same day: five more rows became scorable

The frames for the four Cukkemane DISC1 rows, and the mature-chain frames for serum
amyloid A and LECT2, were resolved and **verified by sequence** (see `frame` on each
row). **Scorable rows went from 7 to 12. The confirmatory result did not move** — those
two rows were already scored and nothing about them changed.

| row | stratum | cpad | m | M | P | **v** |
|---|---|---|---|---|---|---|
| serum amyloid A 2-55 | PENDING | member | 8 | 17 | 0.971 | 0.212 |
| LECT2 55-75 | DISCORDANT_DERIVED | member | 3 | 22 | 0.841 | 0.405 |
| DISC1 748-769 | PENDING | absent | 3 | 142 | 0.165 | **0.995** |
| DISC1 691-836 | PENDING | absent | 24 | 142 | 0.736 | **0.999** |
| DISC1 716-761 | PENDING | absent | 6 | 142 | 0.165 | **1.000** |

**AggrescanAI fails hard on the DISC1 C-region.** For 716-761 and 748-769 the region's
best tile sits at the **16th percentile** of the protein — not merely unremarkable but
actively low-scoring, in a region established by solid-state NMR on recombinant protein.
These rows are `stratum: PENDING`, so this is not a registered confirmatory result, and
716-761 is `CIRCULAR` besides. It is recorded because it is the clearest signal in the
run and it points the same way as the confirmatory rows.

Still not scored:

| row | why |
|---|---|
| tau 306-311, tau 275-280 | 6 residues; a 6-residue tile contains them only if phase-aligned |
| TRIOBP-1 324-328, 333-340 | 5 and 8 residues; shorter than one tile, or not tile-aligned |
| DISC1 717-737, 739-761 | composite range, not a single interval |

**The first line is a real limitation of the registered statistic, not an accident.** A
6-residue window cannot score a 6-residue region unless the tiling happens to align with
it. The two rows that validate the pipeline are the two the statistic cannot score.

**One frame resolution is worth reading on its own.** The serum amyloid A row's sequence
is **not found in UniProt P0DJI8**. Aligned against P0DJI8's mature chain it gives exactly
one mismatch — **mature residue 52, canonical A versus hSAA1.1 V — inside the region**.
The dataset's allelic warning fired exactly where it says it does, and the row was right
where the canonical database entry would have been wrong.

---

## An ambiguity in §3.1, resolved on the document's own criterion

**§3.1 does not say whether windows slide or tile, and the two give different answers.**

§3.1 states a procedure *and* the property it must have: *"v ~ Uniform(0, 1)"* under H0.
That property decides it.

| windows | mean v | median v | q0.25 | q0.75 |
|---|---|---|---|---|
| sliding (overlap 5 of 6) | 0.663 | 0.767 | 0.404 | 0.966 |
| **non-overlapping tiling** | **0.495** | **0.486** | **0.250** | **0.745** |
| expected under H0 | 0.500 | 0.500 | 0.250 | 0.750 |

4000 simulations, i.i.d. per-residue scores, 25-residue region in a 652-residue protein.
Sliding windows overlap by 5 of 6 residues and are therefore **not exchangeable**, so
best-of-*m* is far less extreme than *x^m* assumes, and v is biased toward 1 — toward
*"the predictor failed"*. **Tiling reproduces the registered null; sliding does not.**

**Tiling was adopted.** The criterion is the pre-registration's own stated null, not the
analyst's preference, and the simulation is reproducible from `scripts/score_rows.py`.

**When this was decided, relative to seeing scores.** The per-residue profiles existed
and had been validated on tau and α-synuclein. **No v value for any row had been computed
under either reading.** The decision was made on the simulation above alone.

**A free parameter this does not fix:** tiling has 6 possible phases, and §3.1 fixes
none. Phase 0 (tiles from residue 1) is reported as primary, with the full range across
all six phases in the table. **No conclusion here depends on the phase.**

Had the sliding reading been used instead, both confirmatory rows would have scored
*worse*, so this choice is conservative with respect to the reported negative result.

---

## Exactly what was run

| | |
|---|---|
| notebook replicated | `aggrescanai.ipynb` sha256 `1e1e4bc0…94e7d6` (matches the pre-freeze pin) |
| AggrescanAI weights | `alvaro-2/aggrescanai` rev `7aba68e6…3240e7`, the 5-model `cpad_hotidp90` CV ensemble, each file SHA-256'd in every output header |
| embeddings | ProtT5 `Rostlab/prot_t5_xl_half_uniref50-enc` rev `94a6abc0…8dfbf` |
| scoring | soft-voting mean of the 5 models, per-residue |
| window | 6, per §5.3 (PLM tools per-residue, aggregated to 6-residue means) |

**Three deviations from the notebook, each recorded because each could move a number:**

1. **Weights read from pinned revisions, not `/resolve/main`.** The notebook pulls from a
   moving branch. Pinned copies were downloaded and checksummed.
2. **float32 upcast from fp16 weights.** No GPU here, and CPU kernels do not support fp16
   for these ops. An upcast loses nothing relative to the stored weights, but it is a
   deviation.
3. **No smoothing.** In the notebook the moving average is display-only and the exported
   score is the raw per-residue probability. §5.3 aggregates to 6-residue means
   downstream, which is what the statistic does.

Reproduce with `scripts/run_aggrescanai.py` and `scripts/score_rows.py`. Raw per-residue
outputs for all six proteins are archived beside this file, as §5.3 requires.

## What this does and does not license

**Permitted:** *AggrescanAI, a PLM-based predictor, does not recover the experimentally
mapped aggregation-critical regions of DISC1 or TRIOBP-1.*

**Not permitted:** *modern predictors do not recover them.* The modern arm is one tool
(§5.2b), because AggreProt's weights are published nowhere and no reply to the 16 Nov
request had arrived by the freeze.

**Still open:** the legacy arm for these rows is taken from published runs (§5.1a), not
re-executed, so the legacy-versus-modern contrast is not computed here.
