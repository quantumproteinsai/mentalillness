# Draft paragraph: asking Bradshaw for other fragment-level mapped regions

**Status: DRAFT, NOT SENT.** Written by Claude for the author. Intended as an addition to
the next message to N. Bradshaw (with B. Zaharija), not as a separate email.

**Why this is worth one paragraph of his time.** Measured 19 Nov 2026 and corrected
20 Nov: **exactly one of the thirteen structural rows in the dataset is `power_eligible`,
and that one is a CPAD member** and so is excluded from the confirmatory statistic on a
separate ground. All four rows in the benchmark's scarce cell have no structure at all.
*(The 19 Nov version of this file said "not one of thirteen". The Orb2 row's flag was
`null` while its own recorded arithmetic put it below the bar; it is now `true`. The
paragraph sent to Bradshaw contains no number that this changes.)* §10b recruits deposited fibril cores,
which are long regions in short chains, and cannot produce a benchmark row. The scarce
cell holds **4 rows across 2 proteins** — both of them his — and §4 needs **5 proteins**.
A literature screen of five queries on 19 Nov returned **zero candidates**, and the reason
looks structural: two of the four registered search branches (alanine scan, peptide array)
are used almost exclusively on short peptides already known to aggregate, which leaves
deletion and truncation mapping in cells — a literature his group largely *is*.

**What he can do that a search cannot.** Name proteins. He has spent a decade doing this
exact experiment and will know in one sentence what weeks of querying will not find.

**And a "not really" is a result, not a failure.** It would mean the benchmark cannot reach
*n* = 5 proteins under the registered rule — a fact about the field, reportable as one.

---

## The paragraph

> **One last thing, and it is the question I would most value your view on.** I am trying
> to widen this benchmark beyond DISC1 and TRIOBP-1, and I keep coming back to the fact
> that what makes your two regions usable is quite rare: a *short* region shown
> *necessary* for aggregation inside a *large* protein. The rank statistic I use needs
> that geometry — the mapped region has to be a small fraction of the chain, roughly 5% or
> less, or no rank-based test can return a significant result for it no matter which
> predictor is used. Cryo-EM fibril cores, which is where most new "mapped regions" come
> from now, almost always fail that: the ordered core is a large fraction of a short
> construct. Your 25-mer in a 652-residue protein, and the ~30 residues in DISC1, are
> close to ideal and I have not found many others.
>
> **So: are there other proteins — in your work, in the Korth lab's, or anyone's — where a
> short region of a large protein has been shown necessary for aggregation by deletion or
> truncation, the way 384-414 and 324-348 were?** I am not restricting this to psychiatric
> proteins; any protein would do. CRMP1 and dysbindin are the obvious places I looked, but
> as far as I can tell both were identified as aggregating without a region ever being
> narrowed down, so they give me a protein rather than a region.
>
> **If the answer is "not really, there aren't many", that is genuinely useful to me and I
> would rather hear it than keep searching.** It would mean this type of mapping is rare
> enough to be worth saying so in print, which is itself a point about how the field
> measures aggregation.

---

## Optional second paragraph, if the 2014 paper is to be acknowledged

Include this only if the author wants to signal that the PDF was read. It is accurate and
checked, but it lengthens the message.

> Thank you also for the 2014 PLoS ONE paper — it answered something the 2017 paper left
> implicit. I had the TRIOBP-1 entry flagged with a note that the predictor runs behind
> "in our previous analyses" must live in reference 8, and they do, with the thresholds
> stated. It is a useful detail for me that the four servers you used — AGGRESCAN,
> FoldAmyloid, ProA and TANGO — are exactly the four I had frozen as my "legacy" predictor
> set before I read it, so the comparison is tighter than I had any right to expect. The
> ordering also turns out to matter in my favour: predictions came *first*, in 2014, and
> pointed somewhere else, which is a cleaner basis for calling 324-348 a genuine predictor
> miss than if nothing had been run at all.

---

## Notes for the author before sending

- **The arithmetic claim in the paragraph is checkable and correct**: `power_eligible` iff
  *m*/*M* ≤ 0.05 (PREREGISTRATION §3.1b), which at *W* = 6 is approximately *region length
  / chain length* ≤ 5%. TRIOBP-1 324-348 is 0.0370 and DISC1 384-414 is 0.0352.
- **Do not name CRMP1 and dysbindin as failures of his lab's work.** The paragraph says
  only that no *region* was narrowed, which is what the literature shows and is a neutral
  statement about scope. If he knows otherwise, that is exactly the answer being asked for.
- **"any protein would do" is deliberate.** `CLAUDE.md` names widening beyond the
  psychiatric proteins as the outstanding task, and narrowing the question to psychiatry
  would throw away most of the possible answers.
- **Do not promise him co-authorship or a role in the benchmark** in exchange for names.
  He has already offered to check the two records; that is the standing ask.
