# Draft: second message to Bradshaw — 20 Nov 2026

**Status: DRAFT, NOT SENT.** Assembled by Claude at the author's request, from the pending
route (b) question plus two loop-closings.

## Why sending one day after the last message is appropriate here

**It is not a follow-up chase.** The 19 Nov message answered *his* reply and promised two
things. Both can now be delivered:

1. He corrected DISC1 to **384-414**, and we told him the deposited v1.4.0 still carried
   384-415 and that the corrected value would go into the next version. **v1.5.0 is now
   deposited and carries it.**
2. He spotted that the DOI we quoted does not resolve. **That is now diagnosed and
   reported to Zenodo**, and he should hear the outcome from us rather than wonder.

Reporting back on things a correspondent raised is the opposite of pestering. The two
questions ride along at the end and are explicitly marked as optional.

**Verified immediately before drafting, 20 Nov 2026:**

| | |
|---|---|
| `10.5281/zenodo.24394773` (v1.5.0) | **302 → zenodo.org**, resolves |
| `10.5281/zenodo.24342313` (v1.4.0) | **404 at doi.org**, still unregistered at DataCite |

**Nothing sent to him on 19 Nov requires retraction.** Checked: the extract carries no
claim touched by the §10d withdrawal, and its three substantive TRIOBP-1 statements were
independently re-confirmed against the Bradshaw 2017 publisher PDF today — the region is
"essential but not in itself sufficient", it was found by truncation and not by prediction,
and the four legacy predictors are discordant on it. Item 2.9's 48.0% recomputes exactly
from `PLRENKRVPLTALLNQSRGERRGPP` (4 Pro + 8 charged of 25).

---

## The message

**To:** `nicholas.b@biotech.uniri.hr`
**Cc:** `beti.zaharija@biotech.uniri.hr`
**Subject:** Re: DISC1 384-415 boundary in Zaharija & Bradshaw 2024 — and a figure legend query

---

Dear Nick,

Two quick things that close the loops from last time, and then two questions you should
feel free to ignore.

**1. Your correction is deposited.** The dataset version carrying DISC1 **384-414** is now
public, and the boundary is cited to your sequencing as a personal communication rather
than to any printed number:

> https://doi.org/10.5281/zenodo.24394773

That supersedes the version I pointed you at, which recorded 384-415. If you or Beti look
at this row, that is the one to look at.

**2. The DOI you spotted was a real bug, and it is with Zenodo.** You were right that it
did not resolve. The diagnosis is that the record is live and complete at Zenodo but its
version DOI was never registered with DataCite — `doi.org` returns 404 and the handle API
reports the handle as not found, while the concept DOI resolves normally. The version
immediately before it was minted the same day from the same account and registered
correctly, so it appears to be a one-off rather than anything I did. I reported it to
Zenodo support on 20 November; they quote three to four weeks. The new version above
resolves correctly, and I have corrected my README to stop citing the broken one. Thank
you for catching it — it would have gone into a paper otherwise.

**3. A question I would value your view on, and a "not really" is a genuinely useful
answer.** I am trying to widen this benchmark beyond DISC1 and TRIOBP-1, and what makes
your two regions usable turns out to be rare: a *short* region shown *necessary* for
aggregation inside a *large* protein. The rank statistic I use needs that geometry — the
mapped region has to be roughly 5% of the chain or less, or no rank-based test can return a
significant result for it whatever the predictor. I have now measured how rare that is on
an independently curated set of 82 deposited fibril cores from 69 proteins: about one in
eight clears the geometry, and only one of the eighty-two also survives a training-set
check. Your 25-mer in a 652-residue protein, and the ~30 residues in DISC1, are close to
ideal and I have not found many others.

So: **are there other proteins — in your work, the Korth lab's, or anyone's — where a short
region of a large protein has been shown necessary for aggregation by deletion or
truncation, the way 384-414 and 324-348 were?** Not restricted to psychiatric proteins; any
protein would do. CRMP1 and dysbindin were the obvious places I looked, but as far as I can
tell both were identified as aggregating without a region ever being narrowed, so they give
me a protein rather than a region. If the answer is "there aren't many", that is itself
worth saying in print, and I would rather hear it than keep searching.

**4. A much smaller question.** Has TRIOBP-1 aggregation ever been probed with an amyloid
dye — thioflavin T or S, Congo red — or with a conformation-specific antibody such as A11
or OC? I ask because every tool I am benchmarking was trained on amyloid-forming peptides,
and I have been reading Trossbach et al. 2016, where the DISC1 aggregates in the transgenic
rat come out ThS-, ThT- and A11-negative. If TRIOBP-1 aggregates are likewise not amyloid
in the strict sense, I think that *strengthens* the point your 2017 paper makes rather than
weakening it: the predictors would have been missing 324-348 partly because they were being
asked about the wrong physical object, which is a more interesting reason than simply
getting it wrong. I would want to describe the benchmark accordingly, and I would rather
ask you than infer it from the absence of the experiment in the literature.

With thanks again — the boundary correction was the single most useful thing anyone has
told me on this project.

Bertrand

---

## Notes for the author before sending

- **Do not add a third question.** Two is already the limit of what one message should ask
  of someone who answered the last one inside two days.
- **Do not quote the "zero candidates" figure** from the 19 Nov route (b) draft. It was
  obtained by screening per-protein where eligibility is per-region, and it is wrong. The
  measured figures above replace it.
- **If he answers the dye question with "nobody has looked"**, that is a result and belongs
  in `STATE.md` as a recorded absence of measurement, not as a negative.
- **If he names proteins**, every one still has to clear §3.1b and §5.2b before it is a row.
  A name is a candidate, not an admission.
