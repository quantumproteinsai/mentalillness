# Φ for the three admitted rows, and the layer-count deviation closed

**19 November 2026.** Step 2 of the §10b ordering: Φ computed and committed for the newly
admitted rows, **before** any predictor is run on them and **before** any join. This run
also clears the two §10a pre-submission blockers.

---

## 1. The registered layer count, and what the deviation was worth

§10a registers replication to **11 layers**. The 18 Nov run executed **13**
(`copies=6`). That was recorded as a deviation and as a pre-submission blocker, with the
instruction to re-run at 11 and *report whether any value moved*. Both runs are now
committed side by side.

| row | Φ, 13 layers | Φ, 11 layers (registered) | moved? |
|---|---|---|---|
| FUS 39-95 | 0.675 | 0.675 | no (no helical parameters; replication does not apply) |
| hnRNPA1 251-295 | 0.465 | 0.465 | no |
| SAA 2-55 | 0.462 | 0.462 | no |
| LECT2 55-75 | 0.526 | 0.526 | no |
| TMEM106B 120-254 | 0.577 | 0.577 | no |
| ANXA11 39-74 | 0.441 | 0.441 | no |
| **glycinin 164-190** | **0.480** | **0.458** | **YES, −0.022** |
| Orb2 176-206 | 0.897 | 0.897 | no |
| β2m 22-85 | 0.582 | 0.582 | no |
| SOD1 3-55,86-153 | 0.438 | 0.438 | no |

**Nine of ten are identical; one moved.** In glycinin a single arginine sits just at the
SASA < 10 Å² boundary: with thirteen layers it is buried (core 25 of 27), with eleven it is
exposed (core 24 of 27). Two fewer layers of neighbouring subunits leave it fractionally
more accessible. The effect is real, it is confined to one residue of one row, and it is
the size one would expect of a boundary case.

### The registered *n* = 7 test, re-run at 11 layers: unchanged — but by luck, not robustness

**ρ = +0.821, one-sided exact *p* = 0.0171**, identical to six decimal places to the figure
computed on 18 Nov at thirteen layers. The CPAD-absent (*n* = 3, ρ = +1.000, *p* = 0.1667)
and legacy TANGO (*n* = 3, ρ = +0.500, *p* = 0.5000) arms are likewise unchanged.

**This must not be reported as evidence that the result is insensitive to the layer count.**
It is not. Glycinin's Φ **rank moved from 4th to 6th**:

```
13 layers:  FUS > TMEM106B > LECT2 > glycinin > hnRNPA1 > SAA > ANXA11
11 layers:  FUS > TMEM106B > LECT2 > hnRNPA1 > SAA > glycinin > ANXA11
```

Glycinin fell two places while hnRNPA1 and SAA each rose one, and **Σd² happened to stay at
exactly 10** in both orderings. Spearman's ρ depends only on Σd², so the statistic could not
tell the difference. A different pair of neighbours, or a different v for glycinin, and the
number would have moved. **The honest statement is that the deviation changed one Φ value
and one rank, and that ρ was arithmetically insensitive to that particular swap by
coincidence.**

**This was a correction, not a new look at the data.** Same seven rows, same v, same
statistic, run at the layer count that was registered rather than the one that was executed.
§10b S2 — the test is recomputed *once, at the final n* — is not engaged by it, and
`scripts/join_phi_v.py` now takes `--expect-n` and exits non-zero if the primary set is not
the size the caller asserted, so growing *n* requires editing a number on the command line.

### The calibration set is wholly unaffected

All twelve calibration structures were recomputed at 11 layers. **Every one is identical to
the 18 Nov value, to three decimals** — including the two FapC entries whose deposited rise
is ~14.4-14.6 Å, i.e. a β-solenoid with three cross-β rungs per subunit, where replication
moves the most material.

| group | n | Φ range | mean |
|---|---|---|---|
| hydrophobic controls | 8 | 0.208 – 0.563 | 0.395 |
| HYDROPHILIC controls | 4 | 0.477 – 0.778 | 0.583 |

**AUROC (hydrophilic over hydrophobic) = 0.844 at 11 layers**, against the §10a abandonment
condition of **< 0.80**. The metric still separates the two groups it was calibrated to
separate, at the registered layer count.

**Across all 22 structures, exactly one residue in one structure changed state.** That is
the full measured size of the deviation, and it is now a number rather than an argument.

---

## 2. Φ for the three admitted rows

Computed at the registered 11 layers, SASA < 10 Å², Φ = polar-or-charged fraction of core
residues. **No v exists for any of these three** — no predictor has been run on any of the
chains — so none of them appears in any correlation above, and none may until §10b's
ordering reaches that step.

