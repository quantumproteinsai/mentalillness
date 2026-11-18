# The recruiting rule — PROPOSED, 18 November 2026

**Status: a proposal, not an amendment.** Nothing here is in `PREREGISTRATION.md` and no
row has been relabelled. It needs the author's ratification, and one decision in it is
genuinely the author's to make rather than mine.

---

## What this had to answer

`STATE.md` records, from yesterday, that widening the dataset failed at its purpose: 10 →
21 rows and **the confirmatory cell did not move off 2**. The conclusion written there was
that the recruiting rule must change — *"a search over methods sections, papers that ran a
predictor and reported it failing"*.

**That conclusion was wrong, and this report retracts it.** It was reasoned from the
observation that 12 rows sit at `stratum: PENDING` with no predictor run in their source
paper. The inference — that the stratum therefore has to come from the source paper — does
not follow, and §7 of the pre-registration already says otherwise.

## The rule that is already registered, and was not being applied

§7's amendment of 16 Nov, registered **before any predictor ran**:

> **Every row carries a `stratum` label assigned before scoring**, derived from the
> published predictor results where they exist, and **otherwise from the legacy arm's own
> output** — which means the assignment for new rows is made *after* the legacy run and
> *before* the modern run, and **that ordering is part of the freeze.**

So `PENDING` was never meant to mean "the source paper ran no predictor, so we cannot
say". It means **"the legacy arm has not been run on this row yet"**. For 9 rows it now
has been. The label simply was not applied afterwards.

### What applying it would give

`DISCORDANT` iff TANGO *v* ≥ 0.05 — the §4 recovery bar, fixed before any run. The rule is
mechanical: no threshold is chosen here, and no row is judged by eye.

| row | TANGO *v* | current | mechanical call | |
|---|---|---|---|---|
| TRIOBP-1 1-59 | 0.9995 | PENDING | DISCORDANT | **enters** |
| DISC1 748-769 | 0.9227 | PENDING | DISCORDANT | **enters** |
| TMEM106B 120-254 | 0.7156 | PENDING | DISCORDANT | **enters** |
| ANXA11 39-74 | 0.4134 | PENDING | DISCORDANT | **enters** |
| DISC1 384-415 | 0.3189 | DISCORDANT | DISCORDANT | already in |
| glycinin G4 164-190 | 0.1645 | PENDING | DISCORDANT | **enters** |
| TRIOBP-1 324-348 | 0.1235 | DISCORDANT | DISCORDANT | already in |
| DISC1 691-836 | 0.0812 | PENDING | DISCORDANT | **enters** |
| TRIOBP-1 333-340 | 0.0388 | PENDING | **CONCORDANT** | becomes a positive control |

**Confirmatory set: n = 2 → n = 8.** Minimum attainable one-sided Wilcoxon p: 0.25 → 0.0039.
§4's threshold becomes reachable for the first time.

## THE PROBLEM, AND IT IS THE AUTHOR'S DECISION

**The ordering that §7 calls "part of the freeze" has already been broken.** Stratum was
to be assigned after the legacy run and *before* the modern run. On 17 Nov both arms ran
and no labels were applied in between, so **every one of these rows' AggrescanAI scores
is already known.** Assigning the stratum now is post-hoc.

**The argument that it is still safe**, stated as strongly as it deserves: the rule is a
deterministic function of the legacy *v* and a threshold, both fixed before any number
existed. Knowing the modern score grants no freedom in applying it — there is no
threshold to tune and no row to pick. The ordering requirement exists to remove analyst
discretion, and here there is none left to remove.

**The argument against, which I think is the stronger one**: discretion has not vanished,
it has moved. It now sits in *whether to apply the rule at all* — a choice being made
after seeing that applying it takes n from 2 to 8 and makes the headline test capable of
firing. That is the exact shape `CLAUDE.md` warns against: *scoring first and choosing
the statistic afterwards produces a result that looks convincing and means nothing.*

**Recommendation.** Apply it, and label the result **EXPLORATORY under §12** — never as
the confirmatory statistic. Report both: n = 2 confirmatory as frozen, and n = 8
exploratory with the ordering breach named in the same sentence as the p-value. The
dataset keeps the labels, because they are correct under a registered rule; the
*confirmatory* claim does not get to use them.

**What I will not do without the author saying so:** relabel the rows and present the n = 8
result as confirmatory. That is the decision I am handing over.

### And n = 8 is not n = 8

Of the 8 rows, **3 are DISC1 and 2 are TRIOBP-1**. Checked rather than asserted:
**691-836 wholly contains 748-769**, while 384-415 is disjoint from both. So one DISC1
pair is nested and the third interval is separate — but all three are scored on the same
profile of the same protein by the same tool, which is enough to break independence
without any overlap at all. Five distinct proteins:

