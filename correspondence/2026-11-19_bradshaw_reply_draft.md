# Draft reply: Bradshaw, 19 Nov 2026

**Status: DRAFT, NOT SENT.** Written by Claude for the author to send, amend or discard.

**What his reply settled, and the one thing it overturned.** The DISC1 deletion is
**384-414**, from sequencing of the actual vectors. This project had recorded **384-415**
and had reasoned backwards: the preprint body text writes Δ384-414 three times and *was
right*, while the thesis Table 11 plasmid names and the Figure 5 labels — which we
preferred — are transcriptions. `data/regions.json` is corrected. Under the registered
statistic **no computed number moves**, which PREREGISTRATION 12.1a predicted in advance
on 18 Nov; see `boundary_corrected_2026_11_19` on the row.

**He also raised a real defect in our deposit:** the DOI quoted to him is a superseded
version DOI, and the *current* version DOI `10.5281/zenodo.24342313` is live at Zenodo but
**not registered at DataCite** — `doi.org` returns 404 and the handle API returns
`responseCode 100` (handle not found). The concept DOI resolves correctly. Checked
19 Nov 2026. `README.md` cites the unresolvable one and is corrected in the same commit.

**To:** `nicholas.b@biotech.uniri.hr`
**Cc:** `beti.zaharija@biotech.uniri.hr` *(he added her; keep her on it)*

**Subject:** Re: DISC1 384-415 boundary in Zaharija & Bradshaw 2024 — and a figure legend query

---

Dear Nick,

Thank you — that is exactly the answer I needed, and it corrected me rather than
confirming me, which is more useful.

**1. DISC1 384-414.** I had recorded 384-415 and I had it backwards. The preprint's body
text writes Δ384-414 three times and I treated that as the typo, preferring the Figure 5
labels and the plasmid names in Beti's thesis Table 11 (`DISC1 (delta-384-415)` and two
others). Your sequencing agrees with the body text, so the figure labels and the plasmid
names are the transcription errors, and the "these 32 amino acids" in the same sentence is
one out as well. My dataset now reads 384-414, 31 residues, cited to your sequencing as a
personal communication rather than to a printed number.

One detail that may be worth a line in any future paper: under the rank statistic I use,
the two readings are indistinguishable. The statistic tiles the 854-residue chain in
non-overlapping 6-residue windows, so the windows lying wholly inside the region are the
same five under either boundary — residue 415 falls in no scored window. Every number I
report is identical either way. I had registered that invariance before writing to you,
precisely so the answer could not be used selectively.

**2. TRIOBP-1 324-328 → 324-348.** Thank you for confirming the figure legend slip. I have
recorded your confirmation against that entry, which I keep as a flagged duplicate rather
than deleting, so that anyone who quotes the legend out of context finds the correction
attached to it.

**3. The DOI — my fault, and partly Zenodo's.** Two separate problems, both real:

- I quoted `10.5281/zenodo.24306057`, which is the **version DOI for v1.1.0**, now
  superseded. It does resolve, but it lands you on an old version with fewer records, so
  it was the wrong thing to send you.
- The version DOI for the current release, `10.5281/zenodo.24342313`, is **not resolving**.
  The record is published at Zenodo but the DOI has not been registered with DataCite, so
  `doi.org` returns "not found". I am taking that up with Zenodo and correcting my own
  README, which cites it.

Please use the **concept DOI**, which is stable and always resolves to the current version:

> <https://doi.org/10.5281/zenodo.24290697>

or the direct link <https://zenodo.org/records/24342313>. Current version is v1.4.0,
CC BY 4.0, 24 regions across 14 proteins.

**4. Your offer to check the records — yes, please, and let me make it small.** Rather than
asking you and Beti to read a whole dataset, I will send a one-page extract of just the two
entries, with each claim tagged so you can mark it right or wrong without hunting. The
specific things I would most like checked are the ones where I have made an
*interpretation* rather than copied a number:

- **DISC1, necessity vs sufficiency.** I have recorded 384-414 as *necessary* — deletion
  abolishes aggregation in 1-854, 1-836 and 1-655 — but **not** as demonstrated sufficient,
  on the grounds that 384-414 was never expressed alone; what was expressed alone is the
  whole linker 384-538 and the fragment 1-415. The Discussion's "both sufficient for
  aggregation" reads stronger than that to me. Have I drawn that line where you would?
- **TRIOBP-1, which construct the 25-mer is necessary in.** I have it as necessary in the
  truncation series and in 190-652 Δ324-348, with 333-652 aggregating indistinguishably
  from 324-652 — so 324-332 dispensable in that construct, and 333-340 the narrowed core.
  I record the first cluster of charged residues as *not* required, per your 2017 text.
- **Frames.** DISC1 854 aa, and I have checked that RefSeq NP_061132.2 and UniProt Q9NRI5
  are byte-identical, so Beti's thesis numbers transfer with no offset. TRIOBP-1 in the
  652-residue frame of NP_008963.3, i.e. +59 on the 593-residue variant. Confirming those
  two frames would close the last numbering risk in both rows.

One last small thing, offered only because you found the last one useful: Figure 48's
caption in Beti's thesis gives "AA 383-415", a third variant of the same boundary. With
your sequencing in hand all three printed forms are now resolvable, but it may be worth
knowing where they are if the construct is described again.

Thank you both — the construct tables in the 2017 and 2022 papers are the reason these two
rows are usable at all, and a sequenced boundary is a better provenance than anything I
could have reconstructed from the literature.

With best regards,

Bertrand Mercier des Rochettes
ORCID 0000-0002-1145-1881
contact@quantum-proteins.ai

---

## Notes for the author before sending

- **The sufficiency question in item 4 is the one worth his time.** It is the only place
  where the dataset records something the paper's Discussion states more strongly, and it
  is an interpretation of ours that a reviewer could challenge. If he disagrees, the
  `construct` column changes.
- **Do not promise a deposit update date.** The DataCite registration is not in our
  control.
- **The extract promised in item 4 does not exist yet.** Either build it before sending, or
  soften to "I will send". It is two rows; `scripts/build_release.py` can filter.
- The Venko 2024 consensus places predictor-flagged regions at 388-394, 400-406 and
  403-411, all strictly inside this row. That is recorded in
  `data/references_to_check.json` and cuts against the "predictors miss it" framing for
  DISC1 specifically. **Not raised here**, because it is our analysis problem, not his
  boundary question — but he will find it if he reads the dataset, so it should not come
  as a surprise from us later.
