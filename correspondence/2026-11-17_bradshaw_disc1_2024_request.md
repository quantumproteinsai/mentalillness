# Draft email: Zaharija & Bradshaw 2024, and a figure legend discrepancy

**Status: SENT, 17 Nov 2026**, by the author, to the corresponding author of both papers.
Awaiting reply. The text below is the record of what was asked.

**Nothing is blocked on this reply.** The DISC1 384-415 row is already citable under the
16 Nov amendment, and its range already rests on the 2025 thesis plasmid names. This is a
re-check that could strengthen the row or trigger a dated amendment, not a gap in it.

**To:** `nicholas.b@biotech.uniri.hr`
*(corresponding author on Zaharija et al. 2022 IJMS 23:11048 and on the 2024 paper)*

**Cc (optional):** `ckorth@hhu.de` — Carsten Korth, co-corresponding on the 2022 paper.
Probably unnecessary for this question.

**Subject:** DISC1 384-415 boundary in Zaharija & Bradshaw 2024 — and a figure legend query

---

Dear Dr Bradshaw,

I am building a small, hand-curated benchmark of aggregation predictors against
experimentally mapped aggregation-critical regions, and two of its rows are your
TRIOBP-1 324-348 and DISC1 384-415. Every row is read from its primary source rather
than imported from a database, so I have two questions that only you can settle quickly.

**1. The DISC1 boundary.** I have been unable to obtain the version of record of
Zaharija & Bradshaw (2024) *Prog Neuropsychopharmacol Biol Psychiatry* **130**:110923.
It appears in no open repository, and Europe PMC lists no full text. If you are able to
send a copy I would be grateful.

The specific thing I need is one detail, and **you may be able to answer it in a sentence
without sending anything**: does the published version write the deletion construct as
**Δ384-414 or Δ384-415**? The bioRxiv version writes Δ384-414 three times in the body text
while Figure 5A and panels D-F label it Δ384-415, and the same sentence says "these 32
amino acids", which fits 384-415. I have recorded the region as **384-415**, on the
strength of the plasmid names in Beti Zaharija's 2025 thesis (Table 11:
`DISC1 (delta-384-415)` and two others). I would rather cite your published boundary than
infer it.

**2. A discrepancy I should flag, in case it is useful.** In Zaharija et al. 2022
(*IJMS* **23**:11048), the Figure 6 legend reads *"(B) N-terminal deletions of TRIOBP-1
demonstrate AA 324-328 to be essential for aggregation"*. Panel B itself shows 324-652
aggregating and 349-652 not, which isolates **324-348**, and the Introduction describes
the same 25 amino acid loop. Panel D then narrows the critical region to 333-340, which
lies outside 324-328. I take "324-328" to be a typographic slip for "324-348". I mention
it only because the sentence is easy to quote out of context — I nearly carried it into
my dataset as a separate region before checking it against the panel.

Thank you for making the TRIOBP-1 and DISC1 mapping so precisely specified; the construct
tables in both papers are the reason these rows could be used at all. The dataset is
openly deposited (doi:10.5281/zenodo.24306057, CC BY) and I would be glad to hear if
anything in the TRIOBP-1 or DISC1 entries looks wrong to you.

With best regards,

Bertrand Mercier des Rochettes
ORCID 0000-0002-1145-1881
contact@quantum-proteins.ai

---

## If a reply arrives

- **If the boundary is confirmed as 384-415:** record it on the DISC1 384-415 row, and
  §12 step 1's last open item closes. The row's range does not change.
- **If it is 384-414:** that is an amendment under §12 — made *after* scores were seen,
  so it is reported as such. It would change `residues`, the stored 32-residue sequence,
  and the row's *v* under §3.1. **Both arms would need rescoring on that row.**
- **If the version of record arrives:** set `source_version` to `version_of_record` and
  `verified_against_publisher_pdf` accordingly. Note that the row is *already* citable
  under the 16 Nov amendment, so this is a strengthening, not an unblocking.
- **If no reply:** nothing breaks. The row stays as it is, cited to the preprint with the
  version of record named as unobtainable.