| row | deposit | core / region | **Φ** |
|---|---|---|---|
| **Orb2 176-206** | 6VPS | 29 / 31 | **0.897** |
| **β2-microglobulin 22-85** | 6GK3 | 55 / 64 | **0.582** |
| **SOD1 3-55,86-153** | 7VZF | 105 / 121 | **0.438** |

Against the seven incumbents (0.441–0.675), the three new rows **widen the range at both
ends**: Orb2 is far above anything previously measured, SOD1 just below the previous
minimum.

### Two of the three reproduce their authors' own qualitative description

This is a validity check on the metric, not a result, and it is worth having because Φ was
specified without reference to any of these three papers.

**Orb2, Φ = 0.897.** The core sequence is `QLHQQQHQQQHQQQQHQQQQQLHQHQQQL` — glutamine and
histidine almost throughout. Hervás et al. say so in their own title sentence: *"Unlike the
hydrophobic core of pathogenic amyloids, the **hydrophilic core** of Orb2 filaments..."*,
and their mechanism is *"interdigitated glutamine packing"*. Φ was never shown that claim
and recovers it.

**SOD1, Φ = 0.438, the lowest in the set.** Wang et al.: *"Side chains of most hydrophobic
residues are located in the interior of the SOD1 fibril fold."* Again recovered.

**β2m, Φ = 0.582**, sits high-middle. The paper describes both a classic hydrophobic steric
zipper (Trp60–Leu39–Phe62–Val37–Leu64–Ile35) *and* buried polar features — a Tyr63/Tyr66/Tyr67
π-stack and the buried Cys25–Cys80 disulfide. An intermediate Φ is the expected reading of a
core described in both terms. **Note the registered caveat that applies here:** Y and C count
as polar in the primary Φ, and the pre-specified `phi_YC_nonpolar` variant exists precisely
so that a row like this can be checked against a different convention. Both variants are in
the committed JSON.

---

## 3. A frame trap inside a deposit, not inside a paper

**6VPS numbers its modelled residues 23-53, not 176-206.** The UniProt span appears only in
`_entity.pdbx_fragment` as `'UNP residues 176-206'`; the offset is **−153**. The 31 modelled
residues read `QLHQQQHQQQHQQHQQHQQQQQLHQHQQQLS` in all nine chains, matching Orb2B 176-206
character for character, so the two frames describe the same region.

Asking for 176-206 in that file selects **no atoms**, and the script said so and refused —
which is how this was found. **A silent empty selection would have been the dangerous
failure**; a row scored over zero residues, or over whatever happened to lie at those
indices, is worse than a crash. Every range in `data/phi_spec.json` is now in the deposit's
own numbering, with `uniprot_range` and `range_note` recording the difference where there is
one.

This is the fifth frame collision the project has found, and **the first that is in a
structural deposit rather than in prose.**

---

## 4. Reproducibility: the second §10a blocker is cleared

Previously no coordinate file was committed and none of the Φ numbers could be regenerated
from this repository. Now:

- **`data/phi_spec.json`** — every input: accession, entity, range, deposited rise and
  twist, and which group each row belongs to. The seven incumbents are marked frozen per
  §10b S3 and are not re-selected.
- **`data/coordinate_manifest.json`** — **SHA-256 of all 22 coordinate files** actually
  analysed.
- **`scripts/fetch_coordinates.py`** — fetches them from RCSB and verifies every checksum.
  **A mismatch exits non-zero and names the entry.** If RCSB re-versions a deposit, the Φ
  computed from the new file is not the Φ in this directory, and re-running then becomes a
  deliberate dated act rather than silent drift.

```
python3 scripts/fetch_coordinates.py <dir>
python3 scripts/core_polarity.py <dir> out.json data/phi_spec.json --rows 11
```

The coordinate files themselves remain uncommitted: third-party data, ~90 MB, with RCSB as
the canonical source. The manifest is what makes that safe.

---

## 5. What has NOT been done, and must not be

- **The Φ–*v* test has not been recomputed at *n* = 10 and must not be.** §10b S2: once, at
  the final *n*. The pool is not exhausted — lysozyme is pending on the identity of its
  second entity, three more candidates are pending, five are unscreened — so **the final *n*
  is unknown.**
- **No predictor has been run on Orb2, β2m or SOD1.** Under §7a the stratum for each must be
  assigned from the legacy arm and committed *before* the modern arm runs. All three carry
  `stratum: PENDING`.
- **CPAD status is unchecked for all three.** Recorded as a gap, not as a negative.
- **SOD1 and β2m cannot enter the benchmark arm at all** — SOD1 on `NON_CONTIGUOUS` (§10c
  C3), β2m on *m*/*M* ≈ 0.63. `scripts/score_rows.py` already refuses both: it skips rows
  whose range is not a single interval, and skips proteins with no predictor run. That guard
  predates §10c and was not written for it.
