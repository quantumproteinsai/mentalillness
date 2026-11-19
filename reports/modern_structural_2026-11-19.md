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

## 1. Orb2 — the largest generational difference in the project, and it still does not clear the bar

TANGO scored the best window inside the core at **exactly 0.0000**, ranked **87th of 117**.
AggrescanAI ranks the same region **4th of 117**. *v* falls from 0.9717 to **0.1144**.

That is a direct, quantitative answer to this project's headline question for one row —
*do modern predictors recover what the 2004-2010 generation missed?* — and for Orb2 the
answer is **most of the way, but not past the bar**. §4 requires *v* < 0.05; the floor at
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

## 3. THE CAVEAT THAT GOVERNS BOTH ROWS: neither has been checked against CPAD

**`cpad_status` is `UNCHECKED` for Orb2 and for β2-microglobulin.** AggrescanAI's five MLPs
are trained on CPAD90. Until both are checked against all three CPAD 2.0 tables — by name,
by accession, and through the orthologue route, as §5.2b item 4 requires and as was done
for DISC1 and TRIOBP-1 — **neither number above can be interpreted.**

This bites hardest exactly where the result is most interesting. **β2-microglobulin is a
classical amyloid protein with decades of literature; an entry in an aggregation database
is the expected case, not the surprising one.** If it is in CPAD90, AggrescanAI's rank-1
placement is partly recall, and the comparison against TANGO stops being a comparison of
generations and becomes a comparison of training-set membership. Orb2 is a *Drosophila*
functional amyloid and less likely to be present, but "less likely" is not a check.

**No interpretive claim should be made from §1 or §2 until this is done.** The numbers
stand; their meaning does not.

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
