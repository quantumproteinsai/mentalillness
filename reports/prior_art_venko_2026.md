# The prior-art question, settled: Venko & Žerovnik 2026 does not pre-empt this project

**18 November 2026.** Publisher PDF supplied by the author and **read in full**. The
paper had been sitting in the record as an abstract-only read, flagged as the one
outstanding threat to the project's novelty claim.

> Venko K & Žerovnik E (2026). *Assessment of Aggregation- and Condensation-Prone
> Regions of Proteins Involved in Neurodegenerative, Neurological and Mental-State
> Diseases.* **Biomolecules 16:1286**, doi:10.3390/biom16091286.

---

## Verdict

**NOT PRE-EMPTED. MUST BE CITED.** It is the closest published neighbour this project
has — 20 aggregating proteins, six of them shared with `data/regions.json` (DISC1,
TRIOBP1, FUS, tau, hnRNPA1, α-synuclein), run through more than 40 predictors — but it
reports **predictor output, not a benchmark.**

Absent, and absent by design rather than oversight: a statistic, a null model, a decoy
construction, a pre-registration, a success threshold, an error bar, and a validation
set. Agreement with experiment is assessed **narratively, protein by protein, in prose.**

The authors state the gap themselves, in the Discussion:

> *"A major limitation of the present study is the lack of experimental evidence for the
> investigated proteins, which prevents a direct validation of the predicted CPRs and
> APRs."*

and in the Results:

> *"only a subset of these regions has thus far been experimentally characterized."*

**The thing they say they lack is what `data/regions.json` is.** That is the cleanest
possible statement of why the validation set is the project's core asset, and it now
comes from an independent group rather than from this record.

---

## What it gives us

**1. A published negative on TRIOBP-1 324–348**, from a consensus panel rather than a
single tool:

> *"Unexpectedly, this region was only predicted by FuzzDrop in our analysis, whereas
> several other regions of TRIOBP1 received stronger computational support to be capable
> of inducing aggregation."*

**2. A second published negative, on DISC1 716–761:**

> *"The DISC1 C-region can form amyloid-like fibers in vitro at residues 716–761, which
> surprisingly are not defined in our computational studies."*

**3. A third document pointing at Zaharija & Bradshaw 2024.** Their ref [122] is cited
as the source of the DISC1 central-region result. That paper is still unread here, and
it is what the outstanding Δ384-414/415 query to Bradshaw concerns.

## And one result that cuts against us

**For DISC1 384–415, the Venko consensus is not a miss.** Table 3, same 854-residue
frame as our row:

| their call | support | lies inside our row? |
|---|---|---|
| aggregation-prone 403–411 | ≥2 predictors | **yes** |
| amyloid-prone 388–394 | ≥4 predictors | **yes** |
| amyloid-prone 400–406 | ≥4 predictors | **yes** |

Recorded because it weakens the *"the predictors miss it"* framing **for that row
specifically**, and the record should not quote only the half that helps.

---

## A correction to our own earlier framing

**"44 programs" is the headline but not the denominator for regions.** Only a subset
return residue-level calls. By their Table 2: **5 aggregation-region tools** (SODA,
FuzDrop, ANuPP, Aggrescan, TANGO), 14 amyloid, 5 condensation, 2 prion.

So *"only FuzDrop predicted TRIOBP-1 324–348"* is **1 of 5, not 1 of 44**, and must be
quoted that way wherever it is used.

---

## Three defects, found by reading the full text

**1. A TRIOBP-1 frame collision.** Table 1 declares the sequence as **"593 (1772–2365)"**
under Q9H2D6 — the old 593-residue frame, which `CLAUDE.md` requires **+59** to reach
NP_008963.3. But the experimental region they test their predictions against, **324–348,
is a 652-frame number** (Bradshaw 2017 JBC, read in full here on 16 Nov 2026). In the
593 frame that region is **265–289**. Predictions and target are stated in two frames
59 residues apart, so the "only FuzzDrop" comparison **cannot be verified as written.**

This is the project's own numbering trap, appearing in print in a 2026 paper. Not yet
raised with the authors.

**2. A citation slip.** They attribute 324–348 to ref [123] = **Bradshaw et al. 2014**
*PLoS ONE* 9:e111196. Both papers were read in full here on 16 Nov 2026: the 2014 paper
points at the **PH domain** — our `TRIOBP-1 60-189` row, which the deletion work did not
support. 324–348 is from **Bradshaw et al. 2017** *JBC* 292:9583, whose title is
literally *"An unpredicted aggregation-critical region..."*. **The 2017 paper is not in
their reference list at all.**

**3. An internal inconsistency on DISC1 716–761.** The text says it is "not defined in
our computational studies". That holds for their **amyloid** consensus — nearest calls
699–705 and 823–829, both outside — but **not** for their **aggregation** consensus,
whose DISC1 row lists **751–757**, inside 716–761. The published negative is therefore
true of the 14 amyloid tools and false of their own 5-tool aggregation panel.

---

## What it does not contain

No *m*/*M*, no information limit, no floor, no calibration, no power statement, no
per-row uncertainty of any kind. No CPAD or training-set membership check, hence no
circularity control. **No `construct` column** — regions are compared without regard to
which construct established them. **No `found_by` column**, so prediction-discovered and
experiment-discovered regions sit side by side; for TRIOBP1 their narrative does exactly
this, discussing the PH-domain *prediction* and the 324–348 *experiment* in one
paragraph.

Those are the two columns `CLAUDE.md` says must never be dropped. The nearest published
neighbour has neither.

---

## Consequence for the write-up

Cite as **the state of the art in applying predictors to this protein set**, and as
**independent corroboration of the premise on two rows**. The contrast to draw is
methodological, not territorial:

> They publish predictions for proteins whose regions are mostly unmapped. This project
> publishes mapped regions and a pre-registered test against them.

**Do not claim they failed to benchmark.** They did not attempt to, and they say so in
print.
