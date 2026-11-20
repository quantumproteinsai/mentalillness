# Can the max-statistic be justified independently of our result? — 20 November 2026

> **The stop condition does not fire. The paragraph can be written, and it has two
> independent published witnesses — one of them the very paper that mapped TRIOBP-1
> 324-348, nine years before this project existed.**

---

## The question, as the audit put it

`reports/prior_art_audit_information_limit_2026-11-20.md` §8.1:

> *"**Does the max-statistic survive its own limit?** If the registered `v` is replaced by a
> statistic reading all `m` in-region ranks, the information limit vanishes and with it the
> contribution. Settled by: a paragraph in the manuscript justifying the max-statistic on
> grounds independent of the result (e.g. that a predictor is *used* by reading its top
> peak), written before any re-scoring. **If no such justification exists, stop — this is
> the 'stop' case.**"*

The force of it is real. §3.1b's information limit is a property of the **min-rank family**
— statistics that read the region's single best window rank. A rank-sum over all *m*
in-region windows has floor 1/C(*M*,*m*), which is vanishingly small, and the limit
disappears. So the one surviving claim is a limitation of a statistic we chose, unless the
choice is defensible on grounds that have nothing to do with the answer it gave.

**The justification must therefore be external, and it must predate or ignore our result.**
Writing it from our own reasoning would be circular.

## Witness 1 — Bradshaw et al. 2017, the paper that mapped the region [READ]

*J Biol Chem* 292(23):9583-9598. Discussion, verbatim:

> *"In our previous analyses (8), this portion of TRIOBP-1 was one of the less strongly
> predicted to contain an 'aggregation motif,' with only the sequence around aa 230-236
> predicted to have some aggregate-forming propensity by the AGGRESCAN, FoldAmyloid, and
> ProA servers. It was not predicted as such by TANGO. In all instances, however, **at least
> four sites elsewhere in the protein were more strongly predicted** to be capable of
> inducing aggregation; thus, this location for an aggregation-critical region was an
> unexpected result."*

**That is a max-rank evaluation, performed by the experimentalists, in print, in 2017.**
They did not compute an enrichment of high scores across the region. They asked **how many
sites ranked above it** — and answered "at least four, in every tool". The judgement that
the predictors missed the region is reached *by reading the ranking from the top*.

This is the strongest form the witness could take: it is **the source paper for one of the
two confirmatory proteins**, it predates this project by nine years, and it had no
knowledge of any statistic we would later register.

## Witness 2 — Singh, Jangid & Srivastava 2026 (AmyloCore-ML) [READ]

bioRxiv v3, 18 Nov 2026 — an independent group, benchmarking this project's own
confirmatory arm. Methods, verbatim:

> *"AUROC and AUPRC were used to measure residue-ranking performance, while **localization
> was assessed using distance of the highest-scoring region from the experimental core**."*

And in Results, as a headline metric reported for every model and for both external
predictors: *"mean peak distance of 12.4 residues"*, *"a larger mean peak distance of 30.2
residues"*.

**They report a peak-based localisation metric beside AUROC, and they treat the two as
answering different questions** — which is exactly the distinction between a max-statistic
and a rank-sum. Their Figure 4c makes peak distance a primary axis of comparison. **A 2026
paper, written without knowledge of us, evaluates aggregation predictors by where the top
of the profile falls.**

## Witness 3 — what the tools themselves emit

This is weaker and is offered third, but it is the mechanism behind the other two. None of
the registered legacy tools outputs a ranking of the whole chain as its product. **TANGO
reports segments above a threshold; AGGRESCAN reports "hot spots"; FoldAmyloid reports
predicted amyloidogenic regions; AggrescanAI reports APRs.** The artefact a user receives
is a short list of locations, ordered by score. **Asking "did the tool find this region?"
is therefore natively a question about the top of that list**, not about the average rank
of the region's residues.

## What this licenses, and what it does not

**It licenses:** reporting the information limit as a real constraint on how these tools are
actually used and actually evaluated — by two published groups, one of them the mapping
group itself.

**It does not license:** calling the max-statistic the only legitimate choice, or presenting
the limit as general. §3.1b's dated correction already restricts the claim to the min-rank
family and gives the β2-microglobulin counterexample (1/C(16,10) = 1.25×10⁻⁴ against
*m*/*M* = 0.625). **That restriction stands and this report does not relax it.**

> **The honest scope, which the manuscript must use:** *for the min-rank reading of a
> predictor's output — the reading used by the group that mapped TRIOBP-1 324-348 and by the
> 2026 group that benchmarks AggrescanAI — there is a floor on the attainable p-value that
> is fixed by region length against chain length, and for 13 of our 23 scored rows it sits
> above α.* Not "rank-based benchmarks have an information limit". The qualifier is load-bearing.

## Registration status

**Nothing is re-scored and no statistic changes.** §3.1 is frozen and stays frozen. This is
a *justification of a pre-registered choice using external evidence*, which is permitted and
is not an amendment. Both witnesses were read from publisher PDFs on 20 Nov 2026, and both
are recorded in `data/references_to_check.json` with
`verified_against_publisher_pdf: true`.

**The audit's §8.1 is therefore CLOSED, and the "stop" case does not fire.**

## And §8.2 is closed too, against the audit's own expectation

The audit predicted that screening Singh et al.'s 82 regions would yield *"~0 admissible
rows"*. **It yields 10 of 82 (12%)** — see `results/amylocore_screen_2026-11-20/`. The
audit's reasoning was right and its arithmetic guess was wrong. The CPAD gate then removes
nine of the ten, so the joint yield is 1 in 82 and the practical conclusion the audit
reached — that the 15-row floor is not reachable by this route — survives, for a different
reason than it gave.

**§8.3 remains open:** the per-row versus per-dataset distinction still needs arXiv:2611.15555
read in full.
