# The legacy arm on the three structurally recruited rows — 19 Nov 2026

**What was asked:** run the legacy arm on Orb2, β2-microglobulin and SOD1, the three rows
admitted on 18–19 November under PREREGISTRATION §10b/§10c.

**What was done:** TANGO at the pinned digest over the registered 9-point pH/temperature
grid on **two** chains. The third row takes no *v* and was refused by name.

**Ordering, which is the only thing that makes these labels worth anything.** No modern
predictor has been run on any of these three chains. The strata below are committed to git
**before** the modern arm, as §7a requires and as §7a itself could not claim — on 17 Nov
both arms ran with no labels applied in between. For these rows the commit graph shows the
ordering intact from the start.

| | row | *v* | stratum | call |
|---|---|---|---|---|
| ✅ | Orb2 176-206 | **0.9717** | DISCORDANT | **earned** |
| ⚠️ | β2-microglobulin 22-85 | **0.2720** | DISCORDANT | **forced — and false about the world** |
| ⛔ | SOD1 3-55,86-153 | — | unassignable | refused by rule |

---

## 1. Orb2 — a clean, earned miss, and the strongest legacy-arm result in the set

*v* = 0.9717 at the reporting point, grid range 0.9705–0.9791, **call stable at all nine
grid points**. Scored on the 704-residue canonical Q9VSR3, which is the Orb2B frame; the
profile slice at 176-206 was checked against the row's stored sequence character for
character at every grid point.

**The call is earned, and that was checked rather than assumed.** The smallest *v*
attainable at *M* = 117, *m* = 4 is **0.0170**, so *v* < 0.05 was reachable and was not
reached.

**What *v* alone understates.** The best 6-residue window inside the core scores **exactly
0.0000** and ranks **87th of 117** windows in the chain. TANGO's chain maximum, 78.70, sits
at residue 493 — far outside. This is not a near miss: the tool assigns zero aggregation
propensity to an amyloid core that was determined by cryo-EM from endogenous material
purified from three million fly heads.

> **DO NOT PRESENT THIS AS NOVEL WITHOUT A PRIOR-ART CHECK.** The core is
> `QLHQQQHQQQHQQHQQHQQQQQLHQHQQQLS` — glutamine/histidine-rich — and TANGO carries no
> polyglutamine term. A zero on a polyQ tract is quite possibly a documented limitation of
> the tool, in which case our number reproduces a known fact and is a positive control on
> the pipeline, not a finding. **The measurement stands; the interpretation needs the
> literature first.** This is the §9.1 situation that retired H3, and it should be checked
> before, not after.

It is worth noting what this row pairs with: Φ = 0.897, the most polar core in the Φ set.
A polar core scoring zero on a hydrophobicity-driven predictor is exactly the shape of H4.
**That is a hypothesis-consistent pair of numbers, not evidence for H4**, which needs the
modern arm and a pre-registered test.

## 2. β2-microglobulin — the registered rule returns a label that is the opposite of the truth

*v* = 0.2720, **identical at all nine grid points**. Scored on the **mature 99-residue
chain** (P61769 minus the 20-residue signal peptide), the frame the row's residues are
stored in; scoring the 119-residue precursor would have put a signal peptide into the
window pool as a decoy, the defect already registered for glycinin.

*v* ≥ 0.05, so §7 returns **DISCORDANT**. **That label is false about what happened.**

The smallest *v* attainable at *M* = 16, *m* = 10 is **0.2720** — and the observed *v* **is
0.2720, to every digit.** The statistic is sitting exactly on its floor, which happens only
when the region's best window is the single highest-scoring window in the whole chain. It
is:

- TANGO's chain maximum is **94.39**, at the window starting at residue **61**;
- residue 61 is **inside** the mapped core 22-85;
- it ranks **1 of 16**;
- residue 61 opens the native **E-strand (Phe62-Phe70)**, which this row's `found_by` field
  already records as *"long been identified as a region of high amyloidogenicity"*.

**TANGO succeeded maximally, and the registered statistic cannot say so.**

**The label was nevertheless left as DISCORDANT.** The rule is registered and mechanical,
and an agent that overrides a registered rule because the answer looks wrong has replaced
pre-registration with its own judgement. The label stands, the defect is recorded beside
it, and the row is marked `confirmatory_eligible: false` so nothing is computed from it.

### 2a. The general defect, which belongs to §7 and not to β2-microglobulin

**§7 thresholds *v* against 0.05 without asking whether 0.05 was attainable.** It inherits
the §3.1b information limit without saying so. Measured across the dataset:

> **5 of the 10 rows whose stratum came from our own TANGO *v* carry a DISCORDANT label
> that no predictor output could have avoided** — CHCHD10 42-75 (floor 0.1041), CHCHD2
> 54-86 (0.0961), DISC1 691-836 (0.0812), TAF15 7-99 (0.0739), TMEM106B 120-254 (0.2179).
> β2-microglobulin makes it 6 of 11.

The remaining nine assigned strata came from the **literature**, not from our *v*, and the
floor is irrelevant to those: TRIOBP-1 60-189 is CONCORDANT because the predictors *called*
the PH domain and the experiment refuted it, which is a published false positive and not a
reading of our statistic. **Mixing the two kinds of label is how this audit first produced
a wrong number**, and the two are separated above.

