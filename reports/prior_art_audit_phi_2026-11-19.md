# Prior-art audit of the core-polarity claim — 19 November 2026

**Run before spending anything further on Φ, with the numbers and the error bar in hand.
It found what it was run to find.** Four claims audited; the headline one is pre-empted by
a 2023 paper, and the pre-emption includes a numerical collision on one of the ten
structures.

---

## Claim 1 — the Φ metric: **PRE-EMPTED**

> **García-Pardo J, Bartolomé-Nafría A, Chaves-Sanjuan A, Gil-Garcia M, Visentin C,
> Bolognesi M, Ricagno S, Ventura S (2023). "Cryo-EM structure of hnRNPDL-2 fibrils, a
> functional amyloid associated with limb-girdle muscular dystrophy D3." *Nature
> Communications* 14:239. doi:10.1038/s41467-023-35854-0.**

**VERIFIED INDEPENDENTLY, NOT TAKEN ON THE AUDITOR'S WORD.** The Europe PMC full text
(PMC9842712) was downloaded on 19 Nov 2026 and the two load-bearing sentences read in
place. Methods, verbatim:

> *"The percentage of buried polar residues and the exposed surfaces of hnRNPDL-2,
> hnRNPA2, hnRNPA1, hSAA1, Aβ−42 and α-synuclein fibrillar structures were calculated
> using PDBePISA."*

Results, verbatim:

> *"a percentage of polar residues in the buried area of 64%; both values being
> significantly higher than in disease-associated fibrils (Supplementary Table 2)."*

So the quantity — **polar fraction of the buried residues of a fibril core, tabulated per
structure and compared across proteins** — is in print, in *Nature Communications*, since
January 2023. Φ is not a new measure.

### The collision is numerical, not merely conceptual

Their comparison table includes **hSAA1, PDB 6MST, residues 2-55** — the identical entry
and identical range as this project's SAA row. Their published value is **46%**. Ours is
**Φ = 0.4615**, computed by a different method (Shrake-Rupley SASA < 10 Å² against their
PDBePISA interface burial). `results/core_polarity_2026-11-19/phi_rows_11layers.json`
confirms the entry, the range and the value.

> **THE RIGHT RESPONSE IS TO PUBLISH THE AGREEMENT, IN OUR OWN WORDS, BEFORE A REFEREE
> PUBLISHES IT AS AN ACCUSATION.** Two independent implementations, two different burial
> definitions, one structure, 46% against 46.2%. That is a validation of the
> implementation. It stops being a validation the moment someone else points it out first.

### What survives, stated narrowly

Not the metric. The **operationalisation**, and only if it is presented as that:

- **Shrake-Rupley per-residue SASA < 10 Å² with a declared polar set**, against PDBePISA
  interface burial — ours is reproducible from a committed script and a checksummed
  coordinate manifest; theirs is a web server.
- **Edge-free burial via 11-layer helical replication.** Their numbers are computed on a
  deposited 5-rung model, so edge layers contribute. **Their own paper sizes that artefact
  for us**: 64% for the upper layer against 67% for the inner layers of the same
  structure, a 3-point difference that our replication removes by construction.
- **Scale and calibration**: 22 structures with an AUROC against a pre-registered
  abandonment bar, against their six-structure descriptive table.
- **Use as a covariate on predictor output** — which is Claim 2, not Claim 1.

## Claim 2 — the Φ–predictor association: **NOVEL, and narrower than it looked**

> ### SETTLED 20 Nov 2026: the survival condition below was tested, and the claim did not survive.
>
> This section identified the risk precisely and prescribed the test. **The test was
> registered as §10d and run on 20 Nov: verdict `COLLAPSED`, at both burial cutoffs.**
> ρ(Φ_seq, *v*) = **+0.8929** (*p* = 0.0062) against ρ(Φ, *v*) = +0.8214 (*p* = 0.0171);
> collinearity ρ = +0.9643; partial ρ(Φ, *v* │ Φ_seq) = **−0.3315**.
>
> **The sequence-only covariate did not merely do as well. It did better, and the partial
> reversed sign.** The structural claim is withdrawn and the finding is Louros 2020, as
> this section warned. **This audit paid for itself here**: the risk was named in writing
> before the compute, and the test it specified cost about ten minutes.
>
> One correction to this section's own arithmetic, found by running it: the rule-2 check
> below took Φ's error bar from the cut-5/cut-10 difference. That was right, and it
> understated the problem — **at cut 5 the headline ρ is +0.6786, *p* = 0.0548, failing the
> project's own α.** See `results/seq_polarity_control_2026-11-20/`.