| unit | n | min attainable p |
|---|---|---|
| rows | 8 | 0.0039 |
| **proteins** | **5** | **0.031** |

Stouffer's Z and the Wilcoxon both assume independent pairs. **Overlapping intervals of
one protein scored by the same tool on the same profile are not independent** — they
share residues, and in the worst case share their best-scoring tile. Treating them as 8
is the kind of margin-versus-error-bar failure `CLAUDE.md` rule 2 exists to stop.

**So the honest unit is the protein, n = 5**, and §4's threshold is *just* reachable
(0.031 < 0.05) with no margin at all. One protein fewer and it is unreachable again.

---

# THE RECRUITING RULE

**Recruit one row per NEW protein, from post-2020 structural work, and resolve its stratum
from our own legacy run before the modern arm is allowed to see it.**

### Why not "search methods sections for reported predictor failures"

1. **It selects on the outcome.** Recruiting rows because a paper reported a predictor
   failing, then reporting how often predictors fail, is circular. The post-2020 route
   selects on *date and method*, which are independent of how any predictor scores.
2. **Publication bias runs both ways and is unmeasurable.** A paper mentions a predictor
   when the result is notable — a striking failure, or a tidy confirmation. Papers where
   prediction was run and was unremarkable say nothing. The sampling fraction is unknown.
3. **It imports someone else's threshold.** Each paper calls "agreement" by its own
   criterion and its own tool version. Stratum assigned that way is not comparable across
   rows. Our own legacy run applies **one tool, one parameter set, one bar** to every row.
4. **It is rarer than the alternative and gets smaller over time.** Structural papers
   increasingly do not run aggregation predictors at all.

**This supersedes the open item in `STATE.md` dated 17 Nov.**

### Inclusion criteria, all required

1. **A new protein.** Not a second interval of a protein already in the set. The unit of
   independence is the protein; a second interval adds rows without adding power.
2. **Region mapped after 2020**, which makes it CPAD-absent by construction (CPAD 2.0 is
   frozen at 2020) — still subject to the orthologue check, which the homologue-transfer
   route requires separately.
3. **No aggregation predictor in the discovery path** → `circularity_status: CLEAN`.
   Cryo-EM, ssNMR and unbiased experimental scanning qualify; a deleted predicted segment
   does not.
4. **Fragment-level resolution**: an ordered core or a mapped necessary region, not
   "this protein aggregates".
5. **A frame fixed and sequence-verified before scoring**, with any non-aggregating
   hydrophobic segment (signal peptide, TM helix) excluded from the scored chain — the
   decoy-window rule.
6. **The source read as a publisher PDF**, including its SI where a claim rests on it.

### The ordering, which is the part that must not slip again

```
recruit row  ->  freeze frame + sequence  ->  RUN LEGACY (TANGO)
             ->  ASSIGN STRATUM mechanically (v >= 0.05 -> DISCORDANT)
             ->  COMMIT the label  ->  only then run the modern arm
```

**The stratum label must be committed to git before `run_aggrescanai.py` is invoked on
that row.** That is checkable after the fact from the commit graph, which is what makes
it a constraint rather than an intention. It is the discipline that was lost on 17 Nov,
and losing it is what cost the 8 rows above their confirmatory standing.

*Worth building, if this is ratified:* a check in `score_rows.py` that refuses to report
a modern score for a row whose `stratum` is still `PENDING`. A warning in prose is not a
constraint.

### Where to look

Post-2020 cryo-EM of **ex vivo** fibrils is the richest seam: every such structure is a
new core, CPAD-absent by date, and found by density rather than by prediction. TMEM106B
and ANXA11 both arrived this way. Systemic amyloidoses, patient-derived deposits, and
non-human or non-disease aggregates (glycinin is the precedent) widen the protein pool
beyond the classic amyloids that are mostly CPAD members already.

### How many are needed

To reach **n = 5 independent proteins** in the confirmatory cell under a clean ordering:
**five new proteins**, since none of the existing 8 rows can carry confirmatory standing
if the recommendation above is followed. At roughly one protein per row and the care each
row has taken, that is the real scope of the outstanding work.

### What this does not fix

- **It does not make the Δv contrast fair.** Selecting rows where legacy missed biases the
  head-to-head *toward* modern. Modern is currently losing 7 of 9 anyway, which makes that
  negative stronger, not weaker — but the contrast must carry the caveat.
- **It does not resolve `stratum` being a property of a (region, predictor) pair.** With
  one legacy tool the question does not arise; it returns the moment a second legacy tool
  runs.
- **It does not settle the four recorded pre-registration defects**, including the tiling
  phase, which remain recorded and unpatched.
