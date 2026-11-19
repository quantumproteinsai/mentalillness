# Pre-registration — do modern predictors recover the experimentally mapped regions?

**STATUS: DRAFT, 15 Nov 2026. NOT YET IN FORCE.** Written by Claude, for the author to
amend, reject or ratify. Nothing in this document binds anything until §12 is signed and
the freeze commit exists.

**All three open decision points were resolved on 15 Nov 2026 by Claude, on the author's
instruction**, and each is marked **RESOLVED** at the point of use with the reasoning
attached: the combination statistic (§3.1), the handling of a FoldAmyloid
reimplementation that fails its own checks (§5.1), and the entry rule for modern
predictors (§5.2). **The author should read those three and overturn any of them — they
are judgement calls delegated, not facts established**, and a pre-registration is worth
nothing if its author has not actually agreed with it.

Read `STATE.md` first. This document assumes it.

---

## 1. The question

> Do modern aggregation predictors recover the experimentally mapped
> aggregation-critical regions of DISC1 and TRIOBP-1 that the 2004-2010 generation
> missed, and if not, what structural feature are they all missing?

**What is not being asked.** That the 2017-generation tools failed on these proteins is
already in print, stated by the primary papers themselves. It is cited evidence, not a
result to re-establish. Any analysis below that merely reproduces a published failure is
a positive control on our pipeline, not a finding.

## 2. Hypotheses, stated so they can fail

- **H1 (primary).** Modern sequence-only predictors rank the mapped region above chance
  within its own parent protein.
- **H0 (primary).** They do not: the mapped region's score is indistinguishable from
  that of ordinary windows of the same protein.
- **H2 (secondary).** Any failure is a *flanking-context* effect rather than core
  chemistry — i.e. the narrowed core scores positive in isolation and negative in
  context.
- **H3 (secondary, RETIRED AS A NOVELTY CLAIM 16 Nov 2026).** Aggregation-critical
  psychiatric regions are gatekeeper-rich relative to crystallised steric zippers.
  Demoted to n = 1 on 15 Nov; **retired as a claim of novelty on 16 Nov**, because the
  paradox is published for tau and resolved there — see §9.1. It is retained as
  **descriptive context with citations**, and may not be presented as a finding.
- **H4 (PROMOTED 16 Nov 2026 — the claim this project now rests on).** A window-scanning
  predictor fails to rank a mapped region **even when that region contains a
  zipper-grade, low-gatekeeper window that the predictor is built to detect** — in a case
  structurally identical to one where the same predictors succeed.
  - **Positive control, built in: tau.** Global 35.6% gatekeeper, local PHF6 16.7%,
    and the predictors *find* it.
  - **Test case: TRIOBP-1 324-348.** 48.0% gatekeeper, contains a **0%** hexapeptide,
    and the predictors *missed* it.
  - **H0 for H4.** The failure tracks window-level composition — i.e. predictors miss
    regions whose best window is not zipper-grade, and the TRIOBP-1 case is not
    distinguishable from that.
  - **This is a claim about prediction, not about composition**, which is why tau
    pre-empts H3 without touching H4.

---

## 3. The statistic, and why a hit/miss criterion is forbidden

**A binary "did it flag the region?" criterion is uninformative and must not be used.**
Computed on our own proteins `[COMPUTED 15 Nov 2026]`, the probability that a predictor
calling a fraction *f* of residues positive **at random** overlaps the mapped region at
least once:

| protein | length | region | f = 0.05 | f = 0.10 | f = 0.20 | f = 0.30 |
|---|---|---|---|---|---|---|
| TRIOBP-1 | 652 | 25 aa | 63.8% | 86.9% | 98.3% | 99.8% |
| DISC1 | 854 | 32 aa | 74.6% | 93.6% | 99.6% | 100.0% |

At any realistic call rate a random predictor "recovers" either region essentially
always. **Rank is mandatory.**

A naive rank threshold is not much better: for a 20-window region in a ~650-window
protein, the chance that its best window lands in the top 1% is **18.2%**, top 5%
**64.2%** `[COMPUTED]`. So the threshold must be calibrated against a null that accounts
for region length.

### 3.1 The pre-registered primary statistic

For each row *i* (one mapped region in one protein) and each predictor:

1. Score every window of the protein at the predictor's own native window size (§5.3).
2. Let **M** = number of windows in the protein, **m** = number of windows wholly inside
   the mapped region.
