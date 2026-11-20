# What the row-level bound buys over the dataset-level ones — 20 November 2026

> **The sentence can be written, and the distinction is the enabling condition for an
> exclusion operation that a shared bound cannot support. §8.3 closes; B does not collapse
> into B1.**

---

## The test, as the audit set it

`reports/prior_art_audit_information_limit_2026-11-20.md` §8.3: settle it by *"reading
arXiv:2611.15555 in full ... and arXiv:2605.28873, and writing the one sentence that says
what the row-level version buys. **If that sentence cannot be written, B collapses into
B1.**"* The audit had read B1's abstract and extracted passages only, and called the
distinction *"real and it is thin."*

Both were read in full today from the arXiv HTML.

## What the two prior bounds actually are

**B1 — Malekpouri & Lotfi, arXiv:2611.15555.** Proposition 2 (Feasibility), verbatim:

> *"Conformal p-values satisfy p_j ≥ 1/(n_cal + 1) **for every candidate**. BH at level q
> over m candidates rejects the k-th smallest only if p_(k) ≤ qk/m."*

**The bound is identical for every candidate.** It depends on `n_cal`, a property of the
calibration cohort, and on nothing about the candidate. Their remedy is correspondingly a
property of the study: *"mean power reaches 0.5 only at ρ ≈ 0.99 and n ≈ 200 validated
guides."* **Grow the cohort.**

**B2 — Zhuang, Li & Fan, arXiv:2605.28873.** The paired MDE δ\* is derived from
(*m*, ρ_d, α, 1−β). The per-item differences *D_i* are the **inputs** to a single aggregate
bound, not per-item bounds: *"the mean over m items has variance (ρ_d − δ²)/m."* One δ\*
for the comparison. **Dataset-level.**

**Neither paper contains the words `per-instance`, `per-candidate`, `untestable` or
`admit`, and neither performs any exclusion of individual hypotheses.** B1's single use of
"exclude" is about a genome scan omitting bulges; its single "discard" is about windows
containing non-ACGT bases.

> **A trap worth recording.** A substring search for `Gart` returns **four hits in B1**,
> which looks like it cites Gart, Chu & Tarone. Every one is **List*gart*en** — Jennifer
> Listgarten, a CRISPR researcher. **B1 does not cite the exclusion literature at all.**
> This is the second time today that a literal grep would have produced a confident false
> conclusion; see `CLAUDE.md` rule 1.

## The sentence

| | bound depends on | varies across candidates? | operation it supports | implied remedy |
|---|---|---|---|---|
| **B1** conformal / CRISPR | `n_cal` | **no** — identical for all | go / no-go on the study | grow the cohort |
| **B2** paired MDE / quantization | *m*, ρ_d, α, β | **no** — one δ\* | go / no-go on the comparison | more items |
| **§3.1b** ours | *m*, *M* **of that row** | **yes** — measured 0.0102 to 1.0000 | **select: admit or reject each instance** | recruit differently-*shaped* instances |

> **A shared floor supports only a verdict on the whole study, because discarding
> candidates does not move it. A per-instance floor supports a selection — and that
> selection is exactly the Gart/Chu/Tarone–Mantel–Tukey exclusion of untestable hypotheses,
> which has nothing to operate on when every candidate carries the same bound.**

That is what the row-level version buys: **not a tighter bound, but the applicability of an
exclusion rule.** §3.1b is that rule applied at recruitment.

### A second consequence, and it is measurable

Because the floor varies per instance, **the proportion of testable instances is itself a
measurable property of a field**. Measured today on 82 externally curated fibril cores:
**12% clear the geometry; 1 in 82 also clears the training-set check**
(`results/amylocore_screen_2026-11-20/`). **Neither B1 nor B2 can produce such a number**,
because a bound that does not vary across candidates has no distribution to report. B1
reports a *fraction of splits* with an empty accepted set (96.7%) — a property of the
study repeated, not of a population of candidate instances.

## What this does NOT rescue, stated plainly

**The "arithmetic / pre-run design calculation" framing is not ours and the audit was right
about that.** B1 makes the same rhetorical move independently, nine days before the audit:
a floor from a couple of integers, shown to make the target result impossible for the data
that exist, converted into a design calculation. **Any phrasing that presents that framing
as novel must be struck from the manuscript.**

**And the underlying rule is a century old.** The exclusion is Gart, Chu & Tarone (1979) and
Mantel (1980), crediting Tukey — not ours, and not Tarone 1990's either, as
`reports/tarone_1990_read_2026-11-20.md` records.

> **The honest residue, which is what the manuscript may claim:** *the minimum attainable
> p-value of a benchmark row is fixed by that row's own geometry, computable from two
> integers before any predictor is run; applying the classical exclusion of untestable
> hypotheses at the level of the individual benchmark instance makes the testable fraction
> of a field measurable; in aggregation-predictor benchmarking that fraction is about one in
> eight, and 13 of our 23 scored rows cannot reject at α.* Narrow, derivative in its
> machinery, and — so far as five queries and two full texts can show — not previously done
> in this field.

## Audit status after today

| unknown | status |
|---|---|
| §8.1 max-statistic justified independently? | **CLOSED** — `reports/max_statistic_justification_2026-11-20.md`; stop case does not fire |
| §8.2 is the admissible population non-empty? | **CLOSED** — 10 of 82, against the audit's predicted ~0 |
| §8.3 what does row-level buy? | **CLOSED** — this report |

**All three of the audit's "most dangerous remaining unknowns" are now settled, and none of
them stopped the project.** The claim that survives is narrower than the one that entered
the audit, which is the point of running one.
