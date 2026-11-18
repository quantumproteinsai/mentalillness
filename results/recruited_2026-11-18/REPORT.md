# Legacy arm on the three recruited rows, and their stratum labels

**18 November 2026.** TANGO run on TAF15, CHCHD10 and CHCHD2; stratum assigned
mechanically from the result; **committed before the modern arm has seen any of the three
accessions.** That ordering is the point of this run and is checkable from the commit
graph.

---

## Headline

> **All three are DISCORDANT, and the call does not depend on the two parameters that
> were never pre-registered**: it is identical at all nine pH/temperature grid points for
> all three rows.
>
> These are **the first three rows in the project whose stratum label satisfies §7's
> ordering requirement.** The six labelled earlier the same day do not, and are held out.

| row | accession | *P* | *m* | **TANGO *v*** | call at the 0.05 bar | stable over the grid |
|---|---|---|---|---|---|---|
| TAF15 7–99 | Q92804 | 0.4592 | 15 | **0.9999915** | **DISCORDANT** | yes, 9/9 |
| CHCHD10 42–75 | Q8WYQ3 | 0.9783 | 5 | **0.10407** | **DISCORDANT** | yes, 9/9 |
| CHCHD2 54–86 | Q9Y6H1 | 0.9800 | 5 | **0.09608** | **DISCORDANT** | yes, 9/9 |

*v* = 1 − *P*^*m*, §3.1, W = 6, non-overlapping tiling, phase 0, on TANGO's `Aggregation`
column per §5.3. Reporting point pH 7.0 / 310 K, matching the 17 Nov run exactly.

## What the ordering claim rests on, checked rather than asserted

`results/aggrescanai_2026-11-17/` contains eleven profiles. **None of them is Q92804,
Q8WYQ3 or Q9Y6H1**, and those three strings appear nowhere under `results/` outside this
directory — grepped, not assumed. `scripts/score_rows.py` independently lists all three
under **NOT SCORED — "NO PREDICTOR RUN for this protein"**.

So when the §7 rule was applied, there was nothing downstream to see. The 17 Nov six were
labelled knowing their AggrescanAI scores; these three were not. **That is the entire
difference between `confirmatory_eligible: true` and `false`, and it is why the pipeline
puts stage 7 in its own commit.**

## Two things in these numbers that should not pass without comment

### TAF15's *v* is ~1, and *m* is doing much of the work

*P* = 0.4592 means the best tiled window inside TAF15 7–99 sits at the **46th percentile**
of all 98 windows in the chain — TANGO finds the experimentally determined filament core
slightly *below average* for the protein it belongs to. That is a real and complete miss.

But the region is 93 residues, giving **m = 15**, and *v* = 1 − *P*^15 drives to 1 for any
*P* meaningfully below 1. **The statistic is sensitive to region length here**, so the
robustness check: at *m* = 5, the same *P* would still give **v = 0.980**. The DISCORDANT
call does not depend on the long region. The *value* 0.9999915 should not be read as
fifteen times more of a miss than 0.98.

### The two CHCHD rows score almost identically, exactly as predicted

**v = 0.10407 and 0.09608** — a difference of 0.008. The rows were flagged on 18 Nov as
**84.8% identical over the scored span**, with the prediction that they "score almost
identically **by construction**". The legacy arm has now confirmed that prediction on the
one arm that has run.

**This is evidence for the non-independence rule, not a coincidence to note in passing.**
Any pooled statistic that counts both is counting one measurement twice.

Both also sit **near the bar**: at 0.096 and 0.104 against a 0.05 threshold, TANGO is
within a factor of two of recovering these regions. They are not dramatic misses like
TAF15.

## The consequence, and it is sharper than "n goes up"

Once the modern arm runs, the §5.2b confirmatory set goes from **2 rows to 5**. The
confirmatory statistic there is Stouffer *Z*, which is continuous and has no discreteness
floor, so n = 5 is a genuine gain.

**§4's contrast is a different matter, and this is where the pair rule bites.** The exact
one-sided Wilcoxon signed-rank minimum is 2^−n:

| n | 2 | 3 | **4** | **5** |
|---|---|---|---|---|
| min attainable one-sided p | 0.250 | 0.125 | **0.0625** | **0.0312** |

- Counting the CHCHD pair as **two** rows: n = 5, floor **0.031 < 0.05** — §4's contrast
  becomes **testable on the confirmatory set for the first time in the project.**
- Counting it as **one**, which the rule recorded on both rows requires: n = 4, floor
  **0.0625 > 0.05** — **§4 remains unreachable.**

**So whether §4 is answerable at all turns entirely on a question about sequence identity,
not on any predictor result.** That is rule 2 of `CLAUDE.md` arriving before the compute
rather than after it. **The honest reading is n = 4 and §4 still unreachable**, and
reaching the floor needs **one more independent protein**, not one more row.

## Reproduce

```
python3 -I scripts/run_tango_grid.py Q92804  <Q92804.fasta>     # and Q8WYQ3, Q9Y6H1
python3 -I scripts/tango_v_recruited.py . results/recruited_2026-11-18/tango_profiles data/regions.json
python3 -I scripts/apply_strata_recruited.py data/regions.json
```

TANGO binary SHA-256 `d0e381c28f847487069b0df29bb9d4f766391066710500d3170ecb73d9f31dbf`,
verified by the runner before every run; the digest **is** the version. All **27** raw
profiles are in `tango_profiles/`. Every run produced exactly one row per residue, which
the runner checks because **TANGO exits 0 on failure**.

**Frame trap handled:** `tango_v_recruited.py` asserts that the profile's residues at the
row's own coordinates equal the row's stored `sequence`, and refuses to score on a
mismatch. All three passed — 93, 34 and 33 residues respectively.