3. Let **P** = (number of windows scoring **≤** the region's best-scoring window) / M.
   Ties resolved by the **midrank** convention.
4. Define **v = 1 − P^m**.

Under H0 (the predictor carries no information about this region), the region's *m*
windows are an exchangeable subset, the best-of-*m* percentile has CDF *x^m*, and
therefore **v ~ Uniform(0, 1)**. Small *v* means the region scored high — the predictor
succeeded.

This transformation is the reason for the whole construction: it makes a 25-residue
region in a 652-residue protein and a 32-residue region in an 854-residue protein
directly comparable, with no tuning.

### 3.1b The information limit m/M — AMENDMENT, 18 Nov 2026, POST-UNBLINDING

**This amends no formula. It records a bound that was always true of §3.1, states that
nobody computed it, and fixes a recruitment criterion so the bound stops being violated.**

**The bound.** Under H0 the chain's top-ranked window falls inside the region with
probability **exactly m/M**. The smallest p any rank-based statistic can return for that
row is therefore **m/M**. Not this statistic — *any* of them. Amending §3.1 cannot move
it, because it is a property of the data, not of the transformation applied to them.

**What it implies for §4.** Where **m/M > 0.05**, §4's recovery criterion (v < 0.05)
**cannot fire**. "The predictor missed this region" is then true by arithmetic before any
software runs, and it is true in the direction of this project's own H1.

**What was found on 18 Nov 2026, after the modern arm had run:**

- **13 of 23 scored rows have m/M > 0.05.** TMEM106B 120–254 is 0.489, serum amyloid A
  2–55 is 0.471, CHCHD10 42–75 is 0.217.
- **Only 10 of the 23 scored rows can ever reach p < 0.05 under any rank-based test**
  (11 of all 24, counting the row excluded from scoring). *Corrected 18 Nov 2026: this
  first read 7 of 20, before the §3.1a short-region rows were given their sliding-pool
  m = 1 instead of a tiling m = 0.*
- A weaker, formula-specific consequence: v cannot fall below
  **1 − ((M−0.5)/M)^m**, which exceeds 0.05 for **9 of 23** rows, and where that floor is
  attained v is **anti-conservative by 2.1×** (CHCHD10 reports v = 0.104 where the
  calibrated p is 0.218 = 5/23).
- **Both founding confirmatory rows pass**, narrowly: DISC1 384–415 at **0.0352** and
  TRIOBP-1 324–348 at **0.0370**. The project's own question remains answerable.

**That this was never computed is the finding, not the bound.** m/M needs the chain length
and the region length and nothing else. It was available on day one, it is available from
an abstract, and it costs no compute. It was not computed until after three rows had been
recruited, read, verified, scored on both arms and committed. Applied at stage 1 it would
have rejected all three.

**REGISTERED FOR ALL FUTURE ROWS, and it binds recruitment rather than analysis:**

> **A row is `power_eligible` iff m/M ≤ 0.05.** This is checked at **stage 1** of the
> recruitment pipeline, before the paper is read in full, and a candidate that fails it is
> rejected with the ratio recorded.

**Rows already in the dataset are NOT removed.** They are labelled, reported, and excluded
from any statistic that uses §4's recovery criterion. Removing them after seeing the
scores would be exactly the post-hoc selection this document exists to prevent; labelling
them is not. The `power_eligible` flag and the m/M ratio are carried on every row.

**What is NOT licensed by this amendment:**

- no change to v, to W, to the tiling, or to §4's threshold;
- no re-reporting of any existing result with the failing rows silently dropped — where a
  statistic is recomputed on the eligible subset, both versions are shown;
- no claim that a `power_eligible: false` row shows a predictor failing. For those rows
  **the benchmark has no opinion**, and saying so is the only honest report.

**The consequence for recruitment is a change of literature, not of standards.** m/M ≤
0.05 wants a **long protein with a short mapped region**. Recent cryo-EM fibril-core
papers systematically yield the opposite — a short protein whose ordered core is a large
fraction of it — so that pool is close to exhausted for this purpose. Deletion and
truncation mapping on large proteins is the pool that produces eligible rows, and it is
also the pool that produces necessity claims rather than mere ordered cores. DISC1 and
TRIOBP-1 came from it.

### 3.1a Short regions — AMENDMENT, 17 Nov 2026, POST-UNBLINDING AND THEREFORE EXPLORATORY

**Scores had been seen when this was written.** §12 says an amendment made after
unblinding is an exploratory analysis and is reported as one. **So every value produced
by this rule is exploratory, is reported separately, and enters no confirmatory
statistic**, now or later.

**The defect.** §3.1 counts windows *wholly inside* the region. At the native window of 6
(§5.3) a region shorter than 6 residues admits none, and a 6-to-11-residue region admits
one only if the tiling happens to align with it. Those rows are not scored low — they are
**not scored at all**. Four rows are affected:

| row | length | stratum | why it matters |
|---|---|---|---|
| tau 306-311 (VQIVYK) | 6 | CONCORDANT | CPAD member |
| tau 275-280 (VQIINK) | 6 | CONCORDANT | CPAD member |
| TRIOBP-1 324-328 | 5 | PENDING | — |
| TRIOBP-1 333-340 | 8 | PENDING | — |

**This was found by running the statistic, not by reading it.** The two tau rows are the
ones that demonstrate the pipeline works at all — the top 12 residues of the whole
441-residue protein are exactly those two hexapeptides — and they are precisely the rows
§3.1 cannot score. A benchmark that cannot score the canonical amyloid hexapeptide is
reporting a property of its own window arithmetic.

**The rule.** When the registered tiling yields *m* = 0, score the region as **one window
of its own length L**, ranked against **all** same-length windows of the protein:

> *M* = *L*ᴾ − *L* + 1 windows; *m* = 1; *P* = (windows scoring ≤ the region's own
> window) / *M*, midrank; **v = 1 − P**.

**Why this preserves §3.1's stated null, where a sliding window did not.** The objection
to sliding windows is that overlapping windows are not independent, so best-of-*m* is not
distributed as *x^m*. **That objection does not apply at m = 1.** The rank of a *single*
window among identically-distributed windows is uniform under exchangeability alone;
correlation between windows is irrelevant. Verified by simulation on i.i.d. scores, 4000
draws each:

| region length / protein | mean v | q10 / q25 / q50 / q75 / q90 | frac v < 0.05 |
|---|---|---|---|
| 6 in 441 | 0.497 | 0.095 / 0.240 / 0.499 / 0.749 / 0.898 | 0.052 |
| 5 in 652 | 0.497 | 0.101 / 0.249 / 0.496 / 0.746 / 0.900 | 0.051 |
| 8 in 652 | 0.504 | 0.108 / 0.264 / 0.506 / 0.747 / 0.897 | 0.049 |
| **expected** | **0.500** | **0.100 / 0.250 / 0.500 / 0.750 / 0.900** | **0.050** |

**The rule applies ONLY where m = 0.** It is not an alternative statistic to be preferred
where both are defined, and it must never be used because it gives a better answer: the
two are not interchangeable, since v at m = 1 cannot reach the small values m > 1 allows.

**It cannot change the confirmatory result, and that was checked before any value was
computed with it.** All four affected rows are either CPAD members excluded under §5.2b
item 5 (both tau rows) or `stratum: PENDING` and outside the confirmatory set (both
TRIOBP-1 rows). **The confirmatory set remains DISC1 384-415 and TRIOBP-1 324-348, n = 2,
untouched.** Had this amendment been able to move the headline number, it should not have
been made after unblinding at all.

**Combination across rows — RESOLVED 15 Nov 2026, by Claude on the author's instruction.**

**Primary: Stouffer's Z**, equal weights, one-sided.
**Secondary, always reported alongside: Fisher's method**, χ² = −2 Σ ln(v_i) on 2n df.

Fisher is the conventional choice and is more powerful when one row is recovered
spectacularly and the rest are not. **That is exactly this project's recurring failure
mode** — on 15 Nov 2026 a two-protein gatekeeper claim turned out to rest on one protein
plus an excluded row (§9), and H1 is a claim about predictors *in general*, not about
there existing one region somewhere that a predictor finds. Stouffer weights rows
equally and cannot be carried by a single outlier, so it is primary.

Both are reported in every case, because a referee will expect Fisher and because a
disagreement between them **is itself informative**: Stouffer null with Fisher
significant means one row is doing all the work, and the paper must say which row.

### 3.2 The legacy-versus-modern comparison

The generations are run on **the same rows**, so the comparison is **paired**:
Wilcoxon signed-rank on per-row *v*, modern against legacy, one-sided (modern better).
Reported with the median paired difference and its 95% CI, never as a bare p-value.

---

## 4. Success thresholds, fixed now

| | threshold |
|---|---|
| A single row counts as **recovered** by a predictor | **v < 0.05** |
| A predictor counts as **succeeding on the set** | Fisher combined p **< 0.01** across the confirmatory rows |
| Modern counts as **beating legacy** | Wilcoxon one-sided p **< 0.05** *and* median paired Δv **< −0.10** |
| Multiplicity across predictors | **Benjamini-Hochberg at q = 0.10**, applied across all predictors within each family (legacy, modern), reported alongside raw p |

The effect-size floor on the paired comparison is deliberate: a significant p with a
median Δv of −0.01 is a null result with a small standard error, and this project does
not report those as findings.

---

## 5. The predictors, frozen

### 5.1 Legacy generation (the 2017 baseline)

| tool | status **16 Nov 2026**, content-verified | how it will be run |
|---|---|---|
| **TANGO** (Fernandez-Escamilla 2004, *Nat Biotechnol* 22:1302) | **LIVE at `https://tango.crg.es/`**, academic licence, registration required. **The protocol matters**: `http://` serves a CRG maintenance page. **Not** the image-analysis TANGO at `biophysique.mnhn.fr/tango` | **LOCAL EXECUTABLE under academic licence** (author decision, 16 Nov 2026) — **version-pinnable, therefore reproducible**. Record the version string and the exact invocation, not web-form settings |
| **AGGRESCAN** | **LIVE**, redirects to `andromeda.uab.cat/bioinf/aggrescan/` | web, settings recorded verbatim |
| **FoldAmyloid** | **server dead**, both hosts return 000 | **reimplemented** from Garbuzynskiy 2010 + the scales in Galzitskaya 2006b |
| **ProA** | **DEAD.** `abl.ku.edu/ProA/` now returns **HTTP 200 by silently redirecting to the lab homepage** `mgm.ku.edu` | **cannot be run. Recorded as unavailable, not as a failure.** |

**TANGO IS NOW A LOCAL TOOL, WHICH REMOVES THIS SECTION'S OWN OBJECTION TO IT.**
§5.2 excludes web services from the confirmatory arm because *"a web form is not
a reproducible tool — it cannot be version-pinned."* On 16 Nov 2026 the author
obtained TANGO under an **academic licence as a downloadable program**, so that
objection no longer applies to it: the run becomes version-pinnable and
repeatable. **AGGRESCAN is now the only web-only tool left in the legacy arm**,
and its lack of a version string is a stated limitation rather than an oversight.

**What §12 step 4 must capture for TANGO**, given it is now local: the **version
string** of the downloaded program, the **platform and date obtained**, the
**exact command line or parameter set**, and the **licence type** under which it
was obtained. A version-pinnable tool is only reproducible if the pin is actually
written down.

**STATUS-CODE CHECKING IS NOT ENOUGH, AND THREE OF THESE FOUR PROVE IT.** A
naive `curl -o /dev/null -w '%{http_code}'` sweep on 16 Nov 2026 returned **200
for TANGO and 200 for ProA**, and would have recorded both as available. TANGO
serves a 404 page under a 200 status; ProA redirects to a generic lab homepage.
**Only fetching the body and looking for the tool's own name distinguishes a live
server from a tombstone.** Any future availability check in this project must
verify content, not status, and must record the final URL after redirects.

**So two of the four legacy tools are usable right now** (TANGO and AGGRESCAN). That is worse than §5.1
assumed on 15 Nov, and it is the strongest possible restatement of this section's
own rule that *a web form is not a reproducible tool*.

#### 5.1a The legacy arm does not need to be re-run — REGISTERED 16 Nov 2026

**The collapse of the legacy servers turns out not to block the benchmark, because
every discordant row already carries a PUBLISHED legacy run, with the tools
named:**

| row | published legacy run | tools named |
|---|---|---|
| TRIOBP-1 324-348 | Bradshaw 2014, *PLoS ONE* 9:e111196 | AGGRESCAN, FoldAmyloid, ProA, TANGO — **all four**, with thresholds and URLs |
| FUS 39-95 | Murray 2017, *Cell* 171:615 | eight tools, every parameter published |
| hnRNPA1 251-295 | Sharma 2023, *JMB* 435:168211 | seven tools, false positives quantified |
| DISC1 384-415 | Zaharija 2025 thesis §4.3.5 | five tools |

**Registered consequence:** the legacy arm for the discordant stratum is taken
from the **published** runs, cited, not re-executed. Our own runs are attempted
where a server is live, and reported as **corroboration** where they agree and as
a **discrepancy** where they do not.

**This is not a convenience.** It is more defensible than re-running: the
published runs were done on the contemporaneous servers by the groups that
mapped the regions, which is the comparison the project's premise actually rests
on. Re-running a 2026 server and calling it "the 2004-2010 generation" would be
the weaker claim.

**What still must run is the MODERN arm** (§5.2), which is the untested part and
the whole point. Its version-pinnable-and-local rule now looks like the single
most load-bearing decision in this document.

**The FoldAmyloid reimplementation is itself a pre-registered object.** It must reproduce
the paper's own published checks before it may score our rows: the reported 80%/72%
sensitivity/specificity on its 407-peptide set, and the protein-level result that **only
the contact scale finds tau 306-311**. **A SECOND, INDEPENDENT CHECK ADDED 16 Nov 2026,
from the Murray 2017 version of record.** That paper publishes a fully parameterised
FoldAmyloid run on FUS-LC residues 2-214 — `scale = "Expected number of contacts 8 Å"`,
`averaging frame = 5`, `threshold = 21.4`, at `bioinfo.protres.ru/fold-amyloid` — and its
Figure S7 panel shows the score oscillating roughly between 16 and 21 across all 213
positions and **never crossing threshold: zero positive predictions on the entire
sequence.** Our reimplementation must reproduce that curve. It is a **sharper** check than
a sensitivity/specificity figure, because it is a whole-curve comparison on a named
sequence that is also one of our rows. **RESOLVED 15 Nov 2026, by Claude on the author's instruction — and the answer is
neither of the two options originally offered.** If the reimplementation fails those
checks it is **excluded from the confirmatory legacy arm**, so that a bug in our code can
never masquerade as a 2010 tool's failure and contaminate the legacy-versus-modern
comparison. It is **reported in full anyway**, as a methods result, with the discrepancy
quantified against the paper's published figures.

Dropping it silently would hide a result; labelling it "FoldAmyloid" while unvalidated
would attribute our bug to Garbuzynskiy. The legacy arm then has **two live tools plus
one that could not be reconstructed**, which is a weaker comparison and must be stated as
one. That the method is fully specified in print and still could not be reproduced would
be the sharpest reproducibility finding available to this paper.

### 5.2 Modern generation

**AggreProt** (2024, installable Python) and **AggrescanAI** (2026, Colab + pretrained
weights), both sequence-only. Versions and commit hashes recorded in the freeze commit.

**RESOLVED 15 Nov 2026, by Claude on the author's instruction — as a rule rather than a
list**, so that the answer does not change every time a tool appears:

> **A predictor enters the confirmatory modern arm only if it is version-pinnable and
> runs locally.** Everything else is exploratory, reported separately, and excluded from
> the multiplicity correction.

That criterion is not invented here — it is this project's own finding, recorded in
`prior_computation_and_framing.md`: *"a web form is not a reproducible tool — it cannot
be version-pinned, and three of the services checked today were down or gone."* A
benchmark whose baseline evaporates between submission and review is not a benchmark, and
half the 2017 legacy set has already evaporated.

By that rule AggreProt and AggrescanAI are in, and the remaining eleven-plus PLM-era
tools from the September 2026 census are exploratory unless they ship installable
weights. **MEMBERSHIP SUPERSEDED 16 Nov 2026 — see §5.2b. The
rule below is unchanged; AggreProt fails it.** **Any tool meeting the rule may be added freely before the freeze and none
after.** The novelty claim — that no PLM predictor has ever been run on DISC1 or
TRIOBP-1 — is unaffected either way, since it concerns the class, not our coverage of it.

### 5.2b The confirmatory modern arm is ONE tool — REGISTERED 16 Nov 2026

**The rule in §5.2 is not relaxed. AggreProt fails it.**

Its code is public (GitHub, Zenodo v1.0) but its trained weights are not. The README
instructs `unzip nnap-data.zip`, never says where that archive is, and it is in neither
the repository nor the 22.9 kB Zenodo release. The paper's entire data-availability
statement points at the web server. **It therefore cannot be run locally at all**, and is
recorded as **UNAVAILABLE, not as a failure** — the same treatment ProA receives in §5.1.
Evidence: `reports/modern_arm_local_runnability_2026-11-16.md`. A request for the archive
was sent to the corresponding authors on 16 Nov 2026
(`correspondence/2026-11-16_aggreprot_weights_request.md`).

> **Registered: the confirmatory modern arm is AggrescanAI alone.**

#### What this costs, stated rather than buried

**The headline question in `CLAUDE.md` asks about a *generation* of predictors. One tool
cannot answer a question about a generation.** The claim is therefore narrowed, now,
before any score exists:

- **Permitted:** *a PLM-based predictor, AggrescanAI, does / does not recover these
  regions.*
- **Not permitted:** *modern predictors do / do not recover these regions.*

The title and abstract must carry the narrower form. **This is a real loss of scope and
is not to be recovered by rhetoric later.**

#### Consequences for the statistic

1. **There is no multiplicity correction across modern tools, because there is one.**
   Stouffer's Z and Fisher's combination still run **across rows** exactly as §3.1
   registers. Nothing in the per-row machinery changes.
2. **The legacy-versus-modern contrast becomes one-against-one per row**, not an ensemble
   contrast. Any between-generation statement must be worded accordingly.
3. **n = 1 means a tool-specific result cannot be distinguished from a generational one.**
   Where AggrescanAI succeeds or fails, the report says *AggrescanAI*, never *modern
   methods*.

#### Training-set contamination, registered before scoring

Navarro 2026 [READ] states AggrescanAI's shipped model is the **CPAD90** ensemble: CPAD
2.0 **plus homologues** transferred via HoTIDP from OrthoInspector and OmaDB. The
membership list is not published.

**Registered:**

4. **Every row is checked against CPAD 2.0 before scoring**, and the result recorded per
   row. Absence from CPAD is **not** sufficient — a row whose protein has an orthologue in
   CPAD is flagged `TRAINING_SET_UNCERTAIN`.
5. **Confirmatory analysis runs on rows that are not CPAD-implicated.** CPAD-implicated
   rows are reported separately and are **excluded from the primary statistic**, because a
   hit on a training protein is recall, not prediction.
6. **If that exclusion empties the discordant stratum, the confirmatory analysis does not
   run** and the project reports the contamination as its result. Said now so it cannot be
   relitigated once the numbers are visible.

*Expected, not assumed:* the discordant stratum is DISC1 and TRIOBP-1, psychiatric
scaffold proteins unlikely to appear in an amyloid-curated database. **That is a
prediction to be checked under 4, not a reason to skip it.**

#### Item 4 EXECUTED AND COMPLETE — 17 Nov 2026

All 17 rows checked against CPAD 2.0 before any predictor was scored, orthologue check
included. Result recorded per row in `cpad_status` / `cpad_basis` / `cpad_checked`, and
in full under `_CPAD_MEMBERSHIP_CHECK_2026-11-17` in `data/regions.json`.

**All three CPAD datasets were read complete** and each matched the database's own stated
total: APR protein list (286 names), peptide table (2031/2031, contiguous), structures
table (565/565).

**The orthologue check is what makes an absence mean anything**, since CPAD90 enters
AggrescanAI's training set by transferring annotations to *homologues*. Both sources
Navarro names were queried. DISC1: one human protein in its group — itself. TRIOBP: two,
Q9H2D6 and **Q6WCQ1 (MPRIP)**, and that paralogue was checked in its own right and is
also absent. **OMA alone would have missed MPRIP**; one orthology database is not enough.

**The prediction above held: TRIOBP-1 and DISC1 are absent.** The cost falls on the
discordant stratum. Of its 5 rows, **3 are excluded** under item 5 as CPAD members
(FUS 39-95, hnRNPA1 251-295, LECT2 55-75) and **2 survive** (TRIOBP-1 324-348,
DISC1 384-415). No row carries `TRAINING_SET_UNCERTAIN`.

**One dataset is not CPAD.** hnRNPA1 is absent from the APR list *and* the peptide table
and present three times in the structures table; LECT2 is the mirror image, APR list only.
Checking a single table would have cleared both wrongly. Any row added later must be
checked against all three.

**Item 6 does not fire** — the stratum is not empty. But the confirmatory discordant set
is **n = 2**, both rows from the two proteins this project exists to ask about. Against
Navarro 2026's uncertified AUROC separation (0.69 vs 0.60, **no confidence intervals**)
that supports **a case series on two proteins, not a rate**. The write-up must not
promote it.

**What remains uncertain, and will stay so.** The CPAD90 membership list is unpublished,
so no row may be called training-set-clean in absolute terms. `CPAD_ABSENT_ORTHOLOGY_CHECKED`
is the strongest claim public sources support, and it is not a certificate.

#### Re-admission

7. **If the AggreProt weights arrive before the freeze, it is admitted** under §5.2's
   unchanged rule and this section is amended with the date.
8. **If they arrive after the freeze, it is exploratory**, reported separately, excluded
   from the confirmatory claim, with the date of receipt stated. **A pending email does not
   delay the freeze.**

### 5.2a A no-call is not a low score — REGISTERED 16 Nov 2026

Murray 2017's Figure S7 legend states that for ZipperDB **"dotted red lines span segments
where proline residues preclude a prediction."** **ZipperDB structurally cannot evaluate a
proline-containing window — it returns nothing, not a low value.**

This is a mechanism, not a performance problem, and it bears directly on **H4**: TRIOBP-1
324-348 contains **four prolines in 25 residues**, so a tool behaving this way has blind
spots across that region *by construction*. **A predictor that cannot score the windows in
question is not making a wrong prediction; it is making no prediction**, and the two must
not be reported as the same thing.

**Registered before any run:**

1. **Every tool in both arms is checked for no-call behaviour** (prolines, length limits,
   composition filters) **before scoring**, and the behaviour is recorded per tool.
2. **A no-call is not a tie and is never silently midranked** in the `v = 1 − P^m`
   statistic. Where a predictor cannot score a window, that window is **excluded from both
   M and m**, and the exclusion count is reported per row per tool.
3. **If a tool cannot score a majority of a region's windows, it is reported as
   INAPPLICABLE to that row, not as a failure on it.** Scoring a tool as having missed a
   region it was never able to evaluate would be the mirror image of the circularity this
   project exists to avoid.

### 5.3 Window size and score normalisation

Each predictor is scored at **its own native window**: FoldAmyloid 5, Waltz/3D-profile
6, TANGO and AGGRESCAN per-residue (aggregated to 6-residue means), PLM tools per-residue
(aggregated to 6-residue means). **The statistic in §3.1 is invariant to window size by
construction**, which is why no cross-predictor rescaling is applied. Raw per-residue
outputs are archived.

---

## 6. The validation set, and what may enter it

### 6.1 Two tiers, never pooled

- **Tier A — confirmatory.** DISC1 and TRIOBP-1 only. This is the project's question.
  **n = 2 proteins. It is a case study, not a test** — see §7 — and must be reported as
  such regardless of outcome.
- **Tier B — powered generalisation.** Every protein with fragment-level aggregation
  mapping, psychiatric or not. This is where a real recovery rate can be estimated.

Tier A and Tier B are analysed and reported separately. **Pooling them would let a
40-row Tier B result speak for a 2-row Tier A question.**

### 6.2 Inclusion rules

A row enters the confirmatory analysis only if **all** of the following hold:

1. `found_by` records discovery by **experiment, not prediction**. Rows found by
   prediction are analysed **separately** and never pooled (§8).
2. `construct` is recorded. A region may be necessary in one construct and dispensable in
   another, and **both results are correct**; a benchmark that ignores this scores against
   a moving target.
3. The **sequence** has been read from a primary source or a database, not inferred.
4. The **residue range** has been checked against the frame recorded in `_numbering`.
5. `verified_against_publisher_pdf` is **true**.

### 6.3 Both Tier A rows now pass rule 5

**Updated 16 Nov 2026. Both blockers cleared in one day, each by a source this section
had not named.** The confirmatory analysis is no longer blocked on provenance.

| row | sequence | range | status |
|---|---|---|---|
| TRIOBP-1 324-348 | ~~DERIVED~~ **READ** — Zaharija 2022 Fig. 1B | **READ** — Zaharija 2022 §2.2 | **CLEARED** |
| DISC1 384-415 | **READ** — UniProt Q9NRI5, 854 aa, SV=3 | ~~unchecked~~ **READ** — Zaharija & Bradshaw 2023 preprint | **CLEARED, one caveat** |

**The caveat on DISC1, which is not a provenance problem but must travel with the row.**
The range is confirmed three ways in its source: the D region ends at 383, construct
1-383 does not aggregate while 1-415 does, and 383 + 32 = 415 matches both "these 32
amino acids were deleted" and the 32-residue UniProt string already stored. But:

1. **The source is a preprint, and the version of record is still only an abstract.**
   *Prog Neuropsychopharmacol Biol Psychiatry* **130**:110923, PMID 38135095. Its
   **abstract was read 16 Nov 2026** and confirms the claim survived peer review
   unchanged in substance — none of D, I, S or C aggregates alone, D+I+linker does,
   "a region of approximately 30 amino acids ... is critical for aggregation, and
   deletion of this region is sufficient to abolish the aggregation propensity".

   **It cannot close this item, and the reason is exact.** Both abstracts say only
   "approximately 30 amino acids". The claim we carry is **384-415 = 32 residues**,
   which appears nowhere in either abstract. And the case needing exclusion is a
   **one-residue** change at the C-terminal boundary — the preprint's body text wrote
   Δ384-**414** three times against Δ384-**415** in its figures. "Approximately 30" is
   equally consistent with 30, 31 and 32, so the abstract reads identically whichever
   way review resolved that slip. **Only the full text or its Figure 5 settles it.**
   This remains the only §6.3 item, it is a one-residue re-check, and it is now
   quantified rather than open-ended.
2. **The paper's sufficiency claim overreaches its constructs, and §6.2's `construct`
   rule is what catches it.** The Discussion says 384-415 "was both sufficient for
   aggregation", but **384-415 was never expressed alone.** What was expressed alone is
   the whole linker, **384-538** (155 aa), and **1-415**. Necessity is clean — deletion
   abolishes aggregation in 1-854, 1-836 and 1-655 alike. Sufficiency is established for
   the linker, and for 384-415 *in the context of 1-383*. **Do not state 384-415 as
   "sufficient for aggregation" in print without that qualifier.**
3. **`found_by` is clean.** Found by truncation and deletion, no aggregation predictor
   involved. The region also falls outside all four ESPRIT domains — "not found within
   any of 94 most stable DISC1 fragments" — so the structural screen missed it too.

**How the TRIOBP-1 row cleared.** Figure 1B of Zaharija et al. 2022 (*Int. J. Mol. Sci.*
**23**:11048, publisher PDF read in full) prints
`ELEKL|PLRENKRVPLTALLNQSRGERRGPP|SDGHE` beneath a 324-348 numbering row, the coloured
segment flanked by five residues either side. It reproduces the derived string
**byte-for-byte**, and two alignment checks that could have failed did not: 333-340 comes
out `LTALLNQS`, which carries zero charges and which the paper calls "the uncharged
region", and 341-345 comes out `RGERR`, which the paper calls "the cluster of charged
amino acids beginning at AA 341". **The 48.0% gatekeeper figure is no longer a
reconstruction.** Figure 12B of Bradshaw 2017 is no longer required for the letters.

### 6.4 Exclusions fixed now

- ~~**DISC1 716-761 is excluded** from every analysis in this document.~~ **REVISED 16 Nov
  2026 by author decision: CIRCULAR ROWS ARE KEPT AND LABELLED, NOT DROPPED.** Every row in
  `regions.json` now carries `circularity_status` (CLEAN / CIRCULAR / UNDECIDABLE) and a
  written `circularity_basis`. The set stands at **7 CLEAN and 3 CIRCULAR**.

  **CIRCULAR rows are excluded from the primary statistic and reported as their own
  stratum.** They are never silently pooled. The reasoning for keeping them: a benchmark
  that ships its contaminated rows with the contamination documented is more useful to
  other groups than one that silently excludes them, and it lets a reader check our
  circularity calls rather than trust them. DISC1 716-761 keeps its own further caution —
  RADAR-derived *and* a docking restraint rather than a measurement.

  **TRIOBP-1 60-189 is the row that justifies the policy.** It is CIRCULAR — prediction
  nominated it — and the deletion work then **refuted** it. A prediction-nominated region
  that experiment overturned is the most informative false positive in the set, and
  dropping it would have thrown away the clearest evidence the project has.

  **Two rules now fixed.** (i) *Prediction used AFTER mapping does not contaminate* — a
  post-hoc run on an already-mapped region is a mechanistic check, not a selection step;
  this is what keeps DISC1 384-415 CLEAN despite Zaharija 2025 running five predictors on
  DISC1. (ii) *Circularity is tool-specific* — a region AmylPred2 nominated is circular for
  AmylPred2 and any consensus containing it, but a tool that did not exist then is tested
  fairly. CIRCULAR rows may therefore serve as **labelled positive controls for the modern
  arm only**, with the selection bias stated: a region legacy tools ranked top is
  predictable by construction and cannot test whether modern tools recover what legacy
  *missed*.
- **No bulk import from CPAD.** TANGO, CamSol and AGGRESCAN were trained on sequences
  within it; importing without per-row provenance checks reproduces the out-of-sample
  violation that the CANYA paper names.
- **Provenance cannot be grepped.** Circularity is protein-specific, not lab- or
  era-specific. Every row is read before it enters.

---

## 7. The power problem, computed rather than asserted

95% Wilson intervals on a recovery rate `[COMPUTED 15 Nov 2026]`:

| n rows | at p̂ = 0.50 | width | at p̂ = 0.80 | width |
|---|---|---|---|---|
| **2** | [0.09, 0.91] | **0.81** | [0.34, 1.00] | **0.66** |
| 10 | [0.24, 0.76] | 0.53 | [0.49, 0.94] | 0.45 |
| **15** | [0.30, 0.75] | 0.45 | [0.55, 0.93] | 0.38 |
| 25 | [0.30, 0.67] | 0.36 | [0.61, 0.91] | 0.30 |
| 40 | [0.35, 0.65] | 0.30 | [0.65, 0.90] | 0.24 |

- **At n = 2 the interval spans almost the whole unit line.** Tier A cannot estimate a
  rate. It can only show that a specific, named, published failure does or does not
  persist — which is worth reporting, and is a case study.
- **n = 11** is the smallest set at which an observed 80% recovery excludes 50%.
- **n = 15 per arm** separates a legacy 20% from a modern 70% at 80% power, α = 0.05.

**The floor of 15 in `CLAUDE.md` is therefore not arbitrary — it is the number this
design needs, and it is confirmed independently by both calculations.** Tier B is not
optional; without it there is no quantitative claim.

### AMENDMENT, 16 Nov 2026: 15 rows of dataset is not 15 rows of power

Reading three clean rows in full on one day exposed a defect in the calculation above.
It treats every added row as contributing power. **It does not.**

α-syn 71-82, tau PHF6 306-311 and tau PHF6* 275-280 are all clean by `found_by` — and
all three are **regions the predictors find**. That is not an accident of our sweep. A
region gets mapped cleanly and early precisely when it is a classic short hydrophobic or
β-prone motif, which is what the predictors were built to detect. **The literature is
therefore enriched for true positives, and widening the set mostly adds them.**

**A true positive cannot discriminate modern from legacy predictors, because both hit
it.** Power lives only in the **discordant stratum** — rows where experiment and
prediction disagree — which currently holds the two rows we started with.

**Registered now, before any predictor runs:**

- The primary statistic is computed on the **discordant stratum**.
- The **concordant (true-positive) stratum** is reported separately, and its role is a
  **pipeline positive control**: it shows the predictors ran and scored sanely. It is
  never pooled into the primary.
- **Every row carries a `stratum` label assigned before scoring**, derived from the
  published predictor results where they exist, and otherwise from the legacy arm's own
  output — which means the assignment for new rows is made *after* the legacy run and
  *before* the modern run, and that ordering is part of the freeze.
- **The floor of 15 is restated as a floor on the DATASET, not on the test.** The dataset
  is the publishable asset either way (`CLAUDE.md`). **If the discordant stratum cannot
  be grown beyond n = 2, the quantitative claim is withdrawn and the project reports a
  case study plus a dataset — and says so plainly.** That is a pre-registered outcome,
  not a failure.

### 7a The stratum rule applied — AMENDMENT, 18 Nov 2026, POST-UNBLINDING AND THEREFORE EXPLORATORY

**This amends nothing in the rule above. It records that the rule was applied late, and
fixes the consequence.**

**What was found.** Seven rows sat at `stratum: PENDING` with the legacy arm already run
on them. §7 says the label comes from published predictor results "and otherwise from the
legacy arm's own output". `PENDING` had been read as *the source paper ran no predictor,
so the stratum cannot be decided*. **That reading was wrong.** It means *the legacy arm
has not been run on this row yet* — and since 17 Nov, it has.

**What was applied**, mechanically, on 18 Nov 2026: `DISCORDANT` iff TANGO *v* ≥ 0.05,
the recovery bar fixed in §4. Six rows became `DISCORDANT`; TRIOBP-1 333-340
(*v* = 0.0388) became `CONCORDANT`. **No threshold was chosen and no row was judged by
eye**: both the rule and the bar predate every number in this project.

**Why none of those rows is confirmatory.** §7 also fixes an ordering — the assignment is
made after the legacy run and *before* the modern run, and "that ordering is part of the
freeze". **On 17 Nov both arms ran and no labels were applied in between**, so each of
these rows' AggrescanAI scores was already known when the rule was applied.

The rule is deterministic and leaves nothing to tune. But **the discretion did not vanish,
it moved**: it now sits in *whether to apply the rule at all*, a choice made after seeing
that applying it would take the confirmatory set from 2 rows to 8. So:

- the labels **stand**, because they are correct under a rule registered before unblinding;
- every affected row carries **`stratum_assignment.confirmatory_eligible: false`**;
- `scripts/score_rows.py` **reads that flag** and holds those rows out of the confirmatory
  statistic. A stratum label alone no longer admits a row.

**The confirmatory set is therefore unchanged: n = 2, Stouffer Z = −0.7896, p = 0.7851**,
bit-identical to the freeze.

**The exploratory result, reported under §12 and never as confirmatory:** n = 8 gives
**Stouffer Z = −2.4095, one-sided p = 0.9920**. It does not rescue H1 — **it makes the
negative stronger**, which is worth stating precisely because the worry about applying a
rule post-hoc is that it was applied *because* it helped. It did not help.

**And n = 8 is not n = 8.** Three of the eight rows are DISC1 and two are TRIOBP-1;
691-836 wholly contains 748-769, while 384-415 is disjoint. Overlap is not the point —
all three are scored on one profile of one protein by one tool, and Stouffer and Wilcoxon
both assume independent pairs. **The honest unit is the protein: n = 5**, where the
minimum attainable one-sided Wilcoxon p is 0.031 against §4's 0.05 — reachable with no
margin, and unreachable again one protein fewer.

**Registered for new rows, and checkable:** the stratum label must be **committed to git
before the modern arm is run on that row**. That is verifiable after the fact from the
commit graph, which is what makes it a constraint rather than an intention. The recruiting
rule that goes with it is `reports/recruiting_rule_2026-11-18.md`.

---

## 8. Rows found by prediction

Analysed separately, reported separately, never pooled. They are not useless: they
measure **how well a predictor reproduces a region another predictor found**, which
bounds the circularity in the published literature. They cannot speak to H1.

---

## 9. The gatekeeper analysis is demoted, with its reason

`STATE.md` called the gatekeeper inversion "the paper's spine". On 15 Nov 2026, with the
clean DISC1 row supplied from UniProt:

```
crystallised steric zippers   0.0% – 16.7%   (n = 7)
TRIOBP-1 324-348                    48.0%
DISC1    384-415                    18.8%     +2.1 points above the WORST zipper
```

The reported "48.0% to 50.0% (n = 2)" was TRIOBP-1 plus the excluded 716-761 row. **The
separation does not generalise.** H3 is therefore **n = 1**, pre-registered as a
**secondary, descriptive observation**, and may not be stated as a two-protein result.

What is untouched is the **prediction failure at n = 2**: both regions were found by
truncation, neither by prediction, and the predictors missed both. These are two claims
with two different n and must never be written as one number.

### 9.1 AMENDMENT, 16 Nov 2026: H3 is not merely weak, it is pre-empted

**Author's decision, taken on the evidence below.** Recorded here rather than applied
silently, because a pre-registration that edits its own hypotheses without a dated
record is worthless.

Four independent pre-emptions, all READ:

1. **Mandelkow 2007** (*Brain Pathol* 17:83-90) states the paradox for tau and resolves
   it. Tau is "unusually rich in polar and charged amino acids"; this "renders its
   abnormal aggregation ... even more enigmatic". Computed from P10636-8: **whole tau441
   is 35.6% proline-plus-charge and it aggregates.** The resolution is given in the same
   paragraph — "the aggregation of tau is based on **short hexapeptide motifs**" — and
   PHF6 is **16.7%** against the repeat domain's 29.6%. Globally gatekeeper-rich,
   locally zipper-grade. **That is our paradox and our window-matched control, published
   in 2007.**
2. **Murray 2017** (*Cell* 171:615): composition does not discriminate the FUS core.
3. **Seuma 2021** (*eLife* 10:e63364): "seven gatekeeper residues" measured in Aβ42.
   **The gatekeeper concept itself is prior art.**
4. **The concept is also better supported than we need.** ΔK280 deletes a lysine, P301L
   removes a proline, and both *accelerate* PHF aggregation — the converse of Giasson's
   A76E, where adding charge slowed assembly. Graded suppression, both directions,
   measured.

**Consequence.** H3 may appear in the paper only as cited context, with all four
references. **No sentence may imply the gatekeeper observation is new.** The inversion
(48.0% at TRIOBP-1) may be reported as a descriptive extreme, n = 1, nothing more.

**What this buys.** H4, which tau does *not* pre-empt, because tau is the case where the
predictors **succeed**. Tau therefore stops being an optional widening row and becomes
the **required control arm**: without it, H4 has no positive control and is unfalsifiable.

**Registered consequence for the validation set:** tau PHF6 306-311 is a **required**
row, not an optional one. If it cannot be promoted, H4 is withdrawn rather than reported
without its control.

---

## 10. Secondary analyses, each with its decision rule fixed

**10.1 The context test (H2).** Score `LTALLNQS` (TRIOBP-1 333-340, 0% gatekeeper) in
isolation and in its 25-residue context.
- Positive in isolation, negative in context → **the failure is flanking context.**
- Negative in both → **intrinsic core chemistry.**
- Positive in both → the region-level miss is a thresholding artefact, not a chemistry
  failure, and the paper changes.

These are three different papers. The decision rule is fixed **now**, before scoring.

**10.2 Window-level versus region-level.** Report *v* (region-level, primary) alongside
the **minimum per-window *v* inside the region**. TRIOBP-1 324-348 contains hexapeptide
windows at **0.0% gatekeeper**, and 7 of its 20 windows are at or below the worst
crystallised zipper `[COMPUTED]`. If a window-scanning predictor misses a region that
contains a zipper-grade window, that is a **harder** failure than "uninformative by
construction", and the draft should claim the harder one.

**10.3 The legacy baseline is itself a finding.** Of four 2017 tools, two are live, one
is dead, and one requires reimplementation. Reported regardless of outcome.

### 10a Core polarity — REGISTERED 18 Nov 2026, POST-UNBLINDING AND PERMANENTLY EXPLORATORY

**Full specification: `reports/core_polarity_metric_2026-11-18.md`, committed before any
number was computed from it.** Registered here in summary so the decision rules are in
this document with the others.

**Hypothesis.** Both arms score hydrophobicity and β-propensity. A fibril core held by
**polar** contacts is by construction the case they should miss. Raised by the glycinin
structure, whose Figure S6 sorts twelve published fibrils into hydrophobic- and
hydrophilic-core classes.

**Why the obvious version was dropped.** Borrowing S6's labels fails: all three distinct
hydrophilic-core proteins there — FUS, FapC, CsgA — are CPAD 2.0 members, so core
architecture and training-set membership are collinear and one comparison would measure
both.

**The metric.** Φ = the polar-or-charged fraction of the **buried** residues inside a
row's region, computed from deposited coordinates: assembly built to 11 layers using the
deposited helical rise and twist, central chain analysed, Shrake–Rupley SASA (probe 1.4 Å,
92 points, radii fixed in the spec), core residue iff SASA < 10 Å². Sensitivities at 5 and
20 Å², and two alternative polarity tables, are **pre-specified and all reported**.

**Calibration, and the abandonment condition.** Φ is calibrated against S6's twelve
published labels — no *v* is computed for those, so their CPAD status is irrelevant.
**If Φ separates them with AUROC < 0.80 the metric is ABANDONED, not re-tuned.** That
outcome is itself reported.

**The test.** One-sided Spearman ρ between Φ and *v*, modern arm primary, legacy arm
secondary, reported for all eligible rows and for CPAD-absent rows separately, with the
minimum attainable p printed beside the observed one.

**Ordering, checkable from the commit graph:** `structure` fields committed → Φ computed
and committed → only then joined to *v*. Same discipline as §7a.

**WHY THIS CAN NEVER BE CONFIRMATORY, and it is not a matter of procedure.** DISC1 and
TRIOBP-1 have **no deposited fibril structures**, so Φ does not exist for them and the
confirmatory stratum — DISC1 384-415 and TRIOBP-1 324-348 — is entirely outside this
analysis. At most 7 rows are eligible, several are CPAD members, and they are not
independent. **No result here can confirm or refute H1.**

**And the near-tautology is registered in advance**, so that a positive result is not
oversold later: predictors that score hydrophobicity scoring polar cores lower is partly a
restatement of how they work. The finding, if there is one, lies in the experimental half
— that polar-core regions are genuine aggregation determinants anyway. **The claim worth
making is not that the tools dislike polar cores, but that nature does not.**

### 10b Structural recruitment for Φ — REGISTERED 18 Nov 2026, BEFORE ANY SEARCH

**Full rule: `reports/structural_recruiting_rule_2026-11-18.md`, committed before the
first query was issued.** Summarised here so the decision rules sit with the others.

**Why.** At *n* = 7 the §10a result dies if any one of four rows is dropped. *n* is the
only thing that fixes that. **§3.1b does not block this pool**: Φ needs a deposited fibril
structure, §3.1b needs a short region in a long chain, and the two criteria are nearly
disjoint — all seven current Φ rows fail *m*/*M* > 0.05.

**Eligibility (all six):** an experimentally determined region to `regions.json` standard,
read in full, in a named frame, by **either** (a) structure determination **or** (b)
deletion/truncation mapping, with the route recorded; a deposit **of the aggregated state**
covering **≥ 80 %** of the region; Φ computable (deposited rise and twist, or ≥ 5 layers as
deposited); frame verified against UniProt/RefSeq; `found_by` not prediction.
**E1 was corrected the same day, before any candidate was admitted:** as first written it
demanded route (b) only, while **all seven incumbent rows are route (a)**, so recruiting
under it would have mixed evidence types without saying so. ***m*/*M* is NOT a criterion here and
must not be applied** — applying it would reimport the constraint this analysis is free of,
after the geometry is visible.

**One row per protein**, fixed in advance: most region residues modelled, tie to lowest
start residue; for structures, highest coverage, then resolution, then lowest PDB ID.

**Ordering:** screened candidate list committed (rejects included) → Φ computed and
committed → predictor run → join. As §7a and §10a.

**Stopping — the rule that makes this worth doing:** search to pool exhaustion or 15 rows;
**the Φ–*v* test is recomputed ONCE, at the final *n*.** No interim analysis, and
recruitment does not stop because a *p* crossed a threshold. **If fewer than three new rows
are admitted the analysis is not re-run at all** and the *n* = 7 result stands with its
fragility, reported as a negative.

**This stays permanently exploratory.** DISC1 and TRIOBP-1 have no deposited fibril
structures, so the confirmatory stratum is outside this analysis and no *n* changes that.

---

### 10c Discontinuous ordered cores — REGISTERED 19 Nov 2026, BEFORE ANY Φ WAS COMPUTED

**The gap this closes.** §10b E2 says a route (a) row's region *is* the modelled core, and
assumes without saying so that the core is one contiguous span. **All eleven structure rows
already in `data/regions.json` are contiguous** — 37-97, 251-295, 2-55, 55-75, 120-254,
39-74, 164-190, 42-75, 54-86, 7-99, 176-206 — so the assumption has never been tested.
Reading the deposited coordinates of three candidates on 19 Nov broke it: **7VZF (SOD1)
models 3-55 and 86-153** with a 30-residue disordered gap, and **8QUT (human lysozyme)
models 22-34 and 50-128** with a 15-residue gap. Both papers describe the gap in their own
words; it is a real feature of the fold, not a modelling failure.

**Why the obvious mechanical answer is wrong.** R1 ("if a protein yields several eligible
regions, take the one with the greatest fraction of region residues modelled; tie broken by
the lowest start residue") would, applied to segments, pick SOD1 3-55 and lysozyme **22-34**
— thirteen residues — and discard the other seventy-nine. Φ computed on a fragment of a
core is not Φ of that core. R1 was written for *several distinct regions in one protein*,
not for one region in several pieces, and must not be stretched to cover this.

**The rule.** A discontinuous ordered core is **one region**, recorded as an explicit
segment list, with:

- **C1.** `residues` written as comma-separated segments (e.g. `3-55,86-153`), and
  `region_contiguous: false`. Every segment must satisfy E5 separately — the frame is
  verified against each block of the modelled sequence, character for character.
- **C2.** **Φ is computed over all modelled residues of the target entity**, gaps excluded
  because they are not there. The gap is not interpolated, and residues not in the deposit
  are never invented.
- **C3.** The row is **`benchmark_eligible: false`, reason `NON_CONTIGUOUS`** — recorded as
  a ground *separate from m/M*, because it is a different defect. The §3.1 statistic tiles a
  contiguous span and has no defined behaviour on a segment list. This costs nothing: both
  candidates fail *m*/*M* anyway, as all seven incumbent Φ rows do.
- **C4.** If the final Φ set mixes contiguous and discontinuous rows, **the mix is reported
  and the association is repeated within the contiguous subset**, exactly as §10b already
  requires for a route (a)/(b) mix.

**Why admit rather than reject.** Rejecting gapped cores would exclude a structural class
for a reason unrelated to the hypothesis, and it would not be neutral: **the two gapped
candidates are the two largest cores in the pool** (SOD1 121 modelled residues, lysozyme 92,
against a median of ~35 for the eleven incumbents). A contiguity filter is therefore a
size filter wearing a disguise, and if buried polarity varies with core size it would bias
the set in an unknown direction. That argument is about geometry, not about Φ.

> **BLINDNESS, AND HOW TO CHECK IT.** Φ has **not** been computed for SOD1, lysozyme or
> β2-microglobulin, and no *v* has been computed for any of them. This rule is committed
> **before** the first Φ call, in the same commit as the screen that admits the rows and
> ahead of any result. The commit graph is the evidence, as for §7a, §10a and §10b. What
> follows is the honest statement of exposure: **this rule admits rows, so it makes S5's
> three-row threshold easier to reach, and I wrote it while knowing that.** It is recorded
> here so the author can reverse it on exactly that ground.

---

---

## 11. What would falsify the project's thesis

Stated so it cannot be quietly avoided:

- Modern predictors rank both Tier A regions at **v < 0.05** → the premise is wrong, the
  paper becomes "modern predictors fixed it", and that is publishable.
- The FoldAmyloid reimplementation fails its own published checks → the legacy arm is
  two tools, not three, and the comparison weakens.
- Tier B recovery rates for legacy and modern are **indistinguishable within their CIs**
  → there is no generational effect, and the paper is about hexapeptide training, not
  about progress.
- **The 2025 PhD thesis from the experimental group contains modern predictor runs → the
  novelty claim changes.** ~~DISCHARGED 15 Nov 2026 against Samardžija's thesis.~~
  **RE-OPENED AND PARTLY TRIGGERED, 16 Nov 2026 — THERE WERE TWO 2025 THESES.**

  Samardžija's contains no predictor runs. **Zaharija's (read in full, 16 Nov 2026) runs
  five**, in §4.3.5 on full-length DISC1 (NP_061132.2): **TANGO, AGGRESCAN, FoldAmyloid,
  MetAmyl and ANuPP**, six algorithms, default parameters, with a per-residue consensus.

  **The condition is triggered for the legacy arm and NOT for the modern arm.** No PLM, no
  AggreProt, no AggrescanAI appears. §5.2's claim — *"no PLM predictor has ever been run
  on DISC1 or TRIOBP-1"* — is **intact**, and it is the claim this document rests on. What
  changes:

  1. **The retrospective legacy comparison on DISC1 is pre-empted.** Running TANGO,
     AGGRESCAN, FoldAmyloid, MetAmyl or ANuPP on DISC1 and reporting it as new would
     reproduce a published thesis. Cite Zaharija 2025 for it instead.
  2. **Their result strengthens H1 rather than weakening it.** Four of five tools gave
     hotspots "dispersed throughout the entirety of the protein sequence"; only ANuPP
     named the linker (AA 387-395, 400-415). Legacy missed it; one 2021 tool found it.
  3. **TRIOBP-1 is still clean** on present evidence, so the legacy arm survives there.

  **Before the freeze:** restate §5.2's novelty sentence in the abstract and §1 so it says
  *PLM-era* explicitly, and add Zaharija 2025 §4.3.5 as cited prior art for the legacy
  DISC1 scores. See `STATE.md` and `reports/PDFs_to_obtain.md` item 0.

---

## 12. Freeze protocol

1. Clear §6.3. ~~Read Figure 12B~~ **— done 16 Nov 2026, via Zaharija 2022 Fig. 1B
   instead; the TRIOBP-1 sequence and range are READ.** ~~(a) settle the TRIOBP-1 minimal
   region: the thesis says **7 aa**, `regions.json` says **333-340, an 8-mer**~~
   **— SETTLED 16 Nov 2026 at EIGHT. The 2022 paper says "8 amino acids" three times
   (abstract, discussion p.13, Figure 6D legend); the thesis is wrong by one, and
   `regions.json` was right.** ~~Confirm the DISC1 384-415 range in its source~~
   **— done 16 Nov 2026 against the Zaharija & Bradshaw 2023 preprint, which IS that
   source; range confirmed three ways.** **One item left, and it is a re-check rather
   than a gap:** obtain the **full text** of Zaharija & Bradshaw **2024**
   (*Prog Neuropsychopharmacol Biol Psychiatry* 130:110923, PMID 38135095) — its
   abstract was read 16 Nov 2026 and confirms the substance but **not** the boundaries,
   since both versions' abstracts say only "approximately 30 amino acids". What is
   needed is Figure 5 or the Results: **does the published version write Δ384-414 or
   Δ384-415?** Carry the sufficiency qualifier in §6.3(2) with the row regardless.
2. ~~Read the 2025 thesis (§11).~~ **Done 15 Nov 2026 — read in full, condition
   discharged, novelty claim unchanged.**
3. ~~Settle every **[AUTHOR DECISION]**.~~ **Done 15 Nov 2026** (§3.1, §5.1, §5.2),
   delegated to Claude. **The author must still read and ratify or overturn those three**
   — delegation is not agreement, and §13 is the place it becomes binding.
4. Record predictor versions, commit hashes and web-form settings.
5. Commit this file with the SHA-256 of `data/regions.json` recorded in the commit
   message. **That commit is the freeze.**
6. Only then run a predictor.

### 12.2 THE FREEZE — 17 November 2026

**This section is the freeze record. The commit carrying it is the freeze**, and its
message records the SHA-256 of `data/regions.json`.

**No predictor has been run. No score has been seen.** Everything registered above was
fixed before any number existed, which is the only condition under which fixing it is
worth anything.

#### State at the freeze

| | |
|---|---|
| rows | 17 |
| strata | 4 `DISCORDANT`, 1 `DISCORDANT_DERIVED`, 4 `CONCORDANT`, 8 `PENDING` |
| circularity | 14 `CLEAN`, 3 `CIRCULAR` |
| CPAD | 7 rows `CPAD_MEMBER`, 10 `CPAD_ABSENT_ORTHOLOGY_CHECKED` |
| **confirmatory discordant set** | **2 rows** — TRIOBP-1 324-348, DISC1 384-415 |
| legacy arm (§5.1) | TANGO pinned by SHA-256; AGGRESCAN, FoldAmyloid; ProA unavailable |
| modern arm (§5.2b) | AggrescanAI alone; AggreProt unavailable |
| dataset | v1.1.0, tagged, concept DOI `10.5281/zenodo.24290697` |

Predictor pins re-verified by fetch on the day of the freeze, not inherited:
`_FREEZE_REACHABILITY_RECHECK_2026-11-17` in `data/predictor_provenance.json`. The
ProtT5 revision, left open on 16 Nov, is now pinned at `94a6abc0`.

#### Two things carried INTO the freeze as open, stated rather than quietly resolved

**1. The version of record of Zaharija & Bradshaw 2024 has still not been opened.**
Step 1's last item. It is Elsevier, closed access, and Europe PMC confirms it is not in
PMC and has no open full text. The question it would settle is whether the published
version writes Δ384-414 or Δ384-415.

**This does not move our number.** The range is settled at **384-415** by the 2025
thesis's actual plasmid names — `DISC1 (delta-384-415)` and two others — corroborated by
three internal checks, with the preprint's Δ384-414 identified as a typo the thesis does
not repeat. A construct name is stronger evidence than prose. **But the row is one of the
two that survive CPAD exclusion**, so the boundary now carries more weight than it did
when this item was logged, and obtaining the PDF remains worth doing. If it says 414, that
is an amendment made before any score was seen, which is the clean case.

**2. A defect in the §12 prescreen gate, found while auditing it rather than using it.**
The gate says *no manuscript may cite a row whose `verified_against_publisher_pdf` is
false*. **That gate passes DISC1 384-415, whose version of record was never opened** —
because bioRxiv serves a real publisher PDF, so the flag is true for what was actually
read. The row already documents the conflict and states that `source_version` governs.

The gate as written checks *a* PDF, not *the* PDF. **It is left unchanged at the freeze**,
because changing a registered gate at the moment of freezing is exactly the kind of
late adjustment this document exists to prevent. It is recorded here so the write-up
applies `source_version` as well, and so a later tightening is a visible amendment.

**Amendments** after the freeze are permitted, made as commits to this file, each stating
what changed, why, and **whether any score had been seen at the time**. An amendment made
after unblinding is an exploratory analysis and is reported as one.

**`scripts/prescreen.py`-style gate:** no manuscript may cite a row whose
`verified_against_publisher_pdf` is false.

### 12.1 THE FIVE OPEN DECISIONS — ALL SETTLED, 16 Nov 2026

Settled on the author's instruction, **before the freeze and before any predictor
has been run**, which is the only ordering under which settling them is worth
anything. The substance of each is written out so the record is auditable rather
than a rubber stamp. **Any of these may be overturned by saying so; a later
change becomes an amendment under the rule below.**

---

**1. The three delegated decisions (§3.1, §5.1, §5.2): RATIFIED.**

Stated here so that ratification means something:

- **§3.1 — Stouffer's Z primary, Fisher secondary, both always reported.**
  Stouffer weights rows equally and cannot be carried by a single outlier;
  Fisher can. This project's recurring failure mode is precisely one row carrying
  a claim — the gatekeeper result collapsed that way on 15 Nov. A
  Stouffer-null/Fisher-significant disagreement is itself reportable and names
  the row doing the work. **Ratified.**
- **§5.1 — the FoldAmyloid reimplementation must pass Garbuzynskiy's own
  published checks** (80%/72% on the 407-peptide set; only the contact scale
  finds tau 306-311) or be excluded from the confirmatory legacy arm, while being
  reported in full as a methods result. Neither hides a result nor attributes our
  bug to the original authors. **Ratified**, with one consequence that had not
  been noticed — see decision 4.
- **§5.2 — a predictor enters the confirmatory modern arm only if it is
  version-pinnable and runs locally.** **Ratified**, and decision 2 is the first
  real test of it.

---

**2. ANuPP: a named third category, "intermediate generation (exploratory)."**

Not the legacy arm — it is a 2021 tool and §5.1 is a frozen 2004-2010 baseline.
Not the confirmatory modern arm — **it is a web server and fails §5.2's
version-pinnable-and-local rule**, the same rule that already excluded eleven-plus
other PLM-era tools. **Bending that rule for ANuPP specifically would be bending
it for the one tool whose published result is inconvenient**, which is the worst
possible reason to move a line.

So: reported separately, **excluded from the multiplicity correction**, and
Zaharija 2025 §4.3.5's DISC1 hit (AA 387-395 and 400-415, both inside 384-415)
**cited as prior art, not rediscovered.**

**Registered secondary analysis, because it is the question ANuPP actually
raises:** run ANuPP on **TRIOBP-1 324-348, FUS 39-95 and hnRNPA1 251-295** and
report whether its DISC1 success generalises. It has never been run on any of
them. One hit on one protein is not a trend, and four discordant rows can say
which it is.

**The conflict of interest is stated in print either way**, in those words: a
tool succeeding is inconvenient for a project about predictor failure, and the
placement must not be allowed to bury it.

---

**3. The publisher-PDF gate: kept strict, and made precise.**

The gate was unenforceable as written because "publisher PDF" was undefined, and
**the problem is wider than FUS** — today's reading used an NIHMS author
manuscript for hnRNPA1, an accepted manuscript for Tsiolaki, and a **bioRxiv
preprint** for LECT2. Every row now carries **`source_version`**:

| value | citable? |
|---|---|
| `version_of_record` | yes |
| `author_manuscript` (NIHMS / accepted manuscript) | **yes**, with the version named in the citation |
| `pmc_full_text` (read as web text, no PDF) | **no** |
| `preprint` | **no**, unless the row is explicitly about the preprint |

Author manuscripts count because they are the authors' own accepted text; the
version is recorded because copyediting can change wording, and this project
quotes sentences.

**Two consequences, both freeze blockers:**
- **FUS 39-95** is `pmc_full_text`. **Obtain Murray 2017, *Cell* 171:615.**
- **LECT2 55-75** rests on the **bioRxiv preprint**. **Obtain the published
  version, PMC9934627**, and re-check the core range against it.

**A rule is not weakened to accommodate a row when the row can be obtained.**

#### AMENDMENT, 16 Nov 2026: the case where the row *cannot* be obtained

The clause above was written for rows whose version of record is merely
*unfetched*. **DISC1 384-415 is the other case, and it is a primary-stratum row.**

**The negative is documented, not assumed.** For `10.1016/j.pnpbp.2023.110923`,
OpenAlex reports `oa_status: green` with **exactly one** open location — the
bioRxiv preprint already in hand — and **no PMCID**; Europe PMC returns
`pmcid: None, isOpenAccess: N, inEPMC: N, hasPDF: N`. No author manuscript, no
repository copy. The author reports the same.

**Leaving a founding row uncitable on that basis would be a rule defeating its own
purpose.** So, narrowly:

> **A preprint may be cited when, and only when, all three hold:**
> **(i)** the version of record is **demonstrably unobtainable** — a documented
> negative, never an unmade attempt;
> **(ii)** the specific claim is **corroborated by at least one independent
> document that was read in full**; and
> **(iii)** the citation **names the preprint** as the source read and **states
> that the version of record was not consulted.**

**DISC1 384-415 satisfies all three**: (ii) is met twice over, by the Zaharija
2025 thesis (Table 11 names the plasmids `DISC1 (Δ384-415)`, `DISC1 (1-655
Δ384-415)`, `DISC1 (1-836 Δ384-415)`) and by Samardžija 2026, which cites the
2024 paper for *"the aggregation prone-region between"* D and I inside a 257-655
construct — both verified arithmetically against our row.

**This buys citability, not certainty.** It does **not** settle Δ384-414 versus
Δ384-415; that rests on the thesis plasmid names, and **the published boundaries
remain unchecked.** Say so in print.

**The exception is deliberately hard to reuse.** Condition (i) requires evidence
of unobtainability, and condition (ii) requires a document someone actually
opened. **Overturn this amendment if you would rather carry the row as
uncitable** — that is a defensible position and the cost is one row out of the
primary stratum.

---

**4. tau PHF6 306-311 — and it has THREE roles, not two.**

Reading §5.1 to ratify it surfaced the third: **PHF6 is the validation target for
the FoldAmyloid reimplementation** (*"only the contact scale finds tau
306-311"*). It is also (a) the deposited-crystal comparator `2ON9` in
`gatekeeper_density.py` and (b) the H4 control-arm validation row.

Settled:

- **Role (a) is dropped.** PHF6 is **removed from the `ZIPPERS` comparator list.**
  Six deposited zippers remain and the comparator's job — characterising what a
  real steric zipper looks like compositionally — survives losing one. The
  control-arm role has no substitute.
- **Role (c) is kept.** The FoldAmyloid check is specified in Garbuzynskiy's
  print and is a fixed external standard; it is not ours to move.
- **Role (b) is kept, with a pre-registered per-tool exclusion.**
  **FoldAmyloid's score on tau PHF6 306-311 is not counted**, because §5.1
  validates FoldAmyloid on that exact region and a tool pre-validated on a row
  cannot then be tested on it. Every other predictor scores the row normally.

α-syn NACore and preNAC have the same latent conflict but are **CIRCULAR
candidates, not promoted rows**, so no conflict exists yet. **If either is ever
promoted, apply this same rule.**

---

**5. `DISCORDANT_DERIVED` is a separate stratum and is NOT pooled into the
primary statistic.**

LECT2 55-75 is discordant only because **we** chose to compare Tsiolaki 2019 with
Richards 2023 and computed the overlap. **Choosing which two papers to compare is
exactly the researcher degree of freedom that pre-registration exists to
remove** — and the four documented rows have no such freedom, because a single
paper ran the tools and reported the outcome itself.

So: reported as a **pre-specified secondary stratum**, with the derivation shown
in full (7 of 21 core residues predicted; the 14-residue centre 59-72 missed,
including Q59, N65, N67, I69, N71, G72). **If the primary and the derived stratum
disagree, that is reported, not reconciled.**

---

### 12.2 THE TEN `UNRECORDED` ROWS — RESOLVED, 16 Nov 2026

By lookup, not guesswork: each row's `verified_against` field was read, and each
named source was then checked against `data/references_to_check.json` for an
entry recording that it was actually opened.

| rows | source | `source_version` | citable? |
|---|---|---|---|
| TRIOBP-1 324-348, 333-340, 1-59 | Zaharija 2022, *IJMS* 23:11048 | `version_of_record` | **yes** — MDPI CC BY, the publisher PDF *is* the VOR |
| TRIOBP-1 324-328, 60-189 | Bradshaw 2017 | **`source_not_opened`** | no |
| DISC1 691-836, 716-761, 717-737/739-761, 748-769 | Cukkemane 2021 | **`source_not_opened`** | no |
| DISC1 **384-415** | Zaharija & Bradshaw **bioRxiv** 2023 + 2025 thesis | **`preprint`** | **no — see below** |

**A fifth schema value was needed.** The original four presumed the source *had*
been read in some version. **Six rows do not satisfy that presumption:** neither
Bradshaw 2017 nor Cukkemane 2021 has a register entry. Bradshaw 2017 appears only
as a citation inside papers that *were* read; Cukkemane 2021 appears only as a
`claim_as_cited` in an entries list. **All six already carry
`verified_against_publisher_pdf: false`**, so the §12 gate already excluded them
— this records *why*, and changes no status.

**DISC1 384-415 is the one that matters, and it is a freeze blocker.** It is a
**primary-stratum DISCORDANT row** — one of the two the project was founded on —
and its range rests on a **preprint plus a thesis**. The version of record,
Zaharija & Bradshaw (2024) *Prog Neuropsychopharmacol Biol Psychiatry* 130:110923
(PMID 38135095), **has not been obtained**: register key `zaharija2024` records
`read_in_full: false`, *"FULL TEXT NOT OBTAINED — Elsevier/Ovid paywall."*

**This sharpens step 1 rather than adding a new item.** Step 1 already listed that
paper as the one remaining thing, framed as *"does the published version write
Δ384-414 or Δ384-415?"* **It is now more than a re-check: until that paper is
obtained, the row cannot be cited at all**, and the primary analysis would be
computed on a stratum one of whose four members is unprintable.

**Flag conflict, and the rule for it.** DISC1 384-415 carries
`verified_against_publisher_pdf: true`, which is defensible for what was opened —
bioRxiv serves a real PDF — but misleading under §12.1. **Where the boolean flag
and `source_version` disagree, `source_version` governs.** It is the stricter and
more informative column.

---

**Status: §12 step 3 is discharged and the `UNRECORDED` rows are resolved. One
freeze blocker remains — Zaharija & Bradshaw 2024 — plus steps 4 and 5 (predictor
versions, then the freeze commit).**

**Amendments after this point** follow the rule below: a commit to this file
stating what changed, why, and **whether any score had been seen at the time.**

---

### 12.1a The Δ384-414/415 question is numerically inert [18 Nov 2026]

**Scores had been seen when this was computed. It changes nothing registered, and it
reads no predictor output** — only the chain length, the window width and the two
candidate boundaries, exactly as §3.1b does.

Under §3.1 (non-overlapping tiling, *W* = 6, *L* = 854), both candidate regions select
**the same five tiles**:

| region | length | *M* | *m* | tiles | *m*/*M* |
|---|---|---|---|---|---|
| 384–**415** | 32 aa | 142 | 5 | 385-390, 391-396, 397-402, 403-408, 409-414 | 0.035211 |
| 384–**414** | 31 aa | 142 | 5 | 385-390, 391-396, 397-402, 403-408, 409-414 | 0.035211 |

**Residue 415 falls in no scored tile.** The last tile inside the region ends at 414, and
the next begins at 415 but ends at 420, outside either boundary. So *P*, *v*, *m*/*M*,
`power_eligible`, the §5.2b Stouffer input and the §4 verdict are **bit-identical under
either reading.** No result in this project depends on which number the version of
record prints.

**What this retires, and what it does not.** The blocker had two components and they
separate cleanly:

- **The boundary question is closed, now twice over.** It was closed *textually* on
  16 Nov by the 2025 thesis, whose Table 11 names the plasmids `DISC1 (Δ384-415)` and
  whose §4.3.4 and Conclusion 3.1 both say 384-415 — identifying the preprint's Δ384-414
  as a typo. What is added here is that it could never have mattered: the two readings
  are the same measurement. **Rule 2 again, arriving late** — the margin was one residue
  and the resolution of the statistic is six.

  > **THE TEXTUAL CLOSURE WAS WRONG, AND THE NUMERICAL ONE HELD. [19 Nov 2026]**
  > The corresponding author sequenced the deletion vectors and reports the deleted
  > region as **384-414** (1-383 joined to 415-854). So the preprint's Δ384-414 was
  > **not** a typo — the thesis plasmid names, the figure labels and "these 32 amino
  > acids" are. `data/regions.json` now reads 384-414.
  >
  > **This is the amendment working as intended, and it is worth being precise about
  > why — including about its own ordering, which this paragraph first stated wrongly.**
  > §12.1a was committed on **18 Nov, 21:34**: the day *after* the question went to the
  > author (17 Nov) and the day *before* the reply arrived (19 Nov). It was **not**
  > written before the question was put, as first claimed here and as the commit message
  > of `7ce6e71` still claims. **The ordering that matters survives** — the project
  > committed to *no number can move* before learning which way the answer went — but it
  > is a weaker claim than the one first written. In a project whose entire warrant is
  > the order of its commits, an overstated ordering is the worst available error, and
  > this one was caught only because the author proofread the outgoing email against the
  > repository. Re-running on the corrected row
  > confirms it to every digit: *v* = 0.416408 and the confirmatory *n* = 2 Stouffer
  > *Z* = −0.7896, one-sided *p* = 0.7851, equal to the freeze. **Had the prediction
  > been made after the answer arrived it would be worth nothing**; the order is in the
  > commit graph.
  >
  > **One number does move, and it is not covered by the invariance:** gatekeeper
  > density, whose denominator is the region length — 6 of 31 = **19.4%**, formerly 6 of
  > 32 = 18.8%. Ala415 is not a gatekeeper, so the count is unchanged. This moves the
  > region *further* from the worst crystallised zipper (16.7%), from +2.1 to +2.7
  > points, and so does not rescue the retired H3 headline.
  >
  > **What the error was.** Three internal checks passed and all three were checks on
  > *transcriptions* of the construct rather than on the construct. Agreement among
  > restatements that all descend from one document is not independent corroboration.
  > The row's own `source_version_note` had flagged this exact question as unsettled,
  > which is why it was asked; the flag was the thing that worked.
- **The citability question stands, unchanged.** The row's source is a preprint plus a
  thesis; `source_version` governs over the boolean flag, and DISC1 384-415 still cannot
  be cited to a version of record. The 2024 paper is behind an Elsevier paywall the
  author has declined to pay.

**Consequence: the blocker is re-tiered, not cleared.** It no longer gates the analysis
or the freeze — nothing downstream moves — and it is **needed at manuscript submission**,
where a reprint request, an institutional-repository deposit or interlibrary loan has
months rather than days to resolve. One `sequence` field in `data/regions.json` is a
32-residue string; if the version of record proved to say 31, that field would need the
last residue trimmed, with no consequence for any score. The preprint settles it at 32
on three internal checks and the thesis agrees, so this is a formality, not a doubt.

---

## 13. Signature

- Pre-registration ratified by: ____________________  date: __________
- `data/regions.json` SHA-256 at freeze: ____________________
- Tier A rows at freeze: ____  Tier B rows at freeze: ____