Nobody has computed a property from deposited fibril coordinates and correlated it with a
per-region predictor-recovery statistic. **But the boundary is thin and two papers press
on it:**

- **Louros N, Orlando G, De Vleeschouwer M, Rousseau F, Schymkowitz J (2020),
  *Nat Commun* 11:3314** — *"most sequence-based predictors negatively correlate net charge
  to protein aggregation and have increased failure rates when identifying such
  amyloid-forming stretches"*, with APRs missed by sequence predictors carrying **a 20%
  increase in polar and charged side chains**, quantified, ANOVA, 85 of 96 designed
  peptides validated.
- **Thompson M, … Bolognesi B, Lehner B (2025), *Sci Adv* 11:eadt5111** — a deliberate
  "where do the predictors fail" analysis in which failure tracks charge and polarity, at
  *n* > 100,000 measured sequences, *P* < 2×10⁻¹⁶.

**So "polar segments are the ones predictors miss" is established at sequence level, twice,
at enormous n.** Ours is a property of the *coordinates* — which residues are buried — not
of the segment's sequence.

### The survival condition, and it is a real risk

**Φ may be a proxy for the mapped region's own sequence polar fraction.** Where a region is
almost entirely buried, Φ *is* its sequence composition. Our own Orb2 row makes this
concrete: core sequence `QLHQQQHQQQHQQHQQHQQQQQLHQHQQQLS`, Φ = 0.897. We control for
*m*/*M*; **we do not control for sequence polarity.**

> **PRE-REGISTER, THEN RUN:** ρ(*v*, polar fraction of the mapped region's sequence) and
> the partial ρ(Φ, *v* │ sequence polar fraction), on the same seven rows. **If the
> sequence-only covariate does as well, the structural claim collapses into Louros 2020 by
> a more expensive route.** This must be written down before it is computed, exactly as
> §10a was.

## Claim 3 — the information limit: **CONTRADICTED in its universal form; the general fact is old and has a name**

**(a) §3.1b overclaims.** It says *m*/*M* is the smallest *p* **any** rank-based statistic
can return. That is true only for statistics that are a function of the region's **best
window rank alone** — which ours is. A rank-sum over the *m* in-region against the *M*−*m*
out-of-region window scores has minimum attainable one-sided *p* = 1/C(*M*,*m*). On our own
β2-microglobulin row, *m* = 10, *M* = 16: **1/C(16,10) = 1/8008 = 1.25×10⁻⁴**, against
*m*/*M* = 0.625.

That row is exactly where it bites: the predictor's single best window **in the entire
chain** lies inside the mapped region, and our statistic returns *v* = 0.272 and the label
DISCORDANT, because it uses the minimum rank and discards the other nine.

**This is a limit on the claim, not a rescue of the thirteen rows.** A rank-sum answers a
different question, the tiled windows are not independent, and switching statistics after
unblinding is precisely what the pre-registration exists to forbid. The correct wording is
**"no amendment within the min-rank family can rescue it"**, and a rank-sum is a candidate
*pre-registered secondary* statistic for future rows.

**(b) The general fact is published and named.** Minimum attainable *p* under discreteness,
with exclusion of untestable hypotheses, is **Tarone's rule** — Tarone RE (1990), "A
modified Bonferroni method for discrete data", *Biometrics* 46:515-522. **Cite it. Do not
present the bound as a discovery.**

**(c) The aggregation-benchmarking application is EMPTY** across every query tried. So it
is publishable as an application, in the corrected form, with the right citation attached.

**(d) An unrecorded consequence of our own arithmetic.** `floor_v` ≈ *m*/2*M*, so
`floor_v` ≤ 0.05 ⟺ *m*/*M* ≲ 0.103. **The admission bar of *m*/*M* ≤ 0.05 is about twice as
strict as our own statistic requires**, and rows with 0.05 < *m*/*M* ≤ 0.103 are being
refused although *v* < 0.05 is attainable for them. Not a licence to relax it after seeing
scores — recorded as a fact about the rule.

## Claim 4 — competitor sweep: **no pre-emption from Lehner/Bolognesi**

Sixteen records 2022-2026, none defining a structural metric or tying a fibril-core
structural property to predictor failure. The nearest is the Thompson 2025 passage above,
which is sequence-level.

> **AND THE REASON THE PRE-EMPTION WAS MISSED, WHICH IS THE TRANSFERABLE LESSON.** The
> sweep I asked for was keyed on **Bolognesi B** — Benedetta Bolognesi, CRG/IBEC. The
> co-author of the Claim-1 pre-emption is **Bolognesi M** — Martino Bolognesi, structural
> biology, Milan — on a paper with Ventura and Ricagno. **A surname-keyed sweep conflates
> two unrelated labs, and the group that actually pre-empted Φ is the one nobody was
> watching.** Watch **Ventura / García-Pardo**, not CRG.

Limitation stated: Europe PMC's bioRxiv indexing lag means the latest preprint hit is
2026-07-16; anything from Aug-Nov 2026 may be missing.

---

## Two errors in the brief I wrote, found by the auditor

Both are mine, both were in the method statement I sent, and both are now verified against
the output files:

1. **"Computed on an 11-layer assembly … using the deposited rise and twist" is not true of
   FUS**, the rank-2 point. That row records `mode: "AS DEPOSITED (no helical parameters)"`.
   `phi_spec.json` documents it; the brief did not.
2. **5W3N is solid-state NMR with 20 deposited models.** Φ for FUS therefore carries a
   model-selection variance no other row has, and it is undeclared. It should be reported
   as **mean ± SD over the 20 models**; at 20 models that is nearly free, and FUS is
   high-leverage in a seven-point Spearman.

## The rule-2 check the auditor ran that I had not

I supplied no error bar for Φ, so it took one from our own files: the per-structure
difference between the two pre-specified burial cutoffs. **Within the seven frozen rows,
the hnRNPA1/SAA pair reverses order between cut 5 and cut 10** — verified directly:

| | cut 5 Å² | cut 10 Å² |
|---|---|---|
| hnRNPA1 251-295 | 0.4651 | 0.4651 |
| SAA 2-55 | **0.4706** | **0.4615** |

The gap deciding that pair at cut 10 is **0.0036**, smaller than SAA's own cutoff
sensitivity of **0.0090**. Three of the seven values — 0.4651, 0.4615, 0.4583 — span 0.0068
and are a tie cluster the metric cannot resolve.

The exact *n* = 7 null, enumerated over all 5040 permutations, reproduces our *p* exactly
(86/5040 = 0.01706) and shows the headroom: Σ*d*² = 10 → *p* = 0.0171; 12 → 0.0240;
16 → 0.0441; 18 → 0.0548. **Two adjacent rank swaps of headroom, three being fatal — and
one swap is already demonstrated by our own cut_5 column.** The cut_5 sensitivity must be
reported alongside the headline, not kept in reserve.

## What to do, in order

1. **Drop the "new metric" framing of Claim 1** and cite *Nat Commun* 14:239 Supplementary
   Tables 2-3 explicitly, including the 46% / 0.462 agreement on 6MST.
2. **Pre-register, then run, the sequence-polar-fraction control for Claim 2.** It is that
   claim's survival condition.
3. **Report the cut_5 sensitivity** of ρ, and Φ(FUS) as mean ± SD over the 20 models.
4. **Correct §3.1b's universal clause** to the min-rank family, cite Tarone 1990, and
   record the β2m rank-sum counterexample as a limit.

## The document that could remove the last of Claim 1

**García-Pardo J & Ventura S (2024), "Cryo-EM structures of functional and pathological
amyloid ribonucleoprotein assemblies", *Trends Biochem Sci*, doi:10.1016/j.tibs.2023.10.005
— PAYWALLED, Europe PMC `isOpenAccess: N`, NOT READ.** It covers TDP-43, FUS, Orb2,
hnRNPA1, hnRNPA2 and hnRNPDL-2 — **four of our Φ structures including our top two**. If it
extends the buried-polar tabulation to Orb2 and FUS, then the comparative *ranking* of our
highest-Φ structures is also in print and Claim 1 retains nothing. **This is the single
highest-value PDF outstanding on the project.**