**IT CHANGES NO PRIMARY RESULT, AND THAT WAS CHECKED RATHER THAN HOPED.** A call is forced
only above *m*/*M* ≈ 0.1026, while `power_eligible` requires *m*/*M* ≤ 0.05. So the forced
set is a **strict subset** of the power-ineligible set, and **no `power_eligible` row
anywhere in the dataset carries a forced call** — verified exhaustively, not argued. There
is a band, 0.05 < *m*/*M* < 0.1026, that is power-ineligible with an earned call: ANXA11
0.0595, glycinin 0.0698, TRIOBP-1 1-59 0.0833, FUS 0.0920.

The consequence is that §3.1b's filter is **strictly stronger** than the one §7 needed and
was already being applied. Of the *n* = 5 confirmatory set, three rows (CHCHD2, CHCHD10,
TAF15) are forced; the two that are not are **DISC1 384-414 and TRIOBP-1 324-348** — which
are exactly the *n* = 2 `power_eligible` primary. **The project's existing choice of *n* = 2
as primary is independently vindicated by a filter it was not chosen with.**

## 3. SOD1 — refused, by rule, and the enum has no word for it

No *v* was computed and none should be. Under §10c C3 the region is two segments with a
30-residue disordered gap at 56-85, and the §3.1 statistic tiles a contiguous span. The
script **refuses this row by name and prints the reason**, so the refusal is auditable
rather than an absence. It is refused on contiguity, **not** on *m*/*M*, which is a
different defect — for reference only, *m*/*M* would also fail, at ≈ 0.80.

**A schema gap for the author to decide.** `stratum` is left `PENDING`, and that is the
wrong word: §7a fixed PENDING to mean *the legacy arm has not been run on this row yet*,
whereas here the arm **has** been run on the chain and the statistic declined the region.
The permitted values are `DISCORDANT`, `DISCORDANT_DERIVED`, `DISCORDANT_PROVISIONAL`,
`CONCORDANT`, `PENDING`. **A value such as `NOT_APPLICABLE` would be correct, and adding
one to a dataset headed for a DOI is the author's decision, not an agent's.**

The field is **inert** for this row, which is why leaving it is safe rather than merely
convenient: the stratum is consumed only to select rows into the benchmark arm, and this
row is benchmark-ineligible on the separate §10c C3 ground. A new machine-readable field
`stratum_not_assignable` records the reason, because the lesson of the TRIOBP-1 324-328 row
is that **a warning in prose is not a constraint** — that row carried "DO NOT score this
row as an independent region" in its note and was scored anyway, by our own script.

---

## Reproducing this

```
unzip tango2_3_1.linux64.zip -d <some empty dir>        # academic licence, untracked
TANGO_BIN=<dir>/tango_x86_64_release TANGO_OUT=<outdir> \
  python3 -I scripts/run_tango_grid.py Q9VSR3     results/legacy_structural_2026-11-19/Q9VSR3.seq
TANGO_BIN=<dir>/tango_x86_64_release TANGO_OUT=<outdir> \
  python3 -I scripts/run_tango_grid.py B2M_mature results/legacy_structural_2026-11-19/B2M_mature.seq
python3 -I scripts/tango_v_structural.py . <outdir> results/legacy_structural_2026-11-19/v_summary.json
```

The binary's SHA-256 is re-verified at run time against the pin in
`data/predictor_provenance.json` (`d0e381c2…`); the digest **is** the version, so a
different digest refuses to run. The two scored sequences are committed in their scored
frames, which is the thing that was missing from earlier runs — a frame is not reproducible
from an accession alone when the chain is a mature product.

The 18 profiles are archived under `tango_profiles/`.

## What has NOT been done, and must not be

- **No modern predictor has been run on any of these three chains.** That is the next step
  and it is now unblocked for Orb2 and β2m, the strata being committed.
- **The Φ–*v* test is not recomputed.** §10b S2 allows it once, at the final *n*; the pool
  is not exhausted (lysozyme 8QUT pending its unidentified peptide, three candidates
  pending a PDF, five unscreened), so the final *n* is not yet known.
- **β2m contributes no *v* to any statistic** despite having one, being
  confirmatory-ineligible and power-ineligible.
- **Orb2's polyQ interpretation is unchecked against prior art.** See §1.

---

## Appendix, 19 Nov 2026 — an internal contradiction found by preparing an extract for the source authors

While assembling `correspondence/2026-11-19_extract_for_bradshaw.md`, the TRIOBP-1 324-348
row was found to contradict itself. `note_on_the_source_field` read:

> "the document actually opened is Zaharija 2022. **THIS ROW IS SUPPORTED BY ZAHARIJA 2022,
> NOT BY BRADSHAW 2017, which has never been read.**"

while `verified_against`, `source_version_note` and `sequence_provenance` in the same row
all record that the Bradshaw 2017 publisher PDF **was** supplied by the author and read in
full on 16 Nov 2026. **Three fields said read; one said never read** — and the stale one is
the field a reader consults when deciding what to cite. Corrected.

**Two gaps this exposes, neither yet closed:**

1. **Nothing in the pipeline compares a row's fields against each other.**
   `validate_regions.py` checks schema, vocabulary, sequence-vs-range arithmetic and
   duplicates — all *within* a field or *across* rows, never *between* fields of one row.
   A row can therefore assert a source is unread beside a field asserting it was read, and
   validate cleanly. **A check for that specific contradiction is worth adding**: any field
   containing "never been read" or "has not been read" where `verified_against_publisher_pdf`
   is true, or where `source_version` is `version_of_record`.

2. **What actually caught it was the prospect of a subject-matter expert reading the row.**
   Not a script, and not a re-read — the row had been read many times. **That is an
   argument for sending extracts to source authors as a matter of course**, early, as a
   routine integrity check rather than a courtesy. The author offered; the offer turned out
   to be worth more than the confirmation it was made about.

The same row's `frame` field was also expanded from the bare string `"652-residue"` — a
length with no sequence record attached — to name NP_008963.3 / Q9H2D6-7, the +59 offset
and the Figure 12B verification. **A frame is not specified by a chain length.**
